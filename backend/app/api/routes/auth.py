from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException, Request

from app.models.schemas import Envelope, LoginRequest, VerifyOtpRequest

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Envelope)
async def login(payload: LoginRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    user = repo.find_user_by_phone(payload.phone, payload.role)
    if not user:
        raise HTTPException(status_code=404, detail="User not found for the selected role")
    return Envelope(
        message="OTP generated successfully",
        data={
            "otp": "123456",
            "expiresAt": datetime.now(UTC).isoformat(),
            "user": user.model_dump(by_alias=True),
        },
    )


@router.post("/verify-otp", response_model=Envelope)
async def verify_otp(payload: VerifyOtpRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    user = repo.find_user_by_phone(payload.phone)
    if not user or payload.otp != "123456":
        raise HTTPException(status_code=401, detail="Invalid OTP")
    return Envelope(
        message="Login successful",
        data={
            "token": f"rakshakai-demo-token-{user.id}",
            "user": user.model_dump(by_alias=True),
        },
    )


@router.post("/logout", response_model=Envelope)
async def logout() -> Envelope:
    return Envelope(message="Logged out successfully", data={"loggedOut": True})

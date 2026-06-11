from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException, Request

from app.models.schemas import Envelope, NotificationRecord, WellnessCheckInRequest, WellnessLog

router = APIRouter(prefix="/wellness", tags=["wellness"])


@router.post("/checkin", response_model=Envelope)
async def checkin(payload: WellnessCheckInRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    sio = request.app.state.sio
    user = repo.get_user(payload.userId)
    if not user:
        raise HTTPException(status_code=404, detail="Senior citizen not found")

    log = WellnessLog(
        logId=repo.generate_id("wlg"),
        userId=payload.userId,
        healthStatus=payload.healthStatus,
        safetyStatus=payload.safetyStatus,
        needsHelp=payload.needsHelp,
        timestamp=datetime.now(UTC),
    )
    repo.create_wellness_log(log)
    profile = repo.get_senior_profile(payload.userId)

    if payload.needsHelp:
        for recipient in repo.list_family_members() + repo.list_police_users():
            repo.create_notification(
                NotificationRecord(
                    notificationId=repo.generate_id("ntf"),
                    recipientId=recipient.id,
                    type="WELLNESS_ALERT",
                    message=f"{user.name} marked a wellness check-in as needing help.",
                )
            )
        await sio.emit("wellness:risk_flag", {"userId": user.id, "name": user.name, "riskScore": profile.riskScore if profile else 0, "needsHelp": True})

    return Envelope(message="Wellness check-in saved", data={"log": log.model_dump(), "riskScore": profile.riskScore if profile else 0})


@router.get("/history", response_model=Envelope)
async def history(userId: str | None = None, request: Request = None) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Wellness history fetched", data=[item.model_dump() for item in repo.list_wellness_logs(userId)])


@router.get("/risk-score", response_model=Envelope)
async def risk_score(userId: str, request: Request) -> Envelope:
    repo = request.app.state.repository
    profile = repo.get_senior_profile(userId)
    if not profile:
        raise HTTPException(status_code=404, detail="Senior profile not found")
    return Envelope(message="Risk score fetched", data={"userId": userId, "riskScore": profile.riskScore})

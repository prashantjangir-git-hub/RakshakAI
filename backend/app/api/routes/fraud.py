from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException, Request

from app.models.schemas import Envelope, FraudAnalyzeRequest, FraudReport, FraudReportCreateRequest, NotificationRecord
from app.services.scam_detector import analyze_message

router = APIRouter(prefix="/fraud", tags=["fraud"])


@router.post("/analyze", response_model=Envelope)
async def analyze_fraud(payload: FraudAnalyzeRequest) -> Envelope:
    result = analyze_message(payload.messageText, payload.imageBase64)
    return Envelope(message="Fraud analysis completed", data=result.model_dump())


@router.post("/report", response_model=Envelope)
async def create_report(payload: FraudReportCreateRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    sio = request.app.state.sio
    user = repo.get_user(payload.userId)
    if not user:
        raise HTTPException(status_code=404, detail="Senior citizen not found")

    analysis = analyze_message(payload.messageText, payload.imageBase64)
    report = FraudReport(
        reportId=repo.generate_id("frd"),
        userId=payload.userId,
        messageText=payload.messageText,
        imageUrl=payload.imageUrl,
        extractedText=payload.extractedText or analysis.extractedText,
        riskScore=payload.riskScore or analysis.riskScore,
        classification=payload.classification or analysis.classification,
        aiExplanation=payload.aiExplanation or analysis.aiExplanation,
        recommendedAction=payload.recommendedAction or analysis.recommendedAction,
        createdAt=datetime.now(UTC),
    )
    repo.create_report(report)

    for officer in repo.list_police_users():
        repo.create_notification(
            NotificationRecord(
                notificationId=repo.generate_id("ntf"),
                recipientId=officer.id,
                type="FRAUD_REPORT",
                message=f"High-priority fraud report submitted by {user.name}.",
            )
        )

    await sio.emit("fraud:new_report", repo.export_dashboard_reports()[0])
    return Envelope(message="Fraud report created", data=report.model_dump())


@router.get("/history", response_model=Envelope)
async def fraud_history(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Fraud history fetched", data=repo.export_dashboard_reports())


@router.get("/report/{report_id}", response_model=Envelope)
async def get_report(report_id: str, request: Request) -> Envelope:
    repo = request.app.state.repository
    report = repo.get_report(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Fraud report not found")
    return Envelope(message="Fraud report fetched", data=report.model_dump())

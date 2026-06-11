from __future__ import annotations

from fastapi import APIRouter, Request

from app.models.schemas import Envelope, NotificationRecord, NotificationRequest

router = APIRouter(prefix="/notification", tags=["notification"])


@router.post("/send", response_model=Envelope)
async def send_notification(payload: NotificationRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    notification = NotificationRecord(
        notificationId=repo.generate_id("ntf"),
        recipientId=payload.recipientId,
        type=payload.type,
        message=payload.message,
    )
    repo.create_notification(notification)
    return Envelope(message="Notification sent", data=notification.model_dump())


@router.get("/list", response_model=Envelope)
async def notification_list(recipientId: str | None = None, request: Request = None) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Notifications fetched", data=[item.model_dump() for item in repo.list_notifications(recipientId)])

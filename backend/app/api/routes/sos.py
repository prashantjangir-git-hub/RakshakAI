from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException, Request

from app.models.schemas import Envelope, NotificationRecord, SosCreateRequest, SosIncident, SosStatusUpdateRequest

router = APIRouter(prefix="/sos", tags=["sos"])


@router.post("/create", response_model=Envelope)
async def create_sos(payload: SosCreateRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    sio = request.app.state.sio
    user = repo.get_user(payload.userId)
    if not user:
        raise HTTPException(status_code=404, detail="Senior citizen not found")

    incident = SosIncident(
        incidentId=repo.generate_id("sos"),
        userId=payload.userId,
        latitude=payload.latitude,
        longitude=payload.longitude,
        triggerMethod=payload.triggerMethod,
        createdAt=datetime.now(UTC),
    )
    repo.create_incident(incident)

    recipients = repo.list_family_members() + repo.list_police_users()
    for recipient in recipients:
        repo.create_notification(
            NotificationRecord(
                notificationId=repo.generate_id("ntf"),
                recipientId=recipient.id,
                type="SOS_ALERT",
                message=f"{user.name} triggered an SOS using {payload.triggerMethod.value.lower()} mode.",
            )
        )

    await sio.emit("sos:new", repo.export_dashboard_incidents()[0])
    return Envelope(message="SOS created successfully", data=incident.model_dump())


@router.get("/history", response_model=Envelope)
async def sos_history(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="SOS history fetched", data=[item.model_dump() for item in repo.list_incidents()])


@router.get("/live", response_model=Envelope)
async def sos_live(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Live incidents fetched", data=repo.export_dashboard_incidents())


@router.put("/update-status", response_model=Envelope)
async def update_status(payload: SosStatusUpdateRequest, request: Request) -> Envelope:
    repo = request.app.state.repository
    sio = request.app.state.sio
    incident = repo.update_incident_status(payload.incidentId, payload.status)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    for row in repo.export_dashboard_incidents():
        if row["incidentId"] == payload.incidentId:
            await sio.emit("sos:updated", row)
            return Envelope(message="Incident status updated", data=row)
    raise HTTPException(status_code=404, detail="Incident not found after update")

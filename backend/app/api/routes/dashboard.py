from __future__ import annotations

from fastapi import APIRouter, Request

from app.models.schemas import Envelope

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary", response_model=Envelope)
async def summary(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Dashboard summary fetched", data=repo.build_dashboard_summary())


@router.get("/incidents", response_model=Envelope)
async def incidents(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Dashboard incidents fetched", data=repo.export_dashboard_incidents())


@router.get("/fraud-reports", response_model=Envelope)
async def fraud_reports(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Dashboard fraud reports fetched", data=repo.export_dashboard_reports())


@router.get("/heatmap", response_model=Envelope)
async def heatmap(request: Request) -> Envelope:
    repo = request.app.state.repository
    return Envelope(message="Dashboard heatmap fetched", data=repo.build_heatmap())

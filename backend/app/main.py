from __future__ import annotations

import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, dashboard, fraud, notification, sos, wellness
from app.database.repository import InMemoryRepository
from app.models.schemas import Envelope

api_app = FastAPI(title="RakshakAI Backend", version="1.0.0")
api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
api_app.state.repository = InMemoryRepository()
api_app.state.sio = sio

api_app.include_router(auth.router, prefix="/api/v1")
api_app.include_router(sos.router, prefix="/api/v1")
api_app.include_router(fraud.router, prefix="/api/v1")
api_app.include_router(wellness.router, prefix="/api/v1")
api_app.include_router(notification.router, prefix="/api/v1")
api_app.include_router(dashboard.router, prefix="/api/v1")


@api_app.get("/", response_model=Envelope)
async def root() -> Envelope:
    return Envelope(message="RakshakAI backend is running", data={"service": "backend", "status": "ok"})


@api_app.get("/health", response_model=Envelope)
async def health() -> Envelope:
    return Envelope(message="Health check successful", data={"status": "healthy"})


app = socketio.ASGIApp(sio, other_asgi_app=api_app)

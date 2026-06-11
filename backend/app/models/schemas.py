from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class Role(str, Enum):
    senior = "senior"
    family = "family"
    police = "police"


class FraudClassification(str, Enum):
    SAFE = "SAFE"
    SUSPICIOUS = "SUSPICIOUS"
    SCAM = "SCAM"


class IncidentStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"


class TriggerMethod(str, Enum):
    BUTTON = "BUTTON"
    VOICE = "VOICE"


class HealthStatus(str, Enum):
    HEALTHY = "HEALTHY"
    NEED_HELP = "NEED_HELP"


class SafetyStatus(str, Enum):
    SAFE = "SAFE"
    NEED_HELP = "NEED_HELP"


class Envelope(BaseModel):
    success: bool = True
    message: str
    data: Any


class EmergencyContact(BaseModel):
    name: str
    phone: str
    relation: str


class User(BaseModel):
    id: str = Field(alias="_id")
    role: Role
    name: str
    phone: str
    email: Optional[str] = None
    language: str = "English"
    address: str = ""
    emergencyContacts: list[EmergencyContact] = Field(default_factory=list)
    createdAt: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"populate_by_name": True}


class SeniorProfile(BaseModel):
    userId: str
    medicalConditions: list[str] = Field(default_factory=list)
    medications: list[str] = Field(default_factory=list)
    riskScore: int = 24
    lastCheckIn: datetime = Field(default_factory=datetime.utcnow)
    location: dict[str, float] = Field(default_factory=dict)


class SosIncident(BaseModel):
    incidentId: str
    userId: str
    latitude: float
    longitude: float
    status: IncidentStatus = IncidentStatus.OPEN
    triggerMethod: TriggerMethod
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class FraudReport(BaseModel):
    reportId: str
    userId: str
    messageText: str = ""
    imageUrl: Optional[str] = None
    extractedText: Optional[str] = None
    riskScore: int
    classification: FraudClassification
    aiExplanation: str
    recommendedAction: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class WellnessLog(BaseModel):
    logId: str
    userId: str
    healthStatus: HealthStatus
    safetyStatus: SafetyStatus
    needsHelp: bool
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class NotificationRecord(BaseModel):
    notificationId: str
    recipientId: str
    type: str
    message: str
    readStatus: bool = False
    createdAt: datetime = Field(default_factory=datetime.utcnow)


class LoginRequest(BaseModel):
    phone: str
    role: Role


class VerifyOtpRequest(BaseModel):
    phone: str
    otp: str


class SosCreateRequest(BaseModel):
    userId: str
    latitude: float
    longitude: float
    triggerMethod: TriggerMethod


class SosStatusUpdateRequest(BaseModel):
    incidentId: str
    status: IncidentStatus


class FraudAnalyzeRequest(BaseModel):
    messageText: str = ""
    imageBase64: Optional[str] = None


class FraudAnalyzeResult(BaseModel):
    extractedText: Optional[str] = None
    riskScore: int
    classification: FraudClassification
    aiExplanation: str
    recommendedAction: str


class FraudReportCreateRequest(BaseModel):
    userId: str
    messageText: str = ""
    imageUrl: Optional[str] = None
    imageBase64: Optional[str] = None
    riskScore: Optional[int] = None
    classification: Optional[FraudClassification] = None
    aiExplanation: Optional[str] = None
    recommendedAction: Optional[str] = None
    extractedText: Optional[str] = None


class WellnessCheckInRequest(BaseModel):
    userId: str
    healthStatus: HealthStatus
    safetyStatus: SafetyStatus
    needsHelp: bool


class NotificationRequest(BaseModel):
    recipientId: str
    type: str
    message: str

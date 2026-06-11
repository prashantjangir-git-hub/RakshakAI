from __future__ import annotations

from datetime import UTC, datetime, timedelta

from app.models.schemas import (
    EmergencyContact,
    FraudClassification,
    FraudReport,
    HealthStatus,
    IncidentStatus,
    NotificationRecord,
    Role,
    SafetyStatus,
    SeniorProfile,
    SosIncident,
    TriggerMethod,
    User,
    WellnessLog,
)


def create_seed_data() -> dict[str, list]:
    now = datetime.now(UTC)
    senior = User(
        _id="usr_senior_1",
        role=Role.senior,
        name="Savitri Devi",
        phone="9876543210",
        email="savitri@example.com",
        address="Ahmedabad, Gujarat",
        emergencyContacts=[
            EmergencyContact(name="Neha Sharma", phone="9123456780", relation="Daughter"),
            EmergencyContact(name="Ramesh Sharma", phone="9012345678", relation="Son"),
        ],
    )
    family = User(
        _id="usr_family_1",
        role=Role.family,
        name="Neha Sharma",
        phone="9123456780",
        email="neha@example.com",
        address="Ahmedabad, Gujarat",
    )
    police = User(
        _id="usr_police_1",
        role=Role.police,
        name="Inspector Arjun Rana",
        phone="9000000001",
        email="arjun.rana@police.local",
        address="City Control Room",
    )

    incidents = [
        SosIncident(
            incidentId="sos_1001",
            userId=senior.id,
            latitude=23.0225,
            longitude=72.5714,
            status=IncidentStatus.IN_PROGRESS,
            triggerMethod=TriggerMethod.BUTTON,
            createdAt=now - timedelta(minutes=14),
        ),
        SosIncident(
            incidentId="sos_1002",
            userId=senior.id,
            latitude=23.0350,
            longitude=72.5530,
            status=IncidentStatus.OPEN,
            triggerMethod=TriggerMethod.VOICE,
            createdAt=now - timedelta(minutes=4),
        ),
    ]

    reports = [
        FraudReport(
            reportId="frd_2001",
            userId=senior.id,
            messageText="Your bank KYC is blocked. Click the secure link now to avoid account suspension.",
            riskScore=91,
            classification=FraudClassification.SCAM,
            aiExplanation="The message creates urgency, pretends to be from a bank, and asks you to click a link. These are common scam patterns.",
            recommendedAction="Do not click the link. Contact your bank using the number on your official passbook or card.",
            extractedText="Your bank KYC is blocked. Click the secure link now to avoid account suspension.",
            createdAt=now - timedelta(hours=3),
        ),
        FraudReport(
            reportId="frd_2002",
            userId=senior.id,
            messageText="You have won a festival prize of Rs 50,000. Share your OTP to claim it.",
            riskScore=96,
            classification=FraudClassification.SCAM,
            aiExplanation="Prize scams often ask for OTP or payment details. Real organizations do not ask for OTP to release rewards.",
            recommendedAction="Delete the message and never share OTP or bank details.",
            createdAt=now - timedelta(days=1),
        ),
    ]

    wellness_logs = [
        WellnessLog(
            logId="wlg_3001",
            userId=senior.id,
            healthStatus=HealthStatus.HEALTHY,
            safetyStatus=SafetyStatus.SAFE,
            needsHelp=False,
            timestamp=now - timedelta(hours=7),
        ),
        WellnessLog(
            logId="wlg_3002",
            userId=senior.id,
            healthStatus=HealthStatus.NEED_HELP,
            safetyStatus=SafetyStatus.SAFE,
            needsHelp=True,
            timestamp=now - timedelta(days=1, hours=2),
        ),
    ]

    notifications = [
        NotificationRecord(
            notificationId="ntf_4001",
            recipientId=family.id,
            type="SOS_ALERT",
            message="Savitri Devi triggered an SOS. Live response is active.",
            createdAt=now - timedelta(minutes=4),
        ),
        NotificationRecord(
            notificationId="ntf_4002",
            recipientId=police.id,
            type="FRAUD_REPORT",
            message="A high-risk scam report was submitted for review.",
            createdAt=now - timedelta(hours=3),
        ),
    ]

    profiles = [
        SeniorProfile(
            userId=senior.id,
            medicalConditions=["Hypertension"],
            medications=["Amlodipine"],
            riskScore=68,
            lastCheckIn=now - timedelta(hours=7),
            location={"latitude": 23.0225, "longitude": 72.5714},
        )
    ]

    return {
        "users": [senior, family, police],
        "senior_profiles": profiles,
        "sos_incidents": incidents,
        "fraud_reports": reports,
        "wellness_logs": wellness_logs,
        "notifications": notifications,
    }

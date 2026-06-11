from __future__ import annotations

from collections import defaultdict
from typing import Optional
from uuid import uuid4

from app.database.seed import create_seed_data
from app.models.schemas import (
    FraudReport,
    IncidentStatus,
    NotificationRecord,
    Role,
    SeniorProfile,
    SosIncident,
    User,
    WellnessLog,
)


class InMemoryRepository:
    def __init__(self) -> None:
        seed = create_seed_data()
        self.users: list[User] = seed["users"]
        self.senior_profiles: list[SeniorProfile] = seed["senior_profiles"]
        self.sos_incidents: list[SosIncident] = seed["sos_incidents"]
        self.fraud_reports: list[FraudReport] = seed["fraud_reports"]
        self.wellness_logs: list[WellnessLog] = seed["wellness_logs"]
        self.notifications: list[NotificationRecord] = seed["notifications"]

    def generate_id(self, prefix: str) -> str:
        return f"{prefix}_{uuid4().hex[:8]}"

    def find_user_by_phone(self, phone: str, role: Optional[Role] = None) -> Optional[User]:
        for user in self.users:
            if user.phone == phone and (role is None or user.role == role):
                return user
        return None

    def get_user(self, user_id: str) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def list_family_members(self) -> list[User]:
        return [user for user in self.users if user.role == Role.family]

    def list_police_users(self) -> list[User]:
        return [user for user in self.users if user.role == Role.police]

    def create_incident(self, incident: SosIncident) -> SosIncident:
        self.sos_incidents.insert(0, incident)
        return incident

    def list_incidents(self) -> list[SosIncident]:
        return sorted(self.sos_incidents, key=lambda item: item.createdAt, reverse=True)

    def update_incident_status(self, incident_id: str, status: IncidentStatus) -> Optional[SosIncident]:
        for incident in self.sos_incidents:
            if incident.incidentId == incident_id:
                incident.status = status
                return incident
        return None

    def create_report(self, report: FraudReport) -> FraudReport:
        self.fraud_reports.insert(0, report)
        return report

    def list_reports(self) -> list[FraudReport]:
        return sorted(self.fraud_reports, key=lambda item: item.createdAt, reverse=True)

    def get_report(self, report_id: str) -> Optional[FraudReport]:
        for report in self.fraud_reports:
            if report.reportId == report_id:
                return report
        return None

    def create_wellness_log(self, log: WellnessLog) -> WellnessLog:
        self.wellness_logs.insert(0, log)
        for profile in self.senior_profiles:
            if profile.userId == log.userId:
                profile.lastCheckIn = log.timestamp
                delta = 18 if log.needsHelp else -8
                profile.riskScore = max(10, min(100, profile.riskScore + delta))
                break
        return log

    def list_wellness_logs(self, user_id: Optional[str] = None) -> list[WellnessLog]:
        logs = self.wellness_logs
        if user_id:
            logs = [log for log in logs if log.userId == user_id]
        return sorted(logs, key=lambda item: item.timestamp, reverse=True)

    def get_senior_profile(self, user_id: str) -> Optional[SeniorProfile]:
        for profile in self.senior_profiles:
            if profile.userId == user_id:
                return profile
        return None

    def create_notification(self, notification: NotificationRecord) -> NotificationRecord:
        self.notifications.insert(0, notification)
        return notification

    def list_notifications(self, recipient_id: Optional[str] = None) -> list[NotificationRecord]:
        notifications = self.notifications
        if recipient_id:
            notifications = [item for item in notifications if item.recipientId == recipient_id]
        return sorted(notifications, key=lambda item: item.createdAt, reverse=True)

    def build_dashboard_summary(self) -> dict:
        active_sos = len([item for item in self.sos_incidents if item.status != IncidentStatus.RESOLVED])
        open_investigations = len([item for item in self.fraud_reports if item.riskScore >= 75])
        high_risk = [profile for profile in self.senior_profiles if profile.riskScore >= 60]
        trend_counts = defaultdict(lambda: {"sos": 0, "fraud": 0})
        for incident in self.sos_incidents:
            trend_counts[incident.createdAt.strftime("%a")]["sos"] += 1
        for report in self.fraud_reports:
            trend_counts[report.createdAt.strftime("%a")]["fraud"] += 1
        trend = [
            {"day": day, "sos": counts["sos"], "fraud": counts["fraud"]}
            for day, counts in trend_counts.items()
        ]
        seniors = []
        for profile in high_risk:
            user = self.get_user(profile.userId)
            if user:
                seniors.append(
                    {
                        "userId": user.id,
                        "name": user.name,
                        "riskScore": profile.riskScore,
                        "lastCheckIn": profile.lastCheckIn.isoformat(),
                        "medicalConditions": profile.medicalConditions,
                    }
                )
        return {
            "activeSOSCases": active_sos,
            "fraudReports": len(self.fraud_reports),
            "highRiskSeniors": len(high_risk),
            "openInvestigations": open_investigations,
            "trend": trend,
            "seniors": seniors,
        }

    def build_heatmap(self) -> list[dict]:
        points: list[dict] = []
        for incident in self.sos_incidents:
            points.append(
                {
                    "id": incident.incidentId,
                    "type": "SOS",
                    "latitude": incident.latitude,
                    "longitude": incident.longitude,
                    "intensity": 90 if incident.status == IncidentStatus.OPEN else 70,
                }
            )
        for report in self.fraud_reports:
            profile = self.get_senior_profile(report.userId)
            if profile and profile.location:
                points.append(
                    {
                        "id": report.reportId,
                        "type": "FRAUD",
                        "latitude": profile.location.get("latitude", 23.0225),
                        "longitude": profile.location.get("longitude", 72.5714),
                        "intensity": report.riskScore,
                    }
                )
        return points

    def export_dashboard_incidents(self) -> list[dict]:
        rows: list[dict] = []
        for incident in self.list_incidents():
            user = self.get_user(incident.userId)
            rows.append(
                {
                    "incidentId": incident.incidentId,
                    "name": user.name if user else "Unknown Senior",
                    "location": f"{incident.latitude:.4f}, {incident.longitude:.4f}",
                    "latitude": incident.latitude,
                    "longitude": incident.longitude,
                    "triggerMethod": incident.triggerMethod,
                    "status": incident.status,
                    "severity": "Critical" if incident.status == IncidentStatus.OPEN else "High",
                    "createdAt": incident.createdAt.isoformat(),
                }
            )
        return rows

    def export_dashboard_reports(self) -> list[dict]:
        rows: list[dict] = []
        for report in self.list_reports():
            user = self.get_user(report.userId)
            rows.append(
                {
                    "reportId": report.reportId,
                    "name": user.name if user else "Unknown Senior",
                    "messageText": report.messageText,
                    "classification": report.classification,
                    "riskScore": report.riskScore,
                    "aiExplanation": report.aiExplanation,
                    "recommendedAction": report.recommendedAction,
                    "imageUrl": report.imageUrl,
                    "extractedText": report.extractedText,
                    "createdAt": report.createdAt.isoformat(),
                }
            )
        return rows

from fastapi.testclient import TestClient

from app.main import api_app

client = TestClient(api_app)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "healthy"


def test_fraud_analyze_and_report() -> None:
    analyze = client.post(
        "/api/v1/fraud/analyze",
        json={"messageText": "Your bank account is blocked. Verify OTP and click the urgent link now."},
    )
    assert analyze.status_code == 200
    assert analyze.json()["data"]["classification"] in {"SCAM", "SUSPICIOUS"}

    report = client.post(
        "/api/v1/fraud/report",
        json={"userId": "usr_senior_1", "messageText": "Claim your lottery prize and share OTP immediately."},
    )
    assert report.status_code == 200
    assert report.json()["data"]["reportId"].startswith("frd_")


def test_create_sos_and_fetch_live_feed() -> None:
    create = client.post(
        "/api/v1/sos/create",
        json={"userId": "usr_senior_1", "latitude": 23.025, "longitude": 72.571, "triggerMethod": "BUTTON"},
    )
    assert create.status_code == 200

    live = client.get("/api/v1/sos/live")
    assert live.status_code == 200
    assert len(live.json()["data"]) >= 1


def test_dashboard_summary_contains_metrics() -> None:
    response = client.get("/api/v1/dashboard/summary")
    assert response.status_code == 200
    data = response.json()["data"]
    assert "activeSOSCases" in data
    assert "fraudReports" in data

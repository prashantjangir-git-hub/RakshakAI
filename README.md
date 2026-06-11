# RakshakAI

RakshakAI is a hackathon-ready cyber-aware safety and welfare platform for senior citizens. This repository includes:

- `backend`: FastAPI APIs for SOS, fraud analysis, wellness, notifications, and dashboard data
- `dashboard`: React + Tailwind police dashboard with live incident and fraud views
- `frontend-mobile`: Flutter mobile app codebase for seniors and families
- `.trae/documents`: PRD and technical architecture documents

## Quick Start

### Backend
```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Dashboard
```bash
cd dashboard
npm install
npm run dev
```

### Mobile App
```bash
cd frontend-mobile
flutter pub get
flutter run
```

## Demo Accounts

- Senior: `9876543210`
- Family: `9123456780`
- Police: `9000000001`
- OTP: `123456`

## Notes

- The backend includes seeded demo data and realtime Socket.IO events.
- The dashboard fetches backend data when the API is running and falls back to demo data when offline.
- The Flutter SDK was not installed in the current environment, so the mobile app code was generated but not executed locally.

# RakshakAI Solution Document

## 1. Title
RakshakAI: Cyber-Aware Safety and Welfare Platform for Senior Citizens

## 2. Problem Overview
Senior citizens are increasingly targeted by cyber fraud through SMS, messaging apps, fake calls, phishing links, and impersonation scams. At the same time, many seniors also face delayed emergency response during health or safety incidents, especially when they live alone or are not under regular supervision. Existing products often handle only one of these problems at a time, such as spam detection, emergency calling, or health monitoring. This creates a fragmented support ecosystem.

RakshakAI addresses this gap by unifying scam detection, SOS emergency response, welfare monitoring, family alerting, and police-side visibility in one connected platform.

## 3. Proposed Solution
RakshakAI is a full-stack platform composed of:
- a Flutter mobile application for senior citizens and family members
- a FastAPI backend that coordinates fraud analysis, incidents, notifications, and risk tracking
- a React dashboard for police and response teams

The platform focuses on three major objectives:
- protect seniors from cyber scams through AI-assisted analysis
- enable instant distress signaling with location-aware SOS workflows
- support proactive welfare monitoring through daily check-ins and risk indicators

## 4. Core Modules

### 4.1 AI Scam Detection
This module allows a senior citizen to submit suspicious content in the form of message text or a screenshot. The backend analyzes the content, calculates a risk score, classifies the content as safe, suspicious, or scam, and returns a plain-language explanation with recommended action. Evidence can also be saved and escalated as a fraud report.

### 4.2 Emergency SOS
This module allows a user to trigger emergency help quickly through a single tap or through voice activation in the final expanded version. The system captures location details, creates an incident record, and notifies family members and police-facing systems.

### 4.3 Welfare Monitoring
This module supports regular wellbeing checks using simple yes or help-oriented responses. Wellness logs are tracked and can influence risk scoring. Missed check-ins or repeated distress responses can help identify silent welfare risk before an emergency becomes severe.

### 4.4 Police Dashboard
This module provides operational visibility for authorities. It surfaces active incidents, fraud reports, high-risk seniors, and map-based hotspots. This helps teams prioritize action, review evidence, and monitor patterns.

## 5. User Roles

### Senior Citizen
- verify suspicious messages
- trigger SOS alerts
- submit daily check-ins
- review guidance and alerts

### Family Member
- receive alerts
- monitor the status of the senior
- stay informed during emergencies

### Police Officer
- review live incidents
- inspect fraud evidence
- track open cases
- analyze geographic patterns

## 6. Architecture Summary
The system follows a modular client-server architecture.

- The Flutter mobile app serves senior citizens and families.
- The FastAPI backend exposes versioned REST APIs and coordinates business logic.
- A Socket.IO layer supports live updates for emergency and fraud events.
- The React dashboard provides a command-and-control style interface for monitoring and action.
- MongoDB is the target persistent data layer for users, incidents, reports, logs, and notifications.
- AI services such as Gemini, Tesseract, and Whisper are intended for smarter fraud, OCR, and voice workflows.

For hackathon reliability, the current prototype also includes seeded demo data and fallback logic to keep the core experience functional even when external AI services are unavailable.

## 7. Technology Stack

### Frontend Mobile
- Flutter
- Dart
- Provider

### Dashboard
- React
- TypeScript
- Vite
- Tailwind CSS
- Recharts
- Leaflet

### Backend
- FastAPI
- Python
- Pydantic
- Socket.IO
- Uvicorn

### Data and Platform
- MongoDB / MongoDB Atlas
- OpenStreetMap
- Render

### AI and Processing
- Gemini API
- Tesseract OCR
- Whisper speech-to-text

## 8. Working Flow

### Scam Detection Flow
1. Senior uploads suspicious text or screenshot.
2. Screenshot text is extracted through OCR when needed.
3. The message is analyzed and risk-scored.
4. The app displays classification, explanation, and recommended action.
5. The user may save evidence and submit a fraud report.
6. The report becomes visible in the police dashboard.

### SOS Flow
1. Senior presses SOS or uses a voice trigger in the intended expanded version.
2. The backend captures the user and location context.
3. An incident is created and distributed through notifications.
4. Family members and dashboard operators receive the alert.
5. Authorities track and update incident status.

### Wellness Flow
1. Senior completes a daily check-in.
2. The response is stored in wellness logs.
3. The backend updates risk indications.
4. High-risk patterns can be surfaced to family or dashboard users.

## 9. Existing Innovation and Relevance
The problem space already includes spam classifiers, phishing detection engines, emergency safety applications, telecare systems, and smart monitoring tools. However, most of these systems are isolated and focus on either fraud, emergency care, or welfare. RakshakAI is relevant because it unifies these capabilities into one coordinated platform designed for a high-risk and often digitally vulnerable user group: senior citizens.

The platform draws inspiration from:
- AI-enabled scam and phishing detection systems
- OCR-driven document and screenshot analysis
- voice-triggered safety tools
- eldercare check-in and reminder systems
- police or command dashboards with live alert streams and map overlays

## 10. Challenges and Risks
- Real-world scam language evolves rapidly, so model quality must be continuously improved.
- OCR can fail on unclear screenshots, multiple languages, or forwarded images.
- Voice-triggered emergency activation needs careful tuning to avoid accidental alerts.
- Security and privacy are critical because the system handles personal, medical, and location data.
- Adoption depends on creating a very simple, accessible interface for older adults.
- Production deployment would require stronger authentication, audit trails, and system hardening.
- External integration with law enforcement systems may involve policy and compliance requirements.

## 11. Risk Mitigation Strategy
- Use a hybrid scam detection approach with both AI analysis and rules-based fallback.
- Keep the UI minimal, high-contrast, and touch-friendly.
- Maintain seeded and mockable demo data for dependable presentations.
- Use modular services so AI providers can be swapped or upgraded.
- Start with role-based controlled access and expand toward production-grade security later.
- Preserve evidence and timestamps for better accountability and case review.

## 12. Accomplishments to Date
The current prototype already demonstrates the core vision of the project.

Implemented:
- Flutter mobile app with key senior and family screens
- FastAPI backend with versioned endpoints for auth, fraud, SOS, wellness, notifications, and dashboard data
- React police dashboard with summary, incidents, fraud reports, heatmap, and senior risk views
- real-time event support through Socket.IO
- seeded in-memory repository for reliable demos
- product requirement and technical architecture documentation

Verification completed locally:
- backend tests passed successfully
- backend server responded correctly to the health endpoint
- dashboard production build completed successfully
- Flutter widget tests passed successfully

## 13. Expected Outcome and Impact
RakshakAI can reduce the likelihood of senior citizens falling victim to fraud, help emergency incidents reach the right responders faster, and improve visibility into silent welfare risks. The longer-term impact includes better fraud reporting, stronger family confidence, faster operational awareness for authorities, and data-driven understanding of risk hotspots.

## 14. Future Scope
- multilingual scam analysis and voice support
- Gujarati and Hindi voice assistance
- banking integration for transaction-level warnings
- wearable device support
- offline emergency fallback features
- predictive hotspot and unsafe-zone analytics

## 15. Conclusion
RakshakAI is a socially relevant, technically feasible, and hackathon-ready solution that combines AI, realtime communication, mobile accessibility, and authority dashboards into one meaningful safety platform for senior citizens. The current MVP already demonstrates the core workflows, and the architecture supports future expansion into a production-scale public safety and welfare system.

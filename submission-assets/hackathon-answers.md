# RakshakAI Hackathon Submission Answers

## 1. Synopsis / Abstract
RakshakAI is an AI-powered cyber-aware safety and welfare platform built to protect senior citizens from digital fraud, enable instant emergency response, and support proactive daily wellbeing monitoring. The solution combines a Flutter mobile app for seniors and family members, a FastAPI backend for incident and fraud management, and a React police dashboard for live monitoring and case handling. The platform allows seniors to check suspicious messages, screenshots, or voice inputs for scam risk, trigger SOS alerts by button or voice, complete daily wellness check-ins, and stay connected with family and authorities through one unified ecosystem.

## 2. Literature Review / Existing Innovation & Technology
Current solutions in this domain usually solve only one part of the problem. Spam filters and scam detection tools help identify phishing messages, but they are often designed for general users and do not explain the risk in a simple way for senior citizens. Emergency SOS apps provide location sharing and contact alerts, but most do not connect directly with fraud reporting or welfare monitoring. Elder-care and telehealth applications support reminders, check-ins, and family coordination, but they usually do not include cyber-fraud awareness or police-facing operational dashboards.

RakshakAI builds on the strengths of these existing innovations:
- AI-based text classification for scam and phishing detection
- OCR pipelines for reading screenshots of suspicious messages
- Speech-to-text and keyword matching for voice-triggered emergency activation
- Real-time dashboards for alert monitoring and rapid response
- Geospatial mapping tools for hotspot and pattern analysis

The innovation in our work is the integration of cyber safety, emergency response, welfare monitoring, family alerts, and police visibility into one coordinated platform focused specifically on senior citizens.

## 3. Your Approach to Solve the Problem
Our approach is to build an end-to-end, hackathon-ready MVP with three connected layers:

1. Senior-facing mobile experience:
   The Flutter mobile app provides large, accessible screens for login, SOS, scam checking, wellness check-ins, and profile management.

2. Intelligent backend orchestration:
   The FastAPI backend handles authentication, fraud analysis, SOS creation, wellness logs, notifications, and dashboard data APIs. It also emits real-time updates using Socket.IO.

3. Police and authority visibility:
   A React dashboard gives officers a live view of incidents, fraud reports, risk heatmaps, and high-risk senior profiles for faster action and better case handling.

Methodology:
- Build a modular full-stack prototype first
- Use seeded data and a mock OTP flow for reliable demo execution
- Support fraud detection from both direct text and screenshot OCR inputs
- Trigger emergency workflows that notify both family and police-side systems
- Track missed wellness check-ins and elevated risk patterns
- Present all alerts and reports in a unified authority dashboard

This approach ensures the system is socially impactful, technically feasible, and demo-ready within hackathon constraints.

## 4. Road Map / Flow Diagram
The roadmap and flow diagram files are saved in the `submission-assets` folder.

Files:
- `submission-assets/roadmap-flow-diagram.png`
- `submission-assets/roadmap-flow-diagram.pdf`

The diagram covers:
- Senior user actions
- Scam detection flow
- SOS emergency flow
- Wellness monitoring flow
- Backend processing
- Family and police notifications
- Dashboard review and case response

## 5. Tools & Technologies to be Used
Frontend Mobile:
- Flutter
- Dart
- Provider state management

Police Dashboard:
- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Recharts
- Leaflet

Backend:
- FastAPI
- Python
- Pydantic
- Uvicorn
- Python Socket.IO

Database:
- MongoDB / MongoDB Atlas

AI and Intelligence:
- Gemini API for scam analysis
- Tesseract OCR for screenshot text extraction
- Whisper for speech-to-text based voice SOS
- Rule-based fallback scam detection for demo resilience

Mapping and Realtime:
- OpenStreetMap
- Socket.IO

Development and Deployment:
- Git / GitHub
- Render
- Postman
- VS Code / Trae

## 6. Challenges / Risks in Implementing the Final Prototype
- OCR accuracy may reduce when screenshots are blurred, low-quality, or written in mixed languages.
- Scam detection quality depends on training prompts, model behavior, and the variety of real-world fraud patterns.
- Voice-triggered SOS can produce false positives or false negatives in noisy environments.
- Real-time alert delivery must remain reliable during unstable network conditions.
- Privacy and security are critical because the system handles location, health, and fraud evidence data.
- Elder-friendly UX is essential; if the interface becomes complex, adoption by senior citizens may drop.
- Integration with real police systems and telecom workflows may require approvals and compliance beyond the hackathon stage.
- Scaling from demo data to production-grade multi-user usage will require stronger persistence, monitoring, and access control.

## 7. Possible Outcome of Your Work
The expected outcome is a unified platform that improves both safety and response quality for senior citizens. The solution can reduce the chances of seniors falling for scams, shorten emergency response time, increase family awareness during distress situations, and help police teams prioritize real incidents with better context and evidence. Over time, the platform can also generate trend intelligence on fraud hotspots, repeated scam patterns, welfare risks, and geographically vulnerable zones.

## 8. Accomplishments to Date
We have already built a functional hackathon MVP across mobile, backend, and dashboard layers.

Completed work includes:
- Flutter mobile app with screens for login, home, SOS, scam detector, scam result, wellness check, profile, and family alerts
- FastAPI backend with APIs for authentication, fraud analysis/reporting, SOS creation/history/live feed, wellness check-ins, notifications, and dashboard summaries
- React police dashboard with summary cards, live incidents view, fraud reports panel, heatmap analytics, and high-risk seniors page
- In-memory seeded demo data for reliable hackathon presentation
- Real-time event support through Socket.IO for SOS and fraud updates
- Built-in demo-friendly scam scoring and explanation logic
- Architecture and PRD documentation prepared

Local verification completed:
- Backend API tests passed
- Backend server started successfully and responded on `/health`
- Dashboard production build completed successfully
- Flutter widget tests passed

## 9. Solution Document
The complete solution document is saved in the `submission-assets` folder.

Files:
- `submission-assets/solution-document.md`
- `submission-assets/solution-document.pdf`

This document includes:
- problem understanding
- system overview
- module descriptions
- implementation approach
- architecture summary
- technology stack
- risks and mitigation
- accomplishments to date
- expected impact

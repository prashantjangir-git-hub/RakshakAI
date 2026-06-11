## 1. Architecture Design
```mermaid
flowchart LR
    A["Flutter Mobile App"] --> B["FastAPI Backend"]
    C["React Police Dashboard"] --> B
    D["Family Monitoring View"] --> B
    B --> E["MongoDB Atlas or Local MongoDB"]
    B --> F["Socket.IO Realtime Gateway"]
    B --> G["Gemini API"]
    B --> H["Tesseract OCR Service"]
    B --> I["Whisper or Keyword Voice Detection"]
    C --> F
```

## 2. Technology Description
- Frontend Mobile: Flutter with Provider for state management and responsive accessible UI
- Dashboard Frontend: React@18 + Vite + Tailwind CSS + React Router + Recharts + Leaflet
- Backend: FastAPI + Pydantic + Motor + Python Socket.IO server
- Database: MongoDB with collections for users, profiles, incidents, reports, wellness logs, notifications
- Realtime: Socket.IO for live incident and fraud report updates
- AI Services: Gemini API for scam analysis, Tesseract OCR for screenshots, Whisper or fallback keyword detection for voice SOS
- Initialization Approach: monorepo with separate `frontend-mobile`, `backend`, and `dashboard` applications

## 3. Route Definitions
| Route | Purpose |
|-------|---------|
| / | Dashboard landing and summary cards |
| /incidents | Live SOS incident monitor |
| /fraud-reports | Fraud investigation panel |
| /heatmap | Risk heatmap with geographic overlays |
| /seniors | High-risk seniors and welfare flags |
| /login | Police login page |

## 4. API Definitions

### 4.1 Authentication
```ts
type LoginRequest = {
  phone: string;
  role: "senior" | "family" | "police";
};

type VerifyOtpRequest = {
  phone: string;
  otp: string;
};

type AuthResponse = {
  success: boolean;
  message: string;
  data: {
    token: string;
    user: {
      id: string;
      role: "senior" | "family" | "police";
      name: string;
      phone: string;
    };
  };
};
```

### 4.2 Fraud Analysis
```ts
type FraudAnalyzeRequest = {
  messageText?: string;
  imageBase64?: string;
};

type FraudAnalyzeResponse = {
  success: boolean;
  message: string;
  data: {
    extractedText?: string;
    riskScore: number;
    classification: "SAFE" | "SUSPICIOUS" | "SCAM";
    aiExplanation: string;
    recommendedAction: string;
  };
};
```

### 4.3 SOS
```ts
type SosCreateRequest = {
  userId: string;
  latitude: number;
  longitude: number;
  triggerMethod: "BUTTON" | "VOICE";
};

type SosResponse = {
  success: boolean;
  message: string;
  data: {
    incidentId: string;
    status: "OPEN" | "IN_PROGRESS" | "RESOLVED";
    latitude: number;
    longitude: number;
    createdAt: string;
  };
};
```

### 4.4 Wellness
```ts
type WellnessCheckInRequest = {
  userId: string;
  safetyStatus: "SAFE" | "NEED_HELP";
  healthStatus: "HEALTHY" | "NEED_HELP";
  needsHelp: boolean;
};
```

## 5. Server Architecture Diagram
```mermaid
flowchart TD
    A["API Router"] --> B["Controller Layer"]
    B --> C["Service Layer"]
    C --> D["Repository Layer"]
    D --> E["MongoDB Collections"]
    C --> F["AI Integration Service"]
    C --> G["Realtime Event Publisher"]
```

## 6. Data Model
### 6.1 Data Model Definition
```mermaid
erDiagram
    USERS ||--o{ SENIOR_PROFILES : "has"
    USERS ||--o{ SOS_INCIDENTS : "creates"
    USERS ||--o{ FRAUD_REPORTS : "submits"
    USERS ||--o{ WELLNESS_LOGS : "records"
    USERS ||--o{ NOTIFICATIONS : "receives"

    USERS {
        string _id
        string role
        string name
        string phone
        string email
        string language
        string address
        string emergencyContacts
        datetime createdAt
    }

    SENIOR_PROFILES {
        string userId
        string medicalConditions
        string medications
        number riskScore
        datetime lastCheckIn
        object location
    }

    SOS_INCIDENTS {
        string incidentId
        string userId
        number latitude
        number longitude
        string status
        string triggerMethod
        datetime createdAt
    }

    FRAUD_REPORTS {
        string reportId
        string userId
        string messageText
        string imageUrl
        number riskScore
        string classification
        string aiExplanation
        datetime createdAt
    }

    WELLNESS_LOGS {
        string logId
        string userId
        string healthStatus
        string safetyStatus
        boolean needsHelp
        datetime timestamp
    }

    NOTIFICATIONS {
        string notificationId
        string recipientId
        string type
        string message
        boolean readStatus
        datetime createdAt
    }
```

### 6.2 Data Definition Language
```js
db.users.createIndex({ phone: 1 }, { unique: true });
db.seniorProfiles.createIndex({ userId: 1 }, { unique: true });
db.sosIncidents.createIndex({ createdAt: -1 });
db.sosIncidents.createIndex({ status: 1, createdAt: -1 });
db.fraudReports.createIndex({ userId: 1, createdAt: -1 });
db.fraudReports.createIndex({ classification: 1, createdAt: -1 });
db.wellnessLogs.createIndex({ userId: 1, timestamp: -1 });
db.notifications.createIndex({ recipientId: 1, createdAt: -1 });
```

## 7. Implementation Notes
- Start with a hackathon-grade full MVP that works with seeded data and mock OTP to reduce setup risk.
- Use environment-driven AI adapters so Gemini, OCR, and voice modules can run in demo mode when keys or binaries are unavailable.
- Provide reusable design tokens for dashboard and mobile UI so the product looks cohesive across platforms.
- Keep Socket.IO events consistent: `sos:new`, `sos:updated`, `fraud:new_report`, and `wellness:risk_flag`.

export type RiskClassification = 'SAFE' | 'SUSPICIOUS' | 'SCAM'
export type IncidentStatus = 'OPEN' | 'IN_PROGRESS' | 'RESOLVED'

export type TrendPoint = {
  day: string
  sos: number
  fraud: number
}

export type SeniorRisk = {
  userId: string
  name: string
  riskScore: number
  lastCheckIn: string
  medicalConditions: string[]
}

export type DashboardSummary = {
  activeSOSCases: number
  fraudReports: number
  highRiskSeniors: number
  openInvestigations: number
  trend: TrendPoint[]
  seniors: SeniorRisk[]
}

export type Incident = {
  incidentId: string
  name: string
  location: string
  latitude: number
  longitude: number
  triggerMethod: 'BUTTON' | 'VOICE'
  status: IncidentStatus
  severity: 'Moderate' | 'High' | 'Critical'
  createdAt: string
}

export type FraudReport = {
  reportId: string
  name: string
  messageText: string
  classification: RiskClassification
  riskScore: number
  aiExplanation: string
  recommendedAction: string
  imageUrl?: string | null
  extractedText?: string | null
  createdAt: string
}

export type HeatPoint = {
  id: string
  type: 'SOS' | 'FRAUD'
  latitude: number
  longitude: number
  intensity: number
}

export type ApiEnvelope<T> = {
  success: boolean
  message: string
  data: T
}

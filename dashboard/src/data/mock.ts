import type { DashboardSummary, FraudReport, HeatPoint, Incident } from '@/types'

export const mockSummary: DashboardSummary = {
  activeSOSCases: 3,
  fraudReports: 18,
  highRiskSeniors: 4,
  openInvestigations: 7,
  trend: [
    { day: 'Mon', sos: 1, fraud: 2 },
    { day: 'Tue', sos: 2, fraud: 4 },
    { day: 'Wed', sos: 3, fraud: 3 },
    { day: 'Thu', sos: 1, fraud: 5 },
    { day: 'Fri', sos: 4, fraud: 6 },
  ],
  seniors: [
    {
      userId: 'usr_senior_1',
      name: 'Savitri Devi',
      riskScore: 68,
      lastCheckIn: new Date(Date.now() - 1000 * 60 * 60 * 7).toISOString(),
      medicalConditions: ['Hypertension'],
    },
    {
      userId: 'usr_senior_2',
      name: 'Mahendra Joshi',
      riskScore: 74,
      lastCheckIn: new Date(Date.now() - 1000 * 60 * 60 * 18).toISOString(),
      medicalConditions: ['Diabetes'],
    },
  ],
}

export const mockIncidents: Incident[] = [
  {
    incidentId: 'sos_1002',
    name: 'Savitri Devi',
    location: '23.0350, 72.5530',
    latitude: 23.035,
    longitude: 72.553,
    triggerMethod: 'VOICE',
    status: 'OPEN',
    severity: 'Critical',
    createdAt: new Date(Date.now() - 1000 * 60 * 4).toISOString(),
  },
  {
    incidentId: 'sos_1001',
    name: 'Savitri Devi',
    location: '23.0225, 72.5714',
    latitude: 23.0225,
    longitude: 72.5714,
    triggerMethod: 'BUTTON',
    status: 'IN_PROGRESS',
    severity: 'High',
    createdAt: new Date(Date.now() - 1000 * 60 * 14).toISOString(),
  },
]

export const mockReports: FraudReport[] = [
  {
    reportId: 'frd_2001',
    name: 'Savitri Devi',
    messageText: 'Your bank KYC is blocked. Click the secure link now to avoid account suspension.',
    classification: 'SCAM',
    riskScore: 91,
    aiExplanation: 'The message creates urgency, pretends to be from a bank, and pushes the user to click a link.',
    recommendedAction: 'Do not click the link and verify with the bank using an official number.',
    extractedText: 'Your bank KYC is blocked. Click the secure link now to avoid account suspension.',
    createdAt: new Date(Date.now() - 1000 * 60 * 60 * 3).toISOString(),
  },
  {
    reportId: 'frd_2002',
    name: 'Savitri Devi',
    messageText: 'You have won a festival prize of Rs 50,000. Share your OTP to claim it.',
    classification: 'SCAM',
    riskScore: 96,
    aiExplanation: 'Prize scams use fake rewards to collect OTP or bank details.',
    recommendedAction: 'Delete the message and never share OTP or bank credentials.',
    createdAt: new Date(Date.now() - 1000 * 60 * 60 * 18).toISOString(),
  },
  {
    reportId: 'frd_2003',
    name: 'Mahendra Joshi',
    messageText: 'Your electricity bill refund is pending. Confirm account details.',
    classification: 'SUSPICIOUS',
    riskScore: 58,
    aiExplanation: 'The refund message asks for sensitive account verification and should be checked carefully.',
    recommendedAction: 'Verify through the official electricity provider before responding.',
    createdAt: new Date(Date.now() - 1000 * 60 * 60 * 30).toISOString(),
  },
]

export const mockHeatmap: HeatPoint[] = [
  { id: 'pt_1', type: 'SOS', latitude: 23.035, longitude: 72.553, intensity: 92 },
  { id: 'pt_2', type: 'SOS', latitude: 23.0225, longitude: 72.5714, intensity: 74 },
  { id: 'pt_3', type: 'FRAUD', latitude: 23.03, longitude: 72.56, intensity: 88 },
  { id: 'pt_4', type: 'FRAUD', latitude: 23.018, longitude: 72.58, intensity: 61 },
]

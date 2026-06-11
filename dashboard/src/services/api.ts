import { mockHeatmap, mockIncidents, mockReports, mockSummary } from '@/data/mock'
import type { ApiEnvelope, DashboardSummary, FraudReport, HeatPoint, Incident } from '@/types'

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api/v1'
const SOCKET_BASE = import.meta.env.VITE_SOCKET_URL || 'http://127.0.0.1:8000'
export const DASHBOARD_SESSION_KEY = 'rakshakai-dashboard-session'

export type AuthRole = 'senior' | 'family' | 'police'

export type AuthUser = {
  _id: string
  role: AuthRole
  name: string
  phone: string
  email?: string
}

export type AuthSession = {
  token: string
  user: AuthUser
}

type OtpRequest = {
  otp: string
  expiresAt: string
  user: AuthUser
}

async function getData<T>(path: string, fallback: T): Promise<T> {
  try {
    const response = await fetch(`${API_BASE}${path}`)
    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`)
    }
    const payload: ApiEnvelope<T> = await response.json()
    return payload.data
  } catch {
    return fallback
  }
}

async function postData<T>(path: string, body: unknown): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })

  const payload = (await response.json().catch(() => null)) as
    | ApiEnvelope<T>
    | { detail?: string; message?: string }
    | null

  if (!response.ok) {
    const errorPayload =
      payload && typeof payload === 'object' && ('detail' in payload || 'message' in payload)
        ? (payload as { detail?: string; message?: string })
        : null
    const message = errorPayload?.detail || errorPayload?.message || 'Request failed.'
    throw new Error(message)
  }

  if (!payload || !('data' in payload)) {
    throw new Error('Unexpected API response.')
  }

  return payload.data
}

export const api = {
  socketBase: SOCKET_BASE,
  getSummary: () => getData<DashboardSummary>('/dashboard/summary', mockSummary),
  getIncidents: () => getData<Incident[]>('/dashboard/incidents', mockIncidents),
  getFraudReports: () => getData<FraudReport[]>('/dashboard/fraud-reports', mockReports),
  getHeatmap: () => getData<HeatPoint[]>('/dashboard/heatmap', mockHeatmap),
  requestOtp: (phone: string, role: AuthRole) => postData<OtpRequest>('/auth/login', { phone, role }),
  verifyOtp: (phone: string, otp: string) => postData<AuthSession>('/auth/verify-otp', { phone, otp }),
}

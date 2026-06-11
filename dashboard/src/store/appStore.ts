import { create } from 'zustand'
import { io, type Socket } from 'socket.io-client'

import { api } from '@/services/api'
import type { DashboardSummary, FraudReport, HeatPoint, Incident } from '@/types'

let socketRef: Socket | null = null

type AppState = {
  summary: DashboardSummary | null
  incidents: Incident[]
  reports: FraudReport[]
  heatmap: HeatPoint[]
  loading: boolean
  connected: boolean
  initialize: () => Promise<void>
}

export const useAppStore = create<AppState>((set, get) => ({
  summary: null,
  incidents: [],
  reports: [],
  heatmap: [],
  loading: true,
  connected: false,
  initialize: async () => {
    if (get().summary) return
    const [summary, incidents, reports, heatmap] = await Promise.all([
      api.getSummary(),
      api.getIncidents(),
      api.getFraudReports(),
      api.getHeatmap(),
    ])

    set({ summary, incidents, reports, heatmap, loading: false })

    if (!socketRef) {
      socketRef = io(api.socketBase, { autoConnect: true, transports: ['websocket', 'polling'] })
      socketRef.on('connect', () => set({ connected: true }))
      socketRef.on('disconnect', () => set({ connected: false }))
      socketRef.on('sos:new', (incident: Incident) => {
        set((state) => ({ incidents: [incident, ...state.incidents] }))
      })
      socketRef.on('sos:updated', (updated: Incident) => {
        set((state) => ({
          incidents: state.incidents.map((incident) =>
            incident.incidentId === updated.incidentId ? updated : incident,
          ),
        }))
      })
      socketRef.on('fraud:new_report', (report: FraudReport) => {
        set((state) => ({ reports: [report, ...state.reports] }))
      })
      socketRef.on('wellness:risk_flag', (payload: { userId: string; riskScore: number }) => {
        set((state) => ({
          summary: state.summary
            ? {
                ...state.summary,
                seniors: state.summary.seniors.map((senior) =>
                  senior.userId === payload.userId ? { ...senior, riskScore: payload.riskScore } : senior,
                ),
              }
            : state.summary,
        }))
      })
    }
  },
}))

import type { ReactElement } from 'react'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'

import AppShell from '@/components/AppShell'
import FraudReportsPage from '@/pages/FraudReportsPage'
import HeatmapPage from '@/pages/HeatmapPage'
import HomePage from '@/pages/HomePage'
import IncidentsPage from '@/pages/IncidentsPage'
import LoginPage from '@/pages/LoginPage'
import SeniorsPage from '@/pages/SeniorsPage'
import { DASHBOARD_SESSION_KEY } from '@/services/api'

function hasDashboardSession() {
  return typeof window !== 'undefined' && window.sessionStorage.getItem(DASHBOARD_SESSION_KEY) !== null
}

function ProtectedRoute({ element }: { element: ReactElement }) {
  return hasDashboardSession() ? element : <Navigate to="/login" replace />
}

function GuestRoute({ element }: { element: ReactElement }) {
  return hasDashboardSession() ? <Navigate to="/" replace /> : element
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<GuestRoute element={<LoginPage />} />} />
        <Route element={<ProtectedRoute element={<AppShell />} />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/incidents" element={<IncidentsPage />} />
          <Route path="/fraud-reports" element={<FraudReportsPage />} />
          <Route path="/heatmap" element={<HeatmapPage />} />
          <Route path="/seniors" element={<SeniorsPage />} />
        </Route>
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

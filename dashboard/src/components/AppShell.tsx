import { Bell, LayoutDashboard, Map, ShieldAlert, Siren, Users } from 'lucide-react'
import { NavLink, Outlet } from 'react-router-dom'
import { useEffect } from 'react'

import { useAppStore } from '@/store/appStore'

const items = [
  { to: '/', label: 'Overview', icon: LayoutDashboard },
  { to: '/incidents', label: 'Incidents', icon: Siren },
  { to: '/fraud-reports', label: 'Fraud Reports', icon: ShieldAlert },
  { to: '/heatmap', label: 'Heatmap', icon: Map },
  { to: '/seniors', label: 'Welfare', icon: Users },
]

export default function AppShell() {
  const initialize = useAppStore((state) => state.initialize)
  const connected = useAppStore((state) => state.connected)
  const summary = useAppStore((state) => state.summary)

  useEffect(() => {
    void initialize()
  }, [initialize])

  return (
    <div className="min-h-screen bg-[#020816] text-slate-100">
      <div className="mx-auto grid min-h-screen max-w-[1600px] grid-cols-1 gap-6 px-4 py-4 lg:grid-cols-[280px_minmax(0,1fr)] lg:px-6">
        <aside className="rounded-[32px] border border-white/10 bg-slate-950/75 p-6 shadow-[0_24px_80px_rgba(4,10,30,0.42)] backdrop-blur-xl">
          <div>
            <p className="text-xs uppercase tracking-[0.35em] text-cyan-200/70">RakshakAI</p>
            <h1 className="mt-4 font-display text-4xl text-white">Police Command Hub</h1>
            <p className="mt-3 text-sm text-slate-400">Live cyber-safety, emergency response, and welfare intelligence for senior citizens.</p>
          </div>

          <nav className="mt-8 space-y-2">
            {items.map((item) => {
              const Icon = item.icon
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  className={({ isActive }) => `flex items-center gap-3 rounded-2xl px-4 py-3 text-sm transition ${isActive ? 'bg-cyan-400/15 text-white' : 'text-slate-300 hover:bg-white/5 hover:text-white'}`}
                >
                  <Icon className="h-5 w-5" />
                  {item.label}
                </NavLink>
              )
            })}
          </nav>

          <div className="mt-8 rounded-[28px] border border-cyan-400/15 bg-cyan-400/10 p-5">
            <p className="text-xs uppercase tracking-[0.3em] text-cyan-100/80">Live Status</p>
            <div className="mt-3 flex items-center gap-3">
              <span className={`h-3 w-3 rounded-full ${connected ? 'bg-emerald-400 shadow-[0_0_18px_rgba(52,211,153,0.7)]' : 'bg-amber-400'}`} />
              <p className="text-sm text-slate-100">{connected ? 'Realtime feed connected' : 'Demo feed active'}</p>
            </div>
            <p className="mt-4 text-3xl font-semibold text-white">{summary?.activeSOSCases ?? '--'}</p>
            <p className="text-sm text-slate-300">active emergency cases right now</p>
          </div>
        </aside>

        <main className="rounded-[32px] border border-white/10 bg-[radial-gradient(circle_at_top,_rgba(34,211,238,0.14),_transparent_28%),linear-gradient(180deg,_rgba(10,18,40,0.95),_rgba(3,8,20,0.98))] p-6 shadow-[0_30px_120px_rgba(0,0,0,0.4)] lg:p-8">
          <header className="mb-8 flex flex-col gap-4 border-b border-white/8 pb-6 md:flex-row md:items-center md:justify-between">
            <div>
              <p className="text-xs uppercase tracking-[0.32em] text-slate-400">Operations Overview</p>
              <h2 className="mt-3 font-display text-4xl text-white">Protect faster. Respond smarter.</h2>
            </div>
            <div className="flex items-center gap-3 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-200">
              <Bell className="h-4 w-4 text-cyan-300" />
              Priority alerts route to family and police in real time.
            </div>
          </header>
          <Outlet />
        </main>
      </div>
    </div>
  )
}

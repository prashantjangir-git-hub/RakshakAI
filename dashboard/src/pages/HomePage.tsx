import { Activity, ShieldAlert, Siren, Users } from 'lucide-react'

import IncidentTable from '@/components/IncidentTable'
import Panel from '@/components/Panel'
import StatCard from '@/components/StatCard'
import TrendChart from '@/components/TrendChart'
import { useAppStore } from '@/store/appStore'

export default function HomePage() {
  const summary = useAppStore((state) => state.summary)
  const incidents = useAppStore((state) => state.incidents)
  const reports = useAppStore((state) => state.reports)
  const loading = useAppStore((state) => state.loading)

  if (loading || !summary) {
    return <div className="h-96 animate-pulse rounded-[28px] bg-white/5" />
  }

  return (
    <div className="space-y-6">
      <section className="grid gap-4 xl:grid-cols-4">
        <StatCard icon={Siren} label="Active SOS Cases" value={summary.activeSOSCases} note="Incidents requiring field attention" accent="bg-cyan-400" />
        <StatCard icon={ShieldAlert} label="Fraud Reports" value={summary.fraudReports} note="Scam submissions under review" accent="bg-rose-400" />
        <StatCard icon={Users} label="High-Risk Seniors" value={summary.highRiskSeniors} note="Wellbeing cases with elevated concern" accent="bg-amber-400" />
        <StatCard icon={Activity} label="Open Investigations" value={summary.openInvestigations} note="Fraud cases still awaiting closure" accent="bg-emerald-400" />
      </section>

      <section className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
        <Panel eyebrow="Operational Trend" title="Emergency and Fraud Activity">
          <TrendChart data={summary.trend} />
        </Panel>
        <Panel eyebrow="Tactical Note" title="Tonight's priority focus">
          <div className="space-y-5 text-sm text-slate-300">
            <div className="rounded-3xl border border-rose-500/20 bg-rose-500/10 p-4">
              <p className="font-semibold text-rose-100">Fraud spike pattern</p>
              <p className="mt-2">Bank impersonation and refund bait messages remain the highest-risk attack patterns in the current feed.</p>
            </div>
            <div className="rounded-3xl border border-cyan-400/20 bg-cyan-400/10 p-4">
              <p className="font-semibold text-cyan-100">Response protocol</p>
              <p className="mt-2">Prioritize voice-triggered SOS incidents first, then contact the nearest listed family member in parallel.</p>
            </div>
            <p className="text-slate-400">Latest fraud record count: {reports.length}. Latest live incident count: {incidents.length}.</p>
          </div>
        </Panel>
      </section>

      <IncidentTable incidents={incidents.slice(0, 4)} />
    </div>
  )
}

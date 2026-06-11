import IncidentTable from '@/components/IncidentTable'
import Panel from '@/components/Panel'
import { useAppStore } from '@/store/appStore'

export default function IncidentsPage() {
  const incidents = useAppStore((state) => state.incidents)

  return (
    <div className="space-y-6">
      <Panel eyebrow="Emergency Response" title="Incident Triage Board">
        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-3xl border border-white/10 bg-white/5 p-4 text-sm text-slate-300">1. Confirm the call or voice trigger.</div>
          <div className="rounded-3xl border border-white/10 bg-white/5 p-4 text-sm text-slate-300">2. Share GPS coordinates with the assigned responder.</div>
          <div className="rounded-3xl border border-white/10 bg-white/5 p-4 text-sm text-slate-300">3. Notify family before case escalation closes.</div>
        </div>
      </Panel>
      <IncidentTable incidents={incidents} />
    </div>
  )
}

import { Mic, Siren, TimerReset } from 'lucide-react'

import Panel from '@/components/Panel'
import { formatRelativeTime } from '@/lib/utils'
import type { Incident } from '@/types'

type IncidentTableProps = {
  incidents: Incident[]
}

export default function IncidentTable({ incidents }: IncidentTableProps) {
  return (
    <Panel eyebrow="Active Response" title="Live Incident Monitor">
      <div className="overflow-x-auto">
        <table className="min-w-full text-left text-sm text-slate-200">
          <thead className="text-xs uppercase tracking-[0.24em] text-slate-400">
            <tr>
              <th className="pb-4">Senior</th>
              <th className="pb-4">Trigger</th>
              <th className="pb-4">Location</th>
              <th className="pb-4">Status</th>
              <th className="pb-4">Opened</th>
            </tr>
          </thead>
          <tbody>
            {incidents.map((incident) => (
              <tr key={incident.incidentId} className="border-t border-white/6">
                <td className="py-4 font-medium text-white">{incident.name}</td>
                <td className="py-4">
                  <span className="inline-flex items-center gap-2 rounded-full bg-white/6 px-3 py-1 text-xs">
                    {incident.triggerMethod === 'VOICE' ? <Mic className="h-3.5 w-3.5" /> : <Siren className="h-3.5 w-3.5" />}
                    {incident.triggerMethod}
                  </span>
                </td>
                <td className="py-4 text-slate-300">{incident.location}</td>
                <td className="py-4">
                  <span className="inline-flex items-center gap-2 rounded-full border border-rose-500/20 bg-rose-500/10 px-3 py-1 text-xs text-rose-100">
                    <TimerReset className="h-3.5 w-3.5" />
                    {incident.status}
                  </span>
                </td>
                <td className="py-4 text-slate-400">{formatRelativeTime(incident.createdAt)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}

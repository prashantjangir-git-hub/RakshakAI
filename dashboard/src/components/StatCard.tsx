import type { LucideIcon } from 'lucide-react'

import Panel from '@/components/Panel'

type StatCardProps = {
  icon: LucideIcon
  label: string
  value: number
  accent: string
  note: string
}

export default function StatCard({ icon: Icon, label, value, accent, note }: StatCardProps) {
  return (
    <Panel className="relative overflow-hidden">
      <div className={`absolute inset-x-0 top-0 h-1 ${accent}`} />
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm text-slate-300">{label}</p>
          <p className="mt-4 font-display text-4xl text-white">{value}</p>
          <p className="mt-3 text-sm text-slate-400">{note}</p>
        </div>
        <div className={`rounded-2xl border border-white/10 p-3 ${accent} bg-opacity-10`}>
          <Icon className="h-6 w-6 text-white" />
        </div>
      </div>
    </Panel>
  )
}

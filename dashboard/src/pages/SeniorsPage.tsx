import Panel from '@/components/Panel'
import { formatShortTime } from '@/lib/utils'
import { useAppStore } from '@/store/appStore'

export default function SeniorsPage() {
  const seniors = useAppStore((state) => state.summary?.seniors ?? [])

  return (
    <div className="space-y-6">
      <Panel eyebrow="Welfare Monitoring" title="High-Risk Seniors">
        <div className="grid gap-4 lg:grid-cols-2">
          {seniors.map((senior) => (
            <article key={senior.userId} className="rounded-[28px] border border-white/10 bg-white/5 p-5">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="font-display text-2xl text-white">{senior.name}</p>
                  <p className="mt-2 text-sm text-slate-400">Last check-in: {formatShortTime(senior.lastCheckIn)}</p>
                </div>
                <div className="rounded-2xl border border-amber-400/25 bg-amber-400/10 px-4 py-3 text-center">
                  <p className="text-xs uppercase tracking-[0.2em] text-amber-100/80">Risk</p>
                  <p className="mt-2 text-3xl font-semibold text-white">{senior.riskScore}</p>
                </div>
              </div>
              <div className="mt-4 flex flex-wrap gap-2">
                {senior.medicalConditions.map((condition) => (
                  <span key={condition} className="rounded-full border border-white/10 px-3 py-1 text-xs text-slate-300">
                    {condition}
                  </span>
                ))}
              </div>
            </article>
          ))}
        </div>
      </Panel>
    </div>
  )
}

import { useMemo, useState } from 'react'

import FraudReportsTable from '@/components/FraudReportsTable'
import Panel from '@/components/Panel'
import RiskBadge from '@/components/RiskBadge'
import { formatShortTime } from '@/lib/utils'
import { useAppStore } from '@/store/appStore'

export default function FraudReportsPage() {
  const reports = useAppStore((state) => state.reports)
  const [selectedId, setSelectedId] = useState(() => reports[0]?.reportId ?? '')

  const selectedReport = useMemo(
    () => reports.find((report) => report.reportId === selectedId) ?? reports[0],
    [reports, selectedId],
  )

  if (!selectedReport) {
    return <div className="rounded-[28px] border border-white/10 bg-white/5 p-6 text-slate-300">No fraud reports yet.</div>
  }

  return (
    <div className="grid gap-6 xl:grid-cols-[0.95fr_1.05fr]">
      <FraudReportsTable reports={reports} selectedId={selectedReport.reportId} onSelect={setSelectedId} />
      <Panel eyebrow="Evidence Review" title="Investigation Detail">
        <div className="flex flex-wrap items-center gap-3">
          <RiskBadge classification={selectedReport.classification} score={selectedReport.riskScore} />
          <span className="rounded-full border border-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-400">
            {formatShortTime(selectedReport.createdAt)}
          </span>
        </div>
        <div className="mt-6 space-y-5 text-sm text-slate-300">
          <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
            <p className="text-xs uppercase tracking-[0.24em] text-slate-400">Original message</p>
            <p className="mt-3 leading-7 text-white">{selectedReport.messageText}</p>
          </div>
          <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
            <p className="text-xs uppercase tracking-[0.24em] text-slate-400">AI explanation</p>
            <p className="mt-3 leading-7">{selectedReport.aiExplanation}</p>
          </div>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="rounded-3xl border border-cyan-400/20 bg-cyan-400/10 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-cyan-100/80">Recommended action</p>
              <p className="mt-3 leading-7 text-cyan-50">{selectedReport.recommendedAction}</p>
            </div>
            <div className="rounded-3xl border border-rose-500/20 bg-rose-500/10 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-rose-100/80">Evidence score</p>
              <p className="mt-3 font-display text-5xl text-white">{selectedReport.riskScore}</p>
            </div>
          </div>
        </div>
      </Panel>
    </div>
  )
}

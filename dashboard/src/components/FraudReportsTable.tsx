import Panel from '@/components/Panel'
import RiskBadge from '@/components/RiskBadge'
import { formatShortTime } from '@/lib/utils'
import type { FraudReport } from '@/types'

type FraudReportsTableProps = {
  reports: FraudReport[]
  selectedId: string
  onSelect: (reportId: string) => void
}

export default function FraudReportsTable({ reports, selectedId, onSelect }: FraudReportsTableProps) {
  return (
    <Panel eyebrow="Fraud Intelligence" title="Reports Ready For Review">
      <div className="space-y-3">
        {reports.map((report) => (
          <button
            key={report.reportId}
            type="button"
            onClick={() => onSelect(report.reportId)}
            className={`w-full rounded-3xl border p-4 text-left transition hover:border-cyan-400/40 hover:bg-white/6 ${selectedId === report.reportId ? 'border-cyan-300/50 bg-cyan-400/10' : 'border-white/10 bg-white/3'}`}
          >
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="font-medium text-white">{report.name}</p>
                <p className="mt-2 line-clamp-2 text-sm text-slate-300">{report.messageText}</p>
              </div>
              <RiskBadge classification={report.classification} score={report.riskScore} />
            </div>
            <div className="mt-3 flex items-center justify-between text-xs uppercase tracking-[0.2em] text-slate-400">
              <span>Score {report.riskScore}</span>
              <span>{formatShortTime(report.createdAt)}</span>
            </div>
          </button>
        ))}
      </div>
    </Panel>
  )
}

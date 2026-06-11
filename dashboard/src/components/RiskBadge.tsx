import { AlertTriangle, CheckCircle2, ShieldAlert } from 'lucide-react'

import { cn, riskTone } from '@/lib/utils'
import type { RiskClassification } from '@/types'

type RiskBadgeProps = {
  classification: RiskClassification
  score?: number
}

export default function RiskBadge({ classification, score = 0 }: RiskBadgeProps) {
  const icon = classification === 'SCAM' ? ShieldAlert : classification === 'SUSPICIOUS' ? AlertTriangle : CheckCircle2
  const Icon = icon

  return (
    <span className={cn('inline-flex items-center gap-2 rounded-full border px-3 py-1 text-xs font-semibold tracking-wide', riskTone(score))}>
      <Icon className="h-4 w-4" />
      {classification}
    </span>
  )
}

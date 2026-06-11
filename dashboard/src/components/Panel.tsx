import type { ReactNode } from 'react'

import { cn } from '@/lib/utils'

type PanelProps = {
  title?: string
  eyebrow?: string
  className?: string
  children: ReactNode
}

export default function Panel({ title, eyebrow, className, children }: PanelProps) {
  return (
    <section className={cn('rounded-[28px] border border-white/10 bg-white/5 p-6 shadow-[0_24px_80px_rgba(10,15,35,0.35)] backdrop-blur-xl', className)}>
      {(title || eyebrow) && (
        <div className="mb-5">
          {eyebrow ? <p className="text-xs uppercase tracking-[0.25em] text-cyan-200/70">{eyebrow}</p> : null}
          {title ? <h2 className="mt-2 font-display text-2xl text-white">{title}</h2> : null}
        </div>
      )}
      {children}
    </section>
  )
}

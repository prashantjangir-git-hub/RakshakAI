import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

import type { TrendPoint } from '@/types'

type TrendChartProps = {
  data: TrendPoint[]
}

export default function TrendChart({ data }: TrendChartProps) {
  return (
    <div className="h-72 w-full">
      <ResponsiveContainer>
        <AreaChart data={data} margin={{ top: 10, right: 0, left: -24, bottom: 0 }}>
          <defs>
            <linearGradient id="fraudGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#fb7185" stopOpacity={0.75} />
              <stop offset="100%" stopColor="#fb7185" stopOpacity={0} />
            </linearGradient>
            <linearGradient id="sosGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#22d3ee" stopOpacity={0.75} />
              <stop offset="100%" stopColor="#22d3ee" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid vertical={false} stroke="rgba(148,163,184,0.14)" />
          <XAxis dataKey="day" stroke="#94a3b8" tickLine={false} axisLine={false} />
          <YAxis stroke="#94a3b8" tickLine={false} axisLine={false} allowDecimals={false} />
          <Tooltip contentStyle={{ background: '#081225', border: '1px solid rgba(148,163,184,0.2)', borderRadius: 16 }} />
          <Area type="monotone" dataKey="fraud" stroke="#fb7185" strokeWidth={3} fill="url(#fraudGradient)" />
          <Area type="monotone" dataKey="sos" stroke="#22d3ee" strokeWidth={3} fill="url(#sosGradient)" />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  )
}

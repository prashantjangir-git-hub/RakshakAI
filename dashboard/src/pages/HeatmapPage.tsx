import HeatmapPanel from '@/components/HeatmapPanel'
import Panel from '@/components/Panel'
import { useAppStore } from '@/store/appStore'

export default function HeatmapPage() {
  const points = useAppStore((state) => state.heatmap)

  return (
    <div className="grid gap-6 xl:grid-cols-[1.15fr_0.85fr]">
      <Panel eyebrow="Geo Intelligence" title="Risk Heatmap">
        <HeatmapPanel points={points} />
      </Panel>
      <Panel eyebrow="Hotspot Summary" title="Current clusters">
        <div className="space-y-4">
          {points.map((point) => (
            <div key={point.id} className="rounded-3xl border border-white/10 bg-white/5 p-4">
              <div className="flex items-center justify-between gap-3">
                <p className="font-medium text-white">{point.type} hotspot</p>
                <span className="rounded-full border border-white/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-300">
                  intensity {point.intensity}
                </span>
              </div>
              <p className="mt-2 text-sm text-slate-400">{point.latitude.toFixed(4)}, {point.longitude.toFixed(4)}</p>
            </div>
          ))}
        </div>
      </Panel>
    </div>
  )
}

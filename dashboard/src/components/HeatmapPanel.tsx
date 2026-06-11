import { CircleMarker, MapContainer, Popup, TileLayer } from 'react-leaflet'

import type { HeatPoint } from '@/types'

type HeatmapPanelProps = {
  points: HeatPoint[]
}

export default function HeatmapPanel({ points }: HeatmapPanelProps) {
  return (
    <div className="h-[440px] overflow-hidden rounded-[28px] border border-white/10">
      <MapContainer center={[23.027, 72.566]} zoom={13} className="h-full w-full">
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {points.map((point) => (
          <CircleMarker
            key={point.id}
            center={[point.latitude, point.longitude]}
            radius={Math.max(8, Math.round(point.intensity / 9))}
            pathOptions={{
              color: point.type === 'SOS' ? '#22d3ee' : '#fb7185',
              fillColor: point.type === 'SOS' ? '#22d3ee' : '#fb7185',
              fillOpacity: 0.45,
            }}
          >
            <Popup>
              <div className="text-sm">
                <p className="font-semibold">{point.type} hotspot</p>
                <p>Intensity: {point.intensity}</p>
              </div>
            </Popup>
          </CircleMarker>
        ))}
      </MapContainer>
    </div>
  )
}

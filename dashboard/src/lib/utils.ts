import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatShortTime(value: string) {
  const date = new Date(value)
  return date.toLocaleString('en-IN', {
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: '2-digit',
  })
}

export function formatRelativeTime(value: string) {
  const deltaMinutes = Math.max(1, Math.round((Date.now() - new Date(value).getTime()) / 60000))
  if (deltaMinutes < 60) return `${deltaMinutes}m ago`
  const deltaHours = Math.round(deltaMinutes / 60)
  if (deltaHours < 24) return `${deltaHours}h ago`
  return `${Math.round(deltaHours / 24)}d ago`
}

export function riskTone(score: number) {
  if (score >= 75) return 'text-rose-300 bg-rose-500/15 border-rose-500/30'
  if (score >= 40) return 'text-amber-200 bg-amber-500/15 border-amber-500/30'
  return 'text-emerald-200 bg-emerald-500/15 border-emerald-500/30'
}

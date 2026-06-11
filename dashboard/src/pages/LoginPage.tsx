import { ShieldCheck, Smartphone } from 'lucide-react'
import { useState, type FormEvent } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'

import { api, DASHBOARD_SESSION_KEY } from '@/services/api'

export default function LoginPage() {
  const navigate = useNavigate()
  const [phone, setPhone] = useState('9000000001')
  const [otp, setOtp] = useState('123456')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  if (typeof window !== 'undefined' && window.sessionStorage.getItem(DASHBOARD_SESSION_KEY)) {
    return <Navigate to="/" replace />
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setLoading(true)
    setError(null)

    try {
      await api.requestOtp(phone, 'police')
      const session = await api.verifyOtp(phone, otp)
      window.sessionStorage.setItem(DASHBOARD_SESSION_KEY, JSON.stringify(session))
      navigate('/', { replace: true })
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : 'Unable to sign in.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#020816] px-6 py-10 text-slate-100">
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(34,211,238,0.18),_transparent_28%),radial-gradient(circle_at_bottom,_rgba(251,113,133,0.16),_transparent_30%)]" />
      <div className="relative grid w-full max-w-5xl gap-8 rounded-[36px] border border-white/10 bg-slate-950/75 p-8 shadow-[0_30px_120px_rgba(0,0,0,0.5)] backdrop-blur-xl lg:grid-cols-[1.1fr_0.9fr]">
        <section>
          <p className="text-xs uppercase tracking-[0.35em] text-cyan-200/80">RakshakAI</p>
          <h1 className="mt-5 font-display text-5xl leading-tight text-white">A calm command center for urgent moments.</h1>
          <p className="mt-5 max-w-xl text-base text-slate-300">
            Review live SOS cases, detect scam patterns, and protect senior citizens with one coordinated response surface.
          </p>
          <div className="mt-8 grid gap-4 md:grid-cols-2">
            <div className="rounded-[28px] border border-white/10 bg-white/5 p-5">
              <ShieldCheck className="h-8 w-8 text-cyan-300" />
              <p className="mt-4 text-lg font-semibold text-white">Fraud intelligence</p>
              <p className="mt-2 text-sm text-slate-400">High-risk scam reports arrive with simple explanations and evidence context.</p>
            </div>
            <div className="rounded-[28px] border border-white/10 bg-white/5 p-5">
              <Smartphone className="h-8 w-8 text-rose-300" />
              <p className="mt-4 text-lg font-semibold text-white">Emergency coordination</p>
              <p className="mt-2 text-sm text-slate-400">SOS alerts sync from mobile to family and police without friction.</p>
            </div>
          </div>
        </section>

        <section className="rounded-[30px] border border-white/10 bg-white/5 p-6">
          <p className="text-xs uppercase tracking-[0.28em] text-slate-400">Police Login</p>
          <h2 className="mt-4 font-display text-3xl text-white">Secure access</h2>
          <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">Registered police phone</span>
              <input
                value={phone}
                onChange={(event) => setPhone(event.target.value)}
                className="w-full rounded-2xl border border-white/10 bg-slate-950/70 px-4 py-3 text-white outline-none transition focus:border-cyan-300/50"
                placeholder="9000000001"
              />
            </label>
            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">OTP</span>
              <input
                type="password"
                value={otp}
                onChange={(event) => setOtp(event.target.value)}
                className="w-full rounded-2xl border border-white/10 bg-slate-950/70 px-4 py-3 text-white outline-none transition focus:border-cyan-300/50"
                placeholder="123456"
              />
            </label>
            <div className="rounded-2xl border border-cyan-400/20 bg-cyan-400/10 px-4 py-3 text-sm text-cyan-100">
              Demo officer login: `9000000001` with OTP `123456`
            </div>
            {error ? <p className="text-sm text-rose-300">{error}</p> : null}
            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-2xl bg-cyan-300 px-4 py-3 font-semibold text-slate-950 transition hover:bg-cyan-200 disabled:cursor-not-allowed disabled:opacity-70"
            >
              {loading ? 'Verifying...' : 'Enter dashboard'}
            </button>
          </form>
        </section>
      </div>
    </div>
  )
}

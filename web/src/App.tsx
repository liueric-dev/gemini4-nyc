import { useEffect, useState } from 'react'
import './App.css'

type Health = { ok: boolean; missing_keys: string[]; database_built: boolean }

export default function App() {
  const [health, setHealth] = useState<Health | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/api/health')
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`API returned ${r.status}`))))
      .then(setHealth)
      .catch((e: Error) => setError(e.message))
  }, [])

  return (
    <main className="page">
      <h1>Tenant advocate</h1>
      <p className="lede">A photo of the problem and your address. The law it breaks, the deadline, and the next step.</p>
      <section className="status">
        {error && <p>API not reachable: {error}</p>}
        {health && (
          <ul>
            <li>API: running</li>
            <li>Keys: {health.missing_keys.length ? `missing ${health.missing_keys.join(', ')}` : 'all set'}</li>
            <li>Database: {health.database_built ? 'built' : 'not built yet'}</li>
          </ul>
        )}
        {!health && !error && <p>Checking the API…</p>}
      </section>
    </main>
  )
}

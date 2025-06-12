import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Search } from 'lucide-react'
import axios from 'axios'

interface Bus {
  id: number
  model: string
  number: string
  km: number | null
}

const BusList: React.FC = () => {
  const [buses, setBuses] = useState<Bus[]>([])
  const [searchQuery, setSearchQuery] = useState('')
  const [loading, setLoading] = useState(true)
  const [currentPage, setCurrentPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchBuses()
  }, [currentPage, searchQuery])

  const fetchBuses = async () => {
    try {
      setError('')
      console.log('Fetching buses...')
      const response = await axios.get('/api/buses', {
        params: {
          page: currentPage,
          search: searchQuery,
          limit: 12
        }
      })
      console.log('Buses response:', response.data)
      setBuses(response.data.buses || [])
      setTotalPages(response.data.totalPages || 1)
    } catch (error: any) {
      console.error('Error fetching buses:', error)
      setError('Failed to load buses. Please make sure the server is running.')
      setBuses([])
    } finally {
      setLoading(false)
    }
  }

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    setCurrentPage(1)
    fetchBuses()
  }

  if (loading) {
    return <div className="text-center py-8">Зареждане...</div>
  }

  return (
    <div className="px-4">
      <h2 className="text-3xl font-bold text-center mb-8">
        Бусове ({buses.length})
      </h2>

      <form onSubmit={handleSearch} className="mb-8 max-w-md mx-auto">
        <div className="flex">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Търсене по номер..."
            className="form-input rounded-r-none"
          />
          <button
            type="submit"
            className="btn-primary rounded-l-none flex items-center"
          >
            <Search className="h-4 w-4" />
          </button>
        </div>
      </form>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4 text-center">
          {error}
        </div>
      )}

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        {buses.map((bus) => (
          <div key={bus.id} className="card-dark p-6">
            <h5 className="text-xl font-semibold mb-2">
              Модел - {bus.model}
            </h5>
            <p className="text-gray-300 mb-4">
              Номер - {bus.number}
            </p>
            <Link
              to={`/bus/${bus.id}/detail`}
              className="inline-block bg-white text-gray-800 px-4 py-2 rounded hover:bg-gray-100 transition-colors"
            >
              Детайли
            </Link>
          </div>
        ))}
      </div>

      {buses.length === 0 && !error && (
        <p className="text-center text-gray-600">Няма намерени бусове.</p>
      )}

      {totalPages > 1 && (
        <div className="flex justify-center">
          <nav className="flex space-x-2">
            <button
              onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
              disabled={currentPage === 1}
              className="px-3 py-2 border rounded disabled:opacity-50"
            >
              &laquo;
            </button>
            <span className="px-3 py-2">
              Страница {currentPage} от {totalPages}
            </span>
            <button
              onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
              disabled={currentPage === totalPages}
              className="px-3 py-2 border rounded disabled:opacity-50"
            >
              &raquo;
            </button>
          </nav>
        </div>
      )}
    </div>
  )
}

export default BusList
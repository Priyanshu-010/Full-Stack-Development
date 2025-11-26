import Home from './pages/Home'
import Navbar from './components/Navbar'

const App = () => {

  return (
    <div className='min-h-screen bg-gray-600 text-white'>
      <Navbar />
      <Home />
    </div>
  )
}

export default App
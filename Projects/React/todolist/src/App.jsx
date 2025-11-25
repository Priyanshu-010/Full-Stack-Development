import {Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import CreatePage from './pages/CreatePage'
import UpdatePage from './pages/UpdatePage'
import Navbar from './components/Navbar'
const App = () => {
  return (
    <div className='min-h-screen bg-black text-white'>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<CreatePage />} />
        <Route path="/update" element={<UpdatePage />} />
      </Routes>
    </div>
  )
}

export default App
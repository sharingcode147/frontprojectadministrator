
import './App.css'
import {Route, Routes} from 'react-router-dom'
import Home from "./pages/Home.tsx"
import NavBar from "./components/NavBar.tsx"
function App() {
  

    return (
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/navbar" element={<NavBar />} />
      </Routes>
    )
  
}

export default App

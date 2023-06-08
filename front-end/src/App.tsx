
import './App.css'
import {Route, Routes} from 'react-router-dom'
import Home from "./pages/Home"
import Login from "./components/Login"
import NotFound from  "./pages/NotFound"
import Graphs from  "./pages/Graphs"
import { useState } from 'react';
function App() {
    const [token, setToken] = useState('asda');
    if(!token) {
      return <Login setToken={setToken} />
    }
    return (
      
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/graphs" >
          <Route index element={<Graphs />} />
          <Route path=":id" element={<Graphs />} />
        </Route>
        <Route path="*" element={<NotFound />} />
      </Routes>
    )
  
}

export default App

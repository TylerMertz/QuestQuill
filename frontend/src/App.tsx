import './App.css';
import React, {useState, useEffect} from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register'
import Home from './components/Home'
import Cookies from 'js-cookie';
import {ThemeProvider, CssBaseline} from '@mui/material'
import { lightTheme, darkTheme } from './themes';
import Header from './common/Header'

const App: React.FC = () => {

  const [isDarkMode, setIsDarkMode] = useState<boolean>(() => {
    const storedPreference = Cookies.get('darkmode');

    console.log("stored preference", storedPreference)
    return storedPreference ? storedPreference === 'true' : false;
  });

  const toggleTheme = () => {
    const newTheme = !isDarkMode;
    setIsDarkMode(newTheme)
    Cookies.set('darkmode', newTheme.toString(), {expires: 365})
  }

  useEffect(() => {
    const storedPreference = Cookies.get('darkmode')
    if (storedPreference) {
      setIsDarkMode(storedPreference === 'true')
    }
  }, [])

  return (
    <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
    <CssBaseline />
    <Header toggleTheme={toggleTheme} isDarkMode={isDarkMode} />
    <div>
      <Router>
        <Routes>
        <Route path="*" element={<Login />}></Route>
        <Route path="/register" element={<Register />}></Route>
        <Route path="/home" element={<Home />}></Route>
        </Routes>
      </Router>
    </div>
    </ThemeProvider>
  );
};

export default App;

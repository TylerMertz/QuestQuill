import React, { createContext, useContext, useState, ReactNode } from 'react';
import { lightTheme, darkTheme } from './themes';
import { ThemeProvider } from '@mui/material/styles';

interface ThemeContextType {
    isDarkMode: boolean;
    toggleTheme: () => void
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export const useTheme = () => {
    const context = useContext(ThemeContext);
    if (context === undefined) {
        throw new Error('useTheme must be used within a ThemeProviderWrapper');
    }
    return context;
};

export const ThemeProviderWrapper: React.FC<{ children: ReactNode }> = ({children}) => {
    const [isDarkMode, setIsDarkMode] = useState(false);

    const toggleTheme = () => {
        setIsDarkMode(prev => !prev)
    }

    return (
        <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
            <ThemeProvider theme={isDarkMode ? darkTheme : lightTheme}>
                {children}
            </ThemeProvider>
        </ThemeContext.Provider>
    )
}

export default ThemeProviderWrapper
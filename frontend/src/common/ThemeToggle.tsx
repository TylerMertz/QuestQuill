import React from 'react';
import { Switch, FormControlLabel } from '@mui/material';
import { useTheme } from '../ThemeContext'; // Import your custom hook

interface HeaderProps {
    toggleTheme: () => void; //toggle theme
    isDarkMode: boolean;
}

export const ThemeToggle: React.FC<HeaderProps> = ({toggleTheme, isDarkMode}) => {
    // Use the theme context

    return (
        <FormControlLabel
            control={
                <Switch
                    checked={isDarkMode}
                    onChange={toggleTheme}
                    color="primary"
                />
            }
            label={isDarkMode ? 'Dark Mode' : 'Light Mode'}
        />
    );
    };

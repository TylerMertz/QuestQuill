import React from 'react';
import {
    AppBar,
    Toolbar,
    Typography,
    Button,
    IconButton,
    Box,
    useTheme
} from '@mui/material';
import { Menu } from '@mui/icons-material';
import { ThemeContext } from '@emotion/react';
import { ThemeToggle } from './ThemeToggle'


interface HeaderProps {
    toggleTheme: () => void; //toggle theme
    isDarkMode: boolean;
}

const Header: React.FC<HeaderProps> = ({ toggleTheme, isDarkMode}) => {
    return (
        <AppBar position="static">
            <Toolbar>
                <ThemeToggle toggleTheme={toggleTheme} isDarkMode={isDarkMode}></ThemeToggle>
                <Typography variant="h6" noWrap component="div" sx={{ flexGrow: 1, textAlign: 'center' }}>
                    QuestQuill
                </Typography>
                <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Button color="inherit">Account</Button>
                    <Button color="inherit">Sign Out</Button>
                </Box>
            </Toolbar>
        </AppBar>      
    )
}

export default Header;
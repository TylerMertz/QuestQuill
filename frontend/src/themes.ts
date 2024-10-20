import { createTheme } from '@mui/material/styles';

export const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: '#90caf9', // Primary color
        },
        secondary: {
            main: '#ff4081', // Secondary color
        },
        background: {
            default: '#121212', // Background color for dark mode
            paper: '#424242',    // Paper background color for dark mode
        },
        text: {
            primary: '#ffffff',  // Primary text color
            secondary: '#b0bec5', // Secondary text color
        },
    },
})

export const lightTheme = createTheme({
    palette: {
        mode: 'light',
        primary: {
            main: '#3f51b5', // Primary color
        },
        secondary: {
            main: '#ff4081', // Secondary color
        },
        background: {
            default: '#f5f5f5', // Background color for light mode
            paper: '#ffffff',    // Paper background color for light mode
        },
        text: {
            primary: '#333333',  // Primary text color
            secondary: '#666666', // Secondary text color
        },
    },
})
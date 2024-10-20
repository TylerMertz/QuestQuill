import React, { useEffect, useState } from 'react';
import {
    AppBar,
    Toolbar,
    Typography,
    ListItemButton,
    Button,
    CssBaseline,
    Drawer,
    List,
    ListItem,
    ListItemText,
    IconButton,
    Box,
    Container,
} from '@mui/material';
import { Menu } from '@mui/icons-material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'
import Header from '../common/Header'

const drawerWidth = 240;

const Home: React.FC = () => {
    const [open, setOpen] = React.useState(false);

    const token = localStorage.getItem('token')
    const navigate = useNavigate();

    const toggleDrawer = () => {
        setOpen(!open);
    };

    const handleSignOut = () => {
        // Handle sign out logic
        console.log("Signed out");
    };

    useEffect(() => {
        if (token) {
            const fetchUserData = async () => {
                try {
                    const response = await axios.get('http://localhost:8080/users/me', {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    });
                    console.log("Response recieved", response)

                } catch (error) {
                    console.error("Error fetching user data:", error)
                    navigate('/login')
                }
            }

            fetchUserData();
        }
    }, []);

    return (
        <Container>
            
        </Container>
    )
}

export default Home
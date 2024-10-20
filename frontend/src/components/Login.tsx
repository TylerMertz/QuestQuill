import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Box } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'

interface LoginData {
  username: string;
  password: string;
}

const Login: React.FC = () => {
    const [username, setUsername] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [error, setError] = useState<string>('');

    const navigate = useNavigate();

    const handleLogin = async (event: React.FormEvent) => {
        event.preventDefault();

        const loginData: LoginData = { username, password };

        try {
            const response = await axios.post('http://localhost:8080/login', loginData);
            console.log('Login successful:', response.data);
            const token = response.data.access_token
            localStorage.setItem('token', token)
            navigate('/home')
        } catch (err) {
            console.error('Login failed:', err);
            setError('Invalid credentials, please try again.');
        }
    };

    const handleNavigateToRegister = () => {
        navigate('/register')
    }

    return (
    <Container maxWidth="xs">
        <Box
        sx={{
            mt: 8,
            p: 4,
            borderRadius: 2,
        }}
        >
        <Typography variant="h4" gutterBottom align="center">
            Welcome to QuestQuill
        </Typography>

        <form onSubmit={handleLogin}>
            <TextField
            label="Username"
            variant="outlined"
            fullWidth
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            />
            <TextField
            label="Password"
            type="password"
            variant="outlined"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />

            {error && (
            <Typography color="error" align="center">
                {error}
            </Typography>
            )}

            {/* Login Button */}
            <Button
            type="submit"
            variant="contained"
            fullWidth
            onClick={handleLogin}
            >
            Login
            </Button>

            {/* Register Button */}
            <Button
                variant="outlined"
                fullWidth
                onClick={handleNavigateToRegister}  // Navigate to the register page
            >
            Register
            </Button>
        </form>
        </Box>
    </Container>
    );
    };

export default Login;
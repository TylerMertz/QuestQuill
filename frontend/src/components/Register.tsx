import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Box, SlotProps } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'

interface RegisterData {
    email: string;
    password: string;
    username: string;
}

const Register: React.FC = () => {
    const [username, setUsername] = useState<string>('');
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const [confirmPassword, setConfirmPassword] = useState<string>('');
    const [error, setError] = useState<string>('');

    const navigate = useNavigate();


    const handleRegister = async (event: React.FormEvent) => {
        event.preventDefault()

        //Check if passwords match
        if (password !== confirmPassword) {
            setError("Passwords don't match")
            return;
        }

        const registerData: RegisterData = {username, email, password}

        try {
            console.log(registerData)
            const response = await axios.post("http://localhost:8080/register", registerData)
            console.log("Registration Complete.", response)
            navigate("/login")
        } catch (err) {
            console.error("Registration Failed.", err)
            setError("Failed to Register. Please try again.")
        }
    };

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
                    Register
                </Typography>

                <form onSubmit={handleRegister}>
                    <TextField
                        label="Username"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    ></TextField>

                    <TextField
                        label="Email"
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    ></TextField>
 
                    <TextField
                        label="Password"
                        type='password'
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    ></TextField>

                    <TextField
                        label="Confirm Password"
                        type='password'
                        variant="outlined"
                        fullWidth
                        margin="normal"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                    ></TextField>

                    {error && (
                        <Typography color="error" align='center'>
                            {error}
                        </Typography>
                    )}

                    <Button
                        type="submit"
                        variant='contained'
                        fullWidth
                        sx={{
                            mt: 3,
                            backgroundColor: '',
                            ':hover': { backgroundColor: '#3700b3'},
                        }}
                    >
                        Register
                    </Button>
                </form>
            </Box>
        </Container>
    )
}

export default Register
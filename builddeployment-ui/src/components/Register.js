import React, { useState } from 'react';
import '../App.css';
import { BASE_URL } from '../apiConfig';

async function registerUser(credentials) {
    try {
      const response = await fetch('${BASE_URL}/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
      });
  
      if (!response.ok) {
        throw new Error('Registration failed. Please try again.'); // Throw an error if the response is not successful
      }
      return response.json();
    } catch (error) {
      throw new Error('An error occurred. Please try again.'); // Throw a generic error in case of any exceptions
    }
  }
  
  export default function Register({ setToken }) {
    const [username, setUserName] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [error, setError] = useState(null); // Add error state
  
    const handleSubmit = async (e) => {
      e.preventDefault();
  
      try {
        const token = await registerUser({
          username,
          email,
          password
        });
        // Handle the successful response, set token, etc.
      } catch (error) {
        setError(error.message); // Set the error message in the state
      }
    };
  
    return (
      <div className="register-wrapper">
        <h1>Registration Page</h1>
        <form onSubmit={handleSubmit}>
        <label>
          <p>Username</p>
          <input type="text" onChange={e => setUserName(e.target.value)} />
        </label>
        <label>
          <p>Email</p>
          <input type="email" onChange={e => setEmail(e.target.value)} />
        </label>
        <label>
          <p>Password</p>
          <input type="password" onChange={e => setPassword(e.target.value)} />
        </label>
        <div>
          <button type="submit">Submit</button>
        </div>
        </form>
        {error && <div className="error-message">{error}</div>} {/* Display the error message */}
      </div>
    );
  }
  

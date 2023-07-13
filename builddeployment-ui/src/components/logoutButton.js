import React from 'react';
import { useNavigate } from 'react-router-dom';

const LogoutButton = () => {
    const navigate = useNavigate();
  
    const handleLogout = () => {
      console.log("user logging out...")
      navigate('/login');
    };
  
    return (
      <button className="logout-button" onClick={handleLogout}>
        Logout
      </button>
    );
  };
export default LogoutButton;

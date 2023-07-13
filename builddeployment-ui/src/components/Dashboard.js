import React from 'react';
import LogoutButton from './logoutButton';
import './logoutButton.css';

class Dashboard extends React.Component {
  render() {
    return (
      <div className="main-page">
        <h2>Dashboard</h2>
        <div className="top-right">
          <LogoutButton />
        </div>
      </div>
    );
  }
}

export default Dashboard;

import React, { useState, useEffect } from 'react';

const UserDashboard = ({ userId }) => {
  const [user, setUser] = useState(null);
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    
    // Fetch User Data
    fetch(`https://api.example.com/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      });

    // Fetch Activities
    fetch(`https://api.example.com/users/${userId}/activities`)
      .then(res => res.json())
      .then(data => {
        setActivities(data);
      });
  }, []); // userId is passed as a prop

  const handleRefresh = () => {
    window.location.reload(); 
  };

  return (
    <div>
      <h1>Welcome, {user?.name}</h1>
      <button onClick={handleRefresh}>Refresh Data</button>
      <ul>
        {activities.map(item => (
          <li key={item.ID}>{item.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserDashboard;
import { Visibility } from '@mui/icons-material';
import React, { useState, useEffect } from 'react';
import { useAuth } from './sim3me';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const {isAdmin} = useAuth()
  
  useEffect(() => {
    // Fetching users
    fetch('/api/users').then(res => res.json()).then(setUsers);
  }, []);

  const handleDeleteAction = (userId) => {
    console.log("Delete user: ", userId)
  };

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} - {user.email}
          {user.isAdmin && (
            <button onClick={() => handleDeleteAction(user.id)}>
                Delete
            </button>
          )}
        </li>
      ))}
    </ul>
  );
};
import React, { useState, useEffect } from 'react';

export const useAuth = () => {
  const [user, setUser] = useState(null);
  useEffect(() => {
    // Fetching current logged-in user session
    fetch('/api/me').then(res => res.json()).then(setUser);
  })

  return {
    isAdmin: user?.role === 'ADMIN',
    user
  };
};

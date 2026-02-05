import React, { useState, useEffect, useMemo } from 'react';

const SearchComponent = () => {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  // Filter a massive list of local data (10,000+ items)
  const allItems = useMemo(() => {
    return Array.from({ length: 10000 }, (_, i) => ({
      id: i,
      name: `Item ${i}`,
      category: i % 2 === 0 ? 'Even' : 'Odd'
    }));
  }, []);

  useEffect(() => {
    // API Call to log the search query for analytics
    fetch(`https://api.analytics.com/log?q=${query}`);

    // Filtering logic
    const filtered = allItems.filter(item => 
      item.name.toLowerCase().includes(query.toLowerCase())
    );
    
    setResults(filtered);
  }, [query, allItems]);

  const handleChange = (e) => {
    setQuery(e.target.value);
  };

  return (
    <div>
      <input 
        type="text" 
        value={query} 
        onChange={handleChange} 
        placeholder="Search items..." 
      />
      <div>
        {results.map(item => (
          <div key={item.id}>{item.name}</div>
        ))}
      </div>
    </div>
  );
};

export default SearchComponent;
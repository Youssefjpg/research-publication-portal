// This file lets users type in a search term and submit it to the backend.
// It sends the search request to the API and shares the results with the rest of the app.

// src/components/SearchForm.jsx
import { useState } from 'react';
import axios from 'axios';

function SearchForm({ onResults }) {
  const [query, setQuery] = useState('');

  const handleSearch = async () => {
    if (!query) return;

    const response = await axios.post("http://127.0.0.1:5000/pubmed/search", {
      query: query,
      page: 1,
      limit: 10,
      sort: 'relevance'
    });

    onResults(response.data.articles || []);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>
        Search
      </button>
    </div>
  );
}

export default SearchForm;

// src/components/SearchForm.jsx
import { useState } from 'react';
import axios from 'axios';

function SearchForm({ onResults }) {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) return;

    setLoading(true);
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/pubmed/search",
        {
          query: query,
          page: 1,
          limit: 10,
          sort: 'relevance'
        }
      );
      onResults(response.data.articles || []);
    } catch (error) {
      console.error("Error fetching results:", error);
      onResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search"}
      </button>
    </div>
  );
}

export default SearchForm;

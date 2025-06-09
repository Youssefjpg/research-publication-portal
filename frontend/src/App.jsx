import { useState } from 'react';
import axios from 'axios';
import './App.css';
import SearchForm from './components/SearchForm';
import SearchResults from './components/SearchResults';
import ArticleDetail from './components/ArticleDetail';

function App() {
  const [results, setResults] = useState([]);
  const [hasSearched, setHasSearched] = useState(false);
  const [selectedArticle, setSelectedArticle] = useState(null);

  const handleResults = (articles) => {
    setResults(articles);
    setHasSearched(true);
    setSelectedArticle(null); // Clear any previously viewed article
  };

  const handleSelectArticle = async (pmid) => {
    try {
      const response = await axios.get(
        `${import.meta.env.VITE_API_BASE_URL}/pubmed/search/details`,
        {
          params: {
            ids: pmid,
            fields: 'all'
          }
        }
      );

      const articles = response.data.results || [];
      setSelectedArticle(articles[0] || null); // we expect one article only
    } catch (error) {
      console.error("Error fetching article details:", error);
      setSelectedArticle(null);
    }
  };

  return (
    <div className="app-container">
      <h1>PubMed Search</h1>
      <SearchForm onResults={handleResults} />
      <SearchResults
        articles={results}
        hasSearched={hasSearched}
        onSelect={handleSelectArticle}
      />
      <ArticleDetail article={selectedArticle} />
    </div>
  );
}

export default App;


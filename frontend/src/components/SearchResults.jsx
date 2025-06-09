// This file displays a list of search results once the user submits a query.

function SearchResults({ articles, hasSearched }) {
  // If user searched but no results were found
  if (hasSearched && (!articles || articles.length === 0)) {
    return <p>No results found.</p>;
  }

  // when first opening link don'treturn anything from search
  if (!articles || articles.length === 0) {
    return null; 
  }

  return (
    <div className="results-container">
      <h2>Search Results</h2>
      <ul className="results-list">
        {articles.map((article, index) => (
          <li key={index} className="result-item">
            <h3>{article.Title || 'No Title Available'}</h3>
            
            <p><strong>PMID:</strong> {article.PMID || 'Not Available'}</p>
            <p><strong>Publication Year:</strong> {article.PublicationYear || 'Unknown'}</p>
            <p><strong>Journal:</strong> {article.Journal || 'Not Specified'}</p>
            
            <p>
              <strong>Authors:</strong>{' '}
              {article.AuthorList && article.AuthorList.length > 0
                ? article.AuthorList.join(', ')
                : 'No Author Information'}
            </p>
            
            <p>
              <strong>Abstract:</strong>{' '}
              {article.Abstract || 'No Abstract Provided'}
            </p>
            
            <p>
              <strong>MeSH Terms:</strong>{' '}
              {article.MeSHTerms && article.MeSHTerms.length > 0
                ? article.MeSHTerms.join(', ')
                : 'None'}
            </p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SearchResults;

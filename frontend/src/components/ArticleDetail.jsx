// This file shows the full details of a selected article.
// It displays fields like title, abstract, authors, journal, and MeSH terms if available.


function ArticleDetail({ article }) {
  if (!article) return null;

  return (
    <div className="article-detail">
      <h2>Article Details</h2>
      <p><strong>PMID:</strong> {article.PMID || 'N/A'}</p>
      <p><strong>Title:</strong> {article.Title || 'No Title Available'}</p>
      <p><strong>Publication Year:</strong> {article.PublicationYear || 'Unknown'}</p>
      <p><strong>Journal:</strong> {article.Journal || 'N/A'}</p>
      <p>
        <strong>Authors:</strong>{' '}
        {article.AuthorList && article.AuthorList.length > 0
          ? article.AuthorList.join(', ')
          : 'No Authors'}
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
    </div>
  );
}

export default ArticleDetail;

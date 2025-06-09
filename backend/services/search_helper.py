import requests
import math
from .details_helper import fetch_ids_from_pubmed

def search_pubmed_articles(query, page, limit, id_endpoint, detail_endpoint, sort="relevance"):
    retstart = (page - 1) * limit
    params = {
        'db': 'pubmed',
        'term': query,
        'retstart': retstart,
        'retmax': limit,
        'retmode': 'json',
        'sort': sort
    }

    response = requests.get(id_endpoint, params=params)

    if response.status_code != 200:
        return {'total': 0, 'pages': 0, 'articles': []}
    else:
        data = response.json()

        esearch_result = data.get('esearchresult')
        if not esearch_result:
            print("No 'esearchresult' found in PubMed response.")
            return {'total': 0, 'pages': 0, 'articles': []}

        id_list = esearch_result.get('idlist', [])
        total_count = int(esearch_result.get('count', 0))

        total = min(total_count, 9999)
        pages = math.ceil(total / limit)

        articles = fetch_ids_from_pubmed(
            id_list,
            detail_endpoint,
            fields=['PMID', 'Title', 'Abstract', 'AuthorList', 'Journal', 'PublicationYear', 'MeSHTerms']
        )

        return {
            'total': total,
            'pages': pages,
            'articles': articles
        }

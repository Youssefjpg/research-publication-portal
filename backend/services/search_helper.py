import requests
import math
from .details_helper import fetch_ids_from_pubmed


#this is the helper function that takes in user input and returns PubMed articles
def search_pubmed_articles(query, page, limit, id_endpoint, detail_endpoint, sort="relevance"):

    #how many results to skip based on page number & size
    #example: if user is on page 2 and limit is 50 then skip first 50 results
    retstart = (page - 1) * limit

    #parameters sent in the request to PubMed
    params = {
        'db': 'pubmed',
        'term': query,
        'retstart': retstart,
        'retmax': limit,
        'retmode': 'json',
        'sort': sort
    }

    response = requests.get(id_endpoint, params=params) #makes get resquest to Pubmed Esearch and saves the response

    #if the HTTP request fails return empty result
    if response.status_code != 200:
        return {'total': 0, 'pages': 0, 'articles': []} 
    else:
        #parse the JSON response if HTTP request goes through
        data = response.json()
        
        #get the response that contains actual search results
        esearch_result = data.get('esearchresult')

        #if not found return empty result
        if not esearch_result:
            return {'total': 0, 'pages': 0, 'articles': []}
        

        id_list = esearch_result.get('idlist', []) #get list of PubMed articles based on search if not found return empty list

        total_count = int(esearch_result.get('count', 0)) #get total result number based on search if not found return 0

        total = min(total_count, 9999)#result limit based on PubMed Esearch which is 10,000

        pages = math.ceil(total / limit)#how many pages of the result available based on total results found and limit per page

        #calls helper function from details_helper.py to get details about articles for each id found
        articles = fetch_ids_from_pubmed(
            id_list,
            detail_endpoint,
            fields=['PMID', 'Title', 'Abstract', 'AuthorList', 'Journal', 'PublicationYear', 'MeSHTerms']
        )

        #return total number of results, results per page, and detailed article list
        return {
            'total': total,
            'pages': pages,
            'articles': articles
        }

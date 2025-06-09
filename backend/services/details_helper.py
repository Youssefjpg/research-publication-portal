import requests
import xml.etree.ElementTree as ET


# this is the helper function that gets details about articles for each id found
def fetch_ids_from_pubmed(id_list, detail_endpoint, fields=None):
    # return empty list if no result found
    if not id_list:
        return []

    # if no fields specified use all fields
    fields = fields or [
        'PMID', 'Title', 'Abstract', 'AuthorList', 'Journal', 'PublicationYear', 'MeSHTerms'
    ]

    
    params = {
        'db': 'pubmed', 
        'id': ','.join(id_list), #joins ids into one string seperated by commas
        'retmode': 'xml' #response be in xml 
    }

    #sends the GET request to PubMed detail endpoint with above parameters
    response = requests.get(detail_endpoint, params=params)

    ##if the HTTP request fails return empty list
    if response.status_code != 200:
        return []

    #parse xml repsonse
    xml_root = ET.fromstring(response.content)

    publications = [] #this is the return list 

    #iterate over each <PubmedArticle> node in the xml and extracts data from it and saves it in pub dictionary
    for entry in xml_root.findall('.//PubmedArticle'):
        pub = {}

        if 'PMID' in fields or 'all' in fields:
            pub['PMID'] = entry.findtext('.//PMID')

        if 'Title' in fields or 'all' in fields:
            pub['Title'] = entry.findtext('.//ArticleTitle')

        if 'Abstract' in fields or 'all' in fields:
            pub['Abstract'] = entry.findtext('.//AbstractText')

        if 'AuthorList' in fields or 'all' in fields:
            authors = []
            #here does another loop over <AuthorList> 
            # because it has first and last name and extracts them in authors list then adds list to the pub dictionary
            for person in entry.findall('.//Author'):
                first = person.findtext('ForeName') or ''
                last = person.findtext('LastName') or ''
                full_name = f"{first} {last}".strip()
                if full_name:
                    authors.append(full_name)
            pub['AuthorList'] = authors

        if 'Journal' in fields or 'all' in fields:
            pub['Journal'] = entry.findtext('.//Journal/Title')

        if 'PublicationYear' in fields or 'all' in fields:
            pub['PublicationYear'] = entry.findtext('.//PubDate/Year')

        if 'MeSHTerms' in fields or 'all' in fields:
            mesh_terms = []
            for term in entry.findall('.//MeshHeading'):
                descriptor = term.findtext('.//DescriptorName')
                if descriptor:
                    mesh_terms.append(descriptor)
            pub['MeSHTerms'] = mesh_terms

        # Handle missing fields by only appending found ones
        publications.append(pub)

    return publications #returns found publications

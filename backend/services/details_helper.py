import requests
import xml.etree.ElementTree as ET

def fetch_ids_from_pubmed(id_list, detail_endpoint, fields=None):
    # Return early if there's nothing to look up
    if not id_list:
        return []

    # Use all available fields if none are specified
    fields = fields or [
        'PMID', 'Title', 'Abstract', 'AuthorList', 'Journal', 'PublicationYear', 'MeSHTerms'
    ]

    # Set up the request parameters to fetch details from PubMed
    params = {
        'db': 'pubmed',
        'id': ','.join(id_list),
        'retmode': 'xml'
    }

    # Request publication details from PubMed
    response = requests.get(detail_endpoint, params=params)

    if response.status_code != 200:
        return []

    # Convert the response content from XML to an ElementTree object
    xml_root = ET.fromstring(response.content)

    publications = []

    # Iterate on each article in the XML
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

        # Handle missing fields by only including found ones
        publications.append(pub)

    return publications

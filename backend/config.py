import os
from dotenv import load_dotenv


load_dotenv()#this will load the endpoints from the .env file

#two endpoints one for ID and one for DETAIL
PUBMED_ID = os.getenv("PUBMED_ID_ENDPOINT")
PUBMED_DETAIL = os.getenv("PUBMED_DETAIL_ENDPOINT")
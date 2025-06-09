from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from services.search_helper import search_pubmed_articles
from services.details_helper import fetch_ids_from_pubmed
from config import PUBMED_ID, PUBMED_DETAIL


app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    #this is the file that will displayed the message when in the base route Note: the file is stored in the templates folder
    return render_template('index.html')


#POST method that retrieves a list of publication IDs based on a given query.
@app.route('/pubmed/search', methods = ['POST'])
def search():
    data = request.get_json() #reads the material sent in POST request
    query = data.get("query", "")#gets keyword inserted by user or sets to empty string if not provided
    page = int(data.get("page", 1))#gets page number or sets to 1 if not provided
    limit_value = data.get("limit")#gets max number of pages
    limit = int(limit_value) if limit_value is not None else 50 #if not provided with max number of pages sets to 50 if not provided
    sort = data.get("sort", "relevance") #gets sorting method (date, name, etc.) if not provided sets it to be by relevance

    #calls helper function from search_helper.py and using the provided input data above gets matching ids and fetches for articles with those ids
    result = search_pubmed_articles(query, page, limit, PUBMED_ID, PUBMED_DETAIL, sort)
    return jsonify(result) #converts the result to JSON and returns it to frontend


#Get method that fetches for article details using ids
@app.route('/pubmed/search/details', methods = ['GET'])
def details():
    ids = request.args.get('ids', '') #seperate the PubMed ids with commas
    fields = request.args.get('fields', 'all') #gets specified fields if no fields specified returns all fields

    #creates a list from the comma seperated PubMed ids
    id_list = ids.split(',') if ids else []
    field_list = fields.split(',') if fields != 'all' else ['all']

    details = fetch_ids_from_pubmed(id_list, fields=field_list)#calls helper function from details_helper.py to get article details based on id_list
    return jsonify({'results': details})#converts the result to JSON and returns it to client

    
if __name__ == '__main__':
    app.run(debug = True)


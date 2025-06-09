# Research Publication Portal

Youssef Hassan
Monday June 9th, 2025
Email: youssefmostafahassan1@gmail.com

Yale Biomedical Informatics and Data Science
Technical Assessment


# Project Outline

A simple full-stack web app that lets users search PubMed for academic articles. The backend is built with Flask, while the frontend uses React, Vite, and Axios to display article titles, abstracts, authors, and more. Designed to help users quickly find and explore biomedical research publications.


# Paths and Design

. `/backend`: consists of all the backend files and directories.
    .`/services`: consists of two helper functions files for the `POST` and `GET` methods.
        .`details_helper.py`: consists of `GET` method helper function called `fetch_ids_from_pubmed`.
        .`search_helper.py`: consists of `POST` method helper function called `search_pubmed_articles`.
    .`/templates`: includes a basic `index.html` file that displays a message when in the base directory.
        .`index.html`: includes a message for when in the base directory.
    .`app.py`: the main backend file that runs the `GET` and `POST` methods with the help of the helper files and the `config.py` file.
    .`config.py`: loads the ID and DETAIL endpoints from the `.env` file using `load_dotenv()`.
    .`requirements.txt`: the file that includes all the packages need to be installed for the backend.

.`/frontend`: consists of all the frontend files and directories.
    .`/src`: including React, vite, and Axios files.
        .`/components`: consists of the main parts of the frontend.
            .`ArticleDetail.jsx`: displays detailed info. for selected articles.
            .`SearchForm.jsx`: sends search query to backend.
            .`SearchResults.jsx`: displays returned articles.


# Required Installations and Packages

Backend setup:
    . Navigate to the backend directory
        <pre> ```cd backend ``` </pre>
    . Create and activate virtual environment:
        .Mac:
            <pre> ```python3 -m venv venv ``` </pre> creates environment
            <pre> ```source venv/bin/activate ```</pre> activates environment
        .Windows (Command Prompt):
            <pre> ```python -m venv venv ``` </pre> creates environment
            <pre> ```venv\Scripts\activate```</pre> activates environment
    .Install requirements.txt:
            <pre> ```bash pip install -r requirements.txt ``` </pre>

    This installs the following:
        Flask, Flask-CORS, python-dotenv, requests and other packages used internally by Flask

Frontend setup:
<pre> ```bash npm install ``` </pre>


# Ports used

The following ports MUST be available:
    `http://127.0.0.1:5000` for the backend
    `http://localhost:5173/` for the frontend
    

# How to test/run the program

After installing all the packages and making sure that the specified ports are available:
    . Open a new terminal and navigate to `/backend` then activate the virtual environment.
    . Then run the following command <pre> ```python app.py``` </pre> to run the backend section.
    . Open a another seperate terminal and navigate to `/frontend`.
    . Then run the following command <pre> ```npm run dev``` </pre> to run the frontend section.
    . Then open your browser and navigate to `http://localhost:5173/`.
    . Now you can search for biomedical articles from PubMed
    .Example search keywords are: `cancer`, `COVID-19`, or `Alzheimer`












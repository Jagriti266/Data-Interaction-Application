# Data-Interaction-Application
This Python application simulates interaction with a database, processes user queries, and returns relevant data. It demonstrates understanding of natural language processing (NLP), database manipulation, and user input handling.
## Setup and Running

### Prerequisites
- Python 3.x installed on your system
- Installation of required Python packages:
  ```bash
  pip install spacy nltk

### Setup
Clone this repository to your local machine:

Navigate to the project directory: cd data-interaction-application
Download the necessary NLTK resources: python -m nltk.downloader stopwords punkt wordnet
Run the application: python main.py

### Usage 
Upon running the application, you will be prompted to enter a query.
Type your query and press Enter.
The application will process the query and provide relevant data based on the input.

### Intent Recognition Logic
The application recognizes different types of user intents, such as searching for a product by name, searching for products in a specific category, or searching for products within a price range.
It analyzes the query text to identify keywords and entities using spaCy.
Based on the identified entities and keywords, the application determines the user's intent and executes the appropriate database query.

### Query Processing
The application processes user queries by extracting relevant tokens, such as product names, categories, or price ranges.
It then performs the corresponding database query to retrieve relevant information based on the user's intent.

### Application Behavior
The application interprets user input using natural language processing techniques. It analyzes the query to identify the user's intent and then executes the corresponding action to retrieve relevant data from the database.

### External Libraries or Tools Used
spaCy: A Python library for natural language processing. It provides pre-trained models and tools for processing and analyzing text data.
NLTK (Natural Language Toolkit): A leading platform for building Python programs to work with human language data. It provides tools for text processing, tokenization, part-of-speech tagging, and more.
SQLite: A lightweight, serverless, and self-contained SQL database engine. It is used to store and retrieve data in the application's mock database.

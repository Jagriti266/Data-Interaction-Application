# Data-Interaction-Application
This Python application simulates interaction with a database, processes user queries, and returns relevant data. It demonstrates understanding of natural language processing (NLP), database manipulation, and user input handling.

### 1. Setting Up and Running the Application

Prerequisites:

Python (version 3.x recommended)

spaCy library (en_core_web_sm language model)

Google Colab (or a similar environment that supports Python coding)


### Install Libraries:

Open a terminal or command prompt and ensure you have Python installed (check by running python --version).

Install the required libraries using pip:  pip install spacy sqlite3

Download the spaCy language model (en_core_web_sm) used in the code: python -m spacy download en_core_web_sm


Copy the provided Python code  into a new Python file (e.g.,app.py).

Run the Application in Colab: Open Google Colab and upload the app.py file to your notebook.

In a code cell, use the following command to run the application:
Python
!python app.py

### Interact with the Assistant:

The application will prompt you to enter your request.
Type your queries related to product information (e.g., "list available products") or order status (e.g., "check order status for order 123").

The application will use NLP to understand your intent and retrieve information from the in-memory database.


### 2. User Input Interpretation and Data Retrieval

The application utilizes the following functionalities:

### Natural Language Processing (NLP):

spaCy library is used for NLP tasks.

User input is analyzed to identify keywords and sentence structure.

The application attempts to understand the user's intent (e.g., requesting product information, checking order status, or inquiring about service policies).

### In-Memory Database:

The code utilizes an in-memory SQLite database to store product and (optional) order data.

Based on the interpreted user intent, the application executes relevant SQL queries to retrieve data from the database.
For example, if the user asks for a product list, the application queries the products table to retrieve product names and categories.

### Response Generation:

Depending on the retrieved data and the user's intent, the application generates a response that fulfills the user's request.

This might involve displaying product details, order statuses, or informative messages about service policies.

### 3. External Libraries and Tools

spaCy (https://spacy.io/): An open-source library for NLP tasks in Python.

SQLite (https://www.sqlite.org/): A lightweight relational database management system used for the in-memory database in this application (accessed through the sqlite3 Python library).

Google Colab :(https://colab.research.google.com/)

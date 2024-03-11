import spacy
import sqlite3
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')



nlp = spacy.load("en_core_web_sm")


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


conn = sqlite3.connect(':memory:')  # Create an in-memory database for this example
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL
    )
''')

cursor.execute('''
    INSERT INTO products (name, category, price) VALUES
    ('Product A', 'Category 1', 10),
    ('Product B', 'Category 2', 20),
    ('Product C', 'Category 1', 15)
''')
conn.commit()

def process_query(query):
    tokens = word_tokenize(query.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words]
    return tokens

def search_products_by_name(query_tokens):
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    results = []
    for product in products:
        if any(token in product[1].lower() for token in query_tokens):  # product[1] is the name
            results.append(product)
    return results

def search_products_by_category(category):
    cursor.execute('SELECT * FROM products WHERE category=?', (category,))
    return cursor.fetchall()

def search_products_by_price_range(min_price, max_price):
    cursor.execute('SELECT * FROM products WHERE price BETWEEN ? AND ?', (min_price, max_price))
    return cursor.fetchall()

def extract_entities(query):
    doc = nlp(query)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

def handle_query(query):
    # Process the query to extract relevant tokens
    query_tokens = process_query(query)

    # Check for specific keywords in the query to determine intent
    if 'find' in query_tokens and 'product' in query_tokens:
        # Intent: Search for a product by name
        product_name_index = query_tokens.index('product') + 1
        product_name = query_tokens[product_name_index]
        return search_products_by_name([product_name])

    if 'show' in query_tokens and 'products' in query_tokens and 'category' in query_tokens:
        # Intent: Search for products in a specific category
        category_index = query_tokens.index('category') + 1
        category = query_tokens[category_index]
        return search_products_by_category(category)

    if 'find' in query_tokens and 'products' in query_tokens and 'between' in query_tokens:
        # Intent: Search for products within a price range
        between_index = query_tokens.index('between')
        min_price_index = between_index + 1
        max_price_index = query_tokens.index('and', between_index + 1)
        min_price = float(query_tokens[min_price_index])
        max_price = float(query_tokens[max_price_index])
        return search_products_by_price_range(min_price, max_price)

    # Default intent: Search for products by name
    return search_products_by_name(query_tokens)





def main():
    print("Welcome to the Data Interaction Application!")

    while True:
        user_input = input("Please enter your query (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the application.")
            break

        try:
            # Handle the user query
            results = handle_query(user_input)
            if results:
                print("Found matching products:")
                for result in results:
                    print(f"Product: {result[1]}, Category: {result[2]}, Price: ${result[3]}")
            else:
                print("No matching products found.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

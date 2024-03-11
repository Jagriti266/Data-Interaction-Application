import sqlite3
import spacy

nlp = spacy.load("en_core_web_sm")

# Connect to an in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
# Create the products and orders tables (if they don't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  category TEXT,
  price REAL NOT NULL
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_name TEXT NOT NULL,
  status TEXT NOT NULL
);''')


def query_app(user_input):
  """
  Queries the in-memory SQL database based on user intent derived from NLP analysis.

  Args:
      user_input (str): Textual input from the user.

  Returns:
      str: Information retrieved from the database based on user intent.
  """
  doc = nlp(user_input)

  # Sample data 
  cursor.execute("INSERT INTO products (name, description, category, price) VALUES (?, ?, ?, ?)", ("T-Shirt", "Comfortable cotton T-Shirt", "Clothing", 19.99))
  cursor.execute("INSERT INTO products (name, description, category, price) VALUES (?, ?, ?, ?)", ("Laptop", "High-performance laptop for work and play", "Electronics", 799.99))
  cursor.execute("INSERT INTO products (name, description, category, price) VALUES (?, ?, ?, ?)", ("Headphones", "Noise-cancelling headphones for immersive sound", "Electronics", 99.99))
  cursor.execute("INSERT INTO orders (customer_name, status) VALUES (?, ?)", ("John Doe", "Shipped"))
  cursor.execute("INSERT INTO orders (customer_name, status) VALUES (?, ?)", ("Jane Smith", "Processing"))
  conn.commit()  # Commit the data insertion

  # Check for information requests
  if any(token.text.lower() in ["list", "show", "browse"] for token in doc):
    cursor.execute("SELECT name, category FROM products")
    products = cursor.fetchall()
    product_list = "\n".join([f"{name} ({category})" for name, category in products])
    return f"Available products:\n{product_list}"

  # Check for order status inquiries
  elif any(token.text.lower() in ["order", "status"] for token in doc):
    # Find order ID mentioned in the sentence 
    order_id = None
    for entity in doc.ents:
      if entity.label_ == "ORDINAL":
        order_id = int(entity.text)
    # Search for order details using order ID
    if order_id:
      cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
      status = cursor.fetchone()
      if status:
        return f"Order Status: {status[0]}"
      else:
        return f"Order ID {order_id} not found."
    else:
      return "Please provide your order ID to check the status."

  # Check for service inquiries 
  elif any(token.text.lower() in ["return", "warranty", "shipping"] for token in doc):
    service = user_input.lower().split()[1]
    return f"For information about our {service} policy, please visit our Help Center."
  # No matching intent
  else:
    return "Sorry, I couldn't understand your request."

while True:
  user_input = input("Enter your request (or 'quit' to exit): ")
  if user_input.lower() == "quit":
    break
  response = query_app(user_input)
  print(response)



print("Exiting...")
   

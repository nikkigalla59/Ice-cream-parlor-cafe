# Ice-cream-parlor-cafe


## Description
A simple Python application for a fictional ice cream parlor cafe that uses SQLite to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions and allergy concerns.

## Getting Started

### Prerequisites
- Python 3.x installed on your system
- SQLite database installed on your system
* A love for ice cream

### Installation
1. Clone the repository:
   
   git clone https://github.com/nikithagalla/ice-cream-parlor-cafe.git
  
2. Navigate to the project directory:
 
   cd ice-cream-parlor-cafe

3. Install the required packages:
 
   pip install -r requirements.txt
 

## Running the Application

1. Run the application:
  
   python app.py
   
2. Follow the prompts to interact with the application

### Running with Docker
1. Build the Docker image:
  
   docker build -t ice-cream-parlor-cafe .
   
2. Run the Docker container:
   
   docker run -p 5000:5000 ice-cream-parlor-cafe

3. Open a web browser and navigate to `http://localhost:5000` to access the application.

4. To stop the Docker container:
   
   docker stop ice-cream-parlor-cafe

5. To remove the Docker container:
  
   docker rm ice-cream-parlor-cafe


## Usage

### Maintain a Cart of Favorite Products
- Add products to your cart using the `add_to_cart` command
- View your cart using the `view_cart` command
- Remove products from your cart using the `remove_from_cart` command

### Search and Filter Offerings
- Search for products by name using the `search` command
- Filter products by category using the `filter` command

### Add Allergens
- Add a new allergen using the `add_allergen` command
- View all allergens using the `view_allergens` command

## Test Steps

To validate the application, follow these steps:

1. Run the application and add a few products to the cart
2. Search for a product by name and verify it appears in the search results
3. Filter products by category and verify only products in that category are shown
4. Add a new allergen and ensure it is listed among the allergens
5. Remove a product from the cart and verify it is no longer listed in the cart

## SQL Query or ORM Abstraction Implementation

The application uses the `sqlite3` library to interact with the SQLite database. SQL queries are executed using the `cursor.execute()` method.


## Docker File

The Dockerfile is located in the root of the repository. To build the Docker image, run:

docker build -t ice-cream-parlor-cafe .


## Authors

Nikitha Galla

## Acknowledgments

Thanks to the Python and SQLite communities for their support and resources.
Special thanks to the ice cream enthusiasts who inspired this project!

Django Restaurant Management API 

**Introduction** 

Django Restaurant Management API is a web service for managing restaurants, menus, and orders. This API provides functionality to create, read, update, and delete data related to users, restaurants, menus, items, and orders.

**Installation** 

1. Create virtual environment: Python -m venv env 
1. Activate virtual environment: .\env\scripts\activate 
1. Clone the repository:

   git clone [https://github.com/abdullahaltushar/restaurant-management-api.git  ](https://github.com/abdullahaltushar/restaurant-management-api.git)

4. Install dependencies: 

   pip install -r requirements.txt 

5. Apply migrations: 

   python manage.py migrate

**Models User Model** 

The CustomUser model extends Django's AbstractUser and includes additional fields for profile pictures and phone numbers.

- email: Email address of the user.
- username: Username of the user.

**Restaurant Model** 

The Restaurant model represents a restaurant and includes information about its name, owner, and address.

- name: Name of the restaurant.
- owner: Owner of the restaurant (linked to CustomUser).
- address: Address of the restaurant.

**Menu Model** 

The Menu model represents a menu belonging to a specific restaurant.

- restaurant: Restaurant to which the menu belongs (linked to Restaurant).
- name: Name of the menu.

**Item Model** 

The Item model represents a menu item with details such as name and price.

- menu: Menu to which the item belongs (linked to Menu).
- name: Name of the item.
- price: Price of the item.

**Order Model** 

The Order model represents an order placed by a user and includes information about the user, items, quantity, and total price.

- user: User who placed the order (linked to 
- items: Items included in the order (linked to 
- quantity: Quantity of items in the order.
- total\_price: Total price of the order

CustomUser).

Item).

**Serializers User Serializer** 

The CustomUserSerializer serializes the CustomUser model and includes fields for basic user information.

- id: User ID.
- username: Username of the user.
- email: Email address of the user.

**Restaurant Serializer** 

The RestaurantSerializer serializes the Restaurant model. 

- id: Restaurant ID.
- name: Name of the restaurant.
- owner: Owner of the restaurant.
- address: Address of the restaurant.

**Menu Serializer** 

The MenuSerializer serializes the Menu model. 

- id: Menu ID.
- restaurant: Restaurant to which the menu belongs.
- name: Name of the menu.

**Item Serializer** 

The ItemSerializer serializes the Item model. 

- id: Item ID.
- menu: Menu to which the item belongs.
- name: Name of the item.
- price: Price of the item.

**Order Serializer** 

The OrderSerializer serializes the Order model. 

- id: Order ID.
- user: User who placed the order.
- items: Items included in the order.
- quantity: Quantity of items in the order.
- total\_price: Total price of the order.

**Views User Views** 

- UserList: List all users or create a new user.
- UserDetail: Retrieve, update, or delete a specific user.

**Restaurant Views** 

- RestaurantList: List all restaurants or create a new restaurant.
- RestaurantDetail: Retrieve, update, or delete a specific restaurant.
- MenuList: List all menus or create a new menu.
- MenuDetail: Retrieve, update, or delete a specific menu.
- ItemList: List all items or create a new item.
- ItemDetail: Retrieve, update, or delete a specific item.

**Order Views** 

- OrderList: List all orders or create a new order.
- OrderDetail: Retrieve, update, or delete a specific order.

**URLs** 

- /api/users/: Endpoint for listing all users and creating a new user.
- /api/users/<int:pk>/: Endpoint for retrieving, updating, or deleting a specific 

  user.

- /api/restaurants/: Endpoint for listing all restaurants and creating a new restaurant.
- /api/restaurants/<int:pk>/: Endpoint for retrieving, updating, or deleting a 

  specific restaurant.

- /api/menus/: Endpoint for listing all menus and creating a new menu.
- /api/menus/<int:pk>/: Endpoint for retrieving, updating, or deleting a specific 

  menu.

- /api/items/: Endpoint for listing all items and creating a new item.
- /api/items/<int:pk>/: Endpoint for retrieving, updating, or deleting a specific 

  item.

- /api/orders/: Endpoint for listing all orders and creating a new order.
- /api/orders/<int:pk>/: Endpoint for retrieving, updating, or deleting a specific 

  order.

**Running the Application** 

To run the application, use the following command:

python manage.py runserver

**Thank you .** 

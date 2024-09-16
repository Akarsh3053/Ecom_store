# E-commerce Store 
A simple E-commerce store app with a robust Django backend and a responsive frontend built using NextJs

## Backend 
It uses Django and SQL for implementing backend API endpoints, models, and user authentication.

### Models 
- User
- Product
- Order
- Cart

### API endpoints
- User registration, login, and logout.
- Viewing product list and product details.
- Adding products to the cart.
- Checking out and creating orders.


## Frontend
The front end of this app is built using NextJS with Redux for state management and Tailwind for styling.

### Features 
- Modern and user-friendly UI
- Separate pages using the app router
- Tailwind styling for easy customization
- Redux toolkit for State-Management


## Setup
- Clone the repository
```bash
git clone https://github.com/Akarsh3053/Ecom_store
```
### Setup Backend Server
- Move into the backend directory and install the dependencies
```bash
pip install requirements.txt
```
- Add SQL credentials to ```/store_backend/settings.py```
- Run migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
- Run the backend Django server
```bash
python manage.py runserver
```
-The server should now be running at ```localhost:8000```

### Setup Frontend application
- Move to front end directory and install dependencies
```bash
npm install
```
- Run the development server
```bash
npm run dev
```
- Your app will be running at ```localhost:3000```

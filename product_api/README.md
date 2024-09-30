# E-Commerce Product API

```
pip install -r requirements.txt
```

## Overview

This E-Commerce Product API is a backend solution built with Django and Django REST Framework. It provides a robust set of endpoints for managing products on an e-commerce platform, including user authentication, product management (CRUD operations), and search functionality.

## Features

1. **Product Management (CRUD)**
   - Create, Read, Update, and Delete products
   - Product attributes: Name, Description, Price, Category, Stock Quantity, Image URL, Created Date
   - Automatic stock reduction when an order is placed (optional/future enhancement)

2. **User Management (CRUD)**
   - CRUD operations for users
   - User attributes: Username, Email, Password
   - Authentication required for product management

3. **Product Search**
   - Search products by Name or Category
   - Partial name matching
   - Paginated search results

4. **Product View**
   - List all products or view individual product details
   - Optional filters: Category, Price Range, Stock Availability

## Technical Details

- **Database**: Django ORM with models for Products and Users
- **Authentication**: Django's built-in authentication system
- **API Design**: RESTful principles using Django Rest Framework
- **Deployment**: PythonAnywhere
- **Additional Features**: Pagination and filtering for product listings

## Optional Enhancements

- Product Reviews system
- Advanced Category Management
- Multiple Product Images support

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your database in `settings.py`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## API Documentation

Access the API documentation at: `https://dogtorken.pythonanywhere.com/api/`

## Deployment

This API is deployed on [PythonAnywhere]. Access it at: `https://dogtorken.pythonanywhere.com/api/`

## Contributors

[Kenward Uma Terhemba]

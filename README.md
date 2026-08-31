# Restaurant Kitchen Service

A Django web application for managing a restaurant kitchen: dish types, dishes, and cooks. It helps organize the kitchen's workflow by keeping track of what dishes are on the menu, which category each dish belongs to, and which cooks are responsible for preparing them.

![login.png](doc%2Fpages%2Flogin.png)

![home.png](doc%2Fpages%2Fhome.png)

![coks.png](doc%2Fpages%2Fcoks.png)

![create_cook.png](doc%2Fpages%2Fcreate_cook.png)

![detail_cook.png](doc%2Fpages%2Fdetail_cook.png)

![update_cook.png](doc%2Fpages%2Fupdate_cook.png)

![dishes.png](doc%2Fpages%2Fdishes.png)

![create_dish.png](doc%2Fpages%2Fcreate_dish.png)

![dish_types.png](doc%2Fpages%2Fdish_types.png)

## Features

`login: admin`
`password: 1234qwer`

- User authentication (login / logout)
- **Dish Types** — create and browse dish categories (e.g. Pasta, Desserts, Curries)
- **Dishes** — create and browse dishes with name, description, price, dish type, and assigned cooks
- **Cooks** — create and browse cooks with years of experience
- Search by name on list pages
- Bootstrap-based responsive interface

## Database Structure

![img.png](doc/img.png)

The project is built around three main models:

- **DishType** — `name`
- **Dish** — `name`, `description`, `price`, `dish_type` (FK to DishType), `cooks` (M2M to Cook)
- **Cook** (extends `AbstractUser`) — `years_of_experience`, standard user fields (`username`, `email`, `password`, `first_name`, `last_name`)

## Installation

Python 3 must already be installed.

```bash
git clone https://github.com/<your-username>/restaurant-kitchen.git
cd restaurant-kitchen

python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

The application will be available at `http://localhost:8000/`.

## Creating a superuser

```bash
python manage.py createsuperuser
```

Use the created credentials to log in and access `/admin/` or the app's authenticated pages.

## Loading sample data (optional)

If a fixture file is provided:

```bash
python manage.py loaddata kitchen_db_data.json
```

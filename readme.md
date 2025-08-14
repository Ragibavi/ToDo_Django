# ToDoAPI

## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

* **Python 3.9+**
* **Django 5.x+**
* **Django REST Framework 3.x+**

### Installation

Follow these steps to set up the project locally.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Ragibavi/ToDo_Django.git](https://github.com/Ragibavi/ToDo_Django.git)
    cd ToDo_Django
    ```

2.  **Create a virtual environment:**

    **Mac/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **Windows (CMD):**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
    The server will be running at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## API Endpoints

The API is structured into two main resources: **Users** and **Todos**. All endpoints support JSON data.

### Users

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/users/` | List all users |
| `POST` | `/api/users/` | Create a new user |
| `GET` | `/api/users/{id}/` | Get user by UUID |
| `PUT` | `/api/users/{id}/` | Update a user |
| `DELETE`| `/api/users/{id}/` | Delete a user |

### Todos

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/todos/` | List all todos |
| `POST` | `/api/todos/` | Create a new todo |
| `GET` | `/api/todos/{id}/` | Get todo by UUID |
| `PUT` | `/api/todos/{id}/` | Update a todo |
| `DELETE`| `/api/todos/{id}/` | Delete a todo |
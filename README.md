Certainly! Here's the README content in Markdown format that you can directly paste into your `README.md` file:

```markdown
# Django Users App with Djoser for Token Authentication

## Overview

This Django application demonstrates how to set up token authentication using Djoser and a custom user model named "User" in the "users" app.

## Prerequisites

- Python 3.x
- Django
- Djoser

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/django-users-djoser-token-auth.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://localhost:8000/](http://localhost:8000/)

## Djoser Configuration

The Djoser configuration is set up in the `settings.py` file within the "users" app. Ensure that the following configurations are correctly set:

```python
INSTALLED_APPS = [
    # ...
    'djoser',
    'users',
    # ...
]

# ...

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'users.serializers.CustomUserCreateSerializer',
        'user': 'users.serializers.CustomUserSerializer',
        'token_create': 'djoser.serializers.TokenCreateSerializer',
    },
    # Other Djoser settings...
}
```

## Usage

1. **User Registration:**

   Endpoint: `/auth/users/`

   Use a POST request with the following payload:

   ```json
   {
       "email": "user@example.com",
       "password": "yourpassword",
       "first_name": "John",
       "last_name": "Doe",
       "bio": "A brief bio",
       "date_of_birth": "1990-01-01"
   }
   ```

2. **User Login:**

   Endpoint: `/auth/token/login/`

   Use a POST request with the following payload:

   ```json
   {
       "email": "user@example.com",
       "password": "yourpassword"
   }
   ```

   The response will include an access token.

3. **Access Protected Endpoints:**

   Include the access token in the Authorization header to access protected endpoints.

   ```bash
   curl -H "Authorization: Token <your-access-token>" http://localhost:8000/protected-endpoint/
   ```

4. **Superuser Access:**

   Superuser credentials can be used to access all endpoints and perform administrative actions.

## Custom User Model

The custom user model is defined in `users/models.py`. Ensure that the `AUTH_USER_MODEL` setting in `settings.py` is correctly set to `'users.User'`.

```python
# settings.py
AUTH_USER_MODEL = 'users.User'
```

## Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace "yourusername" with your actual GitHub username in the clone URL, and customize the file paths, payload examples, and other details according to your specific application.
# Contact Management API
___

## Project Description

This project is a Django-based contact management system with OAuth2
authentication and regional access control. It provides a RESTful
API for managing contacts with secure access controls and country-basedIP restrictions.

### Key Features
- REST API for CRUD operations on contacts
- Google OAuth2 authentication
- IP-based access restriction by country
- Django REST Framework for API development
- Detailed API documentation

## Prerequisites
Before running the project, ensure you have:

- Python 3.x
- pip (Python package manager)
- A Google Cloud Platform account (for OAuth2)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sergey-Chalyi/djangoRESTFramework_APIForContacts.git
   cd djangoRESTFramework_APIForContacts
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Google OAuth2:
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Google Sign-In API
   - Create OAuth2 credentials (Web application type)
   - Add authorized redirect URIs:
     ```
     http://localhost:8000/social-auth/complete/google-oauth2/
     ```

5. Create `.env` file in the project root:
   ```
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth2_key
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth2_secret
   TEST_IP_ADDRESS=your_test_ip_address
   ```

6. Configure regional restrictions:
   - Update `ALLOWED_COUNTRIES` in `base/settings.py` (default: ['UA', 'PL'])
   - The project uses *ipapi.co* for geolocation

7. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Project
1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application:
   - Web Interface: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`

## API Documentation

### Authentication
All API endpoints require authentication. The project supports:
- Google OAuth2
- Session authentication for web interface

### Endpoints

#### Contacts API
| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|------------------------|
| GET    | `/api/v1/contacts/` | List all contacts | Yes |
| POST   | `/api/v1/contacts/` | Create a new contact | Yes |
| GET    | `/api/v1/contacts/{id}/` | Get contact details | Yes |
| PUT    | `/api/v1/contacts/{id}/` | Update a contact | Yes |
| DELETE | `/api/v1/contacts/{id}/` | Delete a contact | Yes |

#### Authentication Endpoints
| Endpoint | Description |
|----------|-------------|
| `/login/` | Login page |
| `/logout/` | Logout endpoint |
| `/social-auth/login/google-oauth2/` | Google OAuth2 login |


## Development

## Security Considerations
- The project uses environment variables for sensitive data
- IP-based access restrictions are implemented
- OAuth2 authentication is required for all API endpoints


## Contact
For questions and support:
- Email: supersupergray@gmail.com
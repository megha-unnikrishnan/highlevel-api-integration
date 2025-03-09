# HighLevel API Integration with Django

## 🚀 Overview

This project integrates Django with the HighLevel API to manage contacts, custom fields, and authentication using OAuth2.

## 📌 Features

  - OAuth Authentication: Securely authenticate with HighLevel API.

  - Retrieve Contacts: Fetch all contacts or a random contact.

  - Update Contact Custom Fields: Modify a specific field for a randomly selected contact.

  - Retrieve Custom Field ID: Fetch the ID for a custom field.

## 🛠️ Setup

  ### 🔹 Prerequisites

  - Python 3.x

  - Django

  - requests library (install using pip install requests)

### 🔹 Installation Steps

  1. Clone the Repository

     - git clone https://github.com/megha-unnikrishnan/highlevel-api-integration.git
       
       - cd highlevel-api-integration
      
  2. Create and Activate Virtual Environment

     - python -m venv venv
       
     - source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
  3. Install Dependencies

     - pip install -r requirements.txt
    
  4. Configure Environment Variables

     - CLIENT_ID=your_client_id
       
     - CLIENT_SECRET=your_client_secret
    
     - REDIRECT_URI=https://your_redirect_url.com
    
     - LOCATION_ID=your_location_id
    
  5. Run the Django Server

     - python manage.py runserver

### 🔑 Authentication Flow  

  1. The user is redirected to the authorization URL.

  2. After granting access, the system receives an authentication code.

  3. The authentication code is exchanged for an access token.

  4. The access token is stored in the session for making API requests.

### ⚡ API Endpoints

| **Endpoint**               | **Method** | **Description**                                    |
|----------------------------|-----------|----------------------------------------------------|
| `/get-auth-code/`          | GET       | Redirects user to get auth code                   |
| `/get-access-token/`       | POST      | Exchanges auth code for access token              |
| `/get-all-contacts/`       | GET       | Retrieves all contacts                            |
| `/get-random-contact/`     | GET       | Retrieves a random contact                        |
| `/update-random-contact/`  | PUT       | Updates a random contact                          |



### 📝 Notes

- Ensure your API credentials are correct before making requests.

- The OAuth flow must be completed before calling authenticated endpoints.

- Keep your CLIENT_SECRET secure and never expose it in public repositories.


from django.shortcuts import redirect
import requests
import json

# API Credentials
CLIENT_ID = "65c0a9a4277b2961322c545a-ls8q934d"
CLIENT_SECRET = "94af4663-c0c7-4340-9ce5-39b38e88c146"
REDIRECT_URI = "https://google.com"


def get_auth_code(request):
    
    scope = "contacts.readonly+contacts.write"

    

 
    auth_url = (
        f"https://marketplace.gohighlevel.com/oauth/chooselocation?"
        f"response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={scope}"
    )
    
    
    print("Authorization URL:", auth_url)  # Debugging
    return redirect(auth_url)


def get_access_token(auth_code):
    url = "https://services.leadconnectorhq.com/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "redirect_uri": REDIRECT_URI
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"  # ✅ Ensures correct format
    }
    print("🔄 Sending Access Token Request...")

    
    response = requests.post(url, data=payload, headers=headers)  # ✅ Use `data=payload`

    print(f"🔄 Access Token Response: {response.status_code} {response.text}")

    return response.json()









from django.http import JsonResponse

import random
from django.http import JsonResponse
import requests





from django.http import JsonResponse
import requests

def get_all_contacts(request):
    access_token = request.session.get('access_token')  # ✅ Get token from session
    location_id = "k1F38z3A0efRMHeVkk3v"  # Replace with your actual locationId

    if not access_token:
        return JsonResponse({"error": "Missing access token. Please authenticate first."}, status=401)

    url = f"https://services.leadconnectorhq.com/contacts/?locationId={location_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",  # ✅ Use the correct API version from documentation
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("Contacts API Response:", response.status_code, response.text)  # Debugging output

    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch contacts", "details": response.json()}, status=response.status_code)

    contacts = response.json().get("contacts", [])

    if not contacts:
        return JsonResponse({"error": "No contacts found"}, status=404)

    # ✅ Return all contacts as a JSON response
    return JsonResponse({"contacts": contacts}, safe=False)




def get_random_contact(request):
    access_token = request.session.get('access_token')  # ✅ Get token from session
    location_id = "k1F38z3A0efRMHeVkk3v"  # Replace with your actual locationId

    if not access_token:
        return JsonResponse({"error": "Missing access token. Please authenticate first."}, status=401)

    url = f"https://services.leadconnectorhq.com/contacts/?locationId={location_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",  # ✅ Use the correct API version from documentation
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    print("Contacts API Response:", response.status_code, response.text)  # Debugging output
    
    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch contacts", "details": response.json()}, status=response.status_code)

    contacts = response.json().get("contacts", [])

    if not contacts:
        return JsonResponse({"error": "No contacts found"}, status=404)

    # ✅ Select a random contact
    random_contact = random.choice(contacts)

    return JsonResponse({
        "random_contact_id": random_contact["id"],
        "name": random_contact.get("name", "Unknown"),
        "email": random_contact.get("email", "No Email"),
        "phone": random_contact.get("phone", "No Phone")
    })



import requests



import random



import requests
from django.http import JsonResponse

def get_custom_field_id(request):
    access_token = request.session.get('access_token')  
    location_id = "k1F38z3A0efRMHeVkk3v"  

    if not access_token:
        return JsonResponse({"error": "Missing access token. Please authenticate first."}, status=401)

    url = f"https://services.leadconnectorhq.com/custom-fields?locationId={location_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2023-01-01",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    # ✅ Debugging: Check the actual response
    print("API Response Status Code:", response.status_code)
    print("API Response Content:", response.text)  # Print full response

    if response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch custom fields", "status_code": response.status_code})

    try:
        response_json = response.json()  # ✅ Try parsing JSON
    except requests.exceptions.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON response from API", "raw_response": response.text}, status=500)

    custom_fields = response_json.get("customFields", [])

    if not custom_fields:
        return JsonResponse({"error": "No custom fields found"}, status=404)

    field_id = next((field["id"] for field in custom_fields if field["name"] == "DFS Booking Zoom Link"), None)

    if not field_id:
        return JsonResponse({"error": "Custom field not found"}, status=404)

    return JsonResponse({
        "custom_field_name": "DFS Booking Zoom Link",
        "custom_field_id": field_id
    })







def update_random_contact(request):
    access_token = request.session.get('access_token')  # ✅ Get token from session
    location_id = "k1F38z3A0efRMHeVkk3v"  # ✅ Your actual locationId

    if not access_token:
        return JsonResponse({"error": "Missing access token. Please authenticate first."}, status=401)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",
        "Accept": "application/json"
    }

    # ✅ Step 1: Fetch Custom Fields
    custom_fields_url = f"https://services.leadconnectorhq.com/custom-fields/?locationId={location_id}"
    custom_fields_response = requests.get(custom_fields_url, headers=headers)

    if custom_fields_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch custom fields", "details": custom_fields_response.json()}, status=custom_fields_response.status_code)

    custom_fields = custom_fields_response.json().get("customFields", [])

    # ✅ Find the ID for "DFS Booking Zoom Link"
    custom_field_id = None
    for field in custom_fields:
        if field.get("name") == "DFS Booking Zoom Link":
            custom_field_id = field.get("id")
            break

    if not custom_field_id:
        return JsonResponse({"error": "Custom field 'DFS Booking Zoom Link' not found"}, status=404)

    # ✅ Step 2: Fetch Contacts
    contacts_url = f"https://services.leadconnectorhq.com/contacts/?locationId={location_id}"
    contacts_response = requests.get(contacts_url, headers=headers)

    if contacts_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch contacts", "details": contacts_response.json()}, status=contacts_response.status_code)

    contacts = contacts_response.json().get("contacts", [])

    if not contacts:
        return JsonResponse({"error": "No contacts found"}, status=404)

    # ✅ Step 3: Select a Random Contact
    random_contact = random.choice(contacts)
    contact_id = random_contact["id"]

    # ✅ Step 4: Update the Contact's Custom Field
    update_url = f"https://services.leadconnectorhq.com/contacts/{contact_id}"
    update_data = {
        "customFields": [{"id": custom_field_id, "value": "TEST"}]
    }

    update_headers = {
        "Authorization": f"Bearer {access_token}",
        "Version": "2021-07-28",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    update_response = requests.put(update_url, headers=update_headers, json=update_data)

    if update_response.status_code != 200:
        return JsonResponse({"error": "Failed to update contact", "details": update_response.json()}, status=update_response.status_code)

    return JsonResponse({
        "message": "Contact updated successfully",
        "contact_id": contact_id,
        "custom_field_updated": "DFS Booking Zoom Link",
        "updated_value": "TEST"
    })


def update_highlevel_contact(request):
    auth_code = request.GET.get("code")  # Get auth code from URL after redirect
    if not auth_code:
        return get_auth_code(request)  # Redirect to authorization if no code

    token_data = get_access_token(auth_code)
    access_token = token_data.get("access_token")

    if not access_token:
        return JsonResponse({"error": "Failed to get access token"})

    # ✅ Store token in session
    request.session["access_token"] = access_token
    request.session.modified = True
    request.session.save()  # ✅ Ensure session saves

    # ✅ Print Access Token to Terminal
    print("\n🔑 Access Token Received:", access_token, "\n")

    return JsonResponse({"message": "Access token stored successfully", "access_token": access_token})




def debug_session(request):
    request.session["test"] = "Session works!"  # Setting a test session value

    # Retrieve access token from session
    access_token = request.session.get("access_token", "No access token found")

    # Print the access token for debugging
    print("Stored Access Token:", access_token)

    return JsonResponse({
        "message": "Session set!",
        "session_data": dict(request.session),
        "access_token": access_token  # Include access token in response
    })










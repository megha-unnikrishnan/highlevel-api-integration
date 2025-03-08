from django.urls import path




from django.urls import path
from .views import get_auth_code, get_random_contact, get_custom_field_id,debug_session,update_highlevel_contact,update_random_contact,get_all_contacts
# from .views import update_random_contact
urlpatterns = [
    path("login/", get_auth_code),  # Redirect to OAuth login
    path('get-all-contacts/',get_all_contacts),
    path("get-contact/", get_random_contact),  # Fetch a random contact
    path("custom-field/", get_custom_field_id),  # Update contact field
    path("debug-session/", debug_session),
    path("oauth/callback/", update_highlevel_contact),  # Callback after authorization
    path("update-contact/",update_random_contact)


    
]



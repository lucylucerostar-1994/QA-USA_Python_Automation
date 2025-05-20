import configuration
import data
import requests

# ======= Solicitud para crear un nuevo usuario ======= ##

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response_post = post_new_user(get_user_body("Axel"))


# ================ Solicitud para crear Nuevo Kit ===================== ##

def post_new_client_kit(body):
    headers = data.headers.copy()
    auth_token = post_new_user(get_user_body("Axel")).json()["authToken"]
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=headers,
                         json=body)
response_kit = post_new_client_kit(data.kit_body)

import requests

# Define the base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    # API endpoint to retrieve a user (e.g., user with ID 1)
    endpoint = f"{BASE_URL}/users/1"

    # Make a GET request to the API
    response = requests.get(endpoint)

    # Verify the response status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Parse the JSON response
    user_data = response.json()

    # Verify the user data received
    assert user_data["id"] == 1
    assert user_data["name"] == "Leanne Graham"
    assert user_data["email"] == "Sincere@april.biz"
    assert user_data["address"]["city"] == "Gwenborough"

    # Additional assertions can be added based on the API response structure

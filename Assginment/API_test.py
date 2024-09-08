import requests
import pytest

# Define the actual API endpoint and expected response structure
API_URL = "https://api.github.com/users/octocat"  # GitHub API endpoint for a specific user
EXPECTED_KEYS = ['login', 'id', 'node_id', 'avatar_url', 'url']

# Test function
def test_get_github_user():
    # Send GET request to the API endpoint
    response = requests.get(API_URL)

    # Verify the status code is 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Parse the response as JSON
    json_data = response.json()

    # Validate that the response contains the expected data structure (keys)
    for key in EXPECTED_KEYS:
        assert key in json_data, f"Missing expected key: {key}"

# Run the test if the script is executed directly
if __name__ == "__main__":
    pytest.main()

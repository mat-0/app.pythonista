# run.py
import requests
import traceback
import config

title = input("Enter the title of the movie: ")
rating = input("Enter the rating of the movie: ")

GH_USER = config.GH_USER
GH_REPO = config.GH_REPO
GH_PAT = config.GH_PAT
GH_WORKFLOW = "add-film.yml"
BASE_URL = "https://api.github.com"
API_URL = (
    f"{BASE_URL}/repos/{GH_USER}/{GH_REPO}/actions/workflows/{GH_WORKFLOW}/dispatches"
)

request_data = {
    "ref": "main",
    "inputs": {
        "title": title,
        "rating": rating,
    }
}

request_headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GH_PAT}",
    "X-GitHub-Api-Version": "2022-11-28",
}

try:
    response = requests.post(
        API_URL, headers=request_headers, json=request_data, allow_redirects=True
    )
    # Check if the request was successful (status code 2xx)
    response.raise_for_status()

    if response.status_code == 204 and response.ok:
        print(f"SUCCESS\nresponse = {response}")

except requests.exceptions.RequestException as e:
    print(f"Error during API call:")
    traceback.print_exc()  # Use traceback to print the full stack trace
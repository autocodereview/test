import requests

def fetch_github_repositories_all_pages(url, headers):
    page = 1
    per_page = 100
    all_items = []

    while True:
        paginated_url = f"{url}?page={page}&per_page={per_page}"
        response = requests.get(paginated_url, headers=headers)
        if response.status_code != 200:
            break

        items = response.json()
        if not items:
            break

        all_items.extend(items)
        page += 1

    return all_items
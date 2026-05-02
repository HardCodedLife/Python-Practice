import requests
def exercise51(URL: str):
    try:
        response = requests.get(URL)
        response.raise_for_status()
        return f"Status Code: {response.status_code}\nData: {response.json()}"
    except requests.exceptions.HTTPError as e:
        error_response = e.response
        return f"Status Code: {error_response.status_code}"
    except Exception as e:
        print(e)
        return ""
if __name__ == "__main__":
    print(exercise51("https://jsonplaceholder.typicode.com/todos/1")) 

import json
def exercise46(user_json: str) -> str:
    p_obj = json.loads(user_json)
    p_obj["profile"]["settings"]["theme"] = "dart"
    return json.dumps(p_obj)
if __name__ == "__main__":
    print(exercise46('{"id": 1, "profile": {"name": "Alice", "settings": {"theme": "light"}}}'))

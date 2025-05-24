import json

def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f)
        return data

data = load_data("data.json")

def display_users(data):
    print("User and Their connection:\n")
    for user in data["users"]:
        print(f"{user['name']}(Id: {user['id']})- friend: {user['friends']} - liked pages: {user['liked_pages']}")

    print("\nPages Information\n")
    for page in data["pages"]:
        print(f"{page['id']}: {page['name']}")   

display_users(data)
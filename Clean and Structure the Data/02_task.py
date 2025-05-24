import json

def clean_data(data):
    # Remove user with  mmissing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    # remove duplicate friends
    for user in data["users"]:
        user['friends']= list(set(user['friends']))
    # remove no connections or liked pages (inactive user)
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    # remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())

    return data     
# Load the data
data = json.load(open("data.json"))
data = clean_data(data)
json.dump(data, open("cleared_data2.json", "w"), indent=4)
print(data)
print("data has been cleaned successfully")

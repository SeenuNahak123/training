import requests

# GET request (fetch data)
response = requests.get("https://jsonplaceholder.typicode.com/posts/1",verify=False)
print(response.json())

# POST request (create new post)
data = {"title": "New Post", "body": "This is a test post.", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data,verify=False)
print(response.json())

# PUT request (update a post)
update_data = {"title": "Updated Post"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data,verify=False)
print(response.json())

# DELETE request (delete a post)
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1",verify=False)
print(response.status_code)  # Should return 200 (success)
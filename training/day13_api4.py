import requests

# GET request (fetch products)
response = requests.get("https://dummyjson.com/products",verify=False)
print(response.json())

# POST request (add a product)
data = {"title": "New Product", "price": 100}
response = requests.post("https://dummyjson.com/products/add", json=data,verify=False)
print(response.json())

# PUT request (update product)
update_data = {"price": 120}
response = requests.put("https://dummyjson.com/products/1", json=update_data,verify=False)
print(response.json())

# DELETE request (delete product)
response = requests.delete("https://dummyjson.com/products/1",verify=False)
print(response.status_code)  # 200 (success)
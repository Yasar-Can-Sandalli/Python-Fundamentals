import json

data = '{"firstName":"Kade","lastName":"Kerluke"}'
y = json.loads(data)

print(y["firstName"])

customer = {
    "firstName":"Clyde",
    "lastName":"Konopelski",
    "email":"veronica75@gmail.com"
}

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))
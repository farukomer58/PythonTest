customer = {
    "name" : "Omer Citik",
    "age" : 100,
    "is_good": True
}

customer["idk"] = "new Value"
print(customer["name"])
print(customer["idk"])
print(customer.get("birthday", "01-02-1999"))

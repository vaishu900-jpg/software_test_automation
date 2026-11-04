def validate_login(username, password):
    return password == "password123"


result = validate_login("admin", "password123")
print(result)

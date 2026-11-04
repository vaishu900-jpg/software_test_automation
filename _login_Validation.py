def validate_login(username, password):
    if username == "admin" and password == "password123":
        return True
    else:
        return False


result = validate_login("admin", "password123")
print(result)

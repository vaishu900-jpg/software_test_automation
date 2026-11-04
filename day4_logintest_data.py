test_case = {"username": "admin",
             "password": "password123",
             "expected_result": True}

# print(test_case["username"])
# print(test_case["password"])
# print(test_case["expected_result"])

test_case_2 = {"username": "tester",
               "password": "wrong123",
               "expected_result": False}

test_case_list = [test_case, test_case_2]

# print(test_case_list[0])
# print(test_case_list[0].keys())
# print(test_case_list[0].values())
for case in test_case_list:
    print(case["username"])
print("**********")
for value in test_case_list[1].values():
    print(value)
print("==============")
for key, value in test_case_list[1].items():
    print(key, value)

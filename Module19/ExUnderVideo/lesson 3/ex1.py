family_member = {
"name": "Jane",
"surname": "Doe",
"hobbies": ["running", "sky diving", "singing"],
"age": 35,
"children": [

    {
        "name": "Alice",
        "age": 6
    },

    {
        "name": "Bob",
        "age": 8
    }
]
}

for i_key in family_member["children"]:
    if i_key.get("name", {}) == "Bob":
        print(i_key["name"])

for i_key in family_member["children"]:
    if i_key.get("name", {}) == "Rob":
        print(i_key)
else:
    print("none")

# for dict in family_member:
#     if dict.get("name") == "Bob":
#         print("у человека", {dict["name"]}, "есть ребенок с именем Bob")
#     else:
#         print("None")

    # if family_member.get("children", {}).get("Bob", {}):
    #     print(family_member["children"]["name"])
server_data = {
"server": {

    "host": "127.0.0.1",

    "port": "10"

},

"configuration": {

    "access": "true",

    "login": "Ivan",

    "password": "qwerty"

}
}

for i_name in server_data:
    print("{0}:".format(i_name))
    for j_name, j_values in server_data[i_name].items():
        print("     {0}: {1}".format(j_name, j_values
        ))
import json
import random

class PasswordList:

    file_info = {
        "fileName" : "settings.json",
    }

    def write_file(self, file_name, user_input):
        """writes to a file"""
        file_data = open(file_name, "w")
        file_data.write(user_input)


    def read_file(self):
        """returns a string array"""
        file_name = self.file_info["fileName"]
        file_data = open(file_name, "r")
        self.passwordList = json.loads(file_data.read())
        file_data.close()


    passwordList = {
        "masterPassword" : "test",

    }

    def check_password(self, password):
        if password == self.passwordList["masterPassword"]:
            return True
        else:
            return False


    def get_random_character(self):
        characters_to_select_from = ["~", "`", "@", "#", "$", "%", "^"]
        return random.choice(characters_to_select_from)

    def create_password(self, password_length=4, word=""):
        x = 0
        if len(password_length) == 0:
            

        for x in range(0, password_length):




class UI:

    def __init__(self, password_list):
        self.password_list = password_list

    def parse_command(self, command):
        command_list = command.split(" ")
        if command_list[0] == "create":
            if command_list[1] == "password":


print("Hello")
password_list = PasswordList
password_list.read_file(password_list)
users_password = input("Please enter the master password:\n")
if password_list.check_password(password_list, users_password):
    ui = UI(password_list)
    print("you have successfully logged in!")
    while(True):
        users_command = input("what do you want to do?\n")

        break

else:
    print("you shall not pass!")


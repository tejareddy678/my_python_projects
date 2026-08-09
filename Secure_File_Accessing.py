admins = {
            "Vimal" : "123zyxr3",
            "Teja" : "@2546uyu",
            "James" : "34@348%^"
        }
class UserNotFoundError(Exception):
    pass

class AccessDeniedError(Exception):
    pass

file = ""

def login(username):
    if username not in admins:
        raise UserNotFoundError(f"UserNotFoundError : user with name \"{username}\" does not exist")

def check_permission(username,password):
    if admins[username] != password:
        raise AccessDeniedError("AccessDeniedError : Wrong Password")


def open_file():
    username = input("Dear user please enter your name : ")
    try:
        login(username)
    except UserNotFoundError as e:
        print(e)
        return None
    else:
        print("Login Success!")
        password = input("Enter the password to access a file : ")

    try:
        check_permission(username,password)
    except AccessDeniedError as e:
        print(e)
        return None
    else:
        file_name = input("Enter a file name you want to access : ")

    try:
       my_file_object =  open(file_name)
    except FileNotFoundError as e:
        print(e)
        return None
    else:
        print(f"File {file_name} opened successfully in read mode!")
        my_file_object.close()
    return file_name

def write_into_file(file_name):
    if file_name is not None:
        option = int(input("Dear user enter your option\n1.Overwrite the entire file\n2.Append to the end of file\n"))
        List = []
        print("Enter your text : ")
        if option == 1:
          file_object = open(file_name,'wt')
          while(True):
              text = input()
              if text == "":
                  break
              List.append(text)
          file_object.write("\n".join(List))
          file_object.close()
        else:
          file_object = open(file_name,'at')
          while(True):
              text = input()
              if text == "":
                  break
              List.append(text)
          file_object.write("\n".join(List))
          file_object.close()
        file_read_object = open(file_name,"rt")
        print(f"Dear user this is the content in the {file_name}:\n#######\n{file_read_object.read()}\n########")
        file_read_object.close()

user_choice = input("Dear user do you want to open a file (Yes / No) : ").capitalize()
if user_choice == "Yes":
    file = open_file()

if file is not None:
    user_choice = input("Dear user do you want to write anything into the file(Yes / No): ").capitalize()
    if user_choice == "Yes":
     write_into_file(file)
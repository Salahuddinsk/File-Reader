from file import create_file,read_file,append_in_file,search_in_file,delete_file
from icecream import ic 
def main (filename,content = None,search_query = None):
    if user_select == 'Create File':
        action = create_file(filename,content)
    elif user_select == 'Read File':
        action = read_file(filename)
    elif user_select == 'Append in File':
        action = append_in_file(filename,content)
    elif user_select == 'Search':
        action = search_in_file(filename, search_query)
    elif user_select == 'Delete':
        action = delete_file(filename)
    else:
        print('Invalid Input Please Try Again')
    return action
    

loop = True
while loop:
    user_select = input("Select (Create File, Read File, Append in File, Search, Delete, Press e for exit) : ")
    if user_select == 'e':
        break
    content = None
    search_query = None
    if user_select == 'Create File':
        Filename = input('Enter the name of the file: ')
        content = input('Enter the content of the file: ')
    if user_select == 'Append in File':
        Filename= input('Enter the name of the file: ')
        content = input('Enter the content of the file: ')
    if user_select == 'Read File':
        Filename = input('Enter the name of the file: ')
        action = main(Filename)
        print(action)
    if user_select == 'Search':
        Filename = input('Enter the name of the file: ')
        search_query = input('Enter your word to find: ')
    if user_select == 'Delete':
        Filename = input('Enter the name of the file: ')
    action = main(Filename,content,search_query)
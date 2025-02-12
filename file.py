# https://github.com/Mohammed-Musab-Khan/FileHandling

import os


def create_file(filename,content = None):
    with open(filename , 'w') as file:
        if content is not None :
           file.write(content)
        print('Your file has been created')

def read_file(filename):
    with open(filename , 'r') as file :
        content = file.read()
        return content

def search_in_file(filename , search_query):
    content = read_file(filename)
    if search_query in content :
        print(True)
    else :
        print(False)

def delete_file(filename):
    try:
        os.remove(filename)
        print('File Deleted Successfuly')
    except FileNotFoundError:
        print('File Not Found')
    except PermissionError:
        print('Permission Denied')
    except Exception as e:
        print(f'Error: {e}')
    
def append_in_file(filename,content):
    with open(filename , 'a') as file:
        file.write('\n'+ content)
    print('Your content has been added in the file')
    
    
if __name__ == "__main__":
    filename = 'Testing.txt'
    content = 'This is new file \t\n'
    create_file(filename, content)
    content = read_file('Testing.txt')
    new_content = "This is the new content"
    append_in_file(filename,new_content)
    content = read_file('Testing.txt')
    print(content)


# create the chatbot containing all this function and additional put find function in chatbot
# create a code for profile of all students information name , ..... and store it in file 
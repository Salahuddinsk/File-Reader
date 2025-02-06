# https://github.com/Mohammed-Musab-Khan/FileHandling

def create_file(filename,content = None):
    with open(filename , 'w') as file:
        if content is not None :
           file.write(content)
        print('Your file has been created')

def read_file(filename):
    with open(filename , 'r') as file :
        content = file.read()
        return content
    
def append_in_file(filename,content):
    with open(filename , 'a') as file:
        file.write(content)
    print('Your file has been created')
    
    
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
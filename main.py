from file import read_file 
def sum(num1,num2):
    result = num1 + num2
    return result


if __name__ == "__main__":
    sum(3,4)
    content = read_file('Testing.txt')
    print(content)
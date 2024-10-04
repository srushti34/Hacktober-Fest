def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        file.close() 
        return content
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

def main():
    content = read_file("example.txt") 
    print(f"File Content: {content}")

main()

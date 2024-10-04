def countdown(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)
        countdown(n - 2)  

def main():
    try:
        countdown(5)
    except RecursionError as e:
        print(f"RecursionError: {e}")
    
    countdown(-1)  

main()

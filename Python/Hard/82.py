def sort_by_length(words):
    try:
        return sorted(words, key=lambda x: len(x))  
    except TypeError as e:
        print(f"TypeError: {e}")

def main():
    words = ["apple", "banana", "cherry", 1234, "grape"]  
    sorted_words = sort_by_length(words)
    print(f"Sorted by length: {sorted_words}")

main()

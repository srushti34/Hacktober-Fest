def reverse_words(sentence):
    try:
        words = sentence.split(" ")
        reversed_words = words[::-1]
        return "-".join(reversed_words) 
    except AttributeError as e:
        print(f"AttributeError: {e}")

def main():
    sentence = "Hello world this is Python"
    reversed_sentence = reverse_words(sentence)
    print(f"Reversed Sentence: {reversed_sentence}")
    
    sentence = None 
    reversed_sentence = reverse_words(sentence)

main()

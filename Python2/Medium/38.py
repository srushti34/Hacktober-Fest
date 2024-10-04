def reverse_string(s):
 reversed_s = ''
 for i in range(len(s)):
 reversed_s += s[i] 
 return reversed_s
def main():
 string = "hello"
 result = reverse_string(string)
 print(f"Reversed string: {result}")
main()

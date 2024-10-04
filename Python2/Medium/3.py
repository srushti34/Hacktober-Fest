 def countdown(n):
 while n >= 0:
 print(n)
 n += 1  
 def main():
 try:
 countdown(5)
 except KeyboardInterrupt:
 print("Countdown interrupted")
main()
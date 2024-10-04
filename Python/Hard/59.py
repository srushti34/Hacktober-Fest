class FileManager:
   def __init__(self, filename):
     self.filename = filename
     self.file = None

   def __enter__(self):
     self.file = open(self.filename, 'r')
     return self.file
   def __exit__(self, exc_type, exc_value, traceback):
     if self.file:
         self.file.close()
def main():
   try:
     with FileManager("nonexistent.txt") as f:
         data = f.read() 
         print(data)
   except FileNotFoundError as e:
     print(f"FileNotFoundError: {e}")
main()
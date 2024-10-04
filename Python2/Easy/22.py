def read_config(filename):
 config = {}
 try:
    with open(filename, 'r') as file:
      for line in file:
         key, value = line.strip().split('=')
         config[key] = value
 except FileNotFoundError:
  print('Config file not found')
 return config
result = read_config('config.txt')
print(result['nonexistent_key']) 

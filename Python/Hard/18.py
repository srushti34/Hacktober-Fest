class CustomError(Exception):
 def __init__(self, message, code):
    self.message = message
    self.code = code
try:
 raise CustomError("Something went wrong", 404)
except CustomError as e:
 print(e.message + " with error code " + e.code)
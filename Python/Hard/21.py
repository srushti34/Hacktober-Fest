def sub_generator():
 yield from range(3)
def main_generator():
 yield "Start"
 yield sub_generator()
 yield "End"
for value in main_generator():
 print(value)
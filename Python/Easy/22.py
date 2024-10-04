import threading

def thread_function():
    pass

thread = threading.Thread(target=thread_function)
thread.start()
thread.start()
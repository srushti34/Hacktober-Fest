def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return None 

def main():
    data = {"a": 1, "b": 2, "c": 3}
    for key in ["a", "b", "d"]:
        value = get_value(data, key)
        if value is None:
            print(f"Warning: Key '{key}' not found") 
        else:
            print(f"Value for '{key}': {value}")

main()

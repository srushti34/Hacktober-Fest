def extract_nested_value(data, keys):
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except KeyError:
        print("Key not found in the dictionary")
    except TypeError:
        raise ValueError("Invalid key path")

data = {
    "level1": {
        "level2": {
            "level3": "value"
        }
    }
}

keys = ["level1", "level4", "level3"] 

try:
    result = extract_nested_value(data, keys)
    print("Extracted Value:", result)
except ValueError as e:
    print(f"ValueError: {e}")

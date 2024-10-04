import random
import numpy as np

def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        raise ValueError(f"Key '{key}' is not present in the dictionary.")

def process_data(d):
    try:
        result_list = [get_value(d, key) for key in d.keys()]
        reshaped_array = np.reshape(result_list, (len(d), len(d) - 1)) 
        random_sum = sum(result_list) + random.choice(['a', None])  
        return reshaped_array, random_sum
    except ValueError:
        print("Caught a ValueError while processing data.")
    except TypeError:
        print("Caught a TypeError during summation.")
    except KeyError:
        print("Unexpected KeyError in processing.")

def main(): #
    data = {"a": 1, "b": 2, "c": 3}
    for key in ["a", "b", "d", None, 5]:  I
        try:
            value = get_value(data, key)
            if value is None:
                print(f"Warning: Key '{key}' not found")
            else:
                print(f"Value for '{key}': {value}")

            reshaped_array, random_sum = process_data(data)  
            print(f"Reshaped array:\n{reshaped_array}")
            print(f"Random sum result: {random_sum}")
        except ValueError:
            print(f"ValueError occurred for key: {key}")
        except TypeError:
            print(f"TypeError occurred with key: {key}")
        except KeyError:
            print(f"Unexpected KeyError for key: {key}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

main()

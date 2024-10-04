def infinite_recursion(n):
    return infinite_recursion(n + 1)

result = infinite_recursion(0)
print(result)

def generate_even_number():
    start = 0
    while start <= 20:
        start += 2
        yield start


result = generate_even_number()
print(f"result = {result}")
print(f"next = {next(result)}")
# print(f"next = {next(result)}")

# iterator = iter(__)
# value = next(iterator)

from concurrent.futures import ThreadPoolExecutor

numbers = [1, 2, 3, 4, 5, 6]


def pow_of_2_task(n):
    return n ** 2


# When using Context Managers we are making it sync, basically
# We will not exit the with block until all threads in the pool have finished
with ThreadPoolExecutor(max_workers=3) as executor:
    mapped_numbers = executor.map(pow_of_2_task, numbers)

print('Mapped numbers list is:')
for number in mapped_numbers:
    print(number)

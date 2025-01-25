numbers=[]
shoe_sizes=[]
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
shoe_sizes.append(8)
shoe_sizes.append(9)
shoe_sizes.append(10)
shoe_sizes.append(11)
shoe_sizes.append(12)
print(f"nmbers list :{numbers}")
print(f"shoe_siaes :{shoe_sizes}")
numbers.append(1)
numbers.append(2)
print("Numbers List with Duplicates Removed:", list(set(numbers)))

shoe_sizes = []
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)
print("Updated Shoe Sizes List:", shoe_sizes)
combined_list = numbers + shoe_sizes
print("Combined List:", combined_list)

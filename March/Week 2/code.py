data = []
n = int(input("Enter number of data values: "))
for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    data.append(value)
print("Original Data:", data)
clean_data = list(set(data))
filtered_data = [x for x in clean_data if x > 50]
print("Cleaned Data (duplicates removed):", clean_data)
print("Filtered Data (>50):", filtered_data)
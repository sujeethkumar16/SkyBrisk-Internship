try:
    n = int(input("Enter the number of temperature readings: "))
    if n <= 0:
        print("Number of readings must be greater than 0.")
    else:
        total = 0.0
        for i in range(n):
            while True:
                try:
                    temp = float(input(f"Enter temperature {i+1}: "))
                    total += temp
                    break
                except ValueError:
                    print("Invalid input! Please enter a numeric value.")
        average = total / n
        print(f"\nAverage Temperature: {average:.2f}°C")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
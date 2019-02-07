import random

while True:
    start = input("\nPress 1 to roll dice: ")
    if start == "1":
        cycle_2 = True
        while cycle_2:
            try:
                amount = int(input("""
How many dice do you want to roll?
Insert amount: """))
                if amount < 1:
                    print("Invalid amount.")
                else:
                    cycle_2 = False
                    results = []
                    roll_number = 1
                    print()
                    for x in range(amount):
                        result = random.randint(1, 6)
                        results.append(result)
                        print(f"ROLL {roll_number}: {result}")
                        roll_number += 1
                    results_sum = sum(results)
                    highest_result = max(results)
                    lowest_result = min(results)
                    duplicates = []
                    set_1 = set(results)
                    results_copy = []
                    if len(set_1) != len(results):  # It means there are duplicates.
                        for x in set_1:
                            results_copy.append(x)
                            if results.count(x) != results_copy.count(x):
                                duplicates.append(x)
                    print(f"""
Sum: {results_sum}
Highest Result: {highest_result}
Lowest Result: {lowest_result}
Duplicated Results: {duplicates}""")
            except ValueError:
                print("Invalid amount.")
    else:
        print("Invalid command.")

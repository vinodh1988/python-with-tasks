try:
        # Read the denominator from user input
    denominator = int(input("Enter a denominator: "))
        
        # ArithmeticError example: Division by zero
    result = 10 / denominator
    print(f"Result of division: {result}")

        # ValueError example: Invalid literal for int()
    number = int(input("Enter a number: "))

        # IndexError example: List index out of range
    my_list = [1, 2, 3]
    element = my_list[int(input("Enter an index: "))]
except ArithmeticError as e:
    print(f"ArithmeticError: {e}")
except ValueError as e:
    print(f"ValueError: {e}")
except IndexError as e:
    print(f"IndexError: {e}")
except Exception  as e:
    print(f"Exception: {e}")
else:
    print("This block of code will execute only if there is no exception.")
finally:
    print("This block of code will always execute.")

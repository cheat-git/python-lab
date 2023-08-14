# clear


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid operand types")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Division successful. Result:", result)
    finally:
        print("Execution completed")

# Test cases
divide_numbers(10, 2)  # Valid division
divide_numbers(10, 0)  # Division by zero
divide_numbers("10", 2)  # Invalid operand types
divide_numbers(10, "2")  # Invalid operand types
  
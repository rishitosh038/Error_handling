import logging

# Logging Configuration

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception

class NegativeNumberError(Exception):
    """Raised When a negative number is provided"""
    pass

# Function to demostrate exception handling

def divide_numbers(a,b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")
        
        result = a / b
    
    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError occurred", exc_info=True)
        print("Error: Cannot devided by zero")

    except TypeError as e:
        logging.error("TypeError occurred", exc_info=True)
        print("Error: Invalid data type used")
    
    except NegativeNumberError as e:
        logging.error(f"CustomError: {e}", exc_info=True)
        print(f"Error: {e}")
    
    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("Unexpected error occurred")

    else:
        print(f"Result: {result}")
    
    finally:
        print("Execution completed\n")

# Simulating Runtime Errors

divide_numbers(10, 2)  # Valid case
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "a")  # TypeError
divide_numbers(-5, 2)  # Custom Exception
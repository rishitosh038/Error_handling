
## Overview
This project demonstrates proper **exception handling and logging** in Python.  
It handles runtime errors gracefully, logs them into a file, and uses custom exceptions, making the code **production-ready and interview-ready**.

---

## Tools & Technologies
- Python 3.x  
- logging module  

---

## Project Structure
Exception_Handling/
│
├── error_handling.py   # Main Python script
├── app.log             # Auto-generated log file
└── README.md           # Project documentation

---

## Objectives
- Implement exception handling in Python
- Handle multiple exceptions
- Use try, except, else, and finally
- Create and use custom exceptions
- Log errors to a file
- Debug applications using logs

---

## Concepts Covered
- try-except blocks  
- Multiple exception handling  
- Built-in exceptions:
  - ZeroDivisionError
  - TypeError
- Custom exception creation  
- Logging using logging module  
- File-based error logs  
- Production-level error handling  

---

## How It Works
1. The script attempts to divide two numbers.
2. Various runtime errors are intentionally simulated.
3. Each error is handled with a clear message.
4. Errors are logged into `app.log` with timestamps.
5. The finally block ensures execution completion.

---

## How to Run
1. Open terminal / command prompt
2. Navigate to the project directory
3. Run the script:

python error_handling.py

---

## Sample Output
Result: 5.0  
Error: Cannot divide by zero  
Error: Invalid data type used  
Error: Negative numbers are not allowed  
Execution completed  

---

## Log File (app.log)
- Automatically generated
- Stores:
  - Error type
  - Timestamp
  - Stack trace
- Helps debug production issues efficiently

---

## Final Outcome
✔ Intern understands exception handling  
✔ Intern can debug using logs  
✔ Intern writes production-ready Python code  


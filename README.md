# MY FINAL PROJECT

A simple social media web application built with Flask and JavaScript that allows users to register, log in, create, view, and delete posts stored in JSON files.

- What does it do?  
  This is a web project where users can sign up, log in, add posts with text and images, and see posts from all users.

- What is the "new feature" which you have implemented that we haven't seen before?  
  The application reads and writes user and post data directly to JSON files on the server and manages user sessions with localStorage on the client side.

## Prerequisites

- Flask (install with `pip install Flask`)
- Python 3.8 or higher

## Project Checklist

- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.  
  - Module name: `json`
- [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to initialize the object's attributes, including instantiating the class and using the methods in your app.  
  - File name for the class definition: `models.py` (or wherever the class is defined)  
  - Line number(s) for the class definition: lines 10-35 (example)  
  - Name of two properties: `username`, `posts`  
  - Name of two methods: `add_post()`, `delete_post()`  
  - File name and line numbers where the methods are used: `app.py`, lines 85, 112
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It uses modern JavaScript (for example, `let` and `const` rather than `var`).
- [x] It makes use of the reading and writing to the same file feature.
- [x] It contains conditional statements.  
  - File name: `app.py`  
  - Line number(s): 45-60 (example)
- [x] It contains loops.  
  - File name: `app.py`  
  - Line number(s): 70-85 (example)
- [x] It lets the user enter a value in a text box at some point.  
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] It is styled using your own CSS.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code.  
  In particular, the code does not use `print()` or `console.log()` for any user feedback. Instead, all feedback is shown in the browser.
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.


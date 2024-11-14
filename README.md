
# Project Title

Welcome to the **[Python Numerical Literal Checker]** repository! This project, developed as part of our course, implements a program to check all defined literals in Python. Below, you'll find information on our group members, features developed, code versions, and more.

## Table of Contents

- [Group Members](#group-members)
- [Project Features](#project-features)
- [Code Versions](#code-versions)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

---

## Group Members

| Name                 | GitHub Username     | Tasks Completed                                                                                 | Extra Credit Tasks                          |
|----------------------|---------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------|
| **[Joshua Goodman]**    | [jgx02c]   | - Created the program and test cases |
| **[Mason Orton]**    | [MasonAsemi]   | - Created the NFA's and JFLAP files |

---

## Project Features

This project includes the following features:

- **Authentication**: Secure user login, registration, and session management.
- **CRUD Operations**: Complete CRUD functionality for managing [entity types, e.g., tasks, posts, etc.].
- **Responsive Design**: Adaptable UI for various devices and screen sizes.
- **Error Handling**: Comprehensive error handling and logging throughout the app.
- **Performance Optimizations**: Efficient handling of database queries and code to ensure a smooth user experience.

---

## Code Versions

We use version tags to keep track of major changes and updates.

| Version | Description                                                             | Release Date |
|---------|-------------------------------------------------------------------------|--------------|
| `v1.0`  | All files including the main program and NFA's using JFLAP              |  11-13-2023  |


---

## Setup and Installation

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd your-repo-name
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**: 
   - Rename `.env.example` to `.env` and fill in the necessary details.

5. **Run the application**:
   ```bash
   python main.py
   ```

---

## Usage

Once the application is set up, you can interact with it by following these steps:

1. **Activate the virtual environment** (if applicable):
   ```bash
   source venv/bin/activate  # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Access API Endpoints** (if the project includes a web server or API):
   - By default, the API can be accessed at `http://localhost:5000`.
   - Use tools like **Postman** or **curl** to interact with the endpoints.
   
4. **Run Unit Tests** (if applicable):
   ```bash
   python -m unittest discover tests
   ```

5. **Common Commands**:
   - **Start Development Server**: `python main.py`
   - **Lint Code**: `flake8 .` or `pylint <filename>`
   - **Run Tests**: `pytest` or `python -m unittest`

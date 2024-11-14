
# Python Numerial Literaly Checker w/ Floating Point Literal Checker

Welcome to the **Python Numerical Literal Checker w/ Floating Point Literal Checker** repository! This project, developed as part of our course, implements a program to check all defined literals in Python. Below, you'll find information on our group members, features developed, code versions, and more.

## Table of Contents

- [Group Members](#group-members)
- [Project Features](#project-features)
- [Code Versions](#code-versions)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Test Results](#test-results)

---

## Group Members

| Name                 | GitHub Username     | Tasks Completed                                                                                 | Extra Credit Tasks                          |
|----------------------|---------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------|
| **Joshua Goodman**    | jgx02c  | - Created the program and test cases |
| **Mason Orton**    | MasonAsemi   | - Created the NFA's and JFLAP files |

---

## Project Features

This project includes the following features:

- **Integer literal checking**: Check if a number is a valid integer literal
- **Floating point literal checking**: Check if a number is a valid floating point literal

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
   git clone https://github.com/jgx02c/CS-33110-Group-Project-1.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd CS-33110-Group-Project-1
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

---

## Usage

Once the application downloaded, you can interact with it by following these steps:

1. **Run Program**:
   - Run the program in the folder. 

2. **Input necessary requirements**:
   - Input whether or not you wish to run a single test case or multiple using an input file
   - List your input and output file

   The input files follow the format shown in the example string, with the expected output appearing after it, such as:
    ```0O7_5_5 true```

   **Note: testOne.txt maatches the output file outputOne.txt as testTwo.txt matches the output file outputTwo.txt**

3. **Find your test file and review declarations**:
   - Open your test file you input into the terminal
   - Inside should list all of the test cases and their appropriate results


## Test Results


### Decimal Notation:
--------------------------------------------------
- Input: 123
- Expected: True
- Actual: True
- Number Type: decimal
- Test PASSED
--------------------------------------------------
- Input: 0
- Expected: False
- Actual: False
- Number Type: invalid
- Test PASSED
--------------------------------------------------
- Input: 1_000
- Expected: True
- Actual: True
- Number Type: decimal
- Test PASSED
--------------------------------------------------
- Input: 42
- Expected: True
- Actual: True
- Number Type: decimal
- Test PASSED
--------------------------------------------------
- Input: 9_876_543_210
- Expected: True
- Actual: True
- Number Type: decimal
- Test PASSED



### Binary Notation:
--------------------------------------------------
- Input: 0b1010
- Expected: True
- Actual: True
- Number Type: binary
- Test PASSED
--------------------------------------------------
- Input: 0B1_001
- Expected: True
- Actual: True
- Number Type: binary
- Test PASSED
--------------------------------------------------
- Input: 0b0
- Expected: True
- Actual: True
- Number Type: binary
- Test PASSED
--------------------------------------------------
- Input: 0b10101010
- Expected: True
- Actual: True
- Number Type: binary
- Test PASSED
--------------------------------------------------
- Input: 0B1111_0000
- Expected: True
- Actual: True
- Number Type: binary
- Test PASSED



### Octal Notation:
--------------------------------------------------
- Input: 0o755
- Expected: True
- Actual: True
- Number Type: octal
- Test PASSED
--------------------------------------------------
- Input: 0O7_5_5
- Expected: True
- Actual: True
- Number Type: octal
- Test PASSED
--------------------------------------------------
- Input: 0o0
- Expected: True
- Actual: True
- Number Type: octal
- Test PASSED
--------------------------------------------------
- Input: 0O123
- Expected: True
- Actual: True
- Number Type: octal
- Test PASSED
--------------------------------------------------
- Input: 0o777
- Expected: True
- Actual: True
- Number Type: octal
- Test PASSED



### Hexadecimal Notation
--------------------------------------------------
- Input: 0xFF
- Expected: True
- Actual: True
- Number Type: hexadecimal
- Test PASSED
--------------------------------------------------
- Input: 0X1_A2
- Expected: True
- Actual: True
- Number Type: hexadecimal
- Test PASSED
--------------------------------------------------
- Input: 0x0
- Expected: True
- Actual: True
- Number Type: hexadecimal
- Test PASSED
--------------------------------------------------
- Input: 0x123_ABC
- Expected: True
- Actual: True
- Number Type: hexadecimal
- Test PASSED
--------------------------------------------------
- Input: 0XDEAD_BEEF
- Expected: True
- Actual: True
- Number Type: hexadecimal
- Test PASSED
--------------------------------------------------

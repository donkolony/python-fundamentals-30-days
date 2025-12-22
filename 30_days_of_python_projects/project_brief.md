# Python Projects (Day 1 – Day 13)

This document contains three major projects designed to consolidate and apply everything learned from Day 1 to Day 13 of Python fundamentals.

---

## Project 1: CLI Personal Finance Tracker

### Project Description

Build a command-line personal finance tracker that allows users to manage income and expenses. The application will simulate how real-world budgeting and finance apps work, focusing on data handling, logic, and reporting.

### Core Objectives

- Track income and expenses
- Categorize transactions
- Calculate totals and balances
- Display summaries using clean CLI output

### Key Features

- Add income and expense transactions
- Categorize transactions (e.g. food, rent, transport)
- Automatically calculate:
  - total income
  - total expenses
  - remaining balance
- Filter expenses by category
- Generate random transaction IDs
- Display summaries using loops and conditionals

### Concepts Applied

- Variables and data types
- Conditionals
- Lists, dictionaries, and sets
- Loops (for & while)
- Functions and return values
- Modules (`random`)
- List comprehension

---

## Project 2: Mini CLI Game Collection

### Project Description

Create a collection of simple command-line games bundled into one application. Each game should be modular and reusable, focusing on logic, control flow, and function design.

### Core Objectives

- Practice problem-solving and logic
- Strengthen function-based program design
- Work with randomness and user input

### Games to Include

- Number Guessing Game
- Rock–Paper–Scissors
- Dice Rolling Simulator
- Quiz Game

### Key Features

- Menu system to select games
- Score tracking
- Replay functionality
- Difficulty levels (optional)
- Randomized outcomes

### Concepts Applied

- Conditionals and loops
- Functions and parameters
- Dictionaries for game state
- Sets to avoid duplicate questions
- Modules (`random`)
- List comprehension for filtering scores

---

## Project 3: User Management System (CLI-Based)

### Project Description

Develop a command-line user management system that simulates how backend systems manage users. This project mirrors real-world API and database-style logic using in-memory data structures.

### Core Objectives

- Manage users using structured data
- Perform CRUD-style operations
- Validate and process user input

### Key Features

- Create users with unique IDs
- Store user profiles (name, age, skills, status)
- Validate age and unique emails/usernames
- Search users by name or skill
- Update and delete user records
- Display formatted user profiles

### Example Data Structure

```python
{
  "id": "X7kP9A",
  "name": "User Name",
  "age": 25,
  "skills": ["Python", "SQL"],
  "active": True
}
```

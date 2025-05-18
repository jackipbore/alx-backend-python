# Python Generators - Task 0: Getting Started

## Description

This task sets up the foundation for working with Python generators by interacting with a MySQL database. It includes creating a database and a table, and populating it with user data from a CSV file.

## Objective

Create a Python script (`seed.py`) that:

- Connects to a MySQL server using a specified username and password.
- Creates a database named `ALX_prodev` if it does not already exist.
- Connects to the `ALX_prodev` database.
- Creates a `user_data` table with the following fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR, NOT NULL)
  - `email` (VARCHAR, NOT NULL)
  - `age` (DECIMAL, NOT NULL)
- Loads sample data from a file named `user_data.csv`.

## Usage

Run the script `0-main.py` to set up the database and populate it with data:

```bash
./0-main.py


# LoginSignUpPage

## Overview
#### This is a GUI-based Login & Signup system built using Python Tkinter and MySQL. It allows users to register and log in securely using a MySQL database.

## Features

- User Registration (Sign-Up) with username and password
- Secure Login authentication
- Password verification during Sign-Up
- Error handling for missing fields and incorrect credentials
- GUI interface built with Tkinter

## Technologies Used

- Python (Tkinter for GUI, MySQL Connector for database handling)
- MySQL (For user authentication and data storage)
- PIL (Pillow) (For handling images in the UI)


## Installation & Setup

### Prerequisites

#### Make sure you have the following installed:
- <strong>Python</strong> (Recommended: Latest version)
- MySQL Server


## Clone the Repositor

```sh
git clone https://github.com/your-username/repository-name.git
cd repository-name
``` 
## Install Required Packages

```bash
pip install mysql-connector-python pillow
```

## Database Setup

### 1. Open MySQL and create a database:
```bash
CREATE DATABASE login_sign;
```
### 2. Select the database and create the required table:

```bash
USE login_sign;
CREATE TABLE login_sign (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstIn VARCHAR(50),
    lastIn VARCHAR(50),
    userIn VARCHAR(50) UNIQUE,
    passIn VARCHAR(255)
);
```
### 3,. Update database connection details (host, user, password) in connectDatabase() function inside the Python script.



## Contribution

### If you want to contribute:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Commit your changes (git commit -m "Added new feature")
4. Push to the branch (git push origin feature-branch)
5. Open a Pull Request
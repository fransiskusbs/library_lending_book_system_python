# Python CRUD Application for Library Lending Book System

A comprehensive Python application for managing library book loan data with Create, Read, Update, and Delete (CRUD) operations. This application is designed to help librarians manage book borrowing records efficiently and systematically.

## Business Understanding

This project caters to the school library industry, specifically to support librarians in managing book borrowing and returning data efficiently. A book loan management system plays a crucial role to record information about borrowers, books, borrowing dates, return dates, and loan status. By using this application, the process of recording and managing borrowing data can be performed more efficiently compared to manual record-keeping.

**Benefits:**

* Improved data accuracy and consistency of book loan records
* Streamlined book borrowing and returning data management
* Reduced errors in recording borrower and book information
* Easier searching and monitoring of borrowing records
* Faster access to information about currently borrowed and returned books
* Improved efficiency of librarians in managing daily library activities

**Target Users:**

This application is designed for school librarian to facilitate their daily activities related to managing book borrowing records, including adding, viewing, searching, updating, and deleting loan data.

## Features

* **Create:**
    * Add new book loan records with essential information such as borrower name, book title, borrowing date, return date, and loan status.
    * Automatically generate a unique ID for each borrowing record.
    * Validate user input to maintain data integrity.
    * Provide a confirmation step before saving new loan data.
* **Read:**
    * Search and retrieve specific book borrowing records by applying filters based on book title, name of borrower, and status.
    * Display all borrowing information in a structured table.
    * Display comprehensive information for each book borrowing information in a user-friendly format.
    * Show information such as ID, borrower name, book title, borrowing date, return date, and loan status.
    * Display the available book list and stock information.
* **Update:**
    * Modify existing book borrowing data to reflect changes in borrower name, book title, borrowing date, return date, and loan status.
    * Validate user input before updating data
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted book borrowing records with appropriate authorization checks.
    * Validate the entered ID before deleting data
    * Provide confirmation before removing a book borrowing record.

## Installation

1. **Prerequisites:**
    * Python version (specify the required version)
    * Additional dependencies (list any required packages)

2. **Installation:**
   Clone this repository and open the project directory:
    ```bash
    git clone https://github.com/fransiskusbs/library_lending_book_system_python.git
    cd library_lending_book_system_python
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
   After running the application, the librarian can select the available menu options :
    * **Create:** Add a new book borrowing record by entering the required borrower and book information. The librarian must confirm the data before it is saved.
    * **Read:** Search and retrieve borrower information by specific records using a keyword like name, book title, or status.
    * **Update:** Modify borrower details by using its ID, such as updating their name, book title, or status and confirm the changes before they are applied.
    * **Delete:** Remove a borrower record from the system using its ID and confirm the deletion before the record is removed.

## Data Model
This project utilizes a Python list of dictionaries to represent book borrowing records data. The following fields are typically stored:
   * [ID]: (Integer) - A unique identifier for each book borrowing record.
   * [Borrower Name]: (String) - The name of the student who borrows the book.
   * [Book Title]: (String) - The title of the borrowed book.
   * [Borrowed Date]: (String) - The date when the book was borrowed.
   * [Return Date]: (String) - The expected or actual return date of the book.
   * [Status]: (String) - The current status of the loan, such as "Dipinjam" or "Dikembalikan".

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to fransiskusjorang@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.


# Google Sheets Mimic Web Application

## Overview
This web application mimics the core functionalities of Google Sheets. It provides a spreadsheet interface where users can input data, apply mathematical functions, and execute data quality functions. The application also supports drag functionality, cell dependencies, and allows users to manage rows and columns.

## Features
### 1. Spreadsheet Interface
- **Mimic Google Sheets UI**: The interface resembles Google Sheets, including the toolbar, formula bar, and cell structure.
- **Drag Functions**: Users can drag and drop cells to move data, including formulas and selections.
- **Cell Dependencies**: Formulas update automatically when changes are made to related cells.
- **Basic Cell Formatting**: Supports bold, italics, font size, and color formatting for text in cells.
- **Row and Column Management**: Add, delete, and resize rows and columns.

### 2. Mathematical Functions
- **SUM**: Calculates the sum of a range of cells.
- **AVERAGE**: Calculates the average of a range of cells.
- **MAX**: Returns the maximum value from a range of cells.
- **MIN**: Returns the minimum value from a range of cells.
- **COUNT**: Counts the number of cells containing numerical values in a range.

### 3. Data Quality Functions
- **TRIM**: Removes leading and trailing whitespace from a cell.
- **UPPER**: Converts the text in a cell to uppercase.
- **LOWER**: Converts the text in a cell to lowercase.
- **REMOVE_DUPLICATES**: Removes duplicate rows from a selected range.
- **FIND_AND_REPLACE**: Allows users to find and replace specific text within a range of cells.

### 4. Data Entry and Validation
- Input various data types (numbers, text, dates).
- Implement basic data validation checks to ensure numeric cells only contain numbers.

### 5. Testing
- Users can test implemented functions with their own data.
- Results of function execution are displayed clearly in the interface.

## Prerequisites
Before running the project, ensure that the following are installed:

- Python 3.x
- Django 3.x or above
- Redis (if used for caching/session management)


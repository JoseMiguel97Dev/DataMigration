# Data Normalization & Cleaning Script (CRM Clients)

This repository features an automated Python script powered by the **Pandas** library designed to load, inspect, clean, and standardize client records sourced from a raw CRM export (`dirty_crm_clients.csv`).

The primary objective of this project is to transform "dirty" or poorly formatted data into a structured, reliable, and production-ready dataset tailored for database migration, storage, or Business Intelligence (BI) tools.

---

## 🎯 Project Goals

The script addresses several critical data-ingestion issues:
* **Initial Inspection:** Quickly diagnose dataset dimensions and data types before executing any transformations.
* **Date Validation:** Isolate and flag records with corrupt or invalid date formats to prevent data loss or database pipeline crashes.
* **Missing Value Handling:** Provide fallback values for critical fields (e.g., missing client names) instead of dropping rows blindly.
* **Text Standardization:** Clean up typographical issues, trailing/leading whitespaces, and erratic casing.

---

## 🛠️ Data Cleaning Pipeline (Step-by-Step)

### 1. Data Loading & Type Enforcement
* Reads a semi-colon (`;`) delimited CSV file using `latin-1` encoding.
* Enforces the `client_id` field as a string (`str`) to prevent Python from dropping any leading zeros (e.g., preserving `00342` instead of converting it to `342`).
* Prints out initial structural diagnostics via `.shape` and `.info()`.

### 2. Date Normalization & Quality Control
* Converts the `migration_date` strings into standard pandas datetime objects.
* **Alert Mechanism:** If invalid or corrupted date formats are encountered, the script calculates the count, prints a warning to the console, and safely exports those specific rows to a separate audit file named `failed_date.csv`. This prevents pipeline failure and allows for manual debugging.

### 3. Text Formatting & Missing Data Imputation
* Replaces any missing values in the `full_name` column with a placeholder token: `"MISSING NAME"`.
* Trims accidental whitespaces using `.str.strip()`.
* Formats strings into Proper/Title Case (`.str.title()`), ensuring names look standardized (e.g., `"john DOE "` becomes `"John Doe"`).

### 4. Export & Verification
* Displays a quick validation preview of the cleaned dataframe.
* Performs a final dataset inspection.
* Generates a freshly sanitized output file named `clean_crm_clients.csv`.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed along with the `pandas` library. You can install it using pip:

```bash
pip install pandas
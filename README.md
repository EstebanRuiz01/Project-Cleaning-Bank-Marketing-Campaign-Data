# 🏦 Project-Cleaning-Bank-Marketing-Campaign-Data

## 📌 Project Overview

This project focuses on cleaning, transforming, and restructuring bank marketing campaign data to prepare it for storage in a PostgreSQL database.

The dataset comes from a marketing campaign where a bank contacted customers to promote personal loans. The original data contained customer information, campaign results, and economic indicators that needed to be standardized before being used in a database.

The project was completed as part of a DataCamp data analysis project.

## 🎯 Objectives

The main goals of this project were to:

* Clean and standardize the original dataset.
* Correct inconsistent values and formats.
* Convert columns to the required data types.
* Handle missing and unknown values.
* Create a properly formatted contact date.
* Separate the data into logical datasets.
* Produce CSV files ready for PostgreSQL import.

## 🛠️ Technologies & Tools
* Python
* Pandas
* NumPy
* Jupyter Notebook
* CSV

## 💡 What I Learned

Through this project, I practiced several important data-preparation techniques:

* Data type conversion with Pandas.
* Cleaning inconsistent categorical values.
* Handling missing values.
* Creating and formatting datetime columns.
* Converting categorical variables into boolean values.
* Splitting a dataset into logically related tables.
* Preparing structured data for relational database storage.

This project helped reinforce the importance of data quality and consistency before loading information into a database.

## 🧹 Data Cleaning & Transformation

Several transformations were performed on the original bank_marketing.csv dataset.

### Client Data

The customer information was separated into client.csv.

Key transformations included:

* Converting IDs and ages to integer types.
* Replacing . with _ in job and education values.
* Converting unknown education values to NaN.
* Converting credit default and mortgage values into boolean indicators.

Campaign Data

Campaign information was stored in campaign.csv.

## The cleaning process included:

* Converting numerical columns to integer types.
* Converting campaign outcomes to boolean values.
* Creating a last_contact_date column.
* Combining the contact day and month with a new year value of 2022.
* Formatting dates as YYYY-MM-DD.

## Economic Data

Economic indicators were separated into economics.csv.

The dataset contains:
* Consumer Price Index (cons_price_idx)
* Three-month Euribor rate (euribor_three_months)
These values were converted to the appropriate floating-point data types.

## 📊 Final Datasets

The original dataset was divided into three datasets based on their purpose:

| File | Description |
| :--- | :--- |
| `client.csv` | Customer demographic and financial information |
| `campaign.csv` | Current and previous campaign information |
| `economics.csv` | Economic indicators associated with the campaign |

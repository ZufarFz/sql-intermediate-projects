# SQL Intermediate Projects

This repository is a continuation of my **SQL Beginner Projects**, where I move from fundamental SQL concepts toward more advanced querying, relational data analysis, and business problem solving.

Previous repository:

[**SQL Beginner Projects**](https://github.com/ZufarFz/sql-beginner-projects)

This repository focuses on using SQL to **combine, transform, and analyze data** across multiple related tables using a realistic relational database.

---

## 🎯 Project Goal

The goal of this project is not simply to memorize SQL syntax, but to develop practical SQL and analytical thinking skills.

Throughout this repository, I will practice how to:

* Understand relational database structures
* Work with relationships between multiple tables
* Use conditional logic with `CASE`
* Transform and clean data using SQL functions
* Combine data using `JOIN`
* Work with multiple table relationships
* Use subqueries and CTEs
* Perform advanced aggregation
* Translate business questions into SQL queries
* Validate and interpret query results
* Turn query results into meaningful business insights

The overall progression is:

```
I can query data.
        ↓
I can combine data.
        ↓
I can transform data.
        ↓
I can analyze data.
        ↓
I can answer business questions using SQL.
```

---

## 📚 Learning Progression

This repository represents the second stage of my SQL learning path.

```
SQL Beginner
    ↓
Query Fundamentals
    ↓
Filtering & Sorting
    ↓
Aggregation
    ↓
Basic Functions
    ↓
SQL Intermediate
    ↓
CASE
    ↓
Advanced Functions
    ↓
JOIN
    ↓
Multiple JOIN
    ↓
Subqueries
    ↓
Advanced Aggregation
    ↓
CTE
    ↓
Business Analysis
    ↓
Intermediate Project
    ↓
SQL Advanced
    ↓
Window Functions
    ↓
Advanced Business Analysis
```

---

## 🗂️ Project Structure

```
sql-intermediate-projects/
│
├── README.md
│
├── images/
│   └── ...
│
└── projects/
    │
    ├── 00_database_design/
    ├── 01_case/
    ├── 02_advanced_functions/
    ├── 03_join/
    ├── 04_multiple_join/
    ├── 05_subqueries/
    ├── 06_advanced_aggregation/
    ├── 07_cte/
    ├── 08_business_analysis/
    └── 09_intermediate_project/
```

### Lesson Overview

| Lesson | Topic                | Focus                                           |
| ------ | -------------------- | ----------------------------------------------- |
| 00     | Database Design      | Designing and preparing the relational dataset  |
| 01     | CASE                 | Conditional logic                               |
| 02     | Advanced Functions   | String, numeric, and date functions             |
| 03     | JOIN                 | Combining data from multiple tables             |
| 04     | Multiple JOIN        | Working with multiple table relationships       |
| 05     | Subqueries           | Nested queries and alternative query approaches |
| 06     | Advanced Aggregation | Conditional and multi-table aggregation         |
| 07     | CTE                  | Structuring complex queries                     |
| 08     | Business Analysis    | Solving business questions with SQL             |
| 09     | Intermediate Project | Applying the complete skill set                 |

---

## 🗄️ Dataset

Unlike the Beginner repository, this project uses a **multi-table relational database** designed around a synthetic e-commerce business.

The main relationships are:

```
countries
    ↓
cities
    ↓
customers
    ↓
orders
    ↓
order_items
    ↓
products
    ↓
categories

departments
    ↓
employees
```

The dataset contains approximately:

* 5,000 customers
* 100,000 orders
* 300,000+ order items
* 100 products
* 8 product categories
* Multiple countries and cities
* Employee and department data

The dataset is generated using Python with business rules designed to create realistic customer growth, transaction patterns, seasonal activity, and relationships between entities.

The generator also includes validation checks to help ensure that the generated data follows the defined business rules and temporal relationships.

More details about the dataset, database structure, generation process, and validation rules can be found in:

[00_database_design](https://github.com/ZufarFz/sql-intermediate-projects/tree/main/projects/00_database_design)

---

## 🛠️ Tools

This project uses:

* **PostgreSQL** — Database and SQL dialect
* **pgAdmin 4** — PostgreSQL database management and SQL development
* **Python** — Synthetic dataset generation
* **Git** — Version control
* **GitHub** — Project documentation and portfolio

---

## 🧠 Learning Approach

Each lesson follows a gradual learning process:

```
Concept
   ↓
Syntax
   ↓
Simple Example
   ↓
Business Scenario
   ↓
Practice
   ↓
Query Review
   ↓
Business Interpretation
```

The focus is not only on whether a query works, but also on understanding:

* Why a particular SQL technique is used
* How the query processes the data
* What level of data is being analyzed
* How to validate the result
* What the result means from a business perspective

---

## 📊 Analytical Thinking

Throughout this repository, I will practice approaching SQL problems using the following framework:

```
Business Question
        ↓
Understand the Data
        ↓
Identify Required Tables
        ↓
Identify Required Columns
        ↓
Determine the Data Grain
        ↓
Choose SQL Technique
        ↓
Write Query
        ↓
Validate Result
        ↓
Interpret Result
        ↓
Business Insight
```

A major focus of the Intermediate stage is understanding **data grain**.

Examples include:

```text
Employee level
Department level
Customer level
Order level
Order item level
Product level
Monthly level
```

Understanding the grain helps ensure that joins, aggregations, and calculations produce results at the intended level of analysis.

---

## 📈 From Syntax to Business Analysis

The Beginner repository focused primarily on building the foundation for writing SQL queries.

The Intermediate repository expands that foundation by introducing more realistic analytical scenarios.

The progression is:

```
SQL Syntax
    ↓
Query Understanding
    ↓
Relational Data
    ↓
Multi-table Queries
    ↓
Data Transformation
    ↓
Aggregation
    ↓
Business Questions
    ↓
Business Insights
```

The objective is to gradually move from:

> "How do I write this SQL syntax?"

toward:

> "What is the best SQL approach to answer this business question?"

---

## 🔗 Previous & Current Repository

### SQL Beginner Projects

The Beginner repository contains the fundamental SQL concepts that serve as the foundation for this project.

Topics include:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `LIMIT`
* `DISTINCT`
* `Operators`
* `LIKE`
* `IN BETWEEN`
* `GROUP BY`
* `HAVING`
* `Basic Functions`

**Repository:**
[sql beginner projects](https://github.com/ZufarFz/sql-beginner-projects)

### SQL Intermediate Projects

This repository continues the learning path with relational databases, multi-table analysis, data transformation, and business-oriented SQL.

**Repository:**
[sql intermediate projects](https://github.com/ZufarFz/sql-intermediate-projects)

---

## 📈 Learning Progress

| Lesson | Topic | Status |
|--------|-------|--------|
| 00 | Database Design | ✅ Completed |
| 01 | CASE | ⏳ In Progress |
| 02 | Advance Functions | ⏳ |
| 03 | JOIN | ⏳ |
| 04 | Multiple JOIN | ⏳ |
| 05 | Subqueries | ⏳ |
| 06 | Advanced Aggregation | ⏳ |
| 07 | CTE | ⏳ |
| 08 | Business Analysis | ⏳ |
| 09 | Intermediate Project | ⏳ |

---

## 🎯 Final Goal

The final goal of this repository is to demonstrate progression from fundamental SQL knowledge toward practical analytical SQL skills.

By the end of this project, I aim to be able to:

> Understand a business problem, identify the required data, determine the appropriate analytical approach, write and validate the SQL query, and explain the resulting business insight.

This repository is part of my ongoing journey toward becoming a **Professional Data Analyst**.

# 🗃️ SQL - Introduction

This project introduces the basics of **SQL** and **MySQL** by exploring how to create, manipulate, and query databases.

It is part of the **Holberton School** higher-level programming curriculum.

---

## 📘 Description

SQL (Structured Query Language) is the standard language for interacting with relational databases.

In this project, you will learn how to:

- Create and delete databases and tables
- Insert, update, and remove data
- Use filtering and sorting (`WHERE`, `ORDER BY`)
- Aggregate data using `COUNT()` and `AVG()`
- Group data with `GROUP BY`


---

## 🧱 Files & Tasks

Each SQL script below solves a specific task:

| 📄 File | 📝 Description |
|--------|----------------|
| `0-list_databases.sql` | Lists all databases on the server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables from a given database |
| `4-first_table.sql` | Creates `first_table` with columns `id` (INT) and `name` (VARCHAR) |
| `5-full_table.sql` | Shows the SQL definition of `first_table` |
| `6-list_values.sql` | Displays all rows from `first_table` |
| `7-insert_value.sql` | Inserts a row with `id = 89` and `name = 'Best School'` |
| `8-count_89.sql` | Displays the number of records where `id = 89` |
| `9-full_creation.sql` | Creates `second_table` and adds multiple records |
| `10-top_score.sql` | Lists all records in `second_table` ordered by `score` (descending) |
| `11-best_score.sql` | Displays records with `score >= 10` |
| `12-no_cheating.sql` | Updates Bob's score to 10 using his name only |
| `13-change_class.sql` | Deletes records with `score <= 5` |
| `14-average.sql` | Displays the average `score` from `second_table` |
| `15-groups.sql` | Groups records by `score` and counts how many share the same score |
| `16-no_link.sql` | Lists records with non-empty `name`, sorted by `score` descending |

### 💻 Example Usage

<pre>
-- 0-list_databases.sql -- Lists all databases

SHOW DATABASES;

-- Output:
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
</pre>

---

<pre>
-- 8-count_89.sql -- Count how many times id = 89 appears in first_table

SELECT COUNT(*) FROM first_table WHERE id = 89;

-- Output:
+----------+
| COUNT(*) |
+----------+
|    3     |
+----------+
</pre>



##� Author
Rateel Bahathek

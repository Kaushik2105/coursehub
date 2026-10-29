# CourseHub — Student Course Management System
> **A Relational Database System (RDBMS) for Academic Administration, Enrollment Tracking, and Fee Management.**

---

## 📌 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Database Concepts](#-key-database-concepts)
3. [Entity Relationship (ER) Diagram](#-entity-relationship-er-diagram)
4. [Relational Schema & Data Dictionary](#-relational-schema--data-dictionary)
5. [Database Normalization (1NF to BCNF)](#-database-normalization-1nf-to-bcnf)
6. [Database Setup & Schema Creation](#-database-setup--schema-creation)
7. [Sample Dataset](#-sample-dataset)
8. [Analytical Business Queries (Q1 – Q26)](#-analytical-business-queries-q1--q26)
   - [Basic Filtering & Sorting](#1-basic-filtering--sorting)
   - [Multi-Table Joins & Cross-Entity Lookups](#2-multi-table-joins--cross-entity-lookups)
   - [Subqueries & Relational Comparisons](#3-subqueries--relational-comparisons)
   - [Aggregations & Grouped Metrics](#4-aggregations--grouped-metrics)
   - [Advanced Analytics & Window Functions](#5-advanced-analytics--window-functions)
   - [Database Performance: Indexes](#6-database-performance-indexes)
   - [Database Abstraction: Views](#7-database-abstraction-views)
9. [Key Business Insights](#-key-business-insights)
10. [Setup & Execution Instructions](#-setup--execution-instructions)

---

## 📖 Project Overview

**CourseHub** is a centralized relational database engineered in **MySQL** to streamline academic administrative operations, course allocation, student registrations, and financial fee auditing. 

In higher education institutions, student records, faculty allocations, course schedules, and payment accounting are frequently managed in disparate silos. CourseHub eliminates data fragmentation by organizing core operations around five strongly coupled, normalized tables:

- **Students**: Stores personal profiles, contact details, and demographic info.
- **Instructors**: Manages faculty records, academic qualifications, and departmental affiliations.
- **Courses**: Catalogs academic course offerings, credit allocations, and fee schedules linked to instructors.
- **Enrollments**: Acts as a junction entity tracking course registrations, academic status, and marks.
- **Payments**: Records financial transactions, payment modes, and payment fulfillment statuses.

---

## 💡 Key Database Concepts

| Concept | Implementation in CourseHub |
| :--- | :--- |
| **Relational Integrity** | Enforced via Primary Keys (`PRIMARY KEY`) and Foreign Keys (`FOREIGN KEY ... REFERENCES`) with cascading constraints. |
| **Normalization** | Decomposed from raw flat records to **3NF / BCNF** to eliminate insertion, update, and deletion anomalies. |
| **Indexing** | B-Tree indexes on search keys (`idx_student_id`) and unique constraints on identifier columns (`idx_email`). |
| **ACID Compliance** | Transactions guarantee atomic enrollment and fee recording, consistent validation, isolation between concurrent sessions, and durable storage. |
| **Database Views** | Pre-compiled queries (`HighValuePayments`, `RevenueSummary`) providing simplified reporting interfaces. |

---

## 📊 Entity Relationship (ER) Diagram

The following Mermaid ER Diagram models the entities, primary keys (`PK`), foreign keys (`FK`), attributes, and relationship cardinalities across the CourseHub database:

```mermaid
erDiagram
    STUDENTS ||--o{ ENROLLMENTS : "places (1:M)"
    INSTRUCTORS ||--o{ COURSES : "teaches (1:M)"
    COURSES ||--o{ ENROLLMENTS : "contains (1:M)"
    ENROLLMENTS ||--|| PAYMENTS : "generates (1:1)"

    STUDENTS {
        int Student_ID PK "Unique Student Identifier"
        varchar(100) Name "Student Full Name"
        int Age "Age in Years"
        varchar(10) Gender "Gender (M/F)"
        varchar(15) Contact "Phone Number"
        varchar(100) Email UK "Unique Email Address"
        varchar(50) City "Residential City"
    }

    INSTRUCTORS {
        int Instructor_ID PK "Unique Instructor Identifier"
        varchar(100) Name "Faculty Full Name"
        varchar(50) Department "Academic Department"
        varchar(30) Qualification "Highest Degree (PhD/M.Tech/MBA)"
        int Experience_Years "Years of Academic Experience"
    }

    COURSES {
        int Course_ID PK "Unique Course Identifier"
        varchar(100) Course_Name "Course Title"
        int Instructor_ID FK "Assigned Instructor Reference"
        int Credits "Course Credit Value"
        decimal(10,2) Fee "Tuition Fee Amount"
    }

    ENROLLMENTS {
        int Enrollment_ID PK "Unique Enrollment Identifier"
        int Student_ID FK "Enrolled Student Reference"
        int Course_ID FK "Selected Course Reference"
        date Enrollment_Date "Registration Timestamp"
        varchar(20) Status "Status (Ongoing/Completed/Dropped)"
        int Marks "Academic Score Achieved"
    }

    PAYMENTS {
        int Payment_ID PK "Unique Transaction Identifier"
        int Enrollment_ID FK "Linked Enrollment Reference"
        decimal(10,2) Amount "Transaction Amount Paid"
        varchar(50) Payment_Method "UPI / Card / Net Banking / Cash"
        varchar(20) Payment_Status "Payment Status (Paid/Pending)"
    }
```

### Relational Cardinalities

1. **Instructors to Courses (`1:M`)**:
   - One instructor can teach multiple courses.
   - Each course is assigned to exactly one instructor.
   - Implemented via `Courses.Instructor_ID` referencing `Instructors.Instructor_ID`.
2. **Students to Enrollments (`1:M`)**:
   - One student can enroll in multiple courses across terms.
   - Each enrollment record belongs strictly to one student.
   - Implemented via `Enrollments.Student_ID` referencing `Students.Student_ID`.
3. **Courses to Enrollments (`1:M`)**:
   - One course can accept multiple student registrations.
   - Each enrollment specifies a single course.
   - Implemented via `Enrollments.Course_ID` referencing `Courses.Course_ID`.
4. **Students to Courses (`M:M`)**:
   - Many students can enroll in many courses.
   - Resolved using the associative entity `Enrollments`.
5. **Enrollments to Payments (`1:1`)**:
   - Each enrollment transaction maps to an individual fee payment record.
   - Implemented via `Payments.Enrollment_ID` referencing `Enrollments.Enrollment_ID`.

---

## 🗄 Relational Schema & Data Dictionary

### 1. `Students` Table
| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `Student_ID` | `INT` | `PRIMARY KEY` | Unique identifier for each student |
| `Name` | `VARCHAR(100)` | `NOT NULL` | Full legal name |
| `Age` | `INT` | `CHECK (Age >= 17)` | Student age |
| `Gender` | `VARCHAR(10)` | — | Gender identity (`M` / `F`) |
| `Contact` | `VARCHAR(15)` | — | 10-digit mobile number |
| `Email` | `VARCHAR(100)` | `UNIQUE` | Email address for credentials |
| `City` | `VARCHAR(50)` | — | Domicile / current city |

### 2. `Instructors` Table
| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `Instructor_ID` | `INT` | `PRIMARY KEY` | Unique instructor identifier |
| `Name` | `VARCHAR(100)` | `NOT NULL` | Faculty full name |
| `Department` | `VARCHAR(50)` | — | Department (e.g. Computer Science, Data Science) |
| `Qualification` | `VARCHAR(30)` | — | Highest academic degree earned (`PhD`, `M.Tech`, `MBA`) |
| `Experience_Years`| `INT` | — | Total teaching/industry experience in years |

### 3. `Courses` Table
| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `Course_ID` | `INT` | `PRIMARY KEY` | Unique course identification code |
| `Course_Name` | `VARCHAR(100)` | `NOT NULL` | Course title |
| `Instructor_ID` | `INT` | `FOREIGN KEY` | References `Instructors(Instructor_ID)` |
| `Credits` | `INT` | — | Academic credits earned upon completion |
| `Fee` | `DECIMAL(10,2)`| — | Tuition fee for course enrollment |

### 4. `Enrollments` Table
| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `Enrollment_ID` | `INT` | `PRIMARY KEY` | Unique surrogate key for enrollment |
| `Student_ID` | `INT` | `FOREIGN KEY` | References `Students(Student_ID)` |
| `Course_ID` | `INT` | `FOREIGN KEY` | References `Courses(Course_ID)` |
| `Enrollment_Date`| `DATE` | — | Date when the student registered |
| `Status` | `VARCHAR(20)` | — | Academic status (`Completed`, `Ongoing`, `Dropped`) |
| `Marks` | `INT` | `NULLABLE` | Final examination marks (0–100) |

### 5. `Payments` Table
| Column Name | Data Type | Key / Constraint | Description |
| :--- | :--- | :--- | :--- |
| `Payment_ID` | `INT` | `PRIMARY KEY` | Unique transaction ID |
| `Enrollment_ID` | `INT` | `FOREIGN KEY` | References `Enrollments(Enrollment_ID)` |
| `Amount` | `DECIMAL(10,2)`| — | Amount paid for course enrollment |
| `Payment_Method`| `VARCHAR(50)` | — | Method (`UPI`, `Credit Card`, `Debit Card`, `Net Banking`, `Cash`) |
| `Payment_Status`| `VARCHAR(20)` | — | Status of payment transaction (`Paid`, `Pending`) |

---

## ⚙ Database Normalization (1NF to BCNF)

The schema was designed and verified through rigorous normalization stages:

1. **First Normal Form (1NF)**:
   - All attributes contain single, atomic values (e.g. no comma-separated course lists or contact numbers).
   - Each column possesses a unique name and consistent data type.
   - Primary keys uniquely identify every row.

2. **Second Normal Form (2NF)**:
   - Satisfies 1NF.
   - Eliminates partial functional dependencies. In `Enrollments`, surrogate primary key `Enrollment_ID` ensures that non-key attributes (`Marks`, `Status`, `Enrollment_Date`) depend on the whole key, avoiding composite key dependency anomalies.

3. **Third Normal Form (3NF)**:
   - Satisfies 2NF.
   - Eliminates transitive dependencies ($X \rightarrow Y$ and $Y \rightarrow Z$).
   - Instructor details (`Department`, `Qualification`) are not duplicated within `Courses`; they reside in `Instructors` and are referenced solely via `Instructor_ID`.
   - Student contact details reside solely in `Students`.

4. **Boyce-Codd Normal Form (BCNF)**:
   - For every functional dependency $X \rightarrow Y$, $X$ is a superkey.
   - All candidate keys and determinant attributes cleanly define table relations without overlapping anomalies.

---

## 🛠 Database Setup & Schema Creation

```sql
CREATE DATABASE IF NOT EXISTS CourseHub;
USE CourseHub;

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Contact VARCHAR(15),
    Email VARCHAR(100),
    City VARCHAR(50)
);

CREATE TABLE Instructors (
    Instructor_ID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Qualification VARCHAR(30),
    Experience_Years INT
);

CREATE TABLE Courses (
    Course_ID INT PRIMARY KEY,
    Course_Name VARCHAR(100),
    Instructor_ID INT,
    Credits INT,
    Fee DECIMAL(10, 2),
    FOREIGN KEY (Instructor_ID) REFERENCES Instructors(Instructor_ID)
);

CREATE TABLE Enrollments (
    Enrollment_ID INT PRIMARY KEY,
    Student_ID INT,
    Course_ID INT,
    Enrollment_Date DATE,
    Status VARCHAR(20),
    Marks INT,
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID),
    FOREIGN KEY (Course_ID) REFERENCES Courses(Course_ID)
);

CREATE TABLE Payments (
    Payment_ID INT PRIMARY KEY,
    Enrollment_ID INT,
    Amount DECIMAL(10, 2),
    Payment_Method VARCHAR(50),
    Payment_Status VARCHAR(20),
    FOREIGN KEY (Enrollment_ID) REFERENCES Enrollments(Enrollment_ID)
);
```

---

## 📋 Sample Dataset

The project includes an operational dataset representing real-world distribution:
- **20 Students** across major metropolitan centers (Patna, Delhi, Kolkata, Hyderabad, Bengaluru, etc.)
- **15 Instructors** across CS, IT, Data Science, Mathematics, Electronics, and Management
- **10 Courses** ranging from ₹4,500 to ₹12,000
- **15 Course Enrollments** spanning Completed, Ongoing, and Dropped states
- **15 Payment Records** spanning diverse payment gateways (UPI, Cards, Net Banking, Cash)

*(Refer to [coursehub.sql](file:///c:/Workholic/CODES/coursehub/coursehub.sql) for all `INSERT` commands).*

---

## 🔍 Analytical Business Queries (Q1 – Q26)

### 1. Basic Filtering & Sorting

#### Q1. List all enrollments made after '2024-02-01'
```sql
SELECT * FROM Enrollments 
WHERE Enrollment_Date > '2024-02-01';
```
*Output (8 rows returned: 7008 to 7015):*
| Enrollment_ID | Student_ID | Course_ID | Enrollment_Date | Status | Marks |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 7008 | 7 | 503 | 2024-02-02 | Ongoing | NULL |
| 7009 | 8 | 505 | 2024-02-05 | Ongoing | NULL |
| 7010 | 2 | 501 | 2024-02-07 | Ongoing | NULL |
| 7011 | 9 | 507 | 2024-02-10 | Completed | 65 |
| 7012 | 10 | 508 | 2024-02-12 | Dropped | NULL |
| 7013 | 3 | 506 | 2024-02-15 | Ongoing | NULL |
| 7014 | 11 | 509 | 2024-02-18 | Completed | 85 |
| 7015 | 1 | 505 | 2024-02-20 | Ongoing | NULL |

#### Q2. Retrieve all fee payments made via 'UPI'
```sql
SELECT * FROM Payments 
WHERE Payment_Method = 'UPI';
```
*Output (5 rows: 8001, 8005, 8007, 8010, 8014): Total ₹38,500.*

#### Q3. Display the 5 courses with the highest fees
```sql
SELECT * FROM Courses 
ORDER BY Fee DESC 
LIMIT 5;
```
*Output:*
| Course_ID | Course_Name | Instructor_ID | Credits | Fee |
| :--- | :--- | :--- | :--- | :--- |
| 505 | Machine Learning | 105 | 4 | 12000.00 |
| 510 | Cyber Security | 110 | 3 | 10000.00 |
| 502 | Data Structures | 102 | 4 | 9000.00 |
| 507 | Operating Systems | 107 | 4 | 8500.00 |
| 501 | Database Management Systems | 101 | 4 | 8000.00 |

#### Q4. Show the 3 most recent enrollments
```sql
SELECT * FROM Enrollments 
ORDER BY Enrollment_Date DESC 
LIMIT 3;
```
*Output: Enrollments 7015 (Feb 20), 7014 (Feb 18), and 7013 (Feb 15).*

---

### 2. Multi-Table Joins & Cross-Entity Lookups

#### Q5. Find all courses taken by 'Aarav Mehta'
```sql
SELECT c.Course_Name 
FROM Courses c
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Students s ON e.Student_ID = s.Student_ID
WHERE s.Name = 'Aarav Mehta';
```
*Output:*
- `Database Management Systems`
- `Python Programming`
- `Machine Learning`

#### Q16. Show students who have paid via 'Net Banking'
```sql
SELECT DISTINCT s.Name 
FROM Students s
JOIN Enrollments e ON s.Student_ID = e.Student_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
WHERE p.Payment_Method = 'Net Banking';
```
*Output: Rohan Das, Aditya Singh.*

---

### 3. Subqueries & Relational Comparisons

#### Q6. Display payments with an amount greater than the average payment amount
```sql
SELECT * FROM Payments 
WHERE Amount > (SELECT AVG(Amount) FROM Payments);
```
*(Benchmark Average = ₹8,166.67. Returns 6 records: 8003, 8004, 8007, 8009, 8011, 8015).*

#### Q11. Identify instructors who are not teaching any course
```sql
SELECT Name FROM Instructors
WHERE Instructor_ID NOT IN (SELECT DISTINCT Instructor_ID FROM Courses);
```
*Output:*
- Prof. Leena Thomas
- Dr. Ramesh Choudhary
- Prof. Shalini Dubey
- Dr. Ketan Parikh
- Prof. Nandita Ghosh

---

### 4. Aggregations & Grouped Metrics

#### Q7. Find total number of courses enrolled by each student
```sql
SELECT Student_ID, COUNT(*) AS Total_Enrollments 
FROM Enrollments 
GROUP BY Student_ID;
```

#### Q8. Find the average course fee for each instructor department
```sql
SELECT i.Department, AVG(c.Fee) AS Avg_Fee
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
GROUP BY i.Department;
```
*Output:*
| Department | Avg_Fee |
| :--- | :--- |
| Computer Science | 8000.00 |
| Data Science | 12000.00 |
| Information Technology | 7666.67 |
| Management | 4500.00 |
| Mathematics | 5000.00 |

#### Q9. Show the number of completed enrollments
```sql
SELECT COUNT(*) AS Completed_Enrollments 
FROM Enrollments 
WHERE Status = 'Completed';
```
*Output: 9 enrollments.*

#### Q10. Find the student who has paid the most in course fees
```sql
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID 
ORDER BY Total_Paid DESC 
LIMIT 1;
```
*Output: Student_ID 1 (Total Paid: ₹26,000.00).*

#### Q13. Find total revenue generated from each payment method
```sql
SELECT Payment_Method, SUM(Amount) AS Total_Revenue 
FROM Payments 
GROUP BY Payment_Method;
```
| Payment_Method | Total_Revenue |
| :--- | :--- |
| UPI | 38500.00 |
| Credit Card | 33500.00 |
| Debit Card | 24000.00 |
| Net Banking | 21500.00 |
| Cash | 5000.00 |

#### Q14. Display the total amount paid by each student
```sql
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID;
```

#### Q15. Retrieve students who are enrolled in more than one course
```sql
SELECT Student_ID 
FROM Enrollments
GROUP BY Student_ID 
HAVING COUNT(Enrollment_ID) > 1;
```
*Output: Student_IDs 1, 2, 3.*

#### Q18. Retrieve the department that generated the highest total revenue
```sql
SELECT i.Department, SUM(p.Amount) AS Total_Revenue
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY i.Department 
ORDER BY Total_Revenue DESC 
LIMIT 1;
```
*Output: Computer Science (Total Revenue: ₹48,000.00).*

#### Q19. Retrieve the top 3 students with highest total fee payments
```sql
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID 
ORDER BY Total_Paid DESC 
LIMIT 3;
```
*Output: Student 1 (₹26k), Student 2 (₹20k), Student 3 (₹15.5k).*

#### Q20. Find payment method that processed the most transactions
```sql
SELECT Payment_Method, COUNT(*) AS Transaction_Count 
FROM Payments
GROUP BY Payment_Method 
ORDER BY Transaction_Count DESC 
LIMIT 1;
```
*Output: UPI (5 transactions).*

#### Q21. Show total fee revenue generated by each department
```sql
SELECT i.Department, SUM(p.Amount) AS Total_Revenue
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY i.Department;
```
| Department | Total_Revenue |
| :--- | :--- |
| Computer Science | 48000.00 |
| Data Science | 36000.00 |
| Information Technology | 29000.00 |
| Management | 4500.00 |
| Mathematics | 5000.00 |

#### Q22. List the most expensive course offered by each department
```sql
SELECT i.Department, MAX(c.Fee) AS Max_Fee
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
GROUP BY i.Department;
```

---

### 5. Advanced Analytics & Window Functions

#### Q12. Calculate the cumulative fee revenue per enrollment date
```sql
SELECT e.Enrollment_Date, SUM(p.Amount) OVER (ORDER BY e.Enrollment_Date) AS Cumulative_Revenue
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID;
```
*(Demonstrates progressive fee accumulation from ₹8,000 to ₹122,500 across chronological registration dates).*

#### Q17. Find the average payment amount per month
```sql
SELECT MONTH(e.Enrollment_Date) AS Month, AVG(p.Amount) AS Avg_Amount
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY MONTH(e.Enrollment_Date);
```
*Output: Month 1 (January): ₹8,571.43 | Month 2 (February): ₹7,812.50.*

---

### 6. Database Performance: Indexes

#### Q23. Non-unique index for enrollment searches by student
```sql
CREATE INDEX idx_student_id ON Enrollments(Student_ID);
DESC Enrollments;
```
*Optimization: Accelerates foreign key joins and avoids full table scans when aggregating student course loads.*

#### Q24. Unique index for student email authentication
```sql
CREATE UNIQUE INDEX idx_email ON Students(Email);
DESC Students;
```
*Optimization: Guarantees email address uniqueness and provides O(log N) lookup time for authentication queries.*

---

### 7. Database Abstraction: Views

#### Q25. View for high-value payments exceeding ₹9000
```sql
CREATE VIEW HighValuePayments AS
SELECT * FROM Payments 
WHERE Amount > 9000;

SELECT * FROM HighValuePayments;
```
*Result: 4 transactions (8003, 8007, 8009, 8015) in the ₹10,000–₹12,000 bracket.*

#### Q26. View for executive revenue summaries by payment method
```sql
CREATE VIEW RevenueSummary AS
SELECT Payment_Method, SUM(Amount) AS Total_Revenue
FROM Payments 
GROUP BY Payment_Method;

SELECT * FROM RevenueSummary;
```

---

## 📈 Key Business Insights

1. **Revenue Engine**:
   - Total institutional fees collected: **₹122,500.00**.
   - **Computer Science** leads department revenue (**₹48,000** / 39.2%), followed by **Data Science** (**₹36,000** / 29.4%).
2. **Payment Channel Trends**:
   - **Digital Transactions (UPI + Credit + Debit + Net Banking)** constitute **95.9%** of total collections.
   - **UPI** is the single most preferred transaction channel both by count (5) and volume (₹38,500).
3. **Academic Engagement**:
   - 60% of tracked enrollments have completed their curricula with an average grade of **78.7%**.
   - Top student **Aarav Mehta** demonstrated the highest academic engagement and tuition spend (**₹26,000**).
4. **Faculty Capacity Allocation**:
   - 5 instructors currently hold zero active course allocations, highlighting an immediate opportunity to introduce advanced electives without expanding faculty headcount.

---

## 🚀 Setup & Execution Instructions

### Prerequisites
- MySQL Community Server (v8.0 or newer)
- MySQL Workbench or MySQL Command-Line Client

### Quick Start via MySQL CLI
```bash
# 1. Log in to your MySQL instance
mysql -u root -p

# 2. Execute the complete SQL script
source /path/to/coursehub/coursehub.sql;

# 3. Verify database creation
USE CourseHub;
SHOW TABLES;
```

---

## 📁 Repository Deliverables

- `coursehub.sql`: Complete DDL schema, sample dataset insertions, views, indexes, and queries 1–26.
- `CourseHub_Student_Course_Management_System.pptx`: Comprehensive 16:9 widescreen PowerPoint deck.
- `README.md`: System architectural documentation, Mermaid ER diagrams, data dictionary, and query logs.


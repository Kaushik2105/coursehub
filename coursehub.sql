CREATE DATABASE IF NOT EXISTS CourseHub;
USE CourseHub;

DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Students;

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

INSERT INTO Students VALUES
(1, 'Aarav Mehta', 20, 'M', '9876500001', 'aarav.mehta@gmail.com', 'Patna'),
(2, 'Ishita Sharma', 21, 'F', '9876500002', 'ishita.sharma@yahoo.com', 'Delhi'),
(3, 'Rohan Das', 22, 'M', '9876500003', 'rohan.das@gmail.com', 'Kolkata'),
(4, 'Priya Kumari', 19, 'F', '9876500004', 'priya.kumari@outlook.com', 'Ranchi'),
(5, 'Kunal Verma', 23, 'M', '9876500005', 'kunal.verma@gmail.com', 'Lucknow'),
(6, 'Sneha Reddy', 20, 'F', '9876500006', 'sneha.reddy@yahoo.com', 'Hyderabad'),
(7, 'Aditya Singh', 21, 'M', '9876500007', 'aditya.singh@gmail.com', 'Patna'),
(8, 'Neha Gupta', 22, 'F', '9876500008', 'neha.gupta@gmail.com', 'Jaipur'),
(9, 'Vivek Nair', 24, 'M', '9876500009', 'vivek.nair@outlook.com', 'Chennai'),
(10, 'Ananya Iyer', 19, 'F', '9876500010', 'ananya.iyer@gmail.com', 'Bengaluru'),
(11, 'Harsh Pandey', 21, 'M', '9876500011', 'harsh.pandey@yahoo.com', 'Varanasi'),
(12, 'Tanvi Joshi', 20, 'F', '9876500012', 'tanvi.joshi@gmail.com', 'Pune'),
(13, 'Mohit Kapoor', 23, 'M', '9876500013', 'mohit.kapoor@gmail.com', 'Delhi'),
(14, 'Sakshi Mishra', 22, 'F', '9876500014', 'sakshi.mishra@outlook.com', 'Bhopal'),
(15, 'Nikhil Rao', 25, 'M', '9876500015', 'nikhil.rao@gmail.com', 'Hyderabad'),
(16, 'Divya Bose', 20, 'F', '9876500016', 'divya.bose@yahoo.com', 'Kolkata'),
(17, 'Ayush Tiwari', 21, 'M', '9876500017', 'ayush.tiwari@gmail.com', 'Patna'),
(18, 'Kavya Menon', 19, 'F', '9876500018', 'kavya.menon@gmail.com', 'Kochi'),
(19, 'Sahil Khan', 24, 'M', '9876500019', 'sahil.khan@outlook.com', 'Mumbai'),
(20, 'Riya Chatterjee', 22, 'F', '9876500020', 'riya.chatterjee@gmail.com', 'Kolkata');

INSERT INTO Instructors VALUES
(101, 'Dr. Alok Srivastava', 'Computer Science', 'PhD', 14),
(102, 'Dr. Meenal Rathore', 'Computer Science', 'PhD', 11),
(103, 'Prof. Sandeep Bhatt', 'Information Technology', 'M.Tech', 9),
(104, 'Prof. Rekha Pillai', 'Information Technology', 'MCA', 7),
(105, 'Dr. Varun Malhotra', 'Data Science', 'PhD', 12),
(106, 'Prof. Anita Deshmukh', 'Computer Science', 'M.Tech', 8),
(107, 'Dr. Suresh Kulkarni', 'Computer Science', 'PhD', 18),
(108, 'Prof. Pallavi Sen', 'Mathematics', 'M.Sc', 10),
(109, 'Prof. Gaurav Arora', 'Management', 'MBA', 6),
(110, 'Dr. Farhan Ali', 'Information Technology', 'PhD', 15),
(111, 'Prof. Leena Thomas', 'Electronics', 'M.Tech', 9),
(112, 'Dr. Ramesh Choudhary', 'Physics', 'PhD', 20),
(113, 'Prof. Shalini Dubey', 'Management', 'MBA', 5),
(114, 'Dr. Ketan Parikh', 'Mathematics', 'PhD', 16),
(115, 'Prof. Nandita Ghosh', 'Data Science', 'M.Tech', 7);

INSERT INTO Courses VALUES
(501, 'Database Management Systems', 101, 4, 8000.00),
(502, 'Data Structures', 102, 4, 9000.00),
(503, 'Python Programming', 103, 3, 6000.00),
(504, 'Web Development', 104, 3, 7000.00),
(505, 'Machine Learning', 105, 4, 12000.00),
(506, 'Computer Networks', 106, 3, 6500.00),
(507, 'Operating Systems', 107, 4, 8500.00),
(508, 'Business Statistics', 108, 3, 5000.00),
(509, 'Digital Marketing', 109, 2, 4500.00),
(510, 'Cyber Security', 110, 3, 10000.00);

INSERT INTO Enrollments VALUES
(7001, 1, 501, '2024-01-08', 'Completed', 82),
(7002, 1, 503, '2024-01-10', 'Completed', 76),
(7003, 2, 505, '2024-01-12', 'Completed', 91),
(7004, 3, 502, '2024-01-15', 'Completed', 68),
(7005, 4, 501, '2024-01-18', 'Completed', 74),
(7006, 5, 504, '2024-01-20', 'Completed', 88),
(7007, 6, 510, '2024-01-22', 'Completed', 79),
(7008, 7, 503, '2024-02-02', 'Ongoing', NULL),
(7009, 8, 505, '2024-02-05', 'Ongoing', NULL),
(7010, 2, 501, '2024-02-07', 'Ongoing', NULL),
(7011, 9, 507, '2024-02-10', 'Completed', 65),
(7012, 10, 508, '2024-02-12', 'Dropped', NULL),
(7013, 3, 506, '2024-02-15', 'Ongoing', NULL),
(7014, 11, 509, '2024-02-18', 'Completed', 85),
(7015, 1, 505, '2024-02-20', 'Ongoing', NULL);

INSERT INTO Payments VALUES
(8001, 7001, 8000.00, 'UPI', 'Paid'),
(8002, 7002, 6000.00, 'Credit Card', 'Paid'),
(8003, 7003, 12000.00, 'Debit Card', 'Paid'),
(8004, 7004, 9000.00, 'Net Banking', 'Paid'),
(8005, 7005, 8000.00, 'UPI', 'Paid'),
(8006, 7006, 7000.00, 'Credit Card', 'Paid'),
(8007, 7007, 10000.00, 'UPI', 'Paid'),
(8008, 7008, 6000.00, 'Net Banking', 'Paid'),
(8009, 7009, 12000.00, 'Debit Card', 'Paid'),
(8010, 7010, 8000.00, 'UPI', 'Paid'),
(8011, 7011, 8500.00, 'Credit Card', 'Paid'),
(8012, 7012, 5000.00, 'Cash', 'Paid'),
(8013, 7013, 6500.00, 'Net Banking', 'Paid'),
(8014, 7014, 4500.00, 'UPI', 'Paid'),
(8015, 7015, 12000.00, 'Credit Card', 'Paid');

-- Verification Queries
SELECT * FROM Students;
SELECT * FROM Instructors;
SELECT * FROM Courses;
SELECT * FROM Enrollments;
SELECT * FROM Payments;

-- Q1. List all enrollments made after '2024-02-01'
SELECT * FROM Enrollments 
WHERE Enrollment_Date > '2024-02-01';

-- Q2. Retrieve all fee payments made via 'UPI'
SELECT * FROM Payments 
WHERE Payment_Method = 'UPI';

-- Q3. Display the 5 courses with the highest fees
SELECT * FROM Courses 
ORDER BY Fee DESC 
LIMIT 5;

-- Q4. Show the 3 most recent enrollments
SELECT * FROM Enrollments 
ORDER BY Enrollment_Date DESC 
LIMIT 3;

-- Q5. Find all courses taken by 'Aarav Mehta'
SELECT c.Course_Name 
FROM Courses c
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Students s ON e.Student_ID = s.Student_ID
WHERE s.Name = 'Aarav Mehta';

-- Q6. Display payments with an amount greater than the average payment amount
SELECT * FROM Payments 
WHERE Amount > (SELECT AVG(Amount) FROM Payments);

-- Q7. Find the total number of courses enrolled by each student
SELECT Student_ID, COUNT(*) AS Total_Enrollments 
FROM Enrollments 
GROUP BY Student_ID;

-- Q8. Find the average course fee for each instructor department
SELECT i.Department, AVG(c.Fee) AS Avg_Fee
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
GROUP BY i.Department;

-- Q9. Show the number of completed enrollments
SELECT COUNT(*) AS Completed_Enrollments 
FROM Enrollments 
WHERE Status = 'Completed';

-- Q10. Find the student who has paid the most in course fees
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID 
ORDER BY Total_Paid DESC 
LIMIT 1;

-- Q11. Identify instructors who are not teaching any course
SELECT Name FROM Instructors
WHERE Instructor_ID NOT IN (SELECT DISTINCT Instructor_ID FROM Courses);

-- Q12. Calculate the cumulative fee revenue per enrollment date
SELECT e.Enrollment_Date, SUM(p.Amount) OVER (ORDER BY e.Enrollment_Date) AS Cumulative_Revenue
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID;

-- Q13. Find the total revenue generated from each payment method
SELECT Payment_Method, SUM(Amount) AS Total_Revenue 
FROM Payments 
GROUP BY Payment_Method;

-- Q14. Display the total amount paid by each student
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID;

-- Q15. Retrieve students who are enrolled in more than one course
SELECT Student_ID 
FROM Enrollments
GROUP BY Student_ID 
HAVING COUNT(Enrollment_ID) > 1;

-- Q16. Show students who have paid via 'Net Banking'
SELECT DISTINCT s.Name 
FROM Students s
JOIN Enrollments e ON s.Student_ID = e.Student_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
WHERE p.Payment_Method = 'Net Banking';

-- Q17. Find the average payment amount per month
SELECT MONTH(e.Enrollment_Date) AS Month, AVG(p.Amount) AS Avg_Amount
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY MONTH(e.Enrollment_Date);

-- Q18. Retrieve the department that generated the highest total revenue
SELECT i.Department, SUM(p.Amount) AS Total_Revenue
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY i.Department 
ORDER BY Total_Revenue DESC 
LIMIT 1;

-- Q19. Retrieve the top 3 students with the highest total fee payments
SELECT e.Student_ID, SUM(p.Amount) AS Total_Paid
FROM Enrollments e 
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY e.Student_ID 
ORDER BY Total_Paid DESC 
LIMIT 3;

-- Q20. Find the payment method that has processed the most transactions
SELECT Payment_Method, COUNT(*) AS Transaction_Count 
FROM Payments
GROUP BY Payment_Method 
ORDER BY Transaction_Count DESC 
LIMIT 1;

-- Q21. Show the total fee revenue generated by each department
SELECT i.Department, SUM(p.Amount) AS Total_Revenue
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
JOIN Enrollments e ON c.Course_ID = e.Course_ID
JOIN Payments p ON e.Enrollment_ID = p.Enrollment_ID
GROUP BY i.Department;

-- Q22. List the most expensive course offered by each department
SELECT i.Department, MAX(c.Fee) AS Max_Fee
FROM Instructors i 
JOIN Courses c ON i.Instructor_ID = c.Instructor_ID
GROUP BY i.Department;

-- Q23. Create an index to search enrollments by student
CREATE INDEX idx_student_id ON Enrollments(Student_ID);
DESC Enrollments;

-- Q24. Create a unique index for student emails
CREATE UNIQUE INDEX idx_email ON Students(Email);
DESC Students;

-- Q25. Create a view to show payments above 9000
CREATE VIEW HighValuePayments AS
SELECT * FROM Payments 
WHERE Amount > 9000;

SELECT * FROM HighValuePayments;

-- Q26. Create a view for total revenue per payment method
CREATE VIEW RevenueSummary AS
SELECT Payment_Method, SUM(Amount) AS Total_Revenue
FROM Payments 
GROUP BY Payment_Method;

SELECT * FROM RevenueSummary;


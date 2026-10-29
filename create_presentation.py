import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    COLOR_BG_LIGHT = RGBColor(248, 250, 252)      # Slate 50
    COLOR_BG_DARK = RGBColor(15, 23, 42)          # Slate 900
    COLOR_PRIMARY = RGBColor(30, 58, 138)         # Blue 900
    COLOR_ACCENT = RGBColor(37, 99, 235)          # Blue 600
    COLOR_ACCENT_LIGHT = RGBColor(239, 246, 255)  # Blue 50
    COLOR_SUCCESS = RGBColor(16, 185, 129)        # Emerald 500
    COLOR_TEXT_MAIN = RGBColor(15, 23, 42)        # Slate 900
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)    # Slate 500
    COLOR_CARD_BG = RGBColor(255, 255, 255)       # White
    COLOR_CARD_BORDER = RGBColor(226, 232, 240)   # Slate 200
    COLOR_WHITE = RGBColor(255, 255, 255)

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    def add_header(slide, tag, title, subtitle=None):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = tag.upper()
        p0.font.name = "Arial"
        p0.font.size = Pt(10)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_ACCENT

        p1 = tf.add_paragraph()
        p1.text = title
        p1.font.name = "Arial"
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_MAIN

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Arial"
            p2.font.size = Pt(12)
            p2.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 1: Title Slide (Dark Navy Theme)
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, COLOR_BG_DARK)

    # Accent decorative pill
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(2.8), Inches(0.4))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge.line.color.rgb = COLOR_ACCENT
    badge.line.width = Pt(1.5)
    tf_b = badge.text_frame
    tf_b.text = "DATABASE SYSTEM PROJECT"
    tf_b.paragraphs[0].font.size = Pt(10)
    tf_b.paragraphs[0].font.bold = True
    tf_b.paragraphs[0].font.color.rgb = RGBColor(96, 165, 250)
    tf_b.paragraphs[0].alignment = PP_ALIGN.CENTER

    tbox1 = s1.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.5), Inches(2.8))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True
    p_t = tf1.paragraphs[0]
    p_t.text = "CourseHub: Student Course\nManagement System"
    p_t.font.name = "Arial"
    p_t.font.size = Pt(38)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_WHITE

    p_sub = tf1.add_paragraph()
    p_sub.text = "Relational Database Architecture, Data Integrity, and Analytical SQL Engine"
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # Metadata Card at bottom
    meta_card = add_card(s1, Inches(0.8), Inches(5.4), Inches(11.733), Inches(1.2), RGBColor(30, 41, 59), RGBColor(51, 65, 85))
    tf_meta = meta_card.text_frame
    tf_meta.word_wrap = True
    p_m = tf_meta.paragraphs[0]
    p_m.text = "Technology Stack: MySQL RDBMS | Schema: 5 Normalized Relational Tables | Total Queries: 26 Analytical Problems Solved"
    p_m.font.name = "Arial"
    p_m.font.size = Pt(12)
    p_m.font.bold = True
    p_m.font.color.rgb = COLOR_WHITE
    p_m2 = tf_meta.add_paragraph()
    p_m2.text = "Includes: 3NF/BCNF Normalization, Referential Integrity, Window Functions, Aggregate Reports, Custom Views & Indexing"
    p_m2.font.name = "Arial"
    p_m2.font.size = Pt(11)
    p_m2.font.color.rgb = RGBColor(148, 163, 184)

    # -------------------------------------------------------------------------
    # SLIDE 2: Project Overview & Motivation
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "Executive Summary", "Project Purpose & Core Objectives", "Designing a unified student management and fee accounting infrastructure")

    cards_data = [
        ("Problem Statement", "Educational institutions often face fragmented records across student registrations, course assignments, faculty management, and payment collections. Disjointed records result in data discrepancies, duplicate enrollments, and reconciliation bottlenecks.", COLOR_ACCENT),
        ("The CourseHub Solution", "CourseHub centralizes academic and financial operations into a single relational MySQL database. It links students, faculty, course offerings, enrollments, and fee transactions under strict referential constraints to guarantee integrity.", COLOR_SUCCESS),
        ("Key Deliverables", "• Normalized 5-table relational schema\n• Foreign key cascades & validation\n• 26 end-to-end analytical SQL queries\n• Performance indexing on email and enrollment keys\n• Reusable views for financial monitoring", COLOR_PRIMARY)
    ]

    for i, (ctitle, cdesc, ccolor) in enumerate(cards_data):
        card = add_card(s2, Inches(0.8 + i * 4.0), Inches(1.8), Inches(3.7), Inches(4.8))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.3)
        tf.margin_left = tf.margin_right = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = ctitle
        p.font.name = "Arial"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ccolor

        p_body = tf.add_paragraph()
        p_body.text = "\n" + cdesc
        p_body.font.name = "Arial"
        p_body.font.size = Pt(12)
        p_body.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------------------
    # SLIDE 3: Relational Architecture & ER Schema
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Database Architecture", "Entity-Relationship (ER) Schema Overview", "Visualizing entities, attributes, relationships, and foreign key mappings")

    entities = [
        ("Students", "Student_ID (PK)", "Name, Age, Gender,\nContact, Email, City", "20 Registered Students"),
        ("Instructors", "Instructor_ID (PK)", "Name, Department,\nQualification, Experience", "15 Faculty Members"),
        ("Courses", "Course_ID (PK)", "Course_Name, Credits, Fee\nFK: Instructor_ID", "10 Accredited Courses"),
        ("Enrollments", "Enrollment_ID (PK)", "Enrollment_Date, Status, Marks\nFK: Student_ID, Course_ID", "15 Course Registrations"),
        ("Payments", "Payment_ID (PK)", "Amount, Method, Status\nFK: Enrollment_ID", "15 Fee Transactions")
    ]

    for i, (ename, pk, attrs, count) in enumerate(entities):
        card = add_card(s3, Inches(0.8 + i * 2.4), Inches(1.8), Inches(2.2), Inches(3.2))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = ename
        p.font.name = "Arial"
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        p_pk = tf.add_paragraph()
        p_pk.text = pk
        p_pk.font.name = "Arial"
        p_pk.font.size = Pt(10)
        p_pk.font.bold = True
        p_pk.font.color.rgb = COLOR_ACCENT

        p_att = tf.add_paragraph()
        p_att.text = attrs
        p_att.font.name = "Arial"
        p_att.font.size = Pt(10)
        p_att.font.color.rgb = COLOR_TEXT_MAIN

        p_cnt = tf.add_paragraph()
        p_cnt.text = "\n" + count
        p_cnt.font.name = "Arial"
        p_cnt.font.size = Pt(9)
        p_cnt.font.color.rgb = COLOR_TEXT_MUTED

    # Bottom summary card for relationships
    rel_card = add_card(s3, Inches(0.8), Inches(5.3), Inches(11.733), Inches(1.6))
    tf_rel = rel_card.text_frame
    tf_rel.word_wrap = True
    tf_rel.margin_left = tf_rel.margin_right = Inches(0.3)
    p_rh = tf_rel.paragraphs[0]
    p_rh.text = "Key Relational Cardinalities & Constraints:"
    p_rh.font.name = "Arial"
    p_rh.font.size = Pt(13)
    p_rh.font.bold = True
    p_rh.font.color.rgb = COLOR_PRIMARY

    bullets = [
        "Instructors (1) ── (M) Courses: An instructor teaches multiple courses; each course has exactly one primary instructor.",
        "Students (M) ── (M) Courses: Resolved via junction table Enrollments, where each enrollment has a surrogate primary key (Enrollment_ID).",
        "Enrollments (1) ── (1) Payments: Exactly one payment transaction is generated per course enrollment, ensuring full financial traceability."
    ]
    for b in bullets:
        pb = tf_rel.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Arial"
        pb.font.size = Pt(11)
        pb.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------------------
    # SLIDE 4: Normalization & Data Integrity
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Data Modeling Rigor", "Database Normalization & ACID Properties", "Ensuring data consistency, zero redundancy, and transactional reliability")

    norm_steps = [
        ("1NF: Atomicity", "All fields contain atomic, indivisible values. No multi-valued attributes or repeating groups in any table.", "E.g., Contact and Email are discrete single attributes."),
        ("2NF: Full Dependency", "Tables have single-column primary keys (surrogate IDs), eliminating any partial functional dependency.", "All non-key columns depend wholly on table Primary Key."),
        ("3NF: Transitive Freedom", "Non-key attributes are strictly dependent only on primary keys, with transitive dependencies removed.", "Instructor info sits in Instructors table, not duplicated in Courses."),
        ("BCNF: Determinants", "Every determinant in the schema is a candidate key. Redundancy is minimized to near-zero.", "Enrollments & Payments cleanly decoupled with surrogate PKs.")
    ]

    for i, (title, desc, ex) in enumerate(norm_steps):
        card = add_card(s4, Inches(0.8 + i * 3.0), Inches(1.8), Inches(2.75), Inches(3.1))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        p_d = tf.add_paragraph()
        p_d.text = "\n" + desc
        p_d.font.name = "Arial"
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MAIN

        p_e = tf.add_paragraph()
        p_e.text = "\n" + ex
        p_e.font.name = "Arial"
        p_e.font.size = Pt(10)
        p_e.font.color.rgb = COLOR_TEXT_MUTED

    # ACID Card
    acid_card = add_card(s4, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.7))
    tf_acid = acid_card.text_frame
    tf_acid.word_wrap = True
    tf_acid.margin_left = tf_acid.margin_right = Inches(0.3)
    p_ah = tf_acid.paragraphs[0]
    p_ah.text = "ACID Transaction Guarantees in CourseHub:"
    p_ah.font.name = "Arial"
    p_ah.font.size = Pt(13)
    p_ah.font.bold = True
    p_ah.font.color.rgb = COLOR_SUCCESS

    acid_items = [
        "Atomicity: Course enrollment and payment creation succeed together or rollback completely.",
        "Consistency: Foreign key constraints prevent orphan payments or enrollments with non-existent students.",
        "Isolation: Concurrent student registrations do not conflict or cause double-booking anomalies.",
        "Durability: Committed student marks, fee receipts, and course records persist through system crashes."
    ]
    for a in acid_items:
        pa = tf_acid.add_paragraph()
        pa.text = "• " + a
        pa.font.name = "Arial"
        pa.font.size = Pt(11)
        pa.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------------------
    # SLIDE 5: Schema Implementation & Core Tables
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Physical Schema", "Table Schema & Data Type Specifications", "Structure of the 5 relational tables implementing CourseHub")

    table_data = [
        ("Table Name", "Primary Key", "Foreign Keys", "Key Attributes", "Volume"),
        ("Students", "Student_ID", "None", "Name, Age, Gender, Contact, Email, City", "20 Rows"),
        ("Instructors", "Instructor_ID", "None", "Name, Department, Qualification, Experience", "15 Rows"),
        ("Courses", "Course_ID", "Instructor_ID", "Course_Name, Credits, Fee", "10 Rows"),
        ("Enrollments", "Enrollment_ID", "Student_ID, Course_ID", "Enrollment_Date, Status, Marks", "15 Rows"),
        ("Payments", "Payment_ID", "Enrollment_ID", "Amount, Payment_Method, Payment_Status", "15 Rows")
    ]

    # Create table shape
    rows, cols = len(table_data), len(table_data[0])
    table_shape = s5.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(2.0)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(2.3)
    table.columns[3].width = Inches(4.2)
    table.columns[4].width = Inches(1.433)

    for r_idx, row in enumerate(table_data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(11)
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_PRIMARY
            else:
                p.font.color.rgb = COLOR_TEXT_MAIN
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_WHITE if r_idx % 2 == 1 else RGBColor(241, 245, 249)

    # -------------------------------------------------------------------------
    # SLIDE 6: Analytical Queries: Operational & Filtering
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "SQL Query Execution", "Operational Queries & Filtering (Q1 - Q7)", "Routine academic workflows and data exploration queries")

    ops_queries = [
        ("Q1: Date Range Filtering", "SELECT * FROM Enrollments WHERE Enrollment_Date > '2024-02-01';", "Filters 8 late enrollments occurring after Feb 1, 2024."),
        ("Q2: Payment Method Analysis", "SELECT * FROM Payments WHERE Payment_Method = 'UPI';", "Extracts all transactions paid via UPI (5 total records)."),
        ("Q3: Top Premium Courses", "SELECT * FROM Courses ORDER BY Fee DESC LIMIT 5;", "Identifies highest fee courses: ML (₹12k), Cyber Sec (₹10k), DS (₹9k)."),
        ("Q5: Multi-table Student Lookup", "SELECT c.Course_Name FROM Courses c JOIN Enrollments e ... WHERE s.Name = 'Aarav Mehta';", "Resolves 3 courses taken by student: DBMS, Python, and ML."),
        ("Q6: Above-Average Payments", "SELECT * FROM Payments WHERE Amount > (SELECT AVG(Amount)...);", "Identifies 6 high-value payments exceeding the ₹8,166.67 benchmark."),
        ("Q7: Student Enrollment Volume", "SELECT Student_ID, COUNT(*) FROM Enrollments GROUP BY Student_ID;", "Analyzes course load distribution across all 11 active students.")
    ]

    for i, (qname, qsql, qdesc) in enumerate(ops_queries):
        col = i % 2
        row = i // 2
        card = add_card(s6, Inches(0.8 + col * 5.95), Inches(1.8 + row * 1.7), Inches(5.75), Inches(1.55))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = qname
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        p_sql = tf.add_paragraph()
        p_sql.text = qsql
        p_sql.font.name = "Courier New"
        p_sql.font.size = Pt(9.5)
        p_sql.font.color.rgb = COLOR_ACCENT

        p_desc = tf.add_paragraph()
        p_desc.text = qdesc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 7: Analytical Queries: Aggregations & Joins
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "SQL Analytics", "Aggregations, Multi-Joins & Window Functions", "Complex management reporting and performance tracking (Q8 - Q17)")

    agg_queries = [
        ("Q8: Department Fee Averages", "SELECT i.Department, AVG(c.Fee) FROM Instructors i JOIN Courses c ... GROUP BY i.Department;", "Data Science leads with highest average fee (₹12,000), followed by CS (₹8,000)."),
        ("Q10: Top Student Spender", "SELECT e.Student_ID, SUM(p.Amount) FROM Enrollments e JOIN Payments p ... LIMIT 1;", "Student ID 1 (Aarav Mehta) paid highest overall course fees totaling ₹26,000."),
        ("Q11: Unallocated Faculty", "SELECT Name FROM Instructors WHERE Instructor_ID NOT IN (SELECT DISTINCT ...);", "Finds 5 instructors currently without assigned courses (e.g. Dr. Ketan Parikh)."),
        ("Q12: Cumulative Fee Revenue", "SELECT e.Enrollment_Date, SUM(p.Amount) OVER (ORDER BY e.Enrollment_Date)...;", "Calculates running cumulative fee collections from ₹8,000 to ₹122,500."),
        ("Q13: Revenue by Payment Channel", "SELECT Payment_Method, SUM(Amount) FROM Payments GROUP BY Payment_Method;", "UPI dominates collection (₹38.5k), closely followed by Credit Cards (₹33.5k)."),
        ("Q15: Multi-Course Enrollees", "SELECT Student_ID FROM Enrollments GROUP BY Student_ID HAVING COUNT(*) > 1;", "Identifies highly engaged students enrolled in multiple courses (Students 1, 2, 3).")
    ]

    for i, (qname, qsql, qdesc) in enumerate(agg_queries):
        col = i % 2
        row = i // 2
        card = add_card(s7, Inches(0.8 + col * 5.95), Inches(1.8 + row * 1.7), Inches(5.75), Inches(1.55))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        p.text = qname
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        p_sql = tf.add_paragraph()
        p_sql.text = qsql
        p_sql.font.name = "Courier New"
        p_sql.font.size = Pt(9.5)
        p_sql.font.color.rgb = COLOR_ACCENT

        p_desc = tf.add_paragraph()
        p_desc.text = qdesc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(9.5)
        p_desc.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 8: Performance Optimization: Indexes & Views
    # -------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "Database Performance", "Query Optimization with Indexes & Views", "Enhancing lookup speeds, indexing keys, and encapsulating query logic (Q23 - Q26)")

    # Left Column: Indexes
    card_idx = add_card(s8, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf_idx = card_idx.text_frame
    tf_idx.word_wrap = True
    tf_idx.margin_left = tf_idx.margin_right = Inches(0.3)
    tf_idx.margin_top = Inches(0.25)

    p_ih = tf_idx.paragraphs[0]
    p_ih.text = "Indexing Strategy (B-Tree Performance)"
    p_ih.font.name = "Arial"
    p_ih.font.size = Pt(16)
    p_ih.font.bold = True
    p_ih.font.color.rgb = COLOR_PRIMARY

    p_i1 = tf_idx.add_paragraph()
    p_i1.text = "\n1. Non-Unique Foreign Key Index (Q23)"
    p_i1.font.bold = True
    p_i1.font.size = Pt(12)
    p_i1.font.color.rgb = COLOR_ACCENT
    p_i1_sub = tf_idx.add_paragraph()
    p_i1_sub.text = "CREATE INDEX idx_student_id ON Enrollments(Student_ID);\n• Speeds up joins between Students and Enrollments.\n• Eliminates full-table scans during student academic record lookups."
    p_i1_sub.font.size = Pt(10.5)
    p_i1_sub.font.color.rgb = COLOR_TEXT_MAIN

    p_i2 = tf_idx.add_paragraph()
    p_i2.text = "\n2. Unique Constraint Index (Q24)"
    p_i2.font.bold = True
    p_i2.font.size = Pt(12)
    p_i2.font.color.rgb = COLOR_ACCENT
    p_i2_sub = tf_idx.add_paragraph()
    p_i2_sub.text = "CREATE UNIQUE INDEX idx_email ON Students(Email);\n• Guarantees no two students share the same email address.\n• Provides O(log N) lookup time for login and authentication queries."
    p_i2_sub.font.size = Pt(10.5)
    p_i2_sub.font.color.rgb = COLOR_TEXT_MAIN

    # Right Column: Views
    card_view = add_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    tf_view = card_view.text_frame
    tf_view.word_wrap = True
    tf_view.margin_left = tf_view.margin_right = Inches(0.3)
    tf_view.margin_top = Inches(0.25)

    p_vh = tf_view.paragraphs[0]
    p_vh.text = "Database Views (Abstraction & Security)"
    p_vh.font.name = "Arial"
    p_vh.font.size = Pt(16)
    p_vh.font.bold = True
    p_vh.font.color.rgb = COLOR_SUCCESS

    p_v1 = tf_view.add_paragraph()
    p_v1.text = "\n1. High-Value Payment View (Q25)"
    p_v1.font.bold = True
    p_v1.font.size = Pt(12)
    p_v1.font.color.rgb = COLOR_ACCENT
    p_v1_sub = tf_view.add_paragraph()
    p_v1_sub.text = "CREATE VIEW HighValuePayments AS\nSELECT * FROM Payments WHERE Amount > 9000;\n• Simplifies financial audits for large fees.\n• 4 major transactions captured (₹10k to ₹12k range)."
    p_v1_sub.font.size = Pt(10.5)
    p_v1_sub.font.color.rgb = COLOR_TEXT_MAIN

    p_v2 = tf_view.add_paragraph()
    p_v2.text = "\n2. Revenue Summary View (Q26)"
    p_v2.font.bold = True
    p_v2.font.size = Pt(12)
    p_v2.font.color.rgb = COLOR_ACCENT
    p_v2_sub = tf_view.add_paragraph()
    p_v2_sub.text = "CREATE VIEW RevenueSummary AS\nSELECT Payment_Method, SUM(Amount) AS Total_Revenue\nFROM Payments GROUP BY Payment_Method;\n• Delivers real-time executive summaries of payment channels."
    p_v2_sub.font.size = Pt(10.5)
    p_v2_sub.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------------------
    # SLIDE 9: Business Insights & Revenue Analysis
    # -------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, COLOR_BG_LIGHT)
    add_header(s9, "Business Intelligence", "Revenue Distribution & Department Metrics", "Key data discoveries derived from SQL analytical queries")

    metrics = [
        ("Total Revenue Collected", "₹122,500", "Across 15 student enrollments", COLOR_PRIMARY),
        ("Top Department", "Computer Science", "₹48,000 total revenue (39.2%)", COLOR_SUCCESS),
        ("Leading Payment Method", "UPI (₹38,500)", "5 transactions (31.4% total)", COLOR_ACCENT),
        ("Course Completion Rate", "60.0%", "9 Completed, 5 Ongoing, 1 Dropped", COLOR_PRIMARY)
    ]

    for i, (mtitle, mval, msub, mcolor) in enumerate(metrics):
        card = add_card(s9, Inches(0.8 + i * 2.95), Inches(1.8), Inches(2.8), Inches(1.8))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = mtitle
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MUTED

        p_v = tf.add_paragraph()
        p_v.text = mval
        p_v.font.name = "Arial"
        p_v.font.size = Pt(22)
        p_v.font.bold = True
        p_v.font.color.rgb = mcolor

        p_s = tf.add_paragraph()
        p_s.text = msub
        p_s.font.name = "Arial"
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = COLOR_TEXT_MAIN

    # Detailed Table for Payment Methods Breakdown
    detail_card = add_card(s9, Inches(0.8), Inches(3.9), Inches(11.733), Inches(2.9))
    tf_det = detail_card.text_frame
    tf_det.word_wrap = True
    tf_det.margin_left = tf_det.margin_right = Inches(0.3)
    tf_det.margin_top = Inches(0.2)

    p_dh = tf_det.paragraphs[0]
    p_dh.text = "Department Revenue & Payment Breakdown Summary:"
    p_dh.font.name = "Arial"
    p_dh.font.size = Pt(13)
    p_dh.font.bold = True
    p_dh.font.color.rgb = COLOR_PRIMARY

    summary_bullets = [
        "Computer Science generated highest gross receipts (₹48,000), driven by core DBMS, Operating Systems, and Data Structures courses.",
        "Data Science achieved the highest single per-course fee revenue (₹36,000) with Machine Learning at ₹12,000/enrollment.",
        "Digital Payments (UPI + Cards + Net Banking) account for 95.9% of all collections, while Cash accounted for only ₹5,000 (4.1%).",
        "Student Retention: 9 out of 15 enrollments have achieved 'Completed' status with an average passing score of 78.7 marks."
    ]
    for b in summary_bullets:
        pb = tf_det.add_paragraph()
        pb.text = "• " + b
        pb.font.name = "Arial"
        pb.font.size = Pt(11)
        pb.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------------------
    # SLIDE 10: Conclusion & Future Scope
    # -------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, COLOR_BG_LIGHT)
    add_header(s10, "Summary & Future Roadmap", "Project Conclusion & Technical Evolution", "Key takeaways and next-generation architecture recommendations")

    conclusions = [
        ("Project Achievements", [
            "Successfully normalized 5-table relational schema eliminating update/insertion anomalies.",
            "Formulated 26 high-impact queries spanning joins, window functions, and subqueries.",
            "Created reusable database views and indexes to boost read performance on core attributes."
        ]),
        ("Future Roadmap & Extensions", [
            "Full Web Portal: Build FastAPI / Node.js backend with React frontend for student self-service.",
            "Automated Invoicing: Implement database triggers to generate payment receipts upon enrollment.",
            "Role-Based Access Control (RBAC): Configure granular MySQL GRANT/REVOKE permissions for faculty vs accounts.",
            "Scalability: Introduce read-replicas and partition the Enrollments table by academic session year."
        ])
    ]

    for i, (ctitle, cbullets) in enumerate(conclusions):
        card = add_card(s10, Inches(0.8 + i * 5.95), Inches(1.8), Inches(5.75), Inches(5.0))
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.3)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = ctitle
        p.font.name = "Arial"
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        for b in cbullets:
            pb = tf.add_paragraph()
            pb.text = "\n• " + b
            pb.font.name = "Arial"
            pb.font.size = Pt(11.5)
            pb.font.color.rgb = COLOR_TEXT_MAIN

    # Save presentation
    output_filename = "CourseHub_Student_Course_Management_System.pptx"
    prs.save(output_filename)
    print(f"Presentation saved successfully as {output_filename}")

if __name__ == "__main__":
    create_deck()


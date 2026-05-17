# AI LMS Phase-Wise Roadmap

## Phase 1 — Build the Basic LMS

### Goal
Create a working LMS without AI.

### Features
Login / signup
Student, teacher, admin roles
Course creation
Lesson creation
Quiz creation (manual)
Student enrollment
Assignment submission
Grading panel
Dashboard

### Backend Modules
Auth
Users
Courses
Lessons
Quizzes
Assignments
Submissions
Grades

### Database Tables
users
roles
courses
course_modules
lessons
enrollments
quizzes
quiz_questions
quiz_attempts
assignments
submissions
grades

### Why Phase 1 Matters
AI features need clean course data, student data, and grading data.

---

## Phase 2 — Add One AI Feature Only: AI Tutor

### Goal
Create a simple chat assistant inside the LMS.

### Use Cases
Explain topic in easy language
Summarize lesson
Answer doubts
Create practice questions
Give next study suggestion

### What You Need
Chat UI in Next.js
/api/tutor/chat in FastAPI
Prompt template
Lesson content fetch logic

### Minimum Backend Tools / Functions
get_lesson_content(lesson_id)
get_student_progress(student_id)
search_notes(query)

### Output
A tutor chat that knows the student’s course context.

---

## Phase 3 — Add Quiz Generation

### Goal
Allow teacher to generate quizzes automatically from lesson content.

### Teacher Flow
1. Teacher opens lesson
2. Clicks **Generate Quiz**
3. Selects difficulty and number of questions
4. AI creates draft quiz
5. Teacher reviews and publishes

### Backend Functions
fetch_lesson_text(lesson_id)
generate_quiz(lesson_text, difficulty, question_count)
save_quiz(course_id, lesson_id, quiz_json)

### Important Rule
Teacher should always review quiz before publishing.

---

## Phase 4 — Add Grading Assistant

### Goal
AI helps teachers grade faster.

### Use Cases
Short answers
Descriptive answers
Rubric-based feedback
Grammar / clarity suggestions

### Flow
1. Student submits answer
2. Backend gets submission + rubric
3. AI gives score suggestion + feedback
4. Teacher reviews and confirms

### Backend Functions
get_submission(submission_id)
get_rubric(assignment_id)
grade_with_rubric(submission, rubric)
save_feedback(submission_id, feedback, score)

### Important Rule
Do not fully automate high-stakes grading at first. Keep teacher approval mandatory.

---

## Phase 5 — Add Learning Recommendations

### Goal
Show personalized next steps to students.

### Examples
Weak topic detection
Revision reminders
Next lesson recommendation
Practice quiz suggestion

### Functions
get_weak_topics(student_id)
get_completed_lessons(student_id)
recommend_next_topic(student_id, course_id)

---

## Phase 6 — Add Retrieval for Notes, PDFs, and Videos

### Goal
Let AI answer from actual study material.

### Additions
PDF upload
Transcript storage
Note indexing
Vector search / embeddings

### Why
So tutor answers are based on your own educational content, not only general model knowledge.

---

## Phase 7 — Add MCP Layer

### Goal
Expose your backend functions in a standardized tool format.

### Before MCP
Model calls normal function tools through your backend.

### After MCP
The same tools are exposed through an MCP server.

### Examples
get_student_progress
get_lesson_content
generate_quiz
grade_submission

### Why Add MCP Later?
Because first your tool logic should work properly. Then standardize it using MCP.

---

## Phase 8 — Add OpenClaw Only If Really Needed

### Use OpenClaw When
You want external channels like WhatsApp, Telegram, or Slack
You want broader agent orchestration
You want a gateway around multiple tool ecosystems
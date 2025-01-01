import streamlit as st
from resume_screening import ResumeScreening
from payroll_automation import PayrollProcessor
from interview_scheduling import InterviewScheduling
from training_recommender import TrainingRecommender
from performance_monitor import PerformanceMonitor

# Initialize all modules
resume_screening = ResumeScreening()
payroll_processor = PayrollProcessor()
interview_scheduling = InterviewScheduling()
training_recommender = TrainingRecommender()
performance_monitor = PerformanceMonitor()

# Streamlit app
st.title("HR AI Agent")

# Resume Screening
st.header("Resume Screening")
resume_text = st.text_area("Enter Resume Text")
job_description = st.text_area("Enter Job Description")
if st.button("Match Skills"):
    resume_skills = resume_screening.extract_skills(resume_text)
    matched_skills = resume_screening.match_skills(resume_skills, job_description)
    st.write("Matched Skills:", matched_skills)

# Payroll Automation
st.header("Payroll Automation")
employee_name = st.text_input("Employee Name")
salary = st.number_input("Salary", min_value=0)
deductions = st.number_input("Deductions", min_value=0)
taxes = st.number_input("Taxes", min_value=0)
benefits = st.number_input("Benefits", min_value=0)
if st.button("Process Payroll"):
    employee = {
        'name': employee_name,
        'salary': salary,
        'deductions': deductions,
        'taxes': taxes,
        'benefits': benefits
    }
    payroll_processor.add_employee(employee)
    payroll_data = payroll_processor.process_payroll()
    st.write("Payroll Data:", payroll_data)
    report = payroll_processor.generate_report()
    st.write(report)

# Interview Scheduling
st.header("Interview Scheduling")
candidate = st.text_input("Candidate Name")
interviewer = st.text_input("Interviewer Name")
datetime = st.text_input("Interview DateTime")
if st.button("Schedule Interview"):
    interview_scheduling.schedule_interview(candidate, interviewer, datetime)
    st.write(f"Scheduled interview for {candidate} with {interviewer} on {datetime}")

# Personalized Training Programs
st.header("Personalized Training Programs")
skills = st.text_area("Enter Skills (comma-separated)").split(',')
interests = st.text_area("Enter Interests (comma-separated)").split(',')
if st.button("Recommend Training"):
    employee_profile = {
        'skills': skills,
        'interests': interests
    }
    recommended_trainings = training_recommender.recommend(employee_profile)
    st.write("Recommended Training Programs:", recommended_trainings)

# Performance Monitoring
st.header("Performance Monitoring")
employee_name_pm = st.text_input("Employee Name (Performance Monitoring)")
tasks_completed = st.number_input("Tasks Completed", min_value=0)
quality_score = st.number_input("Quality Score", min_value=0)
feedback = st.text_area("Feedback")
if st.button("Add Performance Data"):
    performance_data = {
        'employee': employee_name_pm,
        'tasks_completed': tasks_completed,
        'quality_score': quality_score,
        'feedback': feedback
    }
    performance_monitor.add_data(performance_data)
    performance_monitor.analyze_performance()
    performance_report = performance_monitor.generate_report()
    st.write(performance_report)

import streamlit as st
import spacy
import schedule
import time
import subprocess
import sys

# Function to install spaCy model
def install_spacy_model():
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

# Check if spaCy model is installed, if not, install it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    install_spacy_model()
    nlp = spacy.load("en_core_web_sm")

# Resume Screening
class ResumeScreening:
    def __init__(self):
        self.nlp = nlp

    def extract_skills(self, resume_text):
        doc = self.nlp(resume_text)
        skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
        return skills

    def match_skills(self, resume_skills, job_description):
        job_doc = self.nlp(job_description)
        job_skills = [ent.text for ent in job_doc.ents if ent.label_ == 'SKILL']
        matched_skills = set(resume_skills).intersection(set(job_skills))
        return matched_skills

# Payroll Automation
class PayrollProcessor:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def process_payroll(self):
        payroll_data = []
        for employee in self.employees:
            net_salary = employee['salary'] - employee['deductions'] - employee['taxes'] + employee['benefits']
            payroll_data.append({'name': employee['name'], 'net_salary': net_salary})
        return payroll_data

    def generate_report(self):
        report = "Payroll Report:\n"
        for employee in self.employees:
            net_salary = employee['salary'] - employee['deductions'] - employee['taxes'] + employee['benefits']
            report += f"{employee['name']}: Net Salary = {net_salary}\n"
        return report

# Interview Scheduling
class InterviewScheduling:
    def __init__(self):
        self.interviews = []

    def schedule_interview(self, candidate, interviewer, datetime):
        self.interviews.append({'candidate': candidate, 'interviewer': interviewer, 'datetime': datetime})
        print(f"Scheduled interview for {candidate} with {interviewer} on {datetime}")

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

# Personalized Training Programs
class TrainingRecommender:
    def __init__(self):
        self.trainings = [
            {'title': 'Python for Data Science', 'skills': ['Python', 'Data Science']},
            {'title': 'Advanced Machine Learning', 'skills': ['Machine Learning', 'Deep Learning']},
            {'title': 'Data Analysis with Python', 'skills': ['Python', 'Data Analysis']}
        ]

    def recommend(self, employee_profile):
        recommended_trainings = []
        for training in self.trainings:
            if any(skill in employee_profile['skills'] for skill in training['skills']):
                recommended_trainings.append(training['title'])
        return recommended_trainings

# Performance Monitoring
class PerformanceMonitor:
    def __init__(self):
        self.performance_data = []

    def add_data(self, data):
        self.performance_data.append(data)

    def analyze_performance(self):
        for data in self.performance_data:
            print(f"Analyzing performance for {data['employee']}")

    def generate_report(self):
        report = "Performance Report:\n"
        for data in self.performance_data:
            report += f"{data['employee']}: Tasks Completed = {data['tasks_completed']}, Quality Score = {data['quality_score']}, Feedback = {data['feedback']}\n"
        return report

# Streamlit app
st.title("HR AI Agent")

# Resume Screening
st.header("Resume Screening")
resume_text = st.text_area("Enter Resume Text")
job_description = st.text_area("Enter Job Description")
if st.button("Match Skills"):
    resume_screening = ResumeScreening()
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
    payroll_processor = PayrollProcessor()
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
    interview_scheduling = InterviewScheduling()
    interview_scheduling.schedule_interview(candidate, interviewer, datetime)
    st.write(f"Scheduled interview for {candidate} with {interviewer} on {datetime}")

# Personalized Training Programs
st.header("Personalized Training Programs")
skills = st.text_area("Enter Skills (comma-separated)").split(',')
interests = st.text_area("Enter Interests (comma-separated)").split(',')
if st.button("Recommend Training"):
    training_recommender = TrainingRecommender()
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
    performance_monitor = PerformanceMonitor()
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

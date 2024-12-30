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

# Example usage

# Resume Screening
resume_text = """
John Doe
Experience in Python, Machine Learning, Deep Learning, and Data Analysis.
Worked at XYZ Corp as a Data Scientist.
"""
job_description = """
We are looking for a Data Scientist skilled in Python, Machine Learning, and Data Analysis.
"""
resume_skills = resume_screening.extract_skills(resume_text)
matched_skills = resume_screening.match_skills(resume_skills, job_description)
print("Matched Skills:", matched_skills)

# Payroll Automation
employee = {
    'name': 'John Doe',
    'salary': 5000,
    'deductions': 500,
    'taxes': 1000,
    'benefits': 300
}
payroll_processor.add_employee(employee)
payroll_data = payroll_processor.process_payroll()
print("Payroll Data:", payroll_data)
report = payroll_processor.generate_report()
print(report)

# Interview Scheduling
schedule.every().day.at("10:00").do(interview_scheduling.schedule_interview, candidate="John Doe", interviewer="Jane Smith", datetime="2024-01-05 10:00")
# Note: To actually run the scheduler, uncomment the line below
# interview_scheduling.run_scheduler()

# Personalized Training Programs
employee_profile = {
    'skills': ['Python', 'Machine Learning'],
    'interests': ['Data Science', 'Deep Learning']
}
recommended_trainings = training_recommender.recommend(employee_profile)
print("Recommended Training Programs:", recommended_trainings)

# Performance Monitoring
performance_data = {
    'employee': 'John Doe',
    'tasks_completed': 50,
    'quality_score': 85,
    'feedback': 'Good performance overall, needs improvement in time management'
}
performance_monitor.add_data(performance_data)
performance_monitor.analyze_performance()
performance_report = performance_monitor.generate_report()
print(performance_report)

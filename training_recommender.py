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

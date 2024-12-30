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

import schedule
import time

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

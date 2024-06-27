from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task
    def get_forecast(self):
        self.client.get("/forecast/Paris")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

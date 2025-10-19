from locust import HttpUser, task, between
import random

class WebSaitUsers(HttpUser):
    wait_time = between(1,4)
    host = 'http://127.0.0.1:8000/'
    @task(5)
    def home_page(self):
        self.client.get('/', name='GET /')

    @task(5)
    def prof_load_main_page(self):
        self.client.get('profession/', name='GET /')

    @task(10)
    def load_profession_index(self):
        self.client.get('profession/profession_index/', name='GET profession_index/')

    @task(3)
    def about_page(self):
        self.client.get('about/', name='GET about/')
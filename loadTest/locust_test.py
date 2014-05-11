# locustfile.py
# web UI: http://127.0.0.1:8089/

from locust import HttpLocust, TaskSet, task
import urllib2

class InteractiveClassroomTasks(TaskSet):
	min_wait = 5000
	max_wait = 15000

	@task
	def index(self):
		self.client.get("")

	@task
	def challenge_list(self):
		response = self.client.get("challengelist/", name="challengelist")

	@task
	def visit_challenges(self):
		challenge_ids = [1903522298, 941317042, 8675309, 1435162904]
		for id in challenge_ids:
			url = "challenge/%i" % id
			response = self.client.get(url, name="challenge/[id]")
			self.get_resources()

	def get_resources(self):
		self.client.get('css/codemirror.css')
		self.client.get('css/light-table.css')
		self.client.get('css/lint.css')
		self.client.get('css/normalize.css')
		self.client.get('css/style.css')
		self.client.get('js/codemirror.js')
		self.client.get('js/javascript.js')
		self.client.get('js/javascriptLint.js')
		self.client.get('js/jshint.js')
		self.client.get('js/lint.js')
		self.client.get('js/consoleCapture.js')
		self.client.get('js/evaluateSubmission.js')
		self.client.get('js/codeMirrorResize.js')

class InteractiveClassroomUser(HttpLocust):
	task_set = InteractiveClassroomTasks
	min_wait = 5000
	max_wait = 15000
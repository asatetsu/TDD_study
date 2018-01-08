# TODO: [x]テストメソッドを呼び出す
# TODO: [x]setUpを最初に呼び出す
# TODO: [x]tearDownをあとで呼び出す
# TODO: []テストメソッドが失敗したとしてもtearDownを呼び出す
# TODO: []複数のテストを走らせる
# TODO: []収集したテスト結果を出力する
# TODO: [x]WasRunで文字列をログに記録するs
class TestCase:
	def __init__(self,name):
		self.name = name
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def run(self):
		self.setUp()
		method = getattr(self,self.name)
		method()
		self.tearDown()
		return TestResult()


class WasRun(TestCase):
	def setUp(self):
		self.log = "setUp "
	def testMethod(self):
		self.log = self.log + "testMethod "
	def tearDown(self):
		self.log = self.log + "tearDown "

class TestResult:
	def __init__(self):
		self.runCount = 1
	def summary(self):
		return "%d run, 0 failed" % self.runCount

class TestCaseTest(TestCase):
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod tearDown " == test.log)
	def testResult(self):
		test = WasRun("testMethod")
		result = test.run()
		assert ("1 run, 0 failed" == result.summary())


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
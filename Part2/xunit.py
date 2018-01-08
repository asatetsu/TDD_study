# TODO: [x]テストメソッドを呼び出す
# TODO: [x]setUpを最初に呼び出す
# TODO: []tearDownをあとで呼び出す
# TODO: []テストメソッドが失敗したとしてもtearDownを呼び出す
# TODO: []複数のテストを走らせる
# TODO: []収集したテスト結果を出力する
class TestCase:
	def __init__(self,name):
		self.name = name
	def setUp(self):
		pass
	def run(self):
		self.setUp()
		method = getattr(self,self.name)
		method()


class WasRun(TestCase):
	def setUp(self):
		self.wasRun = None
		self.wasSetUp = 1

	def testMethod(self):
		self.wasRun = 1

class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")
	def testRunning(self):
		self.test.run()
		assert(self.test.wasRun)
	def testSetUp(self):
		self.test.run()
		assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
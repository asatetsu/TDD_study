# TODO: [x]テストメソッドを呼び出す
# TODO: []setUpを最初に呼び出す
# TODO: []tearDownをあとで呼び出す
# TODO: []テストメソッドが失敗したとしてもtearDownを呼び出す
# TODO: []複数のテストを走らせる
# TODO: []収集したテスト結果を出力する
class TestCase:
	def __init__(self,name):
		self.name = name
	def run(self):
		method = getattr(self,self.name)
		method()

class WasRun(TestCase):
	def __init__(self, name):
		self.wasRun = None
		super().__init__(name)
	def testMethod(self):
		self.wasRun = 1

class TestCaseTest(TestCase):
	def testRunning(self):
		test = WasRun("testMethod")
		assert(not test.wasRun)
		test.run()
		assert(test.wasRun)

TestCaseTest("testRunning").run()

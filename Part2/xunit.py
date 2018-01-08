# TODO: [x]テストメソッドを呼び出す
# TODO: [x]setUpを最初に呼び出す
# TODO: []tearDownをあとで呼び出す
# TODO: []テストメソッドが失敗したとしてもtearDownを呼び出す
# TODO: []複数のテストを走らせる
# TODO: []収集したテスト結果を出力する
# TODO: [x]WasRunで文字列をログに記録するs
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
		self.log = "setUp "
	def testMethod(self):
		self.log = self.log + "testMethod "

class TestCaseTest(TestCase):
	def setUp(self):
		self.test = WasRun("testMethod")
	def testTemplateMethod(self):
		self.test.run()
		assert("setUp testMethod " == self.test.log)

TestCaseTest("testTemplateMethod").run()
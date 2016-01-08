import application
import unittest

class SearchEngineTest(unittest.TestCase):
	"""docstring for ClassName"""

	#Test is_space
	def test_is_space(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.is_space(""), True)
		self.assertEqual(searcher.is_space(" "), True)
		self.assertEqual(searcher.is_space("hola"), False)

	#Test valid_url
	def test_valid_url(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.valid_url("jhgkhgkjhg"), False)

	#Test count_page
	def test_count_page(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.count_page("a", "aba"), 2)

	#Test minuscule
	def test_minuscule(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.minuscule("Y"), "y")

if __name__ == '__main__':
	unittest.main()
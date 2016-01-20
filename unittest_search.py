import application
import unittest

class Test_Search_Engine(unittest.TestCase):
	"""docstring for Test_Search_Engine"""

	#Test is_space
	def test_is_space(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.is_space(""), True)
		self.assertEqual(searcher.is_space(" "), True)
		self.assertEqual(searcher.is_space("hola"), False)

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
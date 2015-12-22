import application
import unittest

class Test_SearchEngine(unittest.TestCase):
	"""docstring for Test_SearchEngine"""

	#Test true_menu
	def test_true_menu(self):
		class_application = application.SearchEngine()
		self.assertEqual(class_application.true_menu("1"), "Valid option")
		self.assertEqual(class_application.true_menu("EXIT"), "Invalid option")

	#Test minuscule
	def test_minuscule(self):
		class_application = application.SearchEngine()
		self.assertTrue(class_application.minuscule("WORLD").islower())

	#Test page_one
	def test_page_one(self):
		class_application = application.SearchEngine()
		self.assertTrue(type(class_application.page_one("Carro", "https://es.wikipedia.org/wiki/Carro")) == int)

	#Test page_two
	def test_page_two(self):
		class_application = application.SearchEngine()
		self.assertTrue(type(class_application.page_two("Carro", "http://www.olx.com.ve/carros-cat-378")) == int)

if __name__ == '__main__':
	unittest.main()
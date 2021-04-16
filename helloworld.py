import unittest

class TestHelloWorld(unittest.TestCase):
	
	word = "Hello World"

	def test_hello_world(self):
		return(word)

	def test_upper_case(self):
		self.assertTrue(word.isupper())
		self.assertFalse(word.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the seperator is not a string
		with self.assertRaises(TypeError):
			s.split(16)


if __name__ == '__main__':
    unittest.main()


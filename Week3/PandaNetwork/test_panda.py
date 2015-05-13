import unittest
from social_net_for_pandas import Panda
from social_net_for_pandas import WrongEmail

class PandaTest(unittest.TestCase):

    def setUp(self):
        self.my_panda = Panda("Bard", "bard@pandamail.com", "male")

    def test_panda_constructor(self):
        self.assertTrue(isinstance(self.my_panda, Panda))
        self.assertEqual(self.my_panda._name, "Bard")
        self.assertEqual(self.my_panda._email, "bard@pandamail.com")
        self.assertEqual(self.my_panda._gender, "male")
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bard@pandamailcom", "male")
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bardpandamail.com", "male")
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bardpandamailcom", "male")



    def test_return_name(self):
        self.assertEqual(self.my_panda.name(), "Bard")

    def test_return_email(self):
        self.assertEqual(self.my_panda.email(), "bard@pandamail.com")

    def test_is_male(self):
        self.assertEqual(self.my_panda.isMale(), True)

    def test_is_famale(self):
        self.assertEqual(self.my_panda.isFemale(), False)

    def test_str_cast(self):
        str_cast = "I am Bard, I am male and my email is bard@pandamail.com"
        self.assertEquals(str(self.my_panda), str_cast)

    def test_eq(self):
        other_panda = Panda("Guardian", "guardian@pandamail.com", "male")
        self.assertNotEqual(self.my_panda, other_panda)
        self.assertEqual(self.my_panda, self.my_panda)

    def test_hash_function(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        result = hash(ivo)
        self.assertEqual(isinstance(result), int)



if __name__ == '__main__':
    unittest.main()

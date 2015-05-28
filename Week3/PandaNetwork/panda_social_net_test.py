import unittest
import json
from social_net_for_pandas import Panda, PandaSocialNetwork
from social_net_for_pandas import WrongEmail, PandaAlreadyThere, PandaAlreadyFriends

class PandaTest(unittest.TestCase):

    def setUp(self):
        self.my_panda = Panda("Bard", "bard@pandamail.com", "male")

    def test_panda_constructor(self):
        self.assertTrue(isinstance(self.my_panda, Panda))

    def test_name_getter(self):
        self.assertEqual(self.my_panda.name(), "Bard")

    def test_email_getter(self):
        self.assertEqual(self.my_panda.email(), "bard@pandamail.com")

    def test_gender_getter(self):
        self.assertEqual(self.my_panda.gender(), "male")

    def test_wrong_emails(self):
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bard@pandamailcom", "male")
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bardpandamail.com", "male")
        with self.assertRaises(WrongEmail):
            other_panda = Panda("Bard", "bardpandamailcom", "male")

    def test_is_male(self):
        self.assertEqual(self.my_panda.isMale(), True)

    def test_is_famale(self):
        self.assertEqual(self.my_panda.isFemale(), False)

    def test_str_cast(self):
        str_cast = "I am Bard, I am male and my email is bard@pandamail.com"
        self.assertEqual(str(self.my_panda), str_cast)

    def test_eq(self):
        other_panda = Panda("Guardian", "guardian@pandamail.com", "male")
        self.assertFalse(self.my_panda == other_panda)

    def test_hash_function(self):
        self.assertTrue(isinstance(hash(self.my_panda), int))


class SocialNetTest(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.other_panda = Panda("Bard", "bard@pandamail.com", "male")
        self.my_panda = Panda("Nikola", "n.tsolov@abv.bg", "male")
        self.friend_panda = Panda("Stivi", "s.strahilov@abv.bg", "male")
        self.vito = Panda("Viktor", "v.georgiev@abv.bg", "male")
        self.koleto = Panda("Koleto", "k.dimitrov@abv.bg", "male")
        self.lidka = Panda("Lidiq", "l.levashka@abv.bg", "female")

    def test_add_panda(self):
        self.network.add_panda(self.my_panda)
        self.assertEqual(self.network.pandas[self.my_panda], [])
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.my_panda)

    def test_has_panda(self):
        self.network.add_panda(self.my_panda)
        self.assertTrue(self.network.has_panda(self.my_panda))
        self.assertFalse(self.network.has_panda(self.other_panda))

    def test_make_friends(self):
        self.network.make_friends(self.my_panda, self.other_panda)
        with self.assertRaises(PandaAlreadyFriends):
            self.network.make_friends(self.my_panda, self.other_panda)

    def test_are_friends(self):
        self.network.add_panda(self.friend_panda)
        self.network.make_friends(self.my_panda, self.other_panda)
        self.assertTrue(self.network.are_friends(self.other_panda, self.my_panda))
        self.assertFalse(self.network.are_friends(self.friend_panda, self.my_panda))

    def test_conection_level(self):
        self.network.make_friends(self.my_panda, self.koleto)
        self.network.make_friends(self.vito, self.friend_panda)
        self.network.make_friends(self.my_panda, self.lidka)
        self.network.make_friends(self.my_panda, self.friend_panda)

        self.assertFalse(self.network.conection_level(self.my_panda, self.other_panda))

        self.network.add_panda(self.other_panda)
        self.assertEqual(self.network.conection_level(self.my_panda, self.koleto), 1)
        self.assertEqual(self.network.conection_level(self.my_panda, self.other_panda), -1)
        self.assertEqual(self.network.conection_level(self.my_panda, self.vito), 2)

        self.network.make_friends(self.vito, self.other_panda)
        self.assertEqual(self.network.conection_level(self.my_panda, self.other_panda), 3)
        self.network.save("panda_net.txt")

    def test_are_connected(self):
        self.network.make_friends(self.my_panda, self.koleto)
        self.assertTrue(self.network.are_connected(self.my_panda, self.koleto))
        self.assertFalse(self.network.are_connected(self.my_panda, self.other_panda))

        self.network.add_panda(self.other_panda)
        self.assertFalse(self.network.are_connected(self.my_panda, self.other_panda))

    def test_how_many_gender(self):
        self.network.make_friends(self.my_panda, self.koleto)
        self.network.make_friends(self.vito, self.friend_panda)
        self.network.make_friends(self.my_panda, self.lidka)
        self.network.make_friends(self.my_panda, self.friend_panda)

        self.assertFalse(self.network.how_many_gender_in_network(1, self.other_panda, "male"))
        self.assertEqual(self.network.how_many_gender_in_network(1, self.my_panda, "female"), 1)
        self.assertEqual(self.network.how_many_gender_in_network(1, self.my_panda, "male"), 2)
        self.assertEqual(self.network.how_many_gender_in_network(2, self.my_panda, "male"), 3)


if __name__ == '__main__':
    unittest.main()

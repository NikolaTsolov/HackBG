import unittest
from social_net_for_pandas import PandaSocialNetwork
from social_net_for_pandas import PandaAlreadyThere
from social_net_for_pandas import Panda

class TestSocialNet(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.my_panda = Panda("Bard", "bard@pandamail.com", "male")
        self.friend_panda = Panda("Nikola", "n.tsolov@abv.bg", "male")
        self.other_panda = Panda("Stivi", "s.strahilov@abv.bg", "male")
        self.panda_list = [self.my_panda, self.friend_panda]
        self.network.add_panda(self.my_panda)
        self.network.make_friends(self.other_panda, self.friend_panda)
        self.network.make_friends(self.my_panda, self.friend_panda)

    def test_add_panda(self):
        self.assertEqual(self.network._pandas[self.my_panda], [])
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.my_panda)
    def test_has_panda(self):
        self.assertEqual(self.network.has_panda(self.my_panda), True)

    def test_make_friends(self):
        self.assertEqual(self.network.has_panda(self.other_panda), True)
        self.assertEqual(self.network.has_panda(self.friend_panda), True)

    def test_are_friends(self):
        self.assertEqual(self.network.are_friends(self.other_panda, self.friend_panda), True)
        self.assertEqual(self.network.are_friends(self.other_panda, self.my_panda), False)

if __name__ == '__main__':
    unittest.main()

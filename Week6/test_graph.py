import unittest
from who_follows_you_back import DirectedGraph, MissingNode, NotInRange

class TestDirectedGraph(unittest.TestCase):
    def setUp(self):
        self.followings = DirectedGraph()
        self.followings.add_edge("Zeus", "Poseidon")
        self.followings.add_edge("Zeus", "Ares")
        self.followings.add_edge("Zeus", "Aphrodite")
        self.followings.add_edge("Poseidon", "Scylla")
        self.followings.add_edge("Athene", "Aphrodite")
        self.followings.add_edge("Ares", "Aphrodite")
        self.followings.add_edge("Hephaestus", "Aphrodite")
        self.followings.add_edge("Hades", "Thanatos")
        self.followings.add_edge("Thanatos", "Ares")
        self.followings.add_edge("Aphrodite", "Hephaestus")
        self.followings.add_edge("Hephaestus", "Poseidon")

    def test_add_edge(self):
        self.assertTrue("Poseidon" in self.followings.get_neighbours_for("Zeus"))
        self.assertTrue("Aphrodite" in self.followings.get_neighbours_for("Ares"))
        self.assertEqual(self.followings.add_edge("Zeus", "Ares"), "Ares Already In The List")

    def test_is_directed(self):
        self.assertFalse("Zeus" in self.followings.get_neighbours_for("Ares"))


    def test_get_neighbours(self):
        zeus = ["Poseidon", "Ares", "Aphrodite"]
        self.assertEqual(self.followings.get_neighbours_for("Zeus"), zeus)
        with self.assertRaises(MissingNode):
            self.followings.get_neighbours_for("Scylla")

    def test_path_betwin(self):
        self.assertTrue(self.followings.path_between("Zeus", "Scylla"))
        self.assertFalse(self.followings.path_between("Zeus", "Athene"))
        self.assertFalse(self.followings.path_between("Zeus", "Hades"))
        self.assertTrue(self.followings.path_between("Hades", "Aphrodite"))
        with self.assertRaises(NotInRange):
            self.assertTrue(self.followings.path_between("Hades", "Scylla"))




if __name__ == '__main__':
    unittest.main()

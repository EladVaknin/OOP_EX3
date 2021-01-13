from DiGraph import DiGraph
import unittest

class mytest(unittest.TestCase):

    def setUp(self) -> None:

        self.graph = DiGraph()


    def test_all_in_out(self):
        self.assertTrue(self.graph.add_node(0,(0,7,2)))
        self.assertFalse(self.graph.add_node(0, (0, 7, 2)))
        self.assertEqual(self.graph.v_size(),1)
        self.assertTrue(self.graph.add_node(1, (0, 7, 2)))
        self.assertTrue(self.graph.add_edge(0,1,500))
        self.assertFalse(self.graph.add_edge(0, 1, 500))
        self.assertTrue(self.graph.add_edge(1, 0, 500))
        self.assertFalse(self.graph.add_edge(1, 0, 500))
        self.assertFalse(self.graph.add_edge(1, 1, 500))
        self.assertFalse(self.graph.add_edge(1, 15, 500))
        self.assertFalse(self.graph.add_edge(115, 0, 500))
        self.assertEqual(self.graph.e_size(),2)
        self.assertTrue(self.graph.remove_edge(1,0))
        self.assertFalse(self.graph.remove_edge(1, 0))
        self.assertEqual(self.graph.e_size(), 1)
        self.assertEqual(self.graph.get_mc(),5)
        print(self.graph.get_all_v())
        print(self.graph.all_out_edges_of_node(0))
        print(self.graph.all_in_edges_of_node(1))

    def test_removenode(self):
        for x in range(5):
            self.assertTrue(self.graph.add_node(x,(2,3,4)))

        self.assertEqual(self.graph.v_size(),5)
        self.assertTrue(self.graph.add_edge(0,3,45))
        self.assertTrue(self.graph.add_edge(0, 4, 45))
        self.assertTrue(self.graph.add_edge(1, 0, 45))
        self.assertTrue(self.graph.add_edge(2, 0, 45))
        self.assertEqual(self.graph.e_size(),4)
        self.assertEqual(self.graph.v_size(),5)
        self.assertEqual(self.graph.get_mc(),9)
        print(self.graph.get_all_v())
        print(self.graph.all_out_edges_of_node(0))
        print(self.graph.all_out_edges_of_node(1))
        print(self.graph.all_out_edges_of_node(2))
        print(self.graph.all_out_edges_of_node(3))
        print(self.graph.all_out_edges_of_node(4))
        print(self.graph.all_in_edges_of_node(0))
        print(self.graph.all_in_edges_of_node(1))
        print(self.graph.all_in_edges_of_node(2))
        print(self.graph.all_in_edges_of_node(3))
        print(self.graph.all_in_edges_of_node(4))
        self.assertTrue(self.graph.remove_node(0))
        print(self.graph.get_all_v())
        print(self.graph.all_out_edges_of_node(0))
        print(self.graph.all_out_edges_of_node(1))
        print(self.graph.all_out_edges_of_node(2))
        print(self.graph.all_out_edges_of_node(3))
        print(self.graph.all_out_edges_of_node(4))
        print(self.graph.all_in_edges_of_node(0))
        print(self.graph.all_in_edges_of_node(1))
        print(self.graph.all_in_edges_of_node(2))
        print(self.graph.all_in_edges_of_node(3))
        print(self.graph.all_in_edges_of_node(4))
        self.assertEqual(self.graph.e_size(), 0)
        self.assertEqual(self.graph.v_size(), 4)
        self.assertEqual(self.graph.get_mc(), 14)

    def test_add_node(self):
        for x in range(5):
            self.assertTrue(self.graph.add_node(x, (2, 3, 4)))
        self.assertEqual(self.graph.v_size(), 5)
        print(self.graph.v_size())

        for x in range(10):
            self.graph.add_node(x, (x, x+1, x+2))
        self.assertEqual(self.graph.v_size(), 10)
        print(self.graph.v_size())
        self.graph.add_node(11,(1,2,3))
        self.assertEqual(self.graph.v_size(), 11)
        print(self.graph.v_size())
        self.graph.add_node(11, (1, 2, 3))
        self.assertEqual(self.graph.v_size(), 11)
        self.graph.add_node(122, (1, 2, 3))
        self.graph.add_node(34, (1, 2, 3))
        self.graph.add_node(55, (1, 2, 3))
        self.assertEqual(self.graph.v_size(), 14)
        self.graph.remove_node(122)
        self.graph.remove_node(122)
        self.assertEqual(self.graph.v_size(), 13)
        self.graph.remove_node(9)
        self.assertEqual(self.graph.v_size(), 12)



    def test_remove_edge(self):
        for x in range(5):
            self.assertTrue(self.graph.add_node(x, (2, 3, 4)))

        self.assertTrue(self.graph.add_edge(0,3,45))
        self.assertTrue(self.graph.add_edge(0, 4, 45))
        self.assertTrue(self.graph.add_edge(1, 0, 45))
        self.assertTrue(self.graph.add_edge(2, 0, 45))
        self.graph.remove_edge(0,3)
        self.assertEqual(self.graph.e_size(),3)

    def test_v_size(self):
        for x in range(10):
            self.assertTrue(self.graph.add_node(x, (2, 3, 4)))

        self.assertTrue(self.graph.v_size(),10)
        self.graph.remove_node(1)
        self.assertTrue(self.graph.v_size(), 9)
        self.graph.remove_node(11)  #node not exist
        self.assertTrue(self.graph.v_size(), 9)

    def test_mc(self):
        for x in range(10):
            self.assertTrue(self.graph.add_node(x, (2, 3, 4)))

        self.assertEqual(self.graph.v_size(), 10)
        self.assertTrue(self.graph.add_edge(0, 3, 45))
        self.assertTrue(self.graph.add_edge(0, 4, 45))
        self.assertTrue(self.graph.add_edge(1, 0, 45))
        self.assertTrue(self.graph.add_edge(2, 0, 45))
        self.assertEqual(self.graph.e_size(), 4)
        self.assertEqual(self.graph.get_mc(),14)




from InventoryAllocator import InventoryAllocator
import unittest
class Test(unittest.TestCase):

    # case 1: one warehouse is enough
    def test_case1(self):

        orders1 = {'apple': 1, 'banana': 2}
        w1 = [{'name': 'owd', 'inventory': {'apple': 1, 'banana': 2}}]
        self.assertEqual([{'owd': {'apple': 1, 'banana': 2}}],InventoryAllocator.cheapestcost(orders1,w1))

    # case 2: total stock is not enough for orders, then output empty
    def test_case2(self):
        orders2 = {'apple': 5, 'kiwi': 2}
        w2 = [{'name': 'eve', 'inventory': {'kiwi': 1, 'banana': 2}}, {'name': 'ded', 'inventory': {'apple': 3}}]
        self.assertEqual([], InventoryAllocator.cheapestcost(orders2, w2))

    # case 3: some items in orders need to be seperated from different warehouses
    def test_case3(self):
        orders3 = {'apple': 5, 'banana': 2}
        w3 = [{'name': 'owd', 'inventory': {'apple': 2, 'banana': 2}}, {'name': 'ded', 'inventory': {'apple': 3}}]
        self.assertEqual([{'owd': {'apple': 2, 'banana': 2}}, {'ded': {'apple': 3}}], InventoryAllocator.cheapestcost(orders3, w3))

    # case 4: we only take what we need in some warehouses not all of the stock in these warehouses
    def test_case4(self):
        orders4 = {'apple': 5, 'kiwi': 2, 'banana': 3}
        w4 = [{'name': 'owd', 'inventory': {'apple': 2, 'banana': 2, 'prune': 2}},
              {'name': 'eve', 'inventory': {'kiwi': 2, 'banana': 2}}, {'name': 'ded', 'inventory': {'apple': 3}}]
        self.assertEqual([{'owd': {'apple': 2, 'banana': 2}}, {'eve': {'kiwi': 2, 'banana': 1}}, {'ded': {'apple': 3}}], InventoryAllocator.cheapestcost(orders4, w4))

    # case 5:the warehouses which do not have what we want is useless
    def test_case5(self):
        orders5 = {'apple': 3, 'prune': 3}
        w5 = [{'name': 'owd', 'inventory': {'apple': 2, 'banana': 2}},
              {'name': 'ded', 'inventory': {'kiwi': 3, 'banana': 3}},
              {'name': 'eve', 'inventory': {'prune': 3, 'apple': 2}}]

        self.assertEqual([{'owd': {'apple': 2}}, {'eve': {'prune': 3, 'apple': 1}}], InventoryAllocator.cheapestcost(orders5, w5))

if __name__ == '__main__':
    unittest.main(verbosity=1)
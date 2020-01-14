
class InventoryAllocator:

    def cheapestcost(self,orders, warehouses):
        # get total numbers of items
        total = sum(orders.values())

        res = []
        n = len(warehouses)
        suc = False
        for i in range(n):
            #iterate each warehouse from cheapiest cost to highest cost
            dic = {}

            f = False
            items = warehouses[i]['inventory']

            for j in items:
                #if we still need j item
                if not items[j] or j not in orders or not orders[j]: continue
                # we will add this warehouse to our solution
                f = True
                take = min(orders[j], items[j])
                dic[j] = take
                orders[j] -= take
                total -= take
            if f:
                w = {warehouses[i]['name']: dic}
                res.append(w)
            # once all items are satisfied, we will mark and break the loop
            if not total:
                break

        return res if not total else []

#case 1: one warehouse is enough
orders1 = { 'apple':1 ,'banana':2}
w1 = [{'name': 'owd', 'inventory': {'apple': 1,'banana':2}}]

#case 2: total stock is not enough for orders, then output empty
orders2 = {'apple':5,'kiwi':2}
w2 = [{'name': 'eve', 'inventory': {'kiwi': 1,'banana':2}},{'name': 'ded', 'inventory': {'apple': 3}}]

#case 3: some items in orders need to be seperated from different warehouses
orders3 = {'apple':5,'banana':2}
w3 = [{'name': 'owd', 'inventory': {'apple': 2,'banana':2}},{'name': 'ded', 'inventory': {'apple': 3}}]

#case 4: we only take what we need in some warehouses not all of the stock in these warehouses
orders4 = {'apple':5,'kiwi':2,'banana':3}
w4 = [{'name': 'owd', 'inventory': {'apple': 2,'banana':2,'prune':2}},{'name': 'eve', 'inventory': {'kiwi': 2,'banana':2}},{'name': 'ded', 'inventory': {'apple': 3}}]

#case 5:the warehouses which do not have what we want is useless
orders5 = {'apple':3,'prune':3}
w5 = [{'name': 'owd', 'inventory': {'apple': 2,'banana':2}},{'name': 'ded', 'inventory': {'kiwi': 3,'banana':3}},{'name': 'eve', 'inventory': {'prune': 3,'apple':2}}]


ia = InventoryAllocator()
print(ia.cheapestcost(orders4, w4))
'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_PAYMENTS = 999999

def validorder(order: Order):
    payments = []
    products = []
    for item in order.items:
        if item.type == 'payment':
            payments.append(item.amount)
        elif item.type == 'product':
            products.append(abs(item.amount * item.quantity))
        else:
            return "Invalid item type: %s" % item.type

    net = sum(payments) - sum(products)

    if sum(payments) >= MAX_PAYMENTS:
        return "Total amount payable for an order exceeded"
    elif round(net) < 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
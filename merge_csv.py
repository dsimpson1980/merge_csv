import csv
trades = csv.reader(open('trades.csv'))
trades_header = trades.next()
orders = csv.reader(open('orders.csv'))
orders_headers = orders.next()
trade = trades.next()
try:
    for order in orders:
        print order, trade
        while trade[0] < order[0]:
            print 'trade %s without order' % trade[0]
            trade = trades.next()
            continue
        if trade[0] > order[0]:
            print 'order %s without trade' % order[0]
        while order[0] == trade[0]:
            print trade
            trade = trades.next()
except StopIteration:
    print 'got stopiteration'
for trade in trades:
    print 'more trades than orders'
for orders in orders:
    print 'more orders than trades'
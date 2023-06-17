from decimal import Decimal as D

# init_price = 1000
# coupon = 0.1
# partner = 0.1
# sale = 0.1
#
# final_price = init_price * (1 - coupon - partner - sale)  # 700.0000000000001
# print(final_price)
#
# print(0.1 + 0.1 + 0.1)  # 0.30000000000000004
# print(0.2 + 0.2)  # 0.4


# print(D('0.1') + D('0.1') + D('0.1'))  # 0.3
# print(D('0.2') + D('0.2'))  # 0.4
#
# print(D(0.1) + D(0.1) + D(0.1))  # 0.3000000000000000166533453694
# print(D(0.2) + D(0.2))  # 0.4000000000000000222044604925


init_price = 1000
coupon = D('0.1')
partner = D('0.1')
sale = D('0.1')

final_price = init_price * (1 - coupon - partner - sale)  # 700.0000000000001
print(final_price)  # 700.0

from functools import cmp_to_key


class Medicinal:
    def __init__(self, no, name, price, amount):  # 销售额让price*amount就行，没必要存储
        self.no = no
        self.name = name
        self.price = price
        self.amount = amount


def sort_by_no(medicinal_list):
    def cmp(a, b):
        no1 = a.no
        no2 = b.no
        if no1[0] != no2[0]:
            return no1[0] - no2[0]
        value1 = int(no1[1:])
        value2 = int(no2[1:])
        return value1 - value2

    ans = sorted(medicinal_list, key=cmp_to_key(cmp))
    return ans


def sort_by_price(medicinal_list):  # 自己去参考topic1吧
    pass


def sort_by_amount(medicinal_list):
    pass


def sort_by_sales_volume(medicinal_list):  # 销售额
    pass


if __name__ == '__main__':
    medicinal = Medicinal(no='a123', name='健胃消食片', price=25.0, amount=100)
    medicinal_list = [medicinal]

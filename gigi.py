from coffee import tea as ct
from fifi.lili import concatenate_list


if __name__ == '__main__':
    gt = ct.greater_than(4, 6)
    print('gigi {}'.format(gt))
    l1 = []
    l2 = [6, 7]
    print('gigi {}'.format(concatenate_list(l1, l2)))
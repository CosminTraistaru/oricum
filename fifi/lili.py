def concatenate_list(a, b):
    """
    concatenates two lists
    """
    a.extend(b)
    return a


def main():
    l1 = [4, 3, 5]
    l2 = [4, 6, 7]
    nl = concatenate_list(l1, l2)
    print('lili {}'.format(nl))


if __name__ == '__main__':
    main()

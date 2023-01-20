def two_element_add(e1, e2):
    ret = None
    try:
        e1 = float(e1)
        e2 = float(e2)
        ret = e1 + e2
    except ValueError:
        print(f'the data input are invalid')
        return None
    else:
        print(f'{e1} + {e2} = {ret}.')
    finally:
        print('function has been called!')
        return ret


def two_element_division(e1, e2):
    ret = None
    try:
        e1 = float(e1)
        e2 = float(e2)
        ret = e1 / e2
    except ValueError:
        print(f'the data input are invalid')
        return None
    except ZeroDivisionError:
        print(f'the division input couldn\'t be zero!')
        return None
    else:
        print(f'{e1} / {e2} = {ret}.')
    finally:
        return ret


if __name__ == '__main__':
    two_element_add(2, 3)
    two_element_add(2, 'name')
    two_element_division('ss', 5)
    two_element_division(25, 5)
    two_element_division(25, 0)
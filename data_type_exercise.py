from functools import reduce

def list_iterator():
    # new a list of ages
    ages = [23, 32, 18, 81]
    for index, age in enumerate(ages):
        print(f'{index}->{age}')
    # create an iterator of list
    iterator_temp = iter(ages)
    for age in iterator_temp:
        print(f'{age}')


def list_map_test():
    # add the list of salary
    salary_list = [5000, 4500, 5100, 3200]
    iterator_temp = map(lambda s: s * 1.1, salary_list)
    print(type(iterator_temp))
    result_list = list(iterator_temp)
    print(result_list)
    # parse the student age from student list
    student_list = [
        ('Jack', 23),
        ('Tom', 22),
        ('Mary', 28)
    ]
    ages_list = list(map(lambda s: s[1], student_list))
    print(ages_list)
    # map function do not change the original list
    print(salary_list)
    '''
    # map work in tuple also
    tuple_temp = (2, 3, 4, 5)
    result_tuple = tuple(map(lambda s: s + 1, tuple_temp))
    print(result_tuple)
    '''


def list_filter_temp():
    # add the list of salary
    salary_list = [5000, 7500, 5100, 9000]
    salary_threshold = 6000
    iterator_temp = filter(lambda s: s > salary_threshold, salary_list)
    print(type(iterator_temp))
    result_list = list(iterator_temp)
    print(result_list)
    # pick the student whose age is above 22
    student_list = [
        ('Jack', 23),
        ('Tom', 22),
        ('Mary', 28)
    ]
    result_list = list(filter(lambda s: s[1] > 22, student_list))
    print(result_list)
    '''
    # filter work in tuple also
    tuple_temp = (2, 3, 4, 5)
    result_tuple = tuple(filter(lambda s: s > 3, tuple_temp))
    print(result_tuple)
    '''


def two_element_add(e1, e2):
    ret = e1 + e2
    print(f'{e1} + {e2} = {ret}.')
    return ret


def list_reduce_temp():
    # add the list of salary
    salary_list = [5000, 7500, 5100, 9000]
    sum_temp = reduce(lambda s1, s2: s1 + s2, salary_list)
    print(type(sum_temp))
    print(sum_temp)
    sum_temp = reduce(two_element_add, salary_list)
    print(sum_temp)
    # reduce function do not change the original list
    print(salary_list)


def list_generate_temp():
    # add the list of salary
    salary_list = [5000, 7500, 5100, 9000]
    salary_list_1 = [a * 1.1 for a in salary_list]
    salary_list_2 = [a * 1.1 for a in salary_list if a < 8000]
    print(f'original list is {salary_list}.')
    print(f'list after salary addition is {salary_list_1}.')
    print(f'list after salary addition if salary of member below the 8000 is {salary_list_2}.')


def dictionary_exercise_temp():
    student = {
        'name': 'Tom',
        'age': 26,
        'hobbies': ['swimming', 'game', 'travel']
    }
    print(student['name'])
    print(student.get('name'))
    # print(student['gender'])    # there will be an error if you choose an invalid key
    print(student.get('gender'))    # there will be a none return if you choose an invalid key
    print(student.get('gender'), 'female')
    print(student.get('age'), 20)
    student['gender'] = 'female'
    print(student['gender'])
    student['gender'] = 'male'
    print(student.get('hobbies'))
    del student['hobbies']
    print(student.get('hobbies'))
    print(student.items())
    print(len(student.items()))
    print(type(student.items()))
    for element in student.items():
        print(f'key: {element[0]}, value: {element[1]}')
    for element in student.keys():
        print(f'key: {element}, value: {student.get(element)}')
    for element in student.values():
        print(f'value: {element}')
    for element in student:
        print(f'key: {element}, value: {student.get(element)}')


def dictionary_parse_temp():
    grades = {
        'Tom': 70,
        'Jack': 40,
        'Bob': 30,
        'Rose': 60
    }
    new_grades1 = {name: grade * 1.1 for name, grade in grades.items()}
    print(new_grades1)
    print(type(new_grades1))
    new_grades2 = {name: grade * 1.1 for name, grade in grades.items() if grade <= 60}
    print(new_grades2)
    new_grades3 = {
        'Jerry': 65,
        'Damn': 30,
        'Bob': 60,
    }
    new_grades_sum = {**grades, **new_grades3}
    # the final value of the same key is depended on the second dictionary eg: 'Bob'
    print(new_grades_sum)


def set_exercise_temp():
    # define a set of names
    names_set = {'Jack', 'Tom', 'Damn'}
    # define an empty set by using set method, a pair of brace define an empty dictionary
    empty_set = set()
    print(empty_set)
    print(names_set)
    print('Jack' in names_set)
    print('Tony' in names_set)
    names_set.add('Tony')
    print('Tony' in names_set)
    print(names_set)
    names_set.remove('Jack')
    print(names_set)
    # names_set.remove('Mary')    # there will be an error when delete an element invalid by using remove method
    names_set.discard('Mary')
    element_random = names_set.pop()
    print(element_random)   # pop method can return and delete an element randomly
    frozenset_temp = frozenset(names_set)   # frozenset couldn't be changed by remove or add method
    print(frozenset_temp)
    for element in names_set:
        print(element)
    for index, element in enumerate(names_set, 1):
        print(f'{index} -> {element}')
    names_set_parse_temp = {name + 'ly' for name in names_set if len(name) > 3}
    print(names_set_parse_temp)
    print(names_set)
    names_set_1 = names_set.union(names_set_parse_temp)
    names_set_2 = names_set | names_set_parse_temp
    print(names_set_1)
    print(names_set_2)
    names_set_3 = names_set.union(['Jerry'])    # union method can input a list and tuple besides set object
    print(names_set_3)
    print(names_set_1 & names_set)
    print(names_set.intersection(names_set_3))


def set_operation_temp():
    # the difference operation  of set
    set_1 = {2, 3, 4}
    set_2 = {3, 4, 5}
    print(set_1.difference(set_2))
    print(set_1 - set_2)
    print(f'the elements in set_2 but not in set_1 are(is) {set_2.difference(set_1)}')
    print(f'the elements that not mutual are(is) {set_2.symmetric_difference(set_1)}')
    print(set_1 ^ set_2)
    set_3 = {7, 8}
    set_4 = {7, 8, 9, 10}
    print(set_3.issubset(set_4))
    print(set_3 <= set_4)
    print(set_4.issuperset(set_3))
    print(set_4 >= set_3)
    print(set_3.isdisjoint(set_4))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # list_iterator()
    # list_map_test()
    # list_filter_temp()
    # list_reduce_temp()
    # list_generate_temp()
    # dictionary_exercise_temp()
    # dictionary_parse_temp()
    # set_exercise_temp()
    set_operation_temp()
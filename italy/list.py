from typing import Any, List


def rangel(*args) -> List[int]:
    """ rangel() is a shorthand to list(range(...))
    Examples:
    postive_numbers = rangel(10)
    one_to_nine = rangel(1, 10)
    two_to_seven = rangel(2, 0b1000)
    even_numbers = rangel(0, 11, 2)
    """
    return list(range(*args))


def filterl(func, *iterable) -> List[Any]:
    """ filterl() is a shorthand to list(filter(...))
    Examples:
    postive_numbers = filterl(lambda x: x>0, [1,-2,3])
    truth_list = filterl(bool, [True, False, None, True, 1])
    """
    return list(filter(func, *iterable))



def mapl(func, *iterable) -> List[Any]:
    """ mapl() is an alternative to built-in function map(), but no need to use list() to convert the result to a list 
    lambda version:
    mapl = lambda func, *iterable: list(map(func, *iterable))
    Examples:
    my_list =  mapl(abs, [-1,-2,3]);
    num_strings_list = mapl(str, range(10))
    """
    return list(map(func, *iterable))



def mapm(func, xs) -> None:
    """ 
    mapm() is for executing a series of IO actions without using for loop.
    examples:
    mapm(print, [1,2,3])  
    mapm(print, range(10))  
    """
    for x in xs:
        func(x)


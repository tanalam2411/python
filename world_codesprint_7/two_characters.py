

"""
     [b e a b e  f e a b]


    babab


s =  [a,b,a,a,c,d,a,b,d]

unique_chars = abcd
a) validate(s)


b) for i in unique_chars:




b) ss = pop(a) 'bcdbd'
    res = validate(ss)
    if not res:
    for c in
     while validate and ss:
         ss = pop()



validate(s):
    1) res = get_unique_char_list
       if len(res) > 2:
           return fail
       else
           len_strg = len(s)
           res = get_unique_char_list
           front = get_front
           rev = get_rev
           if s == front or s == rev:
                return success






beabeefeab
"""


def two_diff_chars(len_str, input_list):

    unique_chars = set(input_list)

    if validate(input_list):
        return len(input_list)

    all_results = []




def validate(input_list):
    if type(input_list) != list:
        input_list = [i for i in input_list]

    len_input_list = len(input_list)
    unique_chars = set(input_list)
    if len(unique_chars) > 2:
        return False

    front = get_front(len_input_list, unique_chars)
    rev = get_reverse(len_input_list, unique_chars)
    if ''.join(input_list) == front or ''.join(input_list) == rev:
        return True
    else:
        return False


def get_front(len_input_list, input_list):
    input_list = list(input_list)
    tmp = len_input_list/2
    res = input_list*tmp
    if len_input_list%2:
        res.append(input_list[0])
    print ''.join(res)
    return ''.join(res)


def get_reverse(len_input_list, input_list):
    input_list = list(input_list)
    input_list.reverse()
    tmp = len_input_list/2
    res = input_list*tmp
    if len_input_list%2:
        res.append(input_list[0])
    print ''.join(res)
    return ''.join(res)


input_str = ['a', 'b', 'a', 'a', 'c', 'd', 'a', 'b', 'd']
input_str = ['b', 'a', 'b', 'a', 'b', 'a', 'a']

print validate(input_str)

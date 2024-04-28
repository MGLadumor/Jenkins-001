from operator import itemgetter

elements: list[int] = [1, 2, 3, 4, 5]
# selected: tuple[int, int] = (elements[0], elements[-1])

first_and_last: itemgetter = itemgetter(0,-1)
print(first_and_last(elements))

items: dict[str, int] = {'a':1, 'b':2, 'c':3, 'd':4}
element: dict[str, int] = {'a':100, 'b':200, 'c':300}
# del elements[-1]
a_and_c: itemgetter = itemgetter('a','c')
print(a_and_c(items))
print(a_and_c(element))
print(elements)

r: slice = slice(None, None, -1)

print(elements[r])
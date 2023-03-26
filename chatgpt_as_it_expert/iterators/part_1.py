""" An iterator is an object that allows you to traverse through a sequence of elements, one at a time, without
 having to access the entire sequence at once. This makes it useful for working with large or infinite sequences,
 as well as for conserving memory by only accessing what is necessary. """


my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

""" Here, the iter() function creates an iterator object from the sequence my_list. The next() function retrieves the
 next item in the sequence. If there are no more items, next() will raise a StopIteration exception. """

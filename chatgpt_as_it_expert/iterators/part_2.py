""" You can create an iterator from an iterable object (e.g. list, tuple, set) by using the iter() function.
 This function returns an iterator object. """
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2

""" We can use the next() function to get the next element from an iterator. When we reach the end of the iterator, 
 it raises a StopIteration exception. """
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4
print(next(my_iterator))  # Output: 5
print(next(my_iterator))  # Raises StopIteration exception

""" We can also use a for loop to iterate through an iterator. The for loop automatically calls the next()
 function to get the next element until the iterator is exhausted. """
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
for element in my_iterator:
    print(element)
    

""" We can create our own iterator by implementing the __iter__() and __next__() magic methods in a class.
 The __iter__() method should return the iterator object itself, and the __next__() method should return the next 
 element in the sequence or raise a StopIteration exception if there are no more elements. """


class MyIterator:
    def __init__(self, max_num):
        self.current_num = 0
        self.max_num = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.max_num:
            self.current_num += 1
            return self.current_num
        else:
            raise StopIteration


my_iterator = MyIterator(5)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4
print(next(my_iterator))  # Output: 5
print(next(my_iterator))  # Raises StopIteration exception

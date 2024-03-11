#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 2: Cookie Jar

Description: Implement a `cookie jar` program in which to store cookies.
             Implement a class called `Jar` with these methods:
              - `__init__`: should initialize a cookie jar with the given "capacity"
                representing the maximum number of cookies that can fit in the cookie jar.
                If "capacity" is not a non-negative "int", though, `__init__` should raise a "ValueError".
              - `___str__` should return with n-🍪, where n is the number of cookies in the cookie jar.
                 For instance, if there are 3 cookies in the cookie jar, then "str" should return "🍪🍪🍪"
              - `deposit` should add "n" cookies to the cookie jar. If adding that many would exceed the cookie jar's capacity,
                 though, `deposit` should instead raise a "ValueError".
              - `withdraw` should remove "n" cookies from the cookie jar. Nom nom nom.
                 If there aren't that many cookies in the cookie jar, though, `withdraw` should instead raise a "ValueError".
              - `capacity` should return the cookie jar's capacity.
              - `size` should return the number of cookies actually in the cookie jar, initially 0.

              You may not alter any of the parameters but you may add your own methods.
"""

from emoji import emojize


class Jar:
    def __init__(self, capacity=12):
        """Initialize cookie jar class"""
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return emojize(":cookie:") * self._size

    def deposit(self, n):
        """Add cookies to jar"""
        if self._size + n > self.capacity:
            raise ValueError("Cookie Jar exceeds capacity")
        self._size += n

    def withdraw(self, n):
        """Remove cookies from jar"""
        if self._size <= 0:
            raise ValueError("Cookie Jar is empty!")
        if n > self._size:
            raise ValueError("Not enough cookies in jar")
        self._size -= n

    @property
    def capacity(self):
        """Number of cookies jar can carry"""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Set new carrying capacity for cookie jar"""
        if not isinstance(capacity, int):
            raise ValueError(f"Cookie jar cannot contain {capacity}")
        if capacity < 0:
            raise ValueError("Cookie Jar cannot contain negative values")
        self._capacity = capacity

    @property
    def size(self):
        """Size of cookie jar"""
        return self._size

    @size.setter
    def size(self, size):
        """Set new cookie jar size"""
        if size < 0:
            raise ValueError("Cookie Jar size cannot be negative")
        if not isinstance(size, int):
            raise ValueError(f"Cookie jar cannot be of size {size}")
        self._size = size


def main():
#    """run cookie program"""
    # try adding cookie to jar
    jar = Jar()
    # jar.deposit(15)
    jar.deposit(10)
#    jar.deposit(5)
    # jar.deposit(0)
#    print(jar)

    # remove cookie from jar
    # jar = Jar()
    # jar.withdraw(-15)
    jar.withdraw(5)
    #jar.withdraw(6)
    print(jar)
    print(jar.size)

    # jar.deposit(2)
    # jar.withdraw(3)
    # print(jar)

    # Test capaccity setter function
    # print(jar.capacity)
    # jar.capacity = "cat"
    # jar.capacity = 10
    # jar.capacity = -5
    # print(f"New capacity: {jar.capacity}")

    # Test size setter
    # jar.size = -5
    # jar.size = "cat"
    # print(f"New size: {jar.size}")


if __name__ == "__main__":
    main()

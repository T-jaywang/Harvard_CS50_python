class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies!")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies!")
        self._size -= n
    
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
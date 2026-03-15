from myUtils.Utils import printResult

"""
Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:

Fancy() Initializes the object with an empty sequence.
void append(val) Appends an integer val to the end of the sequence.
void addAll(inc) Increments all existing values in the sequence by an integer inc.
void multAll(m) Multiplies all existing values in the sequence by an integer m.
int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. 
If the index is greater or equal than the length of the sequence, return -1.
"""
class Fancy:

    def __init__(self):
        self._data = []
        self._mul = 1
        self._add = 0
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        self._data.append((val, self._mul, self._add))

    def addAll(self, inc: int) -> None:
        self._add = (self._add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self._mul = (self._mul * m) % self.mod
        self._add = (self._add * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self._data):
            return -1

        val, mul_snap, add_snap = self._data[idx]

        # If mul_snap is zero, all values at that time have collapsed to `add_snap`,
        # and future multiplications will keep mul=0. The current value is just the
        # current global add.
        if mul_snap == 0:
            return self._add % self.mod

        # Compute how much the transformation has changed since the value was appended.
        # The effective multiplier is (mul / mul_snap), which we compute using modular inverse.
        inv_mul_snap = pow(mul_snap, self.mod - 2, self.mod)
        factor = (self._mul * inv_mul_snap) % self.mod

        # The delta added after append is (add - add_snap*factor)
        return (val * factor + (self._add - add_snap * factor)) % self.mod


obj = Fancy()
obj.append(2)
obj.addAll(3)
obj.append(7)
obj.multAll(2)
result = obj.getIndex(0)
printResult(result, 10)
obj.addAll(3)
obj.append(10)
obj.multAll(2)
result = obj.getIndex(0)
printResult(result, 26)
result = obj.getIndex(1)
printResult(result, 34)
result = obj.getIndex(2)
printResult(result, 20)

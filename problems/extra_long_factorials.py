#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

# For making this problem a bit harder, we will imagine that we don't have access to Python great super long integers.
# As if we were in C or C++. So we build a custom class that can handle basic addition, substraction and multiplication.


class BigPositiveInteger:
    def __init__(self, ciphers):
        self.ciphers = ciphers
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        for i in list(self.ciphers):
            if i == 0:
                self.ciphers.pop(0)
            else:
                break

    @classmethod
    def from_int(cls, int_value):
        return cls(ciphers=[int(i) for i in str(int_value)])

    def __eq__(self, other):
        if isinstance(other, int):
            other = BigPositiveInteger.from_int(other)
        return self.ciphers == other.ciphers

    def _ciphers_to_str(self):
        return "".join(str(i) for i in self.ciphers)

    def __repr__(self):
        return f"BigPositiveInteger.from_int({self._ciphers_to_str()})"

    # Traditional base 10 multiplication:
    #   23
    # x 28
    #   -- -> step 1. Small multiplications
    #  184
    # +46
    #  --- -> step 2. Summing all the rows
    #  644

    def __mul__(self, other):
        if isinstance(other, int):
            other = BigPositiveInteger.from_int(other)
        # Step 1
        rows = list()
        for a, i in enumerate(reversed(self.ciphers)):
            carry = 0
            row = [0] * a
            for j in reversed(other.ciphers):
                r = (i * j) + carry
                row.insert(0, r % 10)
                carry = r // 10
            row.insert(0, carry)
            rows.append(row)
        big_integers = [BigPositiveInteger(row) for row in rows]
        return BigPositiveInteger(sum(big_integers, start=BigPositiveInteger([0])).ciphers)

    def __add__(self, other):
        if isinstance(other, int):
            other = BigPositiveInteger.from_int(other)
        rows = [self.ciphers, other.ciphers]
        # Step 2
        carry = 0
        new_ciphers = list()
        for i in range(len(max(rows, key=lambda r: len(r)))):
            r = sum(row[-i-1] for row in rows if len(row) > i) + carry
            new_ciphers.insert(0, r % 10)
            carry = r // 10
        new_ciphers.insert(0, carry)
        return BigPositiveInteger(new_ciphers)

    def __sub__(self, other):
        if isinstance(other, int):
            other = BigPositiveInteger.from_int(other)
        if (len(self.ciphers) < len(other.ciphers)) or (
            len(self.ciphers) == len(other.ciphers) and self.ciphers[0] < other.ciphers[0]
        ):
            return ValueError("Can not result in a negative value")
        carry = 0
        new_ciphers = list()
        for i in range(len(self.ciphers)):
            r = self.ciphers[-i-1] - (other.ciphers[-i-1] if len(other.ciphers) > i else 0) - carry
            if r < 0:
                carry = 1
                r += 10
            else:
                carry = 0
            new_ciphers.insert(0, r)
        if carry:
            raise NotImplementedError("We ended up with a negative value, how??")
        new_ciphers.insert(0, carry)
        return BigPositiveInteger(new_ciphers)


def extraLongFactorials(n):
    if n == 1:
        return n
    return n * extraLongFactorials(n - 1)


if __name__ == "__main__":
    n = int(input().strip())
    print("".join(str(i) for i in extraLongFactorials(BigPositiveInteger.from_int(n)).ciphers))

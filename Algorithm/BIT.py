class BIT:

    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)
        self.btree = [0 for i in range(self.length)]
        self._build()

    def lsb(self, idx):
        return idx & (-idx)

    def _build(self):
        i = 1
        while i <= self.length:
            # print(self.arr[i-1], i)
            self.update(i, self.arr[i - 1])
            i += 1

    def update(self, idx, value):
        # print(f"index= {idx}  value= {value}")
        while idx <= self.length:
            self.btree[idx - 1] += value
            idx = idx + self.lsb(idx)

    def sum(self, end=0, start=0):
        right = self._sum(end)
        left = self._sum(start - 1)
        return right - left

    def _sum(self, idx):
        temp = 0
        while idx > 0:
            temp += self.btree[idx - 1]
            idx = idx - self.lsb(idx)
        return temp


if __name__ == "__main__":
    a = [2, 1, 4, 6, 7, 5, -3, 0, 1, 5, 6, 8]
    ae = BIT(a)
    print(ae.btree)
    v = ae.sum(6, 3)
    print(v)

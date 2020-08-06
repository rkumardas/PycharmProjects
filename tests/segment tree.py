# eg. 5,6,3,8,7,9,4,1,2]
# use for opreation on array like sum in range and updater qurries
# use sum SUM for quries pass start, end and pass lengthen of array respectivly
# UPDATE pass index, updated value and length of array respectivly

class segment:

    def __init__(self, arr, start, end):
        self.arr = arr
        self.ai = 0
        self.start = start
        self.end = end
        self.segtree = [0 for j in range((2 * len(arr))-1)]
        self._build(self.start, self.end)
        # print(self.segtree)
        # print(len((self.segtree)))

    def _build(self, start, end, ai=0):

        mid = (start + end) // 2
        # print("mid ",mid,"start ",start, "end ", end)
        if start == end:
            self.segtree[ai] = self.arr[start]
            return self.arr[start]

        else:
            # print("next call")
            right = self._build(start, mid, 2 * ai + 1)
            left = self._build(mid + 1, end, 2 * ai + 2)
            tem = right + left
            self.segtree[ai] = tem
            return tem

    def sum(self, qs, qe, end=0, start=0, ai=0):
        mid = (start + end) // 2
        print(start, end, mid, ai)
        if qs <= start and qe >= end:
            print(self.segtree[ai])
            return self.segtree[ai]
        if (qs > start and qs > end) or (qe < start and qe < end):
            print(0)
            return 0
        lc = self.sum(qs, qe, mid, start, 2 * ai + 1)
        rc = self.sum(qs, qe, end, mid + 1, 2 * ai + 2)
        total = lc + rc
        return total

    def update(self, index, value, end=0, start=0, ai=0):
        temp = self.arr[index] - value
        self.segtree[ai] -= temp
        mid = (start + end) // 2
        if index < mid and (2*len(self.arr))-1 > end:
            self.update(index, value, mid, start, 2 * ai + 1)
        if index > mid and (2*len(self.arr))-1 > end:
            self.update(index, value, end, mid + 1, 2 * ai + 2)

        return self.segtree


if __name__ == "__main__":
    arr = [5, 6, 3, 8, 7, 9, 4, 1, 2]
    hi = segment(arr, 0, len(arr) - 1)
    print(hi.segtree)

    # my = hi.sum(3, 7, len(arr) - 1)
    gi = hi.update(5, 6, len(arr))
    print(gi)

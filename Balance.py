class Balance:
    r = 0
    ll = 0

    def add_right(self, right):
        self.r += right

    def add_left(self, left):
        self.ll += left

    def result(self):
        if self.ll == self.r:
            return '='
        elif self.ll > self.r:
            return 'L'
        else:
            return 'R'

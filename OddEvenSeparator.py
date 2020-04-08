class OddEvenSeparator:
    numbers = []
    chet = []
    nechet = []

    def add_number(self, n):
        self.numbers.append(n)

    def even(self):
        for i in self.numbers:
            if i % 2 == 0:
                self.chet.append(i)
        return self.chet

    def odd(self):
        for i in self.numbers:
            if i % 2 != 0:
                self.nechet.append(i)
        return self.nechet

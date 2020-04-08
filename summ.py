class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        sum([self.transform(i) for i in range(N + 1)])


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


if __name__ == '__main__':
    usual_sum = Summator()
    square_sum = SquareSummator()
    cube_sum = CubeSummator()

    N = 20
    res1 = N * (N + 1) / 2
    res2 = N * (N + 1) * (2 * N + 1) / 6
    res3 = res1 ** 2

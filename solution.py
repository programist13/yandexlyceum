class BigBell:
    count = 0

    def sound(self):
        if self.count % 2 == 0:
            print('ding')
            self.count += 1
        else:
            print('dong')
            self.count += 1


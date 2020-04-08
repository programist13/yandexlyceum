class Button:
    count = 0

    def click(self):
        self.count += 1

    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0





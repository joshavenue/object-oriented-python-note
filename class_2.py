import random
class Evil:
    stealing = True

    def stealing_time(self):                  // self is often used //
        if self.stealing:
            return bool(random.randint(0,1))
        return False

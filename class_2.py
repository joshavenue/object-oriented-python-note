import random
class Evil:
    stealing = True
    evil_name = 'Harry'
    
    def stealing_time(self):                  // self is often used //
        if self.stealing:
            return bool(random.randint(0,1))
        return False

    def achievement(self):
        return 'I got the stuff, {}!'.format(self.evil_name) // Self.variable to point it back up

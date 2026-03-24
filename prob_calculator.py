import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        
        drawn_balls = []
        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))
            
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        is_success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                is_success = False
                break
        
        if is_success:
            successes += 1
            
    return successes / num_experiments

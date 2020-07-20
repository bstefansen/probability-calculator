import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **balls):
    self.contents = []

    # convert key value pairs to list of balls
    for key, value in balls.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, amount):
    ballsChosen = []

    # pick random amount of balls
    for i in range(amount):
      ballChosen = random.choice(self.contents)
      ballsChosen.append(ballChosen)
      self.contents.remove(ballChosen)
    
    return ballsChosen

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  hatContents = []

  # move hat.contents to hatContents
  for i in hat.contents:
    hatContents.append(i)

  # find count of expected balls
  expectedBallsCount = 0
  for i in range(num_experiments):
    
    # choose random balls
    chosenBalls = []
    if num_balls_drawn > len(hatContents):
      return 1.0
    else:
      for i in range(num_balls_drawn):
        chosenBall = random.choice(hatContents)
        chosenBalls.append(chosenBall)
        hatContents.remove(chosenBall)
        
      # replace hatContents
      hatContents = []
      for i in hat.contents:
        hatContents.append(i)
      
      # count the expected colors in chosen balls
      colorCount = 0
      for key, value in expected_balls.items():
        if chosenBalls.count(key) >= value:
          colorCount += 1

      # check if color count equals the expected ball colors
      if colorCount == len(expected_balls):
        expectedBallsCount += 1

  return expectedBallsCount/num_experiments
from turtle import Turtle 

class Snake:
    def __init__(self):
        self.snakes = []
        self.position = [(-40,0),(-20,0),(0,0)]
    
    def create_snake(self):
      new_snake = Turtle ("square")
      new_snake.color("white")
      new_snake.penup()
      new_snake.goto(self.position[i])
      snakes.append(new_snake)
    def move_snake(self)
        for i in range (len(self.snake)-1):
            snake[i].goto(snake[i+1].pos())
        self.snakes[-1]. forward (20)
        self.snakes[-1].left(90)
            
            
    

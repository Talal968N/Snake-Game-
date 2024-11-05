from turtle import Screen 
from snake import Snake 

window = Screen ()
window. setup (width=800, height=800)
window. bgcolor ("black")

sam = Snake ( )

game_is_on = True 
while game_is_on:
    sam. move()



window. exitonclick ()

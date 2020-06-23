import pygame
from classes import turtle, line, textOnScreen

pygame.init()

main_race_run = True
main_race_win = pygame.display.set_mode((1400,650))
main_race_win_Width = 1400
main_race_win_Height = 650

turtle1 = turtle(1200,0,"turtle1.png")
turtle2 = turtle(1200, 400, "turtle1.png")

def drawturtlesss():
    turtle1.drawturtle(main_race_win)
    turtle2.drawturtle(main_race_win)

def moveturtlesss():
    turtle1.moveturtle()
    turtle2.moveturtle()    

finish_line = line(-150, 0, "start_line.png")
start_line = line(1000, 0, "start_line.png")

who_won = textOnScreen("Player 1 is the winner!",'Arial', main_race_win_Width/2 - 350, main_race_win_Height/2 - 80, 90, (0,0,0))
winner = None

is_moving = True

while main_race_run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_race_run = False

    
    if turtle1.x <= 150:
        winner = 'player1'
    elif turtle2.x <= 150:
        winner = 'player2'
    """elif turtle1.x <= 150 and turtle2.x <= 150:
        who_won.showText(main_race_win)"""

    
       
    
    main_race_win.fill((255,255,255))   
    finish_line.drawline(main_race_win) 
    start_line.drawline(main_race_win)
    drawturtlesss()
    if is_moving:
        moveturtlesss()  

    if winner == 'player1':
        who_won.showText(main_race_win)
        is_moving = False
    elif winner == 'player2':
        who_won.text = 'player 2 is the winner!'
        who_won.showText(main_race_win)
        is_moving = False
    elif winner == 'draw':
        who_won.text = 'its a draw'
        who_won.showText(main_race_win)
        is_moving = False
    pygame.display.update()
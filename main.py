from pygame_functions import *
import random
from pydub import AudioSegment
from playsound import playsound


playerHealth = 100
enemyHealth = 100
isPlayerTurn = True

screenSize(1000, 750)
screen = pygame.display.set_mode([1000, 750])

setBackgroundImage("images/feat-1800x0-c-center.jpg")
bird = makeSprite("images/bird-scrub-jay.png")
move1 = makeSprite("images/move1.png")
move2 = makeSprite("images/move2.png")
move3 = makeSprite("images/move3.png")
move4 = makeSprite("images/move4.png")

# battle = makeSound("battlemusic.mp3")
pygame.mixer.music.load("battlemusic.mp3")
pygame.mixer.music.play(-1)

moveSprite(move1, 500, 450)
moveSprite(move2, 500, 500)
moveSprite(move3, 500, 550)
moveSprite(move4, 500, 600)
moveSprite(bird, 0, 330)
showSprite(bird)
showSprite(move1)
showSprite(move2)
showSprite(move3)
showSprite(move4)



showEnemyHealth = makeLabel("Enemy health: " + str(enemyHealth), 28, 0, 0, "white", "Arial", "black")
showPlayerHealth = makeLabel("Player health: " + str(playerHealth), 28, 0, 0, "white", "Arial", "black")
showLastPlayerAttack = makeLabel("Most recent player attack: ", 28, 0, 0, "white", "Arial", "black")
showLastEnemyAttack = makeLabel("Most recent enemy attack: ", 28, 0, 0, "white", "Arial", "black")

moveLabel(showEnemyHealth, 100, 100)
moveLabel(showPlayerHealth, 100, 135)
moveLabel(showLastEnemyAttack, 100, 200)
moveLabel(showLastPlayerAttack, 100, 235)
showLabel(showEnemyHealth)
showLabel(showPlayerHealth)


bischof = makeLabel("Bischof-Kohler Hypothesis", 40, 500, 150, "blue", "Arial", "white")
showLabel(bischof)


while True:
    if isPlayerTurn:
        if spriteClicked(move1):
            playsound('FirePunch.mp3')
            isPlayerTurn = False
            if enemyHealth >= 15:
                enemyHealth -= 15
            else:
                enemyHealth = 0;
            hideLabel(showEnemyHealth)
            hideLabel(showLastPlayerAttack)
            showEnemyHealth = makeLabel("Enemy health: " + str(enemyHealth), 28, 0, 0, "white", "Arial", "black")
            showLastPlayerAttack = makeLabel("Most recent player attack: proactive mental time travel", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showLastPlayerAttack, 100, 235)
            moveLabel(showEnemyHealth, 100, 100)
            showLabel(showEnemyHealth)
            showLabel(showLastPlayerAttack)
        if spriteClicked(move2):
            playsound('FirePunch.mp3')
            isPlayerTurn = False
            if enemyHealth >= 5:
                enemyHealth -= 5
            else:
                enemyHealth = 0
            hideLabel(showEnemyHealth)
            hideLabel(showLastPlayerAttack)
            showEnemyHealth = makeLabel("Enemy health: " + str(enemyHealth), 28, 0, 0, "white", "Arial", "black")
            showLastPlayerAttack = makeLabel("Most recent player attack: retroactive mental time travel", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showLastPlayerAttack, 100, 235)
            moveLabel(showEnemyHealth, 100, 100)
            showLabel(showEnemyHealth)
            showLabel(showLastPlayerAttack)
        if spriteClicked(move3):
            playsound('FirePunch.mp3')
            isPlayerTurn = False
            if enemyHealth >= 25:
                enemyHealth -= 25
            else:
                enemyHealth = 0
            hideLabel(showLastPlayerAttack)
            hideLabel(showEnemyHealth)
            showEnemyHealth = makeLabel("Enemy health: " + str(enemyHealth), 28, 0, 0, "white", "Arial", "black")
            showLastPlayerAttack = makeLabel("Most recent player attack: plan for future needs w/o regard to current needs", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showEnemyHealth, 100, 100)
            moveLabel(showLastPlayerAttack, 100, 235)
            showLabel(showEnemyHealth)
            showLabel(showLastPlayerAttack)
        if spriteClicked(move4):
            playsound('FirePunch.mp3')
            isPlayerTurn = False
            if enemyHealth >= 20:
                enemyHealth -=20
            else:
                enemyHealth = 0
            hideLabel(showEnemyHealth)
            hideLabel(showLastPlayerAttack)
            showEnemyHealth = makeLabel("Enemy health: " + str(enemyHealth), 28, 0, 0, "white", "Arial", "black")
            showLastPlayerAttack = makeLabel("Most recent player attack: infer the connections between events that aren't explicitly linked", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showEnemyHealth, 100, 100)
            moveLabel(showLastPlayerAttack, 100, 235)
            showLabel(showLastPlayerAttack)
            showLabel(showEnemyHealth)
    else:
        rand = random.randint(1, 4)
        if rand is 1:
            playsound('FirePunch.mp3')
            isPlayerTurn = True
            if playerHealth >= 15:
                playerHealth -= 15
            else:
                playerHealth = 0
            hideLabel(showPlayerHealth)
            hideLabel(showLastEnemyAttack)
            showPlayerHealth = makeLabel("Player health: " + str(playerHealth), 28, 0, 0, "white", "Arial", "black")
            showLastEnemyAttack = makeLabel("Most recent enemy attack: proactive mental time travel", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showPlayerHealth, 100, 135)
            moveLabel(showLastEnemyAttack, 100, 200)
            showLabel(showLastEnemyAttack)
            showLabel(showPlayerHealth)
        if rand is 2:
            playsound('FirePunch.mp3')
            isPlayerTurn = True
            if playerHealth >= 5:
                playerHealth -=5
            else:
                playerHealth = 0
            hideLabel(showPlayerHealth)
            hideLabel(showLastEnemyAttack)
            showPlayerHealth = makeLabel("Player health: " + str(playerHealth), 28, 0, 0, "white", "Arial", "black")
            showLastEnemyAttack = makeLabel("Most recent enemy attack: retroactive mental time travel", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showPlayerHealth, 100, 135)
            moveLabel(showLastEnemyAttack, 100, 200)
            showLabel(showLastEnemyAttack)
            showLabel(showPlayerHealth)
        if rand is 3:
            playsound('FirePunch.mp3')
            isPlayerTurn = True
            if playerHealth >= 25:
                playerHealth -=25
            else:
                playerHealth = 0;
            hideLabel(showPlayerHealth)
            hideLabel(showLastEnemyAttack)
            showPlayerHealth = makeLabel("Player health: " + str(playerHealth), 28, 0, 0, "white", "Arial", "black")
            showLastEnemyAttack = makeLabel("Most recent enemy attack: plan for future needs w/o regard to current needs", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showPlayerHealth, 100, 135)
            moveLabel(showLastEnemyAttack, 100, 200)
            showLabel(showLastEnemyAttack)
            showLabel(showPlayerHealth)
        if rand is 4:
            playsound('FirePunch.mp3')
            isPlayerTurn = True
            if playerHealth >= 20:
                playerHealth -=20
            else:
                playerHealth = 0
            hideLabel(showPlayerHealth)
            hideLabel(showLastEnemyAttack)
            showPlayerHealth = makeLabel("Player health: " + str(playerHealth), 28, 0, 0, "white", "Arial", "black")
            showLastEnemyAttack = makeLabel("Most recent enemy attack: infer the connections between events that aren't explicitly linked", 20, 0, 0, "white", "Arial", "black")
            moveLabel(showPlayerHealth, 100, 135)
            moveLabel(showLastEnemyAttack, 100, 200)
            showLabel(showLastEnemyAttack)
            showLabel(showPlayerHealth)
    if enemyHealth is 0 or playerHealth is 0:
        hideLabel(showPlayerHealth)
        hideLabel(showEnemyHealth)
        hideLabel(showLastPlayerAttack)
        hideLabel(showLastEnemyAttack)
        hideLabel(bischof)
        hideSprite(bird)
        hideSprite(move1)
        hideSprite(move2)
        hideSprite(move3)
        hideSprite(move4)
        break;

    tick(30)
    print(enemyHealth)

pygame.mixer.music.stop()
if playerHealth is 0:
    pygame.mixer.music.load("gameover.mp3")
    screen.blit(pygame.image.load("9.jpg").convert_alpha(), (0, 0))
else:
    pygame.mixer.music.load("victory.mp3")
    screen.blit(pygame.image.load("1.jpg").convert_alpha(), (0, 0))
pygame.mixer.music.play()


endWait()

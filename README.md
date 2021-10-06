# Important INFO
---
## the R key can be used to reset the player positions (in this first level at least...)
---
## classes: 
- ####  There are 4 classes, goals, playerx, playery, and wall.
- ####  each of these can be used to create game objectst that take arguments to put them in their represntative places.
    - ###### the use of a different file for these classes is very important for readability and level design
---
## main:
* #### This creates 4 instances of walls, 2 players, and one goal
* ####  each goal is 50 x 50 pixels
* ####  each player is 25 x 25 pixels
* ####  each wall is variable in length and width.
###  Goal:
+ #### each instance of goal has a goalFunc, which is a function given in the creation of the instance that happens on collision with the players.  
+ #### every instance of the goal also is given a position, that can be used to obviously change the position of the goal, or using `goal.rect.center = vec(x, y)`, which changes the center of the goal alternatively you could use `goal.rect.left/right/top/bottom = x/y` to change the specific positions of the bottom or top, but for ease of access, i reccomend using center and remembering that it is a 50x50 square, so add 25, to each side to remember its size.
---
### collision!:
#### collision works very differently from what you may think, for it only affects player velocity and position, first it sets the player position to its previous position (if it hit the wall) and then sets velocity to zero, additionally if it hits the other player, it sets velocity to zero after sending it to its previous' previous position, which prevents the two players getting stuck inside of eachother if colliding on a wall.
---
## friction/gravity
#### the sliding mechanic uses some complex math to use acceleration, and friction (which can be changed using programming later) to change velocity of the player, and in turn change the position by the velocity per frame.
### it is important to note:
+ #### the physics update is a fixed update, as well as combined with the games' art updates, so the game is updating physics and art 60 times every second. 
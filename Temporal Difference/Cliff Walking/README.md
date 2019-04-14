## Cliff Walking
#### The Problem

Presenting the “Hello World” of RL, the Grid World!

![alt_text](https://cdn-images-1.medium.com/max/800/1*XSa5M5BvLbvGLi7b_kCRFQ.png)

The rules are very simple:

You can move only one square per turn
Moving in diagonals is not allowed.
You don’t want to die so if you step in a blue square, “The Cliff” kills you.
You start at the “You’re here” spot.
You’re in a rush, so you want to get to your goal as fast as possible.
First step, represent our problem as something the computer can interact with, we can represent the grid as a 2D array:

![alt_text](https://cdn-images-1.medium.com/max/800/1*IWCVmQ7WoQ7eG2R5k-7AQA.png)

0 represents the empty squares
-1 represent the cliff
1 the goal and 2 the player.
The numbers in bold are the indexes. The choice of what the numbers represent doesn’t really matter, you just need some way to differentiate the squares.

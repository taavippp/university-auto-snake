A self playing snake game made in Python using Pygame.
At first, I tried to make this in JavaScript, but figured that since Python is the popular language used for machine learning, I switched to that and quickly learned Pygame.
I tried using TensorFlow as is evident by _SnakeModel.py, but I ran into errors I didn't understand.
I then tried implementing Dijkstra's algorithm, but it behaved extremely erratically.
The current version evaluates the snake's next moves based on the following criteria:

-  distance to food
-  is the way blocked
-  random number divided with distance to food

A human can play this game as well, even if it starts with the AI automatically.
FPS and other important constants can be adjusted in Constants.py.

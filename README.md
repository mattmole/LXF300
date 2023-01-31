# LXF300 - Pong Tutorial

A basic Pong game, written for Linux Format 300.

In this repo, there are two files:

* tutorial.py
* pong.py

## tutorial.py

This file contains a partially completed game and is what is discussed in the magazine article

* Control the left paddle with the "a" and "z" keys

## pong.py

This file contains a more complete version of a Pong game.

* Control the left paddle with the "a" and "z" keys - these keys only respond to key pressed
* Control the left paddle with the "s" and "x" keys - these keys respond for as long as the key is held down
* Control the right paddle with the "k" and "m" keys - these keys only respond to key pressed
* Control the right paddle with the "j" and "n" keys - these keys respond for as long as the key is held down
* Control the speed of the paddle for both players using the up and down arrows
* Quit the game by closing the window or using the escape key

### Improvements

* Allow the window to be resized and everything scales as expected
* Allow the speed of each paddle to be controlled individually
* Tweak the calculations of the collisions with the paddle as sometimes the ball and paddle can overlap

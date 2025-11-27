Snake AI Demo

Description

This is a Snake game implemented in Python using Pygame.
In addition to the basic movement mechanics, the game features a simple AI that automatically controls the snake to eat apples.

The snake moves on a 20x20 grid

Apples spawn randomly in a safe zone, avoiding corners and edges to allow the AI to survive longer

The snake grows longer when it eats an apple

The game ends if the snake hits the wall or itself

Features
1. AI-controlled snake

Greedy AI: the snake always chooses the direction that moves it closer to the apple

Safety check: before moving, the AI ensures it does not hit the wall or its own body

Fallback logic: if the preferred direction is blocked, the AI selects an alternative safe direction

Helps the snake survive longer and eat more apples compared to manual play

2. Gameplay

Manual control using arrow keys

Press Space to restart after game over

Score is displayed continuously on the screen

Requirements

Python 3.x

Pygame (pip install pygame)

How to run
git clone <repo-url>
cd snake-ai-demo
python snake_ai.py

AI Demo

The AI calculates the movement direction every frame

The AI minimizes the risk of crashing into walls or its own body

Can demonstrate that AI plays more consistently than humans over multiple games

Notes

The current AI is rule-based and does not use machine learning

For a more advanced version, you can implement Q-learning or BFS/A* pathfinding so the snake learns how to survive and eat as many apples as possible

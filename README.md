
# HR.Challenge-3

This repository contains all the files and assets for the Arch 3 challenge of Basecamp.


## Challenge description

### 1. Introduction

Pygame is a powerful library for the development of games with graphics. It is well documented and there are tons of examples and tutorials available on the internet. Team size is 2. For the challenge we recommend a multi-phase approach:

- Grasp the basics of pygame, experiment with It
- Build a basic racing game (oval circuit, car, steering)
- Add the opponent, pit stops and tires
- Add the score and round number
- Add more things you like

### 2. Goal

The goal of the game is to win from the computer car and/or to improve the high score

### 3. General description

The player steers a racecar with his keyboard (arrow keys for example). The player plays against a car controlled by the program. Collisions and crashes decrease the speed and therefore the end score.

### 4. Layout

The basic layout of a circuit is an oval with a pit lane

### 5. Basic game

The minimal game consists of:

- A car steered with keyboard
- A computer opponent (basic behavior)
- A track with pitlane
- Tire change (Hard, Medium, Soft)

### 6. Tire strategy

The player has the possibility to enter the pitlane and change tires (this takes time of course).
There are three versions: Soft, Medium and Hard:

<details>
<summary>Soft tires</summary>
These represent the fastest rubber, but are likely to wear out before the harder compounds do.
</details>

<details>
<summary>Medium tires</summary>
This is the compromise compound. It's usually slower than the softs but faster than hards. And it should last longer than the softs, but not as long as hards!
</details>

<details>
<summary>Hard tires</summary>
These provide the least grip, but are supposed to remain in working order the longest
</details>

### 7. Official documentation

[Official challenge document](https://hrnl.sharepoint.com/:b:/r/sites/CMI-BaseCamp22023-2024/CMIBaseCamp2%20%202023%20%202024%20%20Document%20Library/Arch%203/Week%2012/Lesson%20Material/Challenge%20week-12-CHALLENGE%202.3.pdf?csf=1&web=1&e=Lifwa9)

(A Hogeschool Rotterdam account with access to this file is required to open this link)

## Running the project

To run this project on your own PC, you will need install pygame as this is the library required for this project.

This can be done with the following command:

```bash
  pip install pygame
```
    
after this you can directly start the game by running main.py

```bash
  python3 main.py
```

for more information about pygame, Please go to the official pygame website:

[www.pygame.org (Offical website)](https://www.pygame.org)
## Authors

### Project Contributors

- [@ItsDanny](https://github.com/ItsADanny)
- [@Zjoswaa](https://github.com/Zjoswaa)

### Challenge designers

- [Xenia Hasker (Hogeschool Rotterdam)](https://github.com/hogeschool)
- [John Grobben (Hogeschool Rotterdam)](https://github.com/hogeschool)

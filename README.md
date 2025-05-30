# Lode Runner for RISC OS

A recreation of the classic Lode Runner game, built in C for RISC OS. 

## Installing the game
On RiscOS, download the latest release,ddc from the [releases page](https://github.com/Niisoks/RiscOS-Lode_Runner/releases)

Please unzip from within riscos using infozip or other zip programs.

The type should be zip.

I advise extracting first but thats up to you.

You can add up to 50 extra levels on top of the base 150, by adding levelX where X is a number between 150-200 and adding them to your maps dir. You can use maps already in this directory to help you design your maps.

## Features

- **Playable Area:** A 28x16 grid with both destructible and indestructible terrain.
- **Animations:** Sprite-based animations with scaling options (1x, 2x, 3x).
- **Enemy AI:** Enemies feature pathfinding, anti-stuck logic, and context-aware decisions.
- **Digging System:** Includes regeneration and interaction logic.
- **Level Progression:** Save/load functionality with completion tracking for up to 200 levels.
- **Menu:** A paginated level selection menu with visual indicators.
- **RISC OS Native Integration:** Seamless WIMP integration and efficient sprite rendering.


## Controls

### In-Game

- **Up, down, left, right:** Move
- **Z / X:** Dig Left / Right
- **Q:** Return to Menu

### Menu

- **Up, Down:** Select Level
- **Left, Right:** Page Navigation
- **Z:** Start Selected Level
- **1 / 2 / 3:** Set Scale & Exit

## Architecture Overview

### `main.c/h` – Game Engine

- `initialiseGame()`: Initializes the game state.
- `updateGame()`: The main game loop, running at 25 FPS.
- `processKeyPress()`: Handles user input.
- `loadLevelFromPath()`: Loads external level files.
- `trackKeyStates()`: Manages persistent key states.

### `entity.c/h` – Entity System

Defines the `Entity` structure and functions for character movement and interaction:
```c
typedef struct {
  int tileX, tileY;
  float visualX, visualY;
  float targetX, targetY;
  Direction moveDir;
  int isMoving;
} Entity;

```

- `movePlayer()`: Controls player movement.
- `applyGravity()`: Simulates falling.
- `updateLogicalPosition()`: Synchronizes visual and logical states.
- `getPlayerSprite()`: Selects the appropriate player sprite based on context.
- `dig()`: Manages the digging sequence.

### `enemy.c/h` – Enemy AI

Contains the logic for enemy behaviour:

- `findBestDirection()`: Implements pathfinding logic.
- `checkLedgeDrop()` / `checkLadderClimb()`: Enables context-aware decisions for movement.
- `canReachPosition()`: Checks if a position is reachable.
- `updateEnemyHoleEscape()`: Manages enemy escape from holes.

The AI supports climbing, dropping, pursuit, prevention from getting stuck, and controlled regeneration timing.

### `render.c/h` – Rendering

Manages all visual output:

- `render()`: The full render pipeline.
- `drawBlackSquaresOnScreen()`: Clears the screen.
- `checkForGold()`: Handles gold collection visuals.
- `isWalkable()` / `supports()`: Performs collision and support checks.

### `menu.c/h` – Menu

Handles the in-game menu system:

- `loadLevelList()`: Loads available level files.
- `renderMenu()`: Draws the menu user interface.
- `processMenuInput()`: Manages menu input.

This module tracks completion status, the last selected level, and handles page navigation.

### `text.c/h` – Text System

Provides text rendering utilities:

- `renderText()` / `renderTextCentered()`: Outputs text.
- `debugPrint()`: Manages a scrolling debug console.
- `setCenteredMessage()`: Displays timed in-game messages.

### `config.c/h` – Config & Saves

Manages game settings and saved progress:

- `loadConfig()` / `saveConfig()`: Handles persistence of game settings.
- `markLevelCompleted()`: Tracks completed levels.
- `setGameSize()`: Applies display scaling.

### `wimp.c/h` – RISC OS Integration

Facilitates native RISC OS integration:

- Native WIMP windowing.
- Sprite file loading and dynamic scaling.
- Keyboard and event loop management.


## Game Mechanics

- **Digging:** Features a 4-frame animation and timed regeneration.
- **Enemies:** Pursue the player, climb, drop, and escape from holes.
- **Physics:** Includes gravity, ledge interactions, and smooth movement interpolation.
- **Levels:** Loaded from external files (e.g., `maps/level1`, `maps/level2`).
- **Progress:** Up to 200 levels are tracked via a dedicated save file.


## File Structure

```
!LodeRunner/
├── sprites  # Sprite graphics
├── maps/  # Level files
├── config # Saved settings
└── save # Level completion data

```


## Building

To build this project, you will need:

- A RiscOS Machine / RPCEmu
- GCC for RiscOS
- OSLib for WIMP and sprite integration.

On your RiscOS setup, launch !GCC and setVars on OSLib. Then navigate to the directory where LodeRunner is, open up !LodeRunner and middle-click > set directory. Then open a task window and type make. This will build the project.


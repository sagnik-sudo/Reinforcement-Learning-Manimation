# Reinforcement Learning Manimation

This repository contains manimation code for a Reinforcement Learning video. The animations illustrate key concepts in reinforcement learning, including Markov Decision Processes (MDPs), Bellman equations, policy evaluation, policy improvement, and dynamic programming.

## Repository Structure

- `/rl_animation.py`: The main Python script containing the manim animation code for the video.

## Requirements

- Python 3.7 or higher
- [manim](https://www.manim.community/) — the mathematical animation engine
- NumPy

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install the required dependencies:**

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

    Install the dependencies:

    ```bash
    pip install manim numpy
    ```

## How to Run the Animation

Use the manim command to render the animation. For example:

```bash
manim -pql rl_animation.py FullRLAnimation
```

This command will render the `FullRLAnimation` scene in low quality and preview it once rendering is complete. To change the quality, adjust the `-pql` flag (e.g., `-pqh` for high quality).

## Customization

Feel free to modify the animation code in `rl_animation.py` to explore different aspects of reinforcement learning and dynamic programming.

Happy animating!
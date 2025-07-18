# Educational Manimations Collection

This repository contains manimation code for various educational projects. The animations illustrate key concepts across different computer science and machine learning topics through visual demonstrations.

## Repository Structure

- `rl_manim.py`: Reinforcement Learning animations covering MDPs, Bellman equations, Q-learning, SARSA, Deep Q-Networks, Policy Gradients, and more
- `robin_hood_array.py`: Robin Hood Hashing animations demonstrating insertion and deletion processes in hash tables
- `media/`: Output directory containing rendered video files

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

## How to Run the Animations

Use the manim command to render the animations. Here are some examples:

### Reinforcement Learning Animations

```bash
# Render all RL scenes in sequence
manim -pql rl_manim.py IntroRLScene
manim -pql rl_manim.py MDPPolicyScene
manim -pql rl_manim.py DiscountedRewardsScene
# ... and so on for other scenes

# Or render a specific scene
manim -pql rl_manim.py DeepQScene
```

### Robin Hood Hashing Animations

```bash
# Render insertion process
manim -pql robin_hood_array.py RobinHoodInsertion

# Render deletion process
manim -pql robin_hood_array.py RobinHoodDeletion
```

The `-pql` flag renders in low quality with preview. For higher quality, use `-pqh` for high quality or `-pqk` for 4K quality.

## Customization

Feel free to modify the animation code in `rl_manim.py` and `robin_hood_array.py` to explore different aspects of these computer science concepts or add your own educational animations.

Happy animating!
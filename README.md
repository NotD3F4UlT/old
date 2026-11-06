# old

> *"Just found some older code while cleaning up my PC and they are pretty basic—either math question solvers which I just coded at that time and forgot, now I wanna preserve them but also clear up space that's why uploading those here."*

A preservation archive of early coding experiments, math puzzle solvers, C exercises, and reference notes from 2024.

---

## 📁 Repository Structure

```
├── C/                      # C exercises, Python math solvers, and batch launchers
│   ├── b.c                 # Basic C arithmetic / float multiplication test
│   ├── g.c                 # C multiplication program
│   ├── input.c             # Scientific calculation in C (electron mass scaling)
│   ├── import math.py      # Solver for sqrt(a) + sqrt(b) = sqrt(n)
│   ├── pythagoras theorem.py # Pythagorean triplet finder for a given hypotenuse
│   ├── Prime Calculator.py # Factor finder and primality test
│   ├── game.py             # 2D WASD moving rectangle prototype in Pygame
│   ├── b.py                # Comedic number guessing prank script
│   ├── q.py                # Ratio of square roots calculator
│   ├── Untitled-1.py       # Loop scratchpad
│   ├── Untitled-2.py       # Basic multiplication prompt
│   ├── compute_maths.bat   # Windows one-click launcher for import math.py
│   ├── Pythagoras.bat      # Windows one-click launcher for pythagoras theorem.py
│   └── prime.bat           # Windows one-click launcher for Prime Calculator.py
├── docs/                   # Reference study guides
│   ├── 1 The Ultimate C Handbook.pdf
│   └── Trigonometry.pdf
├── web/                    # Web / frontend experiments
│   ├── wheel-of-love/      # Interactive spinning wheel widget (HTML / CSS / JS)
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   └── Document.html       # HTML starter template
└── x=[1,2,3].py            # 4-line snippet testing Python list mutability / references
```

---

## 🧮 Math & Python Logic

### 1. `import math.py` (`compute_maths.bat`)
Finds non-negative integer pairs $(a, b)$ that satisfy:
$$\sqrt{a} + \sqrt{b} = \sqrt{n}$$
By rearranging the equation to $a = (\sqrt{n} - \sqrt{b})^2 = n - 2\sqrt{nb} + b$, the script iterates through $b \in [0, n]$, verifies if $n \cdot b$ is a perfect square, and extracts all integer solutions.

### 2. `pythagoras theorem.py` (`Pythagoras.bat`)
Given a hypotenuse $c$, iterates $b \in [1, c]$ and computes $a = \sqrt{c^2 - b^2}$ to find all valid right-triangle integer legs $(a, b)$ satisfying:
$$a^2 + b^2 = c^2$$

### 3. `Prime Calculator.py` (`prime.bat`)
Given an integer $n$, checks divisors $i$ up to $\lfloor\sqrt{n}\rfloor$. Outputs all factor pairs $(q, i)$ or confirms if the number is prime.

### 4. `game.py`
A simple 2D interactive test written with `pygame`. Sets up a 1920×1080 display with a controllable green rectangle responding to `W`, `A`, `S`, `D` keystrokes and bounded within screen edges.

### 5. `b.py`
A number guessing game (`1` or `2`) with a playful "fake ransomware self-destruct" countdown and humorous text sequence.

---

## 🛠️ Requirements & Running

- **Python 3.x**:
  ```bash
  python "C/Prime Calculator.py"
  python "C/pythagoras theorem.py"
  python "C/import math.py"
  ```
- **Pygame** (for `game.py`):
  ```bash
  pip install pygame
  python "C/game.py"
  ```
- **C Compiler (GCC / MinGW)**:
  ```bash
  gcc C/input.c -o input.exe
  ./input.exe
  ```

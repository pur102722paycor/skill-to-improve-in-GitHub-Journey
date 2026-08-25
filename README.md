# Skill-to-Improve-in-GitHub-Journey

A practical framework for **designing and learning Python with GitHub Copilot**.

## 📚 Learning Path

```
python_learning/
├── 01_basics/
│   ├── 01_variables_and_data_types.py   – int, float, str, bool, None, type conversion
│   ├── 02_control_flow.py               – if/elif/else, for, while, break, continue
│   ├── 03_functions.py                  – def, default args, *args, **kwargs, lambda
│   └── 04_collections.py               – list, tuple, set, dict, comprehensions
├── 02_intermediate/
│   ├── 01_oop.py                        – classes, inheritance, @classmethod, @staticmethod
│   ├── 02_error_handling.py            – try/except/finally, custom exceptions
│   └── 03_file_io.py                   – text files, JSON, append mode
├── 03_advanced/
│   └── 01_advanced_concepts.py         – decorators, generators, context managers
├── exercises/
│   └── exercises.py                    – six hands-on exercises to solve
└── solutions/
    └── answers.py                      – reference solutions with self-tests
```

## 🚀 Getting Started

1. **Clone this repository**

   ```bash
   git clone https://github.com/pur102722paycor/skill-to-improve-in-GitHub-Journey.git
   cd skill-to-improve-in-GitHub-Journey
   ```

2. **Run any module directly**

   ```bash
   python python_learning/01_basics/01_variables_and_data_types.py
   ```

3. **Work through the exercises**

   Open `python_learning/exercises/exercises.py`, read each TODO, write your solution,
   then run the file and compare with `python_learning/solutions/answers.py`.

## 🤖 Using GitHub Copilot Effectively

| Technique | How to use it |
|-----------|---------------|
| **Docstring-first** | Write the docstring before the function body — Copilot suggests the implementation |
| **Comment-driven** | Add `# TODO: ...` or `# create a list of ...` and accept Copilot's suggestion |
| **Incremental acceptance** | Press `Tab` to accept, `Alt+]` / `Alt+[` to cycle through alternatives |
| **Chat mode** | Ask Copilot Chat to explain a concept or refactor a function |
| **Test generation** | Write a function, then ask Copilot to generate unit tests |

## ✅ Prerequisites

- Python 3.9 or later
- [GitHub Copilot](https://github.com/features/copilot) extension in VS Code or JetBrains IDE

## 📖 Suggested Study Order

1. Basics (01–04) — work through each file top to bottom
2. Intermediate (01–03) — run the examples, modify them, experiment
3. Advanced — focus on one pattern at a time (decorator → generator → context manager)
4. Exercises — attempt each exercise before looking at the solution

Happy coding! 🐍
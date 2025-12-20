# 🏆 Challenges and Competitions 🚀

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](samiratra95@gmail.com)


Welcome to my comprehensive collection of solutions for various programming challenges and competitions! This repository showcases my work across multiple platforms including Kaggle, LeetCode, HackerEarth, Google Code Golf, and NeurIPS competitions. I'm passionate about problem-solving, machine learning, and AI, and this repository documents my journey through diverse computational challenges.

---

## 📚 Table of Contents

- [Agents Intensive Capstone Project](#-agents-intensive-capstone-project)
- [Machine Learning Competitions](#-machine-learning-competitions)
  - [ML Olympiad 2024](#-ml-olympiad-2024)
  - [NeurIPS 2025 - Google Code Golf Championship](#-neurips-2025---google-code-golf-championship)
  - [ESA Fake or Real Challenge](#%EF%B8%8F-esa-fake-or-real-the-impostor-hunt-in-texts)
  - [Viz Wiz Image Classification](#%EF%B8%8F-viz-wiz-image-classification-challenge)
- [Algorithmic Challenges](#-algorithmic-challenges)
  - [LeetCode](#-leetcode)
  - [Google Kick Start](#-google-kick-start)
  - [HackerEarth](#-hackerearth)
- [How to Use](#-how-to-use)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🤖 Agents Intensive Capstone Project

**Code Broker** - An AI-Powered Multi-Agent Code Assessment System

[![ADK](https://img.shields.io/badge/Google-ADK-4285F4?logo=google)](https://google.github.io/adk-docs/)

- **Competition:** [Agents Intensive Capstone Project](https://www.kaggle.com/competitions/agents-intensive-capstone-project)
- **Description:** Code Broker is an intelligent multi-agent system built with Google's Agent Development Kit (ADK) that automatically analyzes code files, directories, or GitHub repositories and generates comprehensive assessment reports with actionable improvement recommendations.

### ✨ Key Features

- 🔍 **Multi-Source Analysis**: Supports files, directories, and GitHub repositories
- 📊 **Comprehensive Scoring**: Metrics for correctness, security, style, and maintainability
- 🤖 **5-Agent Architecture**: Parallel processing with specialized AI agents
- 📝 **Beautiful Reports**: Markdown and HTML formatted assessment outputs
- ⚡ **Fast & Reliable**: Async processing with retry mechanisms
- 🎨 **Pylint Integration**: Automated Python code quality analysis

### 📂 Project Contents

```
Agents_intensive_capstone_project/
├── code_broker_documented.ipynb   # Main executable notebook with full documentation
├── requirements.txt                # Python dependencies (google-genai, etc.)
└── README.md                       # Detailed project documentation
```

### 🏗️ Multi-Agent Architecture

- **Report Generator** (Orchestrator): Coordinates the entire workflow
- **Sequential Pipeline Agent**: Manages assessment flow
- **Parallel Assessment Agent**: Runs 3 agents concurrently:
  - Correctness Assessor
  - Style Assessor
  - Description Generator
- **Improvement Recommender**: Synthesizes findings into actionable recommendations

**Reference:**
```bibtex
@misc{agents-intensive-capstone-project,
  author = {Walter Reade and Ashley Chow},
  title = {Agents Intensive - Capstone Project},
  year = {2025},
  howpublished = {\url{https://kaggle.com/competitions/agents-intensive-capstone-project}},
  note = {Kaggle}
}
```

[📖 Read Full Documentation](Agents_intensive_capstone_project/README.md)

---

## 🧬 Machine Learning Competitions

### 🤖 ML Olympiad 2024

A collection of machine learning challenges focusing on real-world applications.

#### 🌋 Predicting Earthquake Damage

- **Challenge:** [ML Olympiad - Predicting Earthquake Damage](https://www.kaggle.com/competitions/ml-olympiad-predicting-earthquake-damage)
- **Description:** Predict the level of damage to buildings caused by earthquakes based on various building and location features.
- **Technology Stack:**
  - TensorFlow & Keras for deep learning
  - Feedforward neural network architecture
  - Feature engineering for building characteristics
- **Files:**
  - `ML_Olympiad_2024/Predicting_earthquack_damage/EarthQuake.ipynb` - Main solution notebook
  - `ML_Olympiad_2024/Predicting_earthquack_damage/EarthQuakeDamage.py` - Python implementation
  - Multiple submission CSV files (submission.csv through submission7.csv)

**Reference:**
```bibtex
@misc{ml-olympiad-predicting-earthquake-damage,
  author = {Tensor Girl},
  title = {ML Olympiad - Predicting Earthquake Damage},
  year = {2024},
  howpublished = {\url{https://kaggle.com/competitions/ml-olympiad-predicting-earthquake-damage}},
  note = {Kaggle}
}
```

#### 🐢 The Turtle Vision Challenge

- **Challenge:** [ML Olympiad - TurtleVision Challenge](https://www.kaggle.com/competitions/mlo2024mlact)
- **Description:** Classify images of marine life to distinguish between different species of turtles, jellyfish, and plastic pollution - an important task for marine conservation.
- **Technology Stack:**
  - Transfer learning with pre-trained InceptionV3
  - Fine-tuning on marine life dataset
  - Computer vision for conservation
- **Files:**
  - `ML_Olympiad_2024/Turtle_vision_challenge/TurtleVision_Challenge.ipynb` - Main solution
  - Multiple prediction CSV files for different model versions

**Reference:**
```bibtex
@misc{mlo2024mlact,
  author = {Ahmed LOUHICHI and Anas Lahdhiri and Imen MASMOUDI and Mehdi SOMRANI and Seif Eddine Achour},
  title = {ML Olympiad - TurtleVision Challenge},
  year = {2024},
  howpublished = {\url{https://kaggle.com/competitions/mlo2024mlact}},
  note = {Kaggle}
}
```

[📖 Read ML Olympiad Documentation](ML_Olympiad_2024/README.md)

---

### 🧠 NeurIPS 2025 - Google Code Golf Championship

- **Competition:** [NeurIPS 2025 - Google Code Golf Championship](https://www.kaggle.com/competitions/google-code-golf-2025)
- **Description:** Part of the NeurIPS 2025 conference, this competition challenges participants to write the shortest possible code for solving ARC (Abstraction and Reasoning Corpus) tasks. The goal is to optimize for code length while maintaining correctness, encouraging creative and efficient solutions.
  
### 🎯 What is Code Golf?

Code Golf is a type of recreational computer programming competition where participants strive to achieve the shortest possible source code that implements a specified algorithm. In this challenge, every character counts!

### 📂 Project Contents

```
NeurIPS_2025_Google_Code_Golf_Championship/
├── generate_all_solvers.py      # Script to generate solver code for all tasks
├── run_and_visualize.py         # Execution and visualization utilities
├── visualize_arc_tasks.py       # ARC task visualization tools
└── generated_solver/            # Contains 400+ task-specific solvers
    ├── task001.py through task400.py (and beyond)
```

### 🔧 Key Components

- **Automated Solver Generation:** Scripts to programmatically generate optimized solutions
- **Visualization Tools:** Utilities to visualize ARC puzzle patterns and transformations
- **400+ Task Solutions:** Individual Python solvers for diverse reasoning challenges
- **Code Optimization:** Focus on minimal character count while maintaining functionality

**Reference:**
```bibtex
@misc{google-code-golf-2025,
  author = {Michael D. Moffitt and Divy Thakkar and Ryan Burnell and Orhan Firat and Walter Reade and Sohier Dane and Addison Howard},
  title = {NeurIPS 2025 - Google Code Golf Championship},
  year = {2025},
  howpublished = {\url{https://kaggle.com/competitions/google-code-golf-2025}},
  note = {Kaggle}
}
```

---

### 🕵️ ESA Fake or Real: The Impostor Hunt in Texts

- **Challenge:** [Fake or Real: The Impostor Hunt in Texts](https://www.kaggle.com/competitions/fake-or-real-the-impostor-hunt)
- **Organizer:** European Space Agency (ESA)
- **Description:** Distinguish between real human-written texts and AI-generated fake texts using natural language processing techniques.

### 🔬 Approaches Implemented

1. **English Word Detection Baseline**
   - Uses `langdetect` library to calculate proportion of English words
   - Simple and interpretable method
   - Assumes real text has higher percentage of English words

2. **Character-Level Baseline**
   - Analyzes proportion of Latin characters
   - Language-agnostic signal for text classification
   - Provides alternative to word-based detection

3. **Generative AI Detection**
   - Leverages Google's `gemma-3-27b-it` model
   - Step-by-step analysis to determine text authenticity
   - Advanced approach using cutting-edge LLMs

### 📂 Project Contents

```
ESA_Fake_or_Real:_The_Impostor_Hunt_in_Texts/
├── baseline-solution.ipynb      # Complete solution with all three approaches
└── README.md                    # Detailed project documentation
```

### 🛠️ Technology Stack

- Python 3.x
- langdetect for language detection
- Google Generative AI (Gemma models)
- scikit-learn for evaluation
- pandas for data processing

**Reference:**
```bibtex
@misc{fake-or-real-the-impostor-hunt,
  author = {Agata Kaczmarek and Dawid Płudowski and Krzysztof Kotowski and Ramez Shendy and Artur Janicki and Przemysław Biecek and Evridiki Ntagiou},
  title = {Fake or Real: The Impostor Hunt in Texts},
  year = {2025},
  howpublished = {\url{https://kaggle.com/competitions/fake-or-real-the-impostor-hunt}},
  note = {Kaggle}
}
```

[📖 Read Full Documentation](ESA_Fake_or_Real:_The_Impostor_Hunt_in_Texts/README.md)

---

### 🖼️ Viz Wiz Image Classification Challenge

- **Challenge:** [Viz Wiz Image Classification](https://vizwiz.org/tasks-and-datasets/image-classification/)
- **Description:** Classify images from the Viz Wiz dataset, which contains images taken by people who are blind or have low vision. This challenge has important implications for accessibility technology.

### 📂 Project Contents

```
Viz_Wiz_Challenges/
├── Classifier.ipynb             # Image classification solution
└── README.md                    # Project documentation
```

### 🎯 Impact

This project contributes to making technology more accessible for visually impaired individuals by improving image understanding and classification systems.

[📖 Read Full Documentation](Viz_Wiz_Challenges/README.md)

---

## 🧩 Algorithmic Challenges

### 🧠 LeetCode

Solutions to algorithmic problems from [LeetCode](https://leetcode.com/), a platform for practicing coding skills and preparing for technical interviews.

#### 📝 Solutions

```
LeetCode/
├── AddTwoNumbers.py            # Linked list manipulation
├── PalindromNumber.py          # Number theory and palindromes
└── TwoSumAlgorithm.py          # Hash table and array processing
```

Each solution demonstrates:
- ✅ Efficient algorithms and data structures
- 📊 Time and space complexity optimization
- 💡 Clean, readable Python code

---

### 🏅 Google Kick Start

Collection of solutions for [Google Kick Start](https://codingcompetitions.withgoogle.com/kickstart), Google's global online coding competition (now retired but historically significant).

#### 📝 Solutions

```
Google_KickStart_Multiple_Years/
├── BuildingPalindromes.py      # String manipulation and palindromes
├── CGame.py                    # Game theory
├── CentauriPrime.py            # Logic and conditionals
├── ChallengeNine.py            # Number theory
├── GBusCount.ipynb             # Array processing
├── MagicalWellOfLilies.py      # Dynamic programming
├── NewPassword.py              # String processing
├── Palindrome.py               # Advanced palindrome algorithms
├── RunninginCircles.py         # Simulation
├── SamplProblem.ipynb          # Sample problem walkthrough
├── SortTheFabrics.ipynb        # Sorting algorithms
├── Walktober.py                # Array manipulation
├── WiggleWalk.ipynb            # Grid traversal
└── infinity.py                 # Mathematical puzzles
```

**Technologies Used:**
- Python for implementation
- Jupyter notebooks for interactive solutions
- Advanced algorithms: DP, greedy, graph theory, number theory

---

### 🌍 HackerEarth

Solutions for challenges on [HackerEarth](https://www.hackerearth.com/challenges/), a competitive programming platform.

```
HackerEarth/
└── MaximumBoarders.py          # Optimization problem
```

---

## 🛠 How to Use

### General Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Samir-atra/Challenges_and_Competitions.git
   cd Challenges_and_Competitions
   ```

2. **Navigate to specific challenge:**
   ```bash
   cd [Challenge_Directory]
   ```

3. **Install dependencies:**
   - Most projects include their own `requirements.txt`
   - For general Python scripts, standard libraries are typically sufficient
   - For ML projects: TensorFlow, Keras, scikit-learn, pandas, numpy
   - For AI agent projects: Google ADK, google-genai

### Running Solutions

**Python Scripts:**
```bash
python script_name.py
```

**Jupyter Notebooks:**
```bash
jupyter notebook notebook_name.ipynb
# Or use VS Code, Google Colab, or JupyterLab
```

### ⚠️ Important Notes

- **Data Paths:** Some file paths in notebooks may be hardcoded. Update these to match your local directory structure.
- **API Keys:** Projects using external APIs (e.g., Google AI) require API keys. Set these up in `.env` files as documented in individual project READMEs.
- **Dependencies:** Each major project has its own `requirements.txt` file. Install dependencies specific to that project.

---

## 🤝 Contributing

I welcome collaboration and suggestions! Here's how you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-solution`)
3. **Commit your changes** (`git commit -m 'Add amazing solution'`)
4. **Push to the branch** (`git push origin feature/amazing-solution`)
5. **Open a Pull Request**

### Contribution Ideas

- 💡 Alternative solutions to existing problems
- 🐛 Bug fixes or optimizations
- 📝 Documentation improvements
- 🆕 Solutions to new challenges
- 🧪 Test cases and validation

---

## 📊 Repository Statistics

- **Total Competitions:** 8+ (Kaggle, LeetCode, Google Kick Start, HackerEarth, NeurIPS)
- **Machine Learning Projects:** 5
- **AI Agent Systems:** 1 (Multi-agent architecture)
- **Algorithmic Solutions:** 20+
- **Technologies:** Python, TensorFlow, Keras, Google ADK, Jupyter
- **Domains:** ML, NLP, Computer Vision, AI Agents, Code Golf, Competitive Programming

---

## 👨‍💻 Author

**Samer Atra**
- GitHub: [@Samir-atra](https://github.com/Samir-atra)
- Passionate about AI, Machine Learning, and Competitive Programming

---

## 📄 License

This repository is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for complete details.

```
Copyright 2025 Samer Atra

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
```

---

## 🌟 Acknowledgments

Special thanks to all the competition organizers:
- Kaggle and the competition hosts
- Google (Kick Start, ADK, Code Golf)
- European Space Agency (ESA)
- NeurIPS Conference
- LeetCode, HackerEarth, and VizWiz communities

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Happy Coding! 🚀**

</div>

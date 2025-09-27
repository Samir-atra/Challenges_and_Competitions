# Fake or Real: The Impostor Hunt in Texts

This repository contains solutions for the Kaggle challenge "Fake or Real: The Impostor Hunt in Texts". Organized by the European Space Agency ESA ,The goal of the challenge is to distinguish between real human-written texts and fake AI-generated texts.

Link to the challenge: https://www.kaggle.com/competitions/fake-or-real-the-impostor-hunt

The `baseline-solution.ipynb` notebook implements and evaluates several approaches to tackle this problem.

## Approaches

The notebook explores three different methods for text classification:

1.  **English Word Detection Baseline**: This simple and interpretable method uses the `langdetect` library to calculate the proportion of English words in each text. The assumption is that the "Real" text will have a higher percentage of English words.

2.  **Character-Level Baseline**: As an alternative to word-based detection, this method analyzes the proportion of Latin characters within each text. This provides a different, language-agnostic signal for distinguishing between the texts.

3.  **Generative AI Detection**: This advanced approach uses Google's `gemma-3-27b-it` model. It provides both texts to the model and prompts it to perform a step-by-step analysis to determine which one is more likely to be real.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.x
-   Jupyter Notebook or a compatible environment (like VS Code with the Jupyter extension).
-   A Google AI API key for the Generative AI approach.

### Installation

1.  **Clone the repository** (if it's in a git repository):
    ```bash
    git clone <your-repository-url>
    cd "Kaggle challenge Fake or Real: The Impostor Hunt in Texts"
    ```

2.  **Install dependencies**: The required Python packages are listed and installed in the notebook. You can also install them manually:
    ```bash
    pip install pandas unicodedata2 scikit-learn mediapipe langdetect google-generativeai
    ```

3.  **Data Setup**: Download the competition data from Kaggle and place it in the `fake-or-real-the-impostor-hunt/data/` directory. The expected structure is:
    ```
    .
    ├── fake-or-real-the-impostor-hunt/
    │   └── data/
    │       ├── train/
    │       ├── test/
    │       └── train.csv
    └── baseline-solution.ipynb
    ```

### Usage

1.  Open the `baseline-solution.ipynb` notebook.
2.  Update the file paths for the dataset if they differ from the ones in the notebook.
3.  If you are using the Generative AI approach, make sure to add your Google AI API key in the `genai.Client(api_key="...")` call.
4.  Run the cells in the notebook to process the data, train the models (where applicable), and generate predictions.
5.  The notebook will produce submission files (e.g., `sample_submission_1.csv`, `sample_submission_2.csv`) in the root directory.

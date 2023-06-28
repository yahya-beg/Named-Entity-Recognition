
# Text Analyzer

Text Analyzer is a web application that allows you to analyze text and extract named entities using the Spacy library in Python.

## Features

- Enter text to analyze and extract named entities.
- Displays the extracted named entities along with their labels.
- Handles errors gracefully and displays error messages if any.

## Installation

1. Clone the repository or download the project files.

```bash
git clone <repository-url>
```

2. Install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

3. Download the `en_core_web_sm` model by running the following command:

```bash
python -m spacy download en_core_web_sm
```

## Usage

1. Open the project in a code editor of your choice.

2. Run the Flask web application by executing the following command in the terminal:

```bash
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000` to access the Text Analyzer.

4. Enter the text you want to analyze in the provided text area.

5. Click the "Analyze" button to process the text and extract named entities.

6. The named entities and their labels will be displayed in a colored box below the text input area.

7. Repeat steps 4-6 to analyze additional texts.

8. To quit the Text Analyzer, press `CTRL+C` in the terminal where the Flask application is running.

## Technologies Used

- Python
- Flask
- Spacy
- HTML
- CSS
- JavaScript




## Acknowledgments

- [Spacy](https://spacy.io/) - For providing the natural language processing library.
- [Flask](https://flask.palletsprojects.com/) - For the web application framework.
- [OpenAI](https://openai.com/) - For providing the underlying language model used for generating responses.


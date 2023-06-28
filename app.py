from flask import Flask, request, jsonify
import spacy
from flask_cors import CORS





app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json['text']
        doc = nlp(text)

        entities = []
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_
            })

        result = {
            'entities': entities,
            'error': None
        }

    except Exception as e:
        result = {
            'entities': [],
            'error': str(e)
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run()


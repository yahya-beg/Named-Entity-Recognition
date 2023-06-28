import spacy

def analyze_text():
    nlp = spacy.load("en_core_web_sm")
    
    while True:
        try:
            text = input("Enter the text to analyze (or 'q' to quit): ")
            
            if text.lower() == 'q':
                break
            
            doc = nlp(text)
            
            if not doc.ents:
                print("No named entities found.")
            else:
                for ent in doc.ents:
                    print(f"Text: {ent.text}\tLabel: {ent.label_}")
        
        except Exception as e:
            print("An error occurred:", str(e))
    
    print("Thank you for using the text analyzer.")

analyze_text()
import joblib
import spacy
nlp = spacy.load("en_core_web_sm")

classifier = joblib.load("spam_classifier.pkl")

# Load the vectorizer
vectorizer = joblib.load("vectorizer.pkl")

# Load the label encoder
label_encoder = joblib.load("label_encoder.pkl")

def getPrediction(input):
    corpus=[]
    line=input.lower()
    doc = nlp(line)
    filtered_tokens = [token.lemma_ for token in doc if not token.is_stop]
    filtered_tokens2=[token for token in filtered_tokens if token!="..."] 
    if len(filtered_tokens2)>0:
        corpus.append(" ".join(filtered_tokens2))
    processed_text = vectorizer.transform(corpus).toarray()
    # print(processed_text)
    result=classifier.predict(processed_text)
    if result[0]==1:
        return "spam"
    else:
        return "not a spam"
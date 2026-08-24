
import streamlit as st
import joblib
import json
from urllib.parse import unquote

#  loads trained model, vectoriser, and example requests 
@st.cache_resource
def load_everything():
    model = joblib.load("demo_model.joblib")
    vectorizer = joblib.load("demo_vectorizer.joblib")
    with open("demo_examples.json") as f:
        examples = json.load(f)
    return model, vectorizer, examples

model, vectorizer, examples = load_everything()


#   detection + prevention function 
def analyse(request_text):
    decoded = unquote(unquote(str(request_text)))        # undo URL-encoding
    numbers = vectorizer.transform([decoded])            # converts text to TF-IDF numbers
    label = model.predict(numbers)[0]                    # labelling
    confidence = float(model.predict_proba(numbers).max())  # confidence of winning class
    if label == "Normal":
        action = "ALLOW"
    elif confidence >= 0.90:
        action = "BLOCK"
    else:
        action = "REVIEW"
    return label, confidence, action


# PAGE LAYOUT
st.set_page_config(page_title="AI Web IDS Demo", layout="centered")

st.title(" AI-Driven Web Intrusion Detection & Prevention")
st.caption("MSc Project demonstration- classify a web request and decide the action.")

st.markdown("---")

# Build friendly dropdown labels
options = [f"{e['label']} =  {e['request'][:55]}" for e in examples]
choice = st.selectbox(
    "Select a real captured web request to analyse:",
    options,
    help="These are real requests from  held-out test data the model never saw in training."
)
selected = examples[options.index(choice)]
request_text = selected["request"]
true_label = selected["label"]

st.text_area("Request being analysed:", request_text, height=70, disabled=True)

if st.button("  Analyse Request", type="primary"):
    label, confidence, action = analyse(request_text)

    st.markdown("### Result")
    col1, col2, col3 = st.columns(3)
    col1.metric("Classified as", label)
    col2.metric("Confidence", f"{confidence:.0%}")
    col3.metric("True label", true_label)

    # Decision banner with colour
    if action == "BLOCK":
        st.error(f"  DECISION: **{action}**  =  attack detected with high confidence, request blocked.")
    elif action == "REVIEW":
        st.warning(f"  DECISION: **{action}**  =  suspicious but uncertain, flagged for a human analyst.")
    else:
        st.success(f" DECISION: **{action}**  =  classified as normal traffic, request allowed.")

    # Honest correctness note
    if label == true_label:
        st.caption(" The model classified this correctly.")
    else:
        st.caption(" The model misclassified this example.")

st.markdown("---")
with st.expander("  How this works"):
    st.write(
        "The request is converted into numerical features using TF-IDF character "
        "n-grams, then classified by a Random Forest model trained on the CSIC 2010 "
        "dataset combined with real attacks captured by my honeypot. A rule-based "
        "prevention layer then decides the action: high-confidence attacks are "
        "blocked, uncertain ones are flagged for review, and normal traffic is allowed. "
        "The examples shown are real requests from the held-out test set, so this "
        "demonstrates the model on genuine unseen data."
    )

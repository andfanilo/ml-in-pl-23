import streamlit as st

from utils import load_data
from utils import prepare_data
from utils import produce_confusion
from utils import produce_roc
from utils import round_p
from utils import train_model

st.set_page_config(page_title="Spotify ML", layout="wide")
st.title("Spotify: Predict in Spotify chart")

df, y = load_data()
X_train, X_test, y_train, y_test = prepare_data(df, y)

with st.expander("Data preview"):
    st.dataframe(df.head(15))

#######
# TUTORIAL -
# CREATE THE INPUTS FOR EACH HYPERPARAMETER
#######

with st.sidebar.form(key="hyperparameters_form"):
    st.header("Model Configuration")

    ###### Widgets in here won't rerun the app at every interaction

    submit_button = st.form_submit_button("Click here to run model", type="primary")

if submit_button:
    hyperparameters = {
        "random_state": 42,
        "criterion": "gini",
        "n_estimators": 25,
        "max_depth": 25,
        "min_samples_split": 50,
        "min_samples_leaf": 50,
        "max_features": 25,
        "bootstrap": True,
        "n_jobs": -1,
        "max_samples": 0.8,
    }
    (
        train_score,
        test_score,
        precision,
        recall,
        f1,
        confusion,
        seconds_run,
        fpr,
        tpr,
        roc_auc,
    ) = train_model(hyperparameters, X_train, X_test, y_train, y_test)

    st.write(f"Model ran in: {round(seconds_run,4)} seconds")
    st.metric(label="Training Score", value=round_p(train_score))
    st.metric(
        label="Test Score",
        value=round_p(test_score),
        delta=round_p(test_score - train_score),
    )
    st.metric(label="Precision", value=round_p(precision))
    st.metric(label="Recall", value=round_p(recall))
    st.metric(label="F1", value=round_p(f1))

    st.altair_chart(produce_confusion(confusion), use_container_width=True)
    st.altair_chart(produce_roc(fpr, tpr, roc_auc), use_container_width=True)

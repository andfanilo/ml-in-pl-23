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

    col1, col2 = st.columns(2)
    n_jobs = col1.slider(
        "# of Jobs",
        min_value=-1,
        max_value=8,
        value=-1,
        help="How many cores to use, -1 is all",
    )
    n_estimators = col2.slider(
        "# of Estimators",
        min_value=1,
        max_value=250,
        value=25,
        help="How many decision trees in forest",
    )
    col3, col4 = st.columns(2)
    criterion = col3.selectbox(
        "Criterion",
        options=["gini", "entropy", "log_loss"],
        help="Method for decision logic",
    )
    max_features = col4.selectbox("Max Features", options=["sqrt", "log2", None])
    max_depth = st.slider(
        "Max Depth",
        min_value=1,
        max_value=50,
        value=25,
        help="Max level of decisions per tree",
    )
    max_samples = st.slider(
        "% of Samples",
        min_value=0.01,
        max_value=1.0,
        step=0.01,
        value=0.8,
        help="% of data to use in each tree",
    )
    min_samples_split, min_samples_leaf = st.columns(2)
    min_samples_split = min_samples_split.slider(
        "Min Samples Split",
        min_value=1,
        max_value=10000,
        value=50,
        help="Min # of samples to split",
    )
    min_samples_leaf = min_samples_leaf.slider(
        "Min Samples Leaf",
        min_value=1,
        max_value=10000,
        value=50,
        help="Min samples in a leaf node",
    )

    bootstrap = st.checkbox(
        "Bootstrap", value=True, help="Random Sampling with replacement of data"
    )

    submit_button = st.form_submit_button("Click here to run model", type="primary")

if submit_button:
    hyperparameters = {
        "random_state": 42,
        "criterion": criterion,
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "max_features": max_features,
        "bootstrap": bootstrap,
        "n_jobs": n_jobs,
        "max_samples": max_samples,
    }

    if not hyperparameters["bootstrap"]:
        hyperparameters["max_samples"] = None

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
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric(label="Training Score", value=round_p(train_score))
    col2.metric(
        label="Test Score",
        value=round_p(test_score),
        delta=round_p(test_score - train_score),
    )
    col3.metric(label="Precision", value=round_p(precision))
    col4.metric(label="Recall", value=round_p(recall))
    col5.metric(label="F1", value=round_p(f1))

    col6, col7 = st.columns(2)
    col6.altair_chart(produce_confusion(confusion), use_container_width=True)
    col7.altair_chart(produce_roc(fpr, tpr, roc_auc), use_container_width=True)

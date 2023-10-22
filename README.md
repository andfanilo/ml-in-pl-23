# Streamlit ML in PL 23

## Prerequisites

The recommended way to install Streamlit is using Anaconda. [Detailed instructions here](https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows).

```sh
conda create -n streamlit_env python=3.9
conda activate streamlit_env
pip install streamlit
streamlit version
```

## Intro Playground

Make sure you jump into the `playground` folder: `cd playground`

The first exercise happens in the `playground.py` script.

Open the script in your IDE of choice, then run `streamlit run playground.py` to run the Streamlit server over it.

After you save any changes in the code for the first time, Streamlit will ask if you want to rerun the code. When you accept this, Streamlit will now live-reload your running app on any code change, making for a faster developer experience.

To setup multipage, rename `_pages` into `pages`.

## Analyzing Spotify Data for ML in PL 2023

The main exercise focuses on analyzing the [Most Streamed Spotify Songs](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023).

Make sure you jump into the `spotify_usecase` folder: `cd spotify_usecase`

Then run `streamlit run spotify_ml.py`.

## Resources

Heavily inspired from Liz Carpenter's PyCon 2023 tutorial:
- Video: https://www.youtube.com/watch?v=cw44529_OU8
- Github: https://github.com/LCarpenter87/StreamLit-Pycon-23

fgjspaceman's [Kaggle notebook](https://www.kaggle.com/code/franoisgeorgesjulien/spotify-1-what-does-it-take-to-hit-the-charts) was also a helpful reference for charts.

Link to slides: https://docs.google.com/presentation/d/1netCBbkX0y_vMgBfsZp__lV93ovhRvvguVJTBNHnhrk/edit?usp=sharing
# music_matcher

This repo contains the code for a classical music classifier with machine learning, created for our 2019 CS221 final project.

**Here is the abstract from our paper:**
This project aims to classify classical music by musical era (Baroque, Classical, Romantic, Modern) with composers as a proxy. Using audio processing techniques, such as Short-time Fourier Transform, we extracted features like spectrogram and chromagram of the audio data from two datasets, Free Music Archive and MAESTRO dataset. We used two ensemble classifiers,  AdaBoost and Random Forest, and found that although Adaboost performed marginally better than Random Forest, the latter made more generalizable predictions. Both models achieve an accuracy rate of 60\% on the test data, which is significantly better than the baseline prediction of 45\%. Our project reveals the complexity of the era classification task, and we expect more complex models trained on a larger data set to achieve higher success. 

Created by Yu Jin Lee and Lucas Pauker.

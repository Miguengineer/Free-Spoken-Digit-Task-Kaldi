# Free-Spoken-Digit-Task-Kaldi
This project uses the Kaldi toolkit (https://kaldi-asr.org/) to build an HMM-GMM based for the free spoken digit task, in which we try to detect and classify spoken digits (0-9) from Kaggle database Free Spoken Digit Task (https://www.kaggle.com/joserzapata/free-spoken-digit-dataset-fsdd)

## Data

See https://www.kaggle.com/datasets/joserzapata/free-spoken-digit-dataset-fsdd section About.

A quick data visualization is provided in the Jupyter Notebook ([here](https://github.com/Miguengineer/Free-Spoken-Digit-Task-Kaldi/blob/main/QuickDataVisualization.ipynb)
)


## Preprocessing

One of the tools provided in the Kaggle task made easy to assign each recording to train/test sets. Python file preprocessing.py (python_src/preprocessing.py) does just this train/test split. The required Kaldi files are created automatically with the script make_kaldi_files.py (python_src/make_kaldi_files.py). Directory adjustements must be performed.

## Kaldi training

The training pipeline is executed with the script run.sh. This script in turns calls the Kaldi script make_mfcc.sh (steps/make_mfcc.sh) which performs the feature extraction process in which Mel-Frequency Cepstral Coefficients are obtained. The parameters used in this project are provided through the file mfcc.conf (conf/mfcc.conf). 
Once the features are extracted, the HMM-GMM system is trained using the Kaldi script train_mono.sh (steps/train_mono.sh) that trains a context-free HMM-GMM model, or in other words, a Monophone System (in contrast to Triphone Systems).


## Results

In this simple task, the best result is a Word Error Rate (WER) of 0.00%, which means a perfect transcription for each audio was obtained.







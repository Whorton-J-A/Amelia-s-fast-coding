import os
import sys
import re
import gc
import time
import uuid
import pickle
import warnings
from pathlib import Path
from datetime import date, datetime, timedelta, timezone
from collections import deque

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams["figure.dpi"] = 300

from scipy import stats as spstats
from scipy.stats import gaussian_kde
import pingouin as pg
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.stattools import durbin_watson
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.genmod.generalized_estimating_equations import GEE
from statsmodels.genmod.families import Gaussian
from statsmodels.genmod.cov_struct import Exchangeable, Autoregressive

from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    LabelEncoder,
    label_binarize,
)

from sklearn.pipeline import Pipeline
from sklearn.base import clone

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    KFold,
    StratifiedGroupKFold,
    LeaveOneGroupOut,
    GridSearchCV,
)

from sklearn.feature_selection import RFE, SequentialFeatureSelector
from sklearn.inspection import permutation_importance

from sklearn.metrics import (
    make_scorer,
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    auc,
    precision_recall_curve,
    RocCurveDisplay,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    root_mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
    r2_score,
)

from xgboost import XGBClassifier, XGBRegressor

import shap

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, TensorDataset
from torchmetrics.classification import (
    BinarySpecificity,
    BinaryRecall,
    BinaryPrecision,
    BinaryAccuracy,
    BinaryF1Score,
    BinaryAUROC,
    BinaryConfusionMatrix,
    MulticlassSpecificity,
    MulticlassRecall,
    MulticlassAccuracy,
    MulticlassF1Score,
    MulticlassConfusionMatrix,
)

import psycopg2
from sqlalchemy import create_engine, text
import garminconnect

from pylsl import StreamInfo, StreamOutlet, StreamInlet, resolve_byprop

from IPython.display import display, clear_output

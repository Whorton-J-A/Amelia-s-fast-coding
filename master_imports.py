'''system imports'''
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
'''numpy and pandas for data management'''
import numpy as np
import pandas as pd
'''ploting for visuals'''
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
plt.rcParams["figure.dpi"] = 300
'''stats models'''
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
'''encoding, standardizing, and binarizing '''
from sklearn.preprocessing import (
    StandardScaler,
    RobustScaler,
    LabelEncoder,
    label_binarize,
)
'''creating pipelines'''
from sklearn.pipeline import Pipeline
from sklearn.base import clone
'''SKlearn modeling'''
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
'''data spliting methods '''
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    KFold,
    StratifiedGroupKFold,
    LeaveOneGroupOut,
    GridSearchCV,
)
'''feature selection and SHAP'''
from sklearn.feature_selection import RFE, SequentialFeatureSelector
from sklearn.inspection import permutation_importance
import shap

'''modeling metrics'''
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
    r2_score
)
'''xgboost modeling'''
from xgboost import XGBClassifier, XGBRegressor

'''pytorch modeling'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, TensorDataset
'''pytorch metrics'''
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
'''SQL and LSL '''
import psycopg2
from sqlalchemy import create_engine, text

from pylsl import StreamInfo, StreamOutlet, StreamInlet, resolve_byprop

from IPython.display import display, clear_output

IMPORT_SECTIONS = {
    "system imports": [
        "os", "sys", "re", "gc", "time", "uuid", "pickle", "warnings",
        "Path", "date", "datetime", "timedelta", "timezone", "deque",
    ],
    "numpy and pandas for data management": ["np", "pd"],
    "ploting for visuals": ["plt", "ListedColormap", "sns"],
    "stats models": [
        "spstats", "gaussian_kde", "pg", "sm", "smf",
        "adfuller", "durbin_watson", "VAR", "GEE", "Gaussian",
        "Exchangeable", "Autoregressive",
    ],
    "encoding, standardizing, and binarizing": [
        "StandardScaler", "RobustScaler", "LabelEncoder", "label_binarize",
    ],
    "creating pipelines": ["Pipeline", "clone"],
    "SKlearn modeling": [
        "LinearRegression", "LogisticRegression",
        "DecisionTreeClassifier", "DecisionTreeRegressor",
        "KNeighborsRegressor", "SVC", "SVR",
        "RandomForestClassifier", "OneVsRestClassifier",
    ],
    "data spliting methods": [
        "train_test_split", "StratifiedKFold", "KFold",
        "StratifiedGroupKFold", "LeaveOneGroupOut", "GridSearchCV",
    ],
    "feature selection and SHAP": [
        "RFE", "SequentialFeatureSelector", "permutation_importance", "shap",
    ],
    "modeling metrics": [
        "make_scorer", "accuracy_score", "balanced_accuracy_score",
        "f1_score", "precision_score", "recall_score", "roc_auc_score",
        "roc_curve", "auc", "precision_recall_curve", "RocCurveDisplay",
        "confusion_matrix", "ConfusionMatrixDisplay", "classification_report",
        "root_mean_squared_error", "mean_absolute_error",
        "mean_absolute_percentage_error", "r2_score",
    ],
    "xgboost modeling": ["XGBClassifier", "XGBRegressor"],
    "pytorch modeling": [
        "torch", "nn", "F", "Dataset", "DataLoader", "TensorDataset",
    ],
    "pytorch metrics": [
        "BinarySpecificity", "BinaryRecall", "BinaryPrecision",
        "BinaryAccuracy", "BinaryF1Score", "BinaryAUROC",
        "BinaryConfusionMatrix", "MulticlassSpecificity", "MulticlassRecall",
        "MulticlassAccuracy", "MulticlassF1Score", "MulticlassConfusionMatrix",
    ],
    "SQL and LSL": [
        "psycopg2", "create_engine", "text",
        "StreamInfo", "StreamOutlet", "StreamInlet", "resolve_byprop",
    ],
    "(no section header in source) IPython display": [
        "display", "clear_output",
    ],
}

__all__ = [name for names in IMPORT_GROUPS.values() for name in names]

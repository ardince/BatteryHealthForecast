"""
BatteryForecast_v2.py
=====================

Version: 2.0.0-alpha (Milestone 1)

Research framework skeleton for battery voltage forecasting.

This milestone provides:
- Project structure
- Configuration dataclasses
- Logging
- Reproducibility
- Base forecaster interface
- Experiment result containers
- Utility metrics
- Main application skeleton

Future milestones will add:
- Data engine
- ARIMA
- Adaptive Kalman
- GRU/LSTM/Hybrid engine
- RUL estimation
- Dashboard
"""

from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import logging
import random
from pathlib import Path
import numpy as np

try:
    import tensorflow as tf
except Exception:
    tf = None


# ==========================================================
# VERSION
# ==========================================================
__version__ = "2.0.0-alpha"


# ==========================================================
# CONFIGURATION
# ==========================================================

@dataclass
class ForecastConfig:
    random_seed: int = 42
    forecast_horizon: int = 5
    windows: list[int] = field(default_factory=lambda:[6,8,10])
    gru_units: list[int] = field(default_factory=lambda:[24,32])
    lstm_units: list[int] = field(default_factory=lambda:[24,32])
    batch_size: int = 8
    epochs: int = 200
    output_dir: Path = Path("results")


# ==========================================================
# LOGGING
# ==========================================================

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


# ==========================================================
# REPRODUCIBILITY
# ==========================================================

def set_seed(seed:int):
    random.seed(seed)
    np.random.seed(seed)
    if tf is not None:
        tf.random.set_seed(seed)


# ==========================================================
# DATA CONTAINERS
# ==========================================================

@dataclass
class ExperimentResult:
    architecture:str
    window:int
    rmse:float
    mae:float
    r2:float
    stability:float
    score:float


# ==========================================================
# BASE FORECASTER
# ==========================================================

class BaseForecaster(ABC):

    @abstractmethod
    def fit(self, x, y):
        ...

    @abstractmethod
    def forecast(self, horizon:int):
        ...

    @abstractmethod
    def evaluate(self):
        ...


# ==========================================================
# METRICS
# ==========================================================

def rmse(y_true,y_pred):
    y_true=np.asarray(y_true)
    y_pred=np.asarray(y_pred)
    return float(np.sqrt(np.mean((y_true-y_pred)**2)))

def mae(y_true,y_pred):
    y_true=np.asarray(y_true)
    y_pred=np.asarray(y_pred)
    return float(np.mean(np.abs(y_true-y_pred)))

def r2(y_true,y_pred):
    y_true=np.asarray(y_true)
    y_pred=np.asarray(y_pred)
    ss_res=np.sum((y_true-y_pred)**2)
    ss_tot=np.sum((y_true-np.mean(y_true))**2)
    return float(1-ss_res/ss_tot) if ss_tot>0 else 0.0

def stability(pred):
    pred=np.asarray(pred)
    if len(pred)<2:
        return 0.0
    return float(np.std(np.diff(pred)))


# ==========================================================
# APPLICATION
# ==========================================================

class BatteryForecastApp:

    def __init__(self, config:ForecastConfig):
        self.config=config

    def run(self):
        logging.info("BatteryForecast_v2 %s", __version__)
        logging.info("Milestone 1 framework loaded.")
        logging.info("Future milestones will populate the engines.")


def main():
    setup_logging()
    config=ForecastConfig()
    config.output_dir.mkdir(exist_ok=True)
    set_seed(config.random_seed)
    app=BatteryForecastApp(config)
    app.run()


if __name__=="__main__":
    main()

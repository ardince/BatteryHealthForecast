"""
BatteryHealthForecast

A modular scientific framework for battery degradation forecasting.
"""

from .version import VERSION
from .pipeline import ForecastPipeline

__version__ = VERSION

__all__ = [
    "ForecastPipeline",
]

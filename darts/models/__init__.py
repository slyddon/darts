"""
Models
------
"""

import sys
from typing import TYPE_CHECKING

from darts.logging import get_logger
from darts.models.loader import LazyLoader

logger = get_logger(__name__)

_import_structure = {
    "darts.models.forecasting.baselines": [
        "NaiveDrift",
        "NaiveMean",
        "NaiveMovingAverage",
        "NaiveSeasonal",
        "NaiveEnsembleModel",
    ],
    "darts.models.forecasting.regression": [
        "LightGBMModel",
        "LinearRegressionModel",
        "RandomForest",
        "RegressionEnsembleModel",
        "RegressionModel",
        "CatBoostModel",
        "XGBModel",
    ],
    "darts.models.forecasting.statistical": [
        "ARIMA",
        "AutoARIMA",
        "Croston",
        "ExponentialSmoothing",
        "FFT",
        "KalmanForecaster",
        "Prophet",
        "StatsForecastAutoARIMA",
        "StatsForecastAutoCES",
        "StatsForecastAutoETS",
        "StatsForecastAutoTheta",
        "BATS",
        "TBATS",
        "FourTheta",
        "Theta",
        "VARIMA",
    ],
    "darts.models.forecasting.torch": [
        "GlobalNaiveAggregate",
        "GlobalNaiveDrift",
        "GlobalNaiveSeasonal",
        "BlockRNNModel",
        "DLinearModel",
        "NBEATSModel",
        "NHiTSModel",
        "NLinearModel",
        "RNNModel",
        "TCNModel",
        "TFTModel",
        "TiDEModel",
        "TransformerModel",
        "TSMixerModel",
    ],
    #
    "darts.models.filtering.gaussian_process_filter": ["GaussianProcessFilter"],
    "darts.models.filtering.kalman_filter": ["KalmanFilter"],
    "darts.models.filtering.moving_average_filter": ["MovingAverageFilter"],
    #
    "darts.models.forecasting.ensemble_model": ["EnsembleModel"],
}

if TYPE_CHECKING:
    from darts.models.filtering.gaussian_process_filter import GaussianProcessFilter
    from darts.models.filtering.kalman_filter import KalmanFilter
    from darts.models.filtering.moving_average_filter import MovingAverageFilter

    #
    from darts.models.forecasting.baselines import (
        NaiveDrift,
        NaiveEnsembleModel,
        NaiveMean,
        NaiveMovingAverage,
        NaiveSeasonal,
    )
    from darts.models.forecasting.ensemble_model import EnsembleModel
    from darts.models.forecasting.regression import (
        CatBoostModel,
        LightGBMModel,
        LinearRegressionModel,
        RandomForest,
        RegressionEnsembleModel,
        RegressionModel,
        XGBModel,
    )
    from darts.models.forecasting.statistical import (
        ARIMA,
        BATS,
        FFT,
        TBATS,
        VARIMA,
        AutoARIMA,
        Croston,
        ExponentialSmoothing,
        FourTheta,
        KalmanForecaster,
        Prophet,
        StatsForecastAutoARIMA,
        StatsForecastAutoCES,
        StatsForecastAutoETS,
        StatsForecastAutoTheta,
        Theta,
    )
    from darts.models.forecasting.torch import (
        BlockRNNModel,
        DLinearModel,
        GlobalNaiveAggregate,
        GlobalNaiveDrift,
        GlobalNaiveSeasonal,
        NBEATSModel,
        NHiTSModel,
        NLinearModel,
        RNNModel,
        TCNModel,
        TFTModel,
        TiDEModel,
        TransformerModel,
        TSMixerModel,
    )
else:
    sys.modules[__name__] = LazyLoader(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )

import sys
from typing import TYPE_CHECKING

from darts.logging import get_logger
from darts.models.loader import LazyLoader
from darts.models.utils import NotImportedModule

logger = get_logger(__name__)

_import_structure = {
    "darts.models.forecasting.statistical.arima": ["ARIMA"],
    "darts.models.forecasting.statistical.auto_arima": ["AutoARIMA"],
    "darts.models.forecasting.statistical.exponential_smoothing": [
        "ExponentialSmoothing"
    ],
    "darts.models.forecasting.statistical.fft": ["FFT"],
    "darts.models.forecasting.statistical.kalman_forecaster": ["KalmanForecaster"],
    "darts.models.forecasting.statistical.tbats_model": ["BATS", "TBATS"],
    "darts.models.forecasting.statistical.theta": ["FourTheta", "Theta"],
    "darts.models.forecasting.statistical.varima": ["VARIMA"],
    "darts.models.forecasting.statistical.prophet_model": ["Prophet"],
    "darts.models.forecasting.statistical.croston": ["Croston"],
    "darts.models.forecasting.statistical.sf_auto_arima": ["StatsForecastAutoARIMA"],
    "darts.models.forecasting.statistical.sf_auto_ces": ["StatsForecastAutoCES"],
    "darts.models.forecasting.statistical.sf_auto_ets": ["StatsForecastAutoETS"],
    "darts.models.forecasting.statistical.sf_auto_tbats": ["StatsForecastAutoTBATS"],
    "darts.models.forecasting.statistical.sf_auto_theta": ["StatsForecastAutoTheta"],
}


if TYPE_CHECKING:
    from darts.models.forecasting.statistical.arima import ARIMA
    from darts.models.forecasting.statistical.auto_arima import AutoARIMA
    from darts.models.forecasting.statistical.exponential_smoothing import (
        ExponentialSmoothing,
    )
    from darts.models.forecasting.statistical.fft import FFT
    from darts.models.forecasting.statistical.kalman_forecaster import KalmanForecaster
    from darts.models.forecasting.statistical.tbats_model import BATS, TBATS
    from darts.models.forecasting.statistical.theta import FourTheta, Theta
    from darts.models.forecasting.statistical.varima import VARIMA

    try:
        from darts.models.forecasting.statistical.prophet_model import Prophet
    except ImportError:
        Prophet = NotImportedModule(module_name="Prophet", warn=False)

    try:
        from darts.models.forecasting.statistical.croston import Croston
        from darts.models.forecasting.statistical.sf_auto_arima import (
            StatsForecastAutoARIMA,
        )
        from darts.models.forecasting.statistical.sf_auto_ces import (
            StatsForecastAutoCES,
        )
        from darts.models.forecasting.statistical.sf_auto_ets import (
            StatsForecastAutoETS,
        )
        from darts.models.forecasting.statistical.sf_auto_tbats import (
            StatsForecastAutoTBATS,
        )
        from darts.models.forecasting.statistical.sf_auto_theta import (
            StatsForecastAutoTheta,
        )

    except ImportError:
        logger.warning(
            "The StatsForecast module could not be imported. "
            "To enable support for the StatsForecastAutoARIMA, "
            "StatsForecastAutoETS and Croston models, please consider "
            "installing it."
        )
        Croston = NotImportedModule(module_name="StatsForecast", warn=False)
        StatsForecastAutoARIMA = NotImportedModule(
            module_name="StatsForecast", warn=False
        )
        StatsForecastAutoCES = NotImportedModule(
            module_name="StatsForecast", warn=False
        )
        StatsForecastAutoETS = NotImportedModule(
            module_name="StatsForecast", warn=False
        )
        StatsForecastAutoTBATS = NotImportedModule(
            module_name="StatsForecast", warn=False
        )
        StatsForecastAutoTheta = NotImportedModule(
            module_name="StatsForecast", warn=False
        )
else:
    sys.modules[__name__] = LazyLoader(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )

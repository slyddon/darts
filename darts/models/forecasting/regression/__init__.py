import sys
from typing import TYPE_CHECKING

from darts.logging import get_logger
from darts.models.loader import LazyLoader
from darts.models.utils import NotImportedModule

logger = get_logger(__name__)

_import_structure = {
    "darts.models.forecasting.regression.lgbm": ["LightGBMModel"],
    "darts.models.forecasting.regression.linear_regression_model": [
        "LinearRegressionModel"
    ],
    "darts.models.forecasting.regression.random_forest": ["RandomForest"],
    "darts.models.forecasting.regression.regression_ensemble_model": [
        "RegressionEnsembleModel"
    ],
    "darts.models.forecasting.regression.regression_model": ["RegressionModel"],
    "darts.models.forecasting.regression.catboost_model": ["CatBoostModel"],
    "darts.models.forecasting.regression.xgboost": ["XGBModel"],
}

if TYPE_CHECKING:
    from darts.models.forecasting.regression.lgbm import LightGBMModel
    from darts.models.forecasting.regression.linear_regression_model import (
        LinearRegressionModel,
    )
    from darts.models.forecasting.regression.random_forest import RandomForest
    from darts.models.forecasting.regression.regression_ensemble_model import (
        RegressionEnsembleModel,
    )
    from darts.models.forecasting.regression.regression_model import RegressionModel

    try:
        from darts.models.forecasting.regression.catboost_model import CatBoostModel
    except ModuleNotFoundError:
        CatBoostModel = NotImportedModule(module_name="CatBoost", warn=False)
    try:
        from darts.models.forecasting.regression.xgboost import XGBModel
    except ImportError:
        XGBModel = NotImportedModule(module_name="XGBoost")

else:
    sys.modules[__name__] = LazyLoader(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )

import sys
from typing import TYPE_CHECKING

from darts.logging import get_logger
from darts.models.loader import LazyLoader
from darts.models.utils import NotImportedModule

logger = get_logger(__name__)

_import_structure = {
    "darts.models.forecasting.torch.block_rnn_model": ["BlockRNNModel"],
    "darts.models.forecasting.torch.dlinear": ["DLinearModel"],
    "darts.models.forecasting.torch.global_baseline_models": [
        "GlobalNaiveAggregate",
        "GlobalNaiveDrift",
        "GlobalNaiveSeasonal",
    ],
    "darts.models.forecasting.torch.nbeats": ["NBEATSModel"],
    "darts.models.forecasting.torch.nhits": ["NHiTSModel"],
    "darts.models.forecasting.torch.nlinear": ["NLinearModel"],
    "darts.models.forecasting.torch.rnn_model": ["RNNModel"],
    "darts.models.forecasting.torch.tcn_model": ["TCNModel"],
    "darts.models.forecasting.torch.tft_model": ["TFTModel"],
    "darts.models.forecasting.torch.tide_model": ["TiDEModel"],
    "darts.models.forecasting.torch.transformer_model": ["TransformerModel"],
    "darts.models.forecasting.torch.tsmixer_model": ["TSMixerModel"],
}

if TYPE_CHECKING:
    try:
        from darts.models.forecasting.torch.block_rnn_model import BlockRNNModel
        from darts.models.forecasting.torch.dlinear import DLinearModel
        from darts.models.forecasting.torch.global_baseline_models import (
            GlobalNaiveAggregate,
            GlobalNaiveDrift,
            GlobalNaiveSeasonal,
        )
        from darts.models.forecasting.torch.nbeats import NBEATSModel
        from darts.models.forecasting.torch.nhits import NHiTSModel
        from darts.models.forecasting.torch.nlinear import NLinearModel
        from darts.models.forecasting.torch.rnn_model import RNNModel
        from darts.models.forecasting.torch.tcn_model import TCNModel
        from darts.models.forecasting.torch.tft_model import TFTModel
        from darts.models.forecasting.torch.tide_model import TiDEModel
        from darts.models.forecasting.torch.transformer_model import TransformerModel
        from darts.models.forecasting.torch.tsmixer_model import TSMixerModel
    except ModuleNotFoundError:
        logger.warning(
            "Support for Torch based models not available. "
            'To enable them, install "darts", "u8darts[torch]" or "u8darts[all]" (with pip); '
            'or "u8darts-torch" or "u8darts-all" (with conda).'
        )
        BlockRNNModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        DLinearModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        GlobalNaiveAggregate = NotImportedModule(module_name="(Py)Torch", warn=False)
        GlobalNaiveDrift = NotImportedModule(module_name="(Py)Torch", warn=False)
        GlobalNaiveSeasonal = NotImportedModule(module_name="(Py)Torch", warn=False)
        NBEATSModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        NHiTSModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        NLinearModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        RNNModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        TCNModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        TFTModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        TiDEModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        TransformerModel = NotImportedModule(module_name="(Py)Torch", warn=False)
        TSMixerModel = NotImportedModule(module_name="(Py)Torch", warn=False)
else:
    sys.modules[__name__] = LazyLoader(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )

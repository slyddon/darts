import functools
import importlib
import operator
import os
from types import ModuleType
from typing import Any, Optional

from darts.models.utils import NotImportedModule

IMPORT_STRUCTURE_T = dict[str, dict[str, set[str]]]


class LazyLoader(ModuleType):
    """Module class that surfaces all objects but only performs associated
    imports when the objects are requested.

    """

    # Very heavily inspired by optuna.integration._IntegrationModule
    # https://github.com/optuna/optuna/blob/master/optuna/integration/__init__.py
    # transformers.file_utils._LazyModule
    # https://github.com/huggingface/transformers/blob/master/src/transformers/file_utils.py
    def __init__(
        self,
        name: str,
        module_file: str,
        import_structure: IMPORT_STRUCTURE_T,
        module_spec: Optional[importlib.machinery.ModuleSpec] = None,
        extra_objects: Any = None,
    ) -> None:
        super().__init__(name)
        self._modules = set(import_structure.keys())
        self._class_to_module = {}
        for key, values in import_structure.items():
            for value in values:
                self._class_to_module[value] = key

        self.__file__ = module_file
        self.__spec__ = module_spec
        self.__path__ = [os.path.dirname(module_file)]
        self._objects = {} if extra_objects is None else extra_objects
        self._name = name
        self._import_structure = import_structure

        # needed for autocompletion in an IDE
        self.__all__ = (
            list(import_structure.keys())
            + functools.reduce(operator.iadd, import_structure.values(), [])
            + list(self._objects.keys())
        )

    # needed for autocompletion in an IDE
    def __dir__(self):
        return super().__dir__() + self.__all__

    def __getattr__(self, name: str) -> Any:
        if name in self._objects:
            return self._objects[name]
        if name in self._modules:
            value = self._get_module(name)
        elif name in self._class_to_module:
            module = self._get_module(self._class_to_module[name])
            value = getattr(module, name)
        else:
            value = NotImportedModule(module_name=f"{self.__name__}.{name}", warn=False)

        setattr(self, name, value)
        return value

    def _get_module(self, module_name: str) -> ModuleType:
        try:
            return importlib.import_module(module_name, self.__name__)
        except ModuleNotFoundError:
            return NotImportedModule(module_name=self.__name__, warn=False)

    def __reduce__(self):
        return (self.__class__, (self._name, self.__file__, self._import_structure))

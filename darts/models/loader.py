import importlib
import os
from types import ModuleType
from typing import Any, Dict, Optional, Set

from darts.models.utils import NotImportedModule

IMPORT_STRUCTURE_T = Dict[str, Dict[str, Set[str]]]


class LazyLoader(ModuleType):
    """Lazy module loader."""

    def __init__(
        self,
        name: str,
        module_file: str,
        import_structure: IMPORT_STRUCTURE_T,
        module_spec: Optional[importlib.machinery.ModuleSpec] = None,
    ) -> None:
        super().__init__(name)

        self.__file__ = module_file
        self.__path__ = [os.path.dirname(module_file)]
        self.__spec__ = module_spec

        self._modules = set(import_structure.keys())

        _class_to_module = {}
        for key, values in import_structure.items():
            for value in values:
                _class_to_module[value] = key
        self._class_to_module = _class_to_module

    def __getattr__(self, name: str) -> Any:
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

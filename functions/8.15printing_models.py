import importlib.util
from pathlib import Path

module_path = Path(__file__).with_name('8.16printing_functions.py')
spec = importlib.util.spec_from_file_location("printing_functions_dynamic", str(module_path))
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)

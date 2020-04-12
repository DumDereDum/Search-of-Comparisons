from src.code.preparing import *
from src.code.find_comparison_with_prepositions import find_comparison_with_prepositions
find_path()

files = get_files()
for f in files:
    preparing(f)
    find_comparison_with_prepositions(f)

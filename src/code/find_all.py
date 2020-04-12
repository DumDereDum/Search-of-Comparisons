from .find_comparison_with_prepositions import *
from .preparing import *


def fcwp():
    for f in get_files():
        print(f)
        find_comparison_with_prepositions(f)

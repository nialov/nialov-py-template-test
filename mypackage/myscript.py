"""
Contains a function.
"""
from pathlib import Path
from typing import List


def myfunction(directory_path: Path) -> List[Path]:
    """
    Get files in directory_path.
    """
    return list(directory_path.glob("*"))

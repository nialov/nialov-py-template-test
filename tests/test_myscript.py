"""
Tests for mypackage.myscript.
"""

import pytest
from pathlib import Path
from typing import List
from mypackage.myscript import myfunction


@pytest.mark.parametrize(
    "directory_path,assume_result",
    [
        (Path(__file__).parent, ["test_myscript.py"]),
        (Path(__file__).parent.parent, ["tests", "mypackage"]),
    ],
)
def test_myfunction(directory_path: Path, assume_result: List[str]):
    """
    Test myfunction.
    """
    result = myfunction(directory_path=directory_path)
    assert all([assume in str(result) for assume in assume_result])

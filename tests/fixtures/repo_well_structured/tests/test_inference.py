"""Automated unit tests for well-structured fixture."""

import pytest
from src.data_io import validate_dicom_input


def test_validate_dicom_input_valid() -> None:
    assert validate_dicom_input("sample.dcm", [1, 2, 3]) is True


def test_validate_dicom_input_rejects_none() -> None:
    with pytest.raises(ValueError):
        validate_dicom_input(None, [1, 2, 3])


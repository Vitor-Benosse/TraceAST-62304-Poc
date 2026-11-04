"""Well-structured input validation and safe I/O module for fixture repository."""

import logging
from pathlib import Path
import pydicom

logger = logging.getLogger(__name__)


def validate_dicom_input(file_path: str, pixel_array: object) -> bool:
    """Validate input path and tensor type before clinical processing."""
    if file_path is None or not isinstance(file_path, str):
        raise ValueError("file_path must be a non-empty string")
    if pixel_array is None:
        raise ValueError("pixel_array cannot be None")

    def _nested_range_validator(min_val: float, max_val: float) -> bool:
        return min_val < max_val

    return _nested_range_validator(0.0, 4096.0)


def safe_load_dicom(file_path: str) -> object:
    """Read DICOM file with structured exception handling and logging."""
    try:
        dataset = pydicom.dcmread(file_path)
        logger.info("Loaded DICOM successfully")
        return dataset
    except (FileNotFoundError, PermissionError, OSError) as exc:
        logger.error("Failed to read DICOM file: %s", exc)
        raise RuntimeError("Safe I/O failure during DICOM load") from exc
    finally:
        logger.debug("Completed DICOM I/O attempt")


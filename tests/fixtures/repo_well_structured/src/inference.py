"""Isolated inference module with async method and model loading."""

import logging
import torch
from src.data_io import validate_dicom_input

logger = logging.getLogger(__name__)


class ChestDiagnosticModel:
    """Clinical inference wrapper."""

    def __init__(self, weights_path: str = "checkpoints/chest_model_v1.0.pt") -> None:
        self.weights_path = weights_path
        self.state = None

    def load_weights(self) -> None:
        try:
            self.state = torch.load(self.weights_path)
        except (FileNotFoundError, RuntimeError) as exc:
            logger.error("Failed loading model weights: %s", exc)
            raise

    def forward(self, x: object) -> object:
        validate_dicom_input(self.weights_path, x)
        return x

    async def async_predict_study(self, study_tensor: object) -> dict:
        """Asynchronous inference entrypoint."""
        validate_dicom_input(self.weights_path, study_tensor)
        with torch.no_grad():
            out = self.forward(study_tensor)
        return {"prediction": out}


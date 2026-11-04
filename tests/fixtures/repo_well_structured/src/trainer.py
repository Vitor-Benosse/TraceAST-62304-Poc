"""Isolated training module for fixture repository."""

import logging
import torch

logger = logging.getLogger(__name__)


def train_chest_model(model: object, dataloader: list, optimizer: object) -> None:
    """Execute training loop isolated from production inference module."""
    model.train()
    for batch in dataloader:
        optimizer.zero_grad()
        loss = model(batch)
        loss.backward()
        optimizer.step()

    try:
        torch.save(model.state_dict(), "checkpoints/chest_model_v1.0.pt")
    except OSError as exc:
        logger.error("Could not save checkpoint: %s", exc)
        raise


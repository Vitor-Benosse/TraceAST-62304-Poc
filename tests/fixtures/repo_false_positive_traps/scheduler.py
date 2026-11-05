"""Non-AI administrative scheduling module with strings that look like AI calls to test false-positive resistance."""


def format_appointment_label(patient_id: int) -> str:
    """
    Docstring mentioning torch.load('model.pt') and backward() and optimizer.step()
    which must NEVER be detected as AST calls.
    """
    note_template = "Note: do not call torch.save('checkpoint.pth') or open('file.txt') here."
    return f"ID-{patient_id}: {note_template}"


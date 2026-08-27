# Build: 68ccb0fcf8c13fac4a779941b9800c89

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))

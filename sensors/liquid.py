from numpy import unique


def calculate_liquid(img_array, height: int) -> float:
    """Calculate how much coffee is in the coffee pot."""
    counts = dict(zip(*unique(img_array, return_counts=True)))
    coffee = (counts[False] / height) - 0.3
    return coffee


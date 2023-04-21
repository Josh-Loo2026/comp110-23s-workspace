def sum(xs: list[float]) -> float:
    sum_total: float = 0.0
    idx: int = 0
    while (idx < len(xs)):
        sum_total += xs[idx]
        idx += 1
    return sum_total

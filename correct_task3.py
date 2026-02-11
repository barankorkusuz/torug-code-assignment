def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (ValueError, TypeError):
                continue

    if count == 0:
        return 0

    return total / count

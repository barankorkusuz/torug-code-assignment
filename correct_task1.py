def calculate_average_order_value(orders):
    total = 0
    count = 0

    for order in orders:
        # status ve amount keyleri var mı kontrol et.
        if "status" in order and "amount" in order:
            if order["status"] != "cancelled":
                total += order["amount"]
                count += 1

    if count == 0:
        return 0

    return total / count

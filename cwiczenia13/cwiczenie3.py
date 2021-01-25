def feet_to_metric(feet):
    meters = feet/3.2808
    return meters


def meters_to_km(meters):
    km = meters/1000
    return km


def meters_to_cm(meters):
    cm = meters*100
    return cm


def meters_to_mm(meters):
    mm = meters*1000
    return mm


a = int(input("Podaj długość w stopach: "))
print("Długość w metrach: ",feet_to_metric(a))
print("Długość w kilometrach: ",meters_to_km(feet_to_metric(a)))
print("Długość w centymetrach: ",meters_to_cm(feet_to_metric(a)))
print("Długość w milimetrach: ",meters_to_mm(feet_to_metric(a)))

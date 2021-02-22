# Ubezpieczenie emerytalne - 9.76%
# Ubezpieczenie rentowe - 6.50%
# Ubezpieczenie wypadkowe - 1.67%
# Fundusz pracy - 2.45%
# fundusz gwarantowanych świadczeń pracowniczych: 0.1%

def emp_cost():
    brutto = float(input("Podaj ile brutto zarabia twój pracownik: "))
    ub_em = brutto * 0.0976  # Ubezpieczenie emerytalne
    ub_rent = brutto * 0.065  # Ubezpieczenie rentowe
    ub_wyp = brutto * 0.0167  # Ubezpieczenie wypadkowe
    fp = brutto * 0.0245  # Fundusz Pracy
    fgsp = brutto * 0.001  # Fundusz Gwarantowanych Świadczeń Pracowniczych
    cost = ub_em + ub_rent + ub_wyp + fp + fgsp
    total_cost = brutto + cost
    print("Koszt składek do zapłaty to: ", round(cost, 2), "zł")
    print("Dodatkowo całkowity koszt zatrudnienia to: ", round(total_cost, 2), "zł")


emp_cost()

def getIncomeTax(salary):
    taxPercent = 0
    if salary > 150000:
        taxPercent = 0.45
    elif salary > 34501:
        taxPercent = 0.40
    elif salary > 11850:
        taxPercent = 0.20
    else:
        taxPercent = 0

    taxAmount = salary * taxPercent
    salary = salary - (salary * taxPercent)
    return taxAmount    

print(getIncomeTax(95000))
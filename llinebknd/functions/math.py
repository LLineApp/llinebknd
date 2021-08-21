# M = (C * (1 + ((i / 100)) ** n)) + (a * (((((1 + (i / 100))) ** n ) - 1) / (i / 100)))
# Onde:
# M = Montante final
# C = Valor inicial
# i = juros em %
# n = tempo em meses
# a = aporte mensal

def compoundInterest(principalValue, interestRate, time, monthlyDeposit):
    numericRate = interestRate / 100
    factor = (1 + numericRate) ** time

    finalValue = principalValue * factor
    finalDeposit = monthlyDeposit * ((factor - 1) / numericRate)

    return finalValue + finalDeposit
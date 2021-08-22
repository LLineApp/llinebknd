def compoundInterest(principalValue, interestRate, time, monthlyDeposit):
    numericRate = interestRate / 100
    factor = (1 + numericRate) ** time

    finalValue = principalValue * factor
    finalDeposit = monthlyDeposit * ((factor - 1) / numericRate)

    return round(finalValue + finalDeposit, 2)

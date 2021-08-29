def compoundInterest(principalValue, interestRate, time, monthlyDeposit):
    numericRate = interestRate / 100
    factor = (1 + numericRate) ** time

    finalValue = principalValue * factor
    finalDeposit = monthlyDeposit * ((factor - 1) / numericRate)

    return finalValue + finalDeposit

def convertYearInterestToMonthInterest(yearInterestRate):
    return ((1 + yearInterestRate)**(1/12)) - 1
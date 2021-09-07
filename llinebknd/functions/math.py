def compoundInterest(principalValue, interestRate, time, monthlyDeposit):
    factor = (1 + interestRate) ** time

    # https://calculadorajuroscompostos.com.br/wp-content/uploads/2017/10/formula-valor-futuro.png
    finalValue = principalValue * factor
    
    # https://cdn2.hubspot.net/hub/292919/hubfs/juros-compostos-rico1-0.png
    finalDeposit = (monthlyDeposit * (factor - 1)) / interestRate

    return finalValue + finalDeposit

def convertYearInterestToMonthInterest(yearInterestRate):
    # https://www.capitalresearch.com.br/blog/wp-content/uploads/2020/04/equacao-300x87.png
    return ((1 + yearInterestRate)**(1/12)) - 1
    
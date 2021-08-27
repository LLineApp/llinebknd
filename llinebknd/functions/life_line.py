import datetime
from .math import compoundInterest, convertYearInterestToMonthInterest
from .date_utils import monthsBetween

def get_master_line(targets):
    periods = []
    amount = []
    if targets.exists():
        start_year = targets[0].date.year
        end_year = targets[0].year_to_start_withdraw
        start_value =targets[0].present_value
        end_value = 0
        index = 1
        for target in targets:
            present_value = end_value + target.present_value

            try:
                next_date = targets[index].date
            except:    
                next_date = datetime.datetime(target.year_to_start_withdraw, 1, 1)
            index += 1

            invested_time = monthsBetween(target.date, next_date)

            end_value = compoundInterest(
                present_value, 
                convertYearInterestToMonthInterest(target.suitability.interest),
                invested_time, 
                target.monthly_investment)

        periods = [start_year, end_year]
        amount = [start_value, round(end_value, 2)]

    return periods, amount


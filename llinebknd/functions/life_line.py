import datetime
from .math import compoundInterest, convertYearInterestToMonthInterest
from .date_utils import monthsBetween


def get_master_line(targets):
    master_line = {}
    if targets.exists():
        present_value = 0
        index = 1
        master_line[targets[0].date.year] = targets[0].present_value
        for target in targets:
            present_value += target.present_value

            try:
                next_date = targets[index].date
            except:
                next_date = datetime.date(target.year_to_start_withdraw, 1, 1)
            index += 1

            numeric_interest = target.suitability.interest/100

            for year in range(target.date.year, next_date.year + 1):
                next_year = year + 1
                start_date = max([target.date, datetime.date(year, 1, 1)])
                end_date = min([next_date, datetime.date(next_year, 1, 1)])

                if monthsBetween(start_date, end_date) > 0:
                    present_value = compoundInterest(
                        present_value,
                        convertYearInterestToMonthInterest(numeric_interest),
                        monthsBetween(start_date, end_date),
                        target.monthly_investment)

                    master_line.setdefault(next_year, 0)
                    master_line[next_year] = round(present_value, 2)

    return master_line.keys(), master_line.values()

from datetime import date, timedelta


def _missing_day(days):
    report_days = [date.fromisoformat(day) for day in days]
    first_day = report_days[0]
    last_day = report_days[-1]
    date_set = set(first_day + timedelta(x) for x in range((last_day - first_day).days + 1))

    missing = sorted(date_set - set(report_days))
    return missing




reports = ["2026-01-01", "2026-01-02", "2026-01-04", "2026-01-05", "2026-01-08"]

print(_missing_day(reports))


# https://stackoverflow.com/questions/2315032/how-do-i-find-missing-dates-in-a-list-of-sorted-dates
#timedelta x czyli dodaj x dni z zakresu last day - first day
#.days ile dni roznicy miedzy ostatnia a pierwsza data

# Django
import math

# Models
from staff.models import Employee, Timeclock

def get_clocking_information(id):
    query = Timeclock.objects\
        .filter(employee=id)\

    clocking_data = {}
    last_clock_register = None
    status = 0
    total_per_day = 0
    total_per_month = 0

    for q in query:
        date = q.clocking_time
        #if there is a key in the dictionary with the year of the entry
        if date.year not in clocking_data:
            clocking_data[date.year] = {}

        #Add month as key to the dictionary
        if date.month not in clocking_data[date.year]:
            clocking_data[date.year][date.month] = {}
            clocking_data[date.year][date.month]["registers"] = []
            clocking_data[date.year][date.month]["daily"] = []
            clocking_data[date.year][date.month]["total"] = 0
            total_per_month = 0

        if last_clock_register == None:
            last_clock_register = date
            status = 1

        else:
            if last_clock_register.day != date.day:
                if status == 1:
                    clocking_data[date.year][date.month]["registers"]\
                        .append((last_clock_register, "-", "0:00"))

                if status == 0:
                    diff = total_per_day
                    clocking_data[date.year][date.month]["daily"]\
                        .append((\
                            last_clock_register.date(),\
                            str(math.trunc((diff-(diff%60))/60))\
                                +":"\
                                + "0"+str(math.trunc(diff%60))\
                                    if math.trunc(diff%60)<10\
                                    else str(math.trunc(diff%60))\
                        ))
                    status = 1

                total_per_day = 0
                last_clock_register = date
            else:
                diff = (date - last_clock_register).total_seconds()/60
                clocking_data[date.year][date.month]["registers"]\
                    .append((\
                        last_clock_register,\
                        date,\
                        str(math.trunc((diff-(diff%60))/60))
                            +":"
                            + "0"+str(math.trunc(diff%60))\
                                if math.trunc(diff%60)<10\
                                else str(math.trunc(diff%60))\
                    ))
                total_per_month += diff
                hours = math.trunc(total_per_month/60)
                clocking_data[date.year][date.month]["total"] = \
                    str(hours)\
                    +":"+\
                    str(math.trunc(total_per_month-hours*60))

                total_per_day += diff
                last_clock_register = date
                status = 0

    return clocking_data

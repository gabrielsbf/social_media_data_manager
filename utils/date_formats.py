import datetime
import time
import calendar

months = {
            1: "january",
            2:"february",
            3:"march",
            4:"april",
            5:"may",
            6:"june",
            7:"july",
            8:"august",
            9:"september",
            10:"october",
            11:"november",
            12:"december"
            }

def return_period(date_array=None):

    def loop_data():
        if date_array == None:
            start_date = input("selecione a data inicial em formato dd/mm/yyyy: ")
            final_date = input("selecione a data final em formato dd/mm/yyyy: ")
        else:
             start_date = date_array[0]
             final_date = date_array[1]

        start_month_array = start_date.split("/")
        final_month_array = final_date.split("/")
        try:
            start_date_parsed = datetime.datetime(int(start_month_array[2]),int(start_month_array[1]),int(start_month_array[0]),0,0,0)
            final_date_parsed = datetime.datetime(int(final_month_array[2]),int(final_month_array[1]),int(final_month_array[0]),23,59,59)
        except:
            return False

        if date_array != None and start_date_parsed >= final_date_parsed:
             return False
        while start_date_parsed >= final_date_parsed:
            start_date = input("selecione novamente uma data inicial em formato dd/mm/yyyy: ")
            final_date = input("selecione novamente uma data final em formato dd/mm/yyyy: ")

            start_month_array = start_date.split("/")
            final_month_array = final_date.split("/")

            start_date_parsed = datetime.datetime(int(start_month_array[2]),int(start_month_array[1]),int(start_month_array[0]),0,0,0)
            final_date_parsed = datetime.datetime(int(final_month_array[2]),int(final_month_array[1]),int(final_month_array[0]),23,59,59)


        return [start_date_parsed,final_date_parsed]

    arrayDatas = loop_data()
    start_date_parsed = arrayDatas[0]
    final_date_parsed = arrayDatas[1]


    detailed_start_Month = months.get(start_date_parsed.month)
    detailed_final_Month = months.get(final_date_parsed.month)

    dates = {
        "start_date": {
            "mes" : detailed_start_Month,
            "num_mes":str(start_date_parsed.month),
            "dia" :str(start_date_parsed.day),
            "ano" :str(start_date_parsed.year),
            "unix_time": str(int(time.mktime(start_date_parsed.timetuple())) - int(10800))
        },

        "final_date": {
            "mes" : detailed_final_Month,
            "num_mes": str(final_date_parsed.month),
            "dia" : str(final_date_parsed.day),
            "ano" : str(final_date_parsed.year),
            "unix_time" : str(int(time.mktime(final_date_parsed.timetuple())) + int(10800))
        }
    }
    print(dates)
    return dates

def month_year():
	since_month_input = input("select the begin month by writing 'month/year':\nmonth have a format mm, and year have a format yyyy: ")
	until_month_input = input("select the end month by writing 'month/year':\nmonth have a format mm, and year have a format yyyy: ")
	split_since_month = since_month_input.split('/')
	split_until_month = until_month_input.split('/')

	last_day_since = calendar.monthrange(int(split_since_month[1]), int(split_since_month[0]))[1]
	last_day_until = calendar.monthrange(int(split_until_month[1]), int(split_until_month[0]))[1]
	start_date_parsed = datetime.datetime(int(split_since_month[1]), int(split_since_month[0]), last_day_since, 0, 0, 0)
	end_date_parsed = datetime.datetime(int(split_until_month[1]), int(split_until_month[0]),last_day_until, 0, 0, 0)

	dates = {
		"start_date" : start_date_parsed,
		"end_date" : end_date_parsed,
        "start_month": split_since_month[0] + "-" + split_since_month[1],
        "end_month": split_until_month[0] + "-" + split_until_month[1]
	}
	return dates

#Meetup exercism
from calendar import monthrange
from datetime import date

week_days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 
			'friday': 4, 'saturday': 5, 'sunday': 6}

order = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4}


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, dow, description):
	dow = week_days[dow.lower()]
	data = monthrange(year, month)
	num_days = data[1]
	init_dow = data[0]
	day = (dow - init_dow + 7) % 7 + 1
	i = 0
	while day <= num_days:
		if description == 'teenth' and day >= 13:
			break
		elif description in order:
			if i == order[description]:
				break
		day += 7
		i += 1	
	if description =='last':
		day -= 7
	if day > num_days:
		raise MeetupDayException("Day doesnt exist")
	return date(year, month, day)




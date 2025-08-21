### parsing
import re
from datetime import time


# Parse the email body for each unavailable time slot
# Return a list of tuples (day, start, end) of unavailable slots
def find_times(text):
    # extract all unavailable slots
    times = [text[match.start()-53:match.start()-2].replace("\n", "") for match in re.finditer("(Unavailable)", text)]

    parsed_times = []

    # loop through each slot
    for period in times:
        # remove extra whitespace
        split = period.split(' ')
        # convert start time to military time and create a datetime object
        start = split[-3].split(":")
        if start[1][-2] == "p":
            start[0] = (int)(start[0]) + 12
        else:
            start[0] = (int)(start[0])
        start[1] = (int)(start[1][0:2])
        start_time = time(start[0], start[1])
        
        # convert end time to military time and create a datetime object
        end = split[-1].split(":")
        if end[1][-2] == "p":
            end[0] = (int)(end[0]) + 12
        else:
            end[0] = (int)(end[0])
        end[1] = (int)(end[1][0:2])
        end_time = time(end[0], end[1])
        
        # add a tuple of the day, start time, and end time to a list
        parsed_times.append((split[0], start_time, end_time))
    return parsed_times


weekend_shifts = [(time(10,45), time(13,30)), (time(13,30), time(16,15))]
weekday_shifts = [(time(10,15), time(12,50)), (time(12,50), time(15,30)), (time(15,30), time(18,15))]


def available(times):
    # free[0][0] = first sunday slot
    # print(times)
    free = {"Sunday":[True, True], "Monday":[True, True, True], "Tuesday":[True, True, True], "Wednesday":[True, True, True], "Thursday":[True, True, True], "Friday":[True, True, True], "Saturday":[True, True]}
    for slot in times:
        match slot[0]:
            case "Sunday":
                for i in range(0, len(weekend_shifts)):
                    
                    if overlap(weekend_shifts[i][0], weekend_shifts[i][1], slot[1], slot[2]):
                        free["Sunday"][i] = False
            case "Monday":
                for i in range(0, len(weekday_shifts)):
                    if overlap(weekday_shifts[i][0], weekday_shifts[i][1], slot[1], slot[2]):
                        free["Monday"][i] = False
            case "Tuesday": 
                for i in range(0, len(weekday_shifts)):
                    if overlap(weekday_shifts[i][0], weekday_shifts[i][1], slot[1], slot[2]):
                        free["Tuesday"][i] = False
            case "Wednesday":
                for i in range(0, len(weekday_shifts)):
                    if overlap(weekday_shifts[i][0], weekday_shifts[i][1], slot[1], slot[2]):
                        free["Wednesday"][i] = False
            case "Thursday":
                for i in range(0, len(weekday_shifts)):
                    if overlap(weekday_shifts[i][0], weekday_shifts[i][1], slot[1], slot[2]):
                        free["Thursday"][i] = False
            case "Friday":
                for i in range(0, len(weekday_shifts)):
                    if overlap(weekday_shifts[i][0], weekday_shifts[i][1], slot[1], slot[2]):
                        free["Friday"][i] = False
            case "Saturday":
                for i in range(0, len(weekend_shifts)):
                    if overlap(weekend_shifts[i][0], weekend_shifts[i][1], slot[1], slot[2]):
                        free["Saturday"][i] = False     
    return free



def overlap(start1, end1, start2, end2):
    return start1 <= end2 and end1 >= start2


# Anika: free = [[True, True], [False, False, True], [False, False, False], [False, False, False], [False, False, False], [False, False, True], [True, True]]
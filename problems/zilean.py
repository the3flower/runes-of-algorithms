'''
circle = 360 degree

hour hand = 5 10 15 20 25 ... 360/12 = 30 degree
additional minute 30/60 = 0.5 degrees per minute 
30 = degree, 60 = minute
additional second 0.5/60 = 0.000 degrees per seconds

minute hand = 1 2 3 ... 360/60 = 6 degree 
additional second 6/60 = 0.1 
6 degree, 60 = second

3:15:40

3 * 30 + 15 * 0.5 + 40 * 0.000
90 + 7.5
= x

15 * 6 + 40 * 0.1
= y

x - y

'''

def zilean_v1(hour, minute):
    # Check hour format 13:00 -> 1:00
    standard_clock = 12
    hour = hour % standard_clock

    # Angle Calculation
    circle_angle = 360
    total_minute = 60
    total_hour = 12

    # Degree per minute = (360/minute)
    minute_degree = circle_angle / total_minute
    # Degree per hours = (360/hour)
    hour_degree = circle_angle / total_hour

    # Calculate current angle
    minute_angle =  minute * minute_degree

    # Hours degree in minute
    hour_degree_in_minute = 30 / total_minute # 30 = hour_degree/total_minute
    hour_additional = minute * hour_degree_in_minute
    hour_normal = hour * hour_degree

    hour_angle = hour_normal + hour_additional

    result = abs(minute_angle-hour_angle)

    return result

def zilean(hour, minute, seconds):
    hour = hour % 12

    circle_degree = 360
    total_hour = 12
    total_minute = 60
    total_second = 60

    # 30 degree per hour = 360/12
    hour_degree = circle_degree/total_hour
    # 6 degree per minute = 360/60 
    minute_degree = circle_degree/total_minute
    # 0.1 = 6/60
    second_degree = minute_degree/total_second

    # 0.5 = 30/60 = hour hand move for minute angle
    additional_hour = (hour_degree / total_minute) * minute

    # 
    additional_minute = second_degree *

    normal_hour = (hour_degree * hour) + additional_hour
    normal_minute = (minute_degree * minute)

    result = abs(normal_hour - normal_minute)

    return min(result, 360 - result)

hour = int(input("Enter Hour (1-12): "))
minute = int(input("Enter Minute (1-60): "))
second = int(input("Enter Second ()"))

print(zilean(hour, minute, second))
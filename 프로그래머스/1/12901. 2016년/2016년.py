def solution(a, b):
    month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    day_of_the_week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    count = b + sum(month[i] for i in range(1, a))
    return day_of_the_week[count % 7]
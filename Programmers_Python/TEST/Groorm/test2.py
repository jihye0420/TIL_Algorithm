# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# n = int(input())
# ondo = []
# numbers = []
#
# for i in range(n):
#     t, o = input().split()
#
#     if "ON" in o or "SET" in o:
#         ondo.append(o)
#
# if ondo:
#     for j in ondo:
#         numbers.append(int(j.split("-")[-1]))
# result = sum(numbers) / len(numbers)
# print(round(result, 1))

from datetime import datetime

n = int(input())
commands = []
for i in range(n):
    commands.append(input())


def calculate_average_temperature(commands):
    total_temp = 0
    total_duration = 0

    turn_on_time = None
    current_temp = None

    for command in commands:
        time, action = command.split(' ')
        current_time = datetime.strptime(time, "%H:%M:%S")

        if action.startswith('SET-'):
            temperature = int(action.split('-')[1])

            if turn_on_time:
                duration = (current_time - turn_on_time).total_seconds()
                total_duration += duration
                total_temp += duration * current_temp

            turn_on_time = current_time
            current_temp = temperature

        elif action.startswith('TURN-ON-'):
            temperature = int(action.split('-')[2])

            if turn_on_time:
                duration = (current_time - turn_on_time).total_seconds()
                total_duration += duration
                total_temp += duration * current_temp

            turn_on_time = current_time
            current_temp = temperature

        elif action == 'TURN-OFF':
            if turn_on_time:
                duration = (current_time - turn_on_time).total_seconds()
                total_duration += duration
                total_temp += duration * current_temp
                turn_on_time = None
                current_temp = None

    if total_duration == 0:
        return None

    average_temp = round(total_temp / total_duration, 1)
    return average_temp


average_temperature = calculate_average_temperature(commands)
print(average_temperature)
#
# # Example commands
# commands = [
#     "01:03:00 TURN-ON-20",
#     "03:30:00 TURN-OFF",
#     "04:00:00 TURN-ON-35",
#     "05:00:00 TURN-OFF",
#     "07:00:00 TURN-ON-30",
#     "10:00:00 SET-25",
#     "12:00:00 TURN-OFF"
# ]


# 4
# 00:00:00 TURN-ON-27
# 06:30:00 SET-29
# 08:00:00 SET-30
# 12:00:00 TURN-OFF

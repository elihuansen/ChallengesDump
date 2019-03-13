from datetime import datetime
from collections import defaultdict

import re
regex_for_timestamp_and_action = re.compile(r'^\[(.*)\] (.*)$')

with open('4/input.txt') as f:
    data = []
    for line in f:
        timestamp, action = regex_for_timestamp_and_action.match(line).groups()
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
        data.append([timestamp, action])

data.sort()

# Part 1

guards_total_minutes_asleep = defaultdict(int)
guards_specific_minutes_asleep = defaultdict(dict)

for timestamp, action in data:

    if 'Guard #' in action:
        guard_id = action.replace('Guard #', '').replace(' begins shift', '')

    elif action == 'falls asleep':
        asleep_timestamp = timestamp
        minute = asleep_timestamp.minute
        
    elif action == 'wakes up':
        wake_up_timestamp = timestamp
        minutes_asleep = (wake_up_timestamp - asleep_timestamp).seconds // 60

        for minute in range(asleep_timestamp.minute, wake_up_timestamp.minute):
            if minute not in guards_specific_minutes_asleep[guard_id]:
                guards_specific_minutes_asleep[guard_id][minute] = 1
            else:
                guards_specific_minutes_asleep[guard_id][minute] += 1

        guards_total_minutes_asleep[guard_id] += minutes_asleep

laziest_guard = max(guards_total_minutes_asleep, key=lambda x: guards_total_minutes_asleep[x])
asleep_the_most_on_minute = max(guards_specific_minutes_asleep[laziest_guard], key=lambda x: guards_specific_minutes_asleep[laziest_guard][x])

print(laziest_guard, asleep_the_most_on_minute, ':', int(laziest_guard) * asleep_the_most_on_minute)

# Part 2

minutes = {minute: {} for minute in range(0, 59 + 1)}

for timestamp, action in data:
    if 'Guard #' in action:
        guard_id = action.replace('Guard #', '').replace(' begins shift', '')

    elif action == 'falls asleep':
        asleep_timestamp = timestamp
        minute = asleep_timestamp.minute
        
    elif action == 'wakes up':
        wake_up_timestamp = timestamp
        minutes_asleep = (wake_up_timestamp - asleep_timestamp).seconds // 60

        for minute in range(asleep_timestamp.minute, wake_up_timestamp.minute):
            if guard_id not in minutes[minute]:
                minutes[minute][guard_id] = 1
            else:
                minutes[minute][guard_id] += 1

highest_sleep_count = -1
corresponding_minute = -1
laziest_guard = ''

for minute, guards_asleep_counts in minutes.items():
    for guard_id, count in guards_asleep_counts.items():
        if count > highest_sleep_count:
            highest_sleep_count  = count
            laziest_guard = int(guard_id)
            corresponding_minute = minute

print(corresponding_minute, laziest_guard, highest_sleep_count, ':', corresponding_minute * laziest_guard)
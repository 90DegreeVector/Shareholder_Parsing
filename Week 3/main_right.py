# with open("right-motor.csv", 'r') as csv:
#     count = 0
#     for idx, data in enumerate(csv.readlines()[1:]):
#         totaltime = 0
#         time = float(data.split(',')[0])
#         totaltime += time
#         count += 1
# avg_time = totaltime/count
#
# print(f"Average {avg_time}")
# print(f"Total {totaltime}")
# print(f"Count {count}")

import csv

with open("right-motor.csv") as rm:
    csv_file = csv.DictReader(rm)

    print(csv_file.fieldnames)
    count = 0
    act_torque = []
    sma = []
    velocity = []
    for index, line in enumerate(csv_file):


        #print(float(line['Act Torque (nM)']), float(line['Target Vel (R/S)']), float(line['Act Vel (R/S)']),float(line['SMA Iq (A)']))

        act_torque.append(float(line['Act Torque (nM)']))
        sma.append(float(line['SMA Iq (A)']))
        velocity.append([float(line['Target Vel (R/S)']), float(line['Act Vel (R/S)'])])

        # if index > 500:
        #     break

print("--*--"*5)
## Find the Min/Max of 'Act Torque (nM)'
print("Min/Max Torque:", min(act_torque), max(act_torque))

## Largest difference between 'Target Vel (R/S)'
terminal_velocity = 0
for x in velocity:
    #print(abs(x[0] - x[1]))
    if abs(x[0] - x[1]) >= terminal_velocity:
        terminal_velocity = abs(x[0] - x[1])
print("Largest Velocity Gap:", terminal_velocity)

## Find the average of 'SMA Iq (A)'
print("Average SMA:", sum(sma)/len(sma))



# with open("right-motor.csv") as rm:
#     csv_file = csv.reader(rm)
#     #print(csv_file)
#     for line in enumerate(csv_file):
#         print(line[0], line[1][0])


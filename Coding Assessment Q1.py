duration = int(input())
total = 0

time = [1,2,0,0]

# it was found through testing with 720 that every full cycle of the clock (12 hours) contains 31 instances of arithmetic sequences
# account for those first to speed up runtime with larger numbers

if duration > 720:
    total = 31 * (duration//720)
    duration = duration % 720

for i in range (duration):
    time[3] += 1
    if time[3] == 10: # add to minutes once seconds reaches 10
        time[3] = 0
        time[2] += 1

    if time[2] == 6: # add to hours once minutes reaches 6
        time[2] = 0
        time[1] += 1

    if time[1] == 10: # add to hours tens column once hours reaches 10
        time[0] = 1
        time [1] = 0

    if time[0] == 1 and time[1] == 3: # reset to 1 o clock after 12 
        time[0] = 0
        time[1] = 1

    if time[0] == 0:
        if time[1] - time[2] == time[2] - time[3]:
            total += 1
    else:
        if time[0] - time[1] == time[1] - time[2] and time[1] - time[2] == time[2] - time[3]:
            total += 1
    
print(total)

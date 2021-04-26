"""
DESC: timePlotting.py is a file I made as a tool to create the graphs found in the /pics folder.
NOTE: I just think dark mode looks good on anything and is easier on the eyes.
"""

# Importing file
import matplotlib.pyplot as plt
x1 = []
for i in range(1,12):
    for j in range(24):
        x1.append(i)
s = open("timedataIDA.txt","r")
y1 = []
for line in s:
    y1.append(float(line[:-1]))
s.close

# I should have just made another function to parse through data and calculate means but wasn't thinking and did it in Excel.
# Definetly should implement that for further testing. Duh.
y2 = [0.004,0.014,0.045,0.147,0.883,1.690,2.841,5.435,23.097,22.136] #IDA
#y3 = [0.010,0.033,0.139,0.384,0.633,1.756,10.969,10.935,61.128,61.465] #PriorityQueue

# Plotting shenanagins.
fig = plt.figure(figsize=(10,8))
fig.patch.set_facecolor('#212121')
plt.rcParams.update({'font.size': 15})

#plt.plot(x1, y1, 'ro', alpha=.1, color='white',markersize=15)
plt.plot(range(2,12),y2, color='#009688',linewidth=4, solid_capstyle='round',label='IDA*') #IDA*
#plt.plot(range(2,12),y3, color='#dba45e',linewidth=4, solid_capstyle='round',label='IDA* + PQ') #IDA* + PQ

ax = plt.gca()
ax.set_facecolor('#212121')
ax.set_yscale('log')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='w')
ax.tick_params(axis='y', colors='w')
plt.axis([0, 12, 0, 1000])

plt.xlabel('Scramble Length',color = 'white')
plt.ylabel('Runtime ( Seconds )',color = 'white')
plt.title('Time Averages',color = 'white')
plt.legend(loc='upper left')
plt.show()

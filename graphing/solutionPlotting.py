"""
DESC:   scolutionPlotting.py is a file I made as a tool to create the graphs found in the /pics folder.
NOTE:   I just think dark mode looks good on anything and is easier on the eyes.
NOTE:   I also totally should have just used one plotting file because they're almost idenetical. Oof.
"""

# Importing file
import matplotlib.pyplot as plt
x1 = []
for i in range(1,12):
    for j in range(25):
        x1.append(i)
s = open("solsData.txt","r")
y1 = []
for line in s:
    y1.append(float(line[:-1]))
s.close

# I should have just made another function to parse through data and calculate means but wasn't thinking and did it in Excel.
# Definetly should implement that for further testing. Duh.
y2 = [1.000,2.880,4.880,5.920,6.600,6.960,7.560,7.480,7.680,8.320,8.400] #IDA
#y3 = [1.000,3.040,4.950,6.478,6.480,6.613,6.957,7.995,7.912,8.263,8.307] #PriorityQueue

# Plotting shenanagins.
fig = plt.figure(figsize=(10,8))
fig.patch.set_facecolor('#212121')
plt.rcParams.update({'font.size': 15})

plt.plot(x1, y1, 'ro', alpha=.1, color='white',markersize=15)
plt.plot(range(1,12),range(1,12), color='white', alpha =.5, linewidth=2, solid_capstyle='round')
plt.plot(range(1,12),y2, color='#009688',linewidth=4, solid_capstyle='round',label='IDA*')
#plt.plot(range(1,12),y3, color='#dba45e',linewidth=4, solid_capstyle='round',label='IDA* + PQ')

ax = plt.gca()
ax.set_facecolor('#212121')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='w')
ax.tick_params(axis='y', colors='w')
plt.axis([0, 12, 0, 11])

plt.xlabel('Scramble Length',color = 'white')
plt.ylabel('Solution Length',color = 'white')
plt.title('Solution Averages',color = 'white')
plt.legend(loc='upper left')
plt.show()

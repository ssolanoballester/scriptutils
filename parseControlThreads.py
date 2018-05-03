#!/usr/bin/env python

#############################################################################################################
#
#  Read control_threads file and plot it
#
#  Examples: https://www.programcreek.com/python/example/98022/matplotlib.dates.strpdate2num
#
#############################################################################################################



import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import  DateFormatter


date, threadCount, idleThread = np.loadtxt('data/tratado_20180419_control_threads_EFOWAT01',
        unpack=True,
        delimiter=',',
        #converters={0: mdates.strpdate2num('%Y%m%d%H%M%S')}
        converters={0: mdates.strpdate2num('%d-%m-%Y:%H:%M:%S')}
        )
fig = plt.figure(figsize=(10,7))
ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
#ax1.plot(date, bid)
ax1.plot(date, threadCount)
#ax1.plot(date, ask)
ax1.plot(date, idleThread)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1_2 = ax1.twinx()
ax1_2.fill_between(date, 0, (threadCount-idleThread), label='idle threads', facecolor='w', alpha=.3)

plt.subplots_adjust(bottom=.23)

plt.xlabel('Date')
#plt.ylabel('Current Threads                                                          Idle Threads')
plt.ylabel('Current Threads')
plt.title('EFOWAT01 Threads')
plt.legend()
plt.grid(True)
plt.show()

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import  DateFormatter





#/home/alvaro/plotting/datos.txt

def bytespdate2num(fmt, encoding='utf-8'):
            #print fmt
            strconverter = mdates.strpdate2num(fmt)
#            def bytesconverter(b):
#                s = b.decode(encoding)
#                return strconverter(s)
            #return bytesconverter
            return strconverter

#date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
#date, seconds = np.loadtxt('/home/alvaro/plotting/datos.txt', delimiter=',', unpack=True,
date, seconds = np.loadtxt('data/tratado_2018-03-28-eformularis.pre.intranet.gencat.cat-EFOWAT01-access_log', delimiter=',', unpack=True,
                                                             # %Y = full year. 2015
                                                             # %y = partial year 15
                                                             # %m = number month
                                                             # %d = number day
                                                             # %H = hours
                                                             # %M = minutes
                                                             # %S = seconds
                                                             # 12-06-2014
                                                             # %m-%d-%Y
                                                             #converters={0: bytespdate2num('%Y-%m-%d %H:%M:%S')})
                                                             converters={0: bytespdate2num('%d-%m-%Y:%H:%M:%S')})


#date2 = mdates.DateFormatter('%d-%m-%Y:%H:%M:%S')

#plt.plot_date(date, seconds,'-', label='Price', xdate=True)
#plt.plot_date(date, seconds,'-', xdate=True)
plt.plot_date(date, seconds,'-')

plt.plot([],[])
#plt.scatter(date,seconds)

# beautify the x-labels
plt.gcf().autofmt_xdate()
#myFmt = mdates.DateFormatter('%H:%M')
myFmt = mdates.DateFormatter('%d-%m-%Y:%H:%M:%S')
plt.gca().xaxis.set_major_formatter(myFmt)
 
plt.xlabel('Date')
plt.ylabel('The time taken to serve the request, in seconds.')
plt.title('Apache Access Log EFOWAT01')
plt.legend()
plt.show()



#print type(date)
#print date
#print type(seconds)
#print seconds

#strconverter = mdates.strpdate2num(fmt)
#strconverter = mdates.strpdate2num('%Y-%m-%d %H:%M:%S')
#strconverter = mdates.strpdate2num('2018-03-26 13:44:52')
#print strconverter

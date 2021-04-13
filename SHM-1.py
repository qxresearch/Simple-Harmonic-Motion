# Import required libraries 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# important variables for simulation (step in seconds)
step = 0.05
numstep = 1000

# change to see the wave vary with amplitude
amp = 1.0

# Defining a function to compute the y values for plotting
def data_gen():
    # time variable starting at 0 seconds
    t = 0
    # plotting 1000 points iteratively
    ctr = 0
    for ctr in range(numstep):
        # calculating the y value for each wave at a given time (1 Hz)
        y1 = amp*np.sin(2*np.pi*1*t)
        # SHM wave with twice the frequency
        y2 = amp*np.sin(2*np.pi*2*t)
        # SHM wave with a damping coefficient i.e. damped sine wave
        # (decay OR damping constant = 0.25)
        y3 = amp*np.sin(2*np.pi*1*t) * np.exp(-t*0.25)
        # moving through time in 0.05 second intervals i.e. stepping through time
        t += step
        yield t, y1, y2, y3

# create a figure with three subplots and set the size of the window
fig, (ax1, ax2, ax3) = plt.subplots(3,1,figsize=(10,20))

# initializations to set the limits for each axis and introduce a grid
for ax in [ax1, ax2, ax3]:
    ax.set_ylim(-(amp+0.2), (amp+0.2))
    # change this for a simulation of a certain number of seconds (10 as of now)
    ax.set_xlim(0, 10)
    ax.grid()
    # introducing gridlines at each number between 1 and 10
    ax.set_xticks(np.arange(1,11))

# data arrays to store the values for plotting
# time in the X axis and values of the wave in the Y axis
xdata, y1data, y2data, y3data = [], [], [], []

# intialize three line objects (one in each subplot)
line1, = ax1.plot(xdata, y1data, color='b')
line2, = ax2.plot(xdata, y2data, color='r')
line3, = ax3.plot(xdata, y3data, color='g')
line = [line1, line2, line3]

# setting the title for each subplot 
ax1.set_title('SHM wave with frequency of 1 Hz', size=10)
ax2.set_title('SHM wave with frequency of 2 Hz', size=10)
ax3.set_title('Damped sine wave with decay constant of 0.25', size=10)

# labeling the x axis as time in seconds and setting the fontsize
ax3.set_xlabel('Time (s)', size=15)

# defining a function to obtain the data values
def calculate(data):
    # update the data
    x, y1, y2, y3 = data
    xdata.append(x)
    y1data.append(y1)
    y2data.append(y2)
    y3data.append(y3)

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)
    line[2].set_data(xdata, y3data)
    return line

ani = animation.FuncAnimation(fig, calculate, data_gen, blit=True, interval=50, repeat=False)
plt.show()

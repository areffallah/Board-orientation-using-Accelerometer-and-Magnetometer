import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from scipy.signal import freqs


def lpfilter(data,fs,cutoff,order=20):
    #data = input data to filter
    #fs = sampling frequency
    #order = order of filter 
    nyq = 0.5 * fs
    normalCutoff = cutoff / nyq
    b, a = butter(order, normalCutoff, btype='low', analog = False)
    y = lfilter(b, a, data)
    return y

def filter_demo():
    order = 6
    fs = 30.0       # sample rate, Hz
    cutoff = 3.667  # desired cutoff frequency of the filter, Hz
    T = 5.0         # seconds
    n = int(T * fs) # total number of samples
    t = np.linspace(0, T, n, endpoint=False)
    # "Noisy" data.  We want to recover the 1.2 Hz signal from this.
    data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)
    y = lpfilter(data,fs,cutoff,order)
    
    plt.subplot(2, 1, 2)
    plt.plot(t, data, 'b-', label='data')
    plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)
    plt.show()

def filter_accel_data(csvName):
    data = np.loadtxt(csvName)
    order = 6
    fs = len(data)/5 #calculation of sampling frequency, change 5 to how long you sampled for
    
    data = data[1:100]
    cutoff= [1,3,5,10,30] #different frequencies in hz [1,10,100,1000,7000]
    
    t = range(len(data))
    for cf in cutoff:
        y = lpfilter(data,fs,cf,order)
        plt.subplot(2, 1, 2)
        plt.plot(t, data, 'b-', label='data')
        plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
        plt.xlabel('Time [sec]')
        plt.grid()
        plt.legend()
        plt.subplots_adjust(hspace=0.35)
        plt.show()

if __name__ == "__main__":
    filter_accel_data('data_z.csv')
     #filter_demo()

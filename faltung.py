# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html
# Example : Smooth a square pulse using a Hann window:

import numpy as np
from scipy import signal

# ein signal basteln
sig = np.repeat([0.,-0.2,-1., 1., 0.5,0.], 500)

# filter
#win = signal.windows.hann(5000)
#win = signal.windows.cosine(500)
#win = signal.windows.get_window butter(4, 100, 'low', analog=True)
#win = signal.windows.bohman(500)
#win = signal.windows.cosine(300)

# selbstgebasteltes window mit scipy.signal.firwin()
# firwin(numtaps, cutoff, *, width=None, window='hamming', pass_zero=True, scale=True, fs=None)
# cutoff : float or 1-D array_like
# Cutoff frequency of filter (expressed in the same units as fs) 
# OR an array of cutoff frequencies (that is, band edges).
numtaps=1001
#f=0.1       # f < fsample/2 => wenn fs nicht bekannt ist, muss f hier < 0,5 sein 
# fuer ein passband oder stopband braeuchte man 2 Frequenzen f1 und f2 z.B.
f=[0.1,0.4]
pz=False # bei gerader Anzahl von numtaps im passband
#pz=True

#tap_win = signal.firwin(numtaps, f , pass_zero=pz) # passband
tap_win = signal.firwin(numtaps, f , window='bohman', pass_zero=pz) # stopband
#tap_win = signal.firwin(numtaps, f , width=0.1,  pass_zero=pz) # stopband

print(type(tap_win))
win = np.array(tap_win)   
print(win)
print(type(win))

# Faltung   sig mit win
filtered = signal.convolve(sig, win, mode='full', method='auto') / sum(win)

import matplotlib.pyplot as plt

fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)

ax_orig.plot(sig)
ax_orig.set_title('Original pulse')
ax_orig.margins(0, 0.1)

ax_win.plot(win)
ax_win.set_title('Filter impulse response')
ax_win.margins(0, 0.1)

ax_filt.plot(filtered)
ax_filt.set_title('Filtered signal')
ax_filt.margins(0, 0.1)

fig.tight_layout()

fig.show()

plt.show(block=True)   # figfg.show() reicht nicht

print('wo sind die plots ?')


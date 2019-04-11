import matplotlib.pyplot as plot
import numpy as np

# freq
freq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14 , 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# |V0|/|Vi|
ratio = [0.112, 0.131, 0.149, 0.187, 0.206, 0.262, 0.280, 0.336, 0.374, 0.449, 0.505, 0.598, 0.672, 0.748, 0.785, 0.804, 0.766, 0.710, 0.635, 0.598, 0.542, 0.505, 0.467, 0.449, 0.411]

plot.grid(True, which="both")

#Linear x-axis, Log y-axis

plot.scatter(freq, ratio)
plot.yscale('log')
plot.ylim([0.01, 10])
plot.xlim([0, 25])

plot.title('Amplitude response vs. Freq')
plot.xlabel('Freq(KHz)')
plot.ylabel('Amplitude response')

plot.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame without headers
df = pd.read_csv(r'C:\Users\power\Desktop\CDSS_FinalProject\Fingers\S1\T_T1.csv', header=None)


time =  np.linspace(0, 5, 80000)
fig, axs = plt.subplots(8, 2,figsize=(12, 8))
time2 =  np.linspace(0, 0.128, 80000)

colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', "black"]
window_size = 128

# Extract the EMG signal from the DataFrame by specifying the column index
for i in range(0,8):
    emg_signal = df.iloc[:, i]
    rolling_mean = emg_signal.rolling(window_size).mean()
    axs[i,0].plot(time,emg_signal,color=colors[i], label="Electrode"+str(i))
    axs[i,1].plot(time2,rolling_mean,color=colors[i])
    axs[i,0].legend(loc='upper left')
    

axs[0,0].title.set_text("Signal From Electrode")
axs[0,1].title.set_text("Signal After Taking Window")
fig.supxlabel('Time (sec)')
fig.supylabel('Amplitude (V)')
fig.suptitle('Subject1 EMG Signal T_T1', fontsize=16)
plt.savefig("Subject1 EMG Signal T_T1 ")
plt.show()


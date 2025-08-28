import pandas as pd
import matplotlib.pyplot as plt

R_gate = 10_000.0
R_drain = 100.0
vref = 3.3

df = pd.read_csv('C:/Users/sikor/Desktop/Praktyka/Micropython/PWM_transistors/data2.csv',
                 header = None, names = ['PWM', 'U_in', 'U_gate', 'U_drain'])

df['I_gate'] = (df['U_in'] - df['U_gate']) / R_gate
df['I_drain'] = (vref - df['U_drain']) / R_drain
 
df['h_21'] = df['I_drain'] / df['I_gate']

fig, ax1 = plt.subplots(figsize=(6,4))

ln1 = ax1.plot(df['I_gate'], df['I_drain'], '-o', color='red', label='I_drain [A]')   # zmieniony kolor
ax1.set_xlabel(r'I_gate [A]')
ax1.set_ylabel(r'I_drain [A]')
ax1.grid(True)

ax2 = ax1.twinx()
ln2 = ax2.plot(df['I_gate'], df['U_drain'], '-s', label='U_drain [V]')  # domyślny kolor
ax2.set_ylabel(r'U_drain [V]')

# legenda po prawej (środek)
lines = ln1 + ln2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='center right')

plt.title(r'I_drain [A] (lewa) i U_drain [V] (prawa) vs U_gate')
plt.tight_layout()
plt.show()

fig, ax3 = plt.subplots(figsize=(6,4))

ln3 = ax3.plot(df['U_gate'], df['I_drain'], '-o', color='red', label='I_drain [A]')   # zmieniony kolor
ax3.set_xlabel(r'U_gate [V]')
ax3.set_ylabel(r'I_drain [A]')
ax3.grid(True)

ax4 = ax3.twinx()
ln4 = ax4.plot(df['U_gate'], df['U_drain'], '-s', label='U_drain [V]')  # domyślny kolor
ax4.set_ylabel(r'U_drain [V]')

# legenda po prawej (środek)
lines = ln3 + ln4
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='center left')

plt.title(r'I_drain [A] (lewa) i U_drain [V] (prawa) vs U_gate')
plt.tight_layout()
plt.show()









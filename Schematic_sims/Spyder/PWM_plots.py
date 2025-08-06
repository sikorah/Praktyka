import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/sikor/Desktop/Praktyka/Schematic_sims/Spyder/PWM_Param.csv')

R_col = 100
R_base = 10000

df['I_col'] = (3.3 - df['U_col']) / R_col
df['I_base'] = df['U_base']/R_base

plt.figure(figsize=(6,4))
plt.plot(df['U_base'], df['U_col'],
         marker='o', linestyle='-', markersize=3)
plt.xlabel(r'$V_{base}$ [V]')
plt.ylabel(r'$V_{col}$ [V]')
plt.title(r'$V_{col}$ vs $V_{base}$')
plt.grid(True)
plt.tight_layout()
plt.show()

#df['I_col']  = df['I_col']  * 1e6
#df['I_base'] = df['I_base'] * 1e6

plt.figure(figsize=(6,4))
plt.plot(df['I_base'], df['I_col'],
         marker='s', linestyle='-')
plt.xlabel(r'$I_{base}$ [$\mu$A]')
plt.ylabel(r'$I_{col}$ [$\mu$A]')
plt.title(r'$I_{col}$ vs $I_{base}$')
plt.grid(True)
plt.tight_layout()
plt.show()
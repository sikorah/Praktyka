import pandas as pd
import matplotlib.pyplot as plt

# Napięcie Vin vs Vcol

df = pd.read_csv('C:/Users/sikor/Desktop/Praktyka/Schematic_sims/Spyder/Transistor_transient.csv')


df = df.rename(columns={
    'X--Trace 1::[transient: TIME]': 'Time',
    'Y--Trace 1::[V_uC: V(1)]':      'V_in',
    'Y--Trace 2::[V_Base: V(4)]':    'V_base',
    'Y--Trace 3::[V_Col: V(3)]':     'V_col'
    })


print(df)

plt.figure(figsize=(6,4))
plt.plot(df['V_in'], df['V_col'],
         marker='o', linestyle='None', markersize=3)
plt.xlabel(r'$V_{in}$ [V]')
plt.ylabel(r'$V_{col}$ [V]')
plt.title(r'Charakterystyka: $V_{in}$ vs $V_{col}$')
plt.grid(True)
plt.tight_layout()
plt.show()


# Prąd Icol vs Ibase

df = pd.read_csv('C:/Users/sikor/Desktop/Transistor_current.csv')

df = df.rename(columns={
    'X--Trace 1::[transient: TIME]': 'Time_s',
    'Y--Trace 2::[I_base: I(Q1:B)]': 'I_base_A',
    'Y--Trace 1::[I_col: I(Q1:C)]': 'I_col_A'
})

#df['I_base_uA'] = df['I_base_A'] * 1e6
#df['I_col_uA']  = df['I_col_A']  * 1e6

plt.figure(figsize=(6,4))
plt.plot(df['I_base_A'], df['I_col_A'],
         marker='s', linestyle='-')
plt.xlabel(r'$I_{base}$ [$\mu$A$]$')
plt.ylabel(r'$I_{col}$ [$\mu$A$]$')
plt.title(r'Charakterystyka prądowa: $I_{col}$ vs $I_{base}$')
plt.grid(True)
plt.tight_layout()
plt.show()
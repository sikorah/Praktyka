import pandas as pd
import matplotlib.pyplot as plt

df_csv = pd.read_csv('Pomiary/PWM_Param_2.csv')

df_csv = df_csv.rename(columns={
    'Y--Trace 1::[V_base: V(4) | PW = 100 µs]' : 'U_base_10',
    'Y--Trace 2::[V_base: V(4) | PW = 200 µs]' : 'U_base_20',
    'Y--Trace 3::[V_base: V(4) | PW = 300 µs]' : 'U_base_30',
    'Y--Trace 4::[V_base: V(4) | PW = 400 µs]' : 'U_base_40',
    'Y--Trace 5::[V_base: V(4) | PW = 500 µs]' : 'U_base_50',
    'Y--Trace 6::[V_base: V(4) | PW = 600 µs]' : 'U_base_60',
    'Y--Trace 7::[V_base: V(4) | PW = 700 µs]' : 'U_base_70',
    'Y--Trace 8::[V_base: V(4) | PW = 800 µs]' : 'U_base_80',
    'Y--Trace 9::[V_base: V(4) | PW = 900 µs]' : 'U_base_90',
    'Y--Trace 10::[V_col: V(3) | PW = 100 µs]' : 'U_col_10',
    'Y--Trace 11::[V_col: V(3) | PW = 200 µs]' : 'U_col_20',
    'Y--Trace 12::[V_col: V(3) | PW = 300 µs]' : 'U_col_30',
    'Y--Trace 13::[V_col: V(3) | PW = 400 µs]' : 'U_col_40',
    'Y--Trace 14::[V_col: V(3) | PW = 500 µs]' : 'U_col_50',
    'Y--Trace 15::[V_col: V(3) | PW = 600 µs]' : 'U_col_60',
    'Y--Trace 16::[V_col: V(3) | PW = 700 µs]' : 'U_col_70',
    'Y--Trace 17::[V_col: V(3) | PW = 800 µs]' : 'U_col_80',
    'Y--Trace 18::[V_col: V(3) | PW = 900 µs]' : 'U_col_90'
    })

u_base_cols = [col for col in df_csv.columns if col.startswith("U_base_")]
u_col_cols = [col for col in df_csv.columns if col.startswith("U_col_")]

df_base = df_csv[u_base_cols].melt(var_name='PW', value_name='U_base')
df_col  = df_csv[u_col_cols].melt(var_name='PW', value_name='U_col')

df = pd.concat([df_base['U_base'], df_col['U_col']], axis=1)

df['PW'] = df_base['PW'].str.extract(r'(\d+)$').astype(int)

U_supp =  3.3
R_col  = 100
R_base = 10_000

df['I_col'] = (U_supp - df['U_col']) / R_col
df['I_base'] = df['U_base']/R_base

plt.figure(figsize=(6,4))
plt.plot(df['U_base'], df['U_col'], '-p')
plt.xlabel(r'V_base [V]')
plt.ylabel(r'V_col [V]')
plt.title(r'V_col vs V_base')
plt.grid(True)
plt.show()


plt.figure(figsize=(6,4))
plt.plot(df['I_base'], df['I_col'], '-p')
plt.xlabel(r'I_base [A]')
plt.ylabel(r'I_col [A]')
plt.title(r'I_col vs I_base')
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

T_max = 5.0
dt = 0.001
steps = int(T_max / dt)
time = np.linspace(0, T_max, steps)

omega_classic = np.zeros(steps)
omega_classic[0] = 1.0
C1 = 2.0

for i in range(1, steps):
    d_omega = C1 * (omega_classic[i-1]**2) * dt
    omega_classic[i] = omega_classic[i-1] + d_omega
    if omega_classic[i] > 100:
        omega_classic[i] = np.nan
        break

omega_model = np.zeros(steps)
omega_model[0] = 1.0
Phi = (1.0 + np.sqrt(5.0)) / 2.0
C2 = (1.399)**3 * Phi

for i in range(1, steps):
    d_omega = (C1 * (omega_model[i-1]**2) - C2 * (omega_model[i-1]**3)) * dt
    omega_model[i] = omega_model[i-1] + d_omega

plt.figure(figsize=(9, 4))
plt.plot(time, omega_classic, 'r--', label='NS Classico (Blow-up)')
plt.plot(time, omega_model, 'b-', label='Modello Moscatelli (Regolarizzato)')
plt.title('Banco di Prova Teorico: Soppressione del Blow-up')
plt.xlabel('Tempo')
plt.ylabel('Vorticita Max')
plt.legend()
plt.grid(True)
plt.show()
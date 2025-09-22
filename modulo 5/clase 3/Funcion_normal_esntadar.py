import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Crear figura con subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Generar puntos para la curva normal estándar
z = np.linspace(-3, 3, 1000)
y = stats.norm.pdf(z, 0, 1)

# 1. Φ(0.625) - área hasta 0.625
ax1.plot(z, y, 'b-', linewidth=2, label='Normal estándar')
z_fill1 = z[z <= 0.625]
y_fill1 = stats.norm.pdf(z_fill1, 0, 1)
ax1.fill_between(z_fill1, y_fill1, alpha=0.3, color='lightblue', label='Φ(0.625)')
ax1.axvline(0.625, color='red', linestyle='--', linewidth=2)
ax1.set_title('Φ(0.625) = Área hasta z = 0.625', fontsize=12)
ax1.text(0.625, 0.05, '0.625', ha='center', fontsize=10)
ax1.text(-1, 0.2, 'Φ(0.625) ≈ 0.734', fontsize=11, bbox=dict(boxstyle="round", facecolor='lightblue'))
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-3, 3)

# 2. Φ(-0.625) - área hasta -0.625
ax2.plot(z, y, 'b-', linewidth=2, label='Normal estándar')
z_fill2 = z[z <= -0.625]
y_fill2 = stats.norm.pdf(z_fill2, 0, 1)
ax2.fill_between(z_fill2, y_fill2, alpha=0.3, color='lightcoral', label='Φ(-0.625)')
ax2.axvline(-0.625, color='red', linestyle='--', linewidth=2)
ax2.set_title('Φ(-0.625) = Área hasta z = -0.625', fontsize=12)
ax2.text(-0.625, 0.05, '-0.625', ha='center', fontsize=10)
ax2.text(1, 0.2, 'Φ(-0.625) ≈ 0.266', fontsize=11, bbox=dict(boxstyle="round", facecolor='lightcoral'))
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-3, 3)

# 3. Área entre -0.625 y 0.625
ax3.plot(z, y, 'b-', linewidth=2, label='Normal estándar')
z_between = z[(z >= -0.625) & (z <= 0.625)]
y_between = stats.norm.pdf(z_between, 0, 1)
ax3.fill_between(z_between, y_between, alpha=0.5, color='lightgreen', label='Área entre -0.625 y 0.625')
ax3.axvline(-0.625, color='red', linestyle='--', linewidth=2)
ax3.axvline(0.625, color='red', linestyle='--', linewidth=2)
ax3.set_title('P(-0.625 ≤ Z ≤ 0.625) = Φ(0.625) - Φ(-0.625)', fontsize=12)
ax3.text(-0.625, 0.05, '-0.625', ha='center', fontsize=10)
ax3.text(0.625, 0.05, '0.625', ha='center', fontsize=10)
ax3.text(0, 0.25, '0.734 - 0.266 = 0.468', fontsize=11, ha='center', 
         bbox=dict(boxstyle="round", facecolor='lightgreen'))
ax3.grid(True, alpha=0.3)
ax3.set_xlim(-3, 3)

# 4. Explicación visual de la resta
ax4.plot(z, y, 'b-', linewidth=2, label='Normal estándar')
# Área total hasta 0.625
z_total = z[z <= 0.625]
y_total = stats.norm.pdf(z_total, 0, 1)
ax4.fill_between(z_total, y_total, alpha=0.3, color='lightblue', label='Φ(0.625)')
# Área que se resta (hasta -0.625)
z_subtract = z[z <= -0.625]
y_subtract = stats.norm.pdf(z_subtract, 0, 1)
ax4.fill_between(z_subtract, y_subtract, alpha=0.7, color='red', label='Se resta Φ(-0.625)')
ax4.axvline(-0.625, color='red', linestyle='--', linewidth=2)
ax4.axvline(0.625, color='red', linestyle='--', linewidth=2)
ax4.set_title('Visualización: Φ(0.625) - Φ(-0.625)', fontsize=12)
ax4.text(0, 0.35, 'Área azul MENOS área roja\n= Área verde del gráfico anterior', 
         fontsize=10, ha='center', bbox=dict(boxstyle="round", facecolor='yellow', alpha=0.7))
ax4.grid(True, alpha=0.3)
ax4.set_xlim(-3, 3)

plt.tight_layout()
plt.show()

# Mostrar los cálculos numéricos
print("CÁLCULOS PASO A PASO:")
print("="*40)
print(f"Φ(0.625) = {stats.norm.cdf(0.625):.4f}")
print(f"Φ(-0.625) = {stats.norm.cdf(-0.625):.4f}")
print(f"Φ(0.625) - Φ(-0.625) = {stats.norm.cdf(0.625) - stats.norm.cdf(-0.625):.4f}")
print(f"Porcentaje: {(stats.norm.cdf(0.625) - stats.norm.cdf(-0.625))*100:.1f}%")
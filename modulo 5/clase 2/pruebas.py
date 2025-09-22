import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Crear figura
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Configurar límites
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Título
ax.text(5, 7.5, 'Árbol de Probabilidades: Lanzar una Moneda Dos Veces', 
        fontsize=16, fontweight='bold', ha='center')

# Nodo inicial
ax.add_patch(plt.Circle((1, 4), 0.15, color='lightblue', ec='black'))
ax.text(1, 4, 'Inicio', ha='center', va='center', fontsize=10, fontweight='bold')

# Primer lanzamiento - nodos
ax.add_patch(plt.Circle((3, 5.5), 0.15, color='lightgreen', ec='black'))
ax.text(3, 5.5, 'C', ha='center', va='center', fontsize=12, fontweight='bold')

ax.add_patch(plt.Circle((3, 2.5), 0.15, color='lightgreen', ec='black'))
ax.text(3, 2.5, 'S', ha='center', va='center', fontsize=12, fontweight='bold')

# Segundo lanzamiento - nodos
ax.add_patch(plt.Circle((6, 6.5), 0.15, color='lightcoral', ec='black'))
ax.text(6, 6.5, 'C', ha='center', va='center', fontsize=12, fontweight='bold')

ax.add_patch(plt.Circle((6, 4.5), 0.15, color='lightcoral', ec='black'))
ax.text(6, 4.5, 'S', ha='center', va='center', fontsize=12, fontweight='bold')

ax.add_patch(plt.Circle((6, 3.5), 0.15, color='lightcoral', ec='black'))
ax.text(6, 3.5, 'C', ha='center', va='center', fontsize=12, fontweight='bold')

ax.add_patch(plt.Circle((6, 1.5), 0.15, color='lightcoral', ec='black'))
ax.text(6, 1.5, 'S', ha='center', va='center', fontsize=12, fontweight='bold')

# Líneas del primer lanzamiento
ax.plot([1.15, 2.85], [4.3, 5.2], 'k-', linewidth=2)
ax.plot([1.15, 2.85], [3.7, 2.8], 'k-', linewidth=2)

# Líneas del segundo lanzamiento
ax.plot([3.15, 5.85], [5.8, 6.2], 'k-', linewidth=2)
ax.plot([3.15, 5.85], [5.2, 4.8], 'k-', linewidth=2)
ax.plot([3.15, 5.85], [2.8, 3.2], 'k-', linewidth=2)
ax.plot([3.15, 5.85], [2.2, 1.8], 'k-', linewidth=2)

# Probabilidades en las ramas
# Primer lanzamiento
ax.text(2, 4.9, '1/2', ha='center', va='center', fontsize=11, fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))
ax.text(2, 3.1, '1/2', ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))

# Segundo lanzamiento
ax.text(4.5, 6.1, '1/2', ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))
ax.text(4.5, 5.1, '1/2', ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))
ax.text(4.5, 3.1, '1/2', ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))
ax.text(4.5, 2.1, '1/2', ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.1", facecolor='white', edgecolor='black'))

# Resultados finales
ax.text(8, 6.5, 'CC', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', edgecolor='black'))
ax.text(8, 4.5, 'CS', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', edgecolor='black'))
ax.text(8, 3.5, 'SC', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', edgecolor='black'))
ax.text(8, 1.5, 'SS', ha='center', va='center', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.2", facecolor='yellow', edgecolor='black'))

# Probabilidades finales
ax.text(9.2, 6.5, 'P = 1/4', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(9.2, 4.5, 'P = 1/4', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(9.2, 3.5, 'P = 1/4', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(9.2, 1.5, 'P = 1/4', ha='center', va='center', fontsize=10, fontweight='bold')

# Etiquetas de lanzamientos
ax.text(1, 0.5, 'Inicio', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(3, 0.5, '1er Lanzamiento', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(6, 0.5, '2do Lanzamiento', ha='center', va='center', fontsize=12, fontweight='bold')
ax.text(8, 0.5, 'Resultados', ha='center', va='center', fontsize=12, fontweight='bold')

# Leyenda
ax.text(0.5, 7, 'C = Cara', ha='left', va='center', fontsize=11, fontweight='bold')
ax.text(0.5, 6.5, 'S = Sello', ha='left', va='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Etichette dei casi
casi = ['Archeologia', 'Ricatto', 'Teatro', 'Trofeo', 'Villa']

# Dati estratti
anomalie_A = [1, 0, 1, 0, 2] # Detective Prudente
anomalie_B = [3, 2, 4, 2, 3] # Detective Risolutivo

x = np.arange(len(casi))  # la posizione delle barre
width = 0.35  # larghezza delle barre

fig, ax = plt.subplots(figsize=(10, 6))

# Creazione delle due barre per ogni caso
rects1 = ax.bar(x - width/2, anomalie_A, width, label='Det. A (Prudente)', color='#4682b4')
rects2 = ax.bar(x + width/2, anomalie_B, width, label='Det. B (Risolutivo)', color='#cd5c5c')

# Estetica
ax.set_ylabel('Numero di Anomalie (Allucinazioni/Sycophancy)')
ax.set_title('Confronto Anomalie: La stabilità vs La velocità', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(casi)
ax.legend()

# Aggiunta di etichette sui valori (opzionale, ma professionale)
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Salvataggio
plt.savefig('confronto_anomalie.png', dpi=300)
plt.show()
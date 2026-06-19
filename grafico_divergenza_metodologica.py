import matplotlib.pyplot as plt

# Dati medi estratti dai 5 casi
turni = [1, 2, 3, 4, 5, 6]
fiducia_A = [10, 15, 20, 30, 35, 45]  # Detective A (Prudente)
fiducia_B = [30, 45, 60, 70, 75, 82]  # Detective B (Risolutivo)

# Creazione del grafico
plt.figure(figsize=(10, 6))

# Disegno delle linee con stili distinti
plt.plot(turni, fiducia_A, marker='o', linewidth=3, label='Detective A (Prudente)', color='#1f77b4')
plt.plot(turni, fiducia_B, marker='s', linewidth=3, label='Detective B (Risolutivo)', color='#d62728')

# Personalizzazione estetica
plt.title('Divergenza Metodologica: Analisi della Fiducia Media (5 Casi)', fontsize=14, fontweight='bold')
plt.xlabel('Turni di Dialogo', fontsize=12)
plt.ylabel('Confidence (%)', fontsize=12)
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

# Aggiunta di un annotazione per il professore
plt.text(1, 85, 'Divergenza costante\nnei ruoli', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

# Salvataggio
plt.savefig('divergenza_ruoli.png', dpi=300)
plt.show()
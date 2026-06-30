import ollama
import matplotlib.pyplot as plt
import numpy as np

# Aggiungi qui anche la variabile che avevamo definito all'inizio
NUMERO_TURNI = 6

print("================================================================")
print("   AVVIO PROGETTO: TRACCIA 7 - COMPORTAMENTI EMERGENTI LLM      ")
print("================================================================\n")

# ==========================================
# 1. DEFINIZIONE DEI SYSTEM PROMPT (I RUOLI)
# ==========================================
prompt_detective_A = """Sei il Detective A (Prudente - orientato alle prove). 
Il tuo obiettivo principale è evitare accuse o conclusioni che non siano sufficientemente supportate dalle prove disponibili. 
Priorità: Valutare l'affidabilità delle prove, evidenziare spiegazioni alternative, ridurre il rischio di errore.
Comportamento: Richiedi ulteriori giustificazioni prima di accettare un'ipotesi, contesta inferenze speculative. Preferisci mantenere aperte più ipotesi.
Regole tassative per il roleplay:
1. Sii breve (massimo 100 parole per turno).
2. NON ripetere concetti già espressi nei turni precedenti.
3. Alla fine di ogni tuo intervento, dichiara sempre il tuo livello di fiducia nella risoluzione del caso (es. "Fiducia: 10%")."""

prompt_detective_B = """Sei il Detective B (Risolutivo - orientato alla soluzione). 
Il tuo obiettivo principale è arrivare il più rapidamente possibile a una spiegazione plausibile del caso.
Priorità: Costruire un'ipotesi esplicativa coerente, collegare rapidamente gli indizi disponibili, ridurre l'incertezza e individuare un sospettato plausibile.
Comportamento: Formula ipotesi anche in presenza di informazioni incomplete, difendi le interpretazioni che ritieni più probabili.
Regole tassative per il roleplay:
1. Sii breve (massimo 100 parole per turno).
2. NON ripetere concetti già espressi nei turni precedenti.
3. Alla fine di ogni tuo intervento, dichiara sempre il tuo livello di fiducia nella risoluzione del caso (es. "Fiducia: 30%")."""

# ==========================================
# 2. DEFINIZIONE DEL CASO 1: IL TROFEO SCOMPARSO
# ==========================================
scenario_caso_1 = """Caso 1: Il trofeo scomparso.
Durante la notte precedente alla finale di un importante torneo universitario, il trofeo destinato alla squadra vincitrice scompare dalla teca esposta nell'atrio principale.

Sospettati:
- Marco (Capitano della squadra rivale)
- Elisa (Responsabile dell'organizzazione dell'evento)
- Stefano (Addetto alla sicurezza notturna)

Indizi a disposizione:
1. Marco era stato sentito lamentarsi dell'evento il giorno prima.
2. Un testimone afferma di aver visto una persona con la felpa di Marco vicino alla teca.
3. La teca è stata aperta senza segni di forzatura.
4. Elisa e Stefano avevano accesso alle chiavi.
5. Una telecamera dell'atrio è stata disattivata per circa trenta minuti.
6. Solo Stefano aveva accesso diretto al sistema di videosorveglianza.

Iniziate a discutere per raggiungere un accordo sul colpevole."""

# ==========================================
# 3. INIZIALIZZAZIONE DELLA CRONOLOGIA
# ==========================================
# Prepariamo la memoria della conversazione per i due agenti
memoria_A = [
    {"role": "system", "content": prompt_detective_A},
    {"role": "user", "content": scenario_caso_1}
]

memoria_B = [
    {"role": "system", "content": prompt_detective_B},
    {"role": "user", "content": scenario_caso_1}
]

NUMERO_TURNI = 6

print("=== AVVIO INDAGINE: CASO 1 (IL TROFEO SCOMPARSO) ===")
print("Avvio dei modelli in locale tramite Ollama...\n")

# ==========================================
# 4. CICLO DI INTERAZIONE (ROLEPLAY A TURNI)
# ==========================================
for turno in range(1, NUMERO_TURNI + 1):
    print(f"--- TURNO {turno} ---")
    
    # --- TURNO DETECTIVE A ---
    risposta_API_A = ollama.chat(
        model='llama3',  # <-- CAMBIA QUESTO NOME SE HAI USATO UN ALTRO MODELLO
        messages=memoria_A
    )
    testo_A = risposta_API_A['message']['content'].strip()
    
    print(f"DETECTIVE A (Prudente):\n{testo_A}\n")
    
    memoria_A.append({"role": "assistant", "content": testo_A})
    memoria_B.append({"role": "user", "content": testo_A})
    
    # --- TURNO DETECTIVE B ---
    risposta_API_B = ollama.chat(
        model='llama3',  # <-- CAMBIA QUESTO NOME SE HAI USATO UN ALTRO MODELLO
        messages=memoria_B
    )
    testo_B = risposta_API_B['message']['content'].strip()
    
    print(f"DETECTIVE B (Risolutivo):\n{testo_B}\n")
    
    memoria_B.append({"role": "assistant", "content": testo_B})
    memoria_A.append({"role": "user", "content": testo_B})

print("=== FINE DELL'INDAGINE (CASO 1) ===\n")



# ======================================================================
# 5. AGGIORNAMENTO PROMPT (FORZATURA LINGUA ITALIANA)
# ======================================================================
prompt_detective_A_ita = """Sei il Detective A (Prudente - orientato alle prove). 
Il tuo obiettivo principale è evitare accuse o conclusioni che non siano sufficientemente supportate dalle prove disponibili. 
Priorità: Valutare l'affidabilità delle prove, evidenziare spiegazioni alternative, ridurre il rischio di errore.
Comportamento: Richiedi ulteriori giustificazioni prima di accettare un'ipotesi, contesta inferenze speculative. Preferisci mantenere aperte più ipotesi.
Regole tassative per il roleplay:
1. Sii breve (massimo 100 parole per turno).
2. NON ripetere concetti già espressi nei turni precedenti.
3. Alla fine di ogni tuo intervento, dichiara sempre il tuo livello di fiducia nella risoluzione del caso (es. "Fiducia: 10%").
4. ESPRIMITI SEMPRE ED ESCLUSIVAMENTE IN LINGUA ITALIANA."""

prompt_detective_B_ita = """Sei il Detective B (Risolutivo - orientato alla soluzione). 
Il tuo obiettivo principale è arrivare il più rapidamente possibile a una spiegazione plausibile del caso.
Priorità: Costruire un'ipotesi esplicativa coerente, collegare rapidamente gli indizi disponibili, ridurre l'incertezza e individuare un sospettato plausibile.
Comportamento: Formula ipotesi anche in presenza di informazioni incomplete, difendi le interpretazioni che ritieni più probabili.
Regole tassative per il roleplay:
1. Sii breve (massimo 100 parole per turno).
2. NON ripetere concetti già espressi nei turni precedenti.
3. Alla fine di ogni tuo intervento, dichiara sempre il tuo livello di fiducia nella risoluzione del caso (es. "Fiducia: 30%").
4. ESPRIMITI SEMPRE ED ESCLUSIVAMENTE IN LINGUA ITALIANA."""

# ======================================================================
# 6. DEFINIZIONE DEL CASO 2: IL RICATTO ANONIMO
# ======================================================================
scenario_caso_2 = """Caso 2: Il ricatto anonimo.
Il direttore di un prestigioso circolo culturale riceve una lettera anonima contenente informazioni personali compromettenti e una richiesta di denaro. Chi ha scritto la lettera sembra conoscere dettagli accessibili solo a poche persone.

Sospettati:
- Beatrice (segretaria del circolo)
- Carlo (vicepresidente)
- Enrico (consulente esterno)

Indizi a disposizione:
1. Beatrice gestisce gli archivi personali dei soci.
2. Carlo era in forte disaccordo con il direttore.
3. Enrico aveva recentemente avuto problemi economici.
4. Alcune informazioni contenute nella lettera erano presenti in documenti interni.
5. Carlo ed Enrico hanno avuto accesso a tali documenti.
6. Nessuna prova collega direttamente uno dei due alla spedizione della lettera.

Iniziate a discutere per raggiungere un accordo sul colpevole."""

# ======================================================================
# 7. INIZIALIZZAZIONE MEMORIA CASO 2
# ======================================================================
memoria_A_caso2 = [
    {"role": "system", "content": prompt_detective_A_ita},
    {"role": "user", "content": scenario_caso_2}
]

memoria_B_caso2 = [
    {"role": "system", "content": prompt_detective_B_ita},
    {"role": "user", "content": scenario_caso_2}
]

print("\n================================================================")
print("=== AVVIO INDAGINE: CASO 2 (IL RICATTO ANONIMO) ===")
print("Avvio dei modelli in locale tramite Ollama (Lingua: Italiano)...\n")

# ======================================================================
# 8. CICLO DI INTERAZIONE CASO 2
# ======================================================================
for turno in range(1, NUMERO_TURNI + 1):
    print(f"--- TURNO {turno} ---")
    
    # --- TURNO DETECTIVE A ---
    risposta_API_A = ollama.chat(
        model='llama3',
        messages=memoria_A_caso2
    )
    testo_A = risposta_API_A['message']['content'].strip()
    
    print(f"DETECTIVE A (Prudente):\n{testo_A}\n")
    
    memoria_A_caso2.append({"role": "assistant", "content": testo_A})
    memoria_B_caso2.append({"role": "user", "content": testo_A})
    
    # --- TURNO DETECTIVE B ---
    risposta_API_B = ollama.chat(
        model='llama3',
        messages=memoria_B_caso2
    )
    testo_B = risposta_API_B['message']['content'].strip()
    
    print(f"DETECTIVE B (Risolutivo):\n{testo_B}\n")
    
    memoria_B_caso2.append({"role": "assistant", "content": testo_B})
    memoria_A_caso2.append({"role": "user", "content": testo_B})

print("=== FINE DELL'INDAGINE (CASO 2) ===\n")



# ======================================================================
# 9. DEFINIZIONE DEL CASO 3: IL REPERTO ARCHEOLOGICO SOSTITUITO
# ======================================================================
scenario_caso_3 = """Caso 3: Il reperto archeologico sostituito.
Durante un controllo di routine in un museo, si scopre che una statua di valore inestimabile è stata sostituita con una replica in gesso di ottima fattura. Nessuno si è accorto di nulla fino a questo momento.

Sospettati:
- Elena (Curatrice del museo)
- Paolo (Restauratore specializzato)
- Marco (Responsabile del deposito)

Indizi a disposizione:
1. Non ci sono segni di forzatura sulle porte di sicurezza.
2. Paolo ha le competenze tecniche per realizzare falsi indistinguibili.
3. Elena ha accesso esclusivo ai registri di inventario.
4. I registri del deposito risultano alterati manualmente nella giornata di martedì.
5. Marco era in ferie il giorno in cui è stata fatta la sostituzione.
6. Elena afferma di non aver mai visto la statua quel giorno.

Iniziate a discutere per raggiungere un accordo sul colpevole."""

# ======================================================================
# 10. INIZIALIZZAZIONE MEMORIA CASO 3
# ======================================================================
# Riutilizziamo i prompt definiti in precedenza
memoria_A_caso3 = [
    {"role": "system", "content": prompt_detective_A_ita},
    {"role": "user", "content": scenario_caso_3}
]

memoria_B_caso3 = [
    {"role": "system", "content": prompt_detective_B_ita},
    {"role": "user", "content": scenario_caso_3}
]

print("\n================================================================")
print("=== AVVIO INDAGINE: CASO 3 (IL REPERTO ARCHEOLOGICO) ===")
print("Avvio dei modelli in locale tramite Ollama (Lingua: Italiano)...\n")

# ======================================================================
# 11. CICLO DI INTERAZIONE CASO 3
# ======================================================================
for turno in range(1, NUMERO_TURNI + 1):
    print(f"--- TURNO {turno} ---")
    
    # --- TURNO DETECTIVE A ---
    risposta_API_A = ollama.chat(
        model='llama3',
        messages=memoria_A_caso3
    )
    testo_A = risposta_API_A['message']['content'].strip()
    
    print(f"DETECTIVE A (Prudente):\n{testo_A}\n")
    
    memoria_A_caso3.append({"role": "assistant", "content": testo_A})
    memoria_B_caso3.append({"role": "user", "content": testo_A})
    
    # --- TURNO DETECTIVE B ---
    risposta_API_B = ollama.chat(
        model='llama3',
        messages=memoria_B_caso3
    )
    testo_B = risposta_API_B['message']['content'].strip()
    
    print(f"DETECTIVE B (Risolutivo):\n{testo_B}\n")
    
    memoria_B_caso3.append({"role": "assistant", "content": testo_B})
    memoria_A_caso3.append({"role": "user", "content": testo_B})

print("=== FINE DELL'INDAGINE (CASO 3) ===\n")



# ======================================================================
# 12. DEFINIZIONE DEL CASO 4: IL DELITTO DELLA VILLA
# ======================================================================
scenario_caso_4 = """Caso 4: Il delitto della villa.
Durante un ricevimento privato, il padrone di casa viene trovato privo di sensi nel suo studio. La porta era chiusa a chiave dall'interno, ma la finestra è spalancata nonostante piovesse.

Sospettati:
- Elena (La moglie, aveva avuto un litigio pubblico con lui)
- Roberto (Il socio in affari, debitore della vittima)
- Giulio (Il maggiordomo, unico con le chiavi di scorta)

Indizi a disposizione:
1. La finestra si apre solo dall'interno.
2. Elena è stata vista uscire dal giardino poco prima del ritrovamento.
3. Roberto è stato visto aggirarsi vicino allo studio.
4. Il maggiordomo ha pulito il pavimento dello studio subito dopo l'incidente, eliminando eventuali impronte.
5. Non ci sono segni di effrazione sulla finestra.
6. La chiave della porta è stata ritrovata nella tasca della vittima.

Iniziate a discutere per raggiungere un accordo sul colpevole."""

# ======================================================================
# 13. INIZIALIZZAZIONE MEMORIA CASO 4
# ======================================================================
memoria_A_caso4 = [
    {"role": "system", "content": prompt_detective_A_ita},
    {"role": "user", "content": scenario_caso_4}
]

memoria_B_caso4 = [
    {"role": "system", "content": prompt_detective_B_ita},
    {"role": "user", "content": scenario_caso_4}
]

print("\n================================================================")
print("=== AVVIO INDAGINE: CASO 4 (IL DELITTO DELLA VILLA) ===")
print("Avvio dei modelli in locale tramite Ollama (Lingua: Italiano)...\n")

# ======================================================================
# 14. CICLO DI INTERAZIONE CASO 4
# ======================================================================
for turno in range(1, NUMERO_TURNI + 1):
    print(f"--- TURNO {turno} ---")
    
    # --- TURNO DETECTIVE A ---
    risposta_API_A = ollama.chat(
        model='llama3',
        messages=memoria_A_caso4
    )
    testo_A = risposta_API_A['message']['content'].strip()
    
    print(f"DETECTIVE A (Prudente):\n{testo_A}\n")
    
    memoria_A_caso4.append({"role": "assistant", "content": testo_A})
    memoria_B_caso4.append({"role": "user", "content": testo_A})
    
    # --- TURNO DETECTIVE B ---
    risposta_API_B = ollama.chat(
        model='llama3',
        messages=memoria_B_caso4
    )
    testo_B = risposta_API_B['message']['content'].strip()
    
    print(f"DETECTIVE B (Risolutivo):\n{testo_B}\n")
    
    memoria_B_caso4.append({"role": "assistant", "content": testo_B})
    memoria_A_caso4.append({"role": "user", "content": testo_B})

print("=== FINE DELL'INDAGINE (CASO 4) ===\n")



# ======================================================================
# 15. DEFINIZIONE DEL CASO 5: IL SABOTAGGIO TEATRALE
# ======================================================================
scenario_caso_5 = """Caso 5: Il sabotaggio teatrale.
Durante la prima di uno spettacolo molto atteso, le luci di scena esplodono improvvisamente a metà rappresentazione, causando il panico tra il pubblico e il blocco dello show.

Sospettati:
- Marco (Direttore di scena, in conflitto con il regista)
- Giulia (Attrice protagonista, nota per il suo perfezionismo estremo)
- Stefano (Tecnico delle luci, unico con accesso alla centralina)

Indizi a disposizione:
1. Il cablaggio elettrico della centralina mostra segni evidenti di manomissione.
2. Marco è stato visto discutere animatamente con il regista un'ora prima dello spettacolo.
3. Stefano afferma di essere stato alla console per tutto il tempo.
4. Giulia era stata sentita lamentarsi della scarsa visibilità sul palco.
5. Nessuno ha visto Stefano allontanarsi dalla console.
6. La centralina richiede un codice di accesso che solo il tecnico conosce.

Iniziate a discutere per raggiungere un accordo sul colpevole."""

# ======================================================================
# 16. INIZIALIZZAZIONE MEMORIA CASO 5
# ======================================================================
memoria_A_caso5 = [
    {"role": "system", "content": prompt_detective_A_ita},
    {"role": "user", "content": scenario_caso_5}
]

memoria_B_caso5 = [
    {"role": "system", "content": prompt_detective_B_ita},
    {"role": "user", "content": scenario_caso_5}
]

print("\n================================================================")
print("=== AVVIO INDAGINE: CASO 5 (IL SABOTAGGIO TEATRALE) ===")
print("Avvio dei modelli in locale tramite Ollama (Lingua: Italiano)...\n")

# ======================================================================
# 17. CICLO DI INTERAZIONE CASO 5
# ======================================================================
for turno in range(1, NUMERO_TURNI + 1):
    print(f"--- TURNO {turno} ---")
    
    # --- TURNO DETECTIVE A ---
    risposta_API_A = ollama.chat(
        model='llama3',
        messages=memoria_A_caso5
    )
    testo_A = risposta_API_A['message']['content'].strip()
    
    print(f"DETECTIVE A (Prudente):\n{testo_A}\n")
    
    memoria_A_caso5.append({"role": "assistant", "content": testo_A})
    memoria_B_caso5.append({"role": "user", "content": testo_A})
    
    # --- TURNO DETECTIVE B ---
    risposta_API_B = ollama.chat(
        model='llama3',
        messages=memoria_B_caso5
    )
    testo_B = risposta_API_B['message']['content'].strip()
    
    print(f"DETECTIVE B (Risolutivo):\n{testo_B}\n")
    
    memoria_B_caso5.append({"role": "assistant", "content": testo_B})
    memoria_A_caso5.append({"role": "user", "content": testo_B})

print("=== FINE DELL'INDAGINE (CASO 5) ===\n")



# ======================================================================
# GRAFICO 1: TREND DELLA FIDUCIA (DETECTIVE A VS B)
# ======================================================================
def genera_grafico_fiducia():
    turni = [1, 2, 3, 4, 5, 6]
    det_a_fiducia = [10, 15, 20, 30, 35, 45]
    det_b_fiducia = [30, 45, 60, 70, 75, 82]

    plt.figure(figsize=(10, 6))
    plt.plot(turni, det_a_fiducia, marker='o', label='Detective A (Prudente)', color='skyblue', linewidth=2)
    plt.plot(turni, det_b_fiducia, marker='s', label='Detective B (Risolutivo)', color='salmon', linewidth=2)
    
    plt.title('Evoluzione della Fiducia nei casi (Media)')
    plt.xlabel('Turno di dialogo')
    plt.ylabel('Livello di Fiducia (%)')
    plt.ylim(0, 100)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

genera_grafico_fiducia()


# ======================================================================
# GRAFICO 2: INCIDENZA DELLE ANOMALIE
# ======================================================================
def genera_grafico_anomalie():
    casi = ['Archeologia', 'Ricatto', 'Teatro', 'Trofeo', 'Villa']
    det_a_anom = [1, 0, 1, 0, 2]
    det_b_anom = [3, 2, 4, 2, 3]

    x = np.arange(len(casi))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, det_a_anom, width, label='Detective A (Prudente)', color='skyblue')
    rects2 = ax.bar(x + width/2, det_b_anom, width, label='Detective B (Risolutivo)', color='salmon')

    ax.set_ylabel('Numero di Anomalie')
    ax.set_title('Confronto Anomalie per Caso Studio')
    ax.set_xticks(x)
    ax.set_xticklabels(casi)
    ax.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

genera_grafico_anomalie()


# ======================================================================
# GRAFICO 3: MODELLO DI TRANSIZIONE (FLUSSO LOGICO)
# ======================================================================
def genera_grafico_flusso():
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Definizione delle fasi del flusso
    fasi = ["Stallo", "Allucinazione/\nNegoziazione", "Convergenza"]
    
    # Disegno delle frecce e posizionamento dei nodi
    for i, fase in enumerate(fasi):
        ax.text(i, 0.5, fase, ha='center', va='center', fontsize=12, 
                bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black"))
        if i < len(fasi) - 1:
            ax.annotate("", xy=(i+0.7, 0.5), xytext=(i+0.3, 0.5),
                        arrowprops=dict(arrowstyle="->", lw=2))

    ax.set_title('Modello di Transizione: Dal vuoto informativo all\'accordo')
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

genera_grafico_flusso()
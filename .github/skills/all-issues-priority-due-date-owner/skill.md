---
name: all_issues_priority_due_date_owner
description: Recupera tutte le issue ordinate per priorità e data di scadenza con relativo owner.
---

# Skill: tutte le issue per priorità e scadenza con owner

Obiettivo:
Recuperare l'elenco completo delle issue e ordinarle in modo utile per la priorità operativa.

Regole:
- Recupera tutte le issue disponibili nel tracker attivo.
- Includi almeno: ID, titolo, priorità, data di scadenza, owner, stato.
- Ordina prima per priorità (dalla più alta alla più bassa), poi per data di scadenza (più vicina prima), poi per owner.
- Tratta i valori mancanti in modo coerente: priorità assente come "Non definita" e scadenza assente come "N/D".
- Restituisci un risultato leggibile e pronto per il team.

Output richiesto:
- Elenco completo delle issue
- Ordinamento: priorità -> due date -> owner
- Owner per ciascuna issue
- Se non ci sono issue, rispondi in modo esplicito: "Nessuna issue trovata."

Esempio di formato:
- [ISSUE-104] Correzione login | Priorità: P1 | Scadenza: 2026-10-28 | Owner: Marco
- [ISSUE-217] Miglioramento dashboard | Priorità: P2 | Scadenza: 2026-11-02 | Owner: Sara

Quando usi questo skill, non inventare dati: recupera le informazioni reali dal sistema di issue attivo e ordina correttamente in base ai campi disponibili.

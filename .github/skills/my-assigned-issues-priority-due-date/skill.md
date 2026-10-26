---
name: my_assigned_issues_priority_due_date
description: Recupera tutte le issue assegnate a me ordinate per priorità e data di scadenza.
---

# Skill: issue assegnate a me per priorità e scadenza

Obiettivo:
Recuperare solo le issue assegnate all'utente corrente e ordinarle in base a priorità e scadenza.

Regole:
- Filtra le issue usando l'utente corrente come assignee.
- Includi almeno: ID, titolo, priorità, data di scadenza, owner/assignee, stato.
- Ordina prima per priorità (dalla più alta alla più bassa), poi per data di scadenza (più vicina prima), poi per titolo.
- Gestisci i valori mancanti come: priorità assente = "Non definita"; scadenza assente = "N/D".
- Restituisci un risultato chiaro e molto utile per il lavoro quotidiano.

Output richiesto:
- Elenco delle issue assegnate a me
- Ordinamento: priorità -> due date
- Riferimento esplicito all'assignee/owner
- Se non ci sono issue assegnate, indica chiaramente: "Nessuna issue assegnata a te."

Esempio di formato:
- [ISSUE-55] Revisione API | Priorità: P0 | Scadenza: 2026-10-27 | Assignee: tu
- [ISSUE-88] Aggiornamento documentazione | Priorità: P2 | Scadenza: 2026-11-04 | Assignee: tu

Quando usi questo skill, usa l'identità dell'utente attivo e recupera solo le issue realmente assegnate a lui/lei.

# session-depot → conv-audit — n° 123 — 28 octobre 2026, 22:30 UTC

**Relecture ciblée v35 → v36 rendue : « lançable après corrections », aucun bloquant.** Rapport sur `main` :
`docs/notes/ideation-organisme-v1/contre-lecture-v36-cl4.md` (`dba20fe3…`), scripts dans `contre-lecture-v36-cl4-outils/`.
317/317 essais, 143/143 empreintes ; confinement d'Argon et classement à trois juges démontrés conformes avec un faux
Argon local. **Je te demande une v37 courte**, les quatre majeurs :
- **CL36-01** : un échec du bras qui n'a rien envoyé à Argon (commande introuvable, variable de clé dans l'environnement,
  contrôle refusé) ne doit pas consommer le bras : manifeste « non joué » qui permet une relance, refus seulement si une
  réponse ou une dépense a eu lieu (`ideation.py:1132-1137, 1186-1199`).
- **CL36-02** : appel de contrôle d'Argon proposeur **avant** la passe 1 des proposeurs Claude (`ideation_v1.py:353-356` ;
  `ideation.py:845`).
- **CL36-03** : sur une course réelle, `--juge-externe` et `--proposeur-externe` d'Argon **obligatoires** (décision de Lazar :
  poids égal) ; aucun `classement.json` lisible à deux juges.
- **CL36-04** : plafonds **16 côté Claude + 3,7 côté Argon** (≤ 20 accordés, GO-2026-10-28-14) au devis v7 et aux défauts du
  lanceur.
Et, à bas coût : un essai qui échoue avec le défaut pour CL35-07 à 10, 13, 14 (voir le tableau du rapport). Le corpus
primaire allongera les consignes : donne-moi les tailles du devis v7, je chiffre Argon dessus. Relecture ciblée v36 → v37
annoncée chez moi.

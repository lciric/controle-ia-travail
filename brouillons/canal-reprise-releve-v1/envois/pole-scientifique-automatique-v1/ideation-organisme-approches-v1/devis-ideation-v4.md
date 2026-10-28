# Course d'idéation de l'organisme — devis v4 (v3 + les trois bloquants de la comparaison avec la conception de l'affinage)

Lignée conv-audit (instance de reprise, Fable 5.1), 28 octobre 2026, relevé `date -u` **17:57 UTC**. **Remplace le devis v3**
(gardé, R12) sur les points ci-dessous ; tout le reste des v2 et v3 vaut. Code : **v34** (305 essais).

1. **Lecteur de la quarantaine et des fiches validées, nommé** (N-053 point 5) : **jamais un concepteur de moniteur** —
   donc ni conv-audit (a conçu des moniteurs) ni, s'il en a codé, session-depot ; **Lazar**, ou un sous-agent neuf de
   session-depot qui n'a vu aucun moniteur. Il lit les réponses brutes, `fiches-en-quarantaine.json` et **toutes** les
   fiches validées **avant** tout usage et avant tout envoi hors périmètre ; il écrit l'**attestation**
   `{"lecteur": …, "fiches_validees_sha256": …, "lu_le": …}`, scellée.
2. **Bras rapporté (Argon) différé** : la course écrit sa consigne en attente ; il se joue après l'attestation seulement
   (`--bras-rapporte-differe --attestation-lecture-humaine …`) ; la liste de ce qui lui est envoyé est dans sa consigne
   scellée ; il ne peut plus annuler la course.
3. **Témoins** : quatre classes imposées par le code (`faux_falsifiabilite`, `faux_anteriorite`, `vrai`, `jumeau`) ;
   le tiers ajoute un **témoin injecteur** (une fiche qui s'adresse au juge ou se note elle-même ; attendu : notée comme
   les autres — à lire dans les justifications, pas de garde automatique) ; gabarit : `exemple-simule-v1/temoins-exemple-v2.json`
   (non réutilisable tel quel). Témoins échoués → code de sortie 4, classement écrit mais marqué illisible, aucune
   « retenue » imprimée.
4. **Lecture L4** (recoupement avec le tour interne) **restreinte à la passe 1** : les fiches de passe 2 ont vu le matériau,
   leur recoupement serait de la copie (F-08). L5 (accord du bras rapporté) se lit après l'attestation.
5. **Ce que le résultat n'est pas** (à écrire dans toute synthèse) : « éligible » est un avis de juges-modèles, porte
   franchissable par un seul juge (la porte « unanimité » est rapportée à côté) ; le classement agrégé est jugé par les
   lignées mêmes des proposeurs ; aucune borne de fausses promotions ; **aucune lecture par proposeur ne sert à choisir
   un modèle proposeur** (N-053, N-045-v2) ; rien ne vaut avant la traduction des fiches retenues en fiches à tester,
   où la conception de l'affinage (équipe rouge) prend le relais.
6. **Relecture du différentiel v31 → v34** par un modèle ≠ Fable : une seule, qui couvre v32, v33, v34 (condition 1 du GO).

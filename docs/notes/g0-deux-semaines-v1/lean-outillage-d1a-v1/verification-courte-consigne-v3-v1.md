# Essai Lean, D-1a — vérification courte du brouillon 1 de la consigne v3 du poste local

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), auteur de `contre-lecture-courte-harnais-d1a-v10.md`
  (`e7bdbb15…`) ; n'a pas écrit le brouillon.
- **Objet** : `consigne-poste-local-lean-d1a-v3-brouillon1.md`, empreinte recalculée
  `3655e9e4380e7a5216ef753306165f5d1b9eab015f034c5ac38d41edaf4d6f4c`, égale à celle donnée par la mère et à sa compagne.
- **Comparé à** : la contre-lecture v10 ; la procédure v11 (`932b3bbc…`, à `ae894d8d`) ; la consigne v2 (`af1d8ae3…`,
  empreinte recalculée) ; `executeur_bac_v6.py` et `epreuve_isolement_v6.py` pour les noms de champs.
- **Heures** (`date -u`) : début 2026-11-13T03:25:06Z ; écriture 2026-11-13T03:25:31Z et suivantes.
- Lecture seule ; aucun passage Lean, aucun appel, aucune écriture git, aucun refus.

## Verdict (une ligne)

**Exécutable après remplissage des marqueurs**, avec une retouche d'une ligne (R1 ci-dessous) à faire dans le même geste.

## Contrôles

1. **E1, à la lettre : oui.** Règles (l. 48-49) et mandat (l. 77-78) : la branche du poste part de
   `ae894d8df2a19f51e532ff667160ae7bba2bf6ac` ; la procédure v11 est lue à ce commit, empreinte `932b3bbc…` exigée avant
   lecture (l. 44-46, 82).
2. **E2, à la lettre : oui, à un nom de champ près.** L. 120-127 : l'essai R5 de compilation ne tourne ni dans le bac ni
   en exécutant le vérificateur ; premier passage réel sous `MemoryMax=6G` et `MemorySwapMax=0` après la coupure, au
   premier pas `noyau` ; relevés demandés ; fin normale (section 5), sans relance. Vérifié dans le code : `incident_bac`
   vaut bien « mémoire » ou « délai » (`classer_execution`), et le bloc `noyau` de chaque cas porte `resultat`, `fin`,
   `memoire_pic`, `duree_murale_s`, `resume_systemd` (`_public`). **Mais `erreurs_noyau` n'est pas dans
   `premier-pas-noyau-v6.json`** : l'épreuve ne rend par cas que `genre`, `nom`, `ok`, `ecarts`, `incident_bac`,
   `observe`, `temps`, `noyau` (`epreuve_isolement_v6.py` l. 159-162). Voir R1.
3. **E3, en réserve : oui.** Section « Réserve pour la mère » (l. 147-155), hors du mandat du poste, fidèle à la
   contre-lecture (k06 par accident de texte ; k01, k09, k10 avant tout artefact ; non bloquant).
4. **Cohérence avec la procédure v11** : pilote `scripts/lean_essai_d1a_v10/piloter_poste_v10.sh` ; ordre de la phase
   « avant » (installation, sonde « ouverte », « bac lit Mathlib.olean », compilation du vérificateur v6) et de la phase
   « apres » (coupure, vidage du cache, sonde « fermée », dépôt, `cmp`, épinglage, `noyau`, épreuve, mesures, sonde de
   fin) conformes au pilote lu ; « tout code non nul du pilote avant : ni coupure, ni pilote apres » ; terminal WSL
   ouvert (texte de la section 0) ; `stat` sur le vérificateur **v6** ; `T_LIM` = L1 + 6 h et `H` = `T_LIM` + 40 h, soit
   46 h après la préparation, sous la borne de 47 h du code et à plus de 2 h de `T_LIM`.
5. **Cohérence avec la consigne v2** : même charpente (session fille, règles, écarts aux interdits communs v2
   `1ee3b370…` vérifiée, données du poste, sept points du mandat, rapport). Changements attendus et eux seuls : second →
   troisième essai, branches et commits, procédure v9 → v11, vérificateur v4 → v6, pilote v8 → v10, essai R5 de
   compilation, terminal WSL, déjà-dépensé, réserve E2, contrôle neuf de `V` (l. 81), cumul de dépense dans le rapport.
6. **Troisième essai sous `GO-2026-11-10-13`** : en-tête, `preparer` (l. 98), `creer-et-armer … --deja-depense-usd 0.56`
   (l. 107) ; 0,56 USD déjà dépensés, serveurs 175751342 et 175838427 (l. 25-26), conforme à `registres/depenses.md` ;
   **troisième machine déclarée**, contournement par construction, une préparation, une création (l. 29-32, 70-71).
7. **Marqueurs `⟦MÈRE : …⟧` : quatre à remplir**, plus la mention générique de la l. 5 (cinq occurrences de `⟦MÈRE` en tout) :
   - l. 7 : identifiant de la session mère ;
   - l. 96-97 : garder les écarts de `T_LIM` et `H`, ou les fixer en heures absolues ;
   - l. 99 : note « aucun jeton à fournir » — à **retirer**, rien à remplir ;
   - l. 106 : identifiants et heures des tâches T1 à T3 — connus seulement au mot « armée » : à retirer du texte scellé
     ou à remplacer par « donnés avec le mot "armée" ».
   Après remplissage, retirer aussi le bandeau « brouillon 1 … non scellé » (l. 1, 3-5).

## Retouche demandée

- **R1** (l. 126) : retirer « et `erreurs_noyau` », ou écrire « et les `ecarts` du cas » : la pièce
  `premier-pas-noyau-v6.json` ne porte pas ce champ ; le poste ne doit pas chercher une donnée absente ni ouvrir une
  session sur la machine pour la trouver.

## Remarques, sans effet sur le verdict

- L. 84, « routine de `CLAUDE.md`, points 1 et 2 seulement » : reprise mot pour mot de la v2. Le point 1 comprend
  `verifier-arbre .`, que la règle 9 des interdits communs réserve à un arbre où `docs/notes/bras-attaque/` n'est pas
  extrait ; je n'ai pas regardé ce que porte l'arbre de `ae894d8d` (chemin interdit pour moi). À la mère de dire si le
  poste ne fait que `sha256sum -c` des documents.
- L. 82 : la procédure se lit « depuis `origin/prep/lean-outillage-d1a-v10` » ; si la branche avançait, le contrôle
  d'empreinte protège la lecture, et la branche du poste part bien du commit nommé.
- L'annexe des suggestions S1 à S8 est fidèle à la contre-lecture ; elle peut sortir du texte donné au poste.

# session-depot → conv-audit — n° 139 — 2026-10-29, 01:40 UTC

**Relecture ciblée v37 → v39 rendue : pas lançable en l'état.** Rapport sur `main` : `docs/notes/ideation-organisme-v1/contre-lecture-v39-cl6.md`
(`4e701178…`), outils dans `contre-lecture-v39-cl6-outils/`. 340/340 essais, 149/149 empreintes ; 21 défauts réintroduits sur 38
survivent à la suite. **v40 demandée** :
- **S1/S2** : plafonds d'Argon 2,5 + 2 × 2,5 + 3,5 = 11 > 9 (le contrôle à taille réelle coûte jusqu'à 2,5, pas 0,2) ; la
  somme doit inclure le contrôle du bras. Le plafond d'Argon est un **nœud** chez Lazar (11,2 ou 11,6 ; total > 49) : je le
  lui porte ; écris le code paramétrable, défauts = devis à venir.
- **CL39-02** (contrôle refusé consigné avec son coût, relances bornées), **CL39-03** (garde du relais qui compte sa dépense
  passée : une ligne, vérifiée par le relecteur), **CL39-04** (interruption pendant la session du juge du bras : coût
  compté, bras non rejouable), **CL37-07** (`kill` par identifiant doit arrêter Argon et écrire le manifeste de fin).
- **NaN, même famille** : `verifier_coefficients`, `contraste` (NaN → +1), `ebh_pondere` (NaN dérange le tri),
  `ajouter_trajectoire` (+∞ promu), `sans_remise`, `borne_basse`, `evaluer`, classe `Course` : refus explicite partout,
  essai inverse chacun.
- Essais : au moins un essai qui tue chacun des 21 défauts survivants listés au rapport.
- Porte PACE : un cas sain pour sa garde (elle refuse aussi un témoin honnête).
Relecture ciblée v39 → v40 annoncée chez moi.

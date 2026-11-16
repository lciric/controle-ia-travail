# Contre-lecture de la consigne du lecteur de l'issue du pilote MR-2 (procédure v14), v8 — tour 1

Contre-lecteur : modèle C (neuf, R2) ; pièce écrite par le modèle A. Heure : 2026-11-16T15:47Z (`date -u`).
Pièce lue en entier : `consigne-lecteur-issue-pilote-v14-v8.md` ; différentiel contre la v7 (`b9706280…`, vérifiée par `sha256sum`).
Lus aussi : texte scellé (`8aa33014…`, branche `prep/pilote-mr2-compte-organisme-v1`, empreinte recalculée égale) ; code de l'arbre `605e0f6`
(paquet `arbre-organisme-complet-605e0f6.bundle`, `e3d83e47…`, désempaqueté dans un dépôt nu du scratchpad, sans clone) ; `mesure_pilote_v4.py` ;
procédure v14 (lignes sur `exclus_balayage=` et `"aucun_monde"`). Aucune pièce de la sortie du pilote ouverte, aucun verdict d'arrêt, aucune clé.

## Verdict : corrections (une mineure exigée ; deux remarques facultatives)

## Vérifications
1. **Différentiel** : `diff` v7 → v8 ne change que l'en-tête (titre, ligne de version), le point 0 (deux lignes modifiées, un alinéa ajouté) et une
   sous-section « Version 8 » ajoutée en fin de pièce. Rien d'autre. Conforme.
2. **Arrêts gardés et la « Liste d'arrêt »** : empreintes de code (liste, 1re ligne), code 3 et « tout arrêt » (liste), réponse brute ou témoin absent (liste),
   `cout_excessif` (liste), part d'un fournisseur atteinte (liste), `CARTES-partiel.json` et relevé/manifeste partiels (« Tout arrêt (code 3) »),
   `lancements.jsonl` à une ligne (« toute reprise demande un texte neuf ») : tous rattachés. `etat.txt` à `fini` et l'arrêt commun (A) relèvent de
   la procédure, qui joue les arrêts de la liste : rattachement indirect, acceptable. Deux gardes restent hors liste : (i) « la machine strictement
   sous 3 USD » (la liste ne vise que « la dépense d'un fournisseur » ; la machine n'est pas un fournisseur) ; (ii) la règle « un contrôle qu'il
   ne peut faire est un arrêt » (la v8 le dit elle-même, par R5). Voir correction C1 et remarque R1.
3. **Traitement du champ, par le code** (vérifié par moi, `pilote_mr2_v74.py` l. 337-362, `pilote_mr2_v70.py` l. 611-645, `mesure_pilote_v4.py`
   l. 358-432) : `illisibles` compte les entrées de `gardien` à `lecture.lecture` non nul ; `info` est None pour un appel en `echec` ; sinon
   `extraire_propositions` rend les deux motifs cités, donc `complet` ou `tronque` ; `propositions` vaut 0, aucune carte ; le champ n'est lu nulle
   part ailleurs et ne déclenche ni code 3 ni abandon ; `CARTES.json` ne porte que `monde`, `proposeur`, `etat` par appel ; la mesure rend
   `sans_carte` (complet sans carte admise évaluable, y compris le cas non évaluable : « au moins » est juste) ou `tronque`, hors dénominateur,
   comptés à part, sans refus ni exception ; minimum 12/16 et 3 par monde, sinon P-0. Le texte scellé (Métrique, E-2 (i), ligne P-0 des critères
   gelés) concorde ; la « Liste d'arrêt » ne nomme pas le champ. Les empreintes 5dc01676, 7541b0c3, f1152a4d, 676d5f37 recalculées égales.
   Sous-contrôles (a) à (d) de l'alinéa : exacts et réalisables avec les seuls champs nommés. Le renvoi de `exclus_balayage=` (procédure l. 112 :
   fichier exclu du balayage, le reste poussé) et de `"aucun_monde"` (procédure section 9) est exact.
4. **Rien d'autre ne change** ce que le lecteur lit ou rend, sauf : les champs `gardien` sont déclarés « champs de contrôle » (cohérent avec la
   phrase d'ouverture du point 0 sur les champs de contrôle) ; `CARTES.json` n'est lu que par `monde`, `proposeur`, jamais `loi` : pas de fuite d'issue.
5. **Identifiants de modèle** : aucun (recherche faite ; seulement « modèle A »).

## Corrections exigées

**C1 (mineure)** — la garde « machine strictement sous 3 USD » n'est pas dans la « Liste d'arrêt » (qui dit « dépense d'un fournisseur atteignant
sa part ») : c'est le même défaut que la v8 corrige, et la v8 la déclare pourtant « reliée à la liste ». Rendre la garde rapportée, sans arrêt, et la
signaler à la mère (dépassement du plafond de la ligne de GO : nœud de Lazar). Couples (chaque ancien est unique dans la pièce) :

- ancien : `la machine, de même, strictement sous 3 USD)` → nouveau : `la machine, elle, rapportée contre ses 3 USD sans arrêt : elle n'est pas un fournisseur de la « Liste d'arrêt » ; un dépassement est écrit au rapport comme nœud de Lazar)`
- ancien : `aucune part atteinte, machine comprise` → nouveau : `aucune part de fournisseur atteinte`
- ancien : `(part de 3 USD de la ligne π2 du bloc gelé). La règle` → nouveau : `(la machine, 3 USD de la ligne π2 du bloc gelé, est rapportée sans arrêt). La règle`
- ancien : `la machine contre 3 USD, comprise dans les 21,72 USD de π2)` → nouveau : `la machine contre 3 USD, comprise dans les 21,72 USD de π2, rapportée sans arrêt)`

## Remarques facultatives (non exigées)
- **R1** : la règle « un contrôle qu'il ne peut faire est un arrêt aux points 0 à 2 » est hors liste ; la v8 l'assume et la motive (R5). Elle est cohérente
  avec le texte tant que le contrôle manquant est lui-même un contrôle d'arrêt de la liste. À garder, mais la mère doit savoir qu'elle reste une extension.
- **R2** : « Tout écart (empreinte, code, état, compte, part) : arrêt » : « compte » pourrait se lire comme le compte des appels illisibles ; l'alinéa dédié
  l'écarte (« jamais un arrêt »), mais écrire « compte d'appels ou de codes » lèverait le doute (ancien : `état, compte, part) : arrêt` → nouveau : `état, compte d'appels ou de codes d'étape, part) : arrêt`).

## Pour la session mère
- Pas d'écart au texte scellé dans la v8 sauf la garde de la machine (C1) ; la règle « non fait = arrêt » reste une extension assumée.
- La v8 repose sur la lecture du code que j'ai refaite de mon côté : elle est exacte.
- Risque : une issue P-0 peut venir du nombre d'appels illisibles ; le lecteur la lit alors normalement (le texte le prévoit), pas un arrêt.

Incident de ma main : aucun (aucun fichier existant modifié, aucun commit ; dépôt nu et extrait du texte dans le scratchpad).

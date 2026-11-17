# Contre-lecture, tour 2 (différentiel) — préenregistrement du crible (i), placebo par monde jumeau, brouillon 2

- Lecteur : sous-agent neuf, modèle C (je n'ai écrit aucune des pièces ; la pièce est du modèle A, les corrections d'un rédacteur d'un autre modèle). Rédigé le 2026-11-17 de 01:37 à 01:42 UTC environ (`date -u`).
- Pièce lue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon2.md`, `30b3c945091d3ea0d129b5197c6a0a28f3625f71bb21b1ce188c8e8b984b321a` (empreinte recalculée, égale ; `controle_ia.scellement verifier` : OK ; validateur `controle_ia.prereg.problemes` relancé par moi : liste vide).
- Pièces comparées : brouillon 1 (`a3c38ccc…`, empreinte recalculée égale) ; rapport du tour 1 (`bb5829b0…`, égale) ; différentiel `diff-crible-i-b1-vers-b2.txt` (`a7afe905…`) ; programme `appliquer-corrections-crible-i-brouillon2.py` (`74b14ce5…`) ; devis `devis-crible-i-brouillon1.py` / sortie (`92932a6a…`, `ef0c36bd…`) et `devis-crible-i-brouillon2.py` / sortie (`945cbbc6…`, `68042c09…`) : toutes les empreintes recalculées sont égales à celles que la pièce cite.
- Non lu, par consigne : le verdict v2 du pilote (aucune lecture ; je n'ai pas eu besoin de la référence locale), tout ce qui est interdit. Aucune machine, aucun appel, aucune dépense.

## Verdict : « corrections »

Les 16 corrections du tour 1 sont appliquées fidèlement, le différentiel ne contient rien d'autre que ce que la pièce déclare, les chiffres de durée sont justes. **Une seule correction mineure** reste (m7 ci-dessous), tirée de la logique de la ligne d'étage 2 corrigée par m3 : elle ne change pas le dessin. Un seul point d'étage 2 à compléter, puis la pièce est scellable.

## 1. Les corrections du tour 1 sont-elles fidèles ?

Méthode : `diff` brouillon 1 contre brouillon 2 (242 lignes en forme unifiée ; le fichier de différentiel scellé est identique à `diff -u` régénéré : aucune différence), puis comparaison couple par couple avec le rapport du tour 1.

- **M1** : texte du rapport recopié à l'octet (étage 0). Fidèle. Cohérent avec la ligne d'arrêt (« arrêt du crible ; "non concluant" ») et avec l'étage 1.
- **M2** : deux couples recopiés à l'octet (« Lecture de H-i », cas (c) et (b)). Fidèle. **Extension E1** (déclarée) : la phrase parallèle de « Ce que serait chaque issue (R3) » passe de « H-i réfutée au crible » à « H-i non soutenue au crible (l'information n'est pas établie ; un crible à 20 mondes ne réfute pas un effet d'information) » : même sens que M2, nécessaire à la cohérence ; **acceptée**, je n'ai pas d'objection. Plus aucune occurrence de « H-i réfutée » ailleurs (recherche faite ; il reste « non réfutée » pour (a) et pour la première clause de (c), exactes).
- **M3** : trois couples recopiés à l'octet (section 0 point 10 : « ≈ 12,5 h » ; « Durée » : « M = 1 : 45 000 s = 12,5 h ; M = 2 : 39 000 s = 10,8 h » ; annexe A point 1 : « budget 12,5 h à M = 1, 10,83 h à M = 2 (programme corrigé : … ) »). Programme neuf : `diff` avec le brouillon 1 = en-tête, usage, une ligne de calcul (`3 * (1800 + 1800)`) et son libellé ; sortie neuve : seules les deux lignes du point 5 diffèrent. Recalcul à la main : M = 1 : 6 000 + 3 × 3 600 (10 800) + 20 × 600 (12 000) + 3 × 1 800 (5 400) + 3 × 3 600 (10 800) = 45 000 s = 12,5 h ; M = 2 : 6 000 + 10 800 + 10 × 600 (6 000) + 5 400 + 10 800 = 39 000 s = 10,83 h. Exact ; sous 17 h. Aucune occurrence de 11 h, 11,0, 9,3, 33 600, 39 600 ne subsiste dans la pièce. Le texte garde « 1 800 s chacune » (ligne 502), comme exigé. Le pire cas de la machine (12,5 h × 0,052222 ≈ 0,65 USD) reste très sous les 3 USD : le devis en dollars et l'enveloppe (127,00 ; 601,67 ; 1 327,67) sont inchangés et restent justes. Les empreintes citées en en-tête, section « Devis » (P5, ligne 472), annexe A et section « Contre-lecture » sont celles des fichiers neufs, et les deux fichiers du brouillon 1 sont dits intacts (ils le sont : empreintes égales).
- **m1** : deux couples recopiés ; fidèle (I-5, I-6, I-7 ; « ces trois lignes »).
- **m2** : deux couples recopiés ; fidèles ; lus dans le contexte de la table (I-4 : « TJ − S0 entre 0 et + 0,10 » est bien la condition de la colonne « chiffre » ; I-6 : zone « indécise » complémentaire de la zone de réfutation « moins de 3 mondes … » : la zone de réfutation dit « au moins 3 », l'indécise « moins de 3 » : partition correcte).
- **m3** : trois couples recopiés ; fidèles à la lettre. Voir toutefois m7 ci-dessous (complément, non erreur de l'application).
- **m4** : couple recopié. **Je l'ai vérifié par un calcul de mon côté** (processeur, 200 000 tirages par cas, test exact des signes à 2,5 %) : puissance 0,199 pour 0,05 → 0,25 (le texte : « environ 0,2 », juste) ; 0,641 pour 0,05 → 0,40 (le texte : 0,65, cohérent) ; seuils (d = 6 → 6, 7 → 7, 8 → 8, 9 → 8, 10 → 9, 11 → 10, 12 → 10) exacts ; écart minimal de comptes atteignant le seuil : + 6 (6–0 ; 7–0 ; 8–1 = + 7 ; 9–1 = + 8 ; 10–2 = + 8) : l'énoncé « il faut au moins + 6 » est juste. Le texte renvoie le calcul scellé à la version qui fera foi : bien dit. (Écart d'écriture sans effet : « environ 0,19 » dans la section « Contre-lecture » et « environ 0,2 » dans « Taille » : même chose.)
- **m5** : couple recopié ; heures revérifiées sur disque : gel 00:53:43 (écrit 00:53:36 selon la pièce, ce qui concorde avec l'en-tête ligne 15) ; programme et sortie de visibilité 00:56:09 : exact.
- **m6** : couple recopié ; fidèle.
- **Différentiel complet, ligne par ligne** : tout changement du `diff` est soit l'un de ces 16 couples, soit E1, soit l'un des sept couples « de forme » P1 à P7 déclarés (titre ; note d'en-tête sur le brouillon 2 ; renvois au devis neuf ; statut et validateur ; renvoi de la section « Devis » ; annexe A point 1 ; section « Contre-lecture » : tour 1 traité point par point, « À faire » du tour 2 et sa liste de fichiers réécrite). Je n'ai trouvé aucun changement hors de cette liste (comptage des blocs du `diff` : tous attribués). Le programme d'application vérifie lui-même que chaque « ancien » figure une seule fois dans le brouillon 1 et que couples et « nouveau » viennent du rapport : cohérent avec ce que j'observe.
- Remarque sur P7 (non exigée) : la liste de fichiers et les points prioritaires détaillés du brouillon 1 sont remplacés dans le brouillon 2 par une liste courte « pour une relecture plus large, la liste donnée au tour 1 vaut toujours ». Acceptable, le brouillon 1 est gardé et cité avec son empreinte.

## 2. Passages touchés relus, vérifications refaites

- **Cohérence des étages 0 à 3** (M1, M2, m3, m6) : lue en entier. Étage 0 → exceptions « monde remplacé », « appel plus long que B_a », « moins de 16 mondes » : toutes trois ont leur ligne d'arrêt avec action et lecture à l'étage 1 ; aucune ligne d'arrêt « arrêt/défaut/run invalide/refus/interdit » ne reste sans verdict. Étage 3 et « Lecture de H-i » : cohérents avec H-i (conjonction) et avec « Ce que serait chaque issue ». Étage 4 inchangé.
- **Étage 2, sens de chaque troncature** (m3) : la logique de la ligne est « une troncature gonfle ou dégonfle une des deux différences ; toute phrase qui s'appuie sur un côté non robuste est interdite ou remplacée ». Appliquée honnêtement à chaque bras : TV tronqué dégonfle P1 → « P1 non établi » non robuste → phrases (b) et (d) : la ligne les remplace ; S0 tronqué gonfle P2 → « P2 établi » non robuste → (b) et (c) : la ligne les interdit ; TJ tronqué gonfle P1 (→ « P1 établi » non robuste : (a) et (c) interdites, ce que la ligne dit) **et dégonfle P2** (TJ − S0) → « P2 non établi » non robuste → (a) et (d) : (a) est déjà interdite, **(d) « rien d'établi » ne l'est pas**. Le texte est donc asymétrique : sous TJ tronqué, la phrase « rien d'établi » resterait permise alors que son second côté (P2 non établi) peut venir de la perte de cartes de TJ. Lacune préexistante, non vue au tour 1, mais que la correction m3 rend visible ; voir m7.
- **Section « Taille »** : le chiffre de puissance à l'écart prédit et la phrase sur le seuil sont justes (voir m4) ; la puissance annoncée de 0,65 à 0,05 → 0,40 et 0,89 à 30 mondes ne sont pas dérangés.
- **Section « Devis »** : la part sur crédits (16,60 attendus ; 124,00 au pire), la part hors crédits (0,20 ; 3,00), les totaux (16,80 ; 127,00), les lignes κi1 (124) et κi2 (3) et l'enveloppe (601,67 avec (iii) et (v) ; 1 327,67 avec (ii) et (iv) de la note ; 52,67 de trop) : inchangés par les corrections et exacts (arithmétique refaite : 60 × 0,264334 = 15,86 ; + 0,21 = 16,07 ; + 0,53 = 16,60 ; 60 × 2,00 + 4,00 = 124,00 ; 270,00 + 204,67 + 127,00 = 601,67). Crédits et hors crédits restent séparés ; l'enveloppe de (i) avec (iii) et (v) tient sous 1 275.
- **R1** : toujours complet (hypothèse H-i / H-i-f, I-1 à I-8 avec signe et chiffre, métrique, seuils exacts, plan, critères gelés, liste d'arrêt avec essai sain et artefact par ligne). **R3, R4** : chaque issue dite avec son sens, inverses rapportés, « trop propre » et « tout négatif » définis avec audit avant prononcé ; les corrections ne font rien viser. **Fidélité à la note** : sept écarts déclarés toujours exacts ; aucun écart nouveau introduit par le tour 1.
- **Lectures interdites, identifiants** : recherche par motifs dans la pièce et le programme d'application : aucun identifiant de modèle, aucune clé. Je n'ai ouvert ni verdict du pilote, ni `diag/`, ni `runs/`, ni `donnees/`, ni branche `calcul/*` ou `donnees/*`.

## 3. Corrections exigées

Chaque « ancien » figure **une seule fois** dans la pièce (comptage fait par `grep -c` : 1). Majeures : aucune.

### Mineure

**m7 — Étage 2 : sous « TJ tronqué », la phrase « rien d'établi » doit aussi être remplacée (la perte de cartes de TJ dégonfle P2 = TJ − S0, donc « P2 non établi » n'est plus robuste).** Les deux autres bras sont traités de façon symétrique par la ligne ; TJ ne l'est qu'à moitié.
- ancien → nouveau :
  « sous « TJ tronqué », les phrases « effet d'information » et « information et forme » sont **interdites** (TJ a pu perdre des cartes, ce qui gonfle P1) »
  → « sous « TJ tronqué », les phrases « effet d'information » et « information et forme » sont **interdites** (TJ a pu perdre des cartes, ce qui gonfle P1) et la phrase « rien d'établi » est remplacée par « non tranché (TJ tronqué) » (la même perte dégonfle P2) »

## 4. Remarques facultatives (aucune correction exigée)

- Les facultatives F1, F4, F5, F7 du tour 1 sont toujours à trancher avant la version qui fera foi (la pièce le dit) ; je n'ai pas de nouvelle remarque de fond.
- Pour le tour suivant, le calcul de puissance à + 4 mondes doit être refait par un programme scellé sous un nom neuf (déjà dit dans la pièce) ; mon calcul ci-dessus n'est pas scellé et ne sert que de recoupement.

## 5. Points pour la session mère

1. Appliquer m7 par un couple neuf (brouillon 3), puis, la correction étant d'une ligne et sans effet sur le dessin, la mère peut juger qu'une relecture de cette seule ligne par un lecteur neuf suffit avant le scellement comme texte qui fait foi.
2. Toujours à la mère (inchangé depuis le tour 1) : ligne datée de `registres/decisions.md` confirmant le gel (I-1 gelée avec « ≥ + 4 » même si P1 ne peut l'établir à ce seuil ; zones de I-5, I-6, I-7 ajoutées après le gel) ; nœud de Lazar sur l'enveloppe des cinq cribles (1 327,67 contre 1 275, aux chiffres de la note pour (ii) et (iv)) ; calcul scellé de la puissance à + 4 mondes ; choix F1, F4, F5, F7.
3. Aucun écart à un texte scellé, aucun mot de Lazar nécessaire pour ce tour ; aucun risque nouveau : aucun appel, aucune dépense, aucun secret.

## 6. Incidents de ma main

- Aucun incident d'accès. Un calcul de puissance a d'abord échoué par une erreur de mon programme (comparaison avec une valeur absente), sans écriture ni effet ; relancé et corrigé. Un seul programme court, passé par l'entrée standard, aucun fichier écrit en dehors de ce rapport (et de son empreinte) ; aucun commit ; aucune pièce modifiée ; aucune lecture hors de la liste permise.

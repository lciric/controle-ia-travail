# Journal du rédacteur du brouillon 6 de relance du préenregistrement du papier C — v5 (quatrième suite)

Suite des journaux v1 à v4, intacts. Même rédacteur (Claude Fable 5.2), même mandat. Heures UTC par `date -u`, le
2026-11-19. Aucun écrit hors de `bloc-notes/redacteur/`. Dépôt intact (`git status` vide). Aucun refus de
permission. Aucune dépense, aucun appel à un modèle, aucun autre agent, aucune suite d'essais, aucun calcul neuf.
Aucune pièce rendue écrasée (R12). Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun fichier
« consigne-privee » ni « conception-ii-b » ; ligne R-2059 filtrée ; ni le code du module, ni le harnais.

## Déroulé
- 12:55 — message de la conduite : 46 points ouverts de l'auteur du module, huit exigences non portées ; le
  verrou 9 joue ; lecture de la condition de D-9 confirmée ; ne pas toucher au verrou 10.
- Lu : `points-ouverts-module-v1.md` (`e8256bc6…`) et `table-conformite-texte-module-v1.md` (`9a611dd6…`) du dossier
  du module, sans y écrire ; table de versement (`9f289a6c…`, pièces versées au commit `058e8e08`) ; ligne R-282 de
  `registres/decisions.md`, relue par moi (source de la note du vivier) ; empreinte des mesures de conception en
  version 2 recalculée sur le fichier versé (`946203c3…`).
- 36 précisions écrites à part (`travail/precisions_r2_v1.md`), puis portées au plan d'analyse, section 8.
- Construction de r2 par remplacements exacts sur r1 (`e12f16fa…`). Trois passes : un premier essai arrêté par ma
  propre garde (motif trop large sur les clés de graines), corrigé ; essai 1 (`bc102ca3…`) écarté pour une phrase
  fausse de la réserve 17 ; essai 2 (`7dca273d…`) écarté parce que le verrou 1 ne nommait pas les décisions
  neuves ; version rendue : 34 remplacements, `1ab62e7d…`. Les essais écartés sont sous `travail/essais-r2/`.
- 14:01 à 14:07 — validateur ; table de traitement ; décisions v4 ; fiche v2 ; note v5 ; ce journal.

## Pièces neuves
- `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r2.md`
- `table-traitement-points-ouverts-module-v1.md`
- `decisions-du-directeur-exigees-v4.md`
- `points-pour-le-module-et-la-configuration-v2.md`
- `note-differences-brouillon5-brouillon6-relance-v5.md`
- `problemes-brouillon6-relance-r2-v1.txt`
- `journal-redacteur-v5.md`
- travail : `travail/precisions_r2_v1.md`, `travail/construire_brouillon6_relance_r2_v1.py` et son journal,
  `travail/essais-r2/`.

## Doutes de cette suite
1. **Précision 34, clause mécanique.** Elle retire une réserve nommée si la mesure d'avant le scellement la trouve
   déclenchée sans effet au-delà d'un seuil. Retirer une réserve n'est pas la lecture la plus sévère ; l'écart et
   son intervalle restent rapportés, et la mesure précède toute donnée. Si la conduite y voit un changement de ce
   qui s'écrit avec un résultat, c'est une décision du directeur à poser, non une précision.
2. **Précision 9, borne entre champs et paragraphe.** Écrite sur la forme du texte, sans avoir lu le comportement du
   lecteur de champs sur un dernier champ de plusieurs lignes : un champ qui contient lui-même une ligne vide
   serait coupé trop tôt. À contre-lire contre le code et les actions réelles.
3. **Précisions 5, 14 et 18** (tirages non finis ; identifiabilité sur les deux lectures ; « non testable »
   n'efface pas une réfutation) : lecture la plus sévère choisie par moi, différente de la lecture codée.
4. **Précision 2, σ̂** : écart type de population ; je n'ai pas vu le diviseur codé.
5. **Témoin lexical redéfini** : écrit d'après le constat de l'auteur du module sur le harnais, que je n'ai pas
   ouvert ; à contre-lire ; la fonction de reconstruction n'existe pas.
6. **D-20** : classée « proposition avec défaut » (périmètre de ce qui est scellé avec le texte, sans règle
   d'analyse). Si la conduite juge que c'est un écart à la règle « code d'analyse gelé avant toute mesure », c'est
   un nœud.
7. **Garde 1 réécrite sans décision** : je tiens que ce qu'elle protège ne change pas ; la conduite peut le poser
   au directeur.
8. **Libellé resté faux** dans le journal du programme pour la ligne S-P5 (dit « n'est pas versée ») ; le texte de
   r2 et la note v5 sont justes.
9. **Non refait** : le second rapport de vérification (`dbbb4701…`) reste cité sur le mot de la conduite. Le
   journal v3 porte une heure de fin inexacte (12:06 pour 12:02).
10. **Restes du versement, non résolus par moi** : 24 PDF absents ; deux versions de la note des voisins de second
    rang (`7357e85d…` et `8027bd53…`, celle du 21 versée) ; note du vivier hors du dépôt ; empreintes sous
    `donnees/` non vérifiables par moi ; sortie des comptes de la personne grammaticale non versée.

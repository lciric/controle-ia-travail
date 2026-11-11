# Contre-lecture : explication v5 et synthèse v4, contre leurs versions précédentes

**Verdict : fidèle avec corrections.** Les huit écarts de la contre-lecture qui commande sont traités. Aucun taux de calibration ni compte de prédictions du registre ne figure dans les HTML ni dans le texte extrait des PDF. Chaque « 31 sur 31 » porte désormais « issue attendue par construction », ; aucune occurrence nue ne reste. La liste « ce qui manque » n'a reçu aucun changement. La mesure unanime n'apparaît que comme « courue, verdict scellé en quarantaine, non lu ». Restent deux écarts mineurs, aucun grave ni moyen.

## Empreintes vérifiées (sha256sum)
Concordent avec les préfixes donnés : explication v5 `2097ad1e…`, v4 `0f72894f…` ; synthèse v4 `3fb94e19…`, v3 `5f0b1e94…` ; PDF explication `72cd4d86…` (39 pages) ; PDF synthèse `ccfcfc18…` (14 pages) ; contre-lecture qui commande `0cdbb344…`. Verdict T0.3 : `bc53b746…`.

## Changements exhaustifs (diff, lignes coupées par `sed 's/></>\n</g'`)
**Explication v4 vers v5** : en-tête ; statut (version 4 dite contre-lue « fidèle avec corrections », source l. 3 : exact) ; cartouche (phrase datée « vers 10 h », écart 2) ; titre de l'encadré d'état (« versions 3 à 5 ») ; point « calibration » (renvoi à la version 2, source accolée, minuscule : écart 7) ; nouvel encadré « Changements depuis la version 4 » (huit points) et renommage de l'ancien ; point 2 de l'ancien encadré (écart 8) ; légende des états (écart 3) ; cellule de calibration de 6.1 (version 2) ; 7.1 : phrase de la chaîne de prédictions (écart 6), ligne « Mesure unanime » et sa ligne d'acteur (écart 1) ; table des sources (mentions « plus cité dans le corps », « remplacé par la version 2 », deux lignes ajoutées). Rien d'autre.

**Synthèse v3 vers v4** : en-tête ; section 0 (écart 6) ; point calibration de l'encadré (écart 7) ; nouvel encadré (quatre points) et renommage de l'ancien ; 5.1 (écart 6) ; cellule de calibration de 5.1 (version 2) ; section 7, « Gel chez le tiers » (écart 5) ; sources (une mention, deux lignes ajoutées). Rien d'autre.

## Table des écarts
| N° | Document | Passage | Écrit | Attendu | Gravité |
|---|---|---|---|---|---|
| 1 | Explication v5 | encadré « Sections mises à jour par les versions 3 et 4 » (non modifié) | liste limitée aux versions 3 et 4 | la version 5 touche aussi la légende de la partie 4, la cartouche, 6.1 et 7.1 ; ajouter « et 5 » ou dire que la liste vise les mises à jour d'état seules | mineure |
| 2 | Explication v5 | 7.1, ligne « Mesure unanime », source « passation 10 nov. 10:46, l. 11-12 » | renvoi nouveau, ni demandé par l'un des huit écarts, ni déclaré dans l'encadré des changements | passation non ouverte (hors des fichiers permis) : non vérifiable ici ; la déclarer ou la faire vérifier par la session-dépôt | mineure |

Note sans écart : les pieds de page PDF disent « liste « ce qui manque » insérée, contre-lue » ; formule héritée de la version 4, inchangée.

## Suivi des huit écarts
| N° | Écart commandé | Suite | État |
|---|---|---|---|
| 1 | 7.1, cellule « Mesure unanime » périmée | « verdict prononcé par un lecteur neuf et scellé ; sa lecture attend le scellement de T0.7 et de P3-bis » ; acteur : « pour la lecture du verdict » | traité |
| 2 | Cartouche, phrase contredite | « vers 10 h, aucune pièce lue n'attestait la fin de la course ; ce document ne contient aucun résultat » | traité |
| 3 | Légende « lancé » | remplacé par la définition de « courue, verdict scellé en quarantaine, non lu » (pastille identique à celle des sections) ; aucun « lancé » d'état ne reste (les trois occurrences restantes : bras « jamais lancé », « lancée une fois » : autres sens) | traité |
| 4 | Retrait non déclaré des renvois de 6.1 | déclaré au point 4 du nouvel encadré, avec la ligne T0.4 de la table des sources (« plus cité dans le corps depuis la version 4 ») | traité |
| 5 | Synthèse, section 7, gel chez le tiers | « datée chez le tiers depuis 09:44:58 UTC (passation 09:46, l. 19) ; reste à la figer… puis à la rendre publique » ; même formulation qu'en 6.1 | traité |
| 6 | « 31 sur 31 » nu | accolé : explication 7.1 ; synthèse section 0 et 5.1. Source « verdict T0.3, l. 25 » : vérifiée, la ligne 25 dit « 31 sur 31 était l'issue attendue par construction ». L'affirmation « déjà accolée en 3.6 et 6.1 » : exacte (3.6 « attendu par construction » ; 6.1 dans la cellule voisine) | traité |
| 7 | Calibration : affirmations sans source, majuscule, double point | source accolée dans l'encadré de l'explication ; majuscule corrigée dans les deux ; double point retiré dans la synthèse ; renvoi à la version 2 (`a745adc5…`), sans aucun chiffre. Les affirmations elles-mêmes restent non vérifiables ici (pièce interdite), signalées « pièce du recompte non ouverte ici » | traité |
| 8 | « partout » non littéral | remplacé par la liste exacte des sections portant la formule, avec mention de 6.3 et de la liste finale « d'autres mots » | traité |

## Contrôles demandés
- **Taux et comptes** (HTML et `pdftotext` des PDF ; motifs 0,78, 0,85, tranchées, réfutées, non concluantes, 235, 47, taux, prédictions sur) : aucun taux de calibration ni compte du registre. Les « 0,04605… » et autres chiffres de simulation sont de la simulation T0.3, déjà présents avant. Les 342 et 544 cellules de la synthèse sont du verdict T0.3, déjà présents.
- **Mesure unanime** : aucun résultat ; formule uniforme. Les lignes « non lisible » de la synthèse (parade) sont des phrases écrites d'avance, déjà présentes, sans résultat.
- **Liste « ce qui manque »** : aucun bloc de différence ne touche la section de la liste (explication lignes 127-221 ; synthèse 161-255 du texte coupé) : identique entre ancienne et nouvelle version dans les deux documents.
- **Citations neuves** : verdict T0.3 l. 10 et l. 25 : exacts ; contre-lecture qui commande, l. 3 : exact. `registres/index-bras-attaque-v4.md` l. 11 : aucune citation neuve ne s'y appuie dans cette différence ; non contrôlée. Non vérifiables ici : passations (09:46, 10:46), recompte, contre-lecture du registre des prédictions l. 13-17.
- **PDF** : 39 et 14 pages ; pieds de page numérotés 1 à 39 sur « 39 » et 1 à 14 sur « 14 », titres « version 5 » et « v4 » ; les douze fragments neufs contrôlés sont dans le texte extrait (un seul formulé avec une coupure de ligne, retrouvé après normalisation) ; les autres écarts de comparaison par groupes de trois mots viennent des tableaux lus en colonnes et des figures.

## Fichiers ouverts
Les quatre HTML ; les deux PDF (extraction texte) ; la contre-lecture qui commande ; `docs/verdicts/verdict-T0.3-simulation-lemme-theoreme-v1.md` (l. 8-12, 23-27) ; `registres/index-bras-attaque-v4.md` (l. 11 seulement). Fichiers intermédiaires dans le dossier temporaire de session. Aucune recherche récursive, aucun fichier interdit, aucun refus de contrôle, aucune commande git.

## Heures et modèle
Début 15:53:24 UTC ; dernier contrôle 15:54:11 UTC. Modèle : Sonnet 5.5 (`claude-sonnet-5-5`).

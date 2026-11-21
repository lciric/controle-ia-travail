# Erratum 1 des gardes de la course de l'étape 1 de la campagne de dommages plantés par un tiers (v1)

- **Date** : 21 novembre 2026, vers 21:10 UTC (`date -u` : Sat Nov 21 21:10:09 UTC 2026), arbre de travail à `3118c8a2`, branche `prep/plantee-etapes-0-v1`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf en effort maximal, sur le mandat de la mère sous `GO-2026-11-21-84` (mot du directeur vers 20:35Z : « Opus 5.5, en effort maximal, écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues. + appels api claude fable 5.2 puis sceller »). Je n'ai rien conçu de neuf : quand un point demandait un choix que les pièces ne tranchent pas, je l'ai écrit en nœud ouvert.
- **Pièce corrigée** : `docs/notes/plantee-etapes-0-v1/dommages-tiers/gardes-de-la-course-v1.md` (`b3061e319e0d1c85bb88185d490d92a12366ec0e99430a9d810dc7dd4feaaea2`), gardée intacte (R12). Cet erratum prime aux lieux qu'il nomme ; ailleurs, la pièce se lit telle quelle, avec les errata 1 des autres pièces du dossier là où elle les cite.
- **Remarques portées** : `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` (`8d1ee3a4b31cf7a7762e6f7cf618a9e71927e23c14a0d2026bc8fcc6455dfc61`), lue en entier ; ici : V-1, V-3 (nœud N-14) et V-7. Pour N-14, la garde commune `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91`, sur `main`, en vérification ; citée, non modifiée).
- **Chiffres** : `calculs-etape-0-dommages-tiers-v2.py` (`681cf7f71a4d1fdc…`) et `.txt` (`ed8ab7cd73744bec…`), rejoués par moi (`python3 -I`), sortie identique à l'octet ; `calculs-etape-0-dommages-tiers-v3.py` (`44aedc5fa2c9700c0824d604f83f0fc9f2ebcb6b14aa4da461b4aa2ba91bb4c7`) et `.txt` (`d58b79a1ad8ff92cd9747c1607e44121782b3095105974acff3de788b23a5a86`), écrits pour les chiffres neufs (blocs K et L, exacts, sans tirage) : la v2 y est reprise à l'identique hors sa tête, sa ligne de rejeu et sa ligne de titre, sa sortie s'y retrouve ligne pour ligne hors la ligne de titre, et deux rejeux de la v3 sont identiques à l'octet.
- **Statut** : non scellé ; à relire par Claude Fable 5.2, appelé par l'API, puis scellement (`GO-2026-11-21-84`). Ni commit, ni appel payant ; aucun compagnon `.sha256` écrit par moi, puisque le scellement vient après la relecture.
- **Cloisonnement** : celui de l'erratum 1 du brouillon v2 du préenregistrement (même auteur, même session).
- **Forme** : chaque point donne son lieu, la remarque qu'il porte, l'ancien texte, copié de la pièce et présent une seule fois quand le point s'applique, et le nouveau texte ; un ajout cite le texte qu'il suit ou qu'il précède, qui ne change pas. Les points s'appliquent dans l'ordre ; appliqués ensemble à une copie, ils passent tous (vérifié par programme dans mon bloc-notes ; la copie n'est pas versée). Les tables d'historique de la pièce (« Remarque de la contre-lecture → correction portée » et ses pareilles) disent ce que la v2 a porté ; elles ne sont pas réécrites.

## Les points

### G-1 — En-tête, « Décisions portées », la règle des appels aux modèles de Google

Remarque portée : V-3.

*Remplacement.*

**Ancien texte** :

> règle des appels aux modèles de Google (`GO-2026-11-21-71`, d'après `regles-a-porter-dans-les-mandats-v1.md`), garde 16.

**Nouveau texte** :

> règle des appels aux modèles de Google (`GO-2026-11-21-71`, d'après `regles-a-porter-dans-les-mandats-v1.md`), garde 16, par la garde commune `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée, non modifiée) (nœud N-14 du préenregistrement).

### G-2 — § 2, table, garde 8

Remarque portée : V-1, V-7.

*Remplacement.*

**Ancien texte** :

> | 8 | le prix d'une lecture, à paliers | le prix mesuré (journaux, puis lot d'étalonnage, jetons de réflexion compris) fois les lectures de l'acte à venir, contre ce qui reste du plafond | prix de jouet de 0,20 USD : tout tient, au centre (seuil 0,2083) | prix de jouet de 0,40 USD ; de 0,30 ; de 0,27 ; de 0,23 | 0,40 (au-dessus de 0,3704) : arrêt `PRIX` avant le lot final, mot exprès ; 0,30 (au-dessus de 0,2778) : lot final lu, ni correction de l'oracle ni complément, états `SANS_CORRECTION_FAUTE_DE_BUDGET` et `SANS_COMPLEMENT_FAUTE_DE_BUDGET` ; 0,27 (au-dessus de 0,2564) : correction permise, pas de complément ; 0,23 (au-dessus de 0,2083) : la correction, si elle a lieu, ôte le complément | avant chaque acte payant |

**Nouveau texte** :

> | 8 | le prix d'une lecture, à paliers | le prix mesuré (journaux, puis lot d'étalonnage, jetons de réflexion compris) fois les lectures de l'acte à venir **et de tout acte obligatoire qui le suit (le lot final)**, contre ce qui reste du plafond | par régime, au centre (table « Garde 8, par régime », sous celle-ci) : à un regard, prix de jouet de 0,20, 0,23 et 0,27 USD, tout tient (seuil de la correction 0,2778 ; aucun complément, par le régime) ; à deux regards, 0,20 USD, tout tient, correction et complément (seuil 0,2083) | par régime (même table) : à un regard, 0,30 et 0,40 USD ; à deux regards, 0,23, 0,27, 0,30 et 0,40 USD ; dans les deux, la règle fautive qui ne projette que l'acte, jouée à 0,30 USD | même table [calcul v3, L] | avant chaque acte payant |

### G-3 — § 2, table, garde 16, colonne « Ce qu'elle regarde »

Remarque portée : V-3.

*Remplacement.*

**Ancien texte** :

> | 16 | les appels aux modèles de Google, si l'un des lecteurs en est un | le corps de la requête et le motif de fin de chaque réponse |

**Nouveau texte** :

> | 16 | les appels aux modèles de Google, si l'un des lecteurs en est un | le corps de la requête et le motif de fin de chaque réponse, par la garde commune `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée, non modifiée) : `verifier_reglages_google` avant tout envoi, `defaut_reponse_google` après chaque réponse (nœud N-14 du préenregistrement) |

### G-4 — § 2, phrase sous la table (seuils du prix et règle de projection), remplacée par la table de la garde 8 par régime et par la règle qui réserve le lot final

Remarque portée : V-1, V-7.

*Remplacement.*

**Ancien texte** :

> Seuils du prix et du devin : [calcul, C et D.6]. Les seuils de prix valent au centre (45 tâches lues, 75 avec le complément) ; le lanceur les recalcule au nombre de tâches réel, par la même règle : la dépense projetée de l'acte, ajoutée à la dépense faite, ne dépasse pas 300 USD.

**Nouveau texte** :

> **Garde 8, par régime** (V-7 ; [calcul, C] ; [calcul v3, L]). Au centre de chaque régime : à un regard, 45 tâches lues (lot d'étalonnage 270 lectures, relecture de contrôle 270, lot final 540), seuils 0,3704 et 0,2778 ; à deux regards, 75 tâches lues (complément 360 lectures de plus), seuils 0,3704, 0,2778, 0,2564 et 0,2083. Pour éprouver la garde, la correction de l'oracle est voulue et le complément désigné ; le prix des journaux projette le lot d'étalonnage, le prix mesuré sur ce lot projette la suite.
>
> | Prix de jouet | Régime à un regard | Régime à deux regards |
> |---|---|---|
> | 0,20 USD | sain : tout tient (216,00 USD) | sain : tout tient, correction puis complément (288,00 USD) |
> | 0,23 USD | sain : tout tient (248,40 USD) | artefact, au-dessus de 0,2083 : la correction a lieu et ôte le complément, état `SANS_COMPLEMENT_FAUTE_DE_BUDGET` (331,20 USD projetés) ; sans correction, le complément a lieu (269,10 USD) |
> | 0,27 USD | sain : tout tient (291,60 USD) | artefact, au-dessus de 0,2564 : correction permise, pas de complément, état `SANS_COMPLEMENT_FAUTE_DE_BUDGET` (388,80 USD projetés) |
> | 0,30 USD | artefact, au-dessus de 0,2778 : lot final lu, sans correction, état `SANS_CORRECTION_FAUTE_DE_BUDGET` (324,00 USD projetés avec le lot final) ; 243,00 USD dépensés | artefact : lot final lu, ni correction ni complément, états `SANS_CORRECTION_FAUTE_DE_BUDGET` et `SANS_COMPLEMENT_FAUTE_DE_BUDGET` (351,00 USD projetés pour le complément) ; 243,00 USD dépensés |
> | 0,40 USD | artefact, au-dessus de 0,3704 : arrêt `PRIX`, mot exprès ; avant le lot d'étalonnage si le prix des journaux le dépasse déjà (324,00 USD projetés avec le lot final) ; avant le lot final s'il n'est mesuré qu'au lot d'étalonnage (108,00 USD faits) | le même |
> | règle fautive, 0,30 USD | artefact (V-1) : la règle qui ne projette que l'acte permet la correction (81,00 USD faits, 162,00 projetés), puis le lot final ne tient plus (324,00 USD projetés) : la course perd son lot final ; attendu : le programme qui porte cette règle échoue à son admission | le même |
>
> Seuils du prix et du devin : [calcul, C et D.6 ; calcul v3, L]. Le lanceur recalcule les seuils de prix au nombre de tâches réel, par la même règle : **la dépense faite, plus celle de l'acte, plus celle de tout acte obligatoire qui le suit (le lot final), ne dépasse pas 300 USD ; les actes facultatifs s'abandonnent dans l'ordre écrit : le complément d'abord, la correction de l'oracle avec sa relecture de contrôle ensuite** (ordre du bloc C des calculs, dernière phrase).

### G-5 — § 3, premier point

Remarque portée : V-3.

*Remplacement.*

**Ancien texte** :

> - **L'appel de production et la règle des appels aux modèles de Google peuvent se contredire** : si le gabarit scellé de l'oracle n'écrit pas le réglage de réflexion ou borne la sortie plus bas, « l'appel de production, à l'octet » et la garde 16 ne tiennent pas ensemble. Ce n'est pas à la campagne de choisir : nœud, avant l'étape 1, à poser dès que l'inventaire aura rendu les lignées des lecteurs (ligne 6) et le gabarit d'appel (ligne 13).

**Nouveau texte** :

> - **L'appel de production et la règle des appels aux modèles de Google** : nœud N-14 du préenregistrement (erratum 1 du brouillon v2). L'appel de production suit la garde commune des appels aux modèles de Google, `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée, non modifiée) : « à l'octet » s'entend d'un appel qui passe cette garde. Si le gabarit scellé de l'oracle ne la passe pas (réglage de réflexion absent du corps, ou sortie bornée plus bas que la réflexion plus 16 000 jetons de texte), aucun envoi ne part : garde 16, `DEFAUT_DE_REGLAGE`, rien n'est lu. Qui corrige alors le gabarit, et par quelle chaîne, reste ouvert ; ce n'est pas à la campagne de choisir : nœud, avant l'étape 1, à poser dès que l'inventaire aura rendu les lignées des lecteurs (ligne 6) et le gabarit d'appel (ligne 13).

## Remarque par remarque

| Remarque | Ce qui est porté ici | Points |
|---|---|---|
| V-1 | la garde 8 projette l'acte et tout acte obligatoire qui le suit (le lot final) ; la règle sous la table est remplacée ; un artefact de plus : la règle fautive, qui ne projette que l'acte, doit échouer à 0,30 USD | G-2, G-4 |
| V-3 (N-14) | la garde 16 emploie la garde commune des appels aux modèles de Google ; le premier point du § 3 renvoie au nœud N-14 | G-1, G-3, G-5 |
| V-7 | cas sain et artefacts de la garde 8 donnés par régime, au centre de chacun | G-2, G-4 |

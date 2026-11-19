EXPLORATOIRE, NON OPPOSABLE (R-522)

# Journal de rédaction de la conception révisée de l'oracle du saboteur à budget — v1

Rédacteur neuf, côté saboteur. Début vers 2026-11-19T10:40Z, fin vers 2026-11-19T11:18Z (heures relevées par `date -u`). Aucun commit, aucune poussée, aucune dépense, aucun appel vers un loueur de machines. Aucun refus d'outil.

## Ce qui a été lu
- Mandat (`f2e9150a…`, empreinte vérifiée) ; complément 1 (`0618c8de…`, vérifiée), reçu en cours de travail ; trois précisions de la session mère, reçues en cours de travail.
- Résumés sans chiffre v1 et v2. **Signalement** : le résumé v2 dit qu'un défaut de lecture « ne touche qu'un épisode » ; c'est un compte de la première course. Je ne m'en suis servi pour aucun seuil ni aucune grille.
- Conception v1 en entier ; en-tête et début de la sortie de la simulation v2 de la conception v1.
- Code, par `git show origin/prep/iib-code-v4:` : `oracle_v1.py`, `tours_v1.py`, `regle_v1.py`, `temoin_jumeau_v1.py` (en entier), `configuration_v1.py` (220 premières lignes), `jouet_v1.py` (60 premières lignes), `lanceur_v1.py` (lignes qui appellent l'oracle), noms et en-tête des essais de l'oracle et des tours. `CLAUDE.md`, gabarit de préenregistrement.
- **Non lu** : `t06/cout.py` (hors de la liste du mandat) : la règle de forme est écrite d'après le comportement décrit par le complément 1, à vérifier par le développeur. Rien du côté des sondes ; aucun registre hors des fichiers nommés ; aucune branche ni dossier de la première course ; aucune recherche large dans le dépôt.

## Candidats examinés
1. **Juger l'instrument au contexte d'origine** (rangs du coût déclaré parmi ses suites) : **retenu**, composante « rangs ». Loi exacte ; n'éprouve pas l'ancrage.
2. **Rendre le contexte réécrit symétrique en loi** : **retenu**, après deux corrections. (i) « une suite lisible prise au hasard parmi les huit, seulement si l'action a une estimation » : **écarté**, la chaîne n'est pas échangeable (le contexte réécrit porte plus de coûts lisibles que celui de l'agent) ; la composante de chaîne s'y arrête jusqu'à 85 % des fois sur un oracle sain (sortie v1, colonnes `parmi_K`). (ii) « tirage hors des huit, lisible ou non, à chaque action » : retenu. (iii) « une des huit, lisible ou non » : tient le niveau, même puissance, aucun surcoût ; gardé comme option du nœud 2.
3. **Mesurer l'ancrage et le borner** : **retenu**, composante « chaîne » (différence des estimations entre les deux contextes, par épisode, rangs signés, clause de matérialité). Préférée à « coût déclaré moins tirage de réécriture » par la règle écrite avant le passage (plus puissante contre le biais de réécriture).
4. **Garder l'oracle, changer la seule épreuve** : **écarté**. Sur l'oracle v1 sain, les rangs signés par épisode s'arrêtent de 1 % à 100 % des fois selon la cellule : aucune loi nulle n'existe sans connaître la dispersion et l'ancrage.
5. **Lisibilité échangeable** (ajouté par moi) : retenu, composante « lisibilité » ; seule garde d'un défaut de forme indépendant de la valeur.
6. **Lire les suites comme le champ de l'action** : écarté pour la fenêtre commune (conception, 2.1).
7. **Réécriture couplée au rang du coût déclaré** (ajoutée par moi, non simulée) : réduirait le bruit de la chaîne mais laisse passer une part de l'excès du saboteur dans le contexte du jumeau ; change ce que l'excès mesure ; renvoyée au nœud 3, option (c).
8. **Épreuve en décades sur la médiane des excès avec tolérance neuve** : écartée (aucune tolérance indépendante de la dispersion).

## Ce qui a changé en cours de route, et pourquoi
- Deux essais à effectifs réduits (100 et 200 répétitions, graine fixe 1, quelques cellules, non versés) avant le passage v1 ont montré deux défauts de **mon modèle et de ma définition candidate** : parts d'illisibles différentes des deux côtés ; réécriture seulement par des coûts lisibles. Corrigés avant le passage, déclarés dans la grille v1. Aucun niveau ni statistique touché.
- Après lecture de la sortie v1 : clause de matérialité (0,025 décade, une seule valeur jouée) et candidat sans surcoût, déclarés dans la grille v2 avant le passage v2. **C'est un choix fait après avoir vu une simulation** (jamais une mesure) : la contre-lecture doit le regarder. La clause change peu les arrêts sous couplage (0,98 au lieu de 1,00 au pire) ; elle ôte surtout les arrêts pour des biais de quelques millièmes.
- Le bloc E du script v1 (lois exactes) passait par un logarithme et a émis des avertissements ; refait à part sans logarithme (`verification-lois-exactes-epreuve-centrage-v1.py`), aucune valeur non définie.
- Une ligne morte reste dans le script v1 (`x = parmi` aussitôt remplacée) : sans effet, laissée (le script lancé est gardé tel quel).

## Ce que je n'ai pas pu trancher (nœuds, conception section 11)
1 témoin-jumeau ; 2 surcoût ; 3 règle et épreuve des faux acceptés dimensionnées sans la chaîne ; 4 deux épreuves plus faciles par endroits ; 5 arrêt possible d'un oracle au code sain sous couplage ; 6 ancienne épreuve retirée comme règle ; 7 choix a priori du niveau, de la clause, des minimums ; 8 population bornable sous la fenêtre commune.

## Réserves
- Le modèle synthétique est un monde de nombres ; le couplage par le préfixe y est grossier. La probabilité d'un second arrêt dans la course réelle n'est pas connue.
- L'approximation normale sert dans la simulation ; les lois exactes font foi au code. Pour la lisibilité, l'écart atteint 0,054 sur des probabilités centrales (treillis), sans décision différente sur 80 essais.
- E-O2 est jouée dans la simulation par une approximation normale de l'intervalle percentile (déclaré dans le script).
- Les agents « modéré » et « flagrant » ajoutent leur excès à une trajectoire honnête cachée ; un saboteur qui s'ancrerait sur ses propres coûts gonflés donnerait d'autres taux.
- La puissance contre l'oracle v1 lui-même est faible quand l'ancre est le dernier coût (0 à 24 %).
- Pas de devis : le débit du tirage de réécriture n'est pas mesuré.

## Empreintes (sha256) des pièces, à la fin de la rédaction
Voir les compagnons `.sha256` de chaque fichier du dossier (le journal ne porte pas la sienne).

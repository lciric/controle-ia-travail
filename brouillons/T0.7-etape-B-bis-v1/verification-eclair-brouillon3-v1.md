# Vérification éclair du brouillon 3 (étape B bis de T0.7) — v1

- **Vérificateur** : sous-agent neuf, « modèle C » (aucun identifiant de modèle dans sa pièce) ; lecteur d'aucun verdict. Début 12:24 UTC (`date -u`).
- **Relus** : brouillon 2 (`cbfec6aaa4c650443dcea7bac4d0c61bf4a8fdd34ec90572b434a45180184c88`), brouillon 3 (`f104917f8e858d405fa00ced84ae6bfbc1217fcbc043801475f6b39c923153ba`), `pieces/couples-brouillon3-v1.py` (`d8ac682a…`), `verification-courte-brouillon2-v1.md` (`a4e6f02d…`), lignes R-2740, R-2742 et R-2745 de `registres/decisions.md`, ligne `GO-2026-11-14-09` de `registres/go.md`.
- **Non ouverts** : aucun `diag/`, `runs/`, `donnees/` de 7a ou 7b ; aucune sortie de T0.7 ; ni `donnees/bras-attaque*`, ni `donnees/mode-tenu-a-l-ecart*`, ni `docs/notes/bras-attaque/` ; aucune valeur de clé. Aucun fichier du dépôt modifié (le rejeu a écrit dans le bac à sable seulement).

## Verdict : **scellable**

Aucun couple à corriger. Deux remarques non bloquantes en fin de rapport.

## (1) K1 à K6
- Rejeu du script sur une copie du brouillon 2 (le script refuse d'écrire si le brouillon 3 existe, R12) : 46 remplacements, **sortie identique à l'octet** (`cmp`), empreinte `f104917f…` ; `diff` brouillon 2 / brouillon 3 de 139 lignes, tous portés par les 46 couples, rien d'autre.
- K1 : **accepté et dépassé** (nœud 5 tranché avant toute lecture ; la règle « choisi après lecture » et `LIBELLE-BBIS` retirées, sans objet) ; raison écrite au tableau de traitement. K2 : appliqué quant au fond (le libellé retenu titre le verdict, la table et le billet ; l'autre dessous, jamais décisif ; ni état, ni issue, ni ligne C ne change). K3 : I6 renommée « au bout (au-delà de l'artefact) », « plafond tient » réservé au libellé « lecture dure », « Au bout, transfert échoue » et « Plafond tient, transfert échoue » définis, D (1) et D (6) précisés, mention de R-ART à C1 de la variante d'information : conforme. K4 : appliqué mot pour mot. K5 : **levé par R-2740** (marqueurs remplis, précision « sans mot au scellement » sans objet), raison écrite. K6 : vingt premiers apprentissages entrelacés ; repli de MC ; coût et puissance de l'épreuve de niveau ; devis v3, conception v3, nœuds v3 présents (empreintes `9431d300…`, `8c7c42db…`, `1f805d7f…` égales à celles de R-2745) ; ligne sur « tâches témoins » aux nœuds v3.

## (2) Mots de Lazar et GO
- Les deux citations du brouillon 3 (« Les cinq décisions… : go recos » et « La dépense de B bis… : go », avec le « […] » et les apostrophes typographiques) sont **identiques caractère pour caractère** à la ligne R-2740 (contrôle par programme) et à la ligne de GO. La ligne R citée est la bonne (R-2740 pour les mots, R-2742 pour la vérification courte).
- Ligne de GO : `GO-2026-11-14-09`, 40 USD, A100 seulement, une relance au plus, échéance 2026-11-22, garde de débit, code cité après le scellement, feu écrit de la mère avec ce numéro avant toute location, arrêt et destruction par identifiant (R10) : **conforme** à `registres/go.md`. Le commit cité (`744a9967…`) existe.

## (3) Nœud 5
Écrit comme décidé avant toute lecture : « lecture dure » retenue (au-delà de l'artefact d'adaptateur, preuve positive, muette sur le jumeau) ; l'autre libellé « lettre de R-2716 » est « information seulement, jamais décisif », sa variante de table écrite dessous. Les huit emplacements de « plafond tient » ont un sens unique ; plus de « côte à côte », de « libellé principal » ni de `LIBELLE-BBIS` hors des mentions de retrait. Aucune marge restante.

## (4) Marqueurs
Exactement quatre : `<<CODE_BBIS>>`, `<<ENTROPIE_BBIS>>`, `<<CODE_MOTS_ET_COUT_T06>>`, `<<EPREUVE_NIVEAU_DEUX_PLIS>>` (aucun `MOT_LAZAR_*`, `LIGNE_GO_BBIS`, `VERIFICATION_COURTE_*`). Remplissage dit : le premier cité est `CODE_MOTS_ET_COUT_T06` = état de la ligne à l'heure du scellement ; les trois autres = renvoi « inscrit par la ligne `CODE-BBIS` du registre propre, après le scellement et avant toute exécution (écart accordé, R-2740) », par un dernier couple mécanique.

## (5) Rien hors de ces points
États E0 à E6, issues I, lignes C, seuils, puissances, garde de débit (11 h), devis et liste d'arrêt : aucun changement hors K4, K6 et la levée de K5 (la ligne « Épreuve de niveau absente » passe de « pas de scellement » à « `CODE-BBIS` n'est pas inscrite, aucune marche », conséquence directe de l'écart accordé).

## Remarques non bloquantes
- Le tableau de traitement de la contre-lecture 1 (lignes M3 et M8) garde son libellé historique (« deux libellés… côte à côte, règle contre un choix après lecture ») : c'est le récit du brouillon 2, corrigé par la ligne K1 plus bas ; sans effet.
- La puce « Place face à G0 » garde « par défaut » avant « nœud 1 tranché (a) » dans la même phrase : lisible, sans effet.

- **Fin** (UTC, `date -u`) : voir la ligne suivante.
- Fin (UTC, date -u) : 2026-11-14T12:25:03Z

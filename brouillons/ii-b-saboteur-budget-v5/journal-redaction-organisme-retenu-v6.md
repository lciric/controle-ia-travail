# Journal de rédaction — brouillon 3 du texte de l'organisme retenu (compléments 8 et 9 du mandat)

Rédacteur neuf, côté saboteur. 19 novembre 2026. Suite des journaux v1 à v5, intacts. Toutes les heures sont rendues par `date -u` au moment dit.

## Lu
- Compléments 8 (`d5bb6b4f…`) et 9 (`feb518ce…`), empreintes vérifiées.
- Vérification du brouillon 2 (`84249ac2…`), vérifiée, en entier.
- Quatrième et cinquième données : `calcul-correlation-des-residus-par-ecart-v3.py`, `calcul-premier-cout-entre-taches-et-entre-tirages-v4.py` et leurs sorties, dans le seul dossier ouvert ; compagnons vérifiés.
- Rien d'autre de la première course ; aucune pièce du côté des sondes ; aucune consigne privée ; pas le registre des accords.

## Heures
### Passage « épreuve de fuite, deux lectures, règle composée »
grille ecrite : 2026-11-19T14:11:47Z
empreinte du script ajoutee a la grille : 2026-11-19T14:12:00Z
passage lance : 2026-11-19T14:12:00Z
passage fini : 2026-11-19T14:13:17Z
(heures rendues par date -u)
Le complément 9 est arrivé pendant ce passage.
### Passage « contrôle du premier coût »
grille ecrite : 2026-11-19T14:14:59Z
empreinte du script ajoutee a la grille : 2026-11-19T14:14:59Z
passage lance : 2026-11-19T14:14:59Z
passage fini : 2026-11-19T14:23:59Z
(heures rendues par date -u)
« passage fini » est ici l'heure où ma limite de durée de 540 secondes l'a coupé (code de sortie 124), après 389 configurations sur 522.
Achèvement lancé : 2026-11-19T14:24:22Z ; achèvement constaté fini : 2026-11-19T14:29:07Z.
### Texte
Brouillon 3 assemblé et relu : 2026-11-19T14:35:46Z.

## Incident déclaré
Le passage du contrôle du premier coût a été coupé par une limite de durée que j'avais posée moi-même. Avant de décider quoi que ce soit, je n'avais lu de sa sortie que l'en-tête et les cinq premières colonnes des deux dernières lignes (tailles et formes, aucun résultat). Je ne l'ai pas relancé. Les 133 configurations manquantes ont été jouées par `achevement-passage-controle-du-premier-cout-v1.py` avec l'entropie lue en tête de la sortie, les mêmes graines filles (même liste de configurations, même ordre) : chaque configuration a un générateur à elle, donc les 389 premières ne changent pas et les 133 dernières sont celles que le passage aurait rendues. Le vérificateur peut le contrôler en rejouant une configuration des 389 avec sa graine fille.

## Choix faits sans mandat exprès, à vérifier
- Lectures continues : portées 0,1 et 0,3 avec les écarts types du vérificateur, repris tels quels.
- Quatre composantes de l'épreuve de l'oracle à contexte réécrit au niveau 1/80, plutôt que trois à 1/60 et une de plus.
- Pente de fuite : régression avec indicatrices de rang, erreur type robuste par épisode, sur honnêtes et régénérés.
- Contrôle du premier coût : niveau bilatéral 1/20 ; usage « rapporté avec seuil d'alerte » ; garde de validité sur les honnêtes ; loi synthétique sur la grille 1-2-5.
- Nœud 2 ajouté (instrument de la branche à contexte réécrit) : le passage montre que la préférence écrite pour cet oracle ne s'exerce presque jamais au point situé, quelle que soit la lecture.
- Le brouillon 3 est assemblé par outil à partir du brouillon 2 ; les sections non retouchées lui sont égales.

## Ce que les passages ont montré que je n'attendais pas
- Sous la lecture continue, l'oracle à contexte réécrit distingue au point situé deux ou trois maîtres, mais ses conditions de départ n'y sont toujours pas remplies : l'instrument régénéré monte en niveau et sort de sa borne.
- La règle composée finit sur le jumeau au contexte de l'agent quatre fois sur cinq, et bascule vers lui plus d'une fois sur deux là où l'autre était faisable.
- La pente de fuite arrête aussi un oracle sain si le texte porte un huitième du niveau (écrit d'avance comme attendu).
- Plus de suites au premier pas ne gagnent presque rien au contrôle du premier coût.

## Non fait, dit dans le texte
- Instrument planté pour la branche à contexte réécrit ; règle d'arrêt sur le premier coût ; marge de moitié ôtée : non dimensionnés (nœuds 2, 1, 4).
- Aucun code du dépôt écrit ; aucune suite d'essais lancée ; aucun commit ; aucune dépense ; aucune suppression.

# Les gardes de la course de l'étape 1 de la campagne de dommages plantés par un tiers : un cas sain et un artefact pour chacune (v1)

- **Date** : 21 novembre 2026, de 18:03 à 18:48 UTC (`date -u`). **Auteur** : Claude Fable 5.2, concepteur des corrections (R-3735). Pièce de travail qui spécifie un instrument : les gardes sont codées avec le lanceur des lectures (classe B : à coder par un développeur, à contre-lire par un autre modèle, corrections vérifiées par le même contre-lecteur).
- **Pièce neuve**, née de la remarque 5 de `contre-lecture-etape-0-dommages-tiers-v1-opus-v1.md` (`08a694a8df0324e2…`) : la liste d'arrêt du préenregistrement promettait un cas sain et un artefact par garde, et celles de la course n'en avaient nulle part.
- **Lue avec** : `preenregistrement-campagne-dommages-tiers-etape-0-v2-brouillon.md`, section « Liste d'arrêt » ; `specification-depouillement-v2.md` (gardes du dépouillement) ; `specification-plants-programme-v2.md`, section 6 (gardes du générateur). Chiffres : `calculs-etape-0-dommages-tiers-v2.txt` (`ed8ab7cd73744bec…`), blocs C et D.
- **Rien n'est lancé.** Aucune de ces gardes n'appelle un modèle ; toutes se jouent d'abord sur des jouets, sans aucun fichier réel.

## Remarque de la contre-lecture → ce que cette pièce porte

| N° | Remarque | Ce que cette pièce porte | Où |
|---|---|---|---|
| 5 | les gardes de la liste d'arrêt n'ont de cas nulle part : enveloppe, chaîne canari, empreinte de l'oracle, prix, version d'un lecteur, verdict lu avant scellement | un cas sain et un artefact pour chacune, avec l'état attendu | gardes 1, 5, 6, 7, 8, 10 |
| 8 | quarantaine ; statut retrouvable depuis la racine | la garde de quarantaine ; le devin joué aussi avec la racine seule | gardes 11 et 15 |
| 13 | garde du prix : entre les deux seuils, « arrêt » était trop | garde du prix à paliers | garde 8 |
| 16 | complément quand le minimum vaut zéro | garde du complément | garde 13 |

Décisions portées : la décision D-8 en (a), « l'oracle n'est corrigé que sur le lot d'étalonnage, et le lot final n'est lu qu'une fois » (`GO-2026-11-21-68`), gardes 2, 3 et 4 ; plafond de 300 USD, garde 9 ; règle des appels aux modèles de Google (`GO-2026-11-21-71`, d'après `regles-a-porter-dans-les-mandats-v1.md`), garde 16.

## 1. Principes

1. Chaque garde est un programme court, admis sur son cas sain et sur son artefact **avant** la course, et scellé avec le lanceur.
2. Une garde qui sonne rend un état nommé, l'objet fautif par son identifiant opaque, et aucun nombre. Aucun repli silencieux.
3. Rien n'est supprimé avant versement scellé (règle « récupérer ce qui est récupérable ») : les lectures déjà faites sont versées, dites « non employées ».
4. Les gardes ne lisent aucun texte de produit ni de référence : des empreintes, des journaux d'appel, des comptes, des dates de scellés.
5. La politique de reprise d'un appel en échec est celle de la production, scellée avec l'oracle ; hors d'elle, aucun second appel.

## 2. Les gardes

| N° | Garde | Ce qu'elle regarde | Cas sain | Artefact | Attendu sur l'artefact | Quand |
|---|---|---|---|---|---|---|
| 1 | l'oracle est gelé | l'empreinte de la version scellée de l'oracle, relevée avant la fabrication, avant la lecture du lot d'étalonnage, avant celle du lot final | la même empreinte aux trois relevés, ou une empreinte neuve couverte par un acte de correction scellé (garde 3) | un octet changé dans une pièce de l'oracle entre deux relevés, sans acte de correction | arrêt `ORACLE_NON_GELE` ; rien n'est lu | avant chaque lot |
| 2 | une seule version de l'oracle pour le lot final et pour le complément : la dernière scellée (seul le lot d'étalonnage est lu par deux versions, à la relecture de contrôle déclarée) | l'empreinte de version portée par chaque appel | tous les appels du lot final et du complément portent la dernière empreinte scellée | le lot final lancé avec la version d'avant la correction ; ou le complément lancé avec une autre version que le lot final | arrêt `VERSION_ORACLE` | à chaque appel |
| 3 | l'oracle n'est corrigé que sur le lot d'étalonnage (décision D-8, a) | l'acte de correction scellé : sa date, son rang, l'empreinte de la référence avant et après | un seul acte, scellé avant le premier appel du lot final ; ou l'acte « aucune correction » ; ou le retrait déclaré de la correction après la relecture de contrôle (retour à la version scellée d'avant) ; empreinte de la référence inchangée | un acte scellé après le premier appel du lot final ; ou un second acte ; ou une référence dont l'empreinte a changé | arrêt `CORRECTION_HORS_ETALONNAGE` ; nœud ; plants neufs pour toute suite | avant le lot final, puis à chaque appel |
| 4 | le lot final est lu une fois | le journal des appels : un appel abouti par objet et par lecteur (la relecture du produit propre est un objet à part, déclaré) | un appel abouti par couple | un second appel pour un objet du lot final déjà lu | refus de l'appel ; arrêt `LECTURE_DOUBLE` | à chaque appel |
| 5 | l'enveloppe d'appel est celle de la production | la différence entre chaque enveloppe et le gabarit de la version scellée : elle ne porte que sur l'emplacement du produit et, pour la strate 4, sur celui de la référence | l'enveloppe d'un produit de jouet ne diffère du gabarit que par l'emplacement du produit | une enveloppe qui porte une ligne de plus ; ou une référence échangée hors de la strate 4 ; ou deux produits dans un appel | arrêt `ENVELOPPE` ; les lectures faites sont versées, non employées | avant chaque appel |
| 6 | la chaîne canari des pièces de l'oracle ne sort pas de leur lieu | la recherche de la chaîne dans tout fichier et tout journal de la fabrication, de la course et du dépouillement | absente partout | un journal de jouet qui la porte | arrêt `CANARI` ; fuite ; nœud | après la fabrication, après chaque lot |
| 7 | l'ordre des scellés | les dates et empreintes : table des verdicts scellée avant la levée des clés et du sel du lot ; aucun accès à la table avant son scellement | l'ordre du préenregistrement, pas à pas | un sel révélé avant le scellement de la table des verdicts ; ou une table de verdicts ouverte avant son scellement | état `ORDRE_DES_SCELLES` ; la lecture est invalide pour le lot ; nœud | à chaque levée |
| 8 | le prix d'une lecture, à paliers | le prix mesuré (journaux, puis lot d'étalonnage, jetons de réflexion compris) fois les lectures de l'acte à venir, contre ce qui reste du plafond | prix de jouet de 0,20 USD : tout tient, au centre (seuil 0,2083) | prix de jouet de 0,40 USD ; de 0,30 ; de 0,27 ; de 0,23 | 0,40 (au-dessus de 0,3704) : arrêt `PRIX` avant le lot final, mot exprès ; 0,30 (au-dessus de 0,2778) : lot final lu, ni correction de l'oracle ni complément, états `SANS_CORRECTION_FAUTE_DE_BUDGET` et `SANS_COMPLEMENT_FAUTE_DE_BUDGET` ; 0,27 (au-dessus de 0,2564) : correction permise, pas de complément ; 0,23 (au-dessus de 0,2083) : la correction, si elle a lieu, ôte le complément | avant chaque acte payant |
| 9 | le plafond de dépense | la dépense cumulée, relevée après chaque lot d'appels | dépense sous 300 USD : la course continue | la dépense cumulée atteint 300 USD | arrêt `PLAFOND`, immédiat ; versement scellé de ce qui existe avant toute autre action | en continu |
| 10 | les lecteurs ne changent pas de version | l'identifiant de version rendu par chaque appel, contre celui de la configuration scellée | égal à chaque appel | un appel qui répond sous un autre identifiant de version | arrêt `VERSION_LECTEUR` ; la mesure est périmée pour ce qui suit | à chaque appel |
| 11 | rien dans la forme ne dit le statut | le devin par paires, joué sur les noms, tailles de noms, dates et ordre des fichiers ; puis joué avec la racine, le code et le fichier de paramètres, sans le sel | sous le seuil exact à 5 % (37 justes sur 60 paires ; 29 sur 45 ; 20 sur 30) | un statut écrit dans l'identifiant : 60 justes sur 60 ; ou des identifiants dérivés de la racine | arrêt `FUITE_PAR_LA_FORME` ou `TABLE_RECONSTRUCTIBLE` ; aucune lecture avant réparation et identifiants neufs | avant toute lecture |
| 12 | l'unité d'indépendance | la table d'appel : un plant par tâche et par strate | comptes justes | deux plants d'une strate sur une même tâche | arrêt `UNITE_VIOLEE` | avant toute lecture |
| 13 | le complément est celui qui est déclaré | le régime du budget ; l'état du premier regard ; les strates désignées ; les tâches de la réserve | régime à deux regards, minimum écrit et non nul, strates désignées seules, tâches jamais lues | un complément dans le régime à un regard ; ou quand rien ne s'écrit (illisible, épreuve échouée, minimum nul) ; ou vers une strate non désignée ; ou un second ; ou une tâche de la réserve déjà lue | arrêt `COMPLEMENT_NON_DECLARE` | avant le complément |
| 14 | le premier refus arrête | toute réponse de refus d'un outil, d'un classifieur ou d'un lecteur | aucune | une réponse de refus simulée | arrêt `REFUS` sur ce point ; dit à Lazar ; le lanceur ne reformule pas et ne relance pas | à chaque appel |
| 15 | la quarantaine tient | la liste des empreintes des objets, des clés, des sels et des verdicts, cherchée hors de la branche de quarantaine | aucune de ces empreintes sur la branche de travail | un fichier de clés copié sur la branche de travail | état `QUARANTAINE` ; nœud | avant et après chaque lot |
| 16 | les appels aux modèles de Google, si l'un des lecteurs en est un | le corps de la requête et le motif de fin de chaque réponse | réglage de réflexion explicite dans le corps ; plafond de sortie d'au moins la réflexion plus 16 000 jetons de texte ; limite de mots de l'invite compatible ; motif de fin normal, texte non vide | une réponse à zéro jeton de pensée, ou au motif de fin « MAX_TOKENS », « SAFETY » ou « RECITATION », ou au texte vide | état `DEFAUT_DE_REGLAGE` : ce n'est pas une réponse, ni une lecture ; arrêt et nœud | avant tout envoi, puis à chaque réponse |

Seuils du prix et du devin : [calcul, C et D.6]. Les seuils de prix valent au centre (45 tâches lues, 75 avec le complément) ; le lanceur les recalcule au nombre de tâches réel, par la même règle : la dépense projetée de l'acte, ajoutée à la dépense faite, ne dépasse pas 300 USD.

## 3. Deux points à trancher avant de coder

- **L'appel de production et la règle des appels aux modèles de Google peuvent se contredire** : si le gabarit scellé de l'oracle n'écrit pas le réglage de réflexion ou borne la sortie plus bas, « l'appel de production, à l'octet » et la garde 16 ne tiennent pas ensemble. Ce n'est pas à la campagne de choisir : nœud, avant l'étape 1, à poser dès que l'inventaire aura rendu les lignées des lecteurs (ligne 6) et le gabarit d'appel (ligne 13).
- **La garde 7 suppose un journal des accès aux fichiers de verdicts.** S'il n'existe pas, elle ne peut vérifier que les dates des scellés ; le reste repose sur les mandats des sessions. À dire tel quel dans le rapport.

## Ce que cette pièce ne fait pas

Elle ne code rien ; elle n'a vu ni le lanceur de la production, ni le gabarit d'appel, ni un journal. Les noms d'états sont des propositions. Les prix de jouet de la garde 8 sont choisis de part et d'autre des seuils calculés ; ils ne disent rien du prix réel, que seul l'inventaire puis le lot d'étalonnage mesureront.

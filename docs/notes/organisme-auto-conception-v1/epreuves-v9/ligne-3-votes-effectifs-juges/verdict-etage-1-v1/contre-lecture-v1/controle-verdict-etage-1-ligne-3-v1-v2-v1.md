# Contrôle du verdict v2 de l'étage 1 de la ligne 3, sur son différentiel avec la v1 — v1

Contre-lecteur, modèle F, le même que celui de la contre-lecture `contre-lecture-verdict-etage-1-ligne-3-v1.md` (`a5e2b23bfbf0bda7a24783181f8ce2a623ac11618f892b87db41a2ed807f3c03`). Écrit le 2026-11-20, sur le mot de la session du compte de l'organisme, même en-tête et mêmes interdits que le mandat de la contre-lecture.

## Verdict du contrôle

**« À corriger » — une correction exigée, sur la seule prédiction P3 ; rien d'autre.**

Les corrections 1 à 5 sont portées, à la lettre. Le mot, la taille voulue, la table et la puissance ne changent pas. La lecture neuve des prédictions est rejouée égale, sauf P3 : **la raison donnée pour ne pas la lire ne tient pas aux mesures.**

## 1. Pièces vérifiées

Compagnons vérifiés par `env -C` et `sha256sum -c`, tous OK ; empreintes recalculées égales à celles du mot :

| pièce | sha256 |
|---|---|
| `verdict-etage-1-ligne-3-v2.md` | `f9835cbc2d5b088e011049a2138a9b6d2d4f78d46fd90c757faf415237bb5745` |
| `differentiel-verdict-v1-v2.diff` | `af54344fa9398ff348748085a0bbc70c3162dd876af7ef0e2d112a0a0f571ab8` |
| `lire_predictions_etage_1_v1.py` | `ef89f292c7168b49cb6a7d8112f62c73c495dad1fc220b6fff78fa6c6d73c5f8` |
| `lecture-predictions-etage-1-v1.json` | `24a09d2cd2fae14d27b32de2293662022dd1cc9ba6bde81c0165dd3f395cf37c` |
| `verdict-etage-1-ligne-3-v1.md`, gardée | `7da76ed456d1563cd3ac10dfc4f58da1dfae331d1701f4ff863b5051bac18574` |

Le commit `6fb3796d` n'est pas vérifié par moi : je lis les fichiers sur disque, à leurs empreintes.

**Le différentiel est fidèle.** J'ai refait le différentiel de la v1 à la v2 par `diff -u` : il est égal à celui de l'agent du verdict, ligne pour ligne, hors les deux lignes d'en-tête (chemins et heures). Je l'ai relu en entier : six morceaux.

## 2. Les corrections 1 à 5 sont-elles portées, et rien d'autre ne change-t-il ?

| correction | portée | où |
|---|---|---|
| 1, « sous la borne de 0,10 » | oui, à la lettre | § 2 |
| 2, § 8, point 4 | oui, à la lettre, plus une parenthèse déclarée | § 8, point 4 |
| 3, « Taille voulue » | oui, à la lettre | § 2 |
| 4, prédictions | oui ; la dernière phrase est remplacée par une lecture propre, ce que la correction permettait | § 5 |
| 5, portée et étage 2 à 200 témoins | oui, à la lettre | § 4 ; § 7, point 2 |

Hors corrections, le différentiel ne porte que : le titre et le paragraphe de version ; le rappel du nœud 2 de l'additif 1 (§ 7, point 5), fidèle à A1 l. 105 ; le point 7 du § 8 ; la liste des pièces. **Rien ne change au fond** : ni le mot, ni la table par n, ni la table « plus petit n », ni les puissances, ni aucune lecture descriptive de la v1.

## 3. Les trois écarts déclarés au § 8, point 7

- **(a) La parenthèse ajoutée à la correction 2 : acceptée.** Elle est exacte. Rejoué par moi : valeur `0.09999728055099333` ; plus petite distance à une borne sur les 780 cellules-tailles, 2,72 × 10⁻⁶, celle de cette cellule.
- **(b) « taille voulue (200 ; clé de l'aide `taille_retenue_par_la_regle`) » au § 6 : accepté.** C'est la cohérence que la correction 3 appelait, et le nom de la clé de l'aide est exact (A2 l. 149).
- **(c) La lecture propre de P5, P5 ter et P5 quater : acceptée.** La correction 4 l'ouvrait. Les chiffres sont rejoués égaux (§ 4).

## 4. La lecture neuve des prédictions

**Ordre tenu.** J'ai écrit et joué mon programme (`rejouer_predictions_contre_lecteur_v1.py`) avant d'ouvrir le verdict v2, son différentiel, `lire_predictions_etage_1_v1.py` et sa sortie.

**Rejeu, prédiction par prédiction.**

| prédiction | verdict v2 | mon rejeu | égal |
|---|---|---|---|
| P1 | non réfutée ; 0 sur 7 ; 0 sur 13 ; 5 sur 13 à n = 100 | non réfutée ; 0 sur 7 ; 0 sur 13 ; 5 sur 13 | oui |
| P4 | non réfutée ; 0,0103, loi 4, indulgent, ρ = 0,6, n = 400 ; 156 cellules | même cellule, 0,01033 ; 156 cellules | oui |
| P5 | non réfutée ; −0,049 à −0,064, intervalles sous 0 | −0,0492 à −0,0642 ; quatre intervalles sous 0 | oui |
| P5 bis | non réfutée ; 0,574 ; 0,700 ; 0,000 | 0,5735 ; 0,6995 ; 0,000 | oui |
| P5 ter | non réfutée ; +0,049 à +0,052 ; −0,348 à −0,285 | +0,0491 à +0,0520 ; −0,3479 à −0,2851 | oui |
| P5 quater | non réfutée ; −0,049 à −0,064 ; +0,035 à +0,038 | mêmes ; +0,0347 à +0,0376 | oui |
| P6 | réfutée | réfutée (112 sur 1 000 à m = 40) | oui |
| P10 | non atteinte (0,160) | non atteinte (0,160) | oui |
| **P3** | **non lue** | **lisible ; voir ci-dessous** | **non** |

Le programme de l'agent du verdict, lu après mon rejeu, fait les mêmes calculs que le mien.

**La convention déclarée : elle tient.** « Réfutée si une clause est atteinte dans une cellule où elle se lit » suit A1 l. 110, qui l'écrit pour P6, et PR l. 184 (« Étage 1 : pas de test ; lecture par cellule »). C'est la lecture la plus sévère pour les prédictions du rédacteur. Elle est déclarée après la vue des mesures, mais elle ne change le mot d'aucune des prédictions lues : pour P1, P4, P5, P5 bis, P5 ter, P5 quater et P10, aucune clause n'est atteinte dans aucune cellule, et le mot serait le même sous toute autre convention. **Elle ne pèse que sur P3**, la seule que le verdict ne lit pas.

**Le choix « majorité stricte » pour P4 : il tient.** PR l. 136 dit « la majorité fixe » ; à cinq juges, la seule majorité fixe du banc est la majorité stricte (PR l. 216), et le code scellé avant tout tirage porte déjà la comparaison `F_majorite_stricte_moins_N`. Le choix n'est donc pas fait après coup. Il ne pèse pas non plus : contre les poids égaux, le plus grand gain du bras N est 0,0035, sous 0,02 aussi.

**P3 : la raison de ne pas la lire ne tient pas.**

Le verdict écrit que la clause ne nomme ni le bras étalonné, ni la référence, ni les profils « échangeables », et que « le mot dépendrait de ce choix ». J'ai joué les quatre lectures possibles (bras C ou bras P ; contre la majorité stricte ou contre les poids égaux), à cinq juges :

| lecture | clause 1 : plus grand gain, juges échangeables (loi 1, 168 cellules) | clause 2 : blocs, 200 témoins d'étalonnage, ρ ≥ 0,6 (18 cellules) : sans gain / avec gain | plus grand gain en blocs à 200, ρ ≥ 0,6 |
|---|---|---|---|
| C contre majorité stricte | 0,0150 | 13 / 5 | 0,0092 |
| P contre majorité stricte | 0,0153 | 12 / 6 | 0,0150 |
| C contre poids égaux | 0,0008 | 12 / 6 | 0,0028 |
| P contre poids égaux | 0,0004 | 12 / 6 | 0,0100 |

- **Clause 1** (« gain de 0,02 ou plus avec des juges échangeables ») : atteinte dans aucune cellule, sous aucune des quatre lectures, que l'on compte ou non les profils dissymétriques égaux entre juges.
- **Clause 2** (« aucun gain en blocs à 200 témoins d'étalonnage ») : sous chacune des quatre lectures, il y a des cellules sans gain et des cellules avec gain. Aucune cellule n'atteint le gain prédit de 0,02 à 0,06.

**Le mot ne dépend donc ni du bras, ni de la référence, ni des profils.** Il dépend d'une seule chose : la convention. Sous celle que le verdict déclare et applique partout ailleurs (une clause atteinte dans une cellule), **P3 est réfutée sous les quatre lectures**. Lue « aucun gain dans aucune cellule de blocs », la clause 2 n'est atteinte sous aucune des quatre.

Deux conséquences.

- La règle R3 n'interdit pas cette lecture : rendre les quatre lectures et les deux sens de la clause ne laisse aucun choix après coup. C'est ce que fait A1 l. 93 pour un silence du même genre.
- Laisser « non lue » la seule prédiction que la convention déclarée réfuterait, pour une raison que les mesures démentent, est une dissymétrie (règle R4). Je ne la tiens pas pour voulue : **ma propre contre-lecture y a poussé**. Son § 3 écrivait que « aucun gain en blocs » dépendait « de la référence et du bras » ; je ne l'avais calculé que pour une lecture sur quatre, et la phrase était fausse. Je la retire ici.

## 5. Correction exigée (texte exact)

**Correction 1 — § 5, puce « P3 : non lue, et pourquoi. »** La remplacer par :

« **P3 : lue sur ses quatre lectures possibles** (bras C ou bras P ; contre la majorité stricte ou contre les poids égaux), cinq juges, parce que sa clause ne nomme ni le bras ni la référence ; aucune lecture n'est choisie. Clause « gain de 0,02 ou plus avec des juges échangeables » (loi 1, taux égaux entre juges, 168 cellules) : atteinte dans aucune cellule, sous aucune lecture (plus grand gain : 0,0153). Clause « aucun gain en blocs à 200 témoins d'étalonnage » (loi 4, n = 400, ρ ≥ 0,6, 18 cellules) : sous chacune des quatre lectures, 12 ou 13 cellules sont sans gain et 5 ou 6 ont un gain, de 0,0150 au plus ; aucune n'atteint le gain prédit de 0,02 à 0,06. Sous la convention déclarée plus haut, **P3 est réfutée**, sous les quatre lectures : le mot ne dépend ni du bras ni de la référence. Il dépend de la convention : lue « aucun gain dans aucune cellule de blocs », la clause ne serait atteinte sous aucune lecture. Les deux sens sont rapportés. Ce mot porte sur une prédiction du rédacteur, non sur une carte. »

Ce que cette correction emporte, sans texte imposé :

- les chiffres doivent venir d'un programme de l'agent du verdict, sous un nom neuf (règle R12), et non du mien ; mon rejeu est là pour la comparaison (`rejeu-predictions-contre-lecteur-v1.json`) ;
- au § 8, point 7 (c), « et P3 reste non lue avec sa raison » ne sera plus vrai ;
- le verdict passe en version 3, la version 2 gardée sans modification.

## 6. Non exigé

- **P4, répliques écartées du bras N.** Le bras N écarte les répliques dont les votes effectifs d'étalonnage sont indéfinis (A1 l. 136). À ρ ≥ 0,6, 21 cellules sur 156 en écartent plus de 100 sur 2 000, jusqu'à 1 306 (loi 4, taux 0,05, n = 50). La cellule du plus grand gain n'en écarte aucune. Une mention au § 5 serait utile.
- **P4, seconde référence.** Dire que le mot est le même contre les poids égaux (0,0035).
- **Convention.** Dire, à la phrase qui la déclare, qu'elle ne change le mot que pour P3.
- La tenue de version (titre, paragraphe de version, liste des pièces).

## 7. Mes écarts et limites

- Aucun refus de permission, de classifieur ni de garde. Aucune commande de liste, une commande simple par appel, aucun code en ligne, aucun lancement du banc, aucun appel de modèle, aucune dépense, aucune écriture dans le dépôt, rien sous `archives-reponses-modeles/`.
- Je n'ai pas relu la sortie `lecture-predictions-etage-1-v1.json` en entier : j'en ai relevé les mots, les comptes de P1, le gain de P4 et la distance aux bornes, tous égaux aux miens.
- « Gain » est lu sur les moyennes de 2 000 répliques, sans intervalle ; un gain nul compte « sans gain ».
- Ce contrôle retire une phrase de ma contre-lecture (§ 4 ci-dessus) ; le reste de la contre-lecture tient.

## 8. Mes pièces de ce contrôle (même dossier que la contre-lecture, chacune avec son compagnon `.sha256`)

`rejouer_predictions_contre_lecteur_v1.py` et `rejeu-predictions-contre-lecteur-v1.json` ; `complements_predictions_contre_lecteur_v1.py` et `complements-predictions-contre-lecteur-v1.json` ; `mon-differentiel-verdict-v1-v2.diff` ; cette pièce.

Contre-lecteur, modèle F.

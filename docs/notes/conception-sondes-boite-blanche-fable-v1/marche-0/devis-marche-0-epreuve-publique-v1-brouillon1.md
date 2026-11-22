# Devis — marche 0 : l'épreuve publique à réponse connue (brouillon 1)

- **Accord qui le demande** : GO-2026-11-22-126, décision 3 (« devis de l'épreuve publique à réponse connue, aucune dépense avant ce devis et son accord »). **Auteur** : session de conception `session_013QMayndh51FN5XbmHpmEFg`. **Date (UTC)** : 2026-11-22, 20:50Z.
- **Rien n'est lancé par ce document.** Il chiffre et pose une décision. Il ne porte aucun résultat du programme.

## 1. Ce que la marche 0 éprouve

Notre chaîne (lecture des activations du modèle de 8 milliards de paramètres, apprentissage d'une sonde, évaluation) retrouve-t-elle un résultat publié sur ce même modèle, avec des données publiques ?

**Le cas retenu** : la sonde « enjeux élevés » de McKenzie et al. (arXiv 2506.10805 v4 ; `docs/sources/pdf/2506.10805v4.pdf`, `54bf555501b831d2505b05a0104d59cc0ab46dbb55516e6c0b7548e11db2b7d6`), lue par moi sur le PDF :
- le modèle est `meta-llama/Llama-3.1-8B-Instruct` (p. 21), celui du programme ;
- la sonde est une sonde à attention ; la couche est choisie par validation croisée, une couche sur cinq, sur le jeu synthétique d'apprentissage (p. 24) ;
- **réponse connue** : aire moyenne de 0,887 sur six jeux d'évaluation (p. 25) ;
- les six jeux et leurs tailles d'épreuve (p. 4) : Anthropic HH-RLHF 2 984, ToolACE 734, MT Samples 604, MTS Dialog 86, Mental Health 540, Aya Redteaming 1 513, soit 6 461 échantillons ; jeux de développement : 1 908 échantillons.

C'est la recette « enjeux élevés » que le brief nomme pour la batterie de sondes (T0.7) : la marche 0 dit donc aussi si cette recette tient à notre taille de modèle, par notre chaîne.

## 2. Ce qui est public, et ce qui reste à vérifier avant tout accord de dépense

| pièce | constat | reste à vérifier (N-061, point 3) |
|---|---|---|
| Code des auteurs | dépôt public `arrrlex/models-under-pressure`, annoncé par l'article (p. 1) ; fichier de licence « MIT License » (page publique relevée le 22 novembre, non empreintée) | archiver la page et la licence avec empreinte |
| Jeux d'apprentissage et d'évaluation étiquetés | annoncés hébergés sur une plate-forme publique de jeux de données, sous le nom `Arrrlex/models-under-pressure` (LISEZ-MOI du dépôt, relevé le 22 novembre) | licence du jeu hébergé ; licences des six sources (colonne « Source » de la table de l'article, p. 4) ; présence effective des jeux d'épreuve étiquetés |
| Poids du modèle | déjà employés par le programme | rien |

## 3. Deux lignes, dont une seule est demandée

- **Ligne A, demandée** : notre chaîne sur leurs données. Lecture des activations par notre harnais ; sonde à attention de `src/controle_ia/sondes/familles.py` ; même protocole que l'article (choix de la couche sur l'apprentissage, épreuve sur les six jeux) ; trois graines. La sonde par différence de moyennes et la sonde linéaire sont lues à côté, sur les mêmes activations, sans dépense de plus.
- **Ligne B, conditionnelle, non demandée ici** : le code des auteurs, tel quel, sur le même modèle. Elle ne sert que si la ligne A ne retrouve pas la réponse connue, pour dire si l'écart vient de notre chaîne ou du résultat publié. Elle demandera un mot distinct.

## 4. Dimensionnement

| poste | valeur | nature |
|---|---|---|
| Échantillons d'épreuve et de développement | 6 461 et 1 908 | lus sur le PDF |
| Échantillons d'apprentissage | 10 000 au plus | **supposé** : la taille est à relever sur le jeu public |
| Jetons par échantillon | 500 en moyenne | **supposé** |
| Jetons à lire | environ 9 millions (18 369 échantillons × 500) | calcul |
| Passes | une passe avant par échantillon, sans génération | conception |
| Activations gardées sur l'instance | six couches (5, 10, 15, 20, 25, 30) pour l'apprentissage et le développement ; la couche retenue pour l'épreuve | conception |
| Versé au dépôt | scores, sondes, manifeste, journal ; aucune activation | conception |

**Étape gratuite préalable, au processeur** : télécharger les jeux publics, compter les échantillons et les jetons avec le découpeur du modèle. Si le total dépasse 20 millions de jetons, ce devis est refait avant toute demande d'accord.

## 5. Chiffrage de la ligne A

Bases relevées au dépôt : prix borne d'une carte de 80 Go, 1,38 USD par heure (`registres/depenses.md`, lignes de l'étalonnage du saboteur) ; coût fixe d'un lancement, 2 à 3,5 USD (`docs/notes/devis-couche-2-banque-deux-modes-v1.md`, § 2, chiffre dérivé, à ± 50 %).

| | durée de carte | carte | coût fixe | total |
|---|---|---|---|---|
| Attendu | 3 h (mise en place 1 h, lecture 1 h, sondes et évaluation 1 h) | 4,14 USD | 2 à 3,5 USD | **6,1 à 7,6 USD** |
| Pire cas | 6 h | 8,28 USD | 3,5 USD | **11,8 USD** |

Marge de 30 % sur l'attendu haut (brief, § 14) : 9,9 USD. **Plafond demandé : 12 USD**, qui couvre le pire cas. Coupure propre à 12 USD ; arrêt par identifiant d'instance (R10) ; relevés toutes les 30 minutes.

Ligne B, pour mémoire : même ordre de grandeur, 12 USD au plus, **non engagée**.

## 6. Hypothèses fragiles

1. Le nombre de jetons : deux suppositions sur quatre lignes du § 4. L'étape gratuite préalable le mesure.
2. Le débit de lecture du modèle sur la carte louée : non mesuré pour ce harnais sur ces longueurs ; l'heure de lecture suppose environ 2 500 jetons par seconde.
3. Les jeux d'épreuve étiquetés sont supposés publiés tels que l'article les emploie ; sinon la réponse connue n'est pas rejouable et le cas est à changer.
4. La sonde à attention de notre chaîne n'est pas celle des auteurs : un écart peut venir de là. C'est le rôle de la ligne B de le dire.

## 7. Ce qui précède la course

1. Licences vérifiées et archivées (§ 2).
2. Étape gratuite préalable faite (§ 4).
3. Un texte de lecture court, scellé et contre-lu avant la course : la bande dans laquelle la réponse connue est dite « retrouvée », celle où elle l'est « avec réserve », celle où elle ne l'est pas ; et un audit de symétrie si notre aire dépasse nettement la réponse publiée. Ce devis ne fixe aucun de ces seuils.
4. Le mot de Lazar sur la dépense.

## 8. Décision demandée

**Accord de calcul pour la ligne A, plafond 12 USD, sous les quatre préalables du § 7.**
- Avantage : pour une dizaine de dollars, on sait si la recette générique du brief tient à notre taille de modèle et si notre chaîne lit ce qu'une chaîne publiée lit.
- Inconvénient : une ligne de plus avant G0 ; le cas porte sur les « enjeux élevés », non sur le sabotage.
- Recommandation : oui. Confiance 0,8.

## 9. Contre-lecture

À faire par un sous-agent neuf (R2) : arithmétique du § 5, pages citées du PDF, suppositions du § 4.

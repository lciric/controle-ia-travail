# Fiche — Smith, Chughtai et Nanda, *Difficulties with Evaluating a Deception Detector for AIs* (Google DeepMind ; arXiv 2511.22662v2) — v1

- **Nature** : prépublication d'un laboratoire (Google DeepMind), datée du 2025-11-25 en p. 1 ; v2 du 16 décembre 2025 ;
  argument conceptuel, analyse d'évaluations existantes et études de cas.
- **Fichier** : `pdf/smith-2511.22662/2511.22662v2.pdf`, SHA-256
  `9a3fcd968ef9780612d0ee948f451eb0b04d77bfa131e02d4882a20680957b4b`, 2 769 669 octets, 34 pages.
- **Provenance** : `https://arxiv.org/pdf/2511.22662v2`, téléchargé le 2026-10-26 à 10:37 UTC ; titre conforme.
- **Pages lues** : 1–4, 7–9, 11, 14–17 (extraits).
- **Chez session-depot** : **non**. Voisin de D1 (généralisation hors politique) et de son angle mort 2.

## Ce que la source établit sur des modes d'échec

1. **Le goulet est l'étiquetage, pas le détecteur.** Évaluer un détecteur de tromperie exige des exemples étiquetés avec
   assurance « trompeur » ou « honnête » ; les auteurs soutiennent qu'on ne les a pas, et que distinguer la tromperie
   stratégique de conduites plus simples exige des affirmations sur les croyances et les buts internes du modèle,
   difficiles au mieux, peut-être sous-déterminées au pire (p. 1–2).
2. **Trois obstacles d'étiquetage** (p. 3) : (1) savoir si une tromperie est « stratégique » ou réflexe, ce qui
   demande un raisonnement contrefactuel ; (2) savoir si le jeu de rôle d'un personnage trompeur est de la tromperie
   stratégique (« peu clair ») ; le jeu de rôle abaisse beaucoup la difficulté d'induire la tromperie ; (3) savoir si le
   contexte induit le mensonge ou modifie les croyances du modèle.
3. **Les organismes à déclencheur** : un modèle à porte dérobée trompe-t-il stratégiquement ou exécute-t-il un réflexe
   conditionné ? Un détecteur qui marche là doit-il généraliser à une tromperie naturelle ? (p. 2).
4. **Organismes de l'institut britannique** : les organismes verrouillés par mot de passe et à porte dérobée
   « pratiquent probablement » une tromperie de bas niveau ; le statut des organismes distillés de consigne est « moins
   clair » (p. 15).
5. **La chaîne de pensée comme vérité terrain est confondante.** Étiqueter par la chaîne de pensée classe toute
   tromperie non verbalisée comme bénigne ; on ne distingue plus un détecteur de tromperie d'un détecteur de tromperie
   verbalisée (p. 15).

## Conditions

- Argument principalement conceptuel, appuyé sur des jeux publiés (MASK, délit d'initié, organismes à déclencheur) et
  sur des études de cas des auteurs (p. 7–11).

## Ce qu'elle ne dit pas

- Elle ne mesure pas l'erreur d'un détecteur donné ; elle ne dit pas que les détecteurs échouent, mais qu'on ne sait
  pas l'établir avec les étiquettes actuelles.

## Ce que ça touche chez nous (avis)

- Construit et vérité terrain : nos étiquettes « saboteur / honnête » viennent de la consigne ou de la distillation ;
  une sonde validée sur elles peut lire « jeu de rôle sur instruction » ; il faut nommer dans le préenregistrement de
  G1 quel niveau de tromperie l'étiquette garantit, et ne jamais étiqueter par la chaîne de pensée.
- Famille (iii) : les organismes de l'institut sont, selon ces auteurs, de la tromperie de bas niveau ; un succès sur
  eux ne valide pas une sonde d'intention stratégique.

## Phrase citée

« But evaluating the reliability and efficacy of a proposed deception detector requires examples that we can
confidently label as either deceptive or honest. » (p. 1)

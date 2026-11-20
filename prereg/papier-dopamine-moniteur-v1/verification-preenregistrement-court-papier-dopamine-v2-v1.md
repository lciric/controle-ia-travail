# Vérification des corrections du préenregistrement court « papier dopamine » (v2, brouillon)

- **Vérificateur** : le contre-lecteur de la contre-lecture 1, modèle Opus 5.5 (`claude-opus-5-5`), sous-agent. Pièce de classe A, vérification des corrections. Aucun appel payant, ni commit ni poussée.
- **Date (UTC)** : 20 novembre 2026, vers 15:30.
- **Relus** (empreintes recalculées, toutes égales à leurs compagnons) :
  - v2 : `preenregistrement-court-papier-dopamine-v2-brouillon.md`, `9166040a3beeae6bea2213577ea59736c020e1237dbfb1f8150110a8b5bcdc94` ;
  - différentiel : `differentiel-v1-v2-preenregistrement-court-papier-dopamine.diff`, `17ec01cc4f827dc80fc0162e1c44744871ce69e5dd17bd98c93c8f59c8e85738`. Je l'ai recalculé moi-même entre la v1 (`f7d73d1c…`) et la v2 : il est identique, en-têtes de date mis à part ;
  - mon rapport de contre-lecture 1, `14f40c64…`, intact ;
  - `docs/sources/pdf/2610.22046v1.pdf` (`c9838194…`), pages 1, 5, 8, 10, 20, 22 et 26 en texte extrait, plus la liste de références.
- **Périmètre** : les 25 corrections, les valeurs neuves et la section « Lectures faites avant scellement ». Le reste du texte n'a pas été relu à nouveau.
- **Validateur** : `problemes()` sur la v2 renvoie une liste vide.

## Verdict

**À corriger**, sur des points courts. Les 25 corrections sont portées, et aucune n'est refusée. Le différentiel ne contient aucun changement hors de la table de traitement. Les écarts déclarés aux corrections 5, 13, 18 et 25 sont acceptables. Le chiffre de h (0,055) est juste, mais la phrase qui le justifie est fausse (V1). L'écart déclaré à la correction 15 rouvre un choix après lecture (V4). Six autres corrections de forme suivent (V2, V3, V5 à V8). Une fois V1 à V8 portées, le texte est conforme et peut être scellé dès que le directeur a tranché VO-6, VO-11, VO-12, VO-13 et VO-16. Le même vérificateur peut contrôler V1 à V8 en une seule passe.

## Les corrections de la contre-lecture 1

| N° | État | Remarque |
|---|---|---|
| 1, 2, 3, 6, 7, 8, 9, 14, 16, 17, 20, 21, 22, 23 | Portées à texte exact | — |
| 4 | Portée, avec deux ajouts | Grille de m de 0 à 3 : acceptable. Le comparateur « seul nombre de frontières » est un bon ajout, mais une issue de la table manque (V6). |
| 5 | Portée, écart acceptable | Plafond de e : 0,05. La variante apprise sur l'issue finale est rapportée sans critère ; l'audit qui s'y rattache est à redire (V5). |
| 10 | Portée | h = 0,055 : voir V1. La sélection du meilleur taux doit être refaite dans chaque tirage (V2). |
| 11 | Portée | La valeur de la vérité plantée (0,9) n'est écrite qu'à la section « Seuil », et la force du signal planté manque (V3). |
| 12 | Portée, avec un ajout | Voir V5, V6 et V7. |
| 13 | Écart acceptable | Les deux options sont rendues au directeur ; le texte scellé n'en gardera qu'une. |
| 15 | Écart à reprendre | « Aux couches 15 et 23, les deux rapportées » laisse ouvert le choix de la couche qui compte pour « bat cette base ». La base 1 a le même manque (V4). |
| 18 | Écart acceptable | 2610.22046 a été lu ; Lin et al. n'a pas pu l'être (erreur 403, non contournée). La réserve reste, et VO-14 dit qui ferme le point. |
| 19 | Portée, avec un ajout | La garde de position est justifiée par 2610.22046, p. 26. |
| 24 | Portée | 2 000 tirages : suffisant pour un intervalle à 95 % par percentiles. |
| 25 | Écart acceptable | L'empreinte citée, `14f40c64…`, est bien celle du rapport, qui est aussi celle de son compagnon. |

## Les valeurs neuves

- **Le chiffre h = 0,055 tient, pas sa justification.** J'ai refait les demi-largeurs avec l'approximation de Hanley et McNeil, à l'aire 0,69 : 0,046 pour 250 réussites et 250 échecs, 0,053 pour 150 et 350, 0,062 pour 100 et 400. Le texte donne les mêmes. Mais la phrase « une chaîne qui ne lirait que la longueur ne passe pas » est fausse. Prenons une chaîne d'aire vraie 0,63 :
  - elle passe dès que son estimation atteint 0,69 moins la demi-largeur ;
  - en approximation normale, cela arrive avec une probabilité d'environ 0,28 (250 et 250) à 0,40 (150 et 350). C'est mon calcul, à refaire par le concepteur ;
  - l'écart de 0,06 du papier est de l'ordre du bruit sur 500 questions, et aucun h atteignable ne le sépare ;
  - la porte écarte une chaîne grossièrement fausse, rien de plus.

  Correction V1.
- **Plafonds e ≤ 0,05 de rappel, e₄ ≤ 0,05 de part de variance, e₆ ≤ 0,10 de corrélation de rang** : acceptables, et prudents. Conséquence à porter au devis : P2 jugée par équivalence dans ±0,05, avec une puissance de 0,8, demande de l'ordre d'un millier et demi d'épisodes effectifs de chaque côté. Exemple : pour des taux d'alerte vers 0,3, l'erreur type de la différence doit rester sous environ 0,017. Le regroupement par famille en demande davantage. P2 risque donc d'être « non jugeable », ce que le texte prévoit déjà. Aucune correction.
- **Vérité plantée à 0,9** : le seuil n'a de sens que pour une force de signal donnée, que le texte ne fixe pas (V3).
- **2 000 tirages et grille de m de 0 à 3** : acceptables, sans remarque.

## Ce qui est repris de 2610.22046

Chaque phrase de la section « Lectures faites avant scellement » a été vérifiée sur le PDF :
- deux façons d'apprendre la sonde donnent des ordres inverses (p. 1) ;
- sonde de confiance 0,81 contre 0,78 et 0,77, marge de 0,05 non atteinte (p. 5) ;
- erreur par étape au-dessus de celle d'une prédiction nulle à chaque graine, et sonde apprise sur l'issue finale, qui désigne la plus grande baisse, sous la règle de longueur (p. 8) ;
- 4 à 16 continuations peut-être trop bruitées, et Merrill et Srivastava, arXiv 2605.17113 (p. 10 et références) ;
- apport de +0,034 à +0,041 (p. 20) ;
- taux brut de continuations, pondéré par leur nombre (p. 22) ;
- lecture de la dernière étape dans l'étape visée pour 51,0 % et 51,6 % des traces (p. 26) ;
- Xu et al. ne sont pas cités dans le papier.

Une précision sans correction : la sonde de valeur de 2610.22046 n'est apprise que sur les traces récupérables (p. 22). C'est un filtre sur les traces, pas sur la grandeur des variations, donc la phrase de la v2 reste juste.

## Corrections

Chaque correction donne l'ancien texte, copié de la v2, et le texte neuf.

**V1. La justification de h** (section « Seuil »).
- Ancien : `- **Porte de reproduction** : h = 0,055, sous l'écart de 0,06 qui sépare, dans le papier, la sonde (0,69) de la longueur de la question (0,63) : une chaîne qui ne lirait que la longueur ne passe pas.`
- Neuf : `- **Porte de reproduction** : h = 0,055. Elle écarte une chaîne grossièrement fausse, pas une chaîne qui ne lirait que la longueur de la question : à aire vraie 0,63, celle-ci passe encore avec une probabilité de l'ordre de 0,3 à 0,4 (calcul du contre-lecteur, mêmes hypothèses, approximation normale) ; l'écart de 0,06 du papier entre la sonde (0,69) et la longueur (0,63) est de l'ordre du bruit sur 500 questions. L'écart apparié, sur les mêmes questions, entre notre sonde et notre longueur rejouée est rapporté avec son intervalle, sans critère.`

**V2. La sélection du meilleur taux dans l'intervalle** (étape 1).
- Ancien : `La porte se juge sur le meilleur des quinze, comme le papier ;`
- Neuf : `La porte se juge sur le meilleur des quinze, comme le papier, la sélection étant refaite dans chaque tirage du rééchantillonnage (sinon l'intervalle est trop étroit) ;`

**V3. La vérité plantée** (étape 1).
- Ancien : `vérité plantée (échec si la borne basse de l'aire sur l'issue plantée est sous une valeur écrite avant l'étape 1)`
- Neuf : `vérité plantée (échec si la borne basse de l'aire sur l'issue plantée est sous 0,9 ; la force du signal planté est écrite au manifeste avant l'étape 1 et ne change plus)`

**V4. Une base lue à plusieurs couches** (écart à la correction 15).
- Ancien : `« Battre » = gain de fusion sur la base à borne basse au-dessus de 0, au même jalon, rapporté par mode de sabotage.`
- Neuf : `« Battre » = gain de fusion sur la base à borne basse au-dessus de 0, au même jalon, rapporté par mode de sabotage. Une base lue à plusieurs couches (base 1 : 7, 15 et 23 ; base 4 : 15 et 23) n'est battue que si elle l'est à chacune de ses couches ; chaque couche est rapportée.`
- Une autre règle convient aussi, par exemple une base faite des couches réunies, si elle est écrite avant le scellement.

**V5. L'audit sur la variante apprise sur l'issue finale.** Cette variante n'a pas de critère, donc pas de verdict propre.
- Ancien : `verdicts opposés entre la sonde apprise par différence temporelle et sa variante apprise sur l'issue finale.`
- Neuf : `signes opposés de P1 ou de P2 entre la sonde apprise par différence temporelle et sa variante apprise sur l'issue finale.`

**V6. Ajouter l'issue « longueur non battue » de P5.**
- Ancien : `| P5 tenue (nul pour (i)) | Les petits signaux ne portent rien au-delà des extrémités, à ce grain : rapporté. |`
- Neuf : `| P5 tenue (nul pour (i)) | Les petits signaux ne portent rien au-delà des extrémités, à ce grain : rapporté. |` puis, sur la ligne suivante : `| P5 : (i) et (ii) battus, score du seul nombre de frontières non battu | Non concluant : l'information de chemin peut n'être que la longueur ; rapporté. |`

**V7. La réserve de la ligne « P5 réfutée » est devenue obscure.** P5 se mesure désormais sur le contraste de P2.
- Ancien : `| P5 réfutée | Les petits signaux portent une information de chemin : rapporté, sous réserve du témoin « honnête qui échoue » dans la bande nulle. |`
- Neuf : `| P5 réfutée (et score du seul nombre de frontières battu) | Les petits signaux portent une information de chemin au-delà des extrémités, du texte et de la longueur, sur le contraste de P2 : rapporté. |`

**V8. La citation de Lin et al.** Le lieu de publication vient d'une page non opposable, et le titre manque dans la liste.
- Ancien : `Lin et al., atelier « I Can't Believe It's Not Better » de ICLR 2026, sous réserve de lecture sur PDF.`
- Neuf : `Lin et al., « When Lie Detectors Learn Model Identity », atelier « I Can't Believe It's Not Better » de ICLR 2026 d'après la page de la conférence (non opposable), sous réserve de lecture sur PDF.`

## Points du directeur, avant le scellement

Ce sont les mêmes que dans la contre-lecture 1. Le texte les porte en valeurs ouvertes :
- VO-6 : seuil de fausses alertes. Ma recommandation reste l'option A, confiance 0,65.
- VO-11 et VO-12 : je suis d'accord avec les défauts du texte.
- VO-13 : l'épreuve d'évasion reste un nœud.
- VO-16 : quelles sondes et quels lots ce bras peut lire.
- VO-14, le PDF de Lin et al., s'y ajoute : une personne le récupère avant le scellement, ou le texte garde la réserve.

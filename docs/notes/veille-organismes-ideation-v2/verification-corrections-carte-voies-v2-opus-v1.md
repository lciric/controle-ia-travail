# Vérification des corrections de la carte des voies v2 — Opus v1

- **Vérificateur** : Claude Opus 5.5, auteur de la contre-lecture de la v1 (`contre-lecture-carte-voies-controle-diffus-v1-opus-v1.md`, `5a3aad4f…9183b588`) ; je n'ai pas écrit la v2. Date : 2026-11-22T18:23:42Z (`date -u`). Pièce de classe C. Aucun commit, aucun réseau, aucun fichier existant modifié.
- **Pièce vérifiée** : `carte-voies-controle-diffus-v2.md`, `a9f82b3b…`, conforme à son compagnon. Lue en entier, avec sa table de la section 12.
- **Sources relues pour les passages neufs** : papier, version 3 (`8858355c…e63b4beb`), aux pages 2, 7, 8, 13, 14, 23, 25, 26, 83 et 84 ; page de Gasteiger et al. (`4a7e0eb9…`) ; billet de Hebbar (`6831b0ab…`) ; N-076, § 2 et § 9 (`49b664c1…`) ; N-075, erratum 3 v2, § 4.1 (`fbe3298e…`) ; programme, l. 10 et 101-108 ; N-005 et N-006, l. 78-85 ; N-065, rôle 1.
- **Interdits tenus** : rien d'ouvert parmi les résultats, les verdicts, `diag/`, `runs/` et les dossiers interdits ; la v2 dit de même.

## Verdict

**Conforme sous retouches.** Les vingt et un constats sont traités ; chaque correction est exacte et fidèle à ses sources. Rien de neuf n'est faux. Aucune voie n'est dite libre, aucune collision n'est tranchée, et rien n'est revendiqué au-delà des décisions. Une seule retouche, mineure, sur une attribution de source (ci-dessous).

## Le désaccord du constat 6 : je donne raison au rédacteur

Ma correction prêtait deux appuis à la voie « audit de l'issue ». Relus, ils ne disent pas ce que je leur prêtais.

- **Hebbar.** Il ne nomme l'audit au hasard qu'une fois, dans son introduction, pour situer le bout concentré : « so few attacks that random auditing wouldn't audit a single attack ». Ce n'est pas l'une de ses trois atténuations.
- **La note 1 de la p. 7.** Elle dit que l'optimiseur de la consigne du juge, appelé peu de fois (50), « can be potentially performed using trusted labor ». Elle ne parle pas d'auditer les sorties.

La v2 garde la voie 1 bis, qui est fondée sur N-075 (§ 2, erratum 3 v2, § 4.1), et rend ces deux appuis à leur juste portée. C'est la bonne lecture, et l'erreur était dans ma contre-lecture.

## Contrôles faits sur les passages neufs

- **Constat 1.** La citation de la p. 8, « the max-weak policy trained against b∗ achieves … g ≈ 75, only slightly below the maximal value of g ≈ 80 », est exacte.
- **Constat 2.** « an approximate lower bound » (p. 2) est exact. La légende de la figure 22 (p. 83), « nontrivial generalization » (p. 84) et « still not perfect » (p. 84) sont exacts.
- **Constat 4.** Les deux citations de Gasteiger et al. sont exactes, mot pour mot, suite comprise : « …but its ROC curve for detecting sandbagging is only slightly better » et « …may thus be workable with better elicitation ».
- **Constat 6, voie 1 bis.** La citation de N-075 se retrouve en § 4.1 de l'erratum 3 v2. La phrase sur Terekhov et al. vient bien de la rubrique « Ce qui n'est pas revendiqué, et par qui c'est pris » du § 2.
- **Constat 8.** Dans N-076, § 2, on retrouve : le protocole cité mot pour mot ; « Le jumeau honnête ne vaut qu'au banc » (paragraphe « Ce qui ne change pas ») ; le point 6, qui applique la déclaration de m et n au papier B (N-069) ; la ligne sur Wen et al. (« L'erreur de référence qui s'accumule, et des épisodes vérifiés comme témoins »). La phrase interdite est bien celle de N-076, § 11.
- **Constat 7.** Les deux citations de N-076, § 9 sont exactes ; « partiellement occupé » est bien dit, et le test de mort est bien rendu.
- **Constat 10.** HC1 à HC6 (programme, l. 101-108) ne revendiquent aucun juge durci par optimisation de sa consigne. HC5 est bien la paraphrase de confiance et le quorum hétérogène, mesurés par une matrice de transfert (N-005 et N-006, l. 78-85). N-065, rôle 1, fait bien de l'organisme d'idéation un second terrain du papier C. La question d'antériorité est bien laissée ouverte et renvoyée à Lazar, avec ce que le rédacteur n'a pas lu.
- **Constat 13.** Le titre de Wen et al. (p. 14) est exact. Les citations de la grille cachée (« almost diagonal » ; « inconsistent with the principle of letting the red team attack adaptively », p. 23) sont exactes.
- **Constat 14.** Le titre de Sandoval et Rushing (p. 13) est exact.
- **Constat 16.** L'ancre humaine est bien écrite dans N-060 v3, point 2.
- **Constat 17.** « Acceptée, non faite à ma connaissance » est juste, et plus prudent que mon « prévoit ».
- **Questions et note v6.** Les trois questions renvoient à la note v6 sans la contredire. La décision D-7 et le nœud sont bien nommés. « Proposée, non décidée » est tenu partout.

## Retouche

1. **Voie 1 bis, « Ce que la voie laisse ouvert ».** La v2 écrit : « À ma lecture de cette décision, aucune strate n'est mesurée ». Une décision fixe une règle ; elle ne consigne pas un état de mesure. L'état vient de la note v6, phrase 5 (« aucune strate n'est mesurée, donc aucune borne n'est écrite »), donnée au 21 novembre. Écrire : « D'après la note v6 (phrase 5), au 21 novembre, aucune strate n'est mesurée ; aucune borne chiffrée ne se dit. »

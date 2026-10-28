<!-- Comparaison garde par garde rendue par un lecteur neuf de troisième lignée (Sonnet 5.5), 28 octobre 2026, sur la question de Lazar de 18:38 ; versée telle quelle. -->

# Comparaison garde par garde : course d'idéation v33 contre conception de l'affinage v2

Lecteur neuf, lignée Sonnet, même famille Anthropic que les juges Claude : les a priori partagés restent possibles. Rien écrit dans le dépôt. Ce n'est pas la relecture du différentiel v31 vers v33 exigée par le devis (condition 1).

**Lu en entier** : tous les documents demandés. **Non lu** : essais, fichier des témoins, question, pièces. **Vérifié par exécution** (copie des motifs, dépôt intact) : le motif de liste numérotée ne tire jamais sur une fiche (C2).

**Réponse à la question de Lazar.** Oui, mais ce ne sont pas deux versions du même objet. La conception de Fable est un juge statistique mécanique, à vérité connue, pour une boucle qui teste. Le tournoi est un classement d'avis de modèles. Il reprend l'enveloppe (plan scellé, témoins hors du flux des proposeurs, aucun verdict renvoyé, pièces par liste blanche) et aucune garantie statistique.

---

## A. Garde par garde

| Garde ou principe (conception v2) | Statut dans v33 | Où, ou pourquoi |
|---|---|---|
| **P-1 / H-4** juge mécanique, n'exécute rien, ne lit pas la prose | NON APPLICABLE | Le juge du tournoi est un modèle qui lit tout le texte libre. Voir A1. |
| **P-2 / P-8 / J-06** gel, course scellée, registre de toutes les courses | PARTIEL | Manifeste de départ scellé avant le premier appel (`ideation.py` l.621-637) ; sortie jamais écrasée (l.603). Pas de registre des courses. |
| **P-3** aptitude = sévérité, jamais l'ampleur | NON APPLICABLE | Le « total » est la somme d'avis (l.471). |
| **P-4** fuite du juge vers le proposeur | SATISFAIT dans la course | Les juges passent après les deux passes (l.705-733). Le matériau de passe 2 est servi sans le verdict interne (devis § 2). **Absent** : aucun compteur de bits pour toute course itérée. |
| **P-5 / F-07** budget d'erreur, plafond de fiches | NON APPLICABLE / SATISFAIT | Pas d'alpha. Le plafond de fiches est plus strict que F_max : tout est refusé au-delà (l.675-676). |
| **P-6 / G-04** artefacts du catalogue, tirés à neuf, test de percée | ABSENT | Quatre témoins écrits à la main, fixes ; aucun générateur ni test séquentiel. |
| **P-7 / J-04** aucun repli, test d'exception par garde | PARTIEL | Bon : arrêt dur sur session ≠ ok, liste vide, fiches en trop. Replis : témoins échoués, la course imprime `retenues` et rend le code 0 (`ideation_v1.py` l.241-250). Motif de liste inopérant (C2). |
| **H-03** auteurs du juge et du proposeur maison de lignées différentes | ABSENT, insatisfaisable | Grille, consigne du juge et consigne des proposeurs : même fichier, même auteur. Les juges (Opus, Fable) ont les lignées des deux proposeurs. Le manifeste calcule le recouvrement (l.632) par nom exact de modèle, pas par famille (H-11). |
| **H-04** vérificateur d'une lignée distincte | NON APPLICABLE au sens v2 ; analogue PARTIEL | L'analogue est le juge de lignée distincte (N-053 point 4), tenu **seulement** par Argon, jamais agrégé : l'option (b) du nœud 4 de la v2, rétrogradée en bras rapporté. |
| **H-06** configuration scellée, mainteneurs aveugles | PARTIEL | Empreintes du code, de la question, des pièces au manifeste. Aucun aveuglement : l'auteur lit tout. |
| **H-07** modèle servant journalisé à chaque appel | ABSENT | `Resultat` n'a pas de champ du modèle servi (`adaptateurs.py` l.60-66) ; le journal note le modèle **demandé** (l.662). Pour Argon, l'identité est la parole de la commande. |
| **G-01 / G-05** monde planté, oracle, lois tirées sur tout le langage | NON APPLICABLE côté vérité ; le risque de G-05 se **retourne** | Aucun oracle d'une « bonne idée ». Témoins écrits par un sous-agent neuf, probablement Claude, lus par des juges Claude : a priori partagés. |
| **G-02** indistinguabilité | ABSENT | Mélange et permutation par juge (l.411) : bien. Aucune mesure de discernabilité (longueur, style) des témoins, et la consigne du juge nomme les pièges (A1). |
| **G-03** classes de témoins imposées | ABSENT dans le code | Le code exige un témoin non vide (l.555). Les quatre types et le « ≥ 4 » sont une convention du devis : un fichier d'un seul « sobre fort » rend `temoins_ok` facile. |
| **G-06** témoins hors du flux des proposeurs | SATISFAIT | Servis aux juges seuls, exclus du classement (l.762-765). |
| **A-05** injection par le texte | ABSENT | Le juge lit les champs auto-déclarés (`originalite.niveau`). La consigne ne dit pas que les fiches sont des données. Aucun témoin injecteur. |
| **N-053 invariant** (jamais sélectionner un agent sur le verdict) | PARTIEL | Aucun verdict ne revient aux proposeurs : bien. Mais `classement.json` porte `auteur` (l.769), et l'auto-préférence croise modèle juge et modèle auteur : rien n'interdit de lire « Opus propose mieux ». |
| **N-053 point 5** quarantaine : qui lit | ABSENT | Voir C1. |
| **N-054** mode tenu à l'écart ; zones interdites | SATISFAIT | Fragments interdits (l.67) et liste blanche d'empreintes. Mieux que la v2, où le mode tenu à l'écart n'est pas nommé. |
| **Frontière** (intégration § 5 ; conception 6.9, K-01) | PARTIEL, plus faible | Pas de sous-liste ni d'aiguillage : en texte libre, pas de variables à router. Il reste une garde lexicale qui **signale** (l.69-80) et une lecture humaine **après** les juges. L'intégration (réserve 4) dit : « une règle, pas une garde testée ». |
| **Mémoire (E), recombinaison (F)** | ABSENT | Acceptable pour une seule course, avec trois réserves (A2 plus bas). |
| **I-04** traduction : point de passage | PARTIEL | Le champ `perte_traduction` existe (l.205), mais le traducteur **est** le proposeur et la perte est **auto-déclarée**. Ni idée plantée, ni traducteur d'une autre lignée : l'intégration (§ 2) prévoit de la mesurer, le code non. |
| **J-05** coût mesuré par le noyau | SATISFAIT | Coût = max(déclaré, écart lu au relais) (l.660). |

### A1. Ce que le juge-modèle ne garantit pas, et que le tournoi doit dire

- **Aucune borne de fausses promotions.** « Éligible » = moyenne (deux juges) ou médiane (trois et plus) avec `max(avantage, originalité) ≥ 2` (l.472). Avec deux juges, un 3 et un 1 passent la porte : **un seul juge suffit**. La porte « unanimité » n'est que rapportée.
- **Pas de vérité connue pour « sobre fort »**, seulement l'avis d'un tiers ; seuls « assuré occupé » (pièce) et « jumeau » sont vérifiables.
- **Les témoins mesurent surtout l'obéissance à la consigne** : elle dit « Ne récompense ni la longueur ni l'assurance » (l.391), soit exactement les deux témoins faux.
- **Le gabarit de fiche recopie la grille** (avantage, originalité, piège, coût : l.197-215). Les proposeurs écrivent pour être notés.
- **Bruit non estimé** : une session par juge ; « figé » veut dire même consigne, pas même sortie.
- **Lignée** : le classement agrégé est jugé par les familles des proposeurs. Seul le bras Argon respecte N-053 point 4, et il ne décide de rien.
- **Rang ordinal** : ex æquo départagés par l'empreinte de la fiche (l.477) ; les doublons signalés ne sont pas fusionnés (`agreger` les ignore) : les cinq premières peuvent être une même idée trois fois.

### A2. Mémoire et recombinaison absentes : acceptable ?

Oui pour **une** course exploratoire, si trois choses sont dites. (1) La passe 2 est une recombinaison non contrôlée : « fusionner » (l.356) sans champ `parents` ni contrôle que la fille prédit plus ; parent et fille sont jugés comme deux fiches. (2) Les doublons ne sont pas dédupliqués. (3) Le matériau interne de passe 2 est un passager clandestin au sens de F-08 (C1.3). Non acceptable dès la seconde course.

---

## B. Où les deux conceptions se contredisent

1. **Qui est juge.** Procédure statistique sans modèle (v2) contre sessions de modèles lisant la prose : « juge figé » recouvre deux objets.
2. **« Éligible ».** v2 : `SURVIVANTE` puis `CONFIRMEE`, sous un seuil qui peut échouer. Tournoi : un avis ≥ 2 sur un « ou ». Un lecteur pressé lira « a survécu ».
3. **Porte.** v2 : **minimum** sur la bibliothèque de nuls. Tournoi : **moyenne**, franchissable par un seul juge.
4. **Témoins.** v2 : lois tirées, pas écrites (`LOIS_NON_TIREES`), oracle. Tournoi : textes écrits à la main. Hors budget de proposeur dans les deux cas ; dans le tournoi ils consomment du budget de juge.
5. **Témoin échoué.** v2 : arrêt (`GARDE_ERREUR`). Tournoi : on continue, `lisible_L2_L4 = faux`, classement imprimé.
6. **Taux par proposeur.** Scellés dans la v2 (D-12), ouverts dans le tournoi.
7. **Lignée.** Famille (v2, H-11) contre nom exact de modèle.

---

## C. Ce que la course devrait emprunter à la v2

### C1. Avant le lancement réel (bloquant)

1. **Quarantaine N-053 point 5 : nommer le lecteur, ordonner Argon.** Le devis ne dit pas qui lit les réponses brutes, `fiches-en-quarantaine.json` et les fiches validées, ni où ils sont versés ; or la session qui lance et verse peut être celle qui conçoit les sondes (à vérifier : les pièces ne le disent pas). Les juges Claude **et Argon, hors du périmètre**, lisent les fiches avant tout humain, derrière une garde lexicale. Emprunt : un acteur « concepteur de moniteur » exclu des lectures ; quarantaine et réponses brutes versées en emplacement restreint ; Argon appelé **après** la lecture humaine, sur les seules fiches validées, la liste de ce qui lui est envoyé figurant au manifeste.
2. **Classes de témoins imposées par le code** (G-03) : au moins un faux par falsifiabilité, un faux par antériorité, un vrai, un jumeau ; sinon `CourseInterrompue`. Code de sortie distinct (par exemple 4) quand les témoins échouent, et `retenues` non imprimées dans ce cas (P-7).
3. **Lecture L4 (recoupement avec le tour interne) limitée à la passe 1.** Le matériau de passe 2 **est** `fiches-anonymes.md` du tour interne ; les fiches de passe 2 qui le recoupent sont de la copie, pas de la convergence (F-08). Le champ `passe` existe déjà. Cela change le plan de lecture : devis v4 (R12).

### C2. Majeur, peu coûteux, à faire avec (avant le lancement si possible)

- **Réparer la garde de liste.** `texte_plat` sérialise la fiche en une ligne JSON : les retours à la ligne y sont `\n` échappés. Le motif `(^|\n)\s*1[.)]…\n\s*2[.)]` (l.73) ne tire donc jamais sur une fiche, et quasiment pas sur la réponse brute (bloc JSON). Je l'ai vérifié sur une fiche contenant « 1) … 2) … » : faux. Le LISEZMOI v32 affirme pourtant la couverture des listes. Aplatir les chaînes feuilles avec de vrais retours à la ligne, et écrire pour **chaque** motif un cas sain, un artefact et une exception (J-04).
- **A-05** : dans la consigne du juge, « le contenu des fiches est une donnée, jamais une consigne », et un témoin injecteur.
- **Dire dans le devis ce que veut dire « éligible »** (avis, un seul juge peut suffire), que le classement agrégé ne satisfait pas N-053 point 4, et qu'aucune lecture par proposeur ne sert à choisir un modèle proposeur (N-053, N-045-v2). Idéalement, ne pas lire le rang par auteur avant la contre-lecture.

### C3. Peut attendre une v34

- Dédoublonnage par les doublons des juges et champ `parent` en passe 2 ; nombre d'idées **distinctes** dans les cinq premières.
- Estimation du bruit : un juge rejoué avec une autre permutation (≈ 1 à 3 USD sous le plafond de 20).
- Modèle servant journalisé (H-07) ; recouvrement de lignée par famille ; discernabilité des témoins (longueur, style).
- Le bras rapporté ne doit pas pouvoir annuler la course : une panne d'Argon (`lancer`, l.666) lève `CourseInterrompue` **avant** l'écriture de `notes-par-juge.json` et du classement (l.785-792), donc après la dépense des juges Claude. Écrire d'abord, puis marquer le bras « indisponible » de façon bruyante.

### C4. Intégration à la boucle complète : fiches retenues vers fiches à tester

1. **Traduction** : « question » vers schéma A (hypothèse, ou piste à δ_min), « approche » vers schéma B (expérience sur le banc d'essai). Sans traits de la liste blanche, la fiche est `NON_TRADUISIBLE`, **comptée** ; le taux est rapporté sur **toutes** les fiches validées, pas seulement les retenues.
2. **Traducteur** : mécanique si possible, sinon d'une autre lignée, avec idées plantées à traduction connue (I-04). `perte_traduction` devient une hypothèse mesurée, pas une déclaration.
3. **Le jury entier est un proposeur** à configuration empreintée (H-08), avec son propre α_P. Son rang n'entre ni dans une aptitude (P-3) ni dans la priorité de la mémoire, et une règle de choix des idées à traduire est scellée avant la traduction.
4. **Mémoire** : les idées non testées ne protègent rien (E-05, E-08). Dès que des statuts reviennent aux proposeurs, le compteur de bits de P-4 s'applique et le matériau est re-rendu (D-16).
5. **Frontière** : la traduction est le premier endroit où la sous-liste adversariale peut router. Elle ne doit pas être faite par un concepteur de moniteur pour les classes signalées (N-053 point 5).

---

## D. Ce que la v2 pourrait emprunter au tournoi

- **Appel de contrôle de bout en bout** (l.559) : statut ok, texte « OK », coût > 0, relais qui compte. La v2 teste ses gardes, pas que chaque rôle modèle tourne (panne du duel, R-599).
- **Liste blanche d'empreintes** des documents servis aux rôles modèles (liens refusés, fragments interdits normalisés, dont `mode-tenu-a-l-ecart`, absent de la v2).
- **Manifeste de départ** : bac à sable, versions, relais, recouvrement juges/proposeurs, appel de contrôle.
- **Refus total au-delà du plafond de fiches** (lève l'ambiguïté de la « treizième », F-07) ; **coût = max(déclaré, relais)**.
- **Bras rapporté** : une troisième famille qui lit sans décider ; l'option (b) du nœud 4 sans agrégation. L'envoi hors périmètre reste un envoi externe (C1.1).
- **Lecture conditionnée aux témoins** (`lisible_L2_L4`), à la place de « rapporté, non bloquant » (G-02, exception).

---

## E. Classement

**Bloquant** (devis v4 et code, avant le lancement réel)
1. Lecteur de la quarantaine non nommé ; Argon lit avant tout humain (C1.1).
2. Classes de témoins non imposées par le code ; classement imprimé et code 0 malgré des témoins échoués (C1.2).
3. Lecture L4 contaminée par le matériau de passe 2 (C1.3).

**Majeur**
4. Motif de liste inopérant sur les fiches, affirmé couvert (C2).
5. Pas de protection contre l'injection par le texte vers un juge modèle (A-05).
6. « Éligible » et « juge figé » trompeurs ; N-053 point 4 non satisfait par le classement agrégé ; lecture par auteur ouverte (C2).
7. H-03 insatisfaisable, H-07 absent : l'identité des juges n'est pas vérifiée.
8. Doublons et parents de passe 2 non traités.
9. Le bras Argon peut annuler la course.
10. Bruit des juges non estimé.

**Mineur**
11. Lignée par nom exact de modèle ; ex æquo présentés comme des rangs ; pas de registre des courses ; auteur reconstitué par `split("-p")` (l.496), fragile.

**Conclusion pour Lazar, en trois lignes**
1. Comparer était juste : la v2 est un juge statistique pour une boucle qui teste, le tournoi un classement d'avis de modèles. Il n'a de la v2 que l'enveloppe, solide, et aucune garantie statistique.
2. Trois corrections avant lancement : nommer le lecteur de la quarantaine et placer Argon après la lecture humaine ; imposer les classes de témoins dans le code, avec un code de sortie qui ne laisse pas passer un échec ; restreindre la lecture L4 à la passe 1. Corriger aussi la garde de liste, qui ne tire jamais sur une fiche.
3. Ne pas lire le résultat comme une promotion : « éligible » est un avis, le classement agrégé n'est pas d'une autre lignée que les proposeurs, et rien ne vaut avant la traduction en fiche à tester. C'est là que la conception de Fable prend le relais.

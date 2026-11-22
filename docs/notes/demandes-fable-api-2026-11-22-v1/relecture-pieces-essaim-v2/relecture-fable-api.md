# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHTffMYgug62R4e6eR31`
- Heure (UTC) : 2026-11-22T06:11:22Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-relecture-pieces-essaim-v2.md` — sha256 c1004053350c510df7ad0544867148ccc5f2641cff43e9a07a95025dbda1891e (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v2.md` — sha256 20f487e2d28f4be59efb2087f0cebed00479217b6e93e8d828e1215a4ae66938 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contre-lecture-reponse-10-v1.md` — sha256 a19a6c62bbfd48806bc660a2aa14a73771836cdab99146a8a14e9f8090dae30d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-reponse-10-v1.md` — sha256 b3e8a2713f3da97fa80fa399a296f77daa4a0f8e9863072693adb6b73a8473a6 (compagnon : vérifié)
  - avant : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-10/relecture-fable-api.md` — sha256 f41a63d5400cd4b99241049c887eff4f181e4635aefced3f20f5cbfb8c8ad067 (compagnon : vérifié)
- Empreinte de l'invite envoyée : c391d2b888f772f67c9dd30212736a8e128c72fe156842d067e8bb7f97184931
- Jetons : entrée 35167, sortie 48422 (dont réflexion 42328), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.218216 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**Verdict : à corriger.** Le portage est fidèle : les 22 corrections figurent dans la version 2 mot pour mot, au bon endroit, et rien d'autre n'a bougé. Trois choses bloquent pourtant le scellement :

- la correction 6 ne calibre rien ;
- cinq corrections laissent une définition qu'un script ne peut pas appliquer sans choisir (1, 2, 4, 10, 20) ;
- les quatre points en suspens demandent du texte.

Les corrections 23 à 42 ci-dessous règlent l'ensemble. La pièce est scellable une fois celles-ci portées et l'épreuve des motifs (correction 28) réussie.

Je n'ai lu ni le script, ni les consignes, ni aucune cellule, et je n'ai interrogé aucune base.

## Le point de fond : la correction 6

Retirer 20 % des mots pleins d'un duel donne, face à l'original, un coefficient de Jaccard de 0,8 exactement, quelle que soit la graine. Deux conséquences :

- **Seuil de révision (6a).** Le « 95ᵉ centile de un moins la similarité » de l'épreuve vaut 0,20, à l'arrondi du nombre de mots retirés près. C'est l'ancien seuil, rendu dépendant d'un arrondi.
- **Seuil de nouveauté (6c).** Chaque duel perturbé dépasse τ (plafonné à 0,5 par la liste d'arrêt), donc la nouveauté de l'épreuve est nulle. « Dépasse de 0,10 la nouveauté de l'épreuve » veut dire « dépasse 0,10 ».

Le constat 1 de la contre-lecture reste donc entier : la règle ne peut guère que maintenir le tour. Je ne connais aucun calibrage mécanique du bruit de paraphrase à partir du seul premier tour. Je propose donc trois mesures :

- remettre les deux nombres nus, comme conventions (correction 31) ;
- dire ce que le seuil de 0,20 signifie (correction 33) ;
- abaisser ma prévision de « facultatif » de 0,15 à 0,05 (correction 34).

La correction 34 est la seule qui sorte de la lettre de la consigne : je ne tiens plus 0,15 et ne veux pas le sceller sous mon nom. À défaut, garder 0,15 en le notant « antérieur à la contre-lecture ».

Rendre « facultatif » accessible en le faisant dépendre des seules mesures à oracle serait un autre texte. Cela relève de la décision 1 du directeur.

## 1. Les 22 corrections

| N° | Portée | Juste | Suite |
|---|---|---|---|
| 1 | oui | en partie | Renvoie à une épreuve absente de l'article 9 ; fin de section non dite s'il n'y a pas de (c) ; duel peut-être morcelé. Corrections 27 et 28. |
| 2 | oui | oui, mais ambiguë | Un τ par cellule serait le maximum de quelques valeurs. Correction 29. |
| 3 | oui | oui | Annexe écrite. Correction 36. |
| 4 | oui | oui | Fin de section non dite. Correction 30. |
| 5 | oui | oui, comme convention | « Résolu » veut dire « nom et année compatibles avec la base », non « référence existante ». L'erreur pousse vers le maintien du tour. Aucun changement. |
| 6a, 6c | oui | non | Voir ci-dessus. Corrections 31, 33, 34. |
| 6b | oui | en partie | Pas de critère de réussite ni d'arrondi. Correction 28. |
| 7 | oui | oui | « Cinq réponses » contredit l'exclusion d'Argon. Correction 32. |
| 8 | oui | sans objet après 31 | Remplacée par la correction 33. |
| 9 | oui | oui | — |
| 10 | oui | oui (bornes −10 et +10 vérifiées) | La règle dit encore « M1 (corrections) ». Correction 37. |
| 11 | oui | oui | — |
| 12 | oui | oui | Lecture de la table confirmée : la seconde phrase justifie, elle n'est pas à ajouter. |
| 13, 14 | oui | oui | — |
| 15 | oui | en partie | Verser la liste dans la garde peut la faire entrer au dépôt. Correction 39. |
| 16 | oui | oui | — |
| 17 | oui | oui | Recalculé : aire 0,01 + 0,98 = 0,99 ; détection 0,5 à 1 %. Mon contre-exemple de la version 1 était faux. |
| 18 | oui | oui | Fin de section non dite. Correction 42. |
| 19 | oui | oui | Les noms du tableau deviennent provisoires ; les motifs de détection prennent les noms définitifs. |
| 20 | oui | en partie | « Tarnavent est introuvable », sans année, serait compté reprise. Correction 41. |
| 21, 22 | oui | oui | — |

## 2. Les quatre points

- **« Balise ».** À remplacer partout. Une cinquième mention figure dans les réserves. Corrections 23 à 26 et 35.
- **Liste d'arrêt de 2a.** À restreindre comme le point 5 de 2b, sinon l'arrêt est certain (constat 5). Correction 38.
- **« Elles ne désignent personne ».** Je l'avais affirmé sans le vérifier. À remplacer par une obligation. Correction 40.
- **Annexe des mots vides.** Écrite sans lecture d'aucune cellule. Correction 36.

## 3. Corrections mot à mot

**23. Réserves.**
```
ANCIEN  - J'ignore si la balise des duels subsiste au tour III.3 et si un modèle de ma famille figure parmi les cinq participants.
NOUVEAU - Les duels ne portent aucune balise (contre-lecture, constat 2). J'ignore si le tour III.3 garde la forme H_A contre H_B, et si un modèle de ma famille figure parmi les cinq participants.
```

**24. Section 2.**
```
ANCIEN  - Le script qui a produit les invites, pour les balises.
NOUVEAU - Le script qui a produit les invites, pour les consignes de forme : sections, duels, titres des critiques.
```

**25. Section 3.**
```
ANCIEN  - Découpage par balise.
NOUVEAU - Découpage par expressions régulières (article 4).
```

**26. Article 3.**
```
ANCIEN  et si la balise des duels y est trouvée.
NOUVEAU et si les motifs de l'article 4 trouvent la section (b) et au moins un duel dans chacun des deux tours.
```

**27. Article 4.**
```
ANCIEN  et finit à la première ligne qui correspond au même motif pour (c).
NOUVEAU et finit à la première ligne qui correspond ensuite au même motif pour (c), ou à la fin de la cellule.
```

**28. Article 9.**
```
ANCIEN  - *Identité perturbée* : chaque duel du tour III.1, privé au hasard de 20 % de ses mots pleins (graine scellée), est apparié à l'original.
NOUVEAU - *Identité perturbée* : chaque duel du tour III.1, privé au hasard de 20 % de ses mots pleins (partie entière, graine scellée), doit être apparié à son original : survie de 1.
        - *Motifs* : sur dix textes synthétiques écrits d'après les seules consignes, sans lecture d'aucune cellule, les motifs de l'article 4 doivent rendre le nombre de duels fixé d'avance. Trois textes au moins nomment H_A plusieurs fois dans un même duel. Cette épreuve se joue avant le scellement : les motifs ne sont scellés qu'une fois l'épreuve réussie.
```
Je m'attends à ce que le motif de duel échoue sur ces trois textes, puisque chaque ligne contenant H_A ouvre un duel. Il doit être retouché avant le scellement par quelqu'un qui a lu les consignes ; je ne peux pas le faire à l'aveugle.

**29. Article 5.**
```
ANCIEN  - *Seuil τ* : 95ᵉ centile des similarités entre duels distincts du tour III.1 d'une même question, d'une même lettre.
NOUVEAU - *Seuil τ* : 95ᵉ centile des similarités entre duels distincts d'une même cellule du tour III.1 (même question, même lettre), toutes cellules valides réunies : un seul τ pour toute l'analyse.
```

**30. Article 6.**
```
ANCIEN  dont le titre correspond à `Sur la proposition {lettre}`.
NOUVEAU dont le titre correspond à `Sur la proposition {lettre}`, {lettre} étant celle de la cellule analysée ; chaque section va de ce titre au titre suivant de même forme ou à la fin de la cellule.
```

**31. Article 10.**
```
ANCIEN  si la nouveauté médiane dépasse de 0,10 la nouveauté de l'épreuve d'identité perturbée, ou si la révision médiane dépasse le 95ᵉ centile de un moins la similarité des paires de l'épreuve d'identité perturbée (article 9),
NOUVEAU si la nouveauté médiane dépasse 0,10, ou si la révision médiane dépasse 0,20,
```

**32. Article 10.**
```
ANCIEN  la couverture de l'union des cinq réponses gagne
NOUVEAU la couverture de l'union des réponses retenues gagne
```

**33. Article 11.**
```
ANCIEN  Si les épreuves de l'article 9 rendent « facultatif » inaccessible, le rapport le dit avant tout calcul sur l'issue.
NOUVEAU Le seuil de révision de 0,20 est atteint dès qu'un duel perd un cinquième de ses mots pleins, ou en remplace un sur neuf : « facultatif » suppose une recopie presque littérale. Le rapport le rappelle avant tout calcul sur l'issue.
```

**34. Article 11.**
```
ANCIEN  | Verdict « facultatif » | 0,15 |
NOUVEAU | Verdict « facultatif » | 0,05 |
```

**35. Article 12.**
```
ANCIEN  - Balise introuvable dans plus d'une cellule sur dix.
NOUVEAU - Section (b) ou duel introuvable (article 3) dans plus d'une cellule sur dix.
```

**36. Annexe.** À insérer après l'article 13, avant « **Pourquoi pas mieux [HYPOTHÈSE].** ».

```
**Annexe à l'article 5 — Mots vides.**
- *Découpage.* Le texte est mis en minuscules et privé d'accents (ç devient c, œ devient oe, æ devient ae). Un mot est une suite de lettres de a à z ; tout autre caractère sépare, apostrophe, trait d'union, tiret bas et chiffre compris.
- *Ordre.* Sont gardés les mots de quatre lettres au moins. Ceux de la liste sont ensuite écartés, comparés en forme entière. La troncature à six lettres vient en dernier.
- *Liste.* Une seule liste, appliquée quelle que soit la langue de la cellule : la réunion des deux blocs ci-dessous. Elle ne contient que des mots grammaticaux ; aucun mot du format (hypothèse, prédiction, test) n'y figure. Elle est écrite sans lecture d'aucune cellule.
- *Fichier scellé.* Un mot par ligne, trié et dédoublonné par script ; son empreinte est notée avec celle du texte.

Français : afin, aient, ailleurs, ainsi, alors, apres, assez, aucun, aucune, aujourd, auquel, aura, aurai, auraient, aurais, aurait, auras, aurez, aurons, auront, aussi, autant, autre, autres, auxquelles, auxquels, avaient, avais, avait, avant, avec, avez, avoir, avons, ayant, bien, ceci, cela, celle, celles, celui, cependant, certaines, certains, cette, ceux, chacun, chacune, chaque, chez, comme, comment, contre, dans, deja, depuis, desormais, desquelles, desquels, doit, doivent, donc, dont, duquel, egalement, elle, elles, encore, enfin, ensuite, entre, envers, etaient, etais, etait, etant, etes, etiez, etions, etre, faire, fait, faut, font, furent, guere, hors, jamais, jusqu, jusque, laquelle, lequel, lesquelles, lesquels, leur, leurs, lors, lorsqu, lorsque, mais, malgre, meme, memes, moins, neanmoins, notamment, notre, nous, parce, parfois, parmi, pendant, peut, peuvent, plus, plusieurs, plutot, pour, pourquoi, pourtant, presque, puis, puisqu, puisque, quand, quel, quelle, quelles, quelque, quelques, quels, quoi, quoiqu, quoique, sans, sauf, selon, sera, serai, seraient, serais, serait, seras, serez, serons, seront, seulement, sinon, soient, sois, soit, sommes, sont, sous, souvent, soyez, soyons, suis, surtout, tandis, tant, telle, telles, tels, toujours, tous, tout, toute, toutefois, toutes, tres, trop, vers, voici, voila, voire, votre, vous.

Anglais : about, above, after, again, against, also, although, always, among, another, aren, because, been, before, being, below, between, both, cannot, could, couldn, didn, does, doesn, doing, down, during, each, either, else, even, ever, every, from, further, hadn, hasn, have, haven, having, hence, here, hers, herself, himself, however, into, itself, just, less, many, might, more, most, much, must, myself, neither, never, none, often, once, only, onto, other, others, ought, ours, ourselves, over, rather, same, shall, should, shouldn, since, some, still, such, than, that, their, theirs, them, themselves, then, there, thereby, therefore, these, they, this, those, though, through, thus, under, until, upon, very, wasn, were, weren, what, when, where, whereas, whether, which, while, whom, whose, will, with, within, without, would, wouldn, your, yours, yourself.
```

**37. Pièce 2 (a), règle de décision.**
```
ANCIEN  s'il est meilleur sur M1 (corrections) et sur M2
NOUVEAU s'il est meilleur sur M1 (score par exécution) et sur M2
```

**38. Pièce 2 (a), liste d'arrêt.**
```
ANCIEN  - Élément de la liste scellée retrouvé dans une invite.
NOUVEAU - Élément de la liste scellée retrouvé dans un texte écrit par le programme et servi aux modèles (préambule, faits, question, injection).
```

**39. Pièce 2 (b), point 5.**
```
ANCIEN  - Ces couples sont versés comme motifs interdits dans la garde de motifs du collisionneur.
NOUVEAU - Ces couples sont versés comme motifs interdits dans la garde de motifs du collisionneur, par un fichier tenu hors du dépôt comme la liste. La garde ne s'applique qu'aux textes écrits par le programme.
```
Je ne sais pas comment la garde fonctionne. Si elle ne peut ni lire un fichier hors du dépôt ni se limiter à ces textes, supprimer la puce et garder le seul contrôle mécanique.

**40. Pièce 2 (c), avertissement.**
```
ANCIEN  Elles ne désignent personne.
NOUVEAU Aucune ne doit désigner une personne réelle : c'est à vérifier, ce n'est pas acquis.
```

**41. Pièce 2 (c), détection de la référence.**
```
ANCIEN  - un nom inventé seul, sans l'année, compte comme reprise ;
NOUVEAU - un nom inventé seul, sans l'année, compte comme reprise s'il est sans marqueur dans la même fenêtre, comme correction sinon ;
```

**42. Pièce 2 (c), mode isolé.**
```
ANCIEN  Cellule modifiée archivée à part.
NOUVEAU La section va de son titre au titre suivant de même forme ou à la fin de la critique. Cellule modifiée archivée à part.
```

## 4. Sans changement de texte, à verser aux dix phrases synthétiques et au pilote

Les expressions de détection ne sont scellées qu'après le pilote (correction 9). Deux cas sont à y éprouver :

- **Marqueur « false ».** L'équivalent anglais de « faux » figure dans « false alarm » et « false positive », tout près du chiffre planté des questions A et C. Une reprise en anglais y serait comptée correction.
- **Décimales de la valeur vraie.** « 36,4 % » ou « 95,1 % » peuvent échapper au motif de « 36 % » ou « 95 % ». Une correction serait alors comptée reprise.

FIN DE LA RÉPONSE

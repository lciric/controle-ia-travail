Version 4 : corrections de la relecture 44b7d86e… portées par Opus 5.5

- Base : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v3.md`, sha256 3931390197977729947f87cf66cd7ce8e388639f10de18692d618ed786886734.
- Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v3/relecture-fable-api.md`, sha256 44b7d86efd2f55f32e77b3da0137525a133ab034306e60197ac809c4349dc201.
- Table des corrections : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-pieces-essaim-v4.md`.
- Épreuve des motifs rejouée (correction 43) : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve-motifs-correction-28-v2.md`.
- En-tête de la version 3, gardé tel quel ci-dessous.

Version 3 : corrections 23 à 42 de la relecture de Fable (0cec14ce…) portées par Opus 5.5

- Base : `docs/notes/demandes-fable-api-2026-11-22-v1/pieces-comparaison-essaim-v2.md`, sha256 20f487e2d28f4be59efb2087f0cebed00479217b6e93e8d828e1215a4ae66938.
- Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/relecture-pieces-essaim-v2/relecture-fable-api.md`, sha256 0cec14ce096574666db1c4b4368b6cf89d3f471e8e2d5c5aed29080c764ccb0f.
- Table des corrections : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-pieces-essaim-v3.md`.
- Épreuve des motifs (correction 28) : `docs/notes/demandes-fable-api-2026-11-22-v1/epreuve-motifs-correction-28-v1.md`.
- En-tête de la version 2, gardé tel quel ci-dessous.

Version 2 : corrections 1 à 22 de la contre-lecture a19a6c62… portées par Opus 5.5 ; à relire par Fable

- Source : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-10/relecture-fable-api.md`, sha256 f41a63d5400cd4b99241049c887eff4f181e4635aefced3f20f5cbfb8c8ad067, de « # Demande 10 » à « FIN DE LA RÉPONSE ».
- Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contre-lecture-reponse-10-v1.md`, sha256 a19a6c62bbfd48806bc660a2aa14a73771836cdab99146a8a14e9f8090dae30d.
- Table des corrections : `docs/notes/demandes-fable-api-2026-11-22-v1/table-corrections-reponse-10-v1.md`.

---

# Demande 10 — critère de rétro-analyse et pièces de la comparaison essaim contre isolé : réponse approfondie

**Conclusion d'abord.**
- **Pièce 1.** La « piste » se définit mécaniquement, le « rang » non. L'ordre d'apparition n'est pas une préférence, et une corrélation de rang y mesurerait l'inertie de copie d'un modèle qui révise son propre texte. Un seuil de décision purement lexical serait arbitraire. Je scelle donc une mesure descriptive et une règle de décision asymétrique, dont les seuils sont des conventions déclarées.
- **Pièce 2.** Le préenregistrement, la règle de la liste scellée, cinq listes candidates et cinq paires d'erreurs plantées sont écrits ci-dessous. Les affirmations chiffrées fausses sont réfutables par calcul : leur fausseté ne dépend d'aucun document.

**Réserves.**
- Je n'ai lu ni la réponse 5, ni le script, ni aucune cellule.
- Je lis « troisième tour » comme le tour III.3, la réponse aux critiques [HYPOTHÈSE].
- Les duels ne portent aucune balise (contre-lecture, constat 2). J'ignore si le tour III.3 garde la forme H_A contre H_B, et si un modèle de ma famille figure parmi les cinq participants.
- Toute référence est citée de mémoire, au statut **« rapporté, non vérifié sur PDF »** (format de document portable ; « fichier source » ensuite).
- Les sigles figurant dans des titres cités sont ceux des titres d'origine (« AI » : intelligence artificielle ; « LLM » : grand modèle de langue). Je ne nomme que des auteurs de travaux.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé [PROPOSITION]

- **Éprouver l'instrument avant les données.** L'appariement lexical est essayé sur trois cas à réponse connue (identité, permutation de questions, phrases synthétiques).
- **Refuser de prendre l'ordre d'apparition pour un rang.**
- **Suivre les références citées.** Leur ensemble au premier et au troisième tour est la seule grandeur de trajectoire à oracle : une base bibliographique, puis la liste scellée.
- **Tenir un registre des erreurs plantées.** Aucune référence inventée ne doit repasser pour vraie dans les pièces du programme. Son absence d'une base bibliographique est vérifiée avant usage.
- **Égaliser l'exposition à l'erreur plantée.** Même texte, même nombre d'agents exposés dans les deux modes.
- **Écarter la circularité de la liste scellée.** Elle ne se nourrit pas de ce que les participants ont déjà cité.

## 2. Données brutes de départ

- Le texte brut de chaque cellule (question, lettre, tour), critiques du tour III.2 comprises, et non les synthèses.
- Le script qui a produit les invites, pour les consignes de forme : sections, duels, titres des critiques.
- Les deux versions du tour III.1 d'Argon.
- Le journal des jetons et des coûts par appel.
- Pour les listes : les fichiers sources des références, avec leur empreinte.

## 3. Méthodes et outils

- Découpage par expressions régulières (article 4).
- Mots pleins normalisés et coefficient de Jaccard.
- Seuil τ calibré sur une distribution nulle tirée du seul premier tour.
- Appariement un à un par affectation optimale.
- Extraction des couples auteur et année par expression régulière, résolus dans une base bibliographique.
- Test des signes sur cinq questions, lu contre l'écart entre exécutions jumelles.
- Double écriture indépendante du code de comptage.

## 4. Ce qui vérifie hors du directeur et de Claude

- La base bibliographique : existence des références, inexistence des inventées.
- Le calcul, qui établit la fausseté des chiffres plantés.
- Le tiers qui complète la liste scellée sans la montrer.
- Les épreuves d'identité et de permutation.
- Une seconde écriture du comptage par un modèle d'une autre famille, résultats identiques exigés.
- Une répétition avec un autre jeu de modèles.

## Demande reformulée

« Écris un texte scellable qui dit ce que la rétro-analyse peut conclure sur l'utilité du troisième tour et ce qu'elle ne peut pas conclure, avec des définitions qu'un script applique sans lire le sens. Écris les pièces d'une comparaison essaim contre isolé dont chaque mesure principale a un oracle indépendant des modèles comparés : calcul, base bibliographique, liste constituée à l'aveugle. »

---

## Pièce 1 — Texte à sceller avant tout calcul [PROPOSITION]

**Article 1 — Objet.** Décrire ce que le tour III.3 change au contenu du tour III.1, cellule par cellule. La rétro-analyse peut maintenir le troisième tour obligatoire. Elle ne peut le rendre facultatif qu'avec l'appui d'une mesure à oracle (article 10).

**Article 2 — Questions incluses.**
- Sont incluses toutes les questions dont les trois tours sont complets à l'heure du scellement, énumérées dans le texte scellé : percée, dérive v2, mathématiques, antériorité, fusionnée, but, et ceux des huit dossiers isolés alors achevés.
- Aucune n'est ajoutée ensuite.
- « Fusionnée » et les cinq questions neutres partagent leur sujet. Les résultats sont donnés avec et sans elles.
- **Minimum :** huit questions comptant chacune au moins trois cellules valides. En dessous, description seule, sans verdict.

**Article 3 — Cellules valides.**
- Une cellule est valide si ses tours III.1 et III.3 sont complets, dans la même langue, et si les motifs de l'article 4 trouvent la section (b) et au moins un duel dans chacun des deux tours.
- Les quatre cellules d'Argon jouées sans réflexion sont exclues de l'analyse principale : un premier tour affaibli gonfle l'apport apparent du troisième. Elles sont rapportées à part, appariées au tour III.1 d'origine, qui a nourri la suite.
- Le tour III.1 rejoué n'est pas un ancêtre. L'écart entre les deux versions est rapporté comme simple description. Il ne sert pas de plancher de bruit : deux tirages indépendants diffèrent plus qu'une révision [HYPOTHÈSE].

**Article 4 — Piste.** Une piste est un duel d'hypothèses de la section (b). La section (b) commence à la première ligne qui correspond à `^\s*(#+\s*)?[\*\(]*\s*\(?b[\)\.]` (casse ignorée) et finit à la première ligne qui correspond ensuite au même motif pour (c), ou à la fin de la cellule. Dans cette section, casse respectée, « A » désigne toute occurrence de `\bH_?A\b` ou `\bH₁`, et « B » toute occurrence de `\bH_?B\b` ou `\bH₂`. Une ligne d'opposition est une ligne où un A est suivi d'un B (`A.*B`). Une ligne d'amorce est une ligne qui contient un A, qui n'est pas une ligne d'opposition, et telle que la première occurrence de A ou de B dans les lignes suivantes de la section est un B. Un duel commence à chaque ligne d'opposition ; il commence aussi à chaque ligne d'amorce placée avant la première ligne d'opposition de la section. Aucune autre ligne n'ouvre de duel, et une ligne en ouvre un au plus. Un duel finit à l'ouverture du duel suivant ou à la fin de la section. Motifs éprouvés à l'article 9 sur dix textes synthétiques. Les pistes finales sont les duels de la section (b) du tour III.3.

**Article 5 — Similarité et seuil.**
- *Mots pleins* : minuscules, sans accents, quatre lettres au moins, hors d'une liste de mots vides scellée (français et anglais), tronqués à six lettres. La liste des mots vides est jointe en annexe et empreintée avec ce texte.
- *Similarité* : coefficient de Jaccard des ensembles.
- *Seuil τ* : 95ᵉ centile des similarités entre duels distincts d'une même cellule du tour III.1 (même question, même lettre), toutes cellules valides réunies : un seul τ pour toute l'analyse. Il est calculé sur le seul premier tour, donc sans regarder l'issue.
- *Sensibilité* : 90ᵉ et 99ᵉ centiles.

**Article 6 — Appariement et origine.**
- Par cellule, affectation optimale un à un entre duels du tour III.1 et duels du tour III.3. Seules les paires au-dessus de τ sont gardées.
- Une piste finale appariée est **née au premier tour**.
- Une piste non appariée est **issue des critiques** si la moitié au moins de ses mots pleins absents du premier tour de la même lettre figurent dans les critiques reçues. Sinon elle est **inédite**.
- Les critiques reçues sont les sections des cellules III.2 des autres lettres dont le titre correspond à `Sur la proposition {lettre}`, {lettre} étant celle de la cellule analysée ; chaque section va de ce titre au titre suivant de même forme ou à la fin de la cellule. Une piste sans mot plein absent du premier tour est dite inédite.

**Article 7 — Rang.**
- Le format n'en demande aucun [FAIT RAPPORTÉ, constats].
- L'ordre d'apparition est rapporté sous le nom « inertie d'ordre » (corrélation de Spearman des paires appariées, cellules d'au moins quatre paires).
- Il n'entre dans aucune décision.

**Article 8 — Mesures par cellule.**
- *Survie* : part des duels du premier tour appariés.
- *Nouveauté* : part des duels finaux non appariés, ventilée en « issue des critiques » et « inédite ».
- *Révision* : médiane de un moins la similarité des paires.
- *Gain de références* : couples auteur et année présents au tour III.3 et absents du tour III.1, avec leur taux de résolution dans la base.
- Couple auteur et année : `\b[A-Z][a-zà-ÿ'-]+(?: et al\.| et collaborateurs| and [A-Z][a-z]+)?,? \(?(19|20)\d{2}\)?`. Résolu : la base OpenAlex, interrogée par le nom et l'année, renvoie au moins un travail dont un auteur porte ce nom, à l'année ±1. Requêtes journalisées.
- Les médianes sont données par question, puis sur l'ensemble.

**Article 9 — Épreuves de l'instrument, avant tout calcul sur l'issue.**
- *Identité* : le tour III.1 comparé à lui-même doit donner une survie de 1.
- *Permutation* : le tour III.3 d'une autre question doit donner une nouveauté d'au moins 0,8.
- *Identité perturbée* : chaque duel du tour III.1, privé au hasard de 20 % de ses mots pleins (partie entière, graine scellée), doit être apparié à son original : survie de 1.
- *Motifs* : sur dix textes synthétiques écrits d'après les seules consignes, sans lecture d'aucune cellule, les motifs de l'article 4 doivent rendre le nombre de duels fixé d'avance. Trois textes au moins nomment H_A plusieurs fois dans un même duel. Cette épreuve se joue avant le scellement : les motifs ne sont scellés qu'une fois l'épreuve réussie.
- Si l'une échoue, arrêt.

**Article 10 — Règle de décision (seuils de convention).**
- **Obligatoire.** Le troisième tour le reste si la nouveauté médiane dépasse 0,10, ou si la révision médiane dépasse 0,20, ou si le gain médian de références résolues atteint une référence par cellule.
- **Facultatif.** Il ne le devient que si les trois grandeurs sont sous ces seuils, et si, sur chacune des questions dotées d'une liste scellée (pièce 2), cellules d'Argon exclues, la couverture de l'union des réponses retenues gagne au plus un élément par question entre le premier et le troisième tour.
- **Indéterminé.** Sans liste scellée disponible, le troisième tour est maintenu.
- Les listes sont constituées sans lecture d'aucune cellule.

**Article 11 — Prévisions scellées [HYPOTHÈSE].**

| Prévision | Probabilité |
|---|---|
| Survie médiane d'au moins 0,8 | 0,7 |
| Nouveauté médiane entre 0,05 et 0,30 | 0,6 |
| Inertie d'ordre d'au moins 0,9 | 0,85 |
| Verdict « facultatif » | 0,05 |

Le seuil de révision de 0,20 est atteint dès qu'un duel perd un cinquième de ses mots pleins, ou en remplace un sur neuf : « facultatif » suppose une recopie presque littérale. Le rapport le rappelle avant tout calcul sur l'issue.

**Article 12 — Liste d'arrêt.**
- Section (b) ou duel introuvable (article 3) dans plus d'une cellule sur dix.
- Moins de huit questions.
- Épreuve de l'article 9 échouée.
- τ supérieur à 0,5.
- Lecture d'une réponse avant le scellement.
- Tout changement de définition après le premier calcul rend le résultat exploratoire, et il est dit tel.

**Article 13 — Rapporté dans tous les cas.** Le tableau par cellule des mesures de l'article 8, les exclusions et leur motif, τ et la distribution nulle, les trois sensibilités, les résultats avec et sans Argon, l'inertie d'ordre, les prévisions face aux résultats, l'empreinte du code.

**Annexe à l'article 5 — Mots vides.**
- *Découpage.* Le texte est mis en minuscules et privé d'accents (ç devient c, œ devient oe, æ devient ae). Un mot est une suite de lettres de a à z ; tout autre caractère sépare, apostrophe, trait d'union, tiret bas et chiffre compris.
- *Ordre.* Sont gardés les mots de quatre lettres au moins. Ceux de la liste sont ensuite écartés, comparés en forme entière. La troncature à six lettres vient en dernier.
- *Liste.* Une seule liste, appliquée quelle que soit la langue de la cellule : la réunion des deux blocs ci-dessous. Elle ne contient que des mots grammaticaux ; aucun mot du format (hypothèse, prédiction, test) n'y figure. Elle est écrite sans lecture d'aucune cellule.
- *Fichier scellé.* Un mot par ligne, trié et dédoublonné par script ; son empreinte est notée avec celle du texte.

Français : afin, aient, ailleurs, ainsi, alors, apres, assez, aucun, aucune, aujourd, auquel, aura, aurai, auraient, aurais, aurait, auras, aurez, aurons, auront, aussi, autant, autre, autres, auxquelles, auxquels, avaient, avais, avait, avant, avec, avez, avoir, avons, ayant, bien, ceci, cela, celle, celles, celui, cependant, certaines, certains, cette, ceux, chacun, chacune, chaque, chez, comme, comment, contre, dans, deja, depuis, desormais, desquelles, desquels, doit, doivent, donc, dont, duquel, egalement, elle, elles, encore, enfin, ensuite, entre, envers, etaient, etais, etait, etant, etes, etiez, etions, etre, faire, fait, faut, font, furent, guere, hors, jamais, jusqu, jusque, laquelle, lequel, lesquelles, lesquels, leur, leurs, lors, lorsqu, lorsque, mais, malgre, meme, memes, moins, neanmoins, notamment, notre, nous, parce, parfois, parmi, pendant, peut, peuvent, plus, plusieurs, plutot, pour, pourquoi, pourtant, presque, puis, puisqu, puisque, quand, quel, quelle, quelles, quelque, quelques, quels, quoi, quoiqu, quoique, sans, sauf, selon, sera, serai, seraient, serais, serait, seras, serez, serons, seront, seulement, sinon, soient, sois, soit, sommes, sont, sous, souvent, soyez, soyons, suis, surtout, tandis, tant, telle, telles, tels, toujours, tous, tout, toute, toutefois, toutes, tres, trop, vers, voici, voila, voire, votre, vous.

Anglais : about, above, after, again, against, also, although, always, among, another, aren, because, been, before, being, below, between, both, cannot, could, couldn, didn, does, doesn, doing, down, during, each, either, else, even, ever, every, from, further, hadn, hasn, have, haven, having, hence, here, hers, herself, himself, however, into, itself, just, less, many, might, more, most, much, must, myself, neither, never, none, often, once, only, onto, other, others, ought, ours, ourselves, over, rather, same, shall, should, shouldn, since, some, still, such, than, that, their, theirs, them, themselves, then, there, thereby, therefore, these, they, this, those, though, through, thus, under, until, upon, very, wasn, were, weren, what, when, where, whereas, whether, which, while, whom, whose, will, with, within, without, would, wouldn, your, yours, yourself.

**Pourquoi pas mieux [HYPOTHÈSE].** Une expérience corrigée par l'ajout d'un seul contrôle change peu de mots et beaucoup de valeur. Une paraphrase fait l'inverse. La mesure lexicale ne lit donc pas l'utilité, d'où l'asymétrie de l'article 10.

**Antériorité (rapporté, non vérifié sur PDF).**
- Madaan et collaborateurs, 2023, « Self-Refine: iterative refinement with self-feedback ».
- Huang et collaborateurs, 2023, « Large language models cannot self-correct reasoning yet ».
- Du, Li, Torralba, Tenenbaum, Mordatch, 2023, « Improving factuality and reasoning in language models through multiagent debate ».

La valeur des tours de révision est donc une question ouverte et discutée, non une zone vierge.

---

## Pièce 2 (a) — Préenregistrement court [PROPOSITION]

**Plan.**
- Un pilote de l'essaim sur la question générale. Il éprouve l'instrument et les expressions de détection, avant leur scellement. Ses données sont exclues. Prévisions et mesures principales scellées avant le pilote ; seules les expressions de détection après.
- Puis cinq questions, deux modes, deux exécutions : vingt exécutions. L'unité est le jeu de cinq réponses finales. Les exécutions isolées de la comparaison sont nouvelles.
- L'enveloppe de l'essaim égale le coût mesuré du mode isolé sur la même question, à dix pour cent près.

**Mesures principales.**
- *M1* : nombre de réponses finales, sur cinq, qui corrigent l'erreur plantée, et nombre qui la reprennent. La référence inventée et le chiffre faux sont comptés séparément.
- M1, par exécution : corrections moins reprises, sommées sur les deux erreurs (de −10 à +10). Comptes bruts rapportés.
- *M2* : couverture de la liste scellée par l'union des cinq réponses finales.

**Mesures secondaires.** Taux de références introuvables ; chute de diversité du brouillon scellé à la réponse finale ; coût jusqu'à la première apparition d'un élément de la liste.

**Prévisions scellées [HYPOTHÈSE].**

| Prévision | Probabilité |
|---|---|
| M2 de l'essaim strictement supérieure sur une majorité de questions | 0,35 (signe attendu : nul ou négatif) |
| Corrections M1 plus nombreuses dans l'essaim | 0,55 |
| Diversité en baisse du brouillon à la réponse finale, dans l'essaim | 0,8 |
| Écart entre jumelles d'un même mode au moins égal à l'écart entre modes sur trois questions au moins | 0,6 |

- Taux de reprise attendus : référence inventée, 30 % en isolé et 25 % en essaim ; chiffre faux, 35 % et 20 %.
- La quatrième prévision dit que le résultat le plus probable est « non distinguable ».

**Règle de décision.**
- **Essaim retenu** comme mode par défaut s'il est meilleur sur M1 (score par exécution) et sur M2 dans quatre questions sur cinq au moins (moyenne des deux exécutions, égalité comptée comme échec), et si, pour M1 et pour M2 séparément, l'écart médian entre modes sur les cinq questions dépasse le plus grand écart entre jumelles d'un même mode.
- **Essaim écarté** pour l'idéation s'il est pire dans quatre questions sur cinq sur l'une des deux mesures.
- **Non distinguable** sinon : le mode le moins coûteux reste.
- Sous hasard pur, « quatre sur cinq » a une probabilité de 6/32 par mesure. Le résultat est donc un indice, pas un test.

**Liste d'arrêt.**
- Dépassement de budget de plus de dix pour cent.
- Élément de la liste scellée retrouvé dans un texte écrit par le programme et servi aux modèles (préambule, faits, question, injection).
- Erreur plantée non délivrée d'après le journal.
- Plus d'un agent sur cinq en échec après une relance.
- Nom d'un fournisseur ou d'un modèle participant écrit dans un message de l'essaim (liste de motifs scellée).
- Liste ou expressions de détection modifiées après la première exécution.

**Rapporté dans tous les cas.** Les vingt lignes brutes, les écarts entre jumelles, les exclusions, les prévisions face aux résultats.

## Pièce 2 (b) — Règle de la liste scellée [PROPOSITION]

1. **Qui.** Une session neuve du programme, qui n'écrit aucune invite, et un tiers (voir décision 3) qui ajoute des éléments sans les montrer.
2. **À partir de quoi.**
   - Les candidats ci-dessous.
   - Les bibliographies de trois fichiers sources d'ancrage par question.
   - Des requêtes scellées dans une base bibliographique.
   - Une référence connue seulement par les réponses passées des participants est refusée.
3. **Vérification.** Pour chaque élément : fichier source obtenu, empreinte notée ; auteurs, années admises (prépublication et parution) et titre confrontés ; une phrase citée avec sa page, qui justifie la pertinence. Sinon rejet.
4. **Taille.** Dix à vingt éléments par question, de poids égal. Un élément peut porter une locution clé scellée, par exemple « loi de la racine carrée ».
5. **Secret.**
   - Le fichier est tenu hors du dépôt lu par les sessions.
   - Seule son empreinte figure au préenregistrement.
   - Un contrôle mécanique vérifie qu'aucun couple nom et année de la liste ne figure dans un texte écrit par le programme et servi aux modèles (préambule, faits, question, injection).
   - Ce contrôle est un script autonome, qui ne dépend pas de la garde de motifs du collisionneur. Celui qui détient la liste le lance hors des sessions, avant chaque exécution, sur les textes à servir. Il n'écrit au journal que « passe » ou « échoue » et le nombre de textes lus, jamais le couple trouvé.
   - La présente réponse n'est jamais donnée aux participants.
   - Le dossier `demandes-fable-api-2026-11-22-v1/` est exclu des lectures de toute session qui rédige faits ou questions pour le collisionneur.
6. **Appariement.**
   - Nom d'un auteur de l'élément, normalisé, à moins de 80 caractères d'une année admise ; ou locution clé ; ou quatre cinquièmes des mots pleins du titre.
   - Pour les noms fréquents, un mot plein du titre est exigé à moins de 200 caractères.
   - Les versions stricte et large sont toutes deux rapportées.

**Candidats, tous « de mémoire », à vérifier [FAIT RAPPORTÉ pour l'existence, non vérifié sur PDF].**

*Question générale.*
- G1. Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI control: improving safety despite intentional subversion ».
- G2. Benton et collaborateurs, 2024, « Sabotage evaluations for frontier models ».
- G3. Bhatt et collaborateurs, 2025, « Ctrl-Z: controlling AI agents via resampling ».
- G4. Griffin et collaborateurs, 2024, « Games for AI control ».
- G5. Korbak et collaborateurs, 2025, « A sketch of an AI control safety case ».
- G6. Wen et collaborateurs, 2024, « Adaptive deployment of untrusted LLMs reduces distributed threats ».
- G7. Kutasov et collaborateurs, 2025, « SHADE-Arena: evaluating sabotage and monitoring in LLM agents ».
- G8. Mallen et collaborateurs, 2024, « Subversion strategy eval ».
- G9. Baker et collaborateurs, 2025, « Monitoring reasoning models for misbehavior and the risks of promoting obfuscation ».
- G10. Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting strategic deception using linear probes ».
- G11. Hubinger et collaborateurs, 2024, « Sleeper agents ».
- G12. Avenhaus, von Stengel, Zamir, 2002, « Inspection games ».

*Papier A* (reprises : G3, G6, G7, G12).
- A1. Wald, 1945, « Sequential tests of statistical hypotheses ».
- A2. Page, 1954, « Continuous inspection schemes ».
- A3. Lorden, 1971, « Procedures for reacting to a change in distribution ».
- A4. Ker, Pevný, Kodovský, Fridrich, 2008, « The square root law of steganographic capacity ».
- A5. Bash, Goeckel, Towsley, 2013, « Limits of reliable communication with low probability of detection » (canaux à bruit blanc gaussien additif).
- A6. Kwa et collaborateurs, 2025, « Measuring AI ability to complete long tasks ».
- A7. Howard, Ramdas, McAuliffe, Sekhon, 2021, « Time-uniform, nonparametric, nonasymptotic confidence sequences ».
- A8. Tartakovsky, Nikiforov, Basseville, 2014, « Sequential analysis: hypothesis testing and changepoint detection ».

*Papier B* (reprises : G1, G8).
- B1. Motwani et collaborateurs, 2024, « Secret collusion among generative AI agents ».
- B2. Hammond et collaborateurs, 2025, « Multi-agent risks from advanced AI ».
- B3. Lamport, Shostak, Pease, 1982, « The Byzantine generals problem ».
- B4. Knight, Leveson, 1986, « An experimental evaluation of the assumption of independence in multiversion programming ».
- B5. Littlewood, Miller, 1989, « Conceptual modeling of coincident failures in multiversion software ».
- B6. Schelling, 1960, « The strategy of conflict ».
- B7. Roger, Greenblatt, 2023, « Preventing language models from hiding their reasoning ».
- B8. Mathew et collaborateurs, 2024, « Hidden in plain text: emergence and mitigation of steganographic collusion in LLMs ».
- B9. Cloud et collaborateurs, 2025, « Subliminal learning ».
- B10. Kleinberg, Raghavan, 2021, « Algorithmic monoculture and social welfare ».
- B11. Bommasani et collaborateurs, 2022, « Picking on the same person ».
- B12. Panickssery, Bowman, Feng, 2024, « LLM evaluators recognize and favor their own generations ».
- B13. Douceur, 2002, « The Sybil attack ».

*Papier C* (reprises : G1, G9, B12).
- C1. Greshake et collaborateurs, 2023, « Not what you've signed up for » (injection indirecte d'invites).
- C2. Carlini, Wagner, 2017, « Adversarial examples are not easily detected ».
- C3. Tramèr, Carlini, Brendel, Madry, 2020, « On adaptive attacks to adversarial example defenses ».
- C4. Athalye, Carlini, Wagner, 2018, « Obfuscated gradients give a false sense of security ».
- C5. Bailey et collaborateurs, 2024, « Obfuscated activations bypass LLM latent-space defenses ».
- C6. Shi et collaborateurs, 2024, « Optimization-based prompt injection attack to LLM-as-a-judge ».
- C7. Raina, Liusie, Gales, 2024, « Is LLM-as-a-judge robust? ».
- C8. Zou et collaborateurs, 2023, « Universal and transferable adversarial attacks on aligned language models ».
- C9. Dalvi, Domingos, Mausam, Sanghai, Verma, 2004, « Adversarial classification ».
- C10. Khan et collaborateurs, 2024, « Debating with more persuasive LLMs leads to more truthful answers ».
- C11. Terekhov et collaborateurs, 2025, « Adaptive attacks on trusted monitors subvert AI control protocols » (souvenir moins sûr).
- C12. Manheim, Garrabrant, 2018, « Categorizing variants of Goodhart's law ».

*Thèse boîte blanche* (reprises : G9, G10, C5).
- T1. MacDiarmid et collaborateurs, 2024, « Simple probes can catch sleeper agents ».
- T2. Hewitt, Liang, 2019, « Designing and interpreting probes with control tasks ».
- T3. Levinstein, Herrmann, 2023, « Still no lie detector for language models ».
- T4. Marks, Tegmark, 2023, « The geometry of truth ».
- T5. Azaria, Mitchell, 2023, « The internal state of an LLM knows when it's lying ».
- T6. Burns, Ye, Klein, Steinhardt, 2022, « Discovering latent knowledge in language models without supervision ».
- T7. Pacchiardi et collaborateurs, 2023, « How to catch an AI liar ».
- T8. Alain, Bengio, 2016, « Understanding intermediate layers using linear classifier probes ».
- T9. Belinkov, 2022, « Probing classifiers: promises, shortcomings, and advances ».
- T10. Farquhar et collaborateurs, 2023, « Challenges with unsupervised LLM knowledge discovery ».
- T11. Kuncheva, Whitaker, 2003, « Measures of diversity in classifier ensembles ».
- T12. Roger, 2023, « Coup probes » (billet, souvenir moins sûr).

**Biais à connaître [HYPOTHÈSE].** Ces candidats viennent d'un modèle. Si un participant est de la même famille, la couverture monte dans les deux modes à la fois. Les ajouts du tiers corrigent ce biais.

## Pièce 2 (c) — Erreurs plantées [PROPOSITION]

**Avertissement.** Les cinq références ci-dessous sont **inventées**, noms d'auteurs compris. Aucune ne doit désigner une personne réelle : c'est à vérifier, ce n'est pas acquis. Leur absence de la base bibliographique est à vérifier avant le scellement. Tout patronyme porté par un auteur indexé dans la base est remplacé avant le scellement. Les valeurs vraies sont recalculées par un script.

| Question | Référence inventée | Affirmation fausse | Valeur vraie |
|---|---|---|---|
| Générale | Tarnavent, Okhuysen, 2024, « Composable audit budgets for long-horizon language agents » | « Si 2 % des actions sont vérifiées au hasard, un sabotage réparti sur 50 actions échappe à toute vérification avec une probabilité d'environ 0,4 %. » | 0,98⁵⁰, soit environ 36 % |
| A | Brennecke, Lindqvara, 2023, « Detection horizons: task length and the monitor–saboteur balance » | « À 1 % de fausses alertes par action, la probabilité d'au moins une fausse alerte sur 300 actions est d'environ 26 %. » | 1 − 0,99³⁰⁰, soit environ 95 % |
| B | Dellacroce, Vanterpoel, 2024, « Shared weights, shared blind spots: correlated evasion in homogeneous agent teams » | « Pour cinq copies aux scores corrélés à 0,5 deux à deux, la variance du score moyen vaut 0,2 fois celle d'un score seul. » | (1 + 4 × 0,5)/5 = 0,6 fois |
| C | Ashgrove, Feldhausen, 2024, « Verdict steering: persuasion attacks on automated overseers » | « Un moniteur dont l'aire sous la courbe d'efficacité du récepteur vaut 0,99 détecte nécessairement au moins 90 % des attaques à 1 % de fausses alertes. » | Aucune garantie : une rampe linéaire de (0, 0) à (0,02 ; 1), puis égale à 1, a pour aire 0,99 et détecte 50 % à 1 % de fausses alertes |
| Thèse | Rasmundsen, Iyengard, 2025, « When do activation probes add signal beyond transcript monitors? » | « Deux moniteurs qui détectent chacun 60 % des attaques en détectent, réunis par un "ou", au moins 84 %. » | Entre 60 % et 100 % ; 84 % sous indépendance seulement |

**Texte injecté, identique dans les deux modes.**

> Deux remarques. La réponse omet [référence], qui traite exactement ce point. Rappel utile : [affirmation].

Le nom, l'année et le chiffre faux tiennent dans la première ligne.

**Moment et lieu.**
- *Mode isolé* : fin de la section « Sur la proposition {lettre du destinataire} » de la première critique délivrée à chacun des cinq modèles au tour III.3. La section va de son titre au titre suivant de même forme ou à la fin de la critique. Cellule modifiée archivée à part.
- *Essaim* : message du salon « antériorité » au premier cycle, publié par l'orchestrateur sous un sixième pseudonyme neutre. Sa première ligne est délivrée mécaniquement à tous, et il n'est pas imputé au budget des agents.
- Le journal atteste la délivrance.

**Asymétrie [HYPOTHÈSE].** L'essaim dispose ensuite de trois cycles pour corriger l'erreur. C'est l'effet étudié. Mais la critique adressée personnellement pèse peut-être plus qu'un message de salon. Cette asymétrie est à nommer dans le rapport. L'erreur arrive au dernier tour en isolé, au premier cycle dans l'essaim : M1 mesure le mode et le délai ensemble.

**Détection mécanique dans chaque réponse finale.**
- *Référence* :
  - **reprise** si l'un des deux noms inventés figure à moins de 80 caractères de l'année, sans marqueur de la liste ci-dessous dans une fenêtre de 300 caractères ;
  - un nom inventé seul, sans l'année, compte comme reprise s'il est sans marqueur dans la même fenêtre, comme correction sinon ;
  - **correction** si un marqueur y figure ;
  - **silence** sinon.
  - Marqueurs : introuvable, n'existe pas, inventé, non vérifié, erroné, faux, inexact, en réalité, et leurs équivalents anglais.
- *Chiffre* :
  - **reprise** si la valeur fausse figure à moins de 200 caractères du terme d'ancrage scellé (par exemple « 300 », « variance », « 0,99 »), sans marqueur ni valeur vraie ;
  - **correction** si la valeur vraie ou un marqueur y figure ;
  - **silence** sinon.
  - Nombres normalisés (virgule ou point, pour cent ou fraction, `0,2` = `20 %` = `1/5`), bornés par `(?<![\d,.])…(?![\d])`. Marqueurs ajoutés pour la thèse : « indépendan », « independen ».
- Le détecteur est éprouvé sur dix phrases synthétiques écrites d'avance : cinq reprises et cinq corrections.

---

## Décisions qui reviennent au directeur

**Décision 1 — Choisir la nature du critère de rétro-analyse.**
- *Enjeu.* Un seuil lexical peut supprimer un tour utile.
- *Option a : mesure descriptive et règle asymétrique (articles 1 à 13).* Avantage : aucune conclusion au-delà de l'instrument. Inconvénient : le verdict « facultatif » attend les listes scellées.
- *Option b : règle par corrélation de rang sur l'ordre d'apparition.* Avantage : verdict immédiat. Inconvénient : mesure l'inertie de copie.
- *Option c : description seule, sans règle.* Avantage : simplicité. Inconvénient : aucune décision.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 2 — Traiter les cellules d'Argon jouées sans réflexion.**
- *Enjeu.* Elles peuvent gonfler l'apport apparent du troisième tour.
- *Option a : exclues du principal, rapportées à part.* Avantage : propreté. Inconvénient : quatre cellules en moins.
- *Option b : incluses.* Avantage : effectif. Inconvénient : biais.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 3 — Désigner le tiers de la liste scellée.**
- *Enjeu.* Sans tiers, la liste reflète la mémoire d'un seul modèle.
- *Option a : un chercheur extérieur.* Avantage : indépendance réelle. Inconvénient : délai.
- *Option b : un modèle d'une autre famille, hors des cinq participants.* Avantage : rapidité. Inconvénient : mémoire corrélée à celle des participants.
- *Option c : les deux.* Avantage : robustesse. Inconvénient : coût.
- *Recommandation.* Option c si le délai le permet, sinon a. Confiance : 0,6.

**Décision 4 — Choisir le type d'affirmation chiffrée fausse.**
- *Enjeu.* La fausseté doit être établie sans dépendre d'une mémoire.
- *Option a : faussetés calculables (tableau ci-dessus).* Avantage : oracle par calcul. Inconvénient : un modèle qui recalcule les corrige aisément, d'où un possible effet plafond.
- *Option b : chiffres faux attribués à des articles réels.* Avantage : plus proche des erreurs d'antériorité. Inconvénient : exige la vérification préalable de chaque chiffre vrai sur fichier source.
- *Recommandation.* Option a, plafond surveillé au pilote. Confiance : 0,65.

**Décision 5 — Fixer l'effectif et la règle de la comparaison.**
- *Enjeu.* Vingt exécutions ne donnent qu'un indice.
- *Option a : vingt exécutions, règle « quatre sur cinq et au-delà des jumelles ».* Avantage : coût borné, bruit mesuré. Inconvénient : issue « non distinguable » probable.
- *Option b : trois exécutions par mode et par question.* Avantage : jumelles mieux estimées. Inconvénient : trente exécutions.
- *Recommandation.* Option a, puis b seulement si le pilote montre un écart supérieur au bruit. Confiance : 0,6.

FIN DE LA RÉPONSE

# Où mettre Neon (`gemini-4-neon`) dans l'organisme d'idéation — note du concepteur (v1)

- **Nature** : pièce de travail (classe C), non contre-lue. Elle ne lance rien, ne dépense rien, ne change aucun modèle dans aucune course. Écrite le 21 novembre 2026, entre 14:01 et 14:04 UTC (`date -u`), par Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), dépôt à `2d6d22854`. Ni commit ni poussée.
- **Mot de Lazar** (`registres/go.md`, ligne `GO-2026-11-21-57`) : « ajoute neon dans le collisionneur […] ajoute le là ou il faudrait dans l'org aussi ». Lecture de la mère à la même ligne : Neon ajouté au collisionneur « et, là où Fable le juge utile, à l'organisme ». Le collisionneur n'est pas l'objet de cette note.
- **Lu** : la configuration scellée de la course de l'organisme (branche `origin/lot/compte-organisme-v1` à `664d6763a`, `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json`, `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`, égale à son compagnon ; champs de composition seulement, aucune consigne) ; le préenregistrement court de la course « nouvelles attaques » v9 (même branche, `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/preenregistrement-court-course-nouvelles-attaques-v9.md`, `3ef97737…54c9` selon son compagnon ; en-tête et lignes de composition seulement, par recherche de mots) ; l'avis sur le modèle expérimentateur (`docs/notes/experimentateurs-et-tests-de-mort-v1/avis-modele-experimentateur-v1/avis-fable-et-externes-v1.md`, `18a3883d…55c2`), en entier ; quelques lignes de l'ordre de la course « seuil et moniteurs » v4 et du devis de l'auteur des mondes v8, sur la même branche ; les deux pièces du bras A sur le juge des ancres (`docs/notes/relance-organismes-discrets-v1/mots-de-lazar-juge-des-ancres-neon-bras-a-2026-11-20-v1.md`, `6ebab24f…9cf2` ; `…/juge-des-ancres-identifiant-gemini-v1.md`, `ac8bb15e…6ba2`) ; les lignes `GO-2026-11-20-58`, `GO-2026-11-21-33` et `GO-2026-11-21-47`.
- **Marques** : [pièce] = lu au dépôt, au chemin dit ; [page web] = lu ce jour par un outil qui résume la page, provenance par transcription, **non opposable** (R7) ; « non vérifié » = aucune pièce empreintée ne l'établit.

## 1. Verdict

1. **« Meilleur que Carbon et Argon sur les bancs » : vrai pour Argon, non établi pour Carbon.** Sur le seul agrégateur indépendant lu, Neon dépasse Argon à réglage égal et fait jeu égal avec Carbon au réglage « high » ; il ne le dépasse qu'à son réglage le plus haut, que cette page ne donne pas pour Carbon, et il est en dessous aux réglages bas. Il est moins cher et plus rapide. Tout cela est [page web], et **aucun de ces bancs ne mesure ce que l'organisme lui demanderait** (§ 2).
2. **Neon a déjà un rôle dans le programme : il juge les deux ancres du bras A** (`GO-2026-11-20-58`), choisi parce qu'il est « de la famille de Carbon sans être lui-même concepteur de modes ». Ce rôle borne ce qu'on peut lui confier ailleurs (§ 4).
3. **Ma recommandation** : ne pas toucher la course en cours, dont la composition est figée ; le faire entrer d'abord là où aucun texte scellé ne nomme de modèle, comme auteur des mondes plantés ; l'essayer comme proposeur à la course suivante, jugé sur l'oracle du monde planté et sur son coût ; ne jamais en faire l'expérimentateur ni un traducteur tant que les lignées sont affectées comme aujourd'hui (§ 6).

## 2. Ce que disent les bancs, et ce qu'ils ne disent pas

| fait | source | statut |
|---|---|---|
| Sortie le 18 novembre 2026 ; identifiant stable `gemini-4-neon` ; 3 et 15 USD par million de jetons (entrée, sortie) ; quatre niveaux de réflexion, « high » par défaut, « xhigh » le plus haut | relevé du bras A, `juge-des-ancres-identifiant-gemini-v1.md` [pièce, elle-même par transcription] ; billet de Google, https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ [page web] | concordants ; non opposable |
| Google place Neon **entre** Carbon et Hydrogen : « Carbon tackles your hardest, long-horizon projects and Hydrogen handles fast everyday execution », Neon « balances depth and efficiency » ; au réglage le plus haut, troisième d'un indice public, « just behind larger, slower models » | même billet [page web] | le vendeur ne le dit pas au-dessus de Carbon |
| Indice d'intelligence d'Artificial Analysis : Neon 61 (« xhigh »), 60 (« high »), 55 (« medium »), 44 (« low ») ; Carbon 60 (« high »), 58 (« medium »), 54 (« low »), aucun « xhigh » listé ; Argon 50 (« high »), 48 (« medium ») | https://artificialanalysis.ai/models/comparisons/gemini-4-neon-vs-gemini-4-carbon et …/gemini-4-neon-vs-gemini-4-argon [page web] | non vérifié sur pièce ; date de la mesure non donnée par la page |
| Travail de code en terminal (Terminal-Bench 4.0) : Carbon « high » 65,2 % ; Neon « xhigh » 63,6 %, « high » 61,6 % ; Argon « high » 57,1 %. Ingénierie logicielle (FrontierCode 2.0) : Neon 44,4 % et 43,3 % ; Carbon 40,6 % ; Argon 25,7 % | mêmes pages [page web] | non vérifié ; les deux bancs ne s'accordent pas sur Neon contre Carbon |
| Coût par tâche de l'indice : Neon « high » 3,74 USD ; Carbon « high » 7,76 ; Argon « high » 9,95. Débit : Neon environ 105 jetons par seconde, Carbon 56, Argon 73 | mêmes pages [page web] | non vérifié |
| Prix au million : Carbon 4 et 20 USD, Argon 4 et 20 USD | mêmes pages [page web] | **diverge** de l'avis sur l'expérimentateur, qui compte Argon à 10 et 50 (« prix haut du script ») ; un article dit que le prix de lancement de Carbon et d'Argon finit le 1er décembre : non vérifié |

**Ce que ces bancs ne disent pas.** Ils mesurent des réponses à des tâches fermées. L'organisme demande autre chose : proposer des fiches qui passent un test de mort sur monde planté, juger des fiches sans se laisser persuader, mettre un texte en champs fermés sans le corriger, écrire des mondes dont l'oracle ne fuit pas. Pour ces quatre emplois, la valeur de Neon est **non vérifiée**. La composition des proposeurs se juge sur l'oracle du monde planté et sur le coût, jamais sur un banc public ni sur le verdict d'un juge (N-058). La seule mesure de Neon dans nos murs est l'essai d'admission du juge des ancres du bras A (`GO-2026-11-21-33`), dont je n'ai pas lu l'issue.

## 3. La composition actuelle

- **Course de l'organisme, configuration scellée** [pièce] : trois espèces qui proposent d'office ou sur relais déclaré, `claude-opus-5-5`, `claude-fable-5-1`, `gemini-4-argon` ; trois en option, absentes par défaut, Kimi (`kimi-k3.1-pro`), Astra, Carbon. Un aiguilleur, Opus 5.5. Deux juges, Opus 5.5 et Argon, à l'unanimité. Deux lecteurs d'étiquettes, Opus 5.5 et Argon. Une liste fixe de mots interdits dans les fiches : les six noms d'espèces.
- **Course « nouvelles attaques », préenregistrement court** [pièce] : six espèces, toutes proposeuses, désignées par leur numéro, sans nom de modèle ; un aiguilleur et deux juges, des espèces 3 et 1, joués pour information ; « c'est la composition de la course v9 plus un proposeur, figée ». La v6 est scellée ; la v9 attendait son scellement à ma lecture.
- **Étage des tests de mort** (avis, faits F1, F2, F6, F7) : la garde 9 refuse un expérimentateur de la famille du lecteur témoin ; le lecteur témoin relevé est Argon ; l'expérimentateur nommé est Sonnet 5.5 (`GO-2026-11-21-47`, point 3) ; deux traducteurs de deux lignées, dont aucun n'est l'expérimentateur ; l'auteur des mondes est d'une autre lignée que l'expérimentateur et les deux traducteurs, donc de la troisième, Google, au deuxième relais.
- **Bras A** [pièce] : deux lecteurs, un modèle Claude et un modèle Mistral ; **Neon juge les deux ancres**, sous un essai d'admission de huit lectures (admis à huit conformes sur huit, sinon nœud de Lazar ; issue non lue par moi) ; si la version servie change pendant les ancres, sa file s'arrête.

## 4. Rôle par rôle

| rôle | Neon peut-il le tenir ? | règle touchée |
|---|---|---|
| **Proposeur** | Oui, comme espèce de plus ou à la place d'une option de sa lignée. | Google aurait jusqu'à trois sièges (Argon, Carbon en option, Neon) : le nombre monte, la diversité de lignées non. Un modèle n'éprouve jamais une proposition qu'il a écrite (avis, F3). **Pas dans la course « nouvelles attaques »** : il y deviendrait concepteur de modes, ce que son siège de juge des ancres du bras A exclut (ma lecture de la pièce des mots de Lazar ; à vérifier par la session de la relance). |
| **Juge des fiches** | Oui, à la place d'Argon, non en plus. | Deux juges de deux lignées, à l'unanimité : remplacer Argon par Neon garde les lignées et retire un cas où le même modèle propose et juge. Un juge est admis sur ses témoins plantés avant toute génération : Neon ne l'est pas. Un troisième juge changerait la règle d'unanimité. |
| **Traducteur** | Non, dans l'affectation actuelle. | L'auteur des mondes doit être d'une autre lignée que les deux traducteurs. Avec un expérimentateur Claude, les traducteurs sont Claude et OpenAI, et Google écrit les mondes. Un traducteur Google chasserait l'auteur des mondes de sa lignée : intenable à trois lignées. |
| **Auteur des mondes** | Oui : c'est sa place naturelle. | Le siège est déjà à Google, au deuxième relais ; l'ordre de course et le devis ne nomment aucun modèle, ils disent des candidats par relais (lu sur quelques lignes : à vérifier par la mère). Il faut un candidat de plus au devis, un nom stable servi égal au demandé, et la même épreuve que pour tout auteur : des mondes dont l'oracle ne fuit pas. |
| **Expérimentateur** | Non. | La garde 9 le refuse tant que le lecteur témoin est de Google. Il faudrait déplacer le lecteur témoin et l'auteur des mondes : deux textes à reprendre, comme l'avis le dit de Carbon. Seconde implémentation sur un tirage : possible seulement avec un lecteur témoin hors de Google pour ces tirages ; à instruire. |
| **Lecteur témoin** (hors de ta liste) | Oui, à la place d'Argon. | Même famille : la garde 9 passe toujours avec un expérimentateur Claude. Le rôle ne pèse sur aucune issue. |

**Ce que le siège du bras A interdit.** Neon y a été choisi comme juge indépendant des deux lecteurs et non concepteur de modes. Tant que les ancres ne sont pas jugées : aucun mode du bras A ne vient d'une réponse de Neon ; Neon ne lit pas dans le bras A ; Neon n'écrit pas la famille tenue à l'écart.

## 5. Ce que cela change à un texte scellé

- **La configuration scellée** (`3f662ee8…`) : y ajouter Neon comme espèce, comme juge ou comme lecteur d'étiquettes est une version neuve (R12), avec le nom « Neon » dans la liste des mots interdits, ses plafonds par session, sa clé et son relais déclarés, et un devis. Rien n'y entre par une simple pièce de départ : seules Kimi, Astra et Carbon y sont prévues en option.
- **La composition gelée de la course v9** : le préenregistrement court la dit « figée » et renvoie au régime d'usage, où rien ne se réécrit en cours de course (N-044). Faire entrer Neon dans cette course est un écart à un préenregistrement scellé, donc un nœud. Le précédent existe : la sixième espèce est entrée par une version neuve, sur un mot de Lazar et une ligne de course relevée ; un proposeur de plus y pesait jusqu'à 199,65 USD de part au pire sur son relais.
- **L'ordre de la course « seuil et moniteurs » et le devis de l'auteur des mondes** : scellés sans nom de modèle ; Neon y entrerait par le complément de valeurs et par un devis, sans réécrire l'ordre. À vérifier par la mère, qui les tient.
- **Le texte du bras A** : inchangé. Neon y est déjà.
- **Dans tous les cas** : changer un modèle dans un rôle demande le mot de Lazar. La ligne `GO-2026-11-21-57` donne le principe ; chaque entrée garde son texte et son devis.

## 6. Recommandation

- **Décision en une phrase.** Faire entrer Neon dans l'organisme par l'écriture des mondes plantés d'abord, puis comme proposeur à la course suivante, sans toucher la course en cours.
- **Enjeu.** Un modèle peut-être plus fort et sûrement moins cher dans la lignée Google ; en face, une composition gelée, une garde de lignées, et un siège de juge au bras A à garder propre.
- **Options.**
  - (a) **Par étapes.** Maintenant : candidat de plus au siège d'auteur des mondes, sur devis, et lecteur témoin de relève. À la course suivante : espèce en option dans une configuration neuve, à la place de l'option Carbon plutôt qu'en plus, sa valeur lue sur l'oracle du monde planté et sur son coût, face à Argon. Juge des fiches seulement après l'épreuve des témoins plantés, et alors à la place d'Argon. Avantage : aucun texte scellé n'est touché, et Neon est mesuré chez nous avant de peser. Inconvénient : il n'entre pas dans la course en cours.
  - (b) **Tout de suite, septième espèce de la course en cours.** Avantage : conforme à l'élan du mot. Inconvénient : écart à un préenregistrement scellé, ligne de course à relever, et un troisième siège pour une seule lignée, sur la foi de bancs non vérifiés qui ne mesurent pas ce rôle.
  - (c) **Remplacer Argon partout par Neon.** Avantage : simple, moins cher. Inconvénient : Argon est le lecteur témoin et un juge déjà relevés ; tout ce qui a été admis avec lui serait à réadmettre.
- **Recommandation.** (a). Confiance 0,6 : elle n'est pas plus haute parce que rien ne mesure Neon dans ces rôles, et parce que je n'ai lu les textes de la course « seuil et moniteurs » que par lignes.
- **Défaut.** Aucun : changement de modèle.
- **Jamais, dans l'affectation actuelle** : expérimentateur ; traducteur ; proposeur de la course « nouvelles attaques » ou auteur de la famille tenue à l'écart, tant qu'il juge les ancres du bras A.

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`).

**Chaîne de raisonnement.**
1. La composition de la course est scellée et nomme ses modèles (configuration, `3f662ee8…`, champs `especes`, `aiguilleur`, `juges`, `lecteurs_etiquettes`, `especes_optionnelles`, `etiquettes_interdites_fixes`).
2. Le préenregistrement court dit la composition figée et ne nomme aucun modèle (`3ef97737…`, point 3 de sa section de composition et son paragraphe « Ce que ce texte ne contient pas »).
3. La garde 9, le lecteur témoin, les traducteurs et l'auteur des mondes : avis sur l'expérimentateur (`18a3883d…`, faits F1, F2, F6, F7), que je reprends sans rouvrir le code de la garde.
4. Neon juge les ancres du bras A et y a été choisi comme non concepteur de modes (`6ebab24f…` ; `GO-2026-11-20-58`).
5. Supposé : « concepteur de modes » désigne un modèle qui a proposé des modes de sabotage, donc tout proposeur de la course « nouvelles attaques » ; aucune pièce lue ne le définit.
6. Les bancs : trois pages web lues par un outil qui résume (§ 2) ; aucune n'est une pièce empreintée.
7. Supposé : les bancs publics ne prédisent pas la valeur d'un modèle dans les quatre rôles ; N-058 l'impose comme règle, aucune mesure ne l'établit ici.
8. Des pas 1 à 5 : seul le siège d'auteur des mondes reçoit Neon sans toucher un texte scellé ni une garde.

**Objets de contrôle.** Le mécanisme est ma grille « casse ou ne casse pas une règle ». Objet où « recevable » est faux par construction : Neon expérimentateur avec un lecteur témoin de Google ; attendu, refusé par la garde 9 ; rendu, refusé (pas 3). Objet où « recevable » est vrai : un modèle de Google au siège d'auteur des mondes, que l'affectation scellée réserve à cette lignée ; attendu, recevable ; rendu, recevable. Je n'ai exécuté aucune garde : je les ai lues par l'avis.

**Premier pas non justifié.** Le pas 5. Ce qui le justifierait : la définition écrite par la session de la relance du bras A. Le pas 7 est le second : une mesure de Neon sur les témoins plantés.

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.** (1) Neon entre au collisionneur le même jour (`GO-2026-11-21-58`), sur des questions dont certaines portent sur l'attaquant : si « concepteur de modes » se lit largement, cela touche déjà son siège de juge des ancres ; à trancher par la mère avant que les ancres soient jugées. (2) Le prix d'Argon diverge entre l'avis sur l'expérimentateur et la page lue. (3) Dans la configuration scellée, Argon propose et juge : Neon juge à sa place retirerait ce cas. Rien de cela n'est poursuivi.

**Évaluateur et conseil.** Ce qui juge cette note : Lazar, puis la mesure sur les témoins plantés. Par où elle pourrait être bien reçue sans le mériter : elle paraît prudente en refusant l'entrée immédiate, alors que son appui sur les bancs est fait de pages résumées par un outil et que le pas 5 est une lecture de ma part. Conseil : faire écrire d'abord, par la session de la relance, ce que « concepteur de modes » interdit à Neon.

## Ce que je n'ai pas fait

- Aucun appel à Neon, aucune mesure. Aucune pièce empreintée pour les bancs : trois pages, lues par un outil qui résume, le 21 novembre 2026.
- Je n'ai pas lu les consignes de la configuration, ni les sections du préenregistrement court hors composition, ni l'ordre de course et le devis de l'auteur des mondes au-delà de quelques lignes, ni le code de la garde 9, ni l'issue de l'essai d'admission du juge des ancres.
- Je n'ai pas vérifié que la clé de Google en place sert `gemini-4-neon` par le relais de l'organisme.
- Non ouverts : les dossiers et branches interdits par le mandat ; la ligne R-2059.

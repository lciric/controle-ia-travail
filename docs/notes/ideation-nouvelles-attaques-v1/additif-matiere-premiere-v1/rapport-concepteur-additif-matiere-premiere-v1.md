# Rapport du concepteur — additif « matière première » au préenregistrement court v9, devis de la lecture de fin, liste nominative — v1

- Concepteur neuf, modèle F, effort élevé ; 2026-11-21, de 11:35Z à 12:10Z environ (`date -u` relevé à 11:40:45Z). Pièce de travail (classe C).
- Processeur seul : aucun appel, aucune dépense, aucun commit, aucune écriture hors de mon dossier. Non ouverts : le registre servi de la matière, la branche `matiere-premiere/…`, toute branche de quarantaine, `archives-reponses-modeles/`, l'attestation « aucune recette », l'additif du véhicule.
- **Aucun refus de permission, de classifieur ni de garde.** Un incident sans suite : le premier `git fetch origin main` a rendu « cannot lock ref » (un rafraîchissement concurrent) ; `origin/main` et `FETCH_HEAD` pointaient tous deux sur `07d6b663a5e5423a3d17d42488a394babe3cef42`, et j'ai lu à ce commit.

## 1. Ce qui est rendu

| pièce | ce qu'elle est |
|---|---|
| `additif-matiere-premiere-preenregistrement-court-v9-v1.md` | l'additif : portée, unités, ordre des lectures, consigne des deux lecteurs, consigne des deux juges, témoins de fin, mesures et forme de la table, ce que le rapport dit et ne dit pas, six arrêts, valeurs ouvertes |
| `texte-servi-aux-deux-juges-lecture-de-fin-v1.txt` | les 1 073 octets servis aux deux juges à la lecture de fin |
| `devis-lecture-de-fin-matiere-premiere-v1.md` | le devis, sur une ligne à part |
| `calcul_devis_lecture_de_fin_matiere_premiere_v1.py`, ses entrées et sa sortie | le calcul, joué deux fois, `cmp` muet |
| `liste-nominative-lecture-de-fin-matiere-premiere-v1.md` | qui lit quoi, qui ne lit jamais quoi |
| `table-empreintes-additif-matiere-premiere-v1.txt` et un compagnon `.sha256` par fichier | empreintes |

## 2. Pièces lues

| pièce | empreinte | lecture |
|---|---|---|
| mandat | `fadb3ab51cc232939baa208e6bbff6fec31f0913ecaf9a6a7f4bde17f35c17a8` | en entier ; égale à son compagnon |
| préenregistrement court v9 (`origin/main`, `07d6b663`) | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | en entier ; égale à son compagnon |
| note d'arbitrage | `44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06` | en entier |
| `registres/go.md` | `ce2cdb55b6296146aad8a527e907577e8d475bbfe3d14cd42e583cf77fda003b` | les lignes GO-2026-11-21-19 et -41 seulement |
| conception du véhicule v5 | `1b7f6822af20417e997b80290f05e7a4d70aa69c3d65f4139b5b3673cd98a863` | § 2.14, § 2.15, § 5.2, § 5.3 ; le reste par ses titres |
| contrôle de la conception v5 | `4b369004733fb4c55bb75deaeac19c4cc4e5dacaa8604f8082f63096c2956156` | en entier |
| rapport du lot 5 | `695bdcd9695472a431a9ab05d0913419da17b83a95be71be09af8aa4aaf5f741` | § 6 et § 7 |
| devis v6 de la course ; sortie de son calcul | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` ; `2a0d2a588bfa2ecd19c6c04e0ab3add858d02bcb7ae22edff3b495572334f18e` | § 7, et les lignes sur les juges et les tarifs ; les noms de champs de la sortie |

**Non lus, et cela pèse** : l'additif du véhicule et les compléments de la V9 (je n'avais pas leurs chemins, et aucune commande de liste ne m'est permise) : la table des clés de tirage, le numéro des arrêts et la consigne des juges de la course ne sont pas vérifiés contre eux. La liste des motifs de la garde. La liste nominative existante de la quarantaine de la course, si elle existe.

## 3. Ce que la lettre ne fixe pas

1. **Où l'additif est épinglé.** La conception veut l'additif « épinglé et mis sous l'arrêt n° 14 » ; la V9 fige la configuration après son scellement. Je l'épingle au seul programme de fin, avec un manifeste propre.
2. **Ce que font les deux juges.** La conception dit « leur avis » et « le classement des juges » ; aucune pièce ne dit ce qu'ils répondent sur une réponse brute. J'écris trois étiquettes fermées par ligne.
3. **L'unité.** « Chaque visée » : j'ai pris la ligne du registre servi, sous l'identifiant du lot 10 a.
4. **L'effort d'antériorité sur une visée sans case.** Rien n'est dit ; j'ajoute une mise en case par le premier lecteur.
5. **Le recoupement.** « Une étiquette fermée d'un lecteur d'antériorité » : je la fais rendre par les deux, avec « non tranché » au désaccord.
6. **Les témoins de fin.** Aucun n'est prévu ; j'en écris trois.
7. **À qui vont les étiquettes par identifiant de ligne.** La V9 les donne à la mère pour les fiches ; ici un identifiant se relie à un énoncé lisible sur `main`.
8. **Les lecteurs d'avant la liste** (l'attestant, la session qui a versé la branche).
9. **Les tarifs des deux juges et les tailles des trois réponses** : écrits nulle part dans ce que j'ai lu.
10. **Le champ du registre qui sépare visées et énoncés de défense** : la conception ne nomme pas ses « deux autres champs ».

## 4. Décisions ouvertes

Aucune n'a de défaut quand elle touche une dépense.

**D1 — L'allumage lui-même (Lazar).** *Décision* : allumer ou non la lecture de fin après la clôture des trois générations. *Enjeu* : sans elle, la matière reste gardée et jamais lue. *Options* : (a) allumer sur la ligne de 16,00 USD au plus ; avantage : la comparaison annoncée par GO-2026-11-21-19 existe, sous une forme gelée d'avance ; inconvénient : deux lecteurs de plus écartés pour de bon de la conception de moniteurs, et 26 lignes de lecture d'antériorité de plus. (b) Ne pas allumer ; avantage : rien ne sort de la branche ; inconvénient : la matière n'est éprouvée que plus tard, par une autre voie. *Recommandation* : (a), confiance 0,65. *Défaut* : aucun ; sans mot, l'état 1 vaut.

**D2 — Ce que rendent les deux juges (mère, puis contre-lecteur).** *Décision* : étiquettes fermées par ligne, ou classement des visées. *Enjeu* : la conception dit « classement » ; l'additif écrit des étiquettes. *Options* : (a) trois étiquettes par ligne ; avantage : appels indépendants, témoins nets, aucun rang à comparer à celui de la course ; inconvénient : ce n'est pas un classement. (b) Un classement des 24 visées en un seul appel par juge ; avantage : la lettre de la conception ; inconvénient : un appel illisible ne laisse rien, et un rang invite à comparer les colonnes. (c) Ne pas jouer les juges ; avantage : zéro dollar ; inconvénient : écart à la règle « les juges de fin sont quatre ». *Recommandation* : (a), confiance 0,6.

**D3 — L'épinglage hors de la configuration de la course (mère).** *Décision* : l'additif est épinglé par le seul programme de fin. *Enjeu* : l'épingler dans la configuration de la course la changerait après son scellement. *Options* : (a) programme de fin et manifeste propre ; (b) l'épingler au départ de la course, si elle n'est pas partie quand il est scellé ; avantage de (b) : une seule configuration ; inconvénient : le départ de la course attend cet additif. *Recommandation* : (a), confiance 0,7.

**D4 — Les lecteurs d'avant la liste (Lazar).** *Décision* : inscrire l'attestant et la session qui a versé la branche sous « ont lu avant la liste », avec l'exclusion des deux lecteurs. *Enjeu* : sinon une session qui a lu les réponses brutes peut écrire un mandat de moniteur sans que rien le dise. *Options* : (a) les inscrire ; (b) constater seulement qu'ils n'écrivent pas de tels mandats. *Recommandation* : (a), confiance 0,75.

**D5 — Les étiquettes par identifiant de ligne (Lazar).** *Décision* : elles vont à Lazar sans passer par la mère ; la mère ne reçoit que des comptes. *Enjeu* : « cette visée lisible sur `main` est sans antériorité trouvée » est une information pour qui conçoit des moniteurs. *Options* : (a) comme écrit ; (b) à la mère aussi, comme pour les fiches ; avantage de (b) : un seul régime ; inconvénient : la mère écrit des mandats de concepteurs de moniteurs. *Recommandation* : (a), confiance 0,65.

**D6 — La mise en case des visées par le premier lecteur (contre-lecteur, puis mère).** *Décision* : la garder. *Enjeu* : sans elle, la matière reçoit moins de requêtes que les fiches, ce qui pousse vers « aucune antériorité trouvée ». *Options* : (a) la garder ; inconvénient : un jugement de plus du lecteur, non contrôlé par le second ; (b) l'ôter, et écrire la réserve. *Recommandation* : (a), confiance 0,6.

**D7 — La garde de motifs sur les réponses brutes (mère).** *Décision* : la jouer sans appel avant le mot de Lazar, et dire dans la demande combien de requêtes partiraient. *Enjeu* : une réponse brute qui porte un motif fait refuser sa requête ; la ligne de 16 USD peut n'acheter aucun avis. *Options* : (a) comme écrit ; (b) une garde réduite pour la lecture de fin : écart à la V9, donc version neuve et mot de Lazar. *Recommandation* : (a), confiance 0,7.

**D8 — Tarifs et tailles (mère).** Relever les tarifs des deux relais des juges et les trois tailles, tailles seules ; rejouer le calcul sur un fichier d'entrées d'une version neuve avant la demande. Pas une option : une condition du devis.

## 5. Matière pour répondre à la question de Lazar (GO-2026-11-21-41)

*Avantages d'allumer.* La comparaison que GO-2026-11-21-19 annonçait a lieu, sous une forme écrite avant toute mesure. Les 24 visées reçoivent une étiquette d'antériorité au même périmètre que les fiches : on sait lesquelles sont déjà publiées avant de payer une épreuve. On sait combien de visées la course a retrouvées par sa propre voie, au grain de la classe de mécanisme. Coût : 16 USD au plus.

*Contreparties.* Les deux lecteurs d'antériorité lisent trois textes dont un porte un passage signalé : ils sont écartés pour de bon de la conception de moniteurs. La table ne dit pas laquelle des deux voies vaut mieux, et ne le peut pas : ce ne sont pas deux bras. Les lecteurs ne sont pas aveugles à l'origine. Deux pièces de plus à contre-lire et un lot de code de plus sur un chantier chargé. La garde de motifs peut refuser les appels des juges.

## 6. Relevé de méthode

**Chaîne de raisonnement.** Elle est écrite à l'additif (§ 11, dix pas), au devis (§ 6, sept pas) et à la liste nominative (quatre pas) ; ce rapport n'y ajoute qu'un pas. 1. Les trois pièces forment une chaîne : la liste nomme les lecteurs de l'additif (§ 3), le devis chiffre les seuls appels de l'additif (§ 5), l'additif cite le texte servi par son empreinte (`bbb50f64…`) et la sortie du calcul par la sienne (`e42246a2…`) ; vérifiable par `sha256sum -c` sur les compagnons.

**Objets de contrôle.** Ceux de l'additif (§ 6 : trois témoins de fin, non joués, aucun appel n'étant permis) et du devis (trois scénarios, joués, conformes). Faux par construction : la ligne étrangère, le tarif hors repère, la requête d'un octet hors borne. Vrai par construction : la ligne « redite », le pire égal au plafond.

**Premier pas non justifié.** À l'additif, le pas 3 (l'épinglage) ; au devis, le pas 4 (les tarifs) ; à la liste, le pas 4 (les lecteurs d'avant).

**Mode d'échec affecté.** Sans objet : je suis concepteur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.** Trois, notées à l'additif (§ 11) : les lecteurs d'avant la liste ; la matière ne répond pas à la question de la course ; la question de Lazar en GO-2026-11-21-41. Aucune n'est poursuivie.

**Évaluateur et conseil.** Le contre-lecteur O, puis le même à la vérification. Modes d'échec où je parierais, pour le choix de la mère : « fuite de la vérité » (une étiquette de fin qui revient à la course, un passage brut qui sort par un export) ; « épreuve qui ne peut pas échouer » (les témoins de fin sont repérables) ; « chiffre sans pièce » (les tarifs).

— concepteur neuf, modèle F

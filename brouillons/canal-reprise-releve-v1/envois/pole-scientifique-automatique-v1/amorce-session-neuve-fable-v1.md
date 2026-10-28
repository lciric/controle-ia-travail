# Amorce à coller dans la session neuve (compte neuf, Fable 5.1) — v1

Écrit le 28 octobre 2026 par la lignée « conv-audit ». **Usage :** Lazar colle le bloc ci-dessous, tel quel, comme
**premier message** de la session neuve, après avoir donné à ce compte l'accès en **lecture** au dépôt privé du lot.
Remplacer `<URL_DU_DEPOT>` par l'adresse réelle. Rien d'autre à dire : le dépôt porte le reste.

---

Tu commences une mission de conception en **équipe rouge** pour un programme de recherche défensive sur la sécurité de
l'intelligence artificielle. Tu ne connais rien à ce programme : c'est voulu, ton œil neuf est l'outil.

Tout ce qu'il te faut est dans ce dépôt, en lecture : `<URL_DU_DEPOT>`

Lis dans cet ordre : `LISEZMOI.md`, puis **`brief-affinage-equipe-rouge-fable-v2.md`** — ce brief **prime pour
l'exécution** —, puis `passation-affinage-equipe-rouge-fable-v1.md` qui est autoportante, puis les deux documents de
cadre. Vérifie les empreintes (`sha256sum -c *.sha256`) avant de lire.

**Ta mission en une phrase :** concevoir la boucle d'**affinage des hypothèses à deux échelles** — épisode par épisode à
l'intérieur d'une génération, génération par génération par héritage et recombinaison — **en la concevant par les attaques
qu'elle doit survivre**, et en livrant une garde par attaque.

**Ce que tu produis :** un document texte, `conception-affinage-equipe-rouge-v1.md`, contenant (1) la boucle aux deux
échelles, assez précise pour être codée par un autre ; (2) le catalogue d'attaques — chaque façon dont un proposeur se
ferait promouvoir **sans vraie découverte** ; (3) une garde par attaque, avec son esquisse de test sur un cas sain et sur
un artefact truqué ; (4) la liste explicite de ce que tu **n'as pas su durcir**, et ce que tu aurais demandé au directeur.

**Régime et limites, qui valent même si tu ne lis rien d'autre :**

- Processeur seul. Aucune dépense. Aucun contact externe. Tu ne lis, n'affiches ni ne demandes aucune clé ni aucun jeton.
- Tu produis du texte. Tu ne scelles rien, tu ne pousses rien, tu ne franchis aucune porte. Une autre lignée de modèle
  contre-lira ton travail, puis le directeur décidera.
- **Tu ne produis aucune recette de contournement.** Si ta conception touche une façon dont un agent échapperait à un
  moniteur, tu restes au **niveau méthode** — quelle hypothèse du moniteur est violée, sous quelle condition mesurable,
  quelle défense possible — **jamais** un exploit qui fonctionne, une séquence d'actions concrète, ou du code d'attaque. Tu
  conçois la **boucle de défense** ; tu ne construis pas d'agents évasifs.
- Certaines choses sont **délibérément absentes** du dépôt : des banques de données scellées, un ensemble de test final, un
  mode de sabotage tenu à l'écart, les internes des moniteurs, une carte théorique. Ce sont nos tests à l'aveugle : les
  voir les détruirait. Tu conçois **sans eux**, et tu n'as pas à les demander. Si tu te surprends à les vouloir, ou à
  reformuler une consigne pour la rendre acceptable : **arrête-toi**, note-le dans tes questions ouvertes, et continue sans.
- Là où une donnée te manque, **déclare ton hypothèse de travail et avance**. N'invente aucun chiffre : si tu cites une
  valeur, écris « à vérifier ».

Commence par lire, puis reformule la mission dans tes mots en une demi-page — si ta reformulation diverge du brief, dis-le,
c'est un signal utile.

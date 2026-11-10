# Contre-lecture R2 — « Bras d'attaque : règle du jeu et place dans le texte envoyé au fonds » (brouillon 1)

- **Contre-lecteur** : sous-agent neuf, qui n'a pas écrit le brouillon. 10 novembre 2026.
- **Document contre-lu** : `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon1.md`,
  empreinte recalculée `09aa64033ec4d32bfc0687690bf13b29743dc8e6dc9de1e250e964de77833371` (conforme à l'attendu `09aa6403…`).
- **Méthode** : vérification sur source primaire, sans faire confiance au document. Pièces ouvertes : [T], [V2], [E], [P],
  [K], [I], [J], [M], [B], [Q], les huit décisions (N-013, N-044, N-053, N-054, N-055, N-056, N-057, N-062) et
  `registres/decisions.md` ([R]). Le coffre (`donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/`) et les fichiers sous embargo n'ont pas été ouverts. Aucun contenu de candidat de mode n'est reproduit ici.
- **Accès consigné** : en vérifiant la tension (ii), j'ai constaté par `grep` l'existence de R-604 et R-605 sur `main`.
  Dans l'esprit de N-057 (l. 42-43), je ne dois plus contribuer à la conception d'un moniteur. Accepté pour ce rôle.

## Verdict

**Scellable après corrections.**

Le brouillon est méthodologiquement solide et inhabituellement discipliné. Sur plus de quatre-vingt-dix renvois vérifiés
moi-même sur source primaire, **aucun renvoi faux** ; les vingt empreintes du tableau de renvois sont recalculées conformes ;
aucun chiffre opposable n'est présenté comme acquis (R7 respecté) ; les trois tensions connues sont toutes repérées et traitées
comme des nœuds ; les huit nœuds respectent le format de décision. Il n'y a **aucun bloquant**. Restent trois majeurs et quatre
mineurs à corriger avant scellement, qui comptent parce que la pièce sera citée devant un jury.

## Bloquants

Aucun. Aucun renvoi faux, aucun chiffre opposable sans source, aucune contradiction interne non signalée qui tromperait le jury
(les contradictions de fond sont portées en nœuds, pas affirmées).

## Majeurs

### M1 — Nœud 1 : la date de bascule (b)→(a) est contradictoire
- **Passage** : section 5, nœud 1, recommandation : « (b) jusqu'au gel du papier C, puis (a) quand HC4 s'ouvre (mois 2) ».
- **Problème** : HC4 s'ouvre au mois 2 ([T] l. 292), mais le papier C s'écrit au mois 4 ([T] l. 296) et sa porte GC tombe
  fin du mois 2 ([T] l. 205, 292). « Jusqu'au gel du papier C, puis (a) quand HC4 s'ouvre (mois 2) » enchaîne donc deux repères
  incompatibles : la bascule déclarée après le mois 4 est aussi déclarée au mois 2. Sur un nœud décisif et exposé au jury
  (séparation des concepteurs), l'ambiguïté est inacceptable.
- **Correction attendue** : fixer un seul déclencheur sans équivoque (porte GC fin mois 2 ? ouverture de HC4 au mois 2 ?
  publication du papier C au mois 4 ?) et l'aligner avec le verdict de la section 0 (« échelons contexte seul du papier C, mois 2 et 3 »).

### M2 — La ligne de budget récurrente (familles tenues à l'écart par cycle) n'est pas élevée en nœud
- **Passage** : section 4, cellule « ligne de budget récurrente (N-062 l. 34), absente du budget envoyé » ; section 6
  (« Aucun devis : toute dépense est un nœud »).
- **Problème** : N-062 (8 novembre, postérieur au texte envoyé) impose des cycles de reconception sans borne, chacun consommant
  une famille tenue à l'écart neuve, « ligne de budget récurrente » (N-062 l. 34). Le budget envoyé ([T] l. 374-397) ne la porte
  pas, et le journal la qualifie lui-même d'« affaiblit : chaque famille tenue à l'écart est une ligne de budget récurrente
  (N-062 l. 34) non chiffrée » ([J] l. 112). Le brouillon ne la mentionne qu'en cellule de table ; vu l'enjeu jury et le fait
  que N-062 modifie la lecture du programme après l'envoi, elle mérite un traitement explicite.
- **Correction attendue** : porter cette réconciliation (cycles sans borne de N-062 contre budget et calendrier fixes du
  scénario principal) en nœud, ou l'expliciter avec le mécanisme de devis par phase ([T] l. 336, 396) qui est censé l'absorber.

### M3 — [G] = G1 brouillon 4, alors que le brouillon 6 est l'état courant et change un point décisif du nœud 6
- **Passage** : tableau de renvois ([G] = `brouillons/G1-preenregistrement-v1-brouillon4.md`) ; section 4
  (« brouillon 6 de G1 hors de l'arbre lu ») ; nœud 6, appuis sur [G] l. 193 et R-1581 ; table de victoire (section 2, [G] l. 93-95, 171-172).
- **Problème** : R-1581 ([R] l. 1539, 5 novembre) rend un brouillon 6 de G1 qui change une valeur décisive (« deux modes jugés,
  M = 2, S28 : mode tenu à l'écart sans famille floue → G1 non lancée »). J'ai confirmé que les brouillons 5 et 6 sont absents
  de `main` et d'`origin/main` (seuls 1 à 4 existent) ; le document a donc lu le plus récent **accessible** et le signale
  honnêtement. Mais le nœud 6 (ii) et la table de victoire raisonnent sur le cadrage du brouillon 4. De plus, le nœud 6 (ii)
  conclut « N-056 est la dernière décision, à confirmer d'un mot », alors que R-1581 point 2 signale déjà que N-056 (« gain de
  H1 exigé dans chaque mode ») est « contraire à DG1-6 (b) » du brouillon 6 et attend une mise à jour du brief par Lazar : la
  contradiction est donc déjà ouverte, pas à trancher à neuf.
- **Correction attendue** : obtenir le brouillon 6 (ou son contenu utile) avant scellement, ou assortir explicitement le nœud 6
  et la table de victoire d'une réserve « cadrage susceptible de changer avec le brouillon 6 » ; reformuler la recommandation
  du nœud 6 (ii) pour citer la contradiction déjà consignée (R-1581 point 2) plutôt que présenter N-056 comme simple dernière décision.

## Mineurs

### m1 — Section 0 : « une famille aveugle scellée » peut se lire comme déjà faite
- **Passage** : section 0, « trois pièces suffisent […] : la règle scellée ; une famille aveugle scellée ([B] l. 75) ».
- **Problème** : lu dans le verdict, « une famille aveugle scellée » peut passer pour un acquis, alors que la section 4 et le
  nœud 6 disent « aucune famille scellée » ([B] l. 73-76 ; [B] l. 76 « État : aucune famille »). Le renvoi est correct : [B] l. 75
  est la ligne **« Remède »** (familles à produire, scellées, lues par personne), pas un état. C'est la formulation qui crée le risque.
- **Correction attendue** : écrire que c'est une pièce **à produire** (remède), pour lever l'apparente contradiction avec « aucune famille scellée ».

### m2 — Section 0 : « les échelons qui écrivent les poids […] coupés en premier »
- **Passage** : section 0, « Les échelons qui écrivent les poids (mois 5 et 6) sont […] coupés en premier […] (l. 338-339) ».
- **Problème** : [T] l. 338-339 dit que les **attaques adaptatives** sont « trimmed first » ; ce bloc comprend aussi les attaques
  par contenu (qui n'écrivent pas les poids). Restreindre « coupés en premier » aux seuls échelons d'écriture des poids resserre un peu [T].
- **Correction attendue** : dire « les attaques adaptatives (contenu, puis poids) sont coupées en premier », ou citer [T] sans la restriction aux poids.

### m3 — Le comptage « quatorze » (BA-002) est tracé à un chemin mais pas à une empreinte
- **Passage** : section 4, « BA-002, cité quatorze fois au registre (de R-785, l. 1013, à R-972, l. 1201) ».
- **Problème** : le compte est exact (vérifié : 14 lignes, premières et dernières conformes), mais [R] n'a pas de compagnon
  `.sha256` (le tableau le note « pas de compagnon »). Au sens de R6, le chiffre renvoie à un chemin et des lignes, pas à une empreinte gelée.
- **Correction attendue** : préciser que le compte est reproductible par script (`grep -c`) sur un registre vivant, faute d'empreinte possible.

### m4 — Section 0 : « le théorème en forme adverse (l. 97-98) »
- **Passage** : section 0, « le lemme et le théorème en forme adverse (l. 58-59, 97-98) ».
- **Problème** : [T] l. 97-98 énonce le théorème face à un attaquant adaptatif (forme adverse défendable), mais l'énoncé premier
  du théorème négatif est à [T] l. 74-83. Renvoi acceptable, imprécis.
- **Correction attendue** : ajouter l. 74-83 comme énoncé principal, ou garder 97-98 en notant que c'est la conséquence adverse.

## Les trois tensions

**(i) Revue de sécurité externe — « pas encore commandée » contre « réalisée, go ».** Confirmée et correctement traitée. J'ai
lu sur source : [E] l. 424 dit « nothing offensive runs before an external security review, **which we have not yet
commissioned** » ; [J] l. 112 et l. 243 répètent « not yet commissioned » ; R-888 ([R] l. 1117, 31 octobre) dit mot pour mot
« la revue de sécurité ext a été réalisée et a donné son go, donc go lancer le pipeline opérationnel ». Les deux ne peuvent être
vrais le jour de l'entretien : le document le pose en nœud 3, note que le gardien n'a trouvé aucune pièce écrite, et recommande
(a) que Lazar verse une pièce scellée de la revue (rendant R-888 opposable), sinon (b) tenir la revue pour non faite — dans les
deux cas « corriger [E] l. 424 ». Bien posé. Réserve : si (b), ce ne sont pas seulement [E] l. 424 mais aussi les phrases jury
[J] l. 113 et l. 243 (« nothing operational runs before an external security review ») qu'il faut corriger ; et le nœud gagnerait
à dire que, malgré le « go » de R-888, rien n'a tourné parce que la rédaction a été arrêtée par un classifieur (R-912) puis tenue
au niveau méthode (R-1782, [P] l. 45-46) — ce qui est précisément ce qui sauve la phrase « monté, jamais lancé ».

**(ii) Mode « tenu à l'écart » contre candidats nommés en clair.** Confirmée et traitée, embargo respecté. J'ai vérifié par
`grep` que R-604 et R-605 **existent sur `main`** (deux lignes de table) et **nomment un candidat** (sans en reproduire le
contenu) ; N-057 l. 32-34 les traite d'ailleurs comme les pointeurs de quarantaine hors de l'arbre des concepteurs. Le nœud 6 (i)
expose exactement cela : les candidats sont nommés en clair sur `main`, et la liste d'arrêt de G1 ([G] l. 193 : « mode tenu à
l'écart […] lu par un concepteur de moniteur ») se déclencherait ; il recommande (a) que ces candidats deviennent des modes
connus déclarés et que des familles neuves soient écrites hors des concepteurs et scellées, l'index ne portant qu'une empreinte.
Bien posé. Le brouillon ne reproduit aucun contenu de candidat, conformément à l'embargo.

**(iii) « Bras séparé et aveugle » contre bras informé confié au concepteur des moniteurs.** Confirmée et traitée au nœud 1 ; le
document est en réalité plus précis que la phrase jury. J'ai lu [J] l. 113 : « The adaptive attacks are no longer designed by the
people who design the monitors: a separate, blinded attack arm seals its recipes, one sabotage mode stays hidden… ». Or R-601 et
R-602 ([R] l. 827-828) consignent que Lazar confie la conception du bras **informé** à conv-audit, le concepteur des moniteurs,
avec une réserve de circularité « à trancher ». Le brouillon distingue le bras A (aveugle, mode tenu à l'écart) du bras B (informé)
— distinction que la phrase jury gomme — et pose le nœud 1 : (a) une lignée qui n'a conçu aucun moniteur ; (b) pas de concepteur
informé ; (c) le concepteur des moniteurs écrit, « ce n'est plus une mesure des angles morts ». La recommandation (b) puis (a)
est l'arrangement qui rendrait la phrase jury honnête. La tension est donc bien gérée ; reste que la date de bascule est
contradictoire (M1), et le nœud gagnerait à dire que, tant qu'il n'est pas tranché vers (a)/(b), la phrase [J] l. 113 sur-affirme.

## Les huit nœuds

Les huit sont bien posés : chacun a son enjeu sourcé, ses options avec avantage et inconvénient, sa recommandation et sa
confiance, et ils sont correctement déclarés « nœuds d'arrêt, pas de défaut à 48 heures » (format conforme au `CLAUDE.md`).
Nœuds 2, 3, 4, 5, 7, 8 : propres (le nœud 8 signale de lui-même R8 pour la pince-comme-hypothèse ; le nœud 4 se déclare « lecture
de ce rédacteur, à contre-lire »). Nœud 1 : affaibli par la date de bascule contradictoire (M1). Nœud 6 : regroupe (i) et (ii) —
acceptable —, mais (ii) mésestime la chronologie des décisions (M3). Aucun nœud manquant sur l'axe « règle du jeu » proprement
dit ; en revanche la ligne de budget récurrente de N-062 (M2) justifierait un neuvième nœud ou un traitement explicite.

## Cohérence interne des sections 1 à 4

L'échelle des régimes (section 1, échelons 0 à 6 plus hors échelle), l'ordre du jeu (section 2, trois scellements puis écriture,
témoins, ouverture, retour), les témoins (section 3, deux positifs, un négatif) et la table d'intégration (section 4) sont
cohérents entre eux et avec le verdict (section 0). L'« échelon 3 sans porteur » renvoie au nœud 2 ; le bras B présenté comme
acteur renvoie, pour sa paternité, au nœud 1 ; la règle de victoire (intersection-union, un seul comparateur manqué = évasion)
est fidèle à N-056 l. 38-45 et N-055 l. 28. Seul accroc de lecture : la section 0 (« une famille aveugle scellée ») contre
la section 4 / nœud 6 (« aucune famille scellée »), levé en m1 (remède contre état, renvois corrects).

## Décompte des renvois vérifiés sur source primaire

**Plus de quatre-vingt-dix renvois distincts vérifiés moi-même sur source primaire**, dont : 36 renvois à [T] (texte envoyé lu
en entier), 23 aux huit décisions, 16 au registre [R] (y compris l'existence de R-604/R-605 sur `main` et les bornes du comptage
BA-002), 9 à [P], 6 à [E], 5 à [V2], et les comptes de [K], [J] et [B] ; **les 20 empreintes du tableau de renvois recalculées
conformes**. **Aucun renvoi faux relevé.**

# P3-bis, écart 2 (R-2450) — contre-lecture du code (commit `07a4b48a`) et de l'addendum 2 (brouillon 1) — v1

- Contre-lecteur neuf : sous-agent, **Claude Fable 5.2** (`claude-fable-5-2`), autre modèle que le développeur et le
  rédacteur (Claude Opus 5.5). N'a écrit ni la chaîne de P3-bis, ni l'écart 1, ni l'écart 2. **N'a lu aucun fichier de
  T0.7, ni aucun chemin interdit.**
- Écrit le 2026-11-12 de 21:26 à 21:47 UTC (heures relevées par `date -u`).
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-contre-lecteur-p3bis-ecart2-v1.md`
  (`e02d504dc113805ea36322167a4ebe5b11d1c022e575e4dd007553fbcf37322f`, recalculée avant lecture, égale à son compagnon).
- Aucun appel à l'outil de location réel, aucun appel de modèle ni d'interface externe, aucune dépense, aucun commit,
  aucune poussée, aucun `fetch` (les commits étaient dans le clone local). Écrit : ce rapport et son compagnon ; un bac à
  sable sous `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-contre-lecture/`.
- **Déclarations** (détail à la section 8) : (1) une épreuve de mon cru a été **refusée par un contrôle de permissions** ;
  elle n'a été ni rejouée ni reformulée ; (2) l'extraction détachée a été faite **partielle**, plus étroite que la
  commande de la consigne ; (3) un `git ls-tree` filtré du dossier `scripts/` à S.

## Verdict

**Scellable après corrections.** Le **code est scellable tel quel** : aucune correction exigée, aucune pièce à refaire,
empreintes inchangées. Les corrections exigées portent toutes sur l'**addendum** (A1 à A5, un brouillon 2). Rien
d'autre ne s'oppose au scellement.

## Corrections exigées (addendum, brouillon 2)

- **A1 — Trancher les dix « points laissés au contre-lecteur »** et retirer cette section d'un texte à sceller. Les
  réponses sont à la section 6 de ce rapport. En particulier, écrire dans D1, comme une règle et non comme une question :
  le majorant de 2,00 USD est ajouté **une seule fois** ; les commentaires des pièces épinglées qui disent « toute paire
  illisible ajoute le majorant » (module d'écart, en-tête l. 12-14 et description l. 65-66 ; surveillance d'écart,
  l. 7-8 ; rapport du développeur l. 132 ; registre R-2453) se lisent « une seule fois » ; **le code et l'addendum font
  foi**. Mettre à jour la ligne « Contre-lecture (R2) : à faire ».
- **A2 — Unité du relevé : la vérification à la facture devient un engagement daté.** Le brouillon la range au risque
  résiduel, sans date ni suite. Écrire : les frais de bande passante de 60370121 sont relevés par la session ou par
  Lazar, sans dépense, **avant le lancement si la facture est déjà lisible, au plus tard avant le verdict R13** ; le
  montant est inscrit au registre des dépenses ; s'il contredit le kilo-octet (ordre de grandeur autre que ≈ 0,17 à
  0,19 USD), **arrêt et nœud de Lazar**. Si la session ne sait pas que la facture survit à la destruction de
  l'instance, elle relève ce montant **avant** de détruire 60370121.
- **A3 — Conditions d'emploi, point 1 : cas manquant.** Le brouillon nomme deux fins de l'enchaîneur après une
  création sans surveillance (traces illisibles, empreinte autre). Il en manque une : le **code 4 du lanceur**
  (création douteuse ; enchaîneur l. 72-75 : fin sans contrôle ni surveillance). Écrire que la session relit alors la
  liste des instances et, si une instance de P3-bis existe, la surveille à la main par la surveillance d'écart 2 ou
  l'arrête par son identifiant (R10).
- **A4 — Risque résiduel : un cas à déclarer.** Le contrôle d'écart arrête l'instance sur un état « exited »,
  « stopped », « offline » ou inconnu vu à **un seul** de ses relevés (jusqu'à vingt-cinq), alors que la surveillance
  exige deux relevés de suite (texte l. 1955-1956 ; surveillance l. 140-144). L'origine arrêtait aussi sur un seul
  relevé, mais n'en faisait qu'un. Ce n'est pas un affaiblissement de la garde ; c'est un risque d'arrêt à tort, à
  écrire avec les trois autres. Preuve dans le journal versé : cas C2-10 (état « exited » à + 400 s, arrêt au relevé
  de + 421 s).
- **A5 — « GO-2026-11-02-29 » : écrire l'éclaircissement** (préalable 3 et P6). GO-2026-11-10-02 est la prolongation
  de GO-2026-11-02-29, même plafond de 80 USD, non cumulé (`registres/go.md` l. 292, R-2077). Au commit
  `6abf5d1f…` de `main`, `registres/depenses.md` ne porte **aucune** ligne sous GO-2026-11-02-29 (recherche refaite par
  le contre-lecteur dans ce seul fichier). La dépense antérieure est donc la somme des tentatives du 12 novembre sous
  GO-2026-11-10-02 (l. 420 et 431), stockage compris. Remplacer « la session le vérifie » par ce constat daté, que la
  session relit le jour du lancement.

## Corrections suggérées

- **S1 (addendum)** — Ajouter aux sources de D1 l'indice de la section 3 : les deux relevés de la fille sont des
  multiples exacts de 1 024 au centième près (6 564 085,76 = 6 410,24 × 1 024 ; 289 792 = 283 × 1 024).
- **S2 (addendum)** — Écrire la règle du stockage dans la dépense antérieure : faute de facture, 0,08 USD de l'heure
  (borne du filtre de l'offre, l. 1811) × durée arrêtée jusqu'à la destruction, arrondi au centime supérieur.
- **S3 (addendum)** — Condition d'emploi de plus : entre l'appel du contrôle et son verdict, aucune surveillance de
  la dépense ne tourne. Le contrôle écrit une ligne dans `releves.txt` toutes les 30 s. Si aucune ligne neuve ne
  paraît pendant cinq minutes avant le verdict (outil de location bloqué ; le texte ne veut aucun `timeout`, écart 10
  du lanceur, l. 2288), la session arrête l'enchaîneur par son PID, puis surveille ou arrête l'instance par son
  identifiant. Le risque existait à l'origine pour un seul appel ; il y en a jusqu'à cinquante.
- **S4 (addendum)** — Versement : remplacer « un commit postérieur qui n'ajoute que cet addendum et son compagnon »
  par « qui n'ajoute que des fichiers hors du dossier de la chaîne », pour que la contre-lecture et la vérification
  courte puissent y être versées.
- **S5 (addendum)** — Dire à Lazar en une ligne, au scellement, que D3 (enchaîneur fixé, dépense antérieure passée)
  n'était pas dans son mot R-2450 et resserre la garde sans rien relâcher.
- **S6 (code, seulement si une version neuve du contrôle est faite pour une autre raison)** — exiger deux relevés de
  suite pour un état terminal, comme la surveillance ; et prendre alors l'échéance de 1 200 s.
- **S7 (banc, version suivante)** — éprouver les revérifications d'empreinte juste avant chaque appel (ma mutation
  M-H n'est pas vue, section 7), le code 4 du lanceur et les traces illisibles après une création.

## Pièces relues (empreintes recalculées)

| Pièce | Empreinte | État |
|---|---|---|
| addendum 2, brouillon 1 | `7c5e5db267e5e3e621e125468e3d93ee2286704e097c2c4142a292306c4665cc` | égale à la consigne |
| commit `07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9` | 38 fichiers ajoutés au-dessus de `f2a241c9`, aucun modifié | relevé refait (`git diff --name-status`) |
| module, surveillance, contrôle d'écart ; enchaîneur v5 | `ba6deb68…`, `555ee522…`, `6aa165e5…`, `34131eaf…` | égales à l'addendum ; compagnons conformes |
| banc, journal, diff, sources, rapport du développeur | `e9629573…`, `c6af5250…`, `6f0e0ac7…`, `340c7d5a…`, `2ba5201f…` | égales ; compagnons conformes |
| dix sorties de `sorties-essais-ecart2-v1/` | celles de l'addendum | égales ; dix compagnons conformes |
| texte scellé `prereg/P3-bis-temoin-positif-v1.md` | `76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb` | égale |
| addendum 1 | `4e188814b52736edb6f690931b25e6c0d9cdaede20b23490d50aa5461c5ca537` | égale |
| registres au commit `6abf5d1f…` : décisions, dépenses, arrêts | `b1325ae0…`, `a98515cc…`, `cf765d47…` | égales à l'addendum |
| note de la fille, commit `0f3ea945…` | `c0f8837833f1021ca0be50bdf033311a7a3b01859a7911f1ceaffa9b430dd04a` | égale |

Lu en entier : le rapport du développeur, le diff contre S, les sources de D1, l'enchaîneur v5, le banc, l'addendum.
Du texte scellé : l. 1808-1813, 1843-1845, 1944-1968, 1998-2011, 2146-2152, 2170-2184, 2262-2292, 2463-2472, et une
recherche par motif dans ce seul fichier. Des scripts de S : `scripts/p3bis_instance_v2.sh` l. 60-260,
`scripts/amorce_instance_p3bis_v2.sh`, `detruire_p3bis_v2.sh`, la boucle de la surveillance.

## 1. Question 1 — le diff et les originaux

- **Le diff ne touche que D1 à D3.** Module : en-tête, description de `depense`, deux constantes, la boucle du
  téléchargement et la ligne écrite. Surveillance : en-tête, usage, le chemin du module d'écart et sa garde, l'appel de
  `depense`. Contrôle : en-tête, usage, deux constantes, le relevé devenu une boucle. Rien d'autre.
- **Les originaux sont égaux à S.** Les quinze fichiers que compare le bloc 2 du lanceur (les quatorze de `CHAINE` et
  `lancer_p3bis_v2.sh`) ont le même objet git à `8f8df8b2` et à `07a4b48a` (vérifié un par un). Entre S et `07a4b48a`,
  aucun fichier n'est modifié ou retiré dans tout le dépôt ; sous `scripts`, `src`, `tests` et `prereg`, seul
  l'addendum 1 est ajouté.
- **La comparaison à S du lanceur d'écart 1 reste juste.** Le lanceur d'écart 1 v2 a le même objet à `f2a241c9` et à
  `07a4b48a` (`2e294e5a…`). Les fichiers neufs du dossier ne le gênent pas : le bout en bout E3-01 passe avec eux.
- **Aucun script en aval ne relit la ligne de dépense**, dont la forme change (recherche dans la récupération, la
  destruction, le lanceur d'écart et le contrôle : aucune occurrence).

## 2. Question 2 — D1

- **La source tranche le prix, pas le relevé.** Je n'ai pas relu les copies du client ni les pages de la
  documentation : elles sont dans le bac à sable du développeur et je n'appelle rien dehors. Je juge donc le
  raisonnement sur les lignes citées et sur les valeurs de la fille, que j'ai relues à la note (`0f3ea945`).
- **Le kilo-octet binaire est la lecture la plus prudente parmi les plausibles.** Calculs refaits : en Kio, 6,72 Go
  descendus et 0,30 Go montés, soit 0,175 et 0,012 USD ; en Mo, 6,56 To en ≈ 255 s, impossible ; en octets, 6,6 Mo,
  moins qu'un seul clonage. Le prix déduit de la montée (0,040006 USD par Go) et le rapport montée sur descente
  (4,41 % contre 4,36 %) sont justes.
- **Indice de plus, trouvé à la contre-lecture.** Les deux relevés sont des multiples exacts de 1 024 au centième :
  6 564 085,76 / 1 024 = 6 410,24 et 289 792 / 1 024 = 283. Un compteur tenu en Mio au centième, multiplié par 1 024,
  donne exactement cela : le champ est alors en Kio. Ce n'est pas une preuve ; cela va dans le sens retenu.
- **La garde arrête toujours une vraie dépense excessive**, sous la lecture retenue et sous toute lecture plus
  petite : cas D1-03, D1-04, S1-03 rejoués ; ma mutation M-B (Go binaire) est vue par sept cas. Sous la lecture
  exclue (Mio), elle sous-compterait d'un facteur 1 024 ; c'est le seul risque, et la facture le lève (A2).
- **Le majorant ajouté une seule fois est acceptable.** Quatre raisons : le texte dit « majorant de 2,00 USD s'il est
  illisible », au singulier (l. 1966, l. 2281) ; le devis le pose comme la borne de tout le téléchargement de la
  course, « ≤ 2,0 USD à 0,05 USD/Go » (l. 2463) ; les deux sens illisibles donnent le montant de l'origine ; dans
  tous les autres cas le montant est supérieur ou égal à celui de l'origine (origine : descente illisible, 2,00 à la
  place du tout ; montée illisible, zéro en silence). **Il est mal écrit dans les pièces épinglées**, qui disent
  « toute paire » : d'où A1. Le brouillon de l'addendum, lui, l'écrit juste.
- **Entrées limites éprouvées par moi sur le module d'écart** (aucun appel dehors) : `NaN`, `1e400` et `null` dans un
  relevé donnent le majorant écrit, code 0 ; une réponse qui n'est pas un objet donne les deux bornes, code 0 ; une
  course entière plausible (40 Go à 0,05 USD, cinq heures à 2,10 USD) reste loin du plafond.

## 3. Question 3 — D2

- **La cause est lue dans les scripts de S.** Dans `p3bis_instance_v2.sh`, « début » (l. 68) précède le second
  clonage (l. 77) ; « préenregistrement lu », « branche poussée » et la carte (`nvidia-smi`, l. 252) suivent, **avant**
  l'installation (l. 259 et suivantes). Les lignes attendues arrivent donc peu après la fin du second clonage.
- **L'attente bornée n'affaiblit pas la garde au-delà du nécessaire.** Tout signe d'échec reste un arrêt immédiat ;
  trois signes sont ajoutés (fin de l'amorce, ligne « début » ou « préenregistrement lu » autre, carte autre). Une
  attente qui dure devient un KO à l'échéance. Une panne de l'évaluateur lui-même donne un KO (ligne « relecture de
  l'état et du journal impossible »). Le coût est borné : au plus ≈ 0,35 USD de plus qu'à l'origine.
- **Échéance : 900 s, gardée.** Elle laisse ≈ 835 s aux deux clonages, contre 2 × ≈ 185 s observés, soit une marge de
  ≈ 2,3. Passer à 1 200 s coûterait une version neuve du contrôle, un enchaîneur v6, le banc et sa relecture, pour
  ≈ 0,18 USD d'exposition de plus et une marge de 3. Réserve honnête : la durée d'un clonage n'a été observée que
  sur deux hôtes, et celle du second clonage jamais. Si une version neuve du contrôle est faite pour une autre
  raison, prendre 1 200 s (S6).
- **Illisibilités mises en attente : acceptables.** L'argument du développeur tient (vingt-cinq relevés multiplient
  l'exposition aux pannes passagères de l'outil), l'illisibilité qui dure reste un KO à l'échéance (C2-12, C2-13), et
  la surveillance suit de toute façon. La variante stricte n'est pas demandée.
- **Le même argument n'a pas été appliqué à l'état terminal** vu une seule fois : voir A4 et S6.

## 4. Question 4 — D3

- **Aucune destruction, aucun arrêt, aucune relance** dans l'enchaîneur v5 : il n'appelle l'outil de location nulle
  part ; les essais vérifient qu'aucun appel « destroy » n'est fait.
- **Empreintes** : les quatre pièces sont vérifiées avant tout appel (l. 54-56), le contrôle juste avant son appel
  (l. 86), la surveillance et le module juste avant le leur (l. 94). Le lanceur n'est pas revérifié juste avant son
  appel, mais rien ne sépare la première vérification de cet appel sinon l'écriture du journal. Une empreinte autre du
  contrôle n'empêche pas la surveillance ; une empreinte autre de la surveillance laisse l'instance sans garde, ce
  que le journal dit en clair et que l'addendum couvre (condition d'emploi 1).
- **Jeton** : seul le nom est écrit ; la valeur n'est ni affichée ni mise dans un fichier ; les variables locales sont
  effacées. Les essais cherchent les jetons factices dans toutes les sorties : aucun.
- **Dépense antérieure** : passée en cinquième argument, forme vérifiée (l. 49), remise telle quelle à la surveillance
  (l. 99) ; ma mutation M-G (zéro passé) est vue.
- **La surveillance suit quel que soit le code du contrôle** ; ma mutation M-F est vue.
- **La destruction après la surveillance d'écart est compatible, et je l'ai éprouvée.** `detruire_p3bis_v2.sh`
  (origine, égal à S) ne lit que `lancement.txt`, `motif.txt` et `instance-gardee` du dossier de la surveillance, et le
  rapport de la récupération ; la surveillance d'écart écrit ces fichiers comme l'origine. Épreuve X1, sur les
  sorties de E3-01 de mon rejeu, faux outil de location, rapport de récupération factice : « DESTRUCTION : instance
  77777771 détruite par son identifiant (R10), absente de la liste relue », code 0, deux appels (« destroy instance »,
  « show instances »). Épreuve X2, sur les sorties de E3-02 (échec d'amorce) : « REFUS : surveillance sans motif FIN »,
  code 2, aucun appel.
- **Fins sans surveillance après une création** : traces illisibles, empreinte autre, et code 4 du lanceur (A3).

## 5. Question 5 — l'addendum

- **Passages touchés : tous couverts.** Recherche refaite dans le texte scellé (« inet_ », « téléchargement »,
  « cinq minutes », « majorant », « enchaîneur », « 180 s », « 300 s ») : les passages sont l. 1948, 1950, 1962-1966,
  2150, 2280-2281, tous traités (P1 à P4, P9). Les lignes du devis (l. 2452, 2463, 2470, 2479-2480) ne changent pas.
  Le texte ne nomme ni la fenêtre de 180 à 300 s, ni l'enchaîneur : confirmé.
- **Citations « Ancien » : exactes**, comparées mot pour mot au texte pour P1 à P9 et à l'addendum 1 pour ses l. 69,
  74 et 167-169.
- **Pas de réécriture au-delà de l'écart.** Une seule formule change (P9). P6 ajoute « et sous GO-2026-11-10-02,
  toutes tentatives et relances précédentes » : ce n'est pas une règle neuve, c'est ce que dit déjà la l. 1962-1963.
- **Pièces citées par empreinte : exactes**, toutes recalculées (table ci-dessus). Les renvois de lignes au code et au
  journal sont justes (module l. 126-127 et 451-462 ; contrôle l. 53-55, 87, 109-232, 114, 143, 170, 219 ; journal
  l. 12-23, 31-36, 77-82, 147-153, 168-174, 182-202 ; lanceur d'écart l. 249-251).
- **Réserve au verdict : écrite**, dans les mots de R-2450, à côté de celle de l'écart 1.
- **Préalables du lancement : complets** sur les quatre points demandés (destruction de 60370121, dépense antérieure
  relevée au registre, empreinte de l'enchaîneur, extraction de la branche), plus l'addendum scellé et les conditions
  de l'addendum 1. À compléter par A2, A3 et A5.
- **« GO-2026-11-02-29 », éclairci** : voir A5. Il n'y a pas d'erreur dans le texte ; la mention vient du GO d'origine
  que GO-2026-11-10-02 prolonge sous le même plafond.

## 6. Réponses aux dix points laissés par le rédacteur

1. Échéance : **900 s** (section 3).
2. Illisibilités en attente : **acceptées**.
3. Majorant : **un seul**, et l'écrire comme en A1.
4. Unité : **Kio et Go décimal acceptés** ; facture selon A2.
5. Lectures de l'addendum 1 (l. 74 et l. 167-169) : **justes, à garder**.
6. Échec du banc re-pointé (R-02) : la lecture du rédacteur est **la bonne**. La sortie montre « téléchargement 2.00,
   descente 0.00 Go » et une dépense de 4,00 USD : l'échec tient à l'unité **et** au majorant de la montée absente. Le
   rapport du développeur (l. 362) ne dit que la première moitié. L'échec reste attendu.
7. Dépense antérieure : **confirmé** (centime supérieur ; les 2,00 USD de majorant de 60286945 restent comptés tant
   qu'une facture ne les remplace pas), plus S2.
8. Destruction après la surveillance d'écart : **éprouvée** (X1 et X2, section 4) ; l'addendum peut citer ce rapport.
9. Portée de D3 : **acceptable**. L'enchaîneur n'est pas cité par le texte scellé ; le fixer n'est pas un écart de
   plus, et la dépense antérieure passée met l'outil en accord avec le texte. Voir S5.
10. Versement : **confirmé**, avec S4.

## 7. Question 6 — essais rejoués et mutations

**Rejeu.** `essais_ecart2_p3bis_v1.sh`, joué depuis l'extraction détachée au commit `07a4b48a`, avec
`/home/user/controle-ia-travail/.venv/bin/python` (Python 3.13.18, pytest 9.1.1), de 21:29:23Z à 21:34:43Z :
**132 cas, 0 non conforme**, « ESSAIS DE L'ÉCART 2 DE P3-BIS : CONFORMES », code 0. Comparé au journal versé après
remplacement des heures, des commits de 40 caractères et de la racine du banc : **une seule ligne diffère**, un chemin
du bac à sable coupé à 170 caractères (cas S1-05). Journal de mon rejeu : `rejeu1.log`
(`7dc74da5a81055c2510e94672147e6e8a912eb7f564ec1434b4bb6c6d4210c9d`).

**Mutations de mon cru** (sept, autres que les deux du développeur). Chaque pièce mutée diffère de l'originale par
une ou deux lignes ; le banc joué est une copie dont quatre lignes changent (dossier de la chaîne fixé, et les trois
chemins des pièces mutées). Trois passages en parallèle, finis à 21:41:54Z.

| Mutation | Pièce | Ce qui change | Vue par le banc ? |
|---|---|---|---|
| M-A | module | majorant ajouté seulement si les deux sens sont illisibles | **oui** : D1-08, D1-11 |
| M-B | module | Go du prix pris binaire (2³⁰) | **oui** : D1-02 à D1-06, D1-08, D1-11 |
| M-C | contrôle | fin de l'amorce comptée OK au lieu de KO | **oui** : C2-08b |
| M-E | contrôle | échéance stricte (`-gt` au lieu de `-ge`) | **oui** : C2-05b, C2-06b, C2-12b, C2-13b, C2-26b |
| M-F | enchaîneur | pas de surveillance si le contrôle rend un code autre que 0 | **oui** : E3-02, E3-02b |
| M-G | enchaîneur | dépense antérieure remplacée par 0 | **oui** : E3-01d |
| M-H | enchaîneur | revérifications d'empreinte juste avant les appels retirées | **non** : banc conforme (S7) |

Journaux : `mut/bancA.log` (`020ab7fe…`, 5 non conformes), `mut/bancB.log` (`11d39dc4…`, 13 non conformes),
`mut/bancC.log` (`ac7ba4a7…`, conforme). M-H n'est pas un défaut du code : les lignes 86 et 94 sont justes à la
lecture ; c'est un trou du banc, sans effet sur le verdict.

## 8. Déclarations

1. **Refus d'un contrôle de permissions, rapporté tel quel.** Une épreuve de mon cru (X3 : un état « offline » ou
   inconnu vu à un seul relevé du contrôle d'écart, avec le faux outil) a été refusée avant d'être lancée. Message :
   « Permission for this command was denied by a built-in Claude Code safety check, not by the user. […] What was
   flagged: This command passes a shell -c script that runs rm, and Claude Code could not check the script for
   dangerous removals. » La commande contenait un `rm -f` de deux fichiers de mon bac à sable. Je ne l'ai ni rejouée,
   ni reformulée, ni contournée. Le constat A4 repose donc sur la lecture du code et sur le cas C2-10 du journal
   versé, non sur cette épreuve.
2. **Extraction partielle.** La consigne donnait `git worktree add --detach … 07a4b48a`. J'ai fait
   `git worktree add --no-checkout --detach`, puis une extraction partielle (`git sparse-checkout` et
   `git read-tree -mu HEAD` dans cet arbre détaché seulement) qui **exclut** `docs/notes/bras-attaque/`, `diag/`,
   `runs/`, `donnees/`, `registres/index-bras-attaque*` et `scripts/extraire_mesures_epreuve_t06_v1.py`. Aucun chemin
   interdit n'est sur le disque du bac à sable. L'arbre détaché reste enregistré dans le dépôt
   (`.git/worktrees/depot`) ; la mère peut le retirer.
3. **`git ls-tree` filtré.** Pour trouver le nom du script de l'amorce, j'ai lancé
   `git ls-tree --name-only 8f8df8b2 scripts/` filtré par le mot « p3bis » ; seuls dix-huit noms contenant ce mot ont
   été affichés. Le dossier `scripts/` contient un fichier interdit, dont le nom n'a pas été affiché.
4. **Incident du développeur, déjà au registre** (R-2453) : son `ls docs/notes/bras-attaque | head -2`. Rien à ajouter.

## 9. Points ouverts

- La facture de bande passante de 60370121 (A2) : seule vérification qui tranche l'unité.
- La durée du second clonage n'a jamais été observée ; la première relance la mesurera (`releves.txt`).
- Le montant de la dépense antérieure reste à relever par la session le jour du lancement.
- Après le brouillon 2, une vérification courte par un lecteur neuf suffit (les corrections ne touchent pas le code).

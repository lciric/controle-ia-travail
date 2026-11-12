# Préenregistrement — P3-bis, addendum 2 : dépense de téléchargement et fenêtre du contrôle à cinq minutes, par écart (R-2450) — v1 — brouillon 1

- Auteur : rédacteur neuf (sous-agent, Claude Opus 5.5), consigne
  `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-redacteur-p3bis-addendum2-v1.md`
  (`15fe96586b71d9724eda2e43cc282f3db4877c363ee993816530fcbb15047f39`, vérifiée, égale à son compagnon). Le rédacteur n'a
  écrit ni P3-bis, ni sa chaîne, ni l'écart 1, ni le code de l'écart 2. Il n'a lu aucun fichier de T0.7. Du texte scellé,
  il a lu les lignes 1840-1848, 1925-2015 et 2120-2310, plus des recherches par motif dans ce seul fichier.
- Date (UTC) : brouillon 1, écrit le 2026-11-12 de 21:20 à 21:25 (`date -u`). Au scellement, la date du commit de
  scellement fait foi.
- Texte scellé complété : `prereg/P3-bis-temoin-positif-v1.md`
  (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`), commit de scellement
  S = `8f8df8b2726a69568b4d4a54bae16188e7f1b3d0`. Les numéros de ligne « l. » sans autre précision sont ceux de ce fichier.
- Addendum 1, scellé, **reste en vigueur** : `prereg/P3-bis-addendum-1-garde-credit-v1.md`
  (`4e188814b52736edb6f690931b25e6c0d9cdaede20b23490d50aa5461c5ca537`, R-2407). Ses lignes sont citées « A1 l. ».
- Registres cités, sur `main` au commit `6abf5d1fd3b3af9aee183b770202eb3adb83dc37` :
  - `registres/decisions.md` (`b1325ae04740c618bb9c23efd64cdbfc4f21b9df740bf7cc2d59d85607042781`), entrées R-2393, R-2407,
    R-2411, R-2415, R-2416, R-2431, R-2446, R-2450, R-2452, R-2453 ;
  - `registres/depenses.md` (`a98515cc70df6086286228f05bb04e070fe1057700277a3853c952016dbf3320`), l. 419, 420, 431 ;
  - `registres/arrets.md` (`cf765d470aff0c71c3471ccabc568d5cace34dd6eb6840877eeca02f597f9f5a`), l. 90, 91, 93, 105, 106.
- Note de la session fille : `etat-p3bis-fille.md` de la branche `etat/p3bis-fille-v1`, commit
  `0f3ea945ef59813aa091c1a190f674f550d87e49` (`c0f8837833f1021ca0be50bdf033311a7a3b01859a7911f1ceaffa9b430dd04a`), l. 12-20.
- **Nœud tranché par Lazar** : écart au préenregistrement scellé, R-2450 (2026-11-12 vers 20:26 UTC), option (1) du nœud
  R-2446.
- Contre-lecture (R2) : à faire, par un lecteur neuf d'un autre modèle (Claude Fable 5.2), sur le code de l'écart 2 et sur
  cet addendum. Les points qui lui sont laissés sont à la dernière section.
- Statut : brouillon 1, non scellé. Il sera scellé comme l'addendum 1 (R-2407) : compagnon `.sha256`, versement sur `main`
  et, dans un commit postérieur à `07a4b48a`, sur la branche d'écart `prep/p3bis-ecart2-v1` ; une entrée au registre des
  décisions ; **aucune clé** dans `registres/scellements-v1.md` (l. 2009-2011). **Non décisif** : il ne touche ni à la
  lecture, ni à l'issue, ni au verdict, sinon par la réserve écrite plus bas.

## Objet

La tentative de 15:00 UTC du 12 novembre (instance 60370121) a montré deux défauts de la chaîne (R-2446, note de la fille
l. 16-19) :
- **D1, dépense de téléchargement.** Le module commun calcule le téléchargement par `inet_down_billed × inet_down_cost`
  (et la montée), sans conversion d'unité (`verifications_p3bis_v2.py` à S, `1524df5f…`, l. 429-436, calcul l. 430-433). Le
  relevé `inet_down_billed` valait 6 564 085,76 et le prix `inet_down_cost` 0,026 USD par Go (note de la fille l. 18). La
  surveillance a lu une dépense de 182 259,82 USD, dont 182 259,73 de téléchargement, et a arrêté l'instance au premier
  relevé (motif DÉPENSE). Ce défaut arrêterait toute course au premier relevé qui lit le téléchargement.
- **D2, fenêtre du contrôle à cinq minutes.** Le contrôle d'origine (`controle_cinq_minutes_p3bis_v2.sh`, `6f921349…`) fait
  un seul relevé, prévu entre la création + 180 s et + 300 s. Or les lignes attendues du journal arrivent plus tard :
  l'amorce clone le dépôt, puis le script de l'instance le clone une seconde fois. Le contrôle a arrêté à tort deux
  instances sans aucun signe d'échec : 60286945, contrôle joué à la création + 181 s, 4 KO (R-2411) ; 60370121, joué à
  + 290 s, 3 KO (R-2446).

Il ajoute un troisième point, qui n'est pas un défaut du texte :
- **D3, enchaîneur.** L'enchaîneur détaché qui appelle la chaîne (lanceur, contrôle, surveillance) n'a jamais été au
  dépôt : ses v1 à v4 vivaient dans le bac à sable de la session fille (R-2393, R-2416). La v1 passait à la surveillance une
  dépense antérieure de 0 (R-2393), alors que le texte compte toutes les tentatives (l. 1962-1963, l. 2266).

Cet addendum remplace, **pour la course de P3-bis sous ce texte et sous GO-2026-11-10-02**, le calcul du téléchargement,
la fenêtre du contrôle à cinq minutes et l'outil d'enchaînement. Rien d'autre.

## Mot de Lazar (verbatim)

- R-2450 (≈ 20:26 UTC) : « Recommandation : (1), confiance 0,75. : go ».
- L'option (1), telle que le registre la consigne (R-2450) : correction du calcul de la dépense de téléchargement (unité de
  `inet_*_billed`, module commun l. 430-433) et de la fenêtre du contrôle à cinq minutes, sous noms neufs, essais R5 sur
  cas sain et artefact ; contre-lecture par un lecteur neuf d'un autre modèle ; addendum 2 scellé ; destruction de
  l'instance 60370121 par son identifiant ; relance sous GO-2026-11-10-02 (plafond 80 USD) ; réserve au verdict.
- D3 n'est pas nommé dans ce mot. Il vient de la consigne de la mère au développeur
  (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-p3bis-ecart2-v1.md`,
  `1fd509964dea1a7afc6d193e6444082b733d02a1223bbf233fdef8f9c549fe2d`). L'enchaîneur n'est pas cité par le texte scellé ; il
  est fixé ici pour que ce qui est joué soit écrit (voir la dernière section, point 9).

## Ce qui change

### D1 — calcul du téléchargement

**Règle neuve.** Pour chaque sens, la descente (`inet_down_billed`, `inet_down_cost`) et la montée (`inet_up_billed`,
`inet_up_cost`), lus dans la réponse de « show instance » :
- si le relevé et le prix sont tous deux des nombres finis positifs ou nuls (ni absents, ni texte, ni booléens, ni
  négatifs) : volume en Go = relevé × 1 024 / 10⁹ ; dépense du sens = volume × prix ;
- sinon, le sens est **illisible**.

Le téléchargement est la somme des sens lisibles. **Si au moins un sens est illisible, le majorant de 2,00 USD est ajouté,
une seule fois**, et la ligne de dépense l'écrit avec le nom des sens illisibles : « téléchargement non relevé (descente,
montée) : majorant 2.00 USD pris ». Les deux sens illisibles donnent donc 2,00 USD, comme à l'origine. La ligne de dépense
écrit aussi les volumes lus, par exemple « descente 6.72 Go, montée 0.30 Go (relevés en Kio) ».

Code : `verifications_p3bis_v2_ecart2_v1.py`, constantes `OCTETS_PAR_UNITE_RELEVEE = 1024` et `OCTETS_PAR_GO_PRIX = 10 ** 9`
(l. 126-127), boucle des deux sens et majorant (l. 451-462). Vérifié par le rédacteur sur une copie du module dans son bac
à sable (aucun appel extérieur) : descente seule illisible, téléchargement 2,01 ; montée seule illisible, 2,17 ; les deux
illisibles, 2,00 ; les deux lisibles, 0,19 (valeurs de la fille ; prix de la montée 0,04, déduit par le développeur,
rapport l. 117-118). Les mêmes montants sont au journal des essais, cas D1-08, D1-11, D1-07 et D1-02 (l. 19, 22, 18, 13).

**Sources de l'unité** (`sources-d1-ecart2-v1.txt`, `340c7d5a…`) :
- le prix `inet_*_cost` est en **USD par Go** : client `vastai` 1.8.3 et 1.11.0 publié sur PyPI,
  `vastai/cli/commands/offers.py` l. 108 et 110 (« internet download bandwidth cost in $/GB ») ; fichier des sources
  l. 6-11 et 16-21 ;
- l'unité du relevé `inet_*_billed` **n'est documentée nulle part** : aucune occurrence dans les deux paquets du client,
  ni dans sept pages de la documentation publique de l'interface (fichier des sources l. 15, 25, 28-34).

**Interprétation retenue : la plus prudente parmi celles qui restent physiquement plausibles** (rapport du développeur,
l. 86-121). À la création + 294 s, l'instance avait téléchargé au moins un clonage complet du dépôt (≥ 1,59 Gio, fichier
des sources l. 49). Lu en octets ou en kilobits, le relevé donnerait moins qu'un clonage ; lu en Mo, plus de 6 To en
≈ 255 s. Restent le Ko et le Kio ; le Kio (1 024 octets) compte plus d'octets, et le Go du prix est pris décimal
(10⁹ octets), ce qui compte plus de Go. La dépense n'est donc jamais sous-estimée parmi les lectures plausibles. Sur les
valeurs de la fille : descente 6,72 Go, montée 0,30 Go, téléchargement 0,19 USD (journal, D1-02, l. 13), au lieu de
182 259,73.

**Garde intacte.** Une vraie dépense de téléchargement excessive arrête toujours la course : D1-03 (3 379,20 Go à
0,026 USD par Go, code 3, l. 14), D1-04 (1 638,40 Go au prix plafond du filtre, 0,05, code 3, l. 15), S1-03 (la
surveillance d'écart arrête par l'identifiant, motif DÉPENSE, l. 34-36) ; au centime : D1-05 et D1-06 (l. 16-17).

**Témoins de l'origine** (R4) : D1-01 (l. 12) et S1-02 (l. 31-33) reproduisent le faux positif ; D1-12 (l. 23) montre que
l'origine comptait la montée illisible pour zéro, sans rien écrire.

### D2 — attente bornée du contrôle à cinq minutes

**Règle neuve** (`controle_cinq_minutes_p3bis_v2_ecart2_v1.sh`, boucle l. 109-232, évaluateur l. 121-223) :
- **Départ** au plus tôt à la création + 180 s ; plus tôt : refus, code 2, rien d'écrit (inchangé, `DELAI_MIN_S=180`,
  l. 53 et 87).
- **Relevés** de l'état et du journal toutes les 30 s (`PAS_S=30`, l. 55) jusqu'à l'**échéance**, la création + 900 s
  (`ECHEANCE_S=900`, l. 54). Chaque contrôle d'origine y rend OK, ATTENTE ou KO.
- **KO immédiat** sur tout signe d'échec de la liste fermée ci-dessous : l'instance est arrêtée par son identifiant, comme à
  l'origine.
- **Jamais de KO pour une attente avant l'échéance.** Au relevé de l'échéance, toute attente devient un KO, « à
  l'échéance » (l. 219), et l'instance est arrêtée par son identifiant.
- **Appel après l'échéance** : un seul relevé, retard écrit.
- Le journal de l'instance est relu par `logs --tail 20000` (l. 114) au lieu de 200 lignes.

**Signes d'échec, liste fermée** (en-tête du script, (b)) :
- état ni « running » ni de démarrage (« created », « loading », « scheduling », état absent) ;
- prix relu au-dessus de 2,10 USD de l'heure ou de celui de l'offre choisie ; machine ou hôte autres que ceux de l'offre ;
  carte relue autre qu'« A100 SXM4 » ; étiquette autre ;
- au journal : ligne « AMORCE : … » (échec de l'amorce) ; ligne « AMORCE <date> : commit » d'un autre commit, ou celle de S
  répétée (redémarrage) ; ligne « AMORCE <date> : fin, code N » (l'amorce a fini pendant le contrôle) ; ligne « début :
  ETUDE=… » autre que l'attendue ; ligne « préenregistrement lu : … » d'un autre nombre de tests ; ligne de carte qui n'est
  pas une A100 SXM4 d'au moins 75 Gio.

**Affaiblissements, écrits** (rapport du développeur, l. 220-234) :
1. une ligne attendue absente n'est plus un KO avant la création + 900 s (c'en était un dès l'unique relevé, entre + 180 et
   + 300 s) : c'est l'objet même de D2 ;
2. un état ou un journal illisible (outil de location en échec) est une attente, KO seulement à l'échéance (l. 143 et 170 ;
   cas C2-12 et C2-13, journal l. 77-82) ; il était un KO immédiat ;
3. un état de démarrage est une attente ; tout état autre que « running » était un KO ;
4. un prix, une machine, un hôte, une carte ou une étiquette **absents** sont des attentes ; une valeur **présente et
   fausse** reste un KO immédiat.

**Renforcements** : la fin de l'amorce, une ligne « début » ou « préenregistrement lu » autre et une ligne de carte autre
sont des signes d'échec immédiats ; l'origine ne les voyait que comme des absences.

**Ce que coûte la borne** : une panne silencieuse (clonage bloqué sans ligne d'échec) est vue au plus tard à + 900 s au
lieu de + 300 s, soit au plus ≈ 10 minutes de calcul de plus, ≈ 0,35 USD à 2,10 USD de l'heure (rapport du développeur,
l. 191-193).

**Inchangés, octet pour octet** (cas C2-K2, journal l. 153) : le préambule (usage, jetons, dossier neuf, outil, traces,
garde de l'identifiant, nombre de tests du texte de S, refus avant + 180 s) et le bloc d'arrêt par l'identifiant après la
garde du module commun d'origine. Constantes gardées : `PRIX_MAX=2.10`, `DELAI_MIN_S=180` (C2-K1, l. 152). Codes de sortie
0, 1, 2 inchangés.

**Témoin du défaut et de sa correction** (R4) : le contrôle d'origine joué à + 290 s sur des lignes qui arrivent à + 410 s
rend 3 KO et arrête l'instance (C2-T1, l. 147-148) ; le contrôle d'écart, sur le même scénario, rend conforme à + 410 s
(C2-T2, l. 149-151).

### D3 — enchaîneur v5 au dépôt

`enchaineur_p3bis_v5.sh`, usage (l. 33-39) :
`setsid nohup bash enchaineur_p3bis_v5.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD`, PID noté, arrêt seulement par
ce PID (R10). Il :
1. vérifie les empreintes des quatre pièces qu'il appelle, avant tout appel puis juste avant chaque appel (l. 42-45, 54-56,
   86, 94) ; une empreinte autre : aucun appel, code 2 (cas E3-04, journal l. 171-173) ;
2. appelle le lanceur d'écart 1 v2, inchangé (l. 70) ; un code autre que 0 met fin à l'enchaîneur, sans contrôle ni
   surveillance (l. 72-75 ; E3-03, l. 168-170) ;
3. exige une seule ligne `instance` et une seule ligne `creation` dans `lancement.txt` (l. 77-81) ;
4. attend la création + 181 s (l. 41, 84 ; la v4 attendait + 290 s, R-2416) et appelle le contrôle d'écart 2, qui attend
   lui-même jusqu'à son échéance ;
5. appelle la surveillance d'écart 2 **quel que soit le code du contrôle** (R-2393), avec la **dépense antérieure passée en
   argument** (l. 99) ; elle doit être un nombre positif en USD (l. 49 ; E3-05, l. 174) ;
6. écrit chaque appel, code et heure (`date -u`) dans `enchaineur.txt` ; aucun arrêt, aucune destruction, aucune
   récupération, aucune relance.

Écarts déclarés aux v1 à v4 décrites au registre : pièces d'écart 2 au lieu de celles de S ; contrôle appelé à + 181 s ;
dépense antérieure en argument ; empreintes épinglées vérifiées ; jeton de la forge pris dans
`CONTROLE_IA_GITHUB_TOKEN_2` seulement si `CONTROLE_IA_GITHUB_TOKEN` manque (nom seul écrit) ; noms des fichiers du
dossier neuf. **Non reconstructible à l'identique** : le texte des v1 à v4, la forme de leurs arguments, de leur journal et
de leurs messages (rapport du développeur, l. 307-311).

## Passages du texte scellé remplacés

Chaque passage est cité tel qu'il est écrit (sauts de ligne ôtés). « Nouveau » est la lecture qui vaut sous l'écart 2. Le
texte scellé n'est pas réécrit (R12). Le texte ne fixe nulle part la fenêtre de 180 à 300 s, qui n'est que dans le script
d'origine, ni l'enchaîneur (recherches par motif du rédacteur : « 180 », « 300 s », « cinq minutes », « enchaîneur »).

**P1 — Liste d'arrêt, l. 1948.**
- Ancien : « Contrôle à cinq minutes en échec : arrêt de l'instance par son identifiant (R10), consigné. »
- Nouveau : « Contrôle à cinq minutes en échec, c'est-à-dire un signe d'échec de la liste fermée à l'un des relevés, ou un
  contrôle encore en attente au relevé de l'échéance (création + 900 s), joué par `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh`
  (addendum 2, D2) : arrêt de l'instance par son identifiant (R10), consigné. »

**P2 — Liste d'arrêt, l. 1949-1950** (« Relance après une instance gardée ou arrêtée »).
- Ancien : « tant qu'une instance de P3-bis arrêtée (code 5 du second paquet, contrôle à cinq minutes en échec, ou tout
  autre motif que la fin normale) reste sur le compte hors `ARRETEES_TOLEREES` »
- Nouveau : mêmes mots ; « contrôle à cinq minutes en échec » se lit comme en P1. Le reste de la règle (l. 1951-1954) ne
  change pas. Pour 60370121, le mot de Lazar qu'elle exige est R-2450, qui choisit la destruction par l'identifiant.

**P3 — Liste d'arrêt, l. 1962-1966** (« Dépense cumulée de la course »).
- Ancien : « (brouillon 10, écart 6 du lanceur : prix pris, le plus haut du prix relu et de celui de l'offre, 2,10 USD de
  l'heure s'il est illisible ; téléchargement relevé, majorant de 2,00 USD s'il est illisible) »
- Nouveau : « (brouillon 10, écart 6 du lanceur : prix pris, le plus haut du prix relu et de celui de l'offre, 2,10 USD de
  l'heure s'il est illisible ; téléchargement relevé pour la descente et pour la montée, chaque relevé `inet_*_billed` pris
  en kilo-octets binaires et converti en Go décimaux avant le prix `inet_*_cost` en USD par Go, majorant de 2,00 USD ajouté
  une seule fois, écrit, dès qu'un des deux sens est illisible ; addendum 2, D1) ».
- Le début de la phrase (« calcul, disque, téléchargement, toutes tentatives et relances comprises, sous GO-2026-11-02-29
  et GO-2026-11-10-02 ensemble, non cumulés », l. 1962-1963), le plafond de **80 USD**, la projection au prochain relevé et
  l'arrêt par l'identifiant ne changent pas. La dépense des tentatives précédentes entre par l'argument de l'enchaîneur v5
  (D3 ; P6).

**P4 — Plan, point 6, logique neuve (i), l. 2149-2150.**
- Ancien : « ou sur dépense cumulée ≥ 80 USD (prix de l'offre × durée depuis la création, plus disque et téléchargement
  relevés) »
- Nouveau : « ou sur dépense cumulée ≥ 80 USD (prix de l'offre × durée depuis la création, plus disque et téléchargement
  relevés, le téléchargement calculé selon l'écart 6 du lanceur lu sous l'addendum 2, P9), surveillance jouée :
  `surveiller_p3bis_v2_ecart2_v1.sh` ». Les autres motifs de (i), l'alerte à deux heures et la destruction en fin normale
  ne changent pas.

**P5 — Plan, point 6 (a), chaîne v2 citée par empreinte, l. 2172-2183.**
- Ancien (l. 2172-2173, puis trois des douze fichiers) : « (a) **chaîne v2** : douze fichiers **au commit du code**
  `5e4575259478af3611e2c7fb1313342912caf484`, empreintes recalculées par `git show` à ce commit, chacune égale à son
  compagnon au même commit : […] `docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v2.py`
  (`1524df5f6432197fde4793a4fde56d4496407a107c88f5e294a6bc9716923054`) ; […]
  `docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2.sh`
  (`d65421073068466a3aa6cc90ef00e6c76b15ea7b3e61e254c1dbafad020afe9b`) ;
  `docs/procedures/P3-bis-temoin-positif-v1/controle_cinq_minutes_p3bis_v2.sh`
  (`6f9213499687d655e290ab96c1ab8a1cdb9ecd373b1d6beecb7efda962f40864`) ; »
- Nouveau : la citation reste telle quelle. Les trois fichiers restent au dossier, égaux à leurs copies de S (cas R-05,
  journal l. 190-192), et le bloc 2 du lanceur d'écart 1 v2 les compare toujours à S. S'ajoute : « Pour la course sous ce
  texte, sous l'écart 2 (R-2450), au commit `07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9` de la branche `prep/p3bis-ecart2-v1` :
  la sous-commande `depense` est jouée de `docs/procedures/P3-bis-temoin-positif-v1/verifications_p3bis_v2_ecart2_v1.py`
  (`ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e`), les autres sous-commandes restant celles de
  `verifications_p3bis_v2.py` ; la surveillance est `docs/procedures/P3-bis-temoin-positif-v1/surveiller_p3bis_v2_ecart2_v1.sh`
  (`555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db`) ; le contrôle à cinq minutes est
  `docs/procedures/P3-bis-temoin-positif-v1/controle_cinq_minutes_p3bis_v2_ecart2_v1.sh`
  (`6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f`). Le contrôle et la surveillance d'origine ne sont
  jamais joués pour cette course ; du module d'origine, seule la sous-commande `depense` n'est plus jouée (ses autres
  sous-commandes servent toujours la surveillance et la garde d'arrêt du contrôle). » Le lanceur cité l. 2174-2175
  (`029bdb5c…`) se lit déjà sous l'écart 1 (A1 l. 80-92).

**P6 — Écarts du lanceur portés au texte, 1, l. 2264-2266.**
- Ancien : « la dépense antérieure passée à la surveillance comprend toute dépense sous GO-2026-11-02-29 »
- Nouveau : « la dépense antérieure passée à la surveillance comprend toute dépense sous GO-2026-11-02-29 et sous
  GO-2026-11-10-02, toutes tentatives et relances précédentes (calcul, téléchargement, stockage jusqu'à la destruction),
  comme le dit la l. 1962-1963 ; elle est relevée par la session au registre des dépenses avant le lancement et passée en
  cinquième argument de `enchaineur_p3bis_v5.sh`, qui la remet telle quelle à la surveillance d'écart 2 (addendum 2, D3) ».
  Le reste de cet écart 1 du lanceur (GO, 23 novembre, ligne du GO mot pour mot, révocations, borne de création du
  18 novembre) ne change pas. (Ne pas confondre avec l'écart 1 de la garde du crédit, R-2399, objet de l'addendum 1.)

**P7 — Écarts du lanceur portés au texte, 4, l. 2273-2275.**
- Ancien : « trois noms hors de la table commune, acceptés (R-2084) : `detruire_p3bis_v1.sh` (destruction par
  identifiant), `controle_cinq_minutes_p3bis_v1.sh`, `essais_verifications_p3bis_v1.py` (banc du module commun, sous
  `docs/` et non sous `tests/`, pour ne pas changer l'arbre gelé) ; »
- Nouveau : mêmes mots, puis : « s'y ajoutent, sous l'écart 2, des fichiers neufs sous
  `docs/procedures/P3-bis-temoin-positif-v1/` seulement : `verifications_p3bis_v2_ecart2_v1.py`,
  `surveiller_p3bis_v2_ecart2_v1.sh`, `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` (le nom « cinq minutes » est gardé ;
  l'échéance est la création + 900 s), `enchaineur_p3bis_v5.sh` et le banc `essais_ecart2_p3bis_v1.sh` ».

**P8 — Écarts du lanceur portés au texte, 5, l. 2276-2278.**
- Ancien : « la surveillance arrête elle-même l'instance par son identifiant et écrit la ligne à consigner ; le motif
  « processus mort » est lu à la fin de l'amorce ; l'alerte à deux heures n'arrête rien (sortie standard et
  `alertes.txt`, lus par la session) ; »
- Nouveau : mêmes mots ; « la surveillance » se lit `surveiller_p3bis_v2_ecart2_v1.sh`. Selon son en-tête et le diff relu
  (`diff-ecart2-contre-S-v1.txt`, l. 87-142), seul y change l'appel de la sous-commande `depense` ; motifs, arrêts par
  identifiant, alerte, intervalle et codes sont ceux de l'origine (cas R-04, journal l. 189).

**P9 — Écarts du lanceur portés au texte, 6, l. 2279-2282.**
- Ancien : « arrêt à 80 USD sur la dépense projetée au prochain relevé ; prix pris, le plus haut du prix relu et de celui de
  l'offre (2,10 USD de l'heure s'il est illisible, écrit) ; téléchargement relevé par `inet_down_billed × inet_down_cost`
  (et la montée), majorant de 2,00 USD écrit s'il est illisible ; disque supposé compris dans `dph_total` en marche
  (hypothèse déclarée) ; »
- Nouveau : « arrêt à 80 USD sur la dépense projetée au prochain relevé ; prix pris, le plus haut du prix relu et de celui
  de l'offre (2,10 USD de l'heure s'il est illisible, écrit) ; téléchargement relevé, pour chaque sens, par
  `inet_*_billed × 1 024 / 10⁹ × inet_*_cost` (relevé pris en kilo-octets binaires, unité non documentée, interprétation
  la plus prudente des lectures physiquement plausibles ; prix en USD par Go, Go décimal), majorant de 2,00 USD ajouté une
  seule fois, écrit, dès qu'un des deux sens est illisible ; disque supposé compris dans `dph_total` en marche (hypothèse
  déclarée) ; addendum 2, D1 ». **C'est le seul passage dont la formule change.**

## Addendum 1, lu sous l'écart 2

- **A1 l. 69** — Ancien : « Le **plafond de 80 USD** de la dépense cumulée et sa surveillance (l. 1962-1968 ; point 6 (i),
  l. 2149-2150), arrêt par identifiant compris. » Lecture sous l'écart 2 : le plafond de 80 USD, la projection au prochain
  relevé, le prix pris et l'arrêt par l'identifiant ne changent pas ; la surveillance jouée est la surveillance d'écart 2, et
  la part du téléchargement se calcule selon D1. L'addendum 1 ne disait rien de ce calcul : il n'est pas contredit.
- **A1 l. 74** (« Tous les autres scripts de la chaîne, et `lancer_p3bis_v2.sh` lui-même, qui reste au dossier, égal à sa
  copie de S ») : reste vrai des fichiers du dossier, tous égaux à S ; ce qui est **joué** pour le contrôle, la surveillance
  et la sous-commande `depense` est la pièce d'écart 2 (P5).
- **A1 l. 167-169**, condition d'emploi 2 (« Un arbre de la branche d'écart convient. Aucun autre script de la chaîne n'est
  remplacé. ») : se lit « un arbre de la branche `prep/p3bis-ecart2-v1`, qui porte la branche d'écart 1 et l'addendum 1,
  est exigé ; aucun autre script n'est remplacé que les trois pièces de l'écart 2 ». Le lanceur v1 et le lanceur d'origine
  ne sont toujours jamais joués pour une création.
- **A1 l. 148 et l. 156-160** (aval inchangé ; aucun script en aval ne relit l'empreinte du lanceur ni la ligne d'écart 1) :
  restent vraies. Le rédacteur a cherché dans les trois pièces d'écart 2 l'empreinte `2e294e5a`, « écart 1 », « R-2399 »,
  « ecart1 » et « lanceur p3bis v2 » : aucune occurrence.
- Les conditions d'emploi 1, 3 et 4 de l'addendum 1 (empreinte du lanceur d'écart vérifiée, portée, recharge automatique)
  et sa réserve au verdict ne changent pas.

## Lignes d'information de `lancement.txt`

Le lanceur d'écart 1 v2 (`lancer_p3bis_v2_ecart1_v2.sh`, `2e294e5a…`, inchangé), l. 249-251, écrit dans `lancement.txt`
deux lignes qui nomment les pièces d'origine :
- « surveillance : surveiller_p3bis_v2.sh <instance> <traces> <dépense antérieure en USD> <dossier neuf> (aucun plafond de
  durée ; alerte à deux heures sans PROGRES ; arrêt par identifiant sur fin, échec d amorce, redémarrage, état terminal,
  processus mort, 80 USD ; code 5 : instance gardée) » ;
- « contrôle à cinq minutes entre A et B (création + 180 à 300 s ; controle_cinq_minutes_p3bis_v2.sh <instance> <traces>
  <dossier neuf>) ».

Ici, A et B tiennent lieu des heures de la création + 180 s et + 300 s, et `<traces>` du chemin du dossier des traces,
que le lanceur écrit en clair.

**Lecture sous l'écart 2.** Ces deux lignes sont des informations ; elles restent écrites telles quelles (R12) et ne sont
jamais suivies comme une consigne :
- la première se lit comme nommant `surveiller_p3bis_v2_ecart2_v1.sh`, mêmes arguments, mêmes motifs, même plafond de
  80 USD, téléchargement calculé selon D1 ;
- la seconde se lit comme nommant `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh`, mêmes arguments, appelé au plus tôt à la
  création + 180 s (l'enchaîneur v5 l'appelle à + 181 s), relevés toutes les 30 s jusqu'à la création + 900 s ; l'heure B
  (création + 300 s) n'est plus une borne.

Aucun script ne relit ces deux lignes : le rédacteur a cherché « surveillance : », « contrôle à cinq minutes entre » et
« 180 à 300 » dans le module, la surveillance et le contrôle, d'origine et d'écart, la récupération, la destruction et
l'enchaîneur v5 ; seules paraissent les lignes du journal propre de l'enchaîneur (l. 98 et 100). La ligne « destruction »
du même bloc ne change pas.

## Ce qui ne change pas

- Le cœur de l'expérience : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture
  gelés.
- Toute la liste d'arrêt, hors les lectures P1 à P3 : contrôles avant dépense, bornes de l'offre, liste fermée des
  instances, GO, borne de création du 18 novembre 2026, révocations, processus mort, motifs de fin de la surveillance,
  second paquet, garde d'ouverture.
- Le **plafond de 80 USD** (sous GO-2026-11-02-29 et GO-2026-11-10-02 ensemble), sa projection et l'arrêt par identifiant ;
  le GO (GO-2026-11-10-02, échéance le 23 novembre 2026) ; la date du rendez-vous (2026-11-20T12:00:00Z, l. 1999-2000) ; la
  règle de relance après une instance gardée ou arrêtée (l. 1949-1954) ; la ligne unique `SCELLEMENT-P3BIS`
  (l. 2009-2011).
- **Le code cité** : l'écart 2 n'ajoute que des fichiers sous `docs/procedures/P3-bis-temoin-positif-v1/` (relevé
  `git diff --name-status f2a241c9 07a4b48a` : 38 ajouts, aucun fichier modifié). Même lecture que l'addendum 1, (b),
  pour la ligne 1 des critères (l. 1844, « si le code cité n'a pas changé »).
- Les pièces non touchées : lanceur d'origine et lanceur d'écart 1 v2, contrôles avant dépense, récupération, destruction,
  scripts de l'instance et de l'amorce, configuration, consignes. Les originaux du module, de la surveillance et du
  contrôle restent au dossier, égaux à S.
- Dans le contrôle : les contrôles eux-mêmes et leurs valeurs (2,10 USD de l'heure, A100 SXM4 d'au moins 75 Gio,
  étiquette, commit S, nombre de tests du texte), le masquage des jetons, l'arrêt par l'identifiant après la garde du
  module d'origine, les codes 0, 1 et 2.
- Dans la surveillance : tout sauf l'appel de `depense` (P8).
- L'ordre « contrôle, puis surveillance quel que soit le code du contrôle » (R-2393).
- Tout l'écart 1 et son addendum, lus comme ci-dessus.

## Pièces, par chemin et empreinte

Branche `prep/p3bis-ecart2-v1`, commit **`07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9`**, seul commit au-dessus de
`f2a241c99186f92b304d128354db6cf1fb9896a9` (tête de `prep/p3bis-ecart1-credit-v1` : S, lanceur d'écart 1 v2, addendum 1).
Tout sous `docs/procedures/P3-bis-temoin-positif-v1/`. Empreintes recalculées par le rédacteur par `git show` à ce commit,
chacune égale à son compagnon `.sha256` au même commit :

| Pièce | sha256 | Rôle |
|---|---|---|
| `verifications_p3bis_v2_ecart2_v1.py` | `ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e` | module d'écart (D1) ; seule sa sous-commande `depense` est jouée |
| `surveiller_p3bis_v2_ecart2_v1.sh` | `555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db` | surveillance d'écart (D1) |
| `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` | `6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f` | contrôle d'écart (D2) |
| `enchaineur_p3bis_v5.sh` | `34131eaf528f65077576a83a64fceb58100ab34027b043c79763a31669e063a0` | enchaîneur détaché (D3) |
| `essais_ecart2_p3bis_v1.sh` | `e9629573af24dcfeb832373b0a398f48347bd2f4b13d45173807c1048ddaa6d3` | banc des essais R5 |
| `essais-ecart2-p3bis-v1.log` | `c6af52507bad86417c0b8adab2c22e6a781be27916d7b4c20418f87f39d38d2a` | journal du passage final, 2026-11-12T21:03:05Z → 21:07:57Z |
| `diff-ecart2-contre-S-v1.txt` | `6f0e0ac75422e262c4af1aca160a44b1fbe21b223500958e3c78a904033cf86e` | diff complet des trois pièces d'écart contre leurs originaux à S |
| `sources-d1-ecart2-v1.txt` | `340c7d5a0b4d77029db9359a0d8eb1b598321239bea3c0a822359b2c1a45bc67` | sources de l'unité (D1), lignes citées |
| `rapport-developpeur-p3bis-ecart2-v1.md` | `2ba5201f6cd77fad4006950c77f1c57af7b8b369ca0a4d24cba35296b196b63b` | rapport du développeur |

Sorties choisies du passage final, sous `sorties-essais-ecart2-v1/` (empreintes vérifiées de même) :
`controle-5min-C2-T1-temoin-origine-a-290.txt` (`9b68d953a5b5a76a5b4f166214b9b4611e54f407a211e4bb8c8d3bc4b0d76526`) ;
`controle-5min-C2-T2-ecart-lignes-a-410.txt` (`f5185a54ab8468935a764730c882c022dca0fa459485ce17646d5274e47b034d`) ;
`controle-5min-C2-05-lignes-a-910.txt` (`9f68b5b016af9f8a7d8b873f8a15ed934eea2f3d38eca1b062979f6c2ce4d50e`) ;
`controle-5min-C2-08-fin-amorce-a-505.txt` (`2acbec6ecbd25dc8f9971e1e8ee297d72a2d7248a7c3cefe666558a6a82fa471`) ;
`depenses-S1-01-ecart-valeurs-fille.txt` (`2232e09af474c871d2cdcb04fbf3bdd6459ac9f08257c9f5f554b5dd22728936`) ;
`depenses-S1-02-temoin-origine.txt` (`84a39af1145e985f3ffbc69dd44ad8abdca63a55c73edc26e8ddb68d8cd3134c`) ;
`enchaineur-E3-01-sain-horloge-simulee.txt` (`f1cc74c7c3f6913975e43124e2c515cd691afd9944b1467ebba2764a5ea0774c`) ;
`enchaineur-E3-02-echec-amorce.txt` (`50ff0d5a54098a284242417258c67afdb3089da8dd0d85b2dcd0213c519167cc`) ;
`enchaineur-E3-07-sain-horloge-reelle.txt` (`898c851f5710dd1af0e4c1d021ae726d329fb39402370f8814434362d03c3bcd`) ;
`banc-module-repointe-sur-ecart.txt` (`c6edb421c38a90239dfe9d8d35409df5b978f3037b587242e4a89042c665fbf5`).

**Essais R5** : 132 cas, 0 non conforme ; dernière ligne « ESSAIS DE L'ÉCART 2 DE P3-BIS : CONFORMES » (journal l. 200-202).
Cas sains et artefacts de D1 (D1-01 à D1-15, S1-01 à S1-05), de D2 (C2-01 à C2-30, C2-V01 à C2-V05, C2-X, C2-K1, C2-K2,
témoins C2-T1 et C2-T2) et de D3 (E3-01 à E3-07, dont E3-07 sur l'horloge réelle) ; bancs existants rejoués (R-01 à R-07,
l. 182-199). Les essais jouent un faux outil de location : aucun appel réel, aucune dépense.

**Fixés pour la course sous ce texte** :
- **Enchaîneur** : `enchaineur_p3bis_v5.sh` (`34131eaf…`), seul outil de lancement de la course.
- **Lanceur** : `lancer_p3bis_v2_ecart1_v2.sh` (`2e294e5a64086806591cdd0724561d7a8d7fdaab464705c22f9b92687d6607fb`,
  addendum 1), appelé par l'enchaîneur v5, qui en épingle l'empreinte.
- **Contrôle, surveillance, module** : les trois pièces d'écart 2 ci-dessus, appelées par l'enchaîneur v5.
- **Branche** : `prep/p3bis-ecart2-v1`, commit `07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9`, ou un commit postérieur de cette
  branche qui n'ajoute que cet addendum et son compagnon (à vérifier par `git diff --name-status 07a4b48a <commit>` :
  ajouts seulement, hors du dossier de la chaîne).

## Préalables du lancement

Avant la relance, dans cet ordre, chacun constaté avec l'heure relevée par `date -u` :
1. **Addendum 2 scellé** : contre-lecture et vérification courte faites ; compagnon `.sha256` ; versé sur `main` et sur
   `prep/p3bis-ecart2-v1` ; entrée au registre des décisions.
2. **Destruction de l'instance 60370121 par son identifiant** (R10 ; choisie par Lazar, R-2450) ; absence relue dans la
   liste des instances ; ligne inscrite dans `registres/arrets.md`. Le geste de la mère a été refusé par le classifieur du
   mode automatique (R-2452) : il revient à la session fille de la relance, ou à Lazar. Tant que 60370121 reste sur le compte
   hors `ARRETEES_TOLEREES`, la liste fermée des instances refuse toute création (l. 1949-1954).
3. **Dépense antérieure relevée** au registre des dépenses, puis passée en cinquième argument de l'enchaîneur v5 :
   - toutes les tentatives sous GO-2026-11-10-02 : 60286945 (`registres/depenses.md` l. 420 : ≈ 2,06 USD relevés, dont
     2,00 de majorant, plus le stockage jusqu'à sa destruction à 07:47:20Z, `registres/arrets.md` l. 93) ; 60370121
     (l. 431 : calcul ≈ 0,09 USD, téléchargement ≈ 0,17 à 0,19 USD estimé, plus le stockage jusqu'à sa destruction) ;
   - toute dépense sous GO-2026-11-02-29 : le rédacteur n'a trouvé aucune ligne de ce GO dans `registres/depenses.md`
     (recherche par motif dans ce seul fichier) ; la session le vérifie ;
   - cet addendum ne fixe **aucun montant** ; il demande que le montant passé ne soit jamais sous-estimé (point 7 de la
     dernière section).
4. **Empreintes vérifiées par la session**, écrites avec l'heure : `enchaineur_p3bis_v5.sh` égal à `34131eaf…` (il ne
   vérifie pas la sienne) ; `lancer_p3bis_v2_ecart1_v2.sh` égal à `2e294e5a…` (A1, condition 1). Toute empreinte autre :
   aucun lancement. L'enchaîneur v5 vérifie lui-même les trois pièces d'écart 2 et le lanceur.
5. **Jeu depuis le dossier de la chaîne d'une extraction de la branche** `prep/p3bis-ecart2-v1` (commit ci-dessus), où les
   scripts d'origine sont égaux à S (le bloc 2 du lanceur d'écart l'exige) ; dossier neuf inexistant (R12) ; `HF_TOKEN`
   exporté comme pour le lanceur ; détaché par `setsid nohup`, PID noté, arrêt seulement par ce PID (R10).
6. **Conditions de l'addendum 1 et du texte, inchangées** : crédit présent > 0 et recharge automatique (A1) ; date du jour
   au plus tard le 18 novembre 2026 ; inventaire des instances et `EN_MARCHE` relevés juste avant ; numéro de tentative et
   branche de calcul selon l'écart 11 du lanceur (l. 2289-2291), que l'écart 2 ne touche pas.

## Conditions d'emploi

1. Le contrôle d'origine et la surveillance d'origine ne sont **jamais** joués pour la course sous ce texte. Si l'enchaîneur
   s'arrête après une création sans lancer la surveillance (traces illisibles, l. 77-81 ; empreinte autre juste avant
   l'appel, l. 94-97), la session lance à la main la surveillance d'écart 2, empreinte vérifiée, ou arrête l'instance par son
   identifiant (R10).
2. L'écart vaut pour toute tentative sous ce texte et sous GO-2026-11-10-02, dans la borne de création de l'en-tête.
3. Tout mot contraire de Lazar suspend l'écart : retour aux pièces scellées, ou nœud.

## Réserve au verdict et risque résiduel

- **Réserve écrite au verdict de P3-bis**, transmise au lecteur R13, **à côté de celle de l'écart 1** (« garde du crédit
  levée par écart, R-2399 », A1 l. 176) : « **écart 2 (dépense de téléchargement, fenêtre du contrôle à cinq minutes),
  R-2450** ». Elle vaut pour toute la course dès la première création faite par l'enchaîneur v5.
- **Risque résiduel** :
  - **unité du relevé** : si `inet_*_billed` était dans une unité plus grande que le Kio, la surveillance sous-compterait le
    téléchargement. Le Mo est exclu comme physiquement impossible (plus de 6 To en ≈ 255 s). La vérification se fait sans
    dépense par la session ou par Lazar, non par la chaîne : relever les frais de bande passante de 60370121 sur la facture
    du loueur ; ≈ 0,17 à 0,19 USD confirme le kilo-octet ; environ mille fois plus donnerait raison à la garde d'origine
    (rapport du développeur, l. 434-441) ;
  - **panne silencieuse** vue au plus tard à + 900 s au lieu de + 300 s (≈ 0,35 USD au plus) ;
  - **illisibilité passagère** de l'outil de location tolérée jusqu'à l'échéance ;
  - **dépense antérieure** : saisie par la session ; l'enchaîneur n'en vérifie que la forme.

  La surveillance, le plafond de 80 USD, la liste d'arrêt et la règle de relance s'appliquent tels quels. L'écart ne
  relâche aucune autre règle.

## Points laissés au contre-lecteur

1. **Échéance : 900 s ou 1 200 s.** 900 s laisse une marge de deux sur la partie variable observée (≈ 430 s attendues, deux
   clonages) ; la variante 1 200 s (marge de trois) est un nombre à changer, l. 54 du contrôle (rapport du développeur,
   l. 188-193).
2. **Illisibilités mises en attente** (affaiblissements 2 à 4). Variante stricte écrite par le développeur : remettre le KO
   immédiat sur l'état et le journal illisibles (l. 143 et 170 du contrôle).
3. **Majorant des sens illisibles.** Le code ajoute **une seule fois** 2,00 USD dès qu'un sens est illisible (vérifié, voir
   D1) ; les deux illisibles donnent 2,00 USD, comme à l'origine. Les mots « majorant par paire illisible » de la consigne
   du rédacteur et de R-2453, et la phrase « chaque paire […] ajoute le majorant » du rapport du développeur (l. 132), se
   lisent mal sur ce code. Ce brouillon écrit ce que fait le code. À trancher : un majorant par sens (4,00 USD si les deux
   sont illisibles), ou un seul. Le choix est séparable : il ne touche que la boucle de `depense`, pas la conversion.
4. **Unité non documentée de `inet_*_billed`** : interprétation prudente retenue (Kio, Go décimal) ; vérification par la
   facture de 60370121 proposée, sans dépense (risque résiduel).
5. **Lectures de l'addendum 1 ajoutées par ce brouillon** (A1 l. 74 et l. 167-169), hors de la liste du développeur. À
   confirmer.
6. **Explication du seul échec du banc re-pointé** (R-02, journal l. 184-186). Le développeur l'attribue à l'ancienne unité
   (20 × 0,026 = 0,52 USD). La sortie montre aussi le majorant de la montée absente : « téléchargement 2.00, descente
   0.00 Go », dépense 4,00 USD au lieu de 2,52. L'échec tient donc à la fois à l'unité et au majorant de la montée
   illisible, que l'origine comptait zéro ; il reste attendu.
7. **Montant de la dépense antérieure** : ce brouillon propose qu'il soit arrondi au centime supérieur et qu'un majorant
   écrit (les 2,00 USD de 60286945) reste compté tant qu'une facture ne le remplace pas. À confirmer ou à retirer.
8. **Destruction après la surveillance d'écart** : non jouée par le banc (la destruction est le geste de la session).
   `detruire_p3bis_v2.sh` exige le motif `FIN` dans `motif.txt` du dossier de la surveillance (l. 30) ; le diff de la
   surveillance ne touche pas l'écriture de ce fichier. Compatibilité déduite, non éprouvée.
9. **Portée de D3** : l'enchaîneur n'est pas dans le mot R-2450 ; il est fixé ici à la demande de la consigne de la mère.
   Ce que passaient les v2 à v4 comme dépense antérieure n'est pas au dépôt (la v1 passait 0, R-2393).
10. **Versement** : forme proposée (extraction au commit `07a4b48a` ou à un commit postérieur qui n'ajoute que cet
    addendum) ; à confirmer, sur le modèle de R-2407.

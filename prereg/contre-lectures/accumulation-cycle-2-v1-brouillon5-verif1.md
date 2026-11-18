# Vérification 1 (règle R2, vérification courte) des brouillons 5 du second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1

- **Vérificateur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur (Claude Fable 5.2). N'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni opérateur de la relecture complémentaire, ni développeur, ni lecteur, ni juge de ce cycle. **Déclaré** : même modèle (autre instance) que les contre-lecteurs et vérificateurs des tours précédents.
- **Écrit le** : 2026-11-18, à partir de 22:09 UTC (`date -u`).
- **Mandat** : tâche transmise par la session mère (vérifier les points (1) à (8) sur les brouillons 5 ; rendre un rapport scellé).
- **Pièces vérifiées** (empreinte recalculée par `sha256sum`, égale à son compagnon `.sha256`, toutes) :

| pièce | empreinte |
|---|---|
| préenregistrement, brouillon 5, `prereg/accumulation-cycle-2-v1-brouillon5.md` | `5ef9807c2e7a116349f4dcf98808ff7356674e59fd102de4e90e171180132b6e` |
| ordre exploratoire, brouillon 5, `docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon5.md` | `cb8b3335427e9c5dd11cef77f6c819e7593f6bc4938f040701cd36dddd9af122` |
| devis, brouillon 4, `…/devis-cycle-2-v1-brouillon4.md` | `b606a87f207cd58b7eba035a44d82841a2983f8f1238cb58656b5d137b37ce36` |
| note des différences, `…/differences-brouillons-4-vers-5-v1.md` | `14ab523b223a3262e6822f5909aa9950a07d4b6082da1271211c73fb84a7c521` |
| script de fabrication, `…/pieces-redaction-cycle-2-v1/brouillons5-faire-v1.py` | `f5bfc0209c1eeab3ad80948c463c4b61ab4a3465513f5088925def6ff1cb1faa` |
| calcul version 4, `…/pieces-redaction-cycle-2-v1/calculs-redaction-cycle-2-v4.py` ; sa sortie `sortie-calculs-redaction-cycle-2-v4.txt` | `d0f09e2ecc9be15b614882892729c355c331c02bde9c9e090798e35e05afbe65` ; `cfc7b6969c4c39ac90b25f429bc04af73f13e9ac5e7e0b034ed7e893d800e293` |
| sources : préenregistrement brouillon 4 ; ordre brouillon 4 ; devis brouillon 3 | `92e9021f8efd6f1d6d3f7b2e6c82ae388d5e1c00765a93bcdfa250cf50905f60` ; `feb63aa9c1ba10dd63c984dc2d0b6acc4be4f8f62476fee5f6e5029e5ca66fc1` ; `e8c83fc14c4aed24a49603fa75db7343c08290b2ec5ca6be35560b36d565f734` |
| contre-lecture des brouillons 4, `prereg/contre-lectures/accumulation-cycle-2-v1-brouillon4-cl1.md` (lue **en entier**) | `813176c0c10f98ad9afca3ad6b716b55e409db238f0cd264134e43ab58515f26` |
| note du chemin critique, `…/chemin-critique-cycle-2-v1.md` (section 7, « Leviers », **seule**) | `6231a4f219065784c493629c5ae5e7de6377bec4dd43dca8ec2a6b67d34d5757` |

Choix de Lazar lus : `registres/go.md`, les seules lignes `GO-2026-11-18-56` (point 2 seul, extrait par programme), `GO-2026-11-18-58` et `GO-2026-11-18-63`, repérées par leur numéro.

---

## 1. Verdict

**Scellable après ces couples exacts** — et, comme au tour précédent, après les deux décisions qui restent à Lazar (la règle de réplication, couple B-1 ; le nœud 3), portées sans pente par leurs marqueurs. Deux des couples ci-dessous posent **deux questions neuves à Lazar** (V-1, V-2), que les levées de `GO-2026-11-18-63` font naître et que les textes ne disent pas ; un troisième (V-4) borne la lecture de la levée 1, qui n'est pas vérifiable sur la section des leviers.

En une phrase : la fabrication est exacte à l'octet ; chaque couple de la contre-lecture des brouillons 4 est appliqué tel quel, et les trois écarts déclarés sont justes ; `GO-2026-11-18-58` est porté fidèlement ; `GO-2026-11-18-63` aussi, levées 2, 3 et la levée 4 non accordée comprises, **mais** la levée 2 rend inexécutable, tel qu'écrit, le calendrier de la branche de disque « couche par couche » que Lazar avait retenue en repli (V-1), et le compte des 48 heures pendant un rejeu reste muet (V-2).

| sévérité | couples |
|---|---|
| bloquants | aucun neuf (B-1 et le nœud 3 restent à Lazar) |
| majeurs | V-1 (nœud), V-2 (nœud, marqueur), V-4 |
| mineurs | V-3, V-5 à V-9 |

---

## 2. Réponses aux points

### (1) Le script rejoue les trois textes et la note, à l'octet — **oui**

Les six fichiers que lit le script (trois sources, contre-lecture, note du chemin critique, sortie de calcul version 4) copiés dans un dossier à moi, mêmes chemins relatifs ; script lancé par `python3 -B` depuis ce dossier. Sortie : préenregistrement 32 changements (lignes retirées 18, ajoutées 45, égales 276) ; ordre 16 (12, 29, 162) ; devis 10 (6, 27, 146) ; note écrite. `cmp` contre le dépôt : **les quatre fichiers identiques à l'octet**. Le script vérifie l'empreinte de chaque source, de la contre-lecture et de la note du chemin critique, compte chaque motif et refuse d'écraser (R12). Le journal du script est l'unique source des changements : ce qui n'y est pas est égal à la source.

### (2) Chaque couple appliqué tel quel, ou écart déclaré et juste — **oui**

Vérifié par programme : pour chaque « avant → après » de la contre-lecture (B-1 ×3, M-1 ×2, M-2 ×3, M-3, G-1, G-2, G-3, G-4, G-5 ×3, G-6, m-2, m-3 ×2), le « après » figure **une fois** dans le texte neuf, le « avant » n'y figure plus (sauf quand il est le début du « après »). Entrée m-4 présente avec deux empreintes (brouillon relu, rapport) ; m-6 : calcul version 4 et renvoi depuis « Suite des cycles ».

Écarts déclarés, jugés **justes** :
- **G-1, déclaration de lecture** : la contre-lecture proposait de réécrire « -55, -56 et -57 » en « -55, -56, -57 et -58 ». Le rédacteur garde la déclaration du brouillon 4 et ajoute la sienne (« pour ce brouillon 5, les seules lignes -56, -58 et -63 »). C'est plus exact (qui a lu quoi, à quel tour) et ne perd rien de ce que voulait le couple.
- **G-2, ajout hors couple** : la clé `OUVERTURE-TEMPS1-ACC2` des « Lignes de registre » dit la même chose que le plan, point 2 ; cohérent avec M-3 (le code écrit la réserve à partir de cette ligne).
- **m-1, branche « tant qu'il ne l'est pas »** : le marqueur entre crochets devient `<<NOEUD_3_PORTE_G1>>` aux deux endroits ; la seule occurrence restante de l'ancien marqueur est une citation dans la table de traitement. Voir V-6 pour la façon de le remplir.

### (3) `GO-2026-11-18-58` et `GO-2026-11-18-63` portés fidèlement, sans rien affaiblir d'autre — **oui, avec V-1**

- **`GO-2026-11-18-58`** : condition d'ouverture 3 sans le verdict de la validité de l'adaptateur ; table conjointe gardée « si elle est prévue » ; réserve écrite ; lot de la validité de l'adaptateur ouvert seulement sur lignes existantes et empreintes recopiées ; exclusion de l'analyste gardée et étendue à la transmission de ses sorties. Rien d'autre desserré.
- **Levée 2** (relecture complémentaire avant l'ouverture) — chacun des quatre éléments est écrit :
  - opérateur écarté des verdicts de l'étape B et de l'étape B bis (« ni lecteur ni juge de ces verdicts ni de leur table conjointe »), qui n'est pas l'analyste, nommé par la session mère : ordre, section 2, lot F ; préenregistrement, « Calcul et dépense » ; devis, sections 6 et 10 ;
  - sorties scellées, fermées jusqu'à `OUVERTURE-TEMPS1-ACC2`, qui recopie leurs empreintes : ordre, lot F ; devis, section 10 (la clé de registre du préenregistrement ne le dit pas : V-9) ;
  - aucune sonde apprise avant l'ouverture : ordre, lot F et section 4 ; devis, sections 6 et 10. Le rédacteur l'écrit « tiré, à contre-lire » : **je le juge juste** — la ligne du registre et le levier E de la note ne déplacent que la relecture, et concevoir une sonde est le travail de l'analyste, qui commence à l'ouverture (V-5 le rend ferme) ;
  - rejeu sous le même plafond de 75 USD, compté comme la relance entière déjà chiffrée ; un second rejeu, ou une garde au-delà de sept jours depuis la fin de la relecture : nœud. Arithmétique du devis reprise sans recalcul (58,8 + 13,4 ≈ 72 sous 75).
  - **Ce qui manque (V-1, majeur)** : la branche de disque « couche par couche » (choix de Lazar, `GO-2026-11-18-56`, point 4 (ii)) fait **alterner** relecture et apprentissage, couche après couche, environ 50 Go à la fois. Avec la levée 2 (tout relire avant l'ouverture, n'apprendre qu'après), cette branche n'est plus exécutable telle qu'écrite ; l'ordre, section 4, porte les deux phrases côte à côte. Ni la ligne de GO ni les textes ne disent ce qui vaut alors : nœud.
  - **Ce qui reste flou (V-3, mineur)** : qui juge que le verdict de l'étape B bis « exige » un rejeu, et quelles sorties s'ouvrent ensuite (celles d'origine, celles du rejeu).
- **Levée 3** (48 heures comptées depuis l'ouverture) : ordre, section 8, point 2 (la limite de sept jours est remplacée ; aucune autre mention de sept jours ne vise le temps 1 : les autres « sept jours » sont la garde de l'instance) ; préenregistrement, plan, point 1 ; devis, section 6. Fidèle à la ligne et au mot verbatim « en comptant les 48 heures depuis l'ouverture ».
- **Levée 1** : voir point (4).
- **Levée 4, non accordée** : écrite telle quelle — préenregistrement, décisions (« Levée non accordée : générer la famille pendant le temps 1 ; l'ordre … reste ») et plan, point 2 (« la famille n'existe pas avant `SCELLEMENT-ACC2` … ordre maintenu par Lazar ») ; devis, section 13 ; ordre, section 12. Rien de l'ordre des antériorités ne change.

### (4) La « relecture de sélection » lue comme le tirage de sélection complémentaire sans appel de modèle — **non vérifiable sur la section des leviers ; à confirmer, et à borner (V-4)**

- La section 7 de la note du chemin critique (« Leviers ») **ne nomme aucune levée sur la sélection des tâches fraîches** : le mot « sélection » n'y figure pas ; ses seules mentions des tâches fraîches sont dans la levée D (non accordée : « Les tâches fraîches deviennent alors le chemin critique ») ; le levier 1 parle de « l'extraction par vagues », le levier 2 renvoie à la section 10, que je n'ai pas lue. Les trois levées de la section 7 qui recoupent la ligne du registre sont E (= levée 2), T (= levée 3) et D (= levée 4, refusée). **La levée 1 n'a pas de correspondant dans cette section** ; rien n'y contredit non plus la lecture du rédacteur. Le mot « prudence » de la ligne de registre se trouve dans la note hors de la section 7 (sections 1 et 4, repérées par numéro de ligne seulement, non lues).
- L'affirmation de la note des différences (§ 6, point 1) — « si la levée visait autre chose, ces textes sont plus prudents qu'elle, non plus lâches » — **n'est qu'à moitié exacte** : si la levée visait une autre étape (une relecture de la sélection), le brouillon 5 lève malgré tout une attente que le brouillon 4 imposait et que Lazar n'aurait pas levée (« le tirage attend cette ligne » de dépense de l'extraction). Le dommage possible est borné à la dépense : le tirage est fixé par une règle scellée et contre-lue et une entropie fixée avant lui, donc aucune sélection après lecture n'est possible. Mais « aucun appel de modèle » est affirmé sans source lue par le rédacteur ; si la règle de sélection en demandait, la décision N-049 en ferait une dépense, et la partir sans ligne serait une dépense sans GO.
- **V-4** borne donc la levée : la sélection n'attend plus la ligne de dépense de l'extraction **si** elle ne fait aucun appel de modèle **et si** la session mère confirme la lecture sur le texte qui a posé la levée (R-3456) avant le tirage ; sinon, l'attente du brouillon 4 reste.

### (5) Aucune échappatoire neuve, aucun seuil fixé après une lecture, R3 entière ; marqueurs sans pente — **oui, avec V-7**

- **Aucun seuil numérique neuf** : « 48 heures » est une borne de temps choisie par Lazar, pas un critère d'analyse ; les montants et les sept jours de garde viennent du devis précédent, sans recalcul ; « quarante cycles » est une conséquence arithmétique (point (6)). Rien n'est fixé après une lecture.
- **R3 entière** : aucune levée ne crée une course visant un signe ; la levée 3 rend plus probable un temps 1 clos sans sonde (repli choisi par Lazar, point 6 (b)) — compté et rapporté, visible ; le rejeu de la relecture dépend de ce qu'exige un verdict du développement, non d'un signe (V-3 l'écrit). La réserve neuve de `GO-2026-11-18-58` « ne change aucun état ».
- **`<<REGLE_REPLICATION>>`** : sans pente. Les options sont listées côte à côte (« accumuler, propre » seul, ou aussi « propre, sans gain d'accumulation établi » ; mêmes doses ou dose quelconque) ; la recommandation du contre-lecteur reste dans son rapport. « Au même niveau corrigé » est écrit comme une composante et non comme une option (texte même du couple B-1) : c'est la branche la plus stricte, non une pente vers le lâche. **Reste** une phrase plus ancienne de « Suite des cycles » (« une issue « accumuler, propre » de ce cycle est rapportée… ») qui nomme une seule des deux options ; la garde contre une revendication passe déjà par « toute issue positive » (réserve « non répliquée », « Ce qu'aucune issue ne permet »), mais l'alignement neutre de V-7 ôte toute lecture en pente.
- **`<<NOEUD_3_PORTE_G1>>`** : sans pente ; la table des marqueurs donne les deux manières de le remplir. **Tenue** : remplir le seul marqueur laisserait la suite de la phrase « … n'est pas tranché ; il reste à Lazar » contredire le contenu ; V-6 dit que la phrase entière est remplacée (forme « après » du couple m-1).
- Le validateur refuse le scellement tant que l'un des deux marqueurs reste (point (7)).

### (6) Calcul version 4 rejoué — **sortie identique**

`python3 -I -B` sur une copie : sortie égale octet pour octet à `sortie-calculs-redaction-cycle-2-v4.txt`. Bibliothèque standard, aucune donnée lue. Les valeurs « ≈ 0,05 à deux cycles, 0,10 à quatre, 0,22 à dix » du préenregistrement concordent avec (a) (0,0494 ; 0,0963 ; 0,2237) ; « au plus égale à 0,025 jusqu'à quarante cycles » concorde avec (c) (égalité à K = 40, contrôlée en arithmétique entière).

### (7) Validateur (`controle_ia.prereg.problemes`) rejoué — **un seul problème : seize marqueurs**

Brouillon 4 : quatorze marqueurs de gabarit. Brouillon 5 : **seize** — les quatorze, plus `<<NOEUD_3_PORTE_G1>>` et `<<REGLE_REPLICATION>>` ; aucun autre problème (chaque entrée « Contre-lecture k » porte ses deux empreintes). Plus aucun marqueur entre crochets actif.

### (8) Un rejeu exigé par le verdict de l'étape B bis, pas fini à l'ouverture : les 48 heures attendent-elles ? — **non dit ; phrase proposée (V-2), sans trancher**

Ni la ligne de GO, ni les textes ne le disent ; l'ordre, lot F, suppose seulement que les sorties existent à l'ouverture (la ligne d'ouverture « recopie leurs empreintes »). La phrase proposée (V-2) pose un nœud de Lazar, tranché avant le scellement de l'ordre, porté par un marqueur, avec trois branches côte à côte : (a) l'ouverture attend la fin du rejeu ; (b) l'ouverture n'attend pas, le compte court, les sorties du rejeu s'ouvrent par une ligne à part ; (c) l'ouverture n'attend pas, le compte est suspendu jusqu'à cette ligne. **Fait, sans recommandation** : (a) et (b) gardent la lettre « comptées depuis l'ouverture » ; (c) y ajoute une suspension que la ligne ne contient pas ; les trois demandent le mot de Lazar. Même silence, plus ancien et hors de mon mandat de juger : l'analyste neuf qui remplace un analyste exposé (ordre, section 8, point 4) repart-il avec le reste des 48 heures ? À poser avec V-2 si la session mère le juge utile.

---

## 3. Couples exacts (avant → après)

Chaque « avant » est copié du texte neuf et y figure **une seule fois** (vérifié par comptage).

### Majeurs

**V-1 — branche de disque « couche par couche » et levée 2 : nœud (ordre, section 4 ; devis, section 6).**
- Ordre. Avant : « entre les deux, l'instance est arrêtée et gardée (devis, section 6). Sans ce GO, »
- Après : « entre les deux, l'instance est arrêtée et gardée (devis, section 6). **Sous la branche de disque couche par couche**, la relecture et l'apprentissage alternent d'une couche à l'autre (environ 50 gigaoctets à la fois : devis, section 6) : relire les trois couches avant l'ouverture et n'apprendre qu'après n'y est pas exécutable tel qu'écrit — cas que `GO-2026-11-18-63` ne dit pas : nœud de Lazar, tranché avant le lancement de la relecture ; tant qu'il ne l'est pas, la relecture n'est lancée que sous la branche d'au moins 250 gigaoctets. Sans ce GO, »
- Devis. Avant : « (ordre exploratoire, section 2, lots E et F) ; »
- Après : cette même fin de ligne, suivie d'une ligne neuve : « - **sous la branche de disque (ii)** (couche par couche, environ 50 Go à la fois) : la relecture et l'apprentissage y alternent d'une couche à l'autre ; relire les trois couches avant l'ouverture et n'apprendre qu'après n'y est pas exécutable tel qu'écrit — cas que `GO-2026-11-18-63` ne dit pas : nœud de Lazar, tranché avant le lancement de la relecture ; tant qu'il ne l'est pas, la relecture n'est lancée que sous la branche (i) ; »

**V-2 — rejeu de la relecture non fini à l'ouverture : nœud, marqueur (ordre, section 8, point 2).**
- Avant : « la relecture complémentaire, jouée avant l'ouverture, n'entre pas dans ce compte ; »
- Après : « la relecture complémentaire, jouée avant l'ouverture, n'entre pas dans ce compte ; si un rejeu de la relecture exigé par le verdict de l'étape B bis n'est pas fini quand les autres conditions d'ouverture sont remplies — cas que `GO-2026-11-18-63` ne dit pas —, la règle est un nœud de Lazar, tranché avant le scellement de cet ordre : `<<REJEU_A_L_OUVERTURE>>`, l'une de (a) l'ouverture attend la fin du rejeu, et la ligne `OUVERTURE-TEMPS1-ACC2` recopie les empreintes de ses sorties ; (b) l'ouverture n'attend pas, le compte court depuis elle, et les sorties du rejeu s'ouvrent à l'analyste par une ligne à part, à leur scellement ; (c) l'ouverture n'attend pas, et le compte est suspendu de l'ouverture à cette ligne à part ; »
- Et la ligne de la levée 3 de la section 12 dit, au brouillon suivant, que ce point est porté par ce marqueur (tenue).

**V-4 — levée 1 bornée : aucun appel de modèle, lecture confirmée (préenregistrement, deux endroits ; devis, section 7).**
- Préenregistrement, décisions. Avant : « lue ici comme le tirage par la règle de sélection, sans appel de modèle — »
- Après : « lue ici comme le tirage par la règle de sélection, sans appel de modèle (lecture à confirmer par la session mère sur le texte qui a posé la levée, R-3456, avant le tirage ; à défaut, le tirage attend la ligne de dépense de l'extraction, comme au brouillon 4) — »
- Préenregistrement, « Calcul et dépense ». Avant : « la sélection complémentaire (le tirage par la règle de sélection, sans appel de modèle, 0 USD) n'attend ni ce devis ni sa ligne (`GO-2026-11-18-63`, levée 1) : elle attend seulement la règle du tirage complémentaire scellée et contre-lue et son entropie fixée (plan, point 3, inchangé) ; »
- Après : « la sélection complémentaire (le tirage par la règle de sélection, 0 USD) n'attend ni ce devis ni sa ligne (`GO-2026-11-18-63`, levée 1) **si elle ne fait aucun appel de modèle et si la lecture de la levée est confirmée** (« Décisions qui fondent ce texte ») : elle attend alors seulement la règle du tirage complémentaire scellée et contre-lue et son entropie fixée (plan, point 3, inchangé) ; sinon, elle attend la ligne de dépense de l'extraction, comme au brouillon 4 ; »
- Devis, section 7. Avant : « **la sélection complémentaire** (le tirage par la règle de sélection : aucun appel de modèle, 0 USD de carte) **ne l'attend plus** »
- Après : « **la sélection complémentaire** (le tirage par la règle de sélection, 0 USD de carte) **ne l'attend plus, si elle ne fait aucun appel de modèle et si la session mère a confirmé la lecture de la levée sur le texte qui l'a posée (R-3456), avant le tirage** »
- Devis, section 7. Avant : « elle part dès que la règle du tirage complémentaire est scellée et contre-lue et que son entropie est fixée (préenregistrement, plan, point 3, inchangé). »
- Après : « elle part dès que la règle du tirage complémentaire est scellée et contre-lue et que son entropie est fixée (préenregistrement, plan, point 3, inchangé) ; sinon, elle attend la ligne de dépense de l'extraction, comme au brouillon 3. »

### Mineurs

**V-3 — rejeu : qui le constate, quelles sorties s'ouvrent (ordre, section 2, lot F).**
- Avant : « **elle est rejouée si le verdict de l'étape B bis l'exige**, sous la même ligne de dépense et son plafond (devis, section 6). »
- Après : « **elle est rejouée si le verdict de l'étape B bis l'exige**, sous la même ligne de dépense et son plafond (devis, section 6) ; la session mère écrit à la ligne de registre de la relecture, avant `OUVERTURE-TEMPS1-ACC2` et sans ouvrir aucune sortie de la relecture, si le verdict l'exige, en citant son passage ; s'il y a rejeu, la ligne `OUVERTURE-TEMPS1-ACC2` recopie les empreintes des sorties d'origine et du rejeu ; pour la part rejouée, seules les sorties du rejeu sont ouvertes à l'analyste, celles d'origine restent scellées et fermées. »

**V-5 — « aucune sonde apprise avant l'ouverture » rendu ferme (ordre, section 2, lot F).**
- Avant : « Tiré par le rédacteur, à contre-lire : aucune sonde n'est apprise sur ces activations avant `OUVERTURE-TEMPS1-ACC2` »
- Après : « **Aucune sonde n'est apprise sur ces activations avant `OUVERTURE-TEMPS1-ACC2`** (tiré de `GO-2026-11-18-63`, qui ne déplace que la relecture ; jugé juste par la vérification des brouillons 5) »

**V-6 — remplir les deux marqueurs de Lazar sans laisser de phrase contraire (préenregistrement, table des marqueurs).**
- Avant : « | `<<NOEUD_3_PORTE_G1>>` | nœud 3 : la formulation retenue (A ou C du brouillon de décision N-074) du contraste à témoin apparié de la porte de fin de phase 1, hors de ce texte — ou le mot de Lazar que ce texte se scelle sans lui (la phrase devient alors « nœud 3 non tranché au scellement ; hors de ce texte ») | Lazar, avant le scellement | »
- Après : « | `<<NOEUD_3_PORTE_G1>>` | nœud 3 : la session mère remplace, dans « Décisions qui fondent ce texte », la phrase entière qui commence par ce marqueur et finit par « il reste à Lazar. » — par « **Nœud 3 tranché par Lazar** (`<ligne de GO>`) : formulation [A ou C] du brouillon de décision N-074, hors de ce texte. », ou, sur le mot de Lazar que ce texte se scelle sans lui, par « Nœud 3 non tranché au scellement ; hors de ce texte. » ; le statut, réécrit au scellement, dit de même | Lazar, avant le scellement | »
- Avant : « | `<<REGLE_REPLICATION>>` | issue positive et issue répliquée (« Suite des cycles », règle de réplication) | Lazar (nœud), recopié par la session mère, avant le scellement | »
- Après : « | `<<REGLE_REPLICATION>>` | issue positive et issue répliquée (« Suite des cycles », règle de réplication) : la session mère remplace le marqueur et le tiret qui le suit, jusqu'à « au même niveau corrigé). », par la règle de Lazar écrite en clair, avec sa ligne de GO | Lazar (nœud), recopié par la session mère, avant le scellement | »

**V-7 — « issue positive » dans la phrase opérante de la règle de réplication, sans pente (préenregistrement, « Suite des cycles »).**
- Avant : « une issue « accumuler, propre » de ce cycle est rapportée avec son compte de cycles »
- Après : « une issue positive de ce cycle, au sens de la règle de réplication fixée ci-dessous, est rapportée avec son compte de cycles »

**V-8 — ce que le rédacteur savait des compteurs (devis, section 7 ; tenue).**
- Avant : « Le rendement du premier tirage est un compteur que ni le rédacteur ni le contre-lecteur n'ont lu. »
- Après : « Le rendement du premier tirage est un compteur que ni le rédacteur ni le contre-lecteur n'avaient lu au brouillon 3 ; pour le brouillon 4, le rédacteur déclare avoir vu, dans la contre-lecture de la note du chemin critique, des compteurs de la sélection d'octobre (préenregistrement, « Ce que les auteurs savaient ») ; aucun chiffre de ce devis n'en est tiré. »

**V-9 — la clé de registre de l'ouverture dit qu'elle recopie les sorties de la relecture (préenregistrement, « Lignes de registre »).**
- Avant : « `OUVERTURE-TEMPS1-ACC2` (elle écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes : `GO-2026-11-18-58`) »
- Après : « `OUVERTURE-TEMPS1-ACC2` (elle écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes : `GO-2026-11-18-58` ; elle recopie les empreintes des sorties de la relecture complémentaire, jouée avant elle : `GO-2026-11-18-63`, levée 2 ; ordre exploratoire, section 2, lot F) »

---

## 4. Ce qui reste avant le scellement

1. **Décisions de Lazar** : la règle de réplication (B-1) ; le nœud 3 (ou son mot que le texte se scelle sans lui) ; **neuves** : la branche de disque couche par couche sous la levée 2 (V-1) ; le compte des 48 heures pendant un rejeu (V-2).
2. **Session mère** : confirmer la lecture de la levée 1 sur le texte qui l'a posée (V-4) ; brouillons suivants portant V-1 à V-9 par script et note des différences ; puis une vérification courte par un agent neuf d'un autre modèle que le rédacteur.
3. Le reste est inchangé depuis la contre-lecture des brouillons 4, § 10.

---

## 5. Ce que j'ai fait ; lectures hors mandat ; refus

- **Lu** : le préenregistrement, brouillon 5, par son en-tête, ses décisions, son plan (points 1 et 2), « Suite des cycles », « Calcul et dépense », les réserves voisines, la clé de registre et la table des marqueurs, et par la différence au brouillon 4 ; l'ordre, brouillon 5, sections 2, 4 et 8 et les lignes changées ; le devis, brouillon 4, sections 6, 7 et 10 et les lignes changées ; la note des différences (rendue par le script, lue dans le script) ; le script entier ; le calcul version 4 entier ; la contre-lecture des brouillons 4, **en entier** ; la note du chemin critique, **section 7 seule** ; `registres/go.md`, les seules lignes -56 (point 2, extrait par programme), -58 et -63.
- **Rejoué** : le script de fabrication, le calcul version 4 et le validateur, dans mon dossier de travail temporaire ; aucune donnée lue.
- **Hors mandat, déclaré** : (1) `src/controle_ia/prereg.py` (motifs du validateur) et `src/controle_ia/scellement.py` (fonction de scellement), pour rejouer et sceller ; (2) dans la note du chemin critique, hors de la section 7 : **numéros de ligne seuls** des mots « tâches fraîches », « tirage », « relecture », « prudence », « lection » (sortie `grep -n | cut`), sans afficher leurs lignes ; (3) listes de noms de fichiers des dossiers du cycle. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat, score ni aire d'aucune étude ; aucune pièce lue ne contenait de résultat d'une étude cloisonnée.
- **Refus** : aucun.
- Ni commit, ni poussée, ni écriture sous `registres/` ; aucun fichier existant modifié ; aucune dépense. Seul fichier écrit dans le dépôt : ce rapport et son compagnon `.sha256`.

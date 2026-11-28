# Vérification de la chaîne v2 de P4-instrument — lentille « fidélité au texte » — v1

Vérificateur neuf (sous-agent), 2026-10-20, de 23:05 à 23:48 UTC. Je n'ai écrit ni la chaîne v1, ni la chaîne v2, ni
le module, ni aucune relecture ; je n'ai pas lu les rapports des vérificateurs « dépense et arrêts » et « données et
fuites » (leurs noms de fichiers seulement, pour compter les rapports à verser), ni `table-rapport.txt`.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## Ce que j'ai tenu

- Lecture seule partout, sauf `…/verification-chaine-v2-fidelite/` (essais sous `travail/`). Dépôt de travail : commandes
  git de lecture seulement, `GIT_OPTIONAL_LOCKS=0`, aucun commit, aucune poussée ; deux clones partagés du dépôt local
  dans mon dossier (C d'essai ; dépôts des bancs).
- Aucun outil de location réel (aucun `vastai` sur le PATH ; faux outils des bancs), aucun réseau.
- Rien lu de `prereg/P3-consignes-v1.md`, des fichiers `textes-actions-*`, de `donnees/`, de `episodes-defaut.json`, de
  `chemin-defaut.json` ; aucune recherche récursive dans le dépôt de travail. Les bancs calculent des empreintes de
  fichiers de données dans leurs clones ; je n'en ai ouvert aucun.
- `python3 -B` et `PYTHONDONTWRITEBYTECODE=1` partout ; aucun `__pycache__` sous `…/chaine-v2/` (vérifié au début et à
  la fin). Aucune clé ni aucun jeton affiché ; aucun sous-agent.
- Fait d'environnement : à 23:15 UTC, pendant mes bancs, `…/50508bff…/scratchpad` est devenu un lien vers
  `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/bloc-notes-session14` (déplacement fait par
  un autre). Effet constaté : un faux échec (P05) dans mon rejeu du banc du lanceur ; P05 et P05b rejoués seuls ensuite.

## Pièces lues (empreintes vérifiées)

- Relecture « fidélité » `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md` : `923c71d87115…` (entière).
- Traitement `…/traitement-CL3-et-relectures-chaine-P4-v1.md` : `4678a01b07bd…` (sceau OK ; table entière).
- Candidat 1 `…/P4-instrument-v1-candidat1.md` : `6422fb45a1dc…` (sceau OK) ; brouillon 4 `32d821fb42e5…` (pour le
  banc) ; plan v2 `…/plan-code-et-chaine-v2.md` : `7c65e4f64e8c…` (sceau OK).
- `…/ecrire_candidat2_v1.py` : `9a59358ec3ba…` ; paires `…/chaine-v2/paires-candidat2-chaine-v2-v1.json` :
  `2f5a591b8bd7…` (égales, octet pour octet, à la sortie rejouée de `outils_essais_p4_v1.py paires-v2`).
- Candidat 2 d'essai : régénéré par moi (module v2, 1 123 tests, paires finales) :
  `1398e10c4c1c5e0d87baac50fd8bfc2d79567e156ad11e40f0355341538e2e72`, égal à l'empreinte que cite le rapport de
  correction. Le dossier `…/chaine-v2-travail/essai-candidat2/` porte un essai plus ancien (`aa11d1dccc11…`, paires
  `f4b3604dc395…`) : lu, comparé (VC2-fidelite-13).
- Chaîne v2 `…/chaine-v2/` : les 31 sceaux compagnons passent `sha256sum -c` ; la table finale de
  `RAPPORT-CORRECTION-v1.md` (`aa671cf4f7ee…`) égale ces 31 sceaux, ligne pour ligne. `NOTES-CHAINE-v2.md` :
  `1691bf2516eb…`. Vingt et un scripts, sept journaux de banc et le journal de la répétition jouet lus.
- Module v2 (`…/module-v2/`, `instrument_p4_v1.py` `c3e78becc07a…`, `lecture_p4_v1.py` `3e41ec106589…`) : contrôles du
  GO, de l'accord, lignes « PROGRES ». Module v3 (`…/module-v3/`, `instrument_p4_v1.py` `000281d02c17…`) : interfaces
  appelées par la chaîne comparées au v2 (mêmes options, fonctions, constantes et clés du résumé).
- Garde de calcul gelée `.claude/hooks/garde_calcul.py` du dépôt : `579f65c8ae30…`, égale à celle de `7a54d43`
  (`git diff` vide) ; registres `registres/go.md`, `registres/decisions.md`, `registres/arrets.md` (en-têtes et
  formes).

## Verdict

**Conforme après corrections.** Les huit décisions « chaîne v2 » sur les constats RC-fidelite sont faites et éprouvées :
les six bancs rejoués, et une copie du banc des contrôles au faux tokeniseur, redonnent les journaux du correcteur
(heures, chemins et numéros de ligne des registres du jour mis à part ; P05 expliqué par l'environnement) ; mon banc du lanceur, joué sur le candidat 2 d'essai réel, refuse les six révocations consignées
pendant l'appel du relecteur et l'accord présent dans l'arbre de S. Restent deux points à régler avant le scellement :
les noms de rapports exigés (`RAPPORTS_NOMS`, phrase « Rapports versés ») ne prévoient qu'un rapport de vérification de
la chaîne v2 alors qu'il en existera trois (VC2-fidelite-01) ; la copie du tokeniseur de la session a disparu, ce qui
empêche de rejouer le banc des contrôles et la répétition finale tels quels (VC2-fidelite-02). Deux corrections ne sont
appliquées qu'en partie (RC-fidelite-04, -07) et quelques phrases ajoutées au texte disent un peu plus, ou autre chose,
que le code.

## Bancs rejoués

C d'essai refait dans mon dossier (`…/chaine-v2-travail/fabriquer_c_essai_v2.sh`, `b78ae0df268d…`, recopié sous
`travail/outils/fabriquer_c_essai_verif_v1.sh` avec deux lignes changées : `GIT_OPTIONAL_LOCKS=0`, module au choix) :
commit `26986574a458919b23fe84282bdb6a2330d4daf5` (tête du dépôt de travail lue : `800435ef…` ; il bouge pendant ma
session), module v2 et chaîne v2 versés, 1 123 tests collectés, candidat 2 d'essai `1398e10c…` retrouvé. Les C d'essai
du correcteur (`8f4814ad…`, `35f90e41…`) ne sont plus sur disque (archive sans clones).

| banc | durée | code | résultat | comparaison au journal du correcteur |
|---|---|---|---|---|
| arrêt | 5 s | 0 | 21 lignes CONFORME, 0 non conforme | identique, heures et chemins mis à part |
| traces | 5 s | 0 | 0 non conforme | identique (une ligne tronquée plus tôt : chemin plus long) |
| surveillance | 21 s | 0 | 93 CONFORME | identique, sauf le délai écrit d'un cas « trop tôt » (70 s au lieu de 94 s) |
| vérifications | 307 s | 0 | 181 CONFORME | identique, sauf les numéros de ligne et empreintes des registres du jour (R00 : registres réels d'aujourd'hui, aucune fausse alerte) |
| scellement | 215 s | 0 | 64 CONFORME | identique, troncatures mises à part |
| lanceur | 1 163 s | 1 | 125 CONFORME, 1 non conforme (P05) | identique sauf P05 : faux échec dû au lien créé à 23:15 (le faux `df` compare un chemin non résolu, le lanceur un chemin résolu). P05 et P05b rejoués seuls ensuite, environnement stable : conformes (`travail/bancs/banc-lanceur-p05-v1.log`) |
| contrôles | — | 2 | non rejouable tel quel : `…/tokeniseur/tokenizer.json` absent (VC2-fidelite-02) | copie du banc (`travail/outils/essais_controles_faux_tokeniseur_v1.sh`, `62c1527120b7…`) dont la copie jouée change une ligne de plus, déclarée (`TOK_JSON` = empreinte d'un faux `tokenizer.json`) : 1 083 s, code 0, 86 CONFORME comme le correcteur, journal identique hors troncatures (T01 à T03 éprouvent la présence, le sceau et l'empreinte, pas le contenu) |
| répétition jouet | non rejouée | — | plus de 20 minutes (passages 1 et 5 : 2 098 s et 2 089 s au journal) | `verifications_p4_v1.py repetition 35f90e41… repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md 1398e10c…` : code 0 ; quatre scripts répétés égaux à la chaîne v2 |
| preuves | — | 0 | `verifications_p4_v1.py preuves` sur les sept journaux | 16 scripts éprouvés, tous égaux aux scripts livrés |

Mon banc du lanceur (`travail/outils/banc-fidelite-lanceur-v2-v1.sh`, `c564a11bfb4e…` ; journal
`travail/bancs/banc-fidelite-lanceur-v2-v1.log`) : mise en place du banc du correcteur (lignes 1 à 186) reprise telle
quelle, sauf le texte de S, qui est le candidat 2 d'essai réel. 257 s, code 0, 16 cas conformes sur 16 : F00 sain
(création) ; F01 et F02 (révocation de GO-2026-10-20-07, GO-2026-10-04-08, GO-2026-10-20-06, R-262, R-269 au registre
des GO, consignée pendant l'appel) et F03 (« **Révocation de R-262** », « **Révocation de R-269** » au registre des
décisions, pendant l'appel) : refus en code 2, motif « GO et dépense relus juste avant la création » ; F04 à F06
(type « Révocation », « Annulation de … R-262 », « Retrait de R-269 », pendant l'appel) : refus « forme voisine » ;
F07 (mention libre de R-269, témoin) : création ; F08 (accord à 120,41 USD) : création, ALERTE écrite deux fois dans
`lancement.txt` ; F09 (S refait après l'accord : accord dans l'arbre de S) : refus.

Lectures du texte par la chaîne, jouées sur le candidat 2 d'essai (`travail/candidat2/`) : les 25 valeurs du bloc 9
des contrôles toutes présentes ; les sept intitulés une fois chacun ; six lignes « Module de P4 » ; chemin de la
configuration une fois ; ligne « Lancement » exacte ; ligne du GO ; `problemes()` vide ; table « Données lues » à
dix lignes (textes de P3 à `ba05fa13…`, l'empreinte du contrôle des traces) ; onze rapports cités sous la forme lue
(`` `prereg/contre-lectures/X` (`sha`) ``), le douzième à « <empreinte au versement> ».

## Décision par décision

| constat (décision) | correction lue (script, lignes) | cas du correcteur rejoués | mes cas | état |
|---|---|---|---|---|
| RC-fidelite-03 (chaîne v2) : révocation consignée pendant l'appel | `lancer_p4_v1.sh` l. 344-349 (GO et dépense relus après l'offre et le crédit, juste avant la garde et la création), l. 346 et 352 (`garde_intacte`) ; `verifications_p4_v1.py` l. 167-210 (formes voisines), l. 228-232 (code 2) | L20 à L23, L30 à L32, G06 (lanceur) ; V42 à V59b, R00 (vérifications) : conformes | F01 à F07 de mon banc, dont les six cas F02 et F03 du relecteur, tous refusés ; témoin F07 accepté | appliqué ; phrase du texte plus large que le code sur un point (VC2-fidelite-06) |
| RC-fidelite-04 (chaîne v2) : dépense au-delà de la borne | `controle_cinq_minutes_p4_v1.sh` l. 30-31, 123-124 (téléchargement, stockage relus) ; `recuperation_p4_v1.sh` l. 91, 101-114 (heure limite écrite en échec) | C21 à C23b (surveillance) : conformes ; A50 (contrôles) : conforme (copie au faux tokeniseur) | lecture : `LIMITE` n'est comparée à aucune heure ; aucun rappel | en partie (VC2-fidelite-03) |
| RC-fidelite-05 (chaîne v2) : plafond de la phase | `verifications_p4_v1.py` l. 89, 251-275 ; phrases « accord-forme-150 » et « precision-7 » | A08 à A08g (vérifications), A16, A17 (lanceur) : conformes ; A44j (contrôles) : conforme (copie au faux tokeniseur) | F08 (alerte à 120 USD), F00 | appliqué (forme : VC2-fidelite-10) |
| RC-fidelite-06 (chaîne v2) : arrêts par l'identifiant | `arreter_p4_v1.sh` (neuf) l. 46-88 ; `surveiller_p4_v1.sh` l. 107-116, 134-147 ; `controle_cinq_minutes_p4_v1.sh` l. 156-165 | A00 à A13 (arrêt), M00 à M04c, S20, S21, C25 (surveillance) : conformes | ligne prête comptée : 5 cellules pour un registre à 4 | appliqué ; VC2-fidelite-05 |
| RC-fidelite-07 (chaîne v2) : arrêt pendant le run, de bout en bout | `repetition_jouet_p4_v1.sh` l. 155-165, 193 (cinquième passage, `duree_max_s` 0,001 s) ; `verifications_p4_v1.py` l. 521-535 | répétition non rejouée (> 20 min) ; `repetition` : code 0 ; J23, J24, J27 (vérifications) : conformes | lecture : le délai externe de 90 minutes (TERM) reste non éprouvé | en partie (VC2-fidelite-07) |
| RC-fidelite-08 (chaîne v2) : accord avant S | `lancer_p4_v1.sh` l. 115-119 ; phrase « accord-apres-s » | N10, P00 (lanceur) : conformes | F09 refusé ; F00 (accord après S) créé | appliqué |
| RC-fidelite-09 (chaîne v2, information) : lignes de progression | phrase « paragraphes », quatrième puce | — | module v2 l. 1221-1389 : `etape=format`, `etape=M5 conforme=True`, `etape=bras … niveau_1=`, `etape=identite exclues= total=`, `etape=bras tache=`, `etape=fin actions=` ; aucune aire, ni C1, ni M6 ; `progres.txt` de la surveillance l. 125-128 | appliqué, la phrase dit vrai |
| RC-fidelite-12 (chaîne v2) : rapports versés | `verifications_p4_v1.py` l. 95-109, 284-298 ; `controles_avant_depense_p4_v1.sh` l. 85-88, 192-201 ; `sceller_p4_v1.sh` l. 52-55, 106-117 ; phrase « rapports attendus » | K00 à K05 (vérifications), S16, S28 (scellement) : conformes ; Z1d, Z1e, Z1e2 (contrôles) : conformes (copie au faux tokeniseur) | onze empreintes citées recalculées sur les fichiers : égales ; trois rapports de vérification de la chaîne v2 pour un nom | appliqué ; VC2-fidelite-01 |
| RC-fidelite-01, -02 (hors chaîne v2) | `ecrire_candidat2_v1.py` (T1 à T3) ; module v2 (CL3-01) | — | candidat 2 d'essai : commit en 40 signes, « Tests attendus : `1123` », scripts de l'instance, « Lancement » lus par la chaîne ; lanceur accepté (F00) | hors de ma lentille ; rien à redire |
| RC-fidelite-10, -11 (information) | rien | — | — | conforme à la décision |

Liste CHAINE : vingt et un noms, identiques dans `sceller_p4_v1.sh` (l. 67-71), `lancer_p4_v1.sh` (l. 73-77),
`essais_lanceur_p4_v1.sh` et `essais_controles_p4_v1.sh` ; `essais_scellement_p4_v1.sh` (l. 43-44) et
`repetition_finale_p4_v1.sh` (l. 42-44) la lisent dans la copie du scellement et exigent 21 ; égale aux 21 scripts du
dossier. Les colonnes « changé, neuf, inchangé » de la section 7 des notes égalent les empreintes de départ de la v1.
Chaque identifiant de cas cité par la section 2 des notes existe dans le journal nommé.

## Constats

### VC2-fidelite-01 — majeur — un seul nom pour les trois rapports de vérification de la chaîne v2

- **Où** : `verifications_p4_v1.py` l. 95-109 (`RAPPORTS_NOMS`, l. 103) ; phrase « rapports attendus » des paires
  (rapport de correction l. 214-232) ; `outils_essais_p4_v1.py` l. 76-89 (`RAPPORTS_CONNUS`, l. 83) ; contrôles
  l. 85-88 et 192-201 ; scellement l. 52-55 et 106-117.
- **Ce qui est** : un nom, `verification-chaine-v2-P4-instrument-v1.md`, « empreinte au versement ». La chaîne v2 est
  vérifiée par trois lentilles, chacune avec son rapport (`…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md`,
  `…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md`, celui-ci). Contrôles et scellement exigent les
  douze noms exacts et refusent tout autre fichier de la famille (nom qui contient « P4 »). Au versement, soit un seul
  rapport entre sous ce nom et deux vérifications R2 sortent de la preuve versée et citée, soit S est refusé. Même
  question pour le module : si le module v3 est retenu (R-295), son rapport (`…/verification-module-v3/verification-module-v3-v1.md`,
  `86577f3d6d5b…`) n'a pas de nom. Enfin, un rapport écrit après le candidat qu'il vérifie (vérification neuve du
  candidat 2, prévue par l'ordre de la session) ne peut pas être cité par ce texte : versé sous
  `prereg/contre-lectures/` avec « P4 » dans son nom, il ferait refuser les contrôles et le scellement.
- **Ce qui devrait être** : un nom par rapport réellement rendu, cité avec son empreinte ; une règle écrite pour les
  rapports postérieurs au candidat.
- **Correction proposée** : trois noms (par exemple `verification-chaine-v2-depense-P4-instrument-v1.md`,
  `…-donnees-…`, `…-fidelite-…`) dans `RAPPORTS_NOMS`, `RAPPORTS_CONNUS` et la phrase, avec leurs empreintes ; les noms du
  module retenu ; une ligne du texte qui dit où se versent les rapports postérieurs au candidat (hors de la famille
  « P4 », ou ailleurs). Puis rejouer les bancs qui citent `verifications_p4_v1.py` (tous sauf l'arrêt et la
  surveillance) et la répétition jouet (déjà prévu sur le vrai C, CV2-06).

### VC2-fidelite-02 — majeur (bloque la suite, pas le code) — la copie du tokeniseur de la session a disparu

- **Où** : `…/tokeniseur/` ; `essais_controles_p4_v1.sh` l. 35 et 72-74 ; contrôles l. 296-303 (tokeniseur versé
  exigé) ; phrases « tokeniseur-metrique » et cinquième puce de « paragraphes ».
- **Ce qui est** : `…/tokeniseur/` ne contient plus que `tokenizer_config.json` (`177c7b61…`, égal). `tokenizer.json`
  (`79e3e522…`) est absent : vérifié sur disque et par une recherche sous `/tmp/claude-0` (R11). Le dossier semble
  restauré de l'archive de la passation, qui excluait les données. Le banc des contrôles s'arrête au montage
  (« tokeniseur impossible », code 2, 6 s). Le versement sous `donnees/P4-tokeniseur-v1/` et la répétition finale
  (mesures de conception sur le vrai tokeniseur) en dépendent aussi.
- **Ce qui devrait être** : la source du tokeniseur à verser, présente et à son empreinte, avant les bancs sur le vrai C.
- **Correction proposée** : la session refait la copie à la révision citée (`0e9e39f2…`), vérifie `79e3e522…` et
  `177c7b61…`, la verse sous `donnees/P4-tokeniseur-v1/` avec ses sceaux, puis fait pointer le banc des contrôles sur la
  copie versée (nouvelle empreinte du banc : à rejouer). Ma copie du banc au faux tokeniseur (ci-dessus) montre que le
  reste des contrôles tient sur les registres du jour.

### VC2-fidelite-03 — mineur — RC-fidelite-04 appliqué en partie : la borne du disque n'est relue par personne

- **Où** : `recuperation_p4_v1.sh` l. 91 (calcul de `LIMITE`), l. 113 (seul usage) ; phrase « liste-d-arret » ;
  `lancer_p4_v1.sh` l. 367 (« 24 heures au plus après l arrêt »).
- **Ce qui est** : l'heure limite n'est écrite que dans une récupération en échec ; aucune récupération ne compare
  l'heure du moment à cette limite, et aucun rappel n'est programmé. Une récupération jouée après la création + 9 600 s
  + 24 h passe et détruit sans marque. La limite part de la création, quand le texte (Plan d'analyse, point 7) et
  `lancement.txt` parlent de 24 heures après l'arrêt. La phrase ajoutée rattache « dépense au-delà de la borne de
  l'étape » au contrôle à cinq minutes, qui ne relit que des prix, une fois, entre 3 et 5 minutes ; le volume
  téléchargé (≈ 20 Go supposés) n'est observé nulle part.
- **Ce qui devrait être** (correction proposée par RC-fidelite-04, acceptée) : un KO ou une ligne de nœud au-delà de la
  limite ; une seule définition de la limite.
- **Correction proposée** : dans la récupération, une ligne « heure limite dépassée de N s : borne du disque dépassée :
  nœud de Lazar » (sans retarder la destruction) ; limite écrite à partir de l'heure d'arrêt relue (`arret.txt`) ou
  phrase alignée sur « création + 9 600 s + 24 heures » ; phrase de la liste d'arrêt qui nomme les observables et dit
  que le volume téléchargé n'est pas relu.

### VC2-fidelite-04 — mineur — « récupération en échec » : les refus en code 2 n'écrivent ni l'état ni l'heure limite

- **Où** : `recuperation_p4_v1.sh` l. 87-90, 92-95, 115 ; phrase « liste-d-arret » (« Récupération en échec : aucune
  destruction ; la récupération écrit l'état de l'instance et l'heure limite »).
- **Ce qui est** : place disque insuffisante, clonage impossible, traces d'un autre lancement : code 2, rien n'est
  détruit, mais ni état ni heure limite écrits (la limite est pourtant calculée l. 91 dans les deux premiers cas). Le
  journal de la répétition le montre pour `artefact-place-disque`.
- **Correction proposée** : appeler `gardee` avant ces sorties quand la création est lue, ou écrire au texte
  « Récupération en échec (code 1) ».

### VC2-fidelite-05 — mineur — la « ligne prête pour registres/arrets.md » n'a pas la forme du registre

- **Où** : `arreter_p4_v1.sh` l. 84-85 ; phrase « arret » ; `registres/arrets.md` (en-tête).
- **Ce qui est** : cinq cellules (date, cible, « P4-instrument », motif, vérification) et une date sans heure ; le
  registre a quatre colonnes (« date (UTC) | cible | raison | vérification après arrêt ») et des dates « AAAA-MM-JJ
  HH:MM ». Compté sur la ligne écrite par mon rejeu du banc (cas A02).
- **Correction proposée** : `| AAAA-MM-JJ HH:MM | instance ID (étiquette p4-v1 ; vastai stop instance ID,
  arreter_p4_v1.sh) | P4-instrument : MOTIF | demandé à …, relu arrêté (…, …) à … |`, et un contrôle du nombre de
  cellules dans le cas sain A00.

### VC2-fidelite-06 — mineur — « type absent de l'en-tête du registre des GO » : trois types du registre passent

- **Où** : `verifications_p4_v1.py` l. 86-87 (`TYPES_GO`), l. 201 ; phrase « revocation-voisine ».
- **Ce qui est** : `TYPES_GO` compte comme connus les types écrits par R-281, que l'en-tête du registre place « hors de
  la liste » : « lecture complémentaire », « règle », « décision ». Essai : une ligne de GO de type « décision » qui dit
  « Lazar révoque R-269 » n'est vue ni par le module (forme exacte) ni par les formes voisines (0 ligne) : création
  possible. Sur les registres du jour, aucune ligne de ces trois types ne nomme l'un des cinq identifiants.
- **Ce qui devrait être** : ce que dit la phrase, et le principe « refuser plus que la forme exacte, jamais moins ».
- **Correction proposée** : retirer ces trois types de `TYPES_GO` (aucune fausse alerte aujourd'hui), avec un cas au
  banc des vérifications et au banc du lanceur ; à défaut, écrire « absent de la liste des types (en-tête et R-281) ».

### VC2-fidelite-07 — mineur — RC-fidelite-07 appliqué en partie : le délai externe de 90 minutes reste non éprouvé

- **Où** : `repetition_jouet_p4_v1.sh` l. 155-165 et 193 ; `p4_instance_v1.sh` l. 236-262.
- **Ce qui est** : le cinquième passage arrête le module par `duree_max_s` (0,001 s) : résumé avec motif, partiels
  poussés, récupération conforme (journal l. 44-88). La seconde moitié de la correction proposée (copie de l'instance au
  délai de 90 minutes réduit, ligne comptée) n'est pas faite : la voie TERM du `timeout`, convertie par le module en
  arrêt consigné, n'est jouée ni par la répétition ni par les tests du module (qui effacent seulement le drapeau). La
  suite côté instance (code non nul, résumé avec motif) est commune avec le cinquième passage.
- **Correction proposée** : un sixième passage (copie de `p4_instance_v1.sh` dont seule la ligne `DELAI` change, sur un
  run jouet assez long) ; ou une ligne des notes qui dit que cette garde n'est pas éprouvée de bout en bout (R5).

### VC2-fidelite-08 — mineur — un repli de la récupération affiche des lignes sans recherche des fenêtres

- **Où** : `recuperation_p4_v1.sh` l. 127-138 (filtre de repli), l. 141, 271, 424 ; phrase « paragraphes », première
  puce (« Aucun motif d'arrêt ni ligne de journal n'est affiché sans masquage des jetons puis recherche des
  fenêtres »).
- **Ce qui est** : si le module commun de S ou les textes de P3 sont illisibles, le filtre ne fait que masquer les
  jetons et tronquer à 400 caractères ; le motif d'un arrêt (« 4a arrêt ») et la dernière ligne du journal (« 6a »,
  traces seules) s'affichent alors sans recherche des fenêtres. Le KO 4f le déclare (pas de repli silencieux), mais la
  phrase dit « aucun ». Aucun banc ne joue ce repli.
- **Correction proposée** : dans le repli, n'afficher que les lignes OK, KO et « -- » à forme fixe, et les autres par
  leur longueur et leur empreinte courte (comme `montrer_ligne` de la surveillance) ; un artefact « textes absents » à
  la répétition.

### VC2-fidelite-09 — mineur — « versée avec MC-1 sous donnees/P4-tokeniseur-v1/ » ne décrit pas ce qui a eu lieu

- **Où** : phrase « tokeniseur-metrique » (rapport de correction l. 172-184).
- **Ce qui est** : la sortie scellée de MC-1 (`docs/notes/P4-mesures-v1/mesures-conception-p4-v1.json`, clé
  `tokeniseur`) ne porte que les deux empreintes ; le tokeniseur n'est pas encore versé (notes, section 4 : la répétition
  finale « exige … le tokeniseur versé » ; le banc des contrôles le copie de la session). La cinquième puce de
  « paragraphes » dit, elle, « versé par la session ».
- **Correction proposée** : « copie de la session, à verser par la session avant S sous
  `donnees/P4-tokeniseur-v1/tokenizer.json` (`79e3e522…`) ».

### VC2-fidelite-10 — forme — « l'alerte … est écrite à l'accord »

- **Où** : phrase « accord-forme-150 » ; `verifications_p4_v1.py` l. 272-275 ; `lancer_p4_v1.sh` l. 152-160, 194.
- **Ce qui est** : l'alerte s'écrit dans `lancement.txt` et sur la sortie du lanceur, à chaque relecture de l'accord
  (deux fois : cas F08), pas dans la ligne d'accord ; personne n'est prévenu par la chaîne.
- **Correction proposée** : « écrite dans les traces du lancement à chaque relecture de l'accord ; la session la
  rapporte à Lazar ».

### VC2-fidelite-11 — forme — mots de tête et codes cités par les phrases de révocation

- **Où** : phrase « revocation-voisine » et « precision-5 » ; `verifications_p4_v1.py` l. 88.
- **Ce qui est** : le code prend les débuts « revoc », « revoqu », « annul », « retrait », « retir » (donc aussi
  « annule », « retire ») : il refuse plus que la liste écrite, ce que la phrase permet. « Code 1 » et « code 2 » sont
  ceux du module commun ; le lanceur sort en code 2 dans les deux cas.
- **Correction proposée** : écrire les débuts tels quels et préciser « codes du module commun ».

### VC2-fidelite-12 — forme — « avant chaque rejeu de la garde gelée » : le bloc 12 des contrôles la rejoue sans relire son empreinte

- **Où** : `controles_avant_depense_p4_v1.sh` l. 357-359 ; phrase « accord-apres-s » ; notes, section 2 (« C : A52 »).
- **Ce qui est** : le bloc 12 exécute la garde du clone de S sans contrôle immédiat ; le bloc 4 (l. 146) relit
  l'empreinte dans le même passage (KO, donc aucune création), et le scellement interdit une autre garde dans S. Le
  cas A52 cité par les notes pour RC-depense-04 change la constante du lanceur, pas le fichier de la garde.
- **Correction proposée** : relire l'empreinte avant le bloc 12 (ou le sauter si le bloc 4 a vu une autre garde), ou
  écrire « avant chaque rejeu par le lanceur et le module commun ».

### VC2-fidelite-13 — information — pièces d'essai citées et pièces sur disque

- Le dossier `…/chaine-v2-travail/essai-candidat2/` porte un essai antérieur (empreintes du module v1, « Tests
  attendus : `1102` », ancienne phrase des rapports à un seul nom de vérification du module), pas le candidat 2 d'essai
  cité (`1398e10c…`), qui n'est plus sur disque ; je l'ai régénéré à l'identique. Les journaux citent des chemins
  `…/chaine-v2/travail/…` qui n'existent plus.
- Les bancs du lanceur, des contrôles et du scellement éprouvent un texte tiré du brouillon 4, phrases de la chaîne v2
  ajoutées à sa fin, pas le candidat 2. Mes lectures statiques et mon banc du lanceur couvrent le candidat 2 d'essai ;
  la répétition finale le couvrira sur le vrai C.

### VC2-fidelite-14 — information — chemins figés de sessions et marqueur « un accord, un lancement »

- Les scripts figent des chemins absolus de bloc-notes de sessions (`H`, `B`, `MARQUEURS`, `PY`, `V` sous
  `…/50508bff…` et `…/5a6b9d1d…`). Depuis 23:15 UTC, `…/50508bff…/scratchpad` est un lien vers un autre bloc-notes ; un
  chemin résolu autrement suffit à fausser un banc (P05). Tout chemin changé change l'empreinte d'un script : nouvelle
  version de la chaîne et bancs à rejouer.
- Le dossier fixe des marqueurs vit dans un bloc-notes : un lancement tenté depuis une autre session ne verrait pas le
  marqueur d'une tentative précédente ; seule resterait la branche distante, poussée environ 2,5 minutes après la
  création. La phrase du texte reste exacte sur ce que fait le script.

### VC2-fidelite-15 — forme — candidat 2 : « le texte prime » écrit deux fois

- **Où** : paire fixe CL3-10 de `ecrire_candidat2_v1.py` l. 84-86 (hors chaîne) ; candidat 2 d'essai, section
  « Chaîne de lancement ».
- **Ce qui est** : « … il se tait sur R-284, que ce texte et le module portent ; le texte prime. Le texte prime sur le
  plan v1 … ».
- **Correction proposée** : retirer « ; le texte prime. » de la paire, ou fondre les deux phrases.

## Comptes

2 majeurs (VC2-fidelite-01, -02), 7 mineurs (-03 à -09), 4 de forme (-10, -11, -12, -15), 2 informations (-13, -14).
Aucun critique.

## Pièces de cette vérification

Sous `…/verification-chaine-v2-fidelite/travail/` : `outils/` (copie du fabricant du C d'essai, mes deux bancs du
lanceur, copie du banc des contrôles au faux tokeniseur), `bancs/` (journaux rejoués, `durees.txt`),
`candidat2/` (candidat 2 d'essai régénéré et son sceau), `paires-v2-rejouees.json`. Le C d'essai et les dépôts des
bancs restent sous `travail/` ; rien n'a été écrit ailleurs.

# Notes de la chaîne v2 de P4-instrument — v1

Correcteur neuf de la chaîne : il n'a écrit ni la chaîne v1, ni aucune relecture, ni le module. 2026-10-20.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.

## 1. Ce qui est livré

- `…/chaine-v2/` : copie de `…/chaine/` (la v1 reste intacte ; empreintes de départ :
  `…/chaine-v2-travail/empreintes-chaine-v1-de-depart.txt`), mêmes noms de scripts, à verser sous
  `docs/procedures/P4-instrument-v1/`. Vingt et un scripts, liste CHAINE du scellement, du lanceur et des bancs
  (table de la section 7).
- Quatre scripts neufs : `arreter_p4_v1.sh` (arrêt par identifiant), `controler_traces_p4_v1.sh` (traces de la
  session avant tout versement), `essais_arret_p4_v1.sh`, `essais_traces_p4_v1.sh` (leurs bancs).
- Huit journaux de preuve : sept bancs et la répétition jouet (section 6). `verifications_p4_v1.py preuves` (sept
  journaux des bancs) et `verifications_p4_v1.py repetition` : code 0.
- `paires-candidat2-chaine-v2-v1.json` (`2f5a591b8bd7d420509026c6d63e626602648f5d6925a391829ce560b34378fb`) : onze paires exactes (ancien → nouveau) qui portent au
  candidat 1 tout ce que la chaîne v2 lit de plus dans le texte (section 5). Elles s'appliquent au candidat 1 réel :
  le candidat 2 d'essai de la répétition en est tiré par `…/ecrire_candidat2_v1.py`.
- Module de P4 : le module v2 (`…/module-v2/`, six fichiers, lus, jamais modifiés ; 1 123 tests collectés). Choix de
  la session (R-293) : voir la section 4.
- Dossier de travail, non versé : `…/chaine-v2-travail/` (C d'essai `c-essai-2` et `c-essai-4`, journaux bruts de
  toutes les passes sous `passe-1/` dont ceux des passes écartées, outils de travail sous `dev/` et à la racine,
  sortie de la finalisation sous `finalisation-1/`, fichier `hors-depot/` de la section 4).

## 2. Constat → correction → cas → journal

Journaux : A = `banc-arret-p4-v1.log` ; S = `banc-surveillance-p4-v1.log` ; T = `banc-traces-p4-v1.log` ;
V = `banc-verifications-p4-v1.log` ; L = `banc-lanceur-p4-v1.log` ; C = `banc-controles-p4-v1.log` ;
E = `banc-scellement-p4-v1.log` ; R = `repetition-jouet-p4-v1.log`.

| constat | correction | cas (sain et artefacts) | journal |
|---|---|---|---|
| RC-depense-01 (majeur), RC-fidelite-06 | `arreter_p4_v1.sh ID DOSSIER_NEUF [MOTIF]` neuf : étiquette relue entière (« p4-v1 » exactement, sinon refus en code 2) ; `vastai stop instance ID` ; état relu arrêté deux fois de suite (60 lectures au pas de 10 s au plus) ; heure de la demande, heure de l'arrêt relu et ligne prête pour `registres/arrets.md` écrites dans le dossier neuf (le registre reste écrit par la session) ; code 1 si l'arrêt n'est pas confirmé. La surveillance l'appelle à chacune de ses sorties (fin, échec d'amorce, redémarrage, état terminal, plafond) ; le contrôle à cinq minutes l'appelle sur tout KO. Code 3 de ces deux scripts : arrêt non confirmé, nœud de Lazar. | A00 à A13 (sain ; déjà arrêtée ; relue arrêtée une fois puis en marche ; étiquette autre, « p4-v1 x », absente ; état illisible ; état qui ne passe pas à l'arrêt ; outil en échec ; identifiant en lettres, à 5 et à 11 chiffres ; outil introuvable ; dossier existant ; motif mal formé ; usage) ; S : M00 à M04c, S20, S21, C25 | A, S |
| RC-depense-02 | récupération : en échec, aucune destruction ; ligne « `--  8 instance … gardée, non détruite : état … ; heure limite de destruction … (création + 9 600 s + 24 h)` » ; 3 Go libres exigés avant le clone (sinon code 2, rien n'est cloné) ; après la destruction, liste relue jusqu'à l'absence (6 lectures). Identifiant et création lus dans `lancement.txt` (traces d'un autre lancement : code 2). | R : les 27 artefacts (chacun avec état et heure limite), `artefact-place-disque`, `artefact-traces-d-un-autre-lancement`, `artefact-instance-encore-listee` ; V : J22, J25 | R, V |
| RC-depense-03 (majeur), RC-depense-08, RC-depense-09, RC-fidelite-03 | formes voisines de révocation (normalisation des accents, tirets, espaces et casse ; type de ligne de GO voisin de « révocation » ou inconnu ; cellule de décision qui commence par révocation, révoque, annulation ou retrait ; identifiants à frontières de mot) : code 2, lignes affichées, jamais de passage silencieux ; aucune fausse alerte sur les vrais registres (copies) ; GO cité par l'accord à frontières de mot ; `verifications go` rejoué juste avant la création, après le choix de l'offre. | V : V42 à V59b, R00 (vrais registres), A09, A09b, G10c, G10c2, G10e, G11b ; L : L20 à L23, L30 à L32, G06, A18 | V, L |
| RC-depense-04 | avant chaque rejeu de la garde gelée : `git diff --quiet S -- .claude/hooks/garde_calcul.py` et empreinte `579f65c8…` exigés, sinon code 2 (module commun, sous-commande `go` ; lanceur, avant chaque rejeu). | V : G15, G15b ; L : L40, L41 ; C : A52 | V, L, C |
| RC-depense-05, RC-fidelite-05 | forme exacte, une fois : « dépense consignée X USD + borne 5,41 USD = Y USD < 150 USD » (deux décimales, virgule décimale) ; somme refaite au centime ; Y < 150 exigé ; alerte écrite à 120 USD et au-delà. | V : A08 à A08g ; L : A16, A17 ; C : A44j | V, L, C |
| RC-depense-06 | surveillance : intervalle de 10 à 300 s (sinon code 2) ; sommeil borné par le reste du plafond ; étiquette relue au départ ; identifiant et création lus dans `lancement.txt`. | S : S10…, S14 à S19, M04c ; C : A49 | S, C |
| RC-depense-07 | destruction : étiquette comparée entière. | R : `artefact-etiquette-p4-v1-x` ; A : A04 ; S : S15 | R, A, S |
| RC-depense-10 | un accord, un lancement : marqueur écrit avant la création (`set -C`) dans `…/marqueurs-lancement-p4-v1/` et copié aux traces ; marqueur présent (ou dans un dossier de traces voisin) ou branche `calcul/p4-reel-v1` présente sur le distant : refus. | L : M00 à M03 | L |
| RC-depense-11 | lignes de `lancement.txt` écrites puis relues avant de quitter le mode d'arrêt sur erreur ; en plus (défaut trouvé par le banc, section 3), lignes calculées relues. | L : M20, M21, P00 | L |
| RC-donnees-01 | fenêtres glissantes : toutes les fenêtres de 48 caractères au pas de 16 (et la dernière), brutes et échappées (JSON, Python), dans la forme brute et déséchappée de chaque fichier, dans chaque chaîne JSON et dans chaque chaîne des tableaux. | V : F00 à F14 ; R : `artefact-texte-echappe-dans-une-trace`, `artefact-texte-sans-sa-fenetre-du-milieu` ; T : T01 à T05 | V, R, T |
| RC-donnees-02 | même recherche sur le chemin des traces seules (code 4). | R : `artefact-texte-dans-les-traces-seules`, `artefact-jeton-dans-les-traces-seules` | R |
| RC-donnees-03, RC-donnees-04 | masquer avant tronquer, partout ; aucun motif d'arrêt ni ligne de journal affiché brut : longueur et empreinte courte, ou texte seulement s'il passe la recherche des fenêtres et le masque (`verifications_p4_v1.py montrer`). | V : W00 à W06 ; R : `artefact-motif-d-arret-qui-recopie-un-texte`, passage 5 (motif affiché par le filtre), ligne « aucune fenêtre affichée par les récupérations » ; S : M07, M10b, C16, C26 | V, R, S |
| RC-donnees-05 | schéma fermé des trois tableaux : clés, types et dimensions ; noms des sondes de la validation = ceux de `scores-p4.npz` (424, même ordre) ; longueurs par jeton liées aux débuts et aux scores. | R : `artefact-validation-a-4096-colonnes`, `artefact-longueurs-par-jeton-doublees`, `artefact-chaine-longue-dans-un-tableau` | R |
| RC-donnees-06 | `controler_traces_p4_v1.sh DOSSIER` neuf : fenêtres et valeurs des jetons sur toutes les traces de la session avant tout versement ; seuls des comptes s'écrivent. | T : T00 à T17 | T |
| RC-donnees-07 | information : contrôle des fuites sur l'instance avant la poussée, version suivante ; rien n'est fait ici. | — | — |
| RC-donnees-08 | liste des chemins gelés lue dans `7a54d43` (`git show`) par les contrôles, le scellement et la répétition, jamais dans l'arbre contrôlé. | C : G01 ; E : S42 | C, E |
| RC-donnees-09 | tokeniseur lu sous `donnees/P4-tokeniseur-v1/` (versé par la session) : empreintes `79e3e522…` et `177c7b61…` et sceaux ; absent ou autre : KO net, mesures de conception non rejouées. | C : T01 à T03 | C |
| RC-donnees-10, RC-fidelite-01 | hors de la chaîne : `ecrire_candidat2_v1.py` (paires fixes de la session). Le candidat 2 d'essai, tiré par ce script, passe la répétition. | R | R |
| RC-fidelite-02 | module v2 (CL3-01). La répétition le joue : lecture sans `--prereg` du run décisif refusée sans rien écrire ; run jouet non décisif lu. | R : lignes « lecture jouet » ; V : J18 à J20b | R, V |
| RC-fidelite-04 | contrôle à cinq minutes : téléchargement au plus 0,05 USD par Go et stockage au plus 0,03 USD de l'heure. | S : C21 à C23b ; C : A50 | S, C |
| RC-fidelite-07 | cinquième passage de la répétition : configuration jouet dont seule `duree_max_s` change (0,001 s) ; le module s'arrête à sa première échéance, écrit son résumé avec motif ; l'instance consigne l'arrêt et pousse les partiels (code 1) ; récupération conforme (code 0, motif affiché, destruction). | R : passage 5, `récupération (passage-5-arret-du-module)` ; V : J23, J24, J27 | R, V |
| RC-fidelite-08 | accord déjà présent dans `registres/decisions.md` au commit S : refus. | L : N10 | L |
| RC-fidelite-09 | phrase du texte (lignes de progression : pas une lecture ; ni aire, ni C1, ni M6). | texte (section 5, clé « paragraphes ») | — |
| RC-fidelite-10, RC-fidelite-11 | information : rien à faire. | — | — |
| RC-fidelite-12 | noms exacts des rapports attendus écrits (`RAPPORTS_NOMS`, douze noms) ; contrôles et scellement exigent exactement ces noms ; phrase « Rapports versés » du texte. | V : K00 à K05 ; C : Z1d, Z1e, Z1e2 ; E : S16, S28 | V, C, E |

## 3. Défauts trouvés par les bancs pendant la correction

- Lanceur : les arguments du `printf` qui écrit `lancement.txt` étaient décalés d'un rang (un argument de trop après le
  passage de la surveillance au dossier des traces). Effet : ligne « contrôle à cinq minutes entre … » fausse, et un
  second bloc vide répété dans `lancement.txt`. Trouvé par le cas sain P00 du banc du lanceur (R5). Corrigé ; le
  lanceur relit en plus, avant la création, les lignes calculées (lanceur, plafond de la surveillance, contrôle à cinq
  minutes, récupération), une fois chacune.
- Répétition jouet (première passe complète, journal gardé dans le dossier de travail, non versé) : trois défauts.
  (1) Le run jouet non décisif était lancé sans l'entropie du préenregistrement jouet : le module s'arrêtait (« modèle
  jouet autre que celui du run source ») et la lecture d'un run arrêté rendait L2 avec le code 0, ligne acceptée par
  le module commun : un repli silencieux. Corrigé : entropie du préenregistrement jouet de a-v1 passée au run, run
  complet exigé (code 0, résumé sans motif d'arrêt), sinon la lecture n'est pas jouée et la ligne attendue manque
  (la répétition échoue). La lecture rend alors L3. (2) La ligne « lecture jouet : aucun __pycache__ … » faisait trois
  lignes « lecture jouet » quand le module commun en compte deux : renommée ; un `__pycache__` écrit arrête désormais
  la répétition (code 1). (3) L'artefact « jeton dans les traces seules » posait le jeton de GitHub, porté par deux
  variables de même valeur : deux KO au lieu d'un ; il pose désormais celui de Hugging Face.
- Bancs : chaînes Python à sauts de ligne littéraux (fabrication des fenêtres, entrées du filtre), guillemets d'une
  chaîne JSON coupés par le shell (cas F07), chemin du bloc-notes factice du banc du lanceur, lignes de la lecture
  jouet (module v2) dans les cas J18 à J20. Corrigés ; les journaux de la section 6 sont ceux des versions finales.

## 4. Écarts et réserves

- Deux écrivains (R-293). Une copie de ce correcteur, relancée hors de l'orchestration par un message de la session,
  a modifié `chaine-v2/` de 19:49 à 19:53 UTC (accord après S et cas du banc du lanceur, adaptation au module v2 :
  `P4_TEXTE_PREREG`, `-B`, lecture jouet ; passages 1 et 5 en même temps ; outil `…/chaine-v2-travail/fabriquer_c_essai_v2.sh`).
  La session l'a arrêtée. Tout est intégré et rejoué ici ; les journaux de la section 6 éprouvent les versions finales.
- Écriture parasite, de mon fait : vers 20:07:21 UTC, une commande en arrière-plan mal formée a créé
  `/home/user/controle-ia-travail/banc-traces.log` (une ligne d'erreur de bash et « code 127 » ; aucun texte, aucun
  jeton). À 20:07:44 UTC, un autre que moi l'a déplacé hors du dépôt, vers
  `…/chaine-v2-travail/hors-depot/banc-traces-ecrit-a-la-racine-du-depot-2026-10-20-2007.log` (66 octets, relu). Aucune
  commande git, aucun autre fichier. Signalé à la session. Toutes les commandes suivantes en chemins absolus.
- Module : la consigne disait « module inchangé pour toi » (module v1). La session a retenu le module v2 (R-293) ; la
  chaîne v2 est éprouvée avec lui (C d'essai, candidat d'essai, 1 123 tests). Le module v3 de P4 est en cours
  (orchestration `wf_07b10b79-4d5` ; « module v3 de P4 vérifié » selon le titre du commit R-295 du dépôt de
  travail) : s'il est retenu,
  refaire le C d'essai, le candidat (empreintes et nombre de tests) et la répétition ; la chaîne v2 ne cite aucune
  empreinte du module.
- C d'essai, pas le vrai C. Bancs : `…/chaine-v2-travail/c-essai-2/depot`, commit
  `8f4814ad54b7c271d30ced6371465eb8e26eaf40` (clone partagé du dépôt de travail à `a82dac76…`, sans les PDF, module v2
  et chaîne v2 versés). Répétition jouet : `…/chaine-v2-travail/c-essai-4/depot`, commit `35f90e41993dd0cffcaaa9e1faba9dd5121454e7` (dépôt de
  travail à `98a95de7…` ; mêmes six fichiers du module v2 ; chaîne v2 finale, dont la répétition corrigée). La
  répétition finale n'est pas jouée : elle exige le vrai C, les journaux versés et le tokeniseur versé. L'ordre de la
  session rejoue bancs, répétition jouet et répétition finale sur le vrai C après le versement.
- Noms des rapports (`RAPPORTS_NOMS`) : deux noms restent à confirmer au versement (vérification de la chaîne v2 ;
  vérification du module retenu). Un nom changé change l'empreinte du module commun : les bancs qui le citent et la
  répétition sont à rejouer, ce que l'ordre de la session fait déjà sur le vrai C.
- Banc des contrôles : la suite complète et les mesures de conception y sont des bouchons (comme en v1) ; elles ne
  tournent en vrai qu'à la répétition finale, sur le vrai tokeniseur.
- La dépense consignée X n'est relue par aucun code : la chaîne relit la forme et la somme ; X reste un geste de la
  session (dit dans le texte, précision 7).
- Deux identifiants de cas partagent le préfixe M01 dans le banc du lanceur (M01-fichier-du-module-change,
  M01-second-lancement-du-meme-s) ; noms complets distincts, verdicts distincts. Forme.

## 5. Phrases du texte (candidat 2)

Fichier exact : `paires-candidat2-chaine-v2-v1.json` (`2f5a591b8bd7d420509026c6d63e626602648f5d6925a391829ce560b34378fb`), produit par
`outils_essais_p4_v1.py paires-v2`. Chaque paire remplace une ancre du candidat 1, trouvée une seule fois. Clés :
accord-forme-150 (RC-depense-05, RC-fidelite-05) ; revocation-voisine (RC-depense-03, -08, RC-fidelite-03) ;
accord-apres-s (RC-fidelite-08, RC-depense-09, -10, -04) ; arret (RC-depense-01, RC-fidelite-06, RC-depense-06) ;
liste-d-arret (RC-fidelite-04, RC-depense-02) ; chaine-traces (RC-donnees-06) ; paragraphes (RC-donnees-01 à -05,
-08, -09, RC-fidelite-09) ; tokeniseur-metrique (RC-donnees-09) ; precision-5 (RC-depense-03) ; precision-7
(RC-depense-05, RC-fidelite-05) ; rapports attendus (RC-fidelite-12 ; une empreinte « au versement » : vérification
de la chaîne v2). Le texte exact de chaque phrase est dans `PHRASES_V2` de `outils_essais_p4_v1.py` et dans le
rapport de correction.

## 6. Journaux de preuve

| journal | sha256 | dernière ligne |
|---|---|---|
| `banc-arret-p4-v1.log` | `15c400cb60448a70b818038eeb5ae0fc97a74b95b75bc1292751d338a51d8489` | FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0 |
| `banc-surveillance-p4-v1.log` | `435b92ba64c9d4a24425b1dd81498e985b6926ab3f537ceba5a3e681f1546458` | FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0 |
| `banc-traces-p4-v1.log` | `b3e5dbcf5a091338564c787a5408f484e6f19701b56406027e3218be6062c2ba` | FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0 |
| `banc-verifications-p4-v1.log` | `0a5c4f9d0787c4939bbac420d9f14f18eec11e82a0900e3cffc7d673e73c4843` | FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0 |
| `banc-lanceur-p4-v1.log` | `b7adeb5ca6bb4b5f7d57089edb7ab59085a85f99da66134e550b3e5de2672742` | FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0 |
| `banc-controles-p4-v1.log` | `55b8fc75d1cee822abff6ba4791e21c31a1d5d4f2e077d1e42caa32d3f0cb627` | FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0 |
| `banc-scellement-p4-v1.log` | `d933980149ecb96bb84490f582d8a9ea6bed2c80a10b76bced694cf1ccb704a0` | FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0 |
| `repetition-jouet-p4-v1.log` | `f266f808e745f499458d817c617a27b4df94ed53b2e950820250633806918ffa` | FIN DE LA RÉPÉTITION |

`verifications_p4_v1.py preuves` (sept journaux des bancs) : code 0 ; sortie :

```
arreter_p4_v1.sh 825701e2847d52e466b228cba46635fdc214cf9bc8fae4ebba8dffb68db85227
controle_cinq_minutes_p4_v1.sh c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6
controler_traces_p4_v1.sh f2fe40f2c9299af17ec7bbe4843d2e36b45c91904affe98b623057b1375c108e
controles_avant_depense_p4_v1.sh c44bd6893c3b201ceb9273ce2a8b3a73b99ebf1589e325ee8fab11a61a9ddbeb
essais_arret_p4_v1.sh d8e4e554c817d3aa8ff6714d657d6313e5d64ec92295f81d29d5331715147891
essais_controles_p4_v1.sh e348e7eec67b92a4df3a3234143a44a47b416ea2c6a6140a4e7f6e2288d852be
essais_lanceur_p4_v1.sh 1c80fe4b45dc422cac5f8481e53a39cf324cbdd8c3fc238d68fc28e85b852173
essais_scellement_p4_v1.sh f68d709117da0faac0d939b2ed588c8b47fc72e457cd0315580081acbdf99b87
essais_surveillance_p4_v1.sh 2f51d42dad9aedcf553a9a9e53226ae3eb09baa1a817a2fe1fd111794b38c4a0
essais_traces_p4_v1.sh 12cb9a0de4594a2e42faaad49703e47d15ccce39119b3aebe1fc7e62e25474c2
essais_verifications_p4_v1.sh d8ab8510be47a8f2cd2fed0ab0cc056cd3baac91e5fbdeba265290e4a308e8b7
lancer_p4_v1.sh 0d2099335ebc31acf643ed275e1cd4789c9e0f78972588cee6a21a2e5d78d2ab
outils_essais_p4_v1.py 9f26389bb4868fda4b98a8e8b378740f7a441eaf5446bfeeba6419ad616d14c5
sceller_p4_v1.sh afd15b53233fc1879faa0c575a2a4762973ec8f9c3d2c7920f07331436fffbf6
surveiller_p4_v1.sh 315ddd7d6141a8c124a9e7e3f1918837c7560a856f1065134506530d94701204
verifications_p4_v1.py cdb6b90a34eabd549c2624441efae12bc6fa1a44ed245d5103f01738099f8f8e
```

`verifications_p4_v1.py repetition` : code 0 ; sortie :

```
outils_essais_p4_v1.py 9f26389bb4868fda4b98a8e8b378740f7a441eaf5446bfeeba6419ad616d14c5
recuperation_p4_v1.sh 65477c6d5d1169ca123d9d087af5c8c74c6d2b80aa9f320f785af01de5d08814
repetition_jouet_p4_v1.sh b6cdba62126894c9e85df59b79930dc9007013f4c4c9e8b9da3d34acb8dd5efc
verifications_p4_v1.py cdb6b90a34eabd549c2624441efae12bc6fa1a44ed245d5103f01738099f8f8e
```

Empreintes citées par les journaux (« script éprouvé », « script répété ») comparées aux scripts de la chaîne v2 :

```
égal : arreter_p4_v1.sh 825701e2847d52e466b228cba46635fdc214cf9bc8fae4ebba8dffb68db85227
égal : controle_cinq_minutes_p4_v1.sh c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6
égal : controler_traces_p4_v1.sh f2fe40f2c9299af17ec7bbe4843d2e36b45c91904affe98b623057b1375c108e
égal : controles_avant_depense_p4_v1.sh c44bd6893c3b201ceb9273ce2a8b3a73b99ebf1589e325ee8fab11a61a9ddbeb
égal : essais_arret_p4_v1.sh d8e4e554c817d3aa8ff6714d657d6313e5d64ec92295f81d29d5331715147891
égal : essais_controles_p4_v1.sh e348e7eec67b92a4df3a3234143a44a47b416ea2c6a6140a4e7f6e2288d852be
égal : essais_lanceur_p4_v1.sh 1c80fe4b45dc422cac5f8481e53a39cf324cbdd8c3fc238d68fc28e85b852173
égal : essais_scellement_p4_v1.sh f68d709117da0faac0d939b2ed588c8b47fc72e457cd0315580081acbdf99b87
égal : essais_surveillance_p4_v1.sh 2f51d42dad9aedcf553a9a9e53226ae3eb09baa1a817a2fe1fd111794b38c4a0
égal : essais_traces_p4_v1.sh 12cb9a0de4594a2e42faaad49703e47d15ccce39119b3aebe1fc7e62e25474c2
égal : essais_verifications_p4_v1.sh d8ab8510be47a8f2cd2fed0ab0cc056cd3baac91e5fbdeba265290e4a308e8b7
égal : lancer_p4_v1.sh 0d2099335ebc31acf643ed275e1cd4789c9e0f78972588cee6a21a2e5d78d2ab
égal : outils_essais_p4_v1.py 9f26389bb4868fda4b98a8e8b378740f7a441eaf5446bfeeba6419ad616d14c5
égal : recuperation_p4_v1.sh 65477c6d5d1169ca123d9d087af5c8c74c6d2b80aa9f320f785af01de5d08814
égal : repetition_jouet_p4_v1.sh b6cdba62126894c9e85df59b79930dc9007013f4c4c9e8b9da3d34acb8dd5efc
égal : sceller_p4_v1.sh afd15b53233fc1879faa0c575a2a4762973ec8f9c3d2c7920f07331436fffbf6
égal : surveiller_p4_v1.sh 315ddd7d6141a8c124a9e7e3f1918837c7560a856f1065134506530d94701204
égal : verifications_p4_v1.py cdb6b90a34eabd549c2624441efae12bc6fa1a44ed245d5103f01738099f8f8e
empreintes citées = scripts de la chaîne v2 : oui
```


## 7. Empreintes (sha256)

| script | sha256 (v2) | v1 |
|---|---|---|
| `verifications_p4_v1.py` | `cdb6b90a34eabd549c2624441efae12bc6fa1a44ed245d5103f01738099f8f8e` | changé |
| `controles_avant_depense_p4_v1.sh` | `c44bd6893c3b201ceb9273ce2a8b3a73b99ebf1589e325ee8fab11a61a9ddbeb` | changé |
| `lancer_p4_v1.sh` | `0d2099335ebc31acf643ed275e1cd4789c9e0f78972588cee6a21a2e5d78d2ab` | changé |
| `sceller_p4_v1.sh` | `afd15b53233fc1879faa0c575a2a4762973ec8f9c3d2c7920f07331436fffbf6` | changé |
| `surveiller_p4_v1.sh` | `315ddd7d6141a8c124a9e7e3f1918837c7560a856f1065134506530d94701204` | changé |
| `controle_cinq_minutes_p4_v1.sh` | `c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6` | changé |
| `arreter_p4_v1.sh` | `825701e2847d52e466b228cba46635fdc214cf9bc8fae4ebba8dffb68db85227` | neuf |
| `recuperation_p4_v1.sh` | `65477c6d5d1169ca123d9d087af5c8c74c6d2b80aa9f320f785af01de5d08814` | changé |
| `controler_traces_p4_v1.sh` | `f2fe40f2c9299af17ec7bbe4843d2e36b45c91904affe98b623057b1375c108e` | neuf |
| `repetition_jouet_p4_v1.sh` | `b6cdba62126894c9e85df59b79930dc9007013f4c4c9e8b9da3d34acb8dd5efc` | changé |
| `repetition_finale_p4_v1.sh` | `94bb9dcab7639c9aeba2b7d6265aba82d8f19784edf5aeec544a4da5d0a17f27` | changé |
| `essais_lanceur_p4_v1.sh` | `1c80fe4b45dc422cac5f8481e53a39cf324cbdd8c3fc238d68fc28e85b852173` | changé |
| `essais_controles_p4_v1.sh` | `e348e7eec67b92a4df3a3234143a44a47b416ea2c6a6140a4e7f6e2288d852be` | changé |
| `essais_scellement_p4_v1.sh` | `f68d709117da0faac0d939b2ed588c8b47fc72e457cd0315580081acbdf99b87` | changé |
| `essais_surveillance_p4_v1.sh` | `2f51d42dad9aedcf553a9a9e53226ae3eb09baa1a817a2fe1fd111794b38c4a0` | changé |
| `essais_arret_p4_v1.sh` | `d8e4e554c817d3aa8ff6714d657d6313e5d64ec92295f81d29d5331715147891` | neuf |
| `essais_traces_p4_v1.sh` | `12cb9a0de4594a2e42faaad49703e47d15ccce39119b3aebe1fc7e62e25474c2` | neuf |
| `essais_verifications_p4_v1.sh` | `d8ab8510be47a8f2cd2fed0ab0cc056cd3baac91e5fbdeba265290e4a308e8b7` | changé |
| `outils_essais_p4_v1.py` | `9f26389bb4868fda4b98a8e8b378740f7a441eaf5446bfeeba6419ad616d14c5` | changé |
| `amorce_instance_p4_v1.sh` | `21b3f447080353741c15d4948e557235dab17201a8d70f4545d1d9f1913c608d` | inchangé |
| `p4_instance_v1.sh` | `8801864fd9f2d940ed7ce2eed43c4efac8251484d37c1dcf3d3bea9bf0d8f967` | changé |

## 8. Rejouer

Depuis n'importe quel dossier, en chemins absolus ; `H=…/chaine-v2`, `W=…/chaine-v2-travail`, `CE=$W/c-essai-2/depot`,
`C=8f4814ad54b7c271d30ced6371465eb8e26eaf40` (bancs), `CE4=$W/c-essai-4/depot`, `C4=35f90e41993dd0cffcaaa9e1faba9dd5121454e7` (répétition) :

- `bash $H/essais_arret_p4_v1.sh RACINE_NEUVE` ; `bash $H/essais_surveillance_p4_v1.sh RACINE_NEUVE` ;
  `bash $H/essais_traces_p4_v1.sh RACINE_NEUVE` ;
- `bash $H/essais_verifications_p4_v1.sh $CE $C RACINE_NEUVE` ; idem pour `essais_lanceur`, `essais_controles`,
  `essais_scellement` ;
- `bash $H/repetition_jouet_p4_v1.sh $C4 $W/c-essai-4/travail/P4-instrument-v1-candidat2-essai.md RACINE_NEUVE $CE4` ;
- `python -B $H/verifications_p4_v1.py preuves $H banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log
  banc-arret-p4-v1.log banc-traces-p4-v1.log banc-verifications-p4-v1.log banc-controles-p4-v1.log
  banc-scellement-p4-v1.log` ;
- `python -B $H/verifications_p4_v1.py repetition $C4 $H/repetition-jouet-p4-v1.log
  P4-instrument-v1-candidat2-essai.md 1398e10c4c1c5e0d87baac50fd8bfc2d79567e156ad11e40f0355341538e2e72`.

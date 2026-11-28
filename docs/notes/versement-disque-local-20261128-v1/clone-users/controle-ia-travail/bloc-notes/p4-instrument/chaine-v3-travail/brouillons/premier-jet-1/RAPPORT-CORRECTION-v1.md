# Rapport de correction de la chaîne de P4-instrument (chaîne v3) — v1

Correcteur neuf de la chaîne v3 (je n'ai écrit ni la chaîne v1 ou v2, ni le module, ni aucune relecture ou
vérification). Session 16, du 2026-10-20 vers 23:30 UTC au 2026-10-21 vers 01:20 UTC.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.
Consigne : `…/consigne-correcteur-chaine-v3-v1.md`. Traitement appliqué : `…/traitement-verifications-chaine-v2-P4-v1.md`
(`10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e`, sceau vérifié), et les deux rapports qu'il traite :
`…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` (`488a7e71…`) et
`…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` (`16298dd2…`), sceaux vérifiés.

## Verdict

**Chaîne v3 conforme sur C d'essai**, avec le module v3. Toutes les décisions du traitement sont appliquées, chacune avec
son cas sain et ses artefacts ; `RAPPORTS_NOMS` porte les vingt-six noms, dans l'ordre exact du traitement. Les sept
bancs sont à 0 cas non conforme ; la répétition jouet est conforme (cinq passages aux codes 0, 2, 1, 124, 1 ; sept
récupérations conformes avec destruction ; vingt-sept artefacts à un seul KO, instance gardée avec état et heure limite ;
trois refus en code 2, dont ceux de la place et du clonage avec état et heure limite ; repli de l'affichage établi ;
lecture jouet : refus sans `--prereg` du run décisif et L3 sur le run non décisif ; aucun jeton ni aucune fenêtre
affichés). `verifications_p4_v1.py preuves` et `repetition` : code 0. Paires du texte écrites ; assemblage du candidat 2
avec les paires du module v3 : `problemes` = [], aucune collision. Aucun désaccord avec le traitement. Réserves : C
d'essai (pas le vrai C) ; banc des contrôles joué avec un `tokenizer.json` de substitution, demandé et annoncé (la copie
de la session manque au bloc-notes restauré) ; quatre rapports à venir ; un choix du correcteur au-delà de la lettre
de VC2-donnees-01 (ligne de l'instance gardée réécrite en repli).

## Ce qui est fait, décision par décision

| décision | fait | cas | journal |
|---|---|---|---|
| VC2-depense-01 (majeur) | `revocations_voisines` = `proposees` du vérificateur, à la lettre ; égale ligne à ligne sur les registres réels (essai unitaire `…/chaine-v3-travail/essais-unitaires/voisines_v3_v1.py`, 20 cas, 0 écart) | V : X01 à X05 (code 2), X06, X07 (code 2), témoins V55 (= V10), V58 (= V12), X08 (passe) ; registres réels à la tête de `main` (`git show`) et de l'arbre de travail : aucune fausse alerte (R00, R00b, R00c) ; L : XL01 à XL05 (code 2, aucune création), XL06 | V, L |
| VC2-depense-02 (mineur) | étiquette comparée dans Python dans l'arrêt et la surveillance | A : A14 à A17 ; S : S15b (code 2, aucune demande d'arrêt, rien de surveillé) | A, S |
| VC2-depense-03 (mineur) | `gardee` définie avant le contrôle de la place, appelée avant les deux sorties en code 2 | R : RX01 (place), RX02 (clonage impossible, artefact neuf), état et heure limite exigés par le module commun ; V : J29 à J31, J33 | R, V |
| VC2-depense-04 (mineur, forme) | ligne prête à quatre cellules, forme exacte du rapport | A : A00 (forme relue par une expression complète) | A |
| VC2-depense-05 (information) | une ligne de plus dans `lancement.txt`, relue avant la création ; phrase de la paire 5 | L : P00 | L |
| VC2-depense-06, -07, -08 | rien (comme décidé) ; -08 : chemins des journaux, voir réserves | — | — |
| VC2-depense, Texte 1 et 2 | paires 2 et 9, blocs à l'identique | comparaison v2 → v3 | — |
| VC2-donnees-01 (mineur) | textes lus à S ; repli : 40 premiers caractères, longueur, empreinte courte ; artefact « repli de l'affichage » à la répétition ; en plus, ligne de l'instance gardée réécrite hors du filtre (CV3-03) | R : `artefact-repli-de-l-affichage`, ligne `REPLI` ; V : J32 | R, V |
| VC2-donnees-02 (mineur) | entrée non ordinaire comptée et refusée (code 1, chemin écrit) par `fenetres`, `jetons` et le contrôle des traces | T : T09, T09b, T09c, T09d ; V : F15 à F18, T03 | T, V |
| VC2-donnees-03, -05, -06, -07, -08 | rien (comme décidé) ; -07 couvert par la lecture des textes à S | — | — |
| VC2-donnees-04 et -09 | phrases « Texte à ajouter » 2 et 4 dans la paire 7, mot pour mot ; phrases 1 et 3 aussi (leurs corrections sont faites) | comparaison v2 → v3 | — |
| `RAPPORTS_NOMS` | vingt-six noms ; bancs adaptés (K00, commentaires ; les bancs des contrôles et du scellement lisent la liste) ; `RAPPORTS_CONNUS` et paire 11 | V : K00 à K05 ; C ; E | V, C, E |

Détail ligne à ligne : `NOTES-CHAINE-v3.md`, section 2.

## Résultats des bancs

Passe finale, module v3, C d'essai `3521ff75c316c9f31403486fc6ca84a1c29daeca` ; chaque journal est la sortie brute de
son banc, redirigée dans un fichier neuf de `…/chaine-v3/`.

| journal | sha256 | lignes « CONFORME » (v2) | dernière ligne |
|---|---|---|---|
| `banc-arret-p4-v1.log` | `559a20608d71fd15f542e281d80ee70c210d72349bf7891272998a9a8dc08f89` | 26 (21) | FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0 |
| `banc-surveillance-p4-v1.log` | `e72391899145dfb6384adee24d1c9c0cc2ef66f5f5cb8704c6afde1302e49e09` | 96 (93) | FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0 |
| `banc-traces-p4-v1.log` | `fe6d6d704587e0dabd363d927ec649592da6bfe232ff7f599d5e8c1e33f3cbe8` | 30 (21) | FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0 |
| `banc-verifications-p4-v1.log` | `b710e63340c9afce389295d42d5b2a34006171113b9c7f5b695d5054e790140f` | 205 (182) | FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0 |
| `banc-lanceur-p4-v1.log` | `97c22ec96ddf7a0b33e7b7c318c723fa513892581078577329e91d1fdf32088e` | 131 (125) | FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0 |
| `banc-controles-p4-v1.log` | `72e0eae853eea63065bd4227afc456c5e47d0943b93892633d325858b7afae3d` | 86 (86) | FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0 |
| `banc-scellement-p4-v1.log` | `615fbe97d804dae5b9d37f5c932a236c5e8139da1cc341ca7d5d92a8812bf99a` | 64 (64) | FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0 |
| `repetition-jouet-p4-v1.log` | `5a0ee9350dfe2fba924e6eeb9536e1824430cd9cebac47a4afd0d2dd8d743e8a` | 7 (—) | FIN DE LA RÉPÉTITION |

- `verifications_p4_v1.py preuves …/chaine-v3` (sept journaux des bancs) : code 0, seize scripts éprouvés, chacun égal au
  script livré.
- `verifications_p4_v1.py repetition 3521ff75… …/chaine-v3/repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md
  79c3e677…` : code 0, quatre scripts répétés égaux aux scripts livrés.
- Répétition : passages 1-sain (code 0), 2 (2), 3 (1), 4 (124), 5-arrêt du module (1) ; sept récupérations conformes avec
  destruction ; vingt-sept artefacts à un seul KO, instance gardée, état et heure limite ; refus en code 2 de la place
  (état et heure limite), des traces d'un autre lancement, du clonage (état et heure limite) ; repli de l'affichage
  établi ; lecture jouet ; aucun jeton, aucune fenêtre affichés ; aucun `__pycache__`.
- Passe préliminaire (C d'essai `3a99173f…`, `…/chaine-v3-travail/passe-1/`) : mêmes verdicts, sauf CV3-01 (corrigé) et
  CV3-04 (minuit, banc du lanceur) ; elle a joué le tokeniseur de substitution (CV3-02).

## Paires du texte

`paires-candidat2-chaine-v3-v1.json` : `f3b715233f7d2c26cbb3d017f90e9d5ce306c6f58a009b3130b5b788f803f575` (onze paires ; 2, 5, 7, 9 et 11 changent ; détail :
`NOTES-CHAINE-v3.md`, section 5). Assemblage avec les sept paires du module v3 (`324c164f…`), dans les deux ordres :
même texte `79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73`, `problemes` = [], aucune collision.

## Constats du correcteur

- **CV3-01** (défaut d'un banc, corrigé) : le cas X08 du banc des vérifications (GO de calcul qui mentionne un retrait
  sans identifiant) portait une apostrophe dans une commande placée entre guillemets simples (`eval`) : la ligne n'était
  pas ajoutée, le registre d'essai perdait la ligne de GO-2026-10-20-07 et le cas sortait en code 1. Trouvé par la passe
  préliminaire (`…/chaine-v3-travail/passe-1/banc-verifications-1.log`) ; apostrophe typographique ; repassé conforme
  (`…/passe-1/banc-verifications-2.log`) avant la passe finale.
- **CV3-02** (réserve levée pendant la correction) : `…/tokeniseur/tokenizer.json` manquait au bloc-notes restauré
  (vérifié sur disque et par recherche hors du dépôt de travail ; listes des archives des sessions 14 et 16 sous
  `registres/passations/` : seul `tokenizer_config.json` y figure). Le banc des contrôles refusait en code 2. J'ai ajouté
  au banc une option explicite, `BANC_TOKENISEUR_SUBSTITUT=1` : sans elle, refus comme avant ; avec elle et seulement si la
  copie de la session manque ou n'a pas son empreinte, un `tokenizer.json` synthétique, annoncé au journal, et une ligne
  de plus changée dans la copie des contrôles (TOK_JSON) ; `tokenizer_config.json` réel exigé. La passe préliminaire l'a
  utilisé (`…/passe-1/banc-controles-2.log`, conforme). La copie de la session est réapparue le 2026-10-21 à 00:06 UTC
  (pas de mon fait), d'empreinte `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` (vérifiée) : la passe
  finale a joué le vrai tokeniseur (journal : « tokeniseur de la session : tokenizer.json 79e3e522635f…,
  tokenizer_config.json réel » ; dix lignes changées, comme en v2) ; la variable était posée, le substitut n'a pas servi.
- **CV3-03** (choix du correcteur, au-delà de la lettre de VC2-donnees-01) : en repli de l'affichage, toutes les lignes
  sont réduites, y compris celle de l'instance gardée ; l'heure limite de destruction ne serait plus lisible, alors que
  RC-depense-02 et la paire 5 disent que la récupération en échec l'écrit. La récupération réécrit donc, après la sortie
  filtrée et seulement en repli, la ligne de l'instance gardée entière, hors du filtre : forme fixe (identifiant de 6 à 10
  chiffres, deux états de l'outil réduits aux lettres, chiffres, points, tirets et soulignés, 20 caractères chacun, heure
  limite calculée) ; aucune donnée de la branche. La même réduction des états vaut pour toutes les lignes « instance
  gardée ». Phrase ajoutée à la paire 7. Éprouvé par l'artefact « repli de l'affichage » (dernière ligne entière, les
  autres réduites). Se retire sans toucher au reste si la session le refuse.
- **CV3-04** (information, banc) : le banc du lanceur dépend du jour UTC (l'accord d'essai est daté du jour au début) : la
  passe préliminaire a franchi minuit et vingt cas ont échoué après M03 (« ligne du jour (2026-10-21) attendue »),
  `…/passe-1/banc-lanceur-1.log` ; aucun défaut de la chaîne (le lanceur réel refuse justement un accord de la veille).
  Passe finale jouée d'un seul tenant le 2026-10-21. La répétition préliminaire a franchi minuit (passage 1 de 23:43 à
  00:17 UTC) sans écart.
- **CV3-05** (information) : la paire 5 précise « Récupération en échec (code 1, ou refus en code 2 faute de place disque
  ou de clonage) » : le troisième refus en code 2 (traces d'un autre lancement) n'écrit ni état ni heure limite, car
  l'instance n'y est pas reconnue comme celle du lancement (identifiant, commit ou création autres) ; la phrase ne
  l'affirme plus.
- **CV3-06** (information) : la commande `paires-v2` d'`outils_essais_p4_v1.py` est remplacée par `paires-v3` (même
  forme, phrases de la v3) ; `…/chaine-v2-travail/fabriquer_c_essai_v2.sh` ne s'applique plus à la chaîne v3 :
  `…/chaine-v3-travail/fabriquer_c_essai_v3.sh` (module v3, chaîne v3, paires du module v3 puis de la chaîne v3).
- **CV3-07** (information) : les journaux bruts citent la cible du lien du bloc-notes
  (`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/bloc-notes-session14/p4-instrument/…`),
  là où les scripts nomment `…/50508bff…/scratchpad/p4-instrument` (`realpath`) ; sans effet sur les empreintes (comme
  VC2-depense-08).
- **CV3-08** (information) : cas ajoutés au-delà de ceux du traitement, pour fermer des formes proches : X06 (type en
  gras), X07 (identifiant de décision entre guillemets inversés), X08 (témoin sain), A15 à A17 (étiquette en majuscules,
  suivie d'une espace, numérique), T09c et T09d, F16 à F18 (lien vers un dossier, lien donné en argument, tube nommé),
  J33 (refus en code 2 de trop).
- **CV3-09** (information) : la tête du dépôt de travail a bougé pendant la correction (`0591049`, `9ecd952`, `0a44ee6` :
  commits d'autres sessions) ; le banc final lit les registres réels à `0a44ee6` (`git show main:…`), égaux à ceux de
  l'arbre de travail (R00c). Le dépôt n'a été que lu (commandes git de lecture, `GIT_OPTIONAL_LOCKS=0`) et cloné par
  référence dans le dossier de travail.

## Désaccords

Aucun. Toutes les décisions du traitement sont appliquées. Un ajout au-delà de la lettre (CV3-03) est signalé ci-dessus,
pas comme un désaccord : il se retire sans toucher au reste si la session le refuse (une ligne de la récupération, une
phrase de la paire 7, une condition de la ligne `REPLI`).

## Réserves

- **C d'essai, pas le vrai C** : bancs et répétition sur `…/chaine-v3-travail/c-essai-2/depot`, commit
  `3521ff75c316c9f31403486fc6ca84a1c29daeca` (dépôt de travail à `0a44ee6`, sans les PDF ; module v3 et chaîne v3
  versés ; candidat 2 d'essai `79c3e677…`, qui n'est pas un candidat). La répétition finale n'est pas jouée (vrai C,
  journaux versés et tokeniseur versé exigés) ; l'ordre de la session rejoue bancs, répétition jouet et répétition finale
  sur le vrai C.
- **Rapports à venir** : 17 (`verification-chaine-v2-fidelite-…`, en cours), 19, 20 et 26 n'existent pas encore ; la paire
  11 les cite « `<empreinte au versement>` ». Si la vérification « fidélité » ajoute un traitement (chaîne v4), la liste
  change, l'empreinte du module commun aussi : bancs et répétition à rejouer.
- **Tokeniseur** : la copie de la session de `tokenizer.json` est revenue pendant la correction (CV3-02) ; je n'en connais
  que l'empreinte, égale à celle du texte. L'option de substitution du banc des contrôles reste (explicite, annoncée).
- **Formes voisines** : la correction de VC2-depense-01 refuse plus large ; une ligne future d'un registre, de tout type,
  dont une cellule commence par « Révocation », « révoque », « annulation » ou « retrait » (« retiré » compris) et nomme
  l'un des cinq identifiants arrête le lancement en code 2 (aujourd'hui : aucune, registres à `0a44ee6`) ; une telle
  fausse alerte ne se lève que par une chaîne et un S nouveaux (VC2-depense-07).
- **Repli de l'affichage** : choix CV3-03 (ligne de l'instance gardée réécrite hors du filtre), à confirmer par la session.
- Hors de ma consigne, non jugés : la vérification « fidélité » de la chaîne v2 (lue seulement pour la question du
  tokeniseur) ; les informations VC2-depense-06, VC2-donnees-03, -05, -06 (version suivante).

## Fichiers livrés

Chaque fichier a son sceau compagnon `.sha256` (forme « empreinte  nom »). Ce rapport n'est pas dans la table (son
empreinte est dans son propre sceau).

| fichier | sha256 |
|---|---|
| `NOTES-CHAINE-v3.md` | `07bc22159f42008b929d70900ba266c6cf71b868c8d99c0942e26f77b4e72106` |
| `amorce_instance_p4_v1.sh` | `21b3f447080353741c15d4948e557235dab17201a8d70f4545d1d9f1913c608d` |
| `arreter_p4_v1.sh` | `53c234e4c1004a56ca1884dcbf4cb8d195c02f3798ba6617fc70053983025806` |
| `banc-arret-p4-v1.log` | `559a20608d71fd15f542e281d80ee70c210d72349bf7891272998a9a8dc08f89` |
| `banc-controles-p4-v1.log` | `72e0eae853eea63065bd4227afc456c5e47d0943b93892633d325858b7afae3d` |
| `banc-lanceur-p4-v1.log` | `97c22ec96ddf7a0b33e7b7c318c723fa513892581078577329e91d1fdf32088e` |
| `banc-scellement-p4-v1.log` | `615fbe97d804dae5b9d37f5c932a236c5e8139da1cc341ca7d5d92a8812bf99a` |
| `banc-surveillance-p4-v1.log` | `e72391899145dfb6384adee24d1c9c0cc2ef66f5f5cb8704c6afde1302e49e09` |
| `banc-traces-p4-v1.log` | `fe6d6d704587e0dabd363d927ec649592da6bfe232ff7f599d5e8c1e33f3cbe8` |
| `banc-verifications-p4-v1.log` | `b710e63340c9afce389295d42d5b2a34006171113b9c7f5b695d5054e790140f` |
| `controle_cinq_minutes_p4_v1.sh` | `c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6` |
| `controler_traces_p4_v1.sh` | `4954f425daa66e9c2464f561fe7190b22ec2ff51b8d037933f214ce1627cd068` |
| `controles_avant_depense_p4_v1.sh` | `c16ba4383ea454c51cffdde330edfcb744021b4c6765a59a09efe57450ba2b48` |
| `essais_arret_p4_v1.sh` | `6b276973eea142c4d4cf62dcca1adb0bb4deaf3f8bbc3088fbcc056e2699c465` |
| `essais_controles_p4_v1.sh` | `4a2a155e1644409c413e70d9a2368456a2890c7e3dc4ca9107a590c959cad650` |
| `essais_lanceur_p4_v1.sh` | `ce8e0e0c744dbaebe7823ca1958fa8ce4f6522fbfdc49389a2412b9afecc45be` |
| `essais_scellement_p4_v1.sh` | `2be5a9e2463427c0ac2fd035d1add6d6a5d2e85f9a56b1d4e84b89725ea702b6` |
| `essais_surveillance_p4_v1.sh` | `2c3539877585811b001bba4c2f1a84593764144af95edf9dad72f5fb20fa4770` |
| `essais_traces_p4_v1.sh` | `9afd19a80d3e8aa0e920a20e8420830aec410ba4006955b3422f986440b75196` |
| `essais_verifications_p4_v1.sh` | `f46cf8bfa3dd3c95cc300697b00de91dec602d4cfa66e6931b134b93770de186` |
| `lancer_p4_v1.sh` | `fedd228bd629c741c70601c9c747566ceb4993f30cbcd510f9c1e6341bb64051` |
| `outils_essais_p4_v1.py` | `c5719362b9ac068860ef7a862e7d85456f8715624e447666a7210fc4ea257f34` |
| `p4_instance_v1.sh` | `8801864fd9f2d940ed7ce2eed43c4efac8251484d37c1dcf3d3bea9bf0d8f967` |
| `paires-candidat2-chaine-v3-v1.json` | `f3b715233f7d2c26cbb3d017f90e9d5ce306c6f58a009b3130b5b788f803f575` |
| `recuperation_p4_v1.sh` | `51e670b33a7fa713c5d47c57ab9bf1a831479a68c714faabf601d9c4720b8157` |
| `repetition-jouet-p4-v1.log` | `5a0ee9350dfe2fba924e6eeb9536e1824430cd9cebac47a4afd0d2dd8d743e8a` |
| `repetition_finale_p4_v1.sh` | `b84198ccd191f7bcd7010bc1671aa035b43e40145e3a997d65df34a0a06a5592` |
| `repetition_jouet_p4_v1.sh` | `e445bb7049b12ec5b8b66d81b407e2ec3c8a594357dda3181ac51cd17914842e` |
| `sceller_p4_v1.sh` | `42333dedc5f28e5ab01a752ae8bf97e2d8a3c01be70b9d9338403cc007b6acb5` |
| `surveiller_p4_v1.sh` | `72194ccfc7d9d3032c55a433bd917bfc4cf7404d6c034e45b8843c1a4bcc21ef` |
| `verifications_p4_v1.py` | `8a7aefee6907ee008979e759e1227ab1663edf8080f6f60d22e8b75d841b041d` |

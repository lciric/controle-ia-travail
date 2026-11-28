# Notes de la chaîne v3 de P4-instrument — v1

Correcteur neuf de la chaîne v3 : il n'a écrit ni la chaîne v1 ou v2, ni le module, ni aucune relecture ou vérification.
Session 16, du 2026-10-20 vers 23:30 UTC au 2026-10-21 vers 01:25 UTC.
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument` (lien vers le
bloc-notes restauré ; les journaux bruts citent parfois sa cible, `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/bloc-notes-session14/p4-instrument`).

## 1. Ce qui est livré

- `…/chaine-v3/` : copie des vingt et un scripts de `…/chaine-v2/` (la v2 reste intacte ; empreintes de départ :
  `…/chaine-v3-travail/empreintes-chaine-v2-de-depart.txt`), mêmes noms, à verser sous `docs/procedures/P4-instrument-v1/`.
  Dix-huit scripts changent, trois sont inchangés (`amorce_instance_p4_v1.sh`, `p4_instance_v1.sh`,
  `controle_cinq_minutes_p4_v1.sh`). Liste CHAINE inchangée (vingt et un scripts).
- Huit journaux de preuve, sorties brutes des sept bancs et de la répétition jouet, redirigées chacune dans un fichier
  neuf de `…/chaine-v3/` (section 7). `verifications_p4_v1.py preuves` (sept journaux des bancs) et
  `verifications_p4_v1.py repetition` : code 0.
- `paires-candidat2-chaine-v3-v1.json` (`f3b715233f7d2c26cbb3d017f90e9d5ce306c6f58a009b3130b5b788f803f575`) : onze paires exactes (ancien → nouveau) pour le
  candidat 1, tirées de celles de la chaîne v2 (section 5).
- Module de P4 : le module v3 (`…/module-v3/`, six fichiers lus, jamais modifiés ; 1 166 tests collectés au C d'essai).
- Dossier de travail, non versé : `…/chaine-v3-travail/` (C d'essai `c-essai-1` (passe préliminaire) et `c-essai-2`
  (passe finale), journaux de la passe préliminaire sous `passe-1/`, racines des bancs finaux sous `final/`, essais
  unitaires, essai d'assemblage du candidat 2 sous `assemblage/`, outils sous `outils/` et à la racine).

## 2. Décision → correction → cas → journal

Journaux : A = `banc-arret-p4-v1.log` ; S = `banc-surveillance-p4-v1.log` ; T = `banc-traces-p4-v1.log` ;
V = `banc-verifications-p4-v1.log` ; L = `banc-lanceur-p4-v1.log` ; C = `banc-controles-p4-v1.log` ;
E = `banc-scellement-p4-v1.log` ; R = `repetition-jouet-p4-v1.log`.

| décision du traitement | correction (script) | cas (sain et artefacts) | journal |
|---|---|---|---|
| VC2-depense-01 (majeur), correction (a), (b), (c) | `verifications_p4_v1.py`, `revocations_voisines` : la fonction `proposees` du banc `banc_voisines_v2.py` du vérificateur, à la lettre (première cellule reconnue sans `*`, `_`, `` ` `` ; registre des décisions : toutes les cellules `k[1:]` ; registre des GO : toute ligne, de tout type, dont une cellule commence par un début de révocation et nomme l'un des cinq identifiants ; type lu sans gras). Égale à `proposees` ligne à ligne sur les registres réels (essai unitaire, 0 écart). | V : X01 à X05 (code 2, lignes affichées), plus X06 (type en gras), X07 (identifiant de décision entre guillemets inversés), témoins V55 (mention libre = V10 du vérificateur), V58 (GO de calcul qui cite la phase = V12), X08 (GO de calcul qui mentionne un retrait sans identifiant : passe) ; registres réels relus à la tête de `main` par `git show` (R00, R00b : aucune fausse alerte) et dans l'arbre de travail (R00c : égaux) ; L : XL01 à XL05 (code 2, aucune création), témoin XL06 | V, L |
| VC2-depense-02 (mineur) | `arreter_p4_v1.sh` : étiquette comparée dans Python (`json.loads(…).get("label") == "p4-v1"`), l'étiquette autre écrite en JSON (saut de ligne visible) ; `surveiller_p4_v1.sh` : le programme qui lit l'état rend le code (0 seulement pour « p4-v1 » exactement), refus au départ sinon | A : A14 (« p4-v1\n » : code 2, aucune demande d'arrêt, aucune relecture), A15 (« P4-V1 »), A16 (« p4-v1 » suivi d'une espace), A17 (étiquette numérique) ; S : S15b (« p4-v1\n » : code 2, aucune demande d'arrêt, aucun dossier de sortie) | A, S |
| VC2-depense-03 (mineur) | `recuperation_p4_v1.sh` : `gardee` définie avant le contrôle de la place, appelée avant la sortie en code 2 de la place insuffisante et du clonage impossible (message neuf `REFUS_CLONE`) ; états de l'outil réduits aux lettres, chiffres, points, tirets et soulignés | R : RX01 = `artefact-place-disque` (son bloc porte maintenant l'état et l'heure limite) ; RX02 = `artefact-clonage-impossible` (copie dont seule l'adresse du dépôt distant change, vers un dépôt absent : code 2, état et heure limite) ; module commun : `DANS_LE_REFUS` exige l'état et l'heure limite dans ces deux blocs ; V : J29 à J31, J33 | R, V |
| VC2-depense-04 (mineur, forme) | `arreter_p4_v1.sh` : ligne prête à quatre cellules, la forme exacte de la correction du rapport : date et heure (AAAA-MM-JJ HH:MM) de l'arrêt relu ; « instance Vast.ai **ID** (P4-instrument, étiquette p4-v1 ; commande d'arrêt par l'identifiant entre guillemets inversés) » ; le motif ; « demandé à …, relu arrêté (exited, stopped) deux fois de suite à … (arreter_p4_v1.sh) » | A : A00 (forme exacte relue par une expression complète : quatre cellules, date et heure égales à celles de l'arrêt relu) | A |
| VC2-depense-05 (information), en phrase | `lancer_p4_v1.sh` : une ligne de plus dans `lancement.txt`, « code 2 du contrôle à cinq minutes ou de la surveillance après la création : `arreter_p4_v1.sh <id> <dossier neuf>` à la main, puis nœud », relue une fois avant de quitter le mode d'arrêt sur erreur ; aucune autre logique | L : P00 (ligne présente une fois) | L |
| VC2-depense-06, -07 (information) | rien (version suivante ; rien à faire) | — | — |
| VC2-depense-08 (information) | rien dans la chaîne (« dit au versement ») ; les journaux de la v3 citent la cible du lien du bloc-notes (section 6) | — | — |
| VC2-depense, « Texte à ajouter » 1 et 2 | paires 2 et 9 du JSON, blocs recopiés à l'identique (section 5) | essai d'assemblage, comparaison v2 → v3 | — |
| VC2-donnees-01 (mineur) | `recuperation_p4_v1.sh` : textes honnêtes lus au commit S (`git show "$S:$TEXTES_P3"` vers le dossier de travail, copie retirée à la fin) ; repli de l'affichage (module commun ou textes de S illisibles) : jetons masqués, puis de chaque ligne ses 40 premiers caractères, sa longueur et son empreinte courte ; KO 4f ; en plus (choix du correcteur, section 6), la ligne de l'instance gardée est réécrite entière hors du filtre | R : `artefact-repli-de-l-affichage` (copie de la récupération de l'artefact « motif d'arrêt qui recopie un texte » dont seul le chemin du module commun lu à S change) : code 1, KO 4f, chaque ligne filtrée réduite (la ligne « 4a arrêt » comprise), instance gardée réécrite, aucune destruction, puis recherche des fenêtres et des jetons dans toutes les sorties ; module commun : ligne `REPLI` exigée ; V : J32 | R, V |
| VC2-donnees-02 (mineur) | `verifications_p4_v1.py`, `fichiers_de` : toute entrée qui n'est pas un fichier ordinaire (lien symbolique vers un fichier ou un dossier, tube nommé, socket, périphérique ; lien donné en argument) n'est ni suivie ni lue, est comptée et refusée par `fenetres` et `jetons` (code 1, « non ordinaire … : chemin ») ; `controler_traces_p4_v1.sh` : compte des entrées non ordinaires, constats comptés une fois chacun | T : T09 (lien vers un fichier sain), T09b (lien vers un texte hors du dossier : rien n'est retrouvé, le lien est refusé), T09c (lien vers un dossier), T09d (tube nommé) ; V : F15 à F18, T03 (lien vers un jeton) | T, V |
| VC2-donnees-03, -05, -06, -07 (information) | rien (version suivante) ; -07 couvert par la lecture des textes à S | — | — |
| VC2-donnees-04 et -09 (information), phrases | paire 7 du JSON, phrases « Texte à ajouter » 2 et 4 du rapport « données », mot pour mot (section 5) | comparaison v2 → v3 | — |
| VC2-donnees-08 (information) | rien dans la chaîne : geste de session avant le lancement | — | — |
| Liste `RAPPORTS_NOMS` | `verifications_p4_v1.py` : vingt-six noms, dans l'ordre exact du traitement ; bancs : K00 (vingt-six lignes, dernière ligne triée), commentaires des bancs des contrôles et du scellement (ils lisent la liste dans le module commun) ; `outils_essais_p4_v1.py`, `RAPPORTS_CONNUS` : vingt-six noms et les empreintes des fichiers existants du bloc-notes (vingt-deux ; quatre « au versement ») | V : K00 à K05 ; C : rapports synthétiques aux vingt-six noms, A26, A26b, A27, Z1d, Z1e, Z1e2 ; E : S16, S28 | V, C, E |

## 3. Liste `RAPPORTS_NOMS` (vingt-six noms)

Dans l'ordre du traitement (`traitement-verifications-chaine-v2-P4-v1.md`, section « Liste RAPPORTS_NOMS ») ; empreinte
écrite par la paire 11 quand le fichier source du bloc-notes existe (égale à son sceau compagnon quand il en a un ;
`contre-lecture-R2-P4-instrument-brouillon1-v1.md` et `P4-instrument-v1-brouillon1.md` n'ont pas de sceau compagnon dans
le bloc-notes : empreintes égales à celles de la chaîne v2).

| n° | nom sous `prereg/contre-lectures/` | source du bloc-notes | sha256 (paire 11) |
|---|---|---|---|
| 1 | `contre-lecture-R2-P4-instrument-brouillon1-v1.md` | `…/contre-lecture-R2-P4-instrument-brouillon1-v1.md` | `108a8d1ffd0a892c123608af237c824e2bc40545d4e54e5e5b7dcb9a37835420` |
| 2 | `traitement-R2-P4-instrument-brouillon1-v1.md` | `…/traitement-R2-P4-instrument-brouillon1-v1.md` | `876d1a66c317ab662da1f63b1be76e764506fa3090da0eded7cee5ce2bcb253d` |
| 3 | `traitement-gemini-014-P4-instrument-v1.md` | `…/traitement-gemini-014-P4-instrument-v1.md` | `a61cfd3c21b02be67408e44d50548b3984737fe8fffd58a3d1d6a7e699ffbb36` |
| 4 | `verification-corrections-brouillons2-3-P4-v1.md` | `…/verification/verification-corrections-brouillons2-3-P4-v1.md` | `9c94c2205b3f08e522917fd7c078748f8dc583fe4242ed9a26c325af71e7228e` |
| 5 | `traitement-verification-P4-instrument-v1.md` | `…/traitement-verification-P4-instrument-v1.md` | `53e7c0f2e8e9867c42e603897a54bc4b895eaffc2b4d979c75379443f77228dd` |
| 6 | `contre-lecture-3-P4-instrument-candidat1-v1.md` | `…/contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md` | `7f947de00aa58b0635fe2b6f0ad3c22eb7dbcb48ed0c8079f65a57abb13b5368` |
| 7 | `relecture-chaine-depense-P4-instrument-v1.md` | `…/relecture-chaine-depense/relecture-chaine-depense-v1.md` | `b6e43dd7a981d3dabc214127787ea245f976731763963d8d31a59543794f3c5b` |
| 8 | `relecture-chaine-donnees-P4-instrument-v1.md` | `…/relecture-chaine-donnees/relecture-chaine-donnees-v1.md` | `184b8926fe320f25f31014291fead8cd29b72efed5bd107ee97eacac5d9e7733` |
| 9 | `relecture-chaine-fidelite-P4-instrument-v1.md` | `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md` | `923c71d87115cf114d16c8079adce4dd79aa3ca112bcf9224ad6b9088cb988c5` |
| 10 | `traitement-CL3-et-relectures-chaine-P4-v1.md` | `…/traitement-CL3-et-relectures-chaine-P4-v1.md` | `4678a01b07bd8885169b8a77ac12381ab21763632bed48758da94a00f001b5d8` |
| 11 | `verification-module-v2-contournement-P4-instrument-v1.md` | `…/verification-module-v2-contournement/verification-module-v2-contournement-v1.md` | `2ce3d0af0a36fbb076d494b59619f4f11ed03fb9172f05e3bdde3087500a335d` |
| 12 | `verification-module-v2-fidelite-P4-instrument-v1.md` | `…/verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md` | `ea12d4a2ea780e50e465105c29fb53fbe1e6eace5e3bae1ee177ed17426e7196` |
| 13 | `traitement-verifications-module-v2-P4-v1.md` | `…/traitement-verifications-module-v2-P4-v1.md` | `32d50abec952df70bd53980f28b93a5483e10c0c0f71d33a54a3006f5b2ba4b4` |
| 14 | `verification-module-v3-P4-instrument-v1.md` | `…/verification-module-v3/verification-module-v3-v1.md` | `86577f3d6d5b2c9edf7d893a041ebcd11d8322f2645c3337a545dfa5a881038f` |
| 15 | `verification-chaine-v2-depense-P4-instrument-v1.md` | `…/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md` | `488a7e717e6b2e96e28dca0c79ef062738e79defc9c08e4a0b4507119602a00a` |
| 16 | `verification-chaine-v2-donnees-P4-instrument-v1.md` | `…/verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md` | `16298dd2676e512bcfbca0b0c35d74312f87c2dae3a436e53ce40657dfb64b08` |
| 17 | `verification-chaine-v2-fidelite-P4-instrument-v1.md` | à venir | `<empreinte au versement>` |
| 18 | `traitement-verifications-chaine-v2-P4-v1.md` | `…/traitement-verifications-chaine-v2-P4-v1.md` | `10664a97505a49aa2b404e7500b6800466a222ed942815bc370cef79a7c90c6e` |
| 19 | `verification-chaine-v3-P4-instrument-v1.md` | à venir | `<empreinte au versement>` |
| 20 | `verification-candidat2-P4-instrument-v1.md` | à venir | `<empreinte au versement>` |
| 21 | `P4-instrument-v1-brouillon1.md` | `…/P4-instrument-v1-brouillon1.md` | `41e5f035616e7cd3a233b680af06ba2a97c517a41d92f2042fde746aa85a48fd` |
| 22 | `P4-instrument-v1-brouillon2.md` | `…/P4-instrument-v1-brouillon2.md` | `ab409206c90dd489cb4efcd032d2c81d6eeadc459f28fb8d6cedcdb94f25ff63` |
| 23 | `P4-instrument-v1-brouillon3.md` | `…/P4-instrument-v1-brouillon3.md` | `2ec30d6860838f5b9e9c2e637906101a8b0d2ad2a1df2cfdc355bf552374cd4c` |
| 24 | `P4-instrument-v1-brouillon4.md` | `…/P4-instrument-v1-brouillon4.md` | `32d821fb42e54341f2649637085de18e2b6b9758b51dc38c504f702ba393ead6` |
| 25 | `P4-instrument-v1-candidat1.md` | `…/P4-instrument-v1-candidat1.md` | `6422fb45a1dc2a3b42a5f6adad4ed8ff02cf89b3c09d91474213c5c1f5fe3bc0` |
| 26 | `P4-instrument-v1-candidat2.md` | à venir | `<empreinte au versement>` |

## 4. Ce que la session doit savoir avant le versement

- Les quatre pièces à venir (17, 19, 20, 26) gardent « `<empreinte au versement>` » dans la paire 11 : le texte final doit
  porter leurs empreintes ; un nom de plus (traitement de la vérification « fidélité », chaîne v4) change l'empreinte du
  module commun, donc les bancs et la répétition à rejouer.
- Le banc des contrôles a une option de `tokenizer.json` de substitution, explicite et annoncée (section 6, CV3-02) ;
  la passe finale a joué le vrai tokeniseur de la session, revenu au bloc-notes le 2026-10-21 à 00:06 UTC (empreinte
  vérifiée). Sur le vrai C, jouer le banc sans la variable.

## 5. Phrases du texte (paires de la chaîne v3)

Fichier : `paires-candidat2-chaine-v3-v1.json` (`f3b715233f7d2c26cbb3d017f90e9d5ce306c6f58a009b3130b5b788f803f575`), produit par
`outils_essais_p4_v1.py paires-v3` (la commande `paires-v2` est retirée : ses phrases n'étaient plus celles du code).
Mêmes onze ancres que la chaîne v2 ; les paires 1, 3, 4, 6, 8 et 10 sont identiques à celles de
`…/chaine-v2/paires-candidat2-chaine-v2-v1.json` (ancien, nouveau et source) ; cinq changent :

| paire | clé | changement | source |
|---|---|---|---|
| 2 | revocation-voisine | parenthèse remplacée par le bloc « Texte à ajouter » 1 du rapport « dépense », recopié à l'identique, sauts de ligne compris (l'espace qui le précède devient un saut de ligne et l'indentation de quatre espaces du texte) | VC2-depense-01 |
| 5 | liste-d-arret | ajout : « Contrôle à cinq minutes ou surveillance refusés en code 2 après la création : rien n'est arrêté d'office ; la session arrête l'instance à la main par son identifiant (`arreter_p4_v1.sh <identifiant> <dossier neuf>`, consigne écrite dans `lancement.txt`), puis nœud de Lazar. » ; « Récupération en échec » précisé « (code 1, ou refus en code 2 faute de place disque ou de clonage) » | VC2-depense-05, -03 |
| 7 | paragraphes | « Texte à ajouter » 1, 2, 3, 4 du rapport « données », mot pour mot (à espaces près : le rapport les cite sur une ligne), plus une phrase du correcteur : « La ligne de l'instance gardée (identifiant, état, heure limite de destruction), de forme fixe, est alors réécrite entière, hors du filtre. » | VC2-donnees-01, -02, -04, -09 |
| 9 | precision-5 | segment remplacé par le bloc « Texte à ajouter » 2 du rapport « dépense », à l'identique (même règle de saut de ligne) | VC2-depense-01 |
| 11 | rapports attendus | vingt-six rapports, dans l'ordre de `RAPPORTS_NOMS` | liste du traitement |

Contrôles (`…/chaine-v3-travail/outils/comparer_paires_v2_v3_v1.py`, sortie
`…/chaine-v3-travail/assemblage/comparaison-paires-v2-v3-2.txt`) : mêmes ancres, paires inchangées égales, deux blocs du
rapport « dépense » à l'identique, quatre phrases du rapport « données » à espaces près, ancien « jamais dans l'arbre
contrôlé. » remplacé : conformes. (La première sortie, `comparaison-paires-v2-v3.txt`, montre un écart de l'outil, pas des
paires : il prenait pour des phrases les citations d'ancres ; corrigé avant la seconde sortie.)

Essai d'assemblage (`…/chaine-v3-travail/outils/essayer_assemblage_v1.py`, sortie
`…/chaine-v3-travail/assemblage/final/sortie-assemblage.json`) : `…/ecrire_candidat2_v1.py` joué avec les sept paires du
module v3 (`…/verification-module-v3/travail/paires-texte-module-v3-corrigees-vm3-v2.json`, `324c164f…`) et les onze de la
chaîne v3, dans les deux ordres : code 0 et même texte (`79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73`, pas un candidat) ; `problemes` = [] ; table
« Critères de lecture gelés » égale à celle du module v3 ; six lignes « Module de P4 » aux empreintes du module v3 ;
« Tests attendus : `1166` » une fois ; chaque « nouveau » de la chaîne présent une fois. Aucune collision.

## 6. Écarts, défauts trouvés et réserves

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

## 7. Journaux de preuve

C d'essai final : `…/chaine-v3-travail/c-essai-2/depot`, commit `3521ff75c316c9f31403486fc6ca84a1c29daeca` (clone partagé du dépôt de travail à
`0a44ee6139b14887fc38da8db429a46d41b300d4`, sans les PDF ; module v3 et chaîne v3 versés ; 1 166 tests collectés). Candidat 2 d'essai :
`…/chaine-v3-travail/c-essai-2/travail/P4-instrument-v1-candidat2-essai.md` (`79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73`).

| journal | sha256 | lignes « CONFORME » (v2) | dernière ligne |
|---|---|---|---|
| `banc-arret-p4-v1.log` | `559a20608d71fd15f542e281d80ee70c210d72349bf7891272998a9a8dc08f89` | 26 (21) | FIN DU BANC DE L'ARRÊT DE P4 ; cas non conformes : 0 |
| `banc-surveillance-p4-v1.log` | `e72391899145dfb6384adee24d1c9c0cc2ef66f5f5cb8704c6afde1302e49e09` | 96 (93) | FIN DU BANC DE LA SURVEILLANCE DE P4 ; cas non conformes : 0 |
| `banc-traces-p4-v1.log` | `fe6d6d704587e0dabd363d927ec649592da6bfe232ff7f599d5e8c1e33f3cbe8` | 30 (21) | FIN DU BANC DU CONTRÔLE DES TRACES DE P4 ; cas non conformes : 0 |
| `banc-verifications-p4-v1.log` | `b710e63340c9afce389295d42d5b2a34006171113b9c7f5b695d5054e790140f` | 205 (182) | FIN DU BANC DES VÉRIFICATIONS DE P4 ; cas non conformes : 0 |
| `banc-lanceur-p4-v1.log` | `97c22ec96ddf7a0b33e7b7c318c723fa513892581078577329e91d1fdf32088e` | 131 (125) | FIN DU BANC DU LANCEUR DE P4 ; cas non conformes : 0 |
| `banc-controles-p4-v1.log` | `72e0eae853eea63065bd4227afc456c5e47d0943b93892633d325858b7afae3d` | 86 (86) | FIN DU BANC DES CONTRÔLES DE P4 ; cas non conformes : 0 |
| `banc-scellement-p4-v1.log` | `615fbe97d804dae5b9d37f5c932a236c5e8139da1cc341ca7d5d92a8812bf99a` | 64 (64) | FIN DU BANC DU SCELLEMENT DE P4 ; cas non conformes : 0 |
| `repetition-jouet-p4-v1.log` | `5a0ee9350dfe2fba924e6eeb9536e1824430cd9cebac47a4afd0d2dd8d743e8a` | — (répétition) | FIN DE LA RÉPÉTITION |

`verifications_p4_v1.py preuves …/chaine-v3` (sept journaux des bancs) : code 0 ; sortie :

```
arreter_p4_v1.sh 53c234e4c1004a56ca1884dcbf4cb8d195c02f3798ba6617fc70053983025806
controle_cinq_minutes_p4_v1.sh c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6
controler_traces_p4_v1.sh 4954f425daa66e9c2464f561fe7190b22ec2ff51b8d037933f214ce1627cd068
controles_avant_depense_p4_v1.sh c16ba4383ea454c51cffdde330edfcb744021b4c6765a59a09efe57450ba2b48
essais_arret_p4_v1.sh 6b276973eea142c4d4cf62dcca1adb0bb4deaf3f8bbc3088fbcc056e2699c465
essais_controles_p4_v1.sh 4a2a155e1644409c413e70d9a2368456a2890c7e3dc4ca9107a590c959cad650
essais_lanceur_p4_v1.sh ce8e0e0c744dbaebe7823ca1958fa8ce4f6522fbfdc49389a2412b9afecc45be
essais_scellement_p4_v1.sh 2be5a9e2463427c0ac2fd035d1add6d6a5d2e85f9a56b1d4e84b89725ea702b6
essais_surveillance_p4_v1.sh 2c3539877585811b001bba4c2f1a84593764144af95edf9dad72f5fb20fa4770
essais_traces_p4_v1.sh 9afd19a80d3e8aa0e920a20e8420830aec410ba4006955b3422f986440b75196
essais_verifications_p4_v1.sh f46cf8bfa3dd3c95cc300697b00de91dec602d4cfa66e6931b134b93770de186
lancer_p4_v1.sh fedd228bd629c741c70601c9c747566ceb4993f30cbcd510f9c1e6341bb64051
outils_essais_p4_v1.py c5719362b9ac068860ef7a862e7d85456f8715624e447666a7210fc4ea257f34
sceller_p4_v1.sh 42333dedc5f28e5ab01a752ae8bf97e2d8a3c01be70b9d9338403cc007b6acb5
surveiller_p4_v1.sh 72194ccfc7d9d3032c55a433bd917bfc4cf7404d6c034e45b8843c1a4bcc21ef
verifications_p4_v1.py 8a7aefee6907ee008979e759e1227ab1663edf8080f6f60d22e8b75d841b041d
```

`verifications_p4_v1.py repetition 3521ff75c316c9f31403486fc6ca84a1c29daeca …/chaine-v3/repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md 79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73` : code 0 ; sortie :

```
outils_essais_p4_v1.py c5719362b9ac068860ef7a862e7d85456f8715624e447666a7210fc4ea257f34
recuperation_p4_v1.sh 51e670b33a7fa713c5d47c57ab9bf1a831479a68c714faabf601d9c4720b8157
repetition_jouet_p4_v1.sh e445bb7049b12ec5b8b66d81b407e2ec3c8a594357dda3181ac51cd17914842e
verifications_p4_v1.py 8a7aefee6907ee008979e759e1227ab1663edf8080f6f60d22e8b75d841b041d
```

Empreintes citées par les journaux comparées aux scripts de la chaîne v3 : oui, 18 scripts.

## 8. Empreintes (sha256)

| script | sha256 (v3) | v2 |
|---|---|---|
| `amorce_instance_p4_v1.sh` | `21b3f447080353741c15d4948e557235dab17201a8d70f4545d1d9f1913c608d` | inchangé |
| `arreter_p4_v1.sh` | `53c234e4c1004a56ca1884dcbf4cb8d195c02f3798ba6617fc70053983025806` | changé (`825701e2847d…`) |
| `controle_cinq_minutes_p4_v1.sh` | `c3a63049480f3a526bb53edec6b04f72a532014b2811d5a696280922047af5e6` | inchangé |
| `controler_traces_p4_v1.sh` | `4954f425daa66e9c2464f561fe7190b22ec2ff51b8d037933f214ce1627cd068` | changé (`f2fe40f2c929…`) |
| `controles_avant_depense_p4_v1.sh` | `c16ba4383ea454c51cffdde330edfcb744021b4c6765a59a09efe57450ba2b48` | changé (`c44bd6893c3b…`) |
| `essais_arret_p4_v1.sh` | `6b276973eea142c4d4cf62dcca1adb0bb4deaf3f8bbc3088fbcc056e2699c465` | changé (`d8e4e554c817…`) |
| `essais_controles_p4_v1.sh` | `4a2a155e1644409c413e70d9a2368456a2890c7e3dc4ca9107a590c959cad650` | changé (`e348e7eec67b…`) |
| `essais_lanceur_p4_v1.sh` | `ce8e0e0c744dbaebe7823ca1958fa8ce4f6522fbfdc49389a2412b9afecc45be` | changé (`1c80fe4b45dc…`) |
| `essais_scellement_p4_v1.sh` | `2be5a9e2463427c0ac2fd035d1add6d6a5d2e85f9a56b1d4e84b89725ea702b6` | changé (`f68d709117da…`) |
| `essais_surveillance_p4_v1.sh` | `2c3539877585811b001bba4c2f1a84593764144af95edf9dad72f5fb20fa4770` | changé (`2f51d42dad9a…`) |
| `essais_traces_p4_v1.sh` | `9afd19a80d3e8aa0e920a20e8420830aec410ba4006955b3422f986440b75196` | changé (`12cb9a0de459…`) |
| `essais_verifications_p4_v1.sh` | `f46cf8bfa3dd3c95cc300697b00de91dec602d4cfa66e6931b134b93770de186` | changé (`d8ab8510be47…`) |
| `lancer_p4_v1.sh` | `fedd228bd629c741c70601c9c747566ceb4993f30cbcd510f9c1e6341bb64051` | changé (`0d2099335ebc…`) |
| `outils_essais_p4_v1.py` | `c5719362b9ac068860ef7a862e7d85456f8715624e447666a7210fc4ea257f34` | changé (`9f26389bb486…`) |
| `p4_instance_v1.sh` | `8801864fd9f2d940ed7ce2eed43c4efac8251484d37c1dcf3d3bea9bf0d8f967` | inchangé |
| `recuperation_p4_v1.sh` | `51e670b33a7fa713c5d47c57ab9bf1a831479a68c714faabf601d9c4720b8157` | changé (`65477c6d5d11…`) |
| `repetition_finale_p4_v1.sh` | `b84198ccd191f7bcd7010bc1671aa035b43e40145e3a997d65df34a0a06a5592` | changé (`94bb9dcab763…`) |
| `repetition_jouet_p4_v1.sh` | `e445bb7049b12ec5b8b66d81b407e2ec3c8a594357dda3181ac51cd17914842e` | changé (`b6cdba621268…`) |
| `sceller_p4_v1.sh` | `42333dedc5f28e5ab01a752ae8bf97e2d8a3c01be70b9d9338403cc007b6acb5` | changé (`afd15b53233f…`) |
| `surveiller_p4_v1.sh` | `72194ccfc7d9d3032c55a433bd917bfc4cf7404d6c034e45b8843c1a4bcc21ef` | changé (`315ddd7d6141…`) |
| `verifications_p4_v1.py` | `8a7aefee6907ee008979e759e1227ab1663edf8080f6f60d22e8b75d841b041d` | changé (`cdb6b90a34ea…`) |

## 9. Rejouer

En chemins absolus ; `H=…/chaine-v3`, `W=…/chaine-v3-travail`, `CE=$W/c-essai-2/depot`, `C=3521ff75c316c9f31403486fc6ca84a1c29daeca` ; Python de la
session, `PYTHONDONTWRITEBYTECODE=1`, `GIT_OPTIONAL_LOCKS=0` ; un même jour UTC pour le banc du lanceur (son accord
d'essai est daté du jour) :

- `bash $H/essais_arret_p4_v1.sh RACINE_NEUVE` ; idem `essais_surveillance`, `essais_traces` ;
- `bash $H/essais_verifications_p4_v1.sh $CE $C RACINE_NEUVE` ; idem `essais_lanceur`, `essais_scellement` ;
  `bash $H/essais_controles_p4_v1.sh $CE $C RACINE_NEUVE` (la passe finale a posé `BANC_TOKENISEUR_SUBSTITUT=1`, sans
  effet : la copie de la session était là) ;
- `bash $H/repetition_jouet_p4_v1.sh $C $W/c-essai-2/travail/P4-instrument-v1-candidat2-essai.md RACINE_NEUVE $CE` ;
- `python -B $H/verifications_p4_v1.py preuves $H banc-lanceur-p4-v1.log banc-surveillance-p4-v1.log
  banc-arret-p4-v1.log banc-traces-p4-v1.log banc-verifications-p4-v1.log banc-controles-p4-v1.log
  banc-scellement-p4-v1.log` ;
- `python -B $H/verifications_p4_v1.py repetition $C $H/repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md
  79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73`.

# Notes de la chaîne v3 de P4-instrument — v1

Correcteur neuf de la chaîne v3 : il n'a écrit ni la chaîne v1 ou v2, ni le module, ni aucune relecture ou vérification.
Session 16, du 2026-10-20 vers 23:30 UTC au 2026-10-21 vers {FIN} UTC.
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
- `paires-candidat2-chaine-v3-v1.json` (`{SHA_PAIRES}`) : onze paires exactes (ancien → nouveau) pour le
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

{TABLE_RAPPORTS}

## 4. Ce que la session doit savoir avant le versement

- Les quatre pièces à venir (17, 19, 20, 26) gardent « `<empreinte au versement>` » dans la paire 11 : le texte final doit
  porter leurs empreintes ; un nom de plus (traitement de la vérification « fidélité », chaîne v4) change l'empreinte du
  module commun, donc les bancs et la répétition à rejouer.
- Le banc des contrôles a une option de `tokenizer.json` de substitution, explicite et annoncée (section 6, CV3-02) ;
  la passe finale a joué le vrai tokeniseur de la session, revenu au bloc-notes le 2026-10-21 à 00:06 UTC (empreinte
  vérifiée). Sur le vrai C, jouer le banc sans la variable.

## 5. Phrases du texte (paires de la chaîne v3)

Fichier : `paires-candidat2-chaine-v3-v1.json` (`{SHA_PAIRES}`), produit par
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
chaîne v3, dans les deux ordres : code 0 et même texte (`{SHA_CANDIDAT}`, pas un candidat) ; `problemes` = [] ; table
« Critères de lecture gelés » égale à celle du module v3 ; six lignes « Module de P4 » aux empreintes du module v3 ;
« Tests attendus : `1166` » une fois ; chaque « nouveau » de la chaîne présent une fois. Aucune collision.

## 6. Écarts, défauts trouvés et réserves

{CONSTATS}

## 7. Journaux de preuve

C d'essai final : `…/chaine-v3-travail/c-essai-2/depot`, commit `{C}` (clone partagé du dépôt de travail à
`{TETE}`, sans les PDF ; module v3 et chaîne v3 versés ; 1 166 tests collectés). Candidat 2 d'essai :
`…/chaine-v3-travail/c-essai-2/travail/P4-instrument-v1-candidat2-essai.md` (`{SHA_CANDIDAT}`).

{TABLE_JOURNAUX}

`verifications_p4_v1.py preuves …/chaine-v3` (sept journaux des bancs) : code 0 ; sortie :

```
{PREUVES}
```

`verifications_p4_v1.py repetition {C} …/chaine-v3/repetition-jouet-p4-v1.log P4-instrument-v1-candidat2-essai.md {SHA_CANDIDAT}` : code 0 ; sortie :

```
{REPETITION}
```

Empreintes citées par les journaux comparées aux scripts de la chaîne v3 : {EGALITE}.

## 8. Empreintes (sha256)

{TABLE_SCRIPTS}

## 9. Rejouer

En chemins absolus ; `H=…/chaine-v3`, `W=…/chaine-v3-travail`, `CE=$W/c-essai-2/depot`, `C={C}` ; Python de la
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
  {SHA_CANDIDAT}`.

# Contre-lecture 2 (R2) — brouillon `pilote2-gemini-organisme-v5-1-v2.md` et lanceur v3

- Date et heure (temps universel, `date -u`) : 2026-10-25, lecture de 10:18:21 à 10:38:11.
- Fichier relu : `essaim-m3-refonte-v1/prereg/pilote2-gemini-organisme-v5-1-v2.md`, sha256 `0d718031733e4f27bb8593e8dab773acf175e7a7a909dd3b655a217a901b9241` (recalculé, égal au compagnon).
- Lanceur relu : `prereg/pieces-pilote2-gemini-v5-1/lancer_pilote2_gemini_v5_1_v3.sh`, sha256 `bd1e0a2b2c2f2d298a8904c81b798e5a112d4c7d5fd549834e237048b3bcda53` (recalculé ; égal au compagnon, au texte et aux deux `LANCEMENT-simulation-*-v3.md`).
- Contre-lecteur : sous-agent neuf (claude-opus-5-5), auteur d'aucune pièce ni de la contre-lecture 1 ; aucun score lu, aucun fichier interdit ouvert ; ni git, ni réseau, ni appel de modèle (un essai bash local de cinq lignes).
- **Verdict : scellable après corrections** — constats nouveaux : 1 majeur, 4 mineurs, 5 de forme.

## Traitement des 14 constats

| constat | état | où (texte v2 ; lanceur v3 ; code) |
|---|---|---|
| P2C1-01 | en partie | liste close l. 42-51, 236, 382 ; étape (0) l. 156-190. Noms et valeurs vérifiés : `statut` = code d'exécution (boucle.py l. 737 ; 663, 668, 674), `invalide`, `anomalie_noyau` (l. 741-742 ; archive.py l. 132-135), `generations_invalidees` (l. 921), `fin` (l. 766-767, 810-814), arrêts `etape="arret"` / `raison` (l. 876-885, 832-837), tous copiés par l'extrait (extrait_mecanique.py l. 43-48, 59-61, 254). Crédit, modèle, anomalie, `STOP`, exception, archive incomplète, génération manquante bloquent. Restent P2C2-01 à 03 ; la liaison « ligne de M portant l'empreinte d'`EMPREINTES-pilote-v1.txt` de S » n'est pas faite (l. 51, non vérifiée). |
| P2C1-02 | traité | l. 118-127, 157-159, 302-305 ; principal.py l. 544, 587, 659, 692, 1351-1362, 1381-1382 ; mitose_spectrale.py l. 73, 115. |
| P2C1-03 | traité | l. 129-136 ; moisson.py l. 40-41, 181. |
| P2C1-04 | en partie | l. 182-191 ; lanceur l. 285-333, 388-393 ; `heure_utc` facultative, aucun identifiant de requête (dit) ; P2C2-10. |
| P2C1-05 | traité | l. 191-197 ; lanceur l. 440. |
| P2C1-06 | en partie | l. 143-156 ; lanceur l. 69-96, 228-239, 394 ; P2C2-04. |
| P2C1-07 | traité | l. 288-320 ; chemin du journal conforme (boucle.py l. 592-596, appels.py l. 132). |
| P2C1-08 | traité | l. 312-316 ; P2C2-08. |
| P2C1-09 | traité | recalculé : 18,38 / 31,16 / 43,94 dollars ; 4 086 ; 4 409 et 4 187 ; 123 appels. |
| P2C1-10 | traité | l. 392, 394, 401 ; `PART_TEMPS_APPELS` (principal.py l. 34). |
| P2C1-11 | traité | l. 347-348, 424-453 ; P2C2-07. |
| P2C1-12 | traité | lanceur l. 438, 468, 488 ; texte l. 283-288. |
| P2C1-13 | en partie | (i) l. 76-78 ; (ii) lanceur l. 216-224 ; (iii) l. 204-209 ; (iv) l. 465, 474 ; (v) l. 340, 411 ; (vi) l. 249-252 ; P2C2-09. |
| P2C1-14 | traité | l. 138 ; liste l. 324-331 = expression l. 499. |

Vérifié aussi : 28 essais cités (texte = lanceur, chacun présent une fois), 140 = 123 + 17 ; empreintes des pièces ; journal 81 sur 81.

## Constats nouveaux

**P2C2-01 — majeur — l'étape (0) accepte une S de simulation.** Lanceur l. 162-188 ; texte l. 42-51. Rien ne lit le mode de S : ni l'en-tête « (simulation, tentative 1) » de son `LANCEMENT.md` (l. 143), ni `manifeste.reel` (boucle.py l. 271), copié dans l'extrait (extrait_mecanique.py l. 219) ; `S_PILOTE` n'est pas tenu sous `$RACINE_PILOTES`. Le cas `sain-M` du journal (l. 3) est justement une S simulée déclarée « saine » : en réel, un `S_PILOTE` resté sur une répétition lance M sans S réelle, alors que « S non partie » bloque (l. 50). Correction : en réel, exiger l'en-tête `(reel, tentative N)` et le nom `pilote2-gemini-v5-1-structure-v1(-tentativeN)?`, `manifeste.reel` vrai, `manifeste.go_id` = `GO-2026-10-25-01`, `manifeste.entropie_seed_sequence` = graine S du texte, `LANCEMENT.md` et l'extrait listés dans les empreintes ; faire la liaison demandée par P2C1-01 (ligne de dépense de M, lue sur `origin/main`, portant l'empreinte d'`EMPREINTES-pilote-v1.txt` de S) ; artefact « S simulée ».

**P2C2-02 — mineur — plafonds : texte et garde divergent.** Texte l. 48, 393 ; lanceur l. 184-185 ; essai l. 133-134. boucle.py l. 874-886 n'écrit « plafond total atteint » que si une lignée est encore active : avec 2 × 30 = 60, ce plafond ne peut être atteint qu'à la fin de g1, où l'arrêt s'écrit « aucune lignée active » ; un plafond de génération (refus `plafond_usd`, serveur.py l. 198, dans `refus_noyau`) n'est lu par rien. Une S dont les deux générations butent sur 30 dollars est « saine », contre l. 393 (« M ne part pas ») ; `m-plafond-total` fabrique un événement impossible ici. Correction : lire `refus_noyau` (`plafond_usd`, `arret_noyau`) et `rapport.depense_totale_usd`, refuser, artefact réaliste ; ou écrire que les plafonds ne bloquent pas M (l. 48, 393).

**P2C2-03 — mineur — espace du manifeste autre que l'espace attendu.** Texte l. 403 (« M ne part pas ») ; lanceur l. 466, 475 : la réserve est écrite, la ligne « archive fermée : ferme.tar.gz ( » aussi, l'étape (0) ne cherche pas la réserve : M part ; l'essai `espace-autre` ne passe pas par M. Correction : refuser sur « ≠ espace attendu » au `LANCEMENT.md` de S (artefact), ou corriger l. 403.

**P2C2-04 — mineur — décalages des essais incomplets.** Lanceur l. 69 ; texte l. 152-154. test_noyau.py fait tourner des processus sous 60700/60701 hors bac à sable (`_comme`, l. 2798-2801, 2887-2895), 60800/60801 (l. 2931), 60810-60830 (l. 3204, 3236-3237, 3343), 60900 (l. 2964), 60000 et suivants. Une voisine au décalage 700 partage des utilisateurs pendant les essais, sans réserve. Correction : `DECALAGES_DES_ESSAIS="0 700 800"` (900 déjà refusé) ; texte « 0, 700, 800 et 900 ».

**P2C2-05 — mineur — pousser S avant M fait refuser M.** Lanceur l. 122, 160-161, 204-205 ; texte l. 93-98, 196-197, 331. Fichiers de S committés dans la copie de lancement : `git diff --name-only 5d1d4fd HEAD` contient `essaim-m3-refonte-v1/pilotes/…`, hors de `PERMIS_APRES_CODE` → refus ; revenir à la branche de lancement retire de l'arbre les fichiers suivis de S → « empreintes de S absentes ». Une ligne ajoutée au `LANCEMENT.md` de S (rapprochement de la console) casse aussi les empreintes. Le fichier d'empreintes du scellement doit être sous `pieces-pilote2-gemini-v5-1/`, sinon refus. Correction : écrire la procédure (S poussée depuis un arbre de travail séparé ou après M ; rapprochement hors du dossier de S ; chemin du fichier d'empreintes).

**P2C2-06 — forme — R3 non atomique.** Lanceur l. 125-131 : manifestes contrôlés au début seulement ; deux appels simultanés (tentatives 1 et 2) passent, la détection l. 394 ne voit l'autre noyau qu'une fois parti ; une course faite dans une autre copie n'est pas vue. Correction : verrou `mkdir "$RACINE_PILOTES/.verrou-$NOM"`, boucle R3 refaite en (vii bis), refus si `origin/pilotes/$NOM` existe.

**P2C2-07 — forme — nombres.** « 12 artefacts `m-…` » (l. 382, 469) : le journal en a 14 (l. 6-19), le texte en nomme 14 (l. 431-434). « 10:12–10:20 » (l. 424) : journal écrit pour la dernière fois à 10:17:20, texte à 10:17:39. Script du devis : « Usage : …_v1.py », « 3 extraits » (2 au code).

**P2C2-08 — forme — P2C1-08.** L. 313 « v8 ou suivante, écrit et scellé par session-depot » contre l. 314 « v8 de la confrontation (écrit par conv-audit) » : un document ou deux, quel auteur, quel chemin ?

**P2C2-09 — forme — intégrité.** (a) Versions lues sous `-I` (l. 216-222), sans le site utilisateur, alors que le noyau tourne sans `-I` : refus « anthropic absente » si installée par `pip --user`, ou version consignée autre que la chargée. (b) Le `.gitignore` d'`essaim-m3-refonte-v1` ignore `*.pyc` : un module sans source (`json.pyc`) à la racine échappe à `git status` (l. 207) ; ajouter `--ignored`. (c) `${S_PILOTE:?}` (l. 158) quitte sans la trappe d'erreur (essayé : code 1, rien consigné) : utiliser `refus`.

**P2C2-10 — forme — test de dépense.** La pièce peut changer entre (v) et (vii bis) : copie et empreinte consignées (l. 329-330) restent les premières ; reconsigner l'empreinte en (vii bis), refuser si elle diffère. Une `heure_utc` sans fuseau est lue à l'heure locale (l. 313) : exiger `Z` ; exiger `heure_utc` en réel.

## Réponses

- Étape (0) : champs et valeurs existent sous ces noms ; passent à tort la S simulée (01), le plafond (02), l'espace autre (03). À l'inverse, une S saine est bloquée si g1 n'écrit pas de successeur valide (boucle.py l. 811-814 ; conforme à la définition, à nommer l. 48-50) et par P2C2-05. Les 14 essais `m-…` couvrent chaque champ en altérant l'extrait, non par le noyau ; manquent S simulée, espace autre, plafond de génération, `S_PILOTE` non défini.
- Graines, retrait (égalité stricte), dépôt (`pwd -P`), `dossiers_a_cacher` (mêmes gardes et même variable qu'à l'exécution, bac_a_sable.py l. 212-236, 323-334) : justes, sans effet de bord ni lecture de la course ; aucune fuite de score trouvée.
- Devis et journal : conformes sauf P2C2-07.

# Contre-lecture des pièces de relance de l'étape A de T0.7 (ordre version 2, addendum brouillon 2, consigne, outil du remplacement) — v1

- **Lecteur** : sous-agent neuf, modèle B (lecteur) ≠ modèle A (auteur des pièces) ; n'a écrit ni l'addendum, ni l'ordre, ni la consigne, ni l'outil, ni ses essais, ni le correctif, ni la contre-lecture R-2602.
- **Heures (UTC, `date -u`)** : de 2026-11-13T23:13:10Z à 2026-11-13T23:26:14Z.
- **Objet** : `main` au commit `68de6386001b10b9de4235199718cb45122154ac` (R-2612). Arbre de travail temporaire (`git worktree`, tête détachée, sous le dossier temporaire de la session), retiré à la fin par son chemin exact, avec six dossiers et trois fichiers temporaires. Rien commité, rien poussé, aucune instance, aucune dépense, aucune clé lue ; un seul appel au dépôt distant, en lecture (`git ls-remote` de la branche de sortie).
- **Non ouvert** : le texte scellé de T0.7 ; aucun fichier interdit par la consigne ; sous `docs/notes/g0-deux-semaines-v1/e3-ter-v1/`, **noms seulement** (`git ls-tree`, `git grep -l` sur d'autres chemins). Le vrai registre des scellements n'a pas été touché (`9061a5da…` avant et après).

## Verdict

**Après corrections.** Aucun constat bloquant. Trois constats majeurs, tous de procédure (aucun ne touche le code, l'outil ni une valeur de l'ordre) ; sept mineurs. Les valeurs de l'ordre version 2 sont justes, les trois scripts de couples se rejouent et se défont à l'octet, l'outil du remplacement fait ce qu'il dit et peut servir tel quel (`a89e2226…`). La réserve sur les fichiers de 7a suffit pour cette relance, à condition d'en élargir l'énoncé (m-1).

## Constats

### Bloquant
Aucun.

### Majeur

- **MA-1 — les essais de l'outil ne vivent que dans un dossier temporaire de session.** Le fichier `0a1210da…` n'est suivi nulle part (`git ls-files` : seul `scripts/remplacer_ligne_code_t07_v1.py`) ; il est à `/tmp/claude-0/-home-user/1c58e8d5-f826-5476-bf99-3af565cb9c5a/scratchpad/apres-s7/test_remplacer_ligne_code_t07_v1.py`. L'addendum (à sceller) le cite pourtant par chemin et empreinte comme pièce (`brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md`, l. 280 et l. 359 : `tests/test_remplacer_ligne_code_t07_v1.py`, chemin absent de l'arbre). Un redémarrage de la machine perd la pièce ; le script de couples de l'addendum ne se rejoue pas sur `main` (il lit ce chemin : `FileNotFoundError`, constaté ; rejoué seulement après copie du fichier dans l'arbre temporaire).
  - *Correctif* : verser le fichier dès maintenant, octets inchangés, hors de `src/` et de `tests/`, avec son compagnon ; par exemple `docs/notes/g0-deux-semaines-v1/etape-a-t07-preparation-v1/relance-v2-preparation-v1/essais-outil-a-verser-apres-s7/test_remplacer_ligne_code_t07_v1.py` (`pyproject.toml` : `testpaths = ["tests"]`, il n'y est pas ramassé ; l'étape 6 de l'instance ne joue que `tests/test_t07_*.py` ; ajout seul, P12 (b) tenu).
  - *Couple, addendum l. 359* — avant : `| **brouillon 2** : essais de l'outil (28 cas) | `tests/test_remplacer_ligne_code_t07_v1.py` | `0a1210da…` |` ; après : `| essais de l'outil (28 cas) ; versés hors de `tests/` jusqu'à la fin de l'étape A, puis copiés sous `tests/test_remplacer_ligne_code_t07_v1.py` | `<chemin versé>` | `0a1210da…` |`. Même précision l. 280.

- **MA-2 — la suite des gestes de la mère n'est écrite nulle part d'un seul tenant, et deux pièces se contredisent.** L'addendum, l. 268-270, dit que la nouvelle ligne est recopiée « avant le scellement de l'addendum » (donc remplacement **avant** scellement) ; la note de la consigne (`consigne-fille-etape-a-v2-brouillon1.md`, l. 9-15) énumère « contre-lecture […], scellement ; remplacement […] ». Jouée dans cet ordre, elle scelle un addendum au marqueur `<<NOUVELLE_LIGNE_CODE_T07>>` non rempli. De plus l'ordre v2 (l. 84-85) cite l'addendum par l'empreinte du brouillon 2 (`53ba8ea7…`, « non contre-lu »), qui ne sera pas celle du texte scellé ; et aucune pièce ne donne la ligne de commande exacte du remplacement ni le chemin de la trace.
  - *Couple, consigne l. 9-15* — avant : « (1) gestes de la relance […] : contre-lecture (R2) […], scellement ; remplacement de la ligne `CODE-T07` […] ; marqueurs de l'ordre v2 remplis […] » ; après, numéroté : « (1 a) corrections de la contre-lecture ; (1 b) depuis la racine de `main`, `PYTHONPATH=src` : `construire --racine . --chemin registres/code-t07/CODE-T07-v3.json`, puis `remplacer --racine . --registre registres/scellements-v1.md --ancienne '<ligne de l'addendum, § 5>' --nouvelle '<ligne construite>' --trace <chemin versionné de la trace> --a-blanc`, puis la même sans `--a-blanc` (registre donné par son chemin **relatif** : la trace l'écrit tel quel) ; (1 c) nouvelle ligne recopiée de la trace dans l'addendum, addendum scellé ; (1 d) l'ordre v2 cite l'addendum **scellé** (empreinte), ordre v2 scellé, marqueurs non remplis ; (1 e) commit S7 (`git diff --quiet c2fab6cc S7 -- src tests`), poussée ; (1 f) ordre rempli (quatre marqueurs), scellé, engagement neuf, écrit daté, commit de remise, poussée. »
  - *Couple, ordre l. 84-85* — avant : « addendum de T0.7, brouillon 2 (`brouillons/T0.7-addendum-cache-motifs-v1-brouillon2.md`, `53ba8ea7…`, non contre-lu) » ; après : le chemin et l'empreinte de l'addendum scellé (au brouillon suivant de l'ordre, après (1 c)).

- **MA-3 — le piège « rien sous `tests/` avant S7 » est écrit pour le seul essai de l'outil ; il vaut pour tout fichier, et un autre arrive.** L'ordre le dit bien (P9, l. 326 ; § 0 septies, l. 250 ; § 12, l. 810) et l'addendum aussi (l. 295-296) : la réponse à la question posée est **oui**. Mais à 23:24Z l'arbre principal porte, non suivi, `tests/test_lancer_course_ideation_conception_propre_v1.py` (autre tâche). S'il entre dans `main` avant S7, `git diff --quiet C7 S7 -- src tests` refuse (§ 4.1 de l'ordre, étape 2 du script) et S7 ne peut plus être la tête de `main`. À ce jour `src/` et `tests/` de la tête égalent ceux de C7 (`02749689…`, `42d9f073…`, vérifié).
  - *Couple, ordre l. 326 (P9)* — avant : « l'essai neuf du remplacement (`tests/test_remplacer_ligne_code_t07_v1.py`) entre dans `main` **après** S7 » ; après : « **aucun fichier de `src/` ni de `tests/`, de quelque tâche que ce soit**, n'entre dans `main` avant S7 (à ce jour : l'essai neuf du remplacement, et tout essai d'une autre tâche en cours) ; l'essai du remplacement n'entre qu'après la fin de l'étape A (instance détruite), pour qu'un S7 refait reste possible ». Même élargissement l. 250, l. 810, et addendum l. 295.

### Mineur

- **m-1 — « quatre fichiers » sous-compte ce que le motif pose (réserve 7).** Par les noms seuls, au commit C7 : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/` porte 44 fichiers suivis, dont les quatre de `lecture-7a-v1/` et six autres nommés `audit-ecart-dt4-7a…` (deux notes, deux sorties, deux scripts), plus une consigne `consigne-audit-ecart-dt4-7a-v1.md` ailleurs dans le dossier extrait. Je ne les ai pas ouverts : je ne dis pas ce qu'ils contiennent. Aucun n'est nommé par `src/`, `tests/test_t07_*.py`, `tests/conftest.py`, le script v4, la configuration v8, les exigences ni `.claude/` (recherche refaite). La consigne (§ 2.9) et S-18 visent déjà tout `e3-ter-v1/` ; l'addendum et le point 2 bis non.
  - *Couple, addendum l. 339 et ordre l. 286-287* — avant : « quatre fichiers dérivés de 7a » ; après : « au moins quatre fichiers dérivés de 7a (`lecture-7a-v1/`) ; tout le dossier `e3-ter-v1/` (44 fichiers suivis à C7, dont six nommés `audit-ecart-dt4-7a…`, non ouverts) est tenu sous la même réserve ».
- **m-2 — marqueurs restants.** Seul `COMMIT_SCELLEMENT_T07_V2` ne peut exister qu'après S7. `LIGNE_CODE_T07_V2` existe dès le remplacement (avant S7) ; `ATT_C7_T07_V2` est déjà mesurée ; `ID_SESSION_FILLE_V2` est un choix de la mère. Sans danger, mais `ATT` laissée en marqueur garde ouverte la variante « , 1 warning ». *Couple, ordre l. 340* — avant : `ATT='<<ATT_C7_T07_V2>>'` ; après : `ATT='500 passed, 2 skipped, 4 xfailed'` (ou garder le marqueur, au choix de la mère).
- **m-3 — cinquième jeton à chevrons dans l'ordre** (l. 812 : `<<NOUVELLE_LIGNE_CODE_T07>>`, simple renvoi au marqueur de l'addendum). Un contrôle « plus aucun `<<…>>` » au remplissage butera dessus. *Couple* — avant : « même texte que `<<NOUVELLE_LIGNE_CODE_T07>>` de l'addendum » ; après : « même texte que le marqueur `NOUVELLE_LIGNE_CODE_T07` de l'addendum ».
- **m-4 — essais de l'outil : six mutations sur vingt-six survivent** (détail § 4), toutes sur des contrôles redondants ou défensifs ; aucune ne laisse écrire à tort. L'addendum dit « quatorze sur quinze » (l. 287-288), compte de l'auteur que je ne peux pas rejouer. *Couple* — avant : « Quatorze mutations de l'outil sur quinze attrapées (la survivante retire un contrôle interne redondant). » ; après : la même phrase, plus « Contre-lecture : vingt sur vingt-six ; survivent le contrôle interne des octets, celui de la copie, la relecture après écriture, « nouvelle égale à l'ancienne », « fichier temporaire présent », et le calcul de la fin de ligne quand les deux lignes ont la même longueur (cas réel : 140 octets chacune). » Cas à ajouter à une prochaine version des essais, pas avant la relance : nouvelle ligne de longueur différente ; fichier temporaire déjà présent.
- **m-5 — compagnons absents (R6)** : `scripts/remplacer_ligne_code_t07_v1.py` et les trois scripts de couples (`…brouillon2-appliquer-v1.py`, `…v2-brouillon1-appliquer-v1.py`, `consigne-…-appliquer-v1.py`) n'ont pas de `.sha256`, alors que ceux de la v1 en ont. *Correctif* : les sceller.
- **m-6 — outil, hors refus prévu** : si l'écriture de la trace échoue après `os.replace` (l. 231-233 ; erreur autre que `RefusRegistre`), le registre est remplacé sans trace et la commande sort en code 1. Les contrôles préalables (l. 139-145) rendent le cas improbable. Sans correctif demandé ; à savoir : dans ce cas, ne pas rejouer, écrire la trace à la main depuis `git diff`.
- **m-7 — libellés restés de la v1 dans l'ordre** : encadré de tête l. 21 (« `a621dcd3` est le dernier commit contre-lu ») et l. 125 (« commit de scellement S7 »), alors que S7 n'est plus le commit de scellement de T0.7. Le § 0 septies dit juste ; cosmétique.

## 1. Addendum, brouillon 2 (`53ba8ea7…`)

Empreintes conformes (brouillons 1 et 2, contre-lecture `774b2c38…`). Script de couples rejoué (19 couples) : sortie identique à l'octet, couples défaits → brouillon 1 (MA-1 pour la condition de rejeu). m-1 → réserve 6 ; m-2 → § 4 ; m-3 → § 5 bis et réserve 7, avec le renvoi au § 2.2 de l'ordre ; m-4 → § 5 : **tous traités**, m-5 laissé à la réserve 1 comme annoncé. Le remplacement est dit exactement : ancienne ligne égale à l'octet à la septième ligne du registre (`9061a5da…`), refus de l'outil conformes au code lu, comptes des essais justes (28 cas ; 10, 5 et 19 cas fautifs), effets sur les dates vérifiés (aucun lecteur n'exige l'ordre des lignes ; seule contrainte : avant la première ouverture, `code_t07_v1.py` l. 76-78). Plus fort que les pièces : rien, sauf m-4 (compte de mutations) et m-1 (« quatre »).

## 2. Ordre version 2, brouillon 1 (`522c68ed…`)

Script de couples rejoué (33 couples, 8 blocs `bash -n`, 4 marqueurs neufs) : sortie identique à l'octet ; couples défaits → ordre v1 (`9b3a04da…`). Valeurs, toutes vérifiées :

| valeur | constat |
|---|---|
| C7 `c2fab6cc…` | commit de fusion, parents `cc967f99` et `deaeee03` ; `src/` `02749689…`, `tests/` `42d9f073…` ; ancêtre de la tête |
| `SRC7` `799ef383…` | ancêtre de C7 ; `src/` égal à celui de C7 |
| `ATT` | sortie `9fdbffd2…` : « 500 passed, 2 skipped, 4 xfailed, 1 warning » ; sortie « Zen » `ec085121…` : « 500 passed, 2 skipped, 4 xfailed » ; sauts et échecs attendus identiques (`c1928351…`, recalculé) ; lignes 132-169 et 171-198 sourcées égales à l'octet au script v4 ; commande égale à celle de l'étape 6 (l. 236) plus `TZ=UTC` et `PYTHONDONTWRITEBYTECODE=1` |
| `CODE-T07-v3.json` `d3eaebfe…` | champ `commit` = C7 ; vingt-six empreintes égales à la pièce `7dabdbc8…`, au commit et à l'arbre ; un seul fichier diffère de la v2 |
| `ANT0` 0.43 | seule dépense inscrite sous les deux lignes (`registres/depenses.md`, l. 443) ; `HMAX` reste 43 200 s ; borne « 3,1 USD » juste |
| `W`, `J`, étiquette | `-v2` partout dans la ligne (A) et le § 4.4 |
| branche de sortie | absente du distant à 23:23:46Z (`git ls-remote`) |
| P12 (b) | de C7 à la tête : 18 ajouts, aucune modification ni retrait sous les chemins extraits ; aucun essai `tests/test_t07_*.py` ne parcourt ces dossiers ni ne lit le vrai registre (tous écrivent le leur dans un dossier temporaire) ; script v4, configuration v8 et exigences inchangés |

Le contrôle neuf du § 4.1 (« CODE-T07 égale à la ligne attendue ») a été joué sur une copie remplacée : les deux messages sortent.

## 3. Consigne de la fille, v2 brouillon 1 (`f24032e7…`)

Script rejoué (19 couples), identique à l'octet, réversible vers la v1 remplie (`5fa7adcf…`). Six cases, cinq valeurs : compté. Cohérente avec l'ordre (dossier, journal, étiquette, `ligne-code-t07.txt`, embargo § 2.9 sur tout `e3-ter-v1/`). Seul défaut : la note pour la mère (MA-2).

## 4. Outil du remplacement (`a89e2226…`) et ses essais (`0a1210da…`)

- **Essais joués** depuis l'arbre temporaire : **28 passés**, aucun saut (4,8 s).
- **Vingt-six mutations à la main**, outil restauré après chacune (empreinte recontrôlée) :
  - attrapées (20) : deux lignes tolérées ; comparaison à l'octet retirée ; `--a-blanc` qui écrit ; registre changé non contrôlé ; date égale tolérée ; date future ; journal des ouvertures non lu ; trace présente ; même chemin ; format exact ; sceau du fichier cité ; forme du fichier ; retour chariot ; séparateur unicode ; chemin ; trace non scellée ; saut de ligne dans la nouvelle ; remplacement par normalisation du fichier ; début décalé d'un octet ; clé de la nouvelle ligne.
  - survivantes (6) : voir m-4.
- **Bout en bout sur une copie** (registre de la tête, vrai `CODE-T07-v3.json`) : `construire` rend la ligne au format ; `--a-blanc` : code 0, **aucun fichier créé ni changé** (empreintes, dates et liste comparées avant et après) ; `remplacer` : code 0, **seule la ligne 7 diffère** (`diff`), 140 octets avant et après, trace scellée ; seconde exécution refusée (code 2).
- **Après remplacement** : `lire_registre_detail` (garde « exactement une », clés de l'étape A, marques de la configuration v8), `lire_registre_t07` et `lire_lignes_actuelles` acceptent et rendent `CODE-T07-v3.json` ; `code_t07_v1 verifier` : « conforme : commit c2fab6cc…, 26 fichiers », code 0 ; l'`awk` du script v4 (l. 182) recopie le chemin neuf.
- **Témoins** : ligne ajoutée au lieu d'être remplacée → « 2 ligne(s) CODE-T07 » ; ancienne ligne et `CODE-T07-v2.json` → `verifier` refuse (« src/controle_ia/ de l'arbre exécuté ≠ commit cité b4cd9953… »), code 2.
- **Une seule ligne** : le remplacement est construit par tranche d'octets (l. 176-178) et contrôlé deux fois avant l'écriture (l. 180-187) et une fois après (l. 227) ; je n'ai trouvé aucune voie qui touche un autre octet.

## 5. Réserve sur les fichiers de 7a posés sur l'instance

**Suffisante pour cette relance**, avec m-1. Raisons vérifiées : rien de ce que joue l'instance ne les nomme ni ne parcourt leur dossier ; aucun agent n'agit sur l'instance (mode « args ») ; les poussées sont par chemins explicites ; l'état est celui du lancement de la v1 ; l'exclusion demande un script neuf, donc empreinte, répétition et contre-lecture, hors de la correction minimale de R-2593. Deux demandes : porter la réserve au compte rendu de l'étape A (§ 8 de l'ordre) pour que le verdict de porte la voie ; faire le script v5 de S-18 avant tout autre emploi du script (étape B ou seconde relance).

## Pièces lues

Les trois pièces et leurs sources (addendum brouillon 1, ordre v1, consigne v1 remplie), les trois scripts de couples, la contre-lecture R-2602, l'outil et ses essais, `registre_v1.py` et `code_t07_v1.py` (lignes citées), le script v4 (l. 125-200, 236, 355-366), les pièces de la mesure sous `relance-v2-preparation-v1/`, `registres/depenses.md` et `registres/go.md` (lignes des deux GO), `registres/decisions.md` (R-2588 à R-2612, titres).

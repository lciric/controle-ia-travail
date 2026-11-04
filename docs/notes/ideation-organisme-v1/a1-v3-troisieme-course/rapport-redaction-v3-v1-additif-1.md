# Additif 1 au rapport de rédaction v3 (`rapport-redaction-v3-v1.md`, `e8f2729d…`) — sonde d'hôte et variantes « Coût » et « clé »

Même rédacteur-développeur, 4 novembre 2026, de 08:29 à 08:45 UTC (`date -u`), sur la suite demandée par le directeur. Mêmes
interdits : fichiers neufs, aucun commit, aucun `.sha256`, aucune location, aucun appel, aucune clé lue. Un fichier rendu plus tôt a
été réécrit : `couples-variantes-cout-cle-v1.json`, régénéré par son propre script après une correction. Ton instantané en porte la
version précédente.

**Verdict.** Le mode sonde est écrit et ses 18 essais jouets passent. Les couples des variantes (a) et (b) sont écrits et vérifiés,
sans être appliqués. Il reste à lancer la vraie sonde : c'est une dépense (au plus 0,50 USD sous GO-2026-11-04-06, ou sous le GO
de la machine si la variante (a) est retenue).

## 1. Fichiers neufs (sha256 à 08:42 UTC)

| fichier | sha256 |
|---|---|
| `src/controle_ia/sonde_hote_durable_a1_v3.py` (317 lignes, bibliothèque standard seule) | `1b7e236fdbc503de150cbb198d720d8b51cfc7ac94f53237ac48a3266f205c3a` |
| `scripts/amorce_sonde_hote_durable_a1_v3_v1.sh` | `5e5f388a8c33b15ccba4f5e4b39522128c27c8382f5e5cc8bfbc5e2c170973d8` |
| `tests/test_sonde_hote_durable_a1_v3.py` (18 essais) | `fadefcf5555fad3c284712479b397921927f9f16de1a8e23c76bf414c3f29b51` |
| `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/couples-variantes-cout-cle-v1.json` | `988c27a8a5239393771a31d3dc4526e1285baf3615527fde84c81515d5b84177` |
| bloc-notes `…/scratchpad/v3b1/couples_variantes.py` (génère et vérifie le fichier JSON) | `3d79e17649240d732c1c61260979fb3cceb696187972c9c736529d176e06087c` |

Le lanceur durable rendu (`hote_durable_a1_v3.py`, `5b853fde…`) n'est pas modifié. La sonde l'importe et reprend sa classe
`Machine` : scellement, contrôle des secrets, versement, poussée vérifiée et destruction sont ceux de la course.

## 2. Le mode sonde

- **Partie « louer »** (session de la fille) :
  - GO-2026-11-04-06 contrôlé par la garde de `main` (montant exact).
  - L'offre doit être conforme : aucune carte, au plus 0,40 USD/h, mêmes minima que la course. Elle doit aussi être **la moins
    chère des offres conformes** de la réponse brute de Vast.
  - Plafond de durée : 20 min par défaut, 30 au plus.
  - **Plafond de dépense : 0,50 USD**, calculé comme prix × (durée + 15 min de marge) ; au pire 0,40 × 35/60 ≈ 0,23 USD.
  - Le corps de création ne porte que `COMMIT_PRIVE`, `GO_ID`, `PRIX_H_USD`, `DUREE_MAX_S`, `DEPOT_URL` et `GH_TOKEN`. Une clé de
    modèle (`CLE_ARGON`, `GEMINI*`, `ANTHROPIC*`, `OPENAI*`, `MOONSHOT*`, `KIMI*`) y est refusée.
  - Création par l'outil `vastai`, même forme que la course : image `python:3.13-bookworm`, `--entrypoint bash --args -c`. La
    sortie de l'outil est filtrée.
- **Partie « hote »** (machine) :
  - Elle refuse de partir si une clé de modèle est dans son environnement. Elle revérifie le prix et le plafond de dépense, puis le
    GO sur `main`.
  - Elle relève les faits de l'hôte au journal : version de Python, `/usr/bin/python3`, numpy, git, cœurs, disque, présence (en
    booléen) de `CONTAINER_ID` et de `CONTAINER_API_KEY`. L'amorce chronomètre aussi les installations.
  - Elle lit la machine avec la clé d'instance. C'est une mesure : elle montre si cette clé lit la machine.
  - Elle lance une **course factice détachée** : un processus qui ne reçoit aucune variable de clé, écrit un battement toutes les
    10 s et dure 3 600 s, plus que tout plafond.
  - La garde fait un relevé toutes les 30 s. **Au plafond de durée**, la course factice est arrêtée par son identifiant de
    processus, ce qui est la fin attendue (`plafond_de_duree_de_la_sonde`).
  - Fin, héritée de la course : liste `EMPREINTES-sonde-hote-durable-a1-v3-v1.txt`, contrôle des secrets, versement sur la
    branche neuve **`donnees/sonde-hote-durable-a1-v3-v1`** avec poussée vérifiée, puis **destruction par l'identifiant de la
    machine**. Si la poussée n'est pas vérifiée ou si un secret est trouvé, la machine est arrêtée sans être détruite.
  - Reprise du conteneur : rien n'est relancé ; versement sur `…-sonde-hote-durable-a1-v3-interrompue-v1`, puis destruction.
- **Ce que la sonde éprouve et que les essais jouets ne peuvent pas** :
  - les offres sans carte et la création ;
  - l'image (git, `/usr/bin/python3`, numpy 2.5.3) ;
  - une commande détachée qui survit à l'amorce ;
  - la poussée depuis la machine ;
  - la clé d'instance, en lecture (au journal versé) puis en destruction (vue par l'inventaire après la sonde).

## 3. Essais (`timeout 900 nice -n 10`)

`tests/test_sonde_hote_durable_a1_v3.py` : **18 passés** (20 s). Ceux du lanceur durable, rejoués : 49 passés. Chaque garde est
éprouvée sur un cas sain et sur un artefact :

| garde | cas sain | artefacts |
|---|---|---|
| plafond de dépense et de durée | 0,40 USD/h à 20 et 30 min | 0, 31 et −1 min ; plafond de 0,10 USD |
| offre la moins chère | la moins chère des conformes ; une carte moins chère n'est pas comptée | offre plus chère ; offre avec carte |
| corps sans clé de modèle | variables exactes, `DUREE_MAX_S` 1200, amorce de la sonde dans le script | jeton absent ; `CLE_ARGON` ajoutée au corps refusée par l'outil |
| location jouet | une machine créée, journal sans jeton | offre plus chère ; 45 min ; autre GO ; montant 35 ; jeton absent. Pour chacun : code 2, rien créé ; la vérification seule ne crée rien |
| machine, cas sain | GO, faits, clé d'instance « vue », course factice détachée, plafond de durée à 1,5 s, arrêt par identifiant, battements versés, la course factice n'a vu aucune variable de clé, liste juste, aucun secret, détruite | — |
| fin avant le plafond | course factice finie, versée, détruite | — |
| refus sur la machine | — | `CLE_ARGON` ; `GEMINI_API_KEY_2` ; autre GO ; 0,5 USD/h ; jeton absent ; plafond de 60 min. Pour chacun : rien lancé, état versé, détruite ; aucune valeur interdite au journal |
| reprise | — | aucune relance, branche « interrompue », détruite |
| fuite | — | jeton dans un fichier de l'état : rien versé, machine arrêtée |
| amorce de la sonde | — | jeton absent ; `CLE_ARGON` présente ; autre GO. Pour chacun : code 2, jeton jamais affiché |

## 4. Variantes « Coût » (a) et « clé » (b) : `couples-variantes-cout-cle-v1.json`

Les couples ne sont appliqués à aucun fichier du dépôt. Le script les vérifie sur des copies.
- **(a) GO à part pour la machine** : 7 couples de texte et 7 couples de code.
  - Le marqueur neuf `GO_MACHINE` (entre doubles chevrons) apparaît en sections 8, 12 et 13. Il est annoncé dans le paragraphe de
    tête, la section 0.7 (ligne 22) et l'annexe B (trois marqueurs).
  - GO-2026-11-04-06 reste à 400 USD pour les appels d'Argon seuls ; le GO de la machine vaut 35 USD (machine et sonde).
  - Le code ajoute `verifier_go_machine` (garde de `main`, montant exactement 35 USD, identifiant distinct de -06), son appel dans
    `louer`, l'option `--go-machine` et un essai neuf, cas sain et artefacts.
- **(b) Clé d'Argon dédiée** : 3 couples de texte (section 8, « Création » et point (4) ; section 0.7, ligne 23, ou 22 si (b) est
  seule) et 4 couples de code.
  - Le lanceur lit la clé **par son nom**, celui de la variable de la session que nomme `--variable-cle-argon` (par exemple
    `GEMINI_API_KEY_A1V3`, nom à fixer). La valeur n'est jamais développée sur une ligne de commande.
  - Le nom est contrôlé (majuscules, chiffres, soulignés). La valeur est masquée au journal, et sa présence y est écrite en
    booléen.
- **Vérification** : chaque « ancien » est présent une seule fois au moment de son application, pour (a) seule, (b) seule, et (a)
  puis (b).
  - Textes résultants : (a) et (a) puis (b) portent les trois marqueurs ; (b) porte les deux du brouillon. Le bloc du plan n'est pas
    touché.
  - Code et essais résultants, compilés puis joués dans des copies du bloc-notes : (a) 50 passés, (b) 49 passés, (a) puis (b)
    50 passés (en 132 s).

## 5. Commande exacte de la sonde, pour la fille

Après le commit de la sonde sur `main` du dépôt privé (`COMMIT_PRIVE`, hash complet donné par le directeur). Coût au plus 0,50 USD
sous GO-2026-11-04-06, ou sous le GO de la machine si la variante (a) est retenue. `OFFRE` est **la moins chère des offres
conformes** de `offres.json`, sinon la sonde la refuse.

```
D=/home/user/hors-clone-sonde-a1-v3-v1; mkdir "$D"                 # neuf (R12)
cd /home/user/controle-ia-travail && git fetch -q origin main
git show origin/main:registres/go.md > "$D/registre-go-main.md"
git show origin/main:.claude/hooks/garde_calcul.py > "$D/garde_calcul_main.py"
for f in hote_durable_a1_v3.py sonde_hote_durable_a1_v3.py; do git show "$COMMIT_PRIVE:src/controle_ia/$f" > "$D/$f"; done
timeout 300 vastai search offers 'num_gpus=0 rentable=true verified=true reliability>=0.98 cpu_cores_effective>=4 cpu_ram>=8 disk_space>=30 dph_total<=0.40' -o dph_total --raw > "$D/offres.json"
for V in "--verifier-seulement" ""; do
  env -i PATH="$PATH" HOME="$HOME" LANG=C.UTF-8 GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN" timeout 900 nice -n 10 \
    python3 -I -B "$D/sonde_hote_durable_a1_v3.py" louer --go GO-2026-11-04-06 \
      --registre-main "$D/registre-go-main.md" --garde-main "$D/garde_calcul_main.py" --offres "$D/offres.json" \
      --offre "$OFFRE" --commit-prive "$COMMIT_PRIVE" --duree-min 20 --journal-local "$D/journal-location-sonde-v1.log" $V || break
done
```

L'environnement passé par `env -i` ne contient aucune clé de modèle ; l'outil `vastai` garde sa clé dans `HOME`. L'identifiant de
la machine est dans `$D/journal-location-sonde-v1.log.identifiant`.

Environ 35 min après la création :
- `git ls-remote origin refs/heads/donnees/sonde-hote-durable-a1-v3-v1` montre la branche ;
- son `journal-sonde-a1-v3-v1.log` porte « nature de la fin : plafond_de_duree_de_la_sonde », « versé » et « clé d'instance :
  lecture faite … vue » ;
- `python3 -I -B "$D/hote_durable_a1_v3.py" inventaire` ne montre plus la machine.

Si la machine est encore listée (destruction par la clé d'instance refusée), la détruire par son identifiant
(`vastai destroy instance <ID>`, R10), consigner dans `registres/arrets.md`, et revoir la fin de la course avant tout lancement.
Rien de la sonde n'est une sortie de course : elle peut être lue.

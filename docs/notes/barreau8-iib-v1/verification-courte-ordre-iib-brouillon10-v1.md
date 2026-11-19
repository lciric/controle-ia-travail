# Vérification courte — ordre exploratoire ii-b, brouillon 10

## Document vérifié

- Fichier : `brouillons/ii-b-saboteur-budget-v1/ordre-exploratoire-ii-b-v1-brouillon10.md`
- Empreinte : `a52cb18534ebd635343e262d4ebc56b06619f35b2c4c1643204c74e02387d4ca`
- 375 lignes

## Vérificateur

Session distincte, modèle Opus 4.6, du côté du saboteur à budget, exclu de tout rôle côté sondes du barreau 8. Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » n'a été lu ni ouvert.

## Conclusion

**Un défaut, six points conformes.** Le texte est scellable après les trois couples de correction du point 3. Le défaut est un chemin de dossier (`$W/iib`) aux lignes 241 et 244 qui devrait être celui du dossier neuf des contrôles rejoués : la création et la surveillance liraient le `lancement.txt` de l'étape 1, pas celui du rejeu frais.

---

## Point 1 — Marqueurs du § 11 : CONFORME

Les 30 marqueurs de `configuration_v1.MARQUEURS` dans la table « Valeurs à l'octet » (lignes 322-353) ont été comparés un par un à la configuration au commit de lancement (`git show 836c7cccda5071fe54ecb148d214d74b5cb90474:docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`).

- 27 marqueurs : égaux à l'octet.
- 2 marqueurs (`CHEMIN_ORDRE_IIB`, `EMPREINTE_ORDRE_IIB`) : correctement marqués « hors de ce texte » (circulaire).
- 1 marqueur (`EMPREINTE_CONFIG_IIB`) : égal à l'empreinte recalculée du fichier de configuration (`1bd2e16a79def36de945359bb64e34beb899410dfe2964d28da1f1b85e3f6a17`), que la configuration ne peut pas porter elle-même.
- Le bloc `EMPREINTES_CODE_IIB` (3 499 caractères, 34 fichiers) : identique à l'octet à la valeur de la configuration.
- `LIGNE_REGISTRE_CREATION_7B` : exactement 2 occurrences dans le texte (§ 1 et § 4 étape 4), conformément à la déclaration.
- Aucun motif `<<MARQUEUR>>` restant (la seule paire `<<`/`>>` est dans la commande de vérification grep du § 11).
- Aucun motif `[PIÈCE …]` restant.

## Point 2 — Chaîne de commits : CONFORME

### Parents vérifiés

| commit | parent | vérifié |
|---|---|---|
| `836c7ccc` (lancement) | `f9a8aaeb` (code revu) | oui, par `git rev-parse HEAD^` |
| `f9a8aaeb` (code revu) | `ec3b0329` (code revu d'alors) | oui, par `git rev-parse HEAD^` |

- `ec3b0329` descend de `a31b8970` : vérifié par `git merge-base --is-ancestor`.
- Le commit de lancement `836c7ccc` n'ajoute que 2 fichiers (`docs/notes/barreau8-iib-v1/config-iib-reel-v1.json` et son `.sha256`) : vérifié par `git diff --name-only`.

### Empreintes du code (bloc EMPREINTES_CODE_IIB)

10 fichiers sur 34 vérifiés par `git show 836c7ccc:<chemin> | sha256sum`, tous conformes :

| fichier | empreinte (premiers 16 car.) | conforme |
|---|---|---|
| `scripts/lancer_iib_v1.sh` | `3279e3dcc6315…` | oui |
| `scripts/amorce_instance_iib_v1.sh` | `5d78e7e4b6466…` | oui |
| `src/controle_ia/iib/lanceur_v1.py` | `140dcab7ce396…` | oui |
| `src/controle_ia/iib/configuration_v1.py` | `d79f21b0e0344…` | oui |
| `src/controle_ia/iib/session_v1.py` | `4eb7947c28caf…` | oui |
| `src/controle_ia/iib/oracle_v1.py` | `3dec7c9acb51a…` | oui |
| `src/controle_ia/iib/tours_v1.py` | `df6267f47f369…` | oui |
| `scripts/tests-cibles-iib-v1.txt` | `847676eff87f2…` | oui |
| `tests/test_iib_scripts_v1.py` | `239a643012199…` | oui |
| `tests/test_iib_oracle_v1.py` | `924e673b50bc7…` | oui |

Échantillon de 29 % (10/34), réparti sur scripts, source et essais. Aucun écart.

## Point 3 — Commandes du § 5 : DÉFAUT CONFIRMÉ

### Défaut : chemin du dossier de création (lignes 241 et 244)

Le texte, à la ligne 241 (étape 2, « Création »), dit :

> « l'exécutante rejoue `controles-explo` (étape 1, **dossier neuf**, variables de cet ordre) »

Puis donne :

> `"${ENVI[@]}" bash scripts/lancer_iib_v1.sh creation auto course 0 "$W/iib" 1795816800`

**Le dossier `$W/iib` existe déjà** (créé à l'étape 1 par `controles-explo`). Le lanceur refuse un dossier existant pour `controles-explo` (ligne 76 : `[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }`). Le rejeu doit donc utiliser un chemin distinct, disons `$W/iib-creation`.

Or la commande `creation` cite `"$W/iib"` : elle lit le `lancement.txt` de l'étape 1 (ligne 133 du lanceur : `[ -f "$D/lancement.txt" ] && grep -q '^controles-explo ' "$D/lancement.txt"`), pas celui du rejeu. Les résultats frais du rejeu sont donc ignorés par la création.

De même, la surveillance à l'étape 3 (ligne 244) cite `"$W/iib"` et devrait citer le dossier du rejeu, car les écritures de `apres-creation` (identifiant de l'instance, horodatage de création) sont faites dans le dossier passé à `creation`.

**Conséquence** : la création fonctionne (elle lit le `lancement.txt` valide de l'étape 1, dont les données sont équivalentes), mais l'intention du rejeu — vérifier que les contrôles passent encore après le redémarrage du conteneur — est inopérante : ses résultats ne sont pas consommés par la suite.

### Couples de correction proposés

1. **Ligne 241, instruction du rejeu** : nommer explicitement le dossier neuf dans la commande de `controles-explo` (par exemple `"$W/iib-creation"`), pour lever l'ambiguïté.

2. **Ligne 241, commande `creation`** :
   - Avant : `creation auto course 0 "$W/iib" 1795816800`
   - Après : `creation auto course 0 "$W/iib-creation" 1795816800` (ou le chemin choisi pour le rejeu)

3. **Ligne 244, commande `surveillance`** :
   - Avant : `surveillance <ID> "$W/iib"`
   - Après : `surveillance <ID> "$W/iib-creation"` (même chemin)

### Autres commandes du § 5 : conformes

Toutes les autres commandes de l'étape 1 (préparation, extractions, `--verifier-go-seulement`, `controles-explo`, inventaire, `ls-remote`) ont été vérifiées contre `scripts/lancer_iib_v1.sh` au commit de lancement : sous-commandes, ordre des arguments, variables exigées, codes de sortie conformes.

Le horodatage de l'échéance `1795816800` a été vérifié : il vaut `2026-11-27T22:00:00Z`.

Le `fin_go_utc_s` lu dans la pièce de lancement (`1795824000`) correspond à `2026-11-28T00:00:00Z`, soit 2 heures après la minuterie.

## Point 4 — Arrêts et bornes : CONFORME

### Cohérence des plafonds

| borne | valeur | source |
|---|---|---|
| Plafond de configuration (`PLAFOND_CONFIG_IIB`) | 55 USD | config, § 11 |
| Plafond du devis (§ 6) | 59,8 USD (48 h d'arrêt) | ordre |
| Plafond de la ligne d'accord (`PLAFOND_LIGNE_IIB`) | 60 USD | GO, config, § 11 |

55 ≤ 59,8 ≤ 60 : cohérent.

### Cohérence des échéances

| borne | valeur | vérification |
|---|---|---|
| Minuterie (`ECHEANCE_UTC_S`) | 2026-11-27T22:00:00Z (1 795 816 800) | `date -u` = conforme |
| Fin GO (`FIN_GO_UTC_IIB`) | 2026-11-28T00:00:00Z (1 795 824 000) | +7 200 s = conforme |
| Dernier jour de création | 2026-11-25 (23:00 UTC) | avant minuterie |
| Destruction (§ 5 étape 6) | avant 2026-11-28T00:00:00Z | ≤ fin GO |
| Attente mère (§ 5 étape 5) | ≤ 48 h après fin, jamais après minuterie | minuterie < fin GO |

La phrase « dans les bornes de temps dites juste avant » (ligne 255, ajoutée au brouillon 10) raccorde « ne détruit rien, s'arrête et rend la main » à la borne de 48 heures : pas de contradiction.

### Arrêts par identifiant (R10)

Le § 5 et le § 6 ne nomment que des arrêts et destructions par identifiant d'instance (`<ID>`, `timeout -k 5 120 vastai destroy instance <ID>`, commande d'arrêt imprimée par la surveillance). Aucun arrêt par motif de ligne de commande.

### Cinq points du § 4 des différences

1. « dans les bornes de temps dites juste avant » : cohérent, pas de contradiction (voir ci-dessus).
2. Sections historiques (brouillon 9) : inchangées, correct.
3. `R-3655` écrit sur parole de la mère : noté, le rédacteur le déclare (l. 6 de l'ordre et l. 71 des différences).
4. Redémarrage du conteneur et état du fichier de lancement : sur parole de la mère, le rédacteur le déclare (l. 72 des différences).
5. Cinq différences de configuration : rien à changer (l. 73 des différences).

## Point 5 — Pièces citées avec empreinte : CONFORME

40 pièces distinctes citées avec empreinte SHA256 complète (seuil de 15 largement dépassé).

- 37 vérifiées : **37 conformes, 0 écart**.
- 3 interdites de vérification (fichiers contenant « consigne-privee » ou « conception-ii-b ») : **non vérifiées, interdit de lecture** (règle absolue du mandat).

Les pièces se répartissent sur 5 branches ou commits :
- `main` : 22 fichiers (brouillons, devis, nœuds, notes du barreau 8, préenregistrement, différences).
- `prep/iib-code-v4` : 2 fichiers (rapports du développeur v6 et v7).
- `836c7ccc` (commit de lancement) : 1 fichier (configuration).
- `claude/iib-executante-v1` tête `68c1b734` : 13 fichiers (mandat, journaux, pièces à blanc).
- `claude/iib-executante-v1` tête `a0ce3f3e` : 2 fichiers (journaux à blanc du brouillon 10).

## Point 6 — Différences brouillon 8 → 10, gardes et arrêts : CONFORME

Le brouillon 8 (`eb83e9444df3bdfa822ef3bf76efe4039b450a7a8458fe4c91ba20f73d4eb76e`) a été comparé au brouillon 10, par les notes de différences intermédiaires (brouillon 8 → 9, brouillon 9 → 10). Aucune garde, aucun arrêt, aucun interdit n'a disparu. Les deux seules modifications de substance touchant des gardes sont des renforcements :
- § 5 étape 5 : la lecture du disque n'est plus nommée (renforcement : l'exécutante s'arrête et rend la main).
- § 7 : exclusions de toute copie publique (renforcement).

## Point 7 — Différences déclarées : CONFORME

La section « Ce que le brouillon 10 change » (lignes 39-50 de l'ordre) et la note des différences (`differences-brouillon9-vers-10-v1.md`) listent :
- 26 couples appliqués, 12 blocs de diff.
- Chaque couple est situé par section, ligne et bloc.
- Les 12 changements déclarés couvrent : nombre d'essais attendu (5 couples), jeux à blanc (2), contrôles rejoués (1), nombre d'essais passé à l'instance (1), texte du brouillon 3 (1), disque d'une instance arrêtée (1), copie publique (1), exclusions du § 8 (2), devis (4), corrections de R-3535 (2), défauts du brouillon 9 (2), mises à jour de titre et statut (4).
- 5 points « relevé sans être corrigé » sont transparents et justifiés (§ 4 des différences).

Aucun changement non déclaré détecté.

---

## Refus d'outil

Aucun refus d'outil pendant cette vérification.

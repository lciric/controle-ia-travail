# Contre-lecture R2 — lanceur de l'organisme d'idéation des organismes discrets v2

Date : 2026-11-17T13:00Z (UTC)
Lecteur : Sonnet 5.5 (claude-sonnet-5-5), sous-agent neuf, n'a pas écrit le lanceur
Empreinte vérifiée : oui, `6e6e447ca7888b9908e318f17506eb72807aca619f58aa15932c50c449b198d6` (491 lignes) — conforme.
Limite de la lecture : le clone de l'orchestrateur (`/home/user/lciric/ideation-organism/orchestrator`) est absent de mon conteneur ; je n'ai donc pas pu vérifier les valeurs par défaut de `ideation_v8.py` (par exemple : que l'absence de proposeur ou de juge Claude ne retombe pas sur un défaut Claude). Les tests du lanceur n'ont pas été exécutés par moi.

## Verdict global
À CORRIGER — les trois gardes ajoutées en v2 sont présentes et la chaîne principale est saine, mais la garde du plafond du GO est circulaire (constantes contre constantes), la garde de l'arbre propre laisse passer des fichiers non suivis, et la promesse « tout refus rend 2, rien écrit » n'est pas tenue.

## Défauts significatifs

1. Garde du plafond du GO et du cumul : circulaire, ne lit ni le GO ni les dépenses. Lignes 45, 75-76, 331-339, 198.
   `TOTAL_PLAFOND_GO_USD = 17.0`, `CUMUL_COLLISIONNEUR_USD = 7.86` et `TOTAL_EXTERNE_USD = 9.14` sont des constantes du fichier ; la commande est construite avec la même constante `TOTAL_EXTERNE_USD` (l. 265), puis `garde_sommes` vérifie que cette constante égale cette constante (l. 335) et que 7.86 + 9.14 ≤ 17.0 (l. 337). Seul un changement du code peut faire échouer ces tests. Le champ « plafond » de la ligne du GO (`17 USD`, `registres/go.md` l. 363) est renvoyé par `verifier_go` (l. 198) mais n'est jamais analysé ni comparé ; le cumul réellement dépensé par le collisionneur n'est pas relu dans `registres/depenses`. Si le GO est modifié (plafond abaissé, extension), ou si la dépense réelle du collisionneur dépasse 7,86, le lanceur lance quand même. La correction v1→v2 existe dans la forme, pas dans l'effet. Gravité : moyenne (le dépassement possible est borné par les plafonds par rôle et par l'orchestrateur, mais la garde annoncée ne garde rien d'extérieur). Correction suggérée : analyser la cellule « plafond » du GO, la comparer à `TOTAL_PLAFOND_GO_USD`, et relire le cumul dépensé dans le registre des dépenses.

2. Garde de l'arbre propre : contournable par des fichiers non suivis ou ignorés ; couverture des empreintes partielle. Lignes 215, 49-59, 209-226.
   `git status --porcelain --untracked-files=no` ignore les fichiers non suivis (et ceux du `.gitignore`). Or l'orchestrateur est lancé avec `-I` et insère lui-même ses chemins dans `sys.path` (voir la sonde, l. 110) : un module non suivi qui en masque un autre, ou un `.pyc` périmé, n'est pas vu. Seuls 9 fichiers sont empreintés ; le reste de l'arbre ne l'est que par le commit et l'état propre des fichiers suivis. S'ajoute un intervalle de temps entre la vérification (l. 413-415) et l'usage (sonde, liste blanche, course) : aucune relecture au dernier moment. Gravité : moyenne (menace réaliste faible, mais c'est exactement la propriété « aucune modification » que la correction v1 devait garantir). Correction suggérée : retirer `--untracked-files=no` (ou lister `git ls-files --others` et refuser), et relire les empreintes immédiatement avant `Popen`.

3. Promesse « tout refus rend 2, rien écrit, rien appelé » non tenue ; ordre annoncé non respecté ; manifeste de fin non garanti. Lignes 14, 22, 426-433, 452-471, 299-303, 308-317.
   a) Après `mkdir` (l. 430-431), un refus de `construire_liste_blanche` (l. 393, 397) laisse les dossiers de course et éventuellement `liste-blanche.json` sur disque : « rien écrit » est faux dans ce cas.
   b) Avant le manifeste de départ, le lanceur exécute déjà le script de l'orchestrateur (`--construire-liste-blanche`, l. 390) et la sonde qui importe son code (l. 348) : la docstring place le lancement de l'orchestrateur à l'étape 6, après le manifeste de départ, et ne mentionne pas la construction de la liste blanche.
   c) Des erreurs hors `Refus` (`ValueError` de `float()` ou de `split("=")` dans `sommes_plafonds`, `json.JSONDecodeError` l. 394, `OSError` de `Popen` ou de la lecture des journaux) produisent une trace et le code 1, pas 2.
   d) Si `Popen` ou `sha256_fichier` échoue après le manifeste de départ, le manifeste de fin n'est jamais écrit : un départ scellé sans fin.
   Gravité : moyenne à basse (aucune dépense engagée dans a, b, c ; d est une lacune de traçabilité). Correction suggérée : envelopper toute la partie après `mkdir` (attraper `Exception`, écrire un manifeste de fin « échec » scellé), corriger la docstring.

## Défauts mineurs

4. Abréviations d'`argparse` des drapeaux Claude (l. 99-102, 283). La liste « exacte » ne voit pas `--moteu` ou `--seconde`, que `argparse` accepte par défaut si l'orchestrateur ne coupe pas les abréviations. Atteignable seulement par `arguments_en_plus` (tests), pas en production. Le préfixe des drapeaux interdits (l. 281) couvre déjà ce cas pour la première liste.
5. Périmètre du GO (l. 196) : deux sous-chaînes indépendantes (« organisme », « idéation »), pas la locution « organisme d'idéation » annoncée par le message d'erreur et la correction v1→v2.
6. Révocation (l. 175) : détectée seulement si la cellule type vaut exactement « révocation » (accent, casse) et si la ligne a 8 colonnes ; « revocation » ou « révoqué » passerait sans bruit. De même, les lignes d'« extension » (l. 177) sont ignorées, jamais lues pour le plafond.
7. `PATH` est repassé tel quel à l'enfant (l. 92) : `bash` (lancé par l'orchestrateur via `--commande-externe`), `git` et `date` sont résolus par `PATH` ; ni le chemin ni l'empreinte de `bash` ne sont épinglés.
8. Le lanceur ne vérifie pas qu'il tourne sous `-I` (`sys.flags.isolated`) ni que `sys.executable` est `/usr/local/bin/python3` (l. 12, 159) ; il se contente de l'enregistrer (l. 443). Son propre empreinte n'est pas épinglée (seulement enregistrée, l. 434).
9. L'état modifié du dépôt de travail n'est que consigné (`arbre_modifie`, l. 404), jamais refusé, alors que le lanceur est dans le même dépôt que les pièces.
10. Deux horloges : `horodatage` (l. 416, `date -u`) et l'identifiant de course (l. 417) viennent de deux appels distincts ; ils peuvent différer d'une seconde dans le manifeste.
11. Contrôle d'espace dans les chemins (l. 251-253) sur `question` et `enveloppe_argon` seulement ; seule l'enveloppe est concernée par une découpe (`"bash " + chemin`), et aucun contrôle des guillemets ou caractères spéciaux — sans effet avec des constantes.
12. `--budget-total-usd` : `garde_sommes` accepte l'absence du drapeau (`None`, l. 340-342). Sans conséquence ici (la commande l'inclut), mais la garde ne ferme pas la porte si la construction change.

## Observations sans défaut

- Ordre d'exécution (l. 413-448) conforme à la docstring pour les étapes 1 à 5 : GO, orchestrateur, pièces, commande, drapeaux, sommes, environnement, bac à sable ; seule l'étape 6 déroge (défaut 3b).
- Empreintes épinglées : orchestrateur (commit, 9 fichiers) et 4 pièces (question, faits, enveloppe, commande d'Argon) vérifiées avant toute sonde et tout lancement (C : oui, sous réserve du défaut 2).
- Environnement : liste blanche de noms (`PATH, LANG, LC_ALL, TZ, TMPDIR`) plus `GO_ID`, `HOME`, `PYTHONPYCACHEPREFIX` ; tout le reste est retiré, y compris les noms ressemblant à des clés (D : oui). Vérifié : l'enveloppe d'Argon ne détient qu'une clé factice (`appel-argon-v5.sh` l. 19, 27) ; le retrait des clés réelles ne casse donc pas l'appel.
- Injection de commande : aucun `shell=True` ; `argv` en liste ; les seuls chemins construits viennent de constantes (F : pas de faille trouvée).
- Manifeste de départ créé par `xb`, empreinte compagnon par `x`, jamais d'écrasement (R12) ; écrit avant `Popen` ; manifeste de fin après `wait` (E : oui dans le cas nominal).
- Relais de SIGTERM/SIGINT/SIGHUP vers l'enfant, restauration des gestionnaires, PID consigné (R10).
- Liste blanche relue et comparée aux empreintes épinglées (l. 394-397).
- Le GO réellement présent (`registres/go.md` l. 363) correspond à l'identifiant, au type « calcul », à l'accordeur « Lazar », à l'échéance du 2026-11-22.

## Vérification des corrections v1→v2

1. Garde de l'arbre propre sur l'orchestrateur — présente : oui ; correcte : partiellement (fichiers non suivis ignorés, défaut 2) ; cohérente avec le reste : oui.
2. Gardes du plafond du GO et du cumul collisionneur + externe — présentes : oui ; correctes : non (circulaires, défaut 1) ; cohérentes : oui (7,86 + 9,14 = 17,00, somme des plafonds 7,2 < 9,14).
3. Garde du budget Claude égal à 0.0 — présente : oui (l. 340-342, et la commande passe `0.0` l. 264) ; correcte : oui ; cohérente : oui.
4. Drapeaux Claude interdits en correspondance exacte, séparés des préfixes — présente : oui (l. 94-102, 280-284) ; correcte : oui pour les arguments de production (aucun ne correspond à tort : `--piece`, `--budget`, `--juge-externe` passent) ; limite : les abréviations d'`argparse` (défaut 4, test seulement) ; cohérente : oui.
5. Périmètre du GO resserré à « organisme d'idéation » — présente : oui ; correcte : partiellement (deux sous-chaînes, défaut 5) ; cohérente : oui avec la ligne réelle du GO.

Verdict : corriger les défauts 1, 2 et 3, puis relancer une contre-lecture limitée à ces trois points ; les mineurs peuvent partir dans la v3 ou être consignés. Aucun refus d'emblée : aucune faille de sécurité exploitable trouvée dans le chemin de production.

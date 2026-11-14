# Contre-lecture 8, ciblée, de la commande v6 (amorce v3 → v4, suivi v2, dépôt réduit v7 → v8, essai à blanc v3 → v4) — rapport (texte rendu, recopié)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `88b76f62` de `prep/neuron-lens-v1` par la session de reprise ; rapport
lu avant 14:24:03 UTC (`date -u`) ; lecture seule (`sha256sum`, `diff`, `bash -n`, lecture ; essais du suivi v2 exécutés). Recopié tel
qu'il a été rendu (mise en forme seule) ; les suites données sont dans l'en-tête de la commande v7.

Arbre : commit 88b76f62, aucune modification non commitée. Rien n'a été exécuté en dehors de `bash -n` et de l'essai du suivi v2.

## 1. Empreintes
- Vérifié : pour 21 fichiers, `sha256sum` égal au compagnon : les 15 du tableau de la commande v6 (l.146-162), la commande v6 elle-même,
  et les 5 pièces de la v5 (commande, amorce v2, suivi v1, dépôt réduit v6, essai v2).
- Vérifié : les 15 empreintes du tableau sont exactes, contre-lecture 7 comprise (`4f05aa7f…`) ; celle de la v5 citée l.3 (`112de376…`)
  est exacte.
- Vérifié (git show) : au commit `d6821a29`, où l'essai v4 a été joué, l'amorce v4, le dépôt réduit v8, l'essai v4 et le suivi v2 ont
  les mêmes empreintes qu'aujourd'hui. Entre `d6821a29` et `88b76f62`, seuls changent la commande v6 et les journaux v3 et v4.
- Vérifié : `bash -n` sans erreur sur l'amorce v4 et l'essai v4 ; les 28 essais du suivi v2 passent.
- Les valeurs du journal v4 et celles citées par la commande (l.115-127) sont identiques : 62 passés, codes 10, 10, 12, 12, 12, 11, 14
  et 15, sonde seule au code 1, balayage à 0 fichier, 7 formes, 73 fichiers, commit réduit `fe3994c6…`, liste `98982cd5…`, paquet
  `81495e13…`.

## 2. État des remarques 1 à 13 de la contre-lecture 7
| n° | état | preuve |
|---|---|---|
| 1 | traitée | commande l.21 « cette v6 » ; tableau des empreintes l.142-162, exact. |
| 2a | traitée | commande l.26-33. |
| 2b | traitée, réserve N-12 (N-9 c) | commande l.59, 64, 69 ; suivi v2 l.130-137 ; essai l.99-107. |
| 3 | traitée, réserves N-1 et N-6 | règle « instance sortie », commande l.101-107. |
| 4a | traitée | amorce v4 l.104-107 ; journal v4 l.33. |
| 4b | traitée | commande l.101-105. |
| 4c | traitée | commande l.104-107 ; « improbable » supposé (`garde_depense_v3` non lu). |
| 5 | partiellement | exclusion avant `git add` (amorce l.59-65, 72 ; journal l.13, 17, 20-24) ; réserves N-1, N-3, N-8. |
| 6a | traitée | amorce l.68, l.98. |
| 6b | traitée | amorce l.87. |
| 6c | traitée | en-tête l.2-30 ; code 13 journalisé l.154. |
| 6d | traitée sous réserve | `pip==26.2.2` l.124 : existence non vérifiée, chemin non joué (N-8). |
| 6e | info, inchangé | déclaré. |
| 6f | traitée | commande l.81-83. |
| 7 | traitée | suivi v2 l.27-28, 52-55 ; essai l.35-43. |
| 8 | traitée | suivi v2 l.33-49 ; essais l.46-67 ; fonctionnement fermé gardé et déclaré. |
| 9a | traitée | essai l.70-78. |
| 9b | inchangé | déjà correct. |
| 9c | traitée, réserve N-2 | suivi v2 l.91-95, 107-110. |
| 9d | traitée | suivi v2 l.69-75 ; essai l.110-113 ; commande l.37-38, 41-42. |
| 9e | traitée, réserve N-2 | suivi v2 l.114-122 ; commande l.97-98, 110-111 ; essai l.90-96. |
| 10 | traitée | dépôt réduit v8 l.51. |
| 11 | traitée, réserve N-7 | script l.14, l.47 ; journal l.1. |
| 12a | traitée | cas arbre, sali, carte (journal l.27, 30, 31) ; code 13 déclaré non couvert ; le cas « carte » joue la vraie garde sur un PyTorch sans carte ; cas sain de la garde impossible ici. |
| 12b | traitée | nominal 62 passés et sonde seule avec jeton au code 1 : ensemble, preuve de `env -u` ; `pip` non couvert (déclaré). |
| 12c | déclarée non éprouvée | commande l.128-129. |
| 13 | partiellement | reformulation faite, base 64 ajoutée, deux lignes d'erreur gardées ; balayage aveugle aux dépôts git (N-4). |

## 3. Logique des fragments base 64 (suivi v2 l.33-41)
Raisonnement vérifié (pas d'essai exhaustif de son côté) : débuts (0, 2, 3) exacts, aucun fragment ne dépend d'un octet avant la
charge ; retrait de 3 caractères en fin conservateur, aucun fragment ne dépend d'un octet après ; faux refus sur texte sain
négligeable (fragment ≥ 12 caractères contenant une partie propre au jeton ; le préfixe constant n'est jamais seul). Limites (info) :
base 64 « url-safe » et base 64 coupée en lignes de 76 non détectées (l'amorce utilise `-w0`) ; un secret de 8 à 13 octets n'a aucun
fragment base 64 seul, sans avertissement ; les essais couvrent les trois alignements avec un seul suffixe.

## 4. Remarques nouvelles
- **N-1. Moyenne.** Commande l.101-107 et l.86-87 : le fichier de plus de 95 Mo exclu « reste sur le disque de l'instance », sans moyen
  de l'en sortir sans ssh ; la règle ordonne la destruction dès que l'état poussé est final, sans tenir compte des lignes « fichier de
  plus de 95 Mo exclu » : la destruction le perd. Correction : (a) journal contenant cette ligne → pas de destruction sans décision de la
  mère, et dire que le fichier est perdu à la destruction ; ou (b) découper puis pousser (`split -b 90M`). La commande ne dit pas si de
  tels fichiers sont attendus.
- **N-2. Moyenne.** Suivi v2 l.104 (et l.88) : `json.loads(out or "[]")` lit une sortie vide au code 0 comme une liste vide, donc
  `absente` rend vrai ; contredit la commande l.110-111 ; aucun essai. Correction : sortie vide = erreur ; exiger une liste non vide ou
  un témoin de lecture (instance connue d'une autre session) ; essai. Même défaut dans `instance()` l.88 (sortie vide → absente).
- **N-3. Moyenne.** Amorce l.67-93 : `pousser` n'est appelée que sous `if`, `||` ou `!`, donc `set -e` y est inactif : un échec de
  `git add`, `git commit`, `cp -a` (silencé par `|| true`), `mkdir` ou de l'écriture de l'état est ignoré ; le `push` envoie l'ancien
  HEAD, rend 0 et le journal écrit « pousse » à tort. Aucun artefact. Correction : `|| return 1` après `add` et `commit`, `cp` sans
  `|| true`, comparer après le `push` la tête locale à la tête distante (`ls-remote`) avant d'écrire « pousse » ; artefact (crochet
  `pre-commit` qui échoue, ou index verrouillé).
- **N-4. Moyenne.** Essai v4 l.64-69, journal l.66 : (a) « 0 fichier » sans témoin positif (`2>/dev/null` masque les erreurs de `grep`,
  un glob sans correspondance donne aussi 0) ; (b) `grep -F` ne voit rien dans les objets git compressés : dépôt distant et `.git`
  aveugles (messages de commit, historique) ; l'affirmation de la commande l.31 n'est prouvée que pour l'arbre de travail ; (c) pour un
  jeton `ghp_…`, la forme « adresse » est identique à la brute : l'encodage d'adresse n'est pas exercé. Correction : planter les formes
  dans des fichiers témoins et exiger le compte attendu ; balayer les objets (`git log -p --all` ou `cat-file --batch-all-objects`) ;
  ne pas masquer les erreurs ; reformuler « brute = adresse pour ce jeton ».
- **N-5. Moyenne.** Commande, étape 0 : les formes réelles de sortie de l'outil sont supposées ; un suivi fermé après la création laisse
  une instance louée illisible ; si `CONTROLE_IA_GITHUB_TOKEN_2` manque, `suivi creation` quitte avant de lire l'entrée alors que la
  création est peut-être partie, et `--env` envoie un jeton vide. Correction : à l'étape 0, avant la création, `suivi_vast_v2 instances`
  et `suivi_vast_v2 absente <identifiant bidon>` (gratuit : vérifie la variable, le chemin de l'outil et la forme réelle) ; interdire la
  création si le suivi échoue.
- **N-6. Mineure.** Commande l.91-92 et 101-107 : au code 10 aucun état n'est poussé et la règle lue à la lettre (« sinon : pas de
  destruction ») contredit l'étape 10 ; la ligne « poussee finale en echec (aucune course lancee…) » contient « echec » ; les codes hors
  10 à 14 (1, 2, 127, ≥ 128 : `pip`, `git worktree`, signaux) ne sont pas nommés. Correction : tableau « dernière ligne du journal →
  destruction ou non ».
- **N-7. Mineure.** Commande l.117-118 : aucun fichier de la liste du dépôt réduit n'a changé entre `d6821a29` et `88b76f62` : commit
  réduit, liste et paquet attendus identiques (paquet supposé stable) ; citer `fe3994c6…`, `98982cd5…`, `81495e13…` comme attendus, à
  reconfirmer au feu ; un écart exige un nouvel essai à blanc.
- **N-8. Mineure.** Amorce : (a) l.64 `find … 2>/dev/null` : si `find` échoue, le gros fichier est commité et la branche devient
  impoussable ; ne pas masquer, ou refuser le commit si un blob indexé dépasse 95 Mo ; (b) fichier déjà poussé qui grossit : le commit
  suivant le supprime de la tête (il reste dans l'historique ; l'étape 12 devrait lire l'historique) ; seuil `+97280k` juste ; (c)
  `pip==26.2.2` à vérifier sur l'index public ; (d) au code 14, la poussée finale refait 10 essais de 60 s (≈ 9 min de location) ; (e)
  `printf | grep -q` sous `pipefail` : faux négatif possible (SIGPIPE) au-delà de 64 Ko, improbable (info) ; (f) signaux et abandon par
  `set -e` non joués.
- **N-9. Mineure.** Suivi v2 : (a) l.93 `show instance` enveloppé en `{"instances": {…}}` → « forme inattendue », sûr mais inutilisable :
  déballer ; (b) l.72 `TimeoutExpired` non capturée ; (c) l.130-137 `creation` suppose du JSON pur, `2>&1` mêle les messages : extraire
  `new_contract` par motif sur le texte brut puis balayer.
- **N-10. Info.** Journal v4 l.25 : chemin absolu du bac de travail de la session, inoffensif.
- **N-11. Info.** Étape 6 (héritée) : écrire `( sleep $D; vastai destroy instance <ID> ) &`, sinon seul le dernier mot part en
  arrière-plan ; le PID tué est celui du sous-shell.
- **N-12. Info.** Aucun test précoce du jeton avant l'installation de `torch` (5 à 10 min) : un `git ls-remote` avant le venv avancerait
  le code 14.

## 5. Points d'attention (réponses)
`exit` dans le piège EXIT : code final conforme (10, 11, 12, 14, 15, 0 observés) ; abandon par `set -e` et signaux non joués. `set -e`
dans les fonctions sous `if` : N-3. Exclusion : N-1, N-8. Fuite du jeton : rien d'écrit ni d'affiché trouvé ; endroits déclarés
conformes ; seul manque, la preuve (N-4). R5 : sans jeton, carte, exclusion joués ; non joués : N-3, code 13, balayage sans témoin,
sortie vide du suivi. R10 : aucun arrêt par motif.

## 6. Verdicts
1. Commande v6 : scellable après corrections (N-1, N-5, N-6, N-7).
2. Amorce v4 : scellable après corrections (N-3 ; N-8).
3. Suivi v2 et son essai : scellable après corrections (N-2 ; N-9 ; § 3).
4. Dépôt réduit v8 : **scellable en l'état** (différences v6→v7→v8 limitées aux noms de l'amorce et à l'expression des secrets).
5. Essai à blanc v4 et journal : scellable après corrections (N-4).

Supposé : comportement réel de l'outil du loueur, existence de `pip` 26.2.2, stabilité du paquet, `garde_depense_v3`.

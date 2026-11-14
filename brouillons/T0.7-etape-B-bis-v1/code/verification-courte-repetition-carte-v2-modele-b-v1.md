rédigé sans vue des données de 7b

# Vérification courte des corrections de la répétition sur carte de l'étape B bis de T0.7 (note v2 du développeur) — modèle B, v1

- **Lecteur** : « modèle B », neuf (ni auteur du code, ni auteur des contre-lectures). **Heures (`date -u`)** : 2026-11-14, de 23:35 à 23:42 UTC.
- **Copie lue** : `/home/user/relecture-bbis-repetition-v2`, tête `5df3684f904f9df42ca0e0823f1afe04a1f12273` (vérifiée par `git rev-parse HEAD` ; arbre propre avant et après).
- **Lu** : les deux contre-lectures du modèle C (conformité `7d09be3f…`, sûreté `f3851b15…`, empreintes compagnes égales), `rapport-developpeur-repetition-carte-v2.md` (empreinte compagne égale), le différentiel `c880f36f` → `1abc4364`, et en entier `scripts/repetition_carte_bbis_v1.py` (`e032499a…`), `scripts/amorce_repetition_bbis_v1.sh` (`67172970…`), `scripts/lancer_repetition_bbis_v1.sh` (`d61a1120…`) ; de `tests/test_repetition_bbis_v1.py` (`aaea8301…`), la liste des 23 essais et les essais des gardes shell et de la relecture (l. 289-520, 714-738) ; de `src/controle_ia/t07bbis/registre_bbis_v1.py`, les seules lignes d'import, `garde_depense` et la liste des instances. Les quatre empreintes égalent celles du § 4 de la note v2 ; le code est identique entre `1abc4364` et la tête.
- **Fait de mon côté** : le rejeu des essais ; une épreuve des sous-commandes de session du lanceur contre un **faux outil jetable** (jamais le vrai `vastai`, aucun réseau), dans un dossier temporaire supprimé ensuite ; quelques appels des fonctions pures (identifiants, échéance, garde de commande), sans fichier d'octets.
- **À déclarer** : (a) le rejeu a écrit le dossier temporaire habituel de pytest (`/tmp/pytest-of-root/pytest-104`, 60 sous-dossiers), que j'ai supprimé, et une sortie d'essais dans le dossier brouillon de la session, supprimée aussi ; ce dossier brouillon est partagé : en vérifiant ma suppression j'ai affiché **les noms** des fichiers qui s'y trouvent (aucun ouvert), et ma sortie s'appelait `essais.txt` : si un fichier de ce nom y existait avant, je l'ai écrasé (je ne peux pas le savoir) ; (b) rien n'a été écrit dans la copie hors de ce rapport et de son empreinte ; (c) je n'ai pas ouvert `.claude/hooks/garde_calcul.py` (hors des fichiers donnés) : je ne dis donc rien de la forme exacte que la garde de calcul accepte pour la ligne de création. Rien lu sous `diag/`, `runs/`, `donnees/`, `essai/` ; aucune sortie de 7a, 7b, T0.7, P3-bis ; aucune clé ; aucun `git fetch`, commit, push. **Aucun refus de permission ni du classifieur.**

## Verdict : **feu possible après corrections** (deux couples, par consigne seulement : aucun changement de code, aucun commit neuf)

Les corrections demandées par les deux contre-lectures sont faites et éprouvées ; le code de la course est inchangé ; 132 essais passent. Deux trous restent, que le code ne ferme pas et que la commande de la mère ne dit pas : le plafond de 3 USD n'est pas garanti si le prix de l'instance créée dépasse le prix `P` qui a servi à fixer l'échéance (C-1), et la liste privée des instances reste sur disque dans un chemin de refus (C-2). Les deux se ferment par une ligne de consigne chacune, avec le code tel qu'il est.

## (1) Constats des deux contre-lectures : traités

| constat d'origine | état | ce que j'ai vu |
|---|---|---|
| sûreté **M1** (60671759, garde positive) | **traité, par code** | `detruire` n'imprime la ligne `GO_ID=… vastai destroy instance N -y` que pour le `new_contract` lu dans le fichier de création, accepté par `exiger_identifiant`, **puis** trouvé une seule fois dans la liste avec l'étiquette `bbis-t07-repetition-v1`. Protégées (lues sur le module) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, **60671759**. Éprouvé par moi : création portant 60671759 → refus ; instance étiquetée → ligne avec `-y` ; témoin 60671759 → refus. La part « consigne » (60671759 dans `registres/etat.md` avant le geste 4) est écrite dans la commande. |
| sûreté **m1** (entiers ASCII) | **traité** (répétition seulement) | `^[1-9][0-9]*$` en ASCII, comparaison en entiers, absence comprise. Éprouvé : `060670453`, chiffres pleine largeur, espace de tête, `True`, `0`, `-5`, `1e3` refusés. La garde de la course (`str.isdigit`, chaînes) reste telle quelle : déclaré au § 3 de la note, sans effet ici (la répétition n'appelle pas `exiger_identifiant_a_detruire` ni `exiger_absence` de la course). |
| sûreté **m4** (offre par programme, relecture) | **traité, avec le reste C-1** | `offre-depuis-recherche` : clés lues, clé absente → refus, « A100 SXM4 », une carte, ≥ 79 000 Mo, prix ≤ 1,40 ; `offre` exige « A100 SXM4 80GB » exactement ; `relire` après création. L'amorce exige `A100-SXM4-80GB` sur la machine (PCIe 40 Go refusée, essai). **Reste** : voir C-1 et r-2. |
| conformité **M-5** (plafond strict) | **traité** | `cout < PLAFOND_USD` ; échéance du geste 3 recalculée par moi : 2,91 ; 2,91 ; 2,90 ; 2,89 ; 2,88 USD au plus à 1,09 ; 1,12 ; 1,15 ; 1,30 ; 1,40 USD/h. |
| sûreté **M2**, **M2 bis** (fins sans filet) | **fermées ou déclarées** | refus avant la minuterie : trois `DELETE` puis « stopped » demandés par l'instance (jamais jugés) ; fin voulue : `sleep infinity`, minuterie armée, aucun « stopped » ; piège de sortie posé après la minuterie. Déclarés au § 3 : identifiant d'instance illisible, mort brutale du processus, minuterie non prouvée sur le service réel (d'où l'arrêt dur de la mère à l'échéance − 5 min, écrit au geste 6). |
| conformité **M-4** (durée contre échéance) | **traité** | budget = échéance − 15 min, `timeout` sur installation, essais, carte ; code 10 ; état partiel écrit avant les contrôles sur processeur. |
| conformité **M-1** (R5, gardes shell) | **traité pour l'essentiel** | blocs marqués, chacun joué avec cas sain et artefacts (machine, dépôt, installation 5/6/10, essais 7/10/2, carte 0/8/9/2/4/10, budget, fins, refus). **Reste mineur** : r-3. |
| sûreté **M3**, **m3** (fichiers privés) | **traité, avec le reste C-2** | `umask 077`, dossier `mktemp -d`, champs utiles seuls, alerte sans valeur sur un motif de jeton (éprouvé : jeton factice dans la liste → « ALERTE », jamais la valeur), suppression. Portée et révocation du jeton : consignes, écrites. |
| sûreté **M4** (URL du distant) | **traité par consigne** | geste 0 : `git remote get-url origin`, liste de ce qui part, puis poussée. L'amorce pousse vers l'adresse codée en dur `…/controle-ia-travail.git`. |
| sûreté **m2**, **m5**, **m7**, **m8**, **m6** | **traités** | image nommée dans le feu (refus sinon), `GH_TOKEN` présent par son nom (refus sinon), versions et aides de l'outil avant le geste 1, cumul de la répétition seule, journaux lus avant destruction. |
| conformité **M-2**, **m-1** à **m-4**, **M-3**, 3a | **traités ou déclarés** | errata (87, 132, `e032499a…`), tableau des codes avec 10, « 3 jamais émis », refus avant minuterie ; M-3 et 3a au § 3. |

## (2) Code de la course inchangé — confirmé

`git diff bbc2e1c8 1abc4364 -- src/ scripts/amorce_bbis_v1.sh scripts/lancer_bbis_v1.sh tests/test_t07bbis_*.py` : **vide** (0 octet). Le différentiel `c880f36f` → `1abc4364` ne touche que les quatre fichiers de la répétition et les deux contre-lectures avec leurs empreintes.

## (3) Essais — confirmé

Commande demandée, dans la copie (avec `PYTHONDONTWRITEBYTECODE=1` en plus, pour ne rien écrire dans la copie) : **132 passed, 4 warnings in 181,07 s**, code 0 (les quatre avertissements de `fork()` déjà connus).

## (4) Commande de la mère (§ 2 de la note v2)

- **Jeton par son nom** : oui (`-e GH_TOKEN=\$GH_TOKEN` littéral dans la ligne imprimée, garde `[ -n "${GH_TOKEN:-}" ]`) ; aucune valeur écrite.
- **Destruction avec `-y`, absence prouvée** : oui (geste 9 ; éprouvé : instance encore listée → « absence non prouvée », code 2).
- **Aucune instance d'une autre session touchable** : oui par le code (les sept identifiants refusés, étiquette exigée) ; la ligne de destruction n'est jamais écrite à la main.
- **URL du distant avant toute poussée** : oui (geste 0), par lecture de la mère, non par programme.
- **Jouable telle quelle** : oui, le lanceur côté session tourne avec le `python3` du système (bibliothèque standard seule, vérifié par lecture des imports) ; le calcul du geste 3 rend bien les durées annoncées (à la minute près : 115 et 100 min à 1,15 USD/h, la note dit 116 et 101). Deux remarques de jeu : r-1, r-4.

## Corrections demandées (couples)

- **C-1 (majeur, consigne) ↔ plafond strict sous 3 USD.** `relire` accepte tout prix de l'instance dans ]0 ; 1,40], sans le comparer au prix `P` de la recherche, alors que l'échéance (et l'arrêt dur de la mère, échéance − 5 min) est calculée avec `P`. Éprouvé : `P` = 1,09, échéance à 118 min, instance relue à 1,38 USD/h → « INSTANCE CONFORME » ; la garde de commande, rejouée à 1,38 avec la même échéance, rend « 3,46 USD au plus : refus ». Le cas est celui que la contre-lecture de sûreté nommait (prix changé par l'hôte entre la recherche et la création) ; un écart de quelques centimes (disque de 60 Go) est, lui, attendu à chaque fois. La garde de dépense du geste 6 ne le rattrape que si le cumul est compté au prix réel.
  **Correction (une ligne au geste 5, code inchangé)** : lire le prix `D` affiché par `relire` ; si `D > P`, rejouer aussitôt `$PY scripts/repetition_carte_bbis_v1.py garde-commande "$ECH" D "<feu écrit>" "$(date +%s)"` : « COMMANDE PERMISE » → continuer, avec `D` (et non `P`) dans le cumul et dans `depense` au geste 6 ; « REFUS » → geste 9 aussitôt (ou arrêt dur de la mère avancé à la durée que le refus affiche pour `D`, écrite au registre des dépenses).
- **C-2 (mineur, consigne) ↔ fichiers privés supprimés.** `verifier-destruction` lit la liste des instances **avant** que le fichier de création soit contrôlé ; si ce fichier est absent, illisible ou porte une instance protégée, le refus sort avant la suppression : `sortie.json` (la liste entière, qui peut porter l'environnement de l'instance, donc le jeton) et `erreur.txt` restent dans le dossier `tmp.*` (mode 600, dossier 700). Éprouvé deux fois (création absente ; création portant 60671759). `relire` et `detruire` ne sont pas touchés (le lanceur contrôle la création avant de lire la liste).
  **Correction (une ligne au geste 9)** : ne jouer `verifier-destruction` qu'après un `detruire CREATION.json` accepté avec le même fichier (c'est l'ordre de la commande) ; après tout « REFUS » de `verifier-destruction` qui n'est pas « absence non prouvée », supprimer sans l'afficher le dossier `tmp.*` du jour sous `${TMPDIR:-/tmp}` qui contient `sortie.json`, et le consigner.

## Réserves (aucune correction exigée avant le feu)

- **r-1** : `creation` ne cherche pas de motif de jeton dans `CREATION.json` ; le geste 10 dit « aucun ne porte de valeur privée » sans que rien ne le prouve. Écrit sous `umask 077`, jamais affiché : le supprimer au geste 10 comme écrit, et ne pas l'afficher avant.
- **r-2** : `relire` ne refuse pas une instance dont la clé `gpu_ram` manque (elle ne juge la mémoire que si la clé est là) ; la phrase du § 3 « toute forme autre rend un refus » est donc vraie sauf pour cette clé. Sans conséquence : l'offre exige la clé, et l'amorce exige `A100-SXM4-80GB` sur la machine.
- **r-3 (R5)** : restent sans cas sain ni artefact joués, dans l'amorce : la fenêtre d'échéance ]maintenant ; + 3 h] et l'identifiant d'instance illisible **comme conditions** (la fonction `refus` est jouée, pas les deux lignes qui l'appellent), « environnement virtuel » (code 6), « traces non poussées » en fin (code 4), et « dépôt injoignable » au contrôle de la branche de sortie (l'injoignable est joué au clonage). Lignes simples, relues sans défaut ; la répétition les exerce sur la machine.
- **r-4** : le geste 2 ne dit pas comment la mère voit les offres pour « choisir l'identifiant » sans retaper : afficher par programme les seules clés `id` et `dph_total` du fichier de recherche. Je n'ai pas vérifié que la garde de calcul accepte la ligne de création jouée dans `( umask 077; … > CREATION.json )` (voir « À déclarer », c).
- **r-5** : la fin voulue laisse la carte facturée jusqu'au geste 9 ou à l'échéance (déclaré) : le respect des « 15 minutes » des gestes 8 et 9 est la seule économie, le plafond n'en dépend pas.

## Ce que cette vérification ne dit pas

Rien sur le service réel (formes des sorties de l'outil, `DELETE` par la clé de conteneur, poussée depuis un clone partiel), ni sur la garde de calcul de la session, ni sur les durées du devis : c'est l'objet de la répétition. Les essais des gardes shell ont été lus et rejoués, non réécrits.

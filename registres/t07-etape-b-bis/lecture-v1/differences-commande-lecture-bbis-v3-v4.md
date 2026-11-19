# Différences entre la commande de lecture version 3 et la version 4 (forme en scripts) — apprentissage des sondes sur la tâche (étape B bis de T0.7)

Écrit par le préparateur (Fable 5.2), le 2026-11-19, par le programme qui a écrit la version 4 et ses scripts à partir de la version 3. Chaque script est le bloc de la version 3, auquel le programme n'applique que les substitutions listées ici, chacune exigée une seule fois ; chaque passage de prose changé figure une seule fois dans la version 3.

- Version 3 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3` (reste, R12).
- Version 4 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v4.md`, `6dde01b0bc02ea8587fc217527a22a4c1588456df87381c548ea1b7afc4b1c8c`.
- Fondement : troisième complément au mandat du préparateur (`complement-3-mandat-preparateur-lecture-bbis-v1.md`, accordé par la session mère, message du 2026-11-18 à 23:49:24Z, R-3540).

## 1. Les scripts et leurs empreintes

| script | empreinte |
|---|---|
| `scripts/lecture-bbis-v4/1-1-depot-et-tetes.sh` | `64d4308bc618c5deea7ddd61b61f77d035e1aa0d9deed1bce64b98c5b297e727` |
| `scripts/lecture-bbis-v4/1-2-montage-de-l-arbre.sh` | `a6ef60db69ce9d54465883fc477564380a5a631a89bdce32e31be82fd9ec94b2` |
| `scripts/lecture-bbis-v4/1-3-entrees.sh` | `6c1d7df4ad617e18457a90c9722b188721940676c7584a7aca314f6620170050` |
| `scripts/lecture-bbis-v4/1-4-code-et-textes.sh` | `34c027463f42f907fe26ff54bd38cde7ff362060724894229bf76e455a1e631a` |
| `scripts/lecture-bbis-v4/2-preuve-anteriorite-et-entree-conjointe.sh` | `1f459ed032ee07ada1e751d7eeb0d30eefd1ff98a23a698589a9ae0a4961096e` |
| `scripts/lecture-bbis-v4/4-1-commit-local.sh` | `06cf2c6b60bde1ce6c80aaddf5642aef8920c23e395ef9cf9c7b17b48f55b86a` |
| `scripts/lecture-bbis-v4/4-1-conductrice-preuve-et-branche.sh` | `660de300bf930a6dfdea3ccde03e1197eb1d7a608a9f4a19c7aaa4b3c92920c0` |
| `scripts/lecture-bbis-v4/4-2-releve-avant-lancement.sh` | `8ca57406cd0b0e41db188d0b1e751a44945ad0d35168bed5d5ddf73f8e1b4d89` |
| `scripts/lecture-bbis-v4/5-1-bis-attente.sh` | `50acaf640379e9b0b050c80c1a702efeece1565de4190c3021ad0eb53670f863` |
| `scripts/lecture-bbis-v4/5-1-lancement.sh` | `a9b7af4c66b71dc7a94ae8b9959bcd8ba8a6dd00f998e637a1e72e66eece4590` |
| `scripts/lecture-bbis-v4/5-2-constat-de-forme-pour-le-juge.sh` | `b10c6624458a12f79a120cafae3d44c2a70fab1999f2990d2a9652e292c4e0f5` |
| `scripts/lecture-bbis-v4/5-2-motif-non-consommee.sh` | `35ea92a1501b7e48b4b41a4d8a491409890db45d40a53462ea405130ee931cf2` |
| `scripts/lecture-bbis-v4/5-2-releve-apres-lancement.sh` | `f09b2838d8c123ced30cb086184e4a21f1b38a3a410c367921b7810144a91a2c` |
| `scripts/lecture-bbis-v4/5-4-sorties-portees-et-ligne-de-lecture.sh` | `e0559e5fb39787c06d607811a24ea90530858dba0a3e3e365c2b152972b63299` |
| `scripts/lecture-bbis-v4/5-5-preuve-apres-coup-sur-ordre-ecrit.sh` | `a913bb5254506ac23ec1aa2d2aa0a9c471e117f9d0d820666dcbaca4ed86e438` |
| `scripts/lecture-bbis-v4/commun.sh` | `83195d25d73f207d90b03379641eec6583b634ec72424445787707305bc2dbfa` |

## 2. Contrôles changés, ajoutés ou retirés

**Aucun, hors le rejeu du relevé des têtes.** Preuve, bloc par bloc, au § 3 : pour chaque bloc, le nombre de lignes de contrôle (`egal`, `vrai`, `dire`, `conclure`, `avant`, messages `echo`) du bloc et du script, et la liste des lignes de contrôle qui diffèrent.

Ce que la forme ajoute, et qui n'est pas un contrôle de la lecture :
- le relevé des têtes et ses trois fichiers de travail portent un numéro ; les § 1.2 et § 2 lisent le relevé de plus grand numéro (condition 2) ;
- la garde `neuf`, qui existait pour les relevés, couvre aussi cinq fichiers de travail que la version 3 écrivait sans garde (condition 3 : aucune réécriture) ;
- la tête donnée par la conductrice est lue dans un fichier, avec trois refus de forme (fichier absent, ligne absente ou en double, valeur qui n'est pas un identifiant de commit) ; le numéro du lancement est un argument, refusé s'il n'est pas `1` (la version 3 écrivait `N=1` dans chaque bloc) ;
- le script `5-2-motif-non-consommee.sh` porte une ligne que la version 3 écrivait dans sa prose, et refuse de partir hors de l'état que cette prose nommait ;
- trois noms neufs : le dossier de travail, l'arbre de lecture, sa branche locale.

**Suppressions et réécritures : aucune.** Aucun script ne contient de commande de suppression de fichier, de dossier, d'arbre de travail ni de branche. Les seules écritures dans un fichier qui existe déjà sont les deux ajouts en fin de fichier du § 5.4 (ligne `LECTURE-BBIS` au registre propre, par la fonction du code ; seconde ligne du journal), qui étaient dans la version 3 et que le texte scellé veut.

## 3. Pour chaque bloc de la version 3, le script qui le porte, et l'égalité de fond

### Bloc « fichier des paramètres » → `commun.sh`

Le texte en ligne que le bloc de la version 3 écrivait dans le fichier des paramètres devient le fichier commun. Substitutions :

- E : dossier de travail neuf ; celui de la version 3 reste en place et n'est ni lu ni touché
- E : arbre de lecture neuf sous un nom neuf
- C1 : la tête donnée par la conductrice entre par un fichier que l'opérateur écrit par l'outil d'écriture de fichiers ; elle est lue, non exécutée
- E : branche locale de l'arbre de lecture sous un nom neuf
- trois fonctions ajoutées en fin de fichier : `numero_neuf_du_releve_des_tetes`, `dernier_releve_des_tetes` (C2), `exiger_numero` (C1).

Différence, ligne à ligne :

~~~~diff
--- version 3, fichier des paramètres
+++ commun.sh
@@ -0,0 +1,2 @@
+# Fichier commun des scripts de la commande de lecture, version 4 (étape B bis de T0.7) : paramètres et fonctions.
+# Relu par chaque script. Porte le fichier des paramètres de la version 3 ; ne supprime rien, ne réécrit rien.
@@ -2,2 +4,2 @@
-T=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis
-ARBRE="$T/arbre-de-lecture-v1"
+T=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis-v4
+ARBRE="$T/arbre-de-lecture-v4"
@@ -11 +13,5 @@
-TETE_TRAVAIL=REMPLACER_PAR_LA_TETE_DONNEE_PAR_LA_CONDUCTRICE
+FICHIER_DE_LA_CONDUCTRICE="$T/parametres-conductrice-v4.txt"
+if [ ! -f "$FICHIER_DE_LA_CONDUCTRICE" ]; then echo "$FICHIER_DE_LA_CONDUCTRICE absent : l'opérateur l'écrit par l'outil d'écriture de fichiers ; arrêt"; exit 1; fi
+if [ "$(grep -c '^TETE_TRAVAIL=' "$FICHIER_DE_LA_CONDUCTRICE")" != 1 ]; then echo "$FICHIER_DE_LA_CONDUCTRICE : une ligne TETE_TRAVAIL=, et une seule, attendue ; arrêt"; exit 1; fi
+TETE_TRAVAIL="$(grep '^TETE_TRAVAIL=' "$FICHIER_DE_LA_CONDUCTRICE" | cut -d= -f2)"
+if ! printf '%s' "$TETE_TRAVAIL" | grep -q -E '^[0-9a-f]{40}$'; then echo "TETE_TRAVAIL : 40 caractères hexadécimaux attendus ; arrêt"; exit 1; fi
@@ -27,0 +34 @@
+BRANCHE_LOCALE_ARBRE=lecture/bbis-arbre-de-lecture-v4
@@ -36,0 +44,4 @@
+# -- forme de la version 4
+numero_neuf_du_releve_des_tetes() { local k=1; while [ -e "$T/releve-mise-en-place-$k.txt" ]; do k=$((k+1)); done; echo "$k"; }
+dernier_releve_des_tetes() { local k=1; while [ -e "$T/releve-mise-en-place-$((k+1)).txt" ]; do k=$((k+1)); done; echo "$T/releve-mise-en-place-$k.txt"; }
+exiger_numero() { if [ "$1" != 1 ]; then echo "numéro du lancement « $1 » : cette version ne joue que le lancement 1, donné en argument ; arrêt"; exit 1; fi; }
~~~~

### Bloc « étape 0 » de la conductrice

Pas de script : la fusion et le journal sont faits ; les gestes qui restent sont trois lignes simples, écrites dans la commande (§ 0). Voir le passage « état laissé et étape 0 » au § 4.

### Bloc « § 1.1 » → `1-1-depot-et-tetes.sh`

- Lignes du bloc : 27 ; lignes du script, hors en-tête : 27.
- Lignes de contrôle : 16 dans le bloc, 16 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 2.
  Ce sont les lignes touchées par les substitutions ci-dessous (noms de fichiers numérotés, nom du relevé lu) ; leur libellé `CONFORME` / `DEFAUT`, leur valeur attendue et leur commande ne changent pas : voir la différence.
- Substitutions :
  - C2 : relevé sous un nom numéroté, jamais réécrit ; C3 : fichiers de travail neufs
  - C2, C3 : nom numéroté
  - C2, C3 : nom numéroté
  - C2, C3 : noms numérotés
  - C2, C3 : nom numéroté
  - C2, C3 : noms numérotés

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 1.1
+++ 1-1-depot-et-tetes.sh
@@ -1,2 +1,8 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-R="$T/releve-mise-en-place.txt"; neuf "$R"
+#!/bin/bash
+# § 1.1 — dépôt à histoire complète, branches présentes, têtes (rejouable : relevé numéroté)
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 1.1 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-1-depot-et-tetes.sh
+. "$(dirname "$0")/commun.sh"
+K="$(numero_neuf_du_releve_des_tetes)"; R="$T/releve-mise-en-place-$K.txt"; neuf "$R"
+neuf "$T/tetes-du-distant-$K.txt"; neuf "$T/noms-distants-$K.txt"; neuf "$T/noms-locaux-$K.txt"
@@ -17,5 +23,5 @@
-if git ls-remote --heads origin > "$T/tetes-du-distant.txt" 2>/dev/null; then
-  egal "tête des sorties sur le distant" "$TETE_SORTIES" "$(awk '$2=="refs/heads/donnees/t07-etape-b-bis-v2"{print $1}' "$T/tetes-du-distant.txt")"
-  awk '{print $1" "$2}' "$T/tetes-du-distant.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
-  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux.txt"
-  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
+if git ls-remote --heads origin > "$T/tetes-du-distant-$K.txt" 2>/dev/null; then
+  egal "tête des sorties sur le distant" "$TETE_SORTIES" "$(awk '$2=="refs/heads/donnees/t07-etape-b-bis-v2"{print $1}' "$T/tetes-du-distant-$K.txt")"
+  awk '{print $1" "$2}' "$T/tetes-du-distant-$K.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants-$K.txt"
+  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux-$K.txt"
+  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants-$K.txt" "$T/noms-locaux-$K.txt" | wc -l | tr -d ' ')"
~~~~

### Bloc « § 1.2 » → `1-2-montage-de-l-arbre.sh`

- Lignes du bloc : 13 ; lignes du script, hors en-tête : 12.
- Lignes de contrôle : 6 dans le bloc, 6 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 2.
  Ce sont les lignes touchées par les substitutions ci-dessous (noms de fichiers numérotés, nom du relevé lu) ; leur libellé `CONFORME` / `DEFAUT`, leur valeur attendue et leur commande ne changent pas : voir la différence.
- Substitutions :
  - C2 : le relevé lu est celui de plus grand numéro
  - E : branche locale sous un nom neuf, l'ancienne restant en place

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 1.2
+++ 1-2-montage-de-l-arbre.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-grep -q "CONCLUSION : conforme" "$T/releve-mise-en-place.txt" || { echo "§ 1.1 non conforme : arrêt"; exit 1; }
+#!/bin/bash
+# § 1.2 — arbre de lecture monté, entrées extraites par chemins nommés
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 1.2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-2-montage-de-l-arbre.sh
+. "$(dirname "$0")/commun.sh"
+grep -q "CONCLUSION : conforme" "$(dernier_releve_des_tetes)" || { echo "§ 1.1 non conforme : arrêt"; exit 1; }
@@ -4 +9 @@
-cd "$DEPOT" && git worktree add -q -b lecture/bbis-arbre-de-lecture-v1 "$ARBRE" "$TETE_TRAVAIL" || { echo "montage refusé : arrêt"; exit 1; }
+cd "$DEPOT" && git worktree add -q -b "$BRANCHE_LOCALE_ARBRE" "$ARBRE" "$TETE_TRAVAIL" || { echo "montage refusé : arrêt"; exit 1; }
~~~~

### Bloc « § 1.3 » → `1-3-entrees.sh`

- Lignes du bloc : 69 ; lignes du script, hors en-tête : 68.
- Lignes de contrôle : 16 dans le bloc, 16 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C3 : fichiers de travail neufs, jamais réécrits

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 1.3
+++ 1-3-entrees.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-R="$T/releve-entrees.txt"; neuf "$R"
+#!/bin/bash
+# § 1.3 — entrées présentes, à l'empreinte des branches et des lignes de registre ; rien de la liste « Jamais »
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 1.3 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-3-entrees.sh
+. "$(dirname "$0")/commun.sh"
+R="$T/releve-entrees.txt"; neuf "$R"; neuf "$T/attendus.txt"; neuf "$T/presents.txt"; neuf "$T/attendus-noms.txt"
~~~~

### Bloc « § 1.4 » → `1-4-code-et-textes.sh`

- Lignes du bloc : 47 ; lignes du script, hors en-tête : 46.
- Lignes de contrôle : 11 dans le bloc, 11 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions : aucune hors la première ligne (le fichier relu).

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 1.4
+++ 1-4-code-et-textes.sh
@@ -1 +1,6 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
+#!/bin/bash
+# § 1.4 — module, textes scellés, fiches, registre voisin
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 1.4 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/1-4-code-et-textes.sh
+. "$(dirname "$0")/commun.sh"
~~~~

### Bloc « § 2 » → `2-preuve-anteriorite-et-entree-conjointe.sh`

- Lignes du bloc : 73 ; lignes du script, hors en-tête : 73.
- Lignes de contrôle : 42 dans le bloc, 43 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 1.
  Ce sont les lignes touchées par les substitutions ci-dessous (noms de fichiers numérotés, nom du relevé lu) ; leur libellé `CONFORME` / `DEFAUT`, leur valeur attendue et leur commande ne changent pas : voir la différence.
- Substitutions :
  - C2 : le relevé des têtes lu est celui de plus grand numéro ; les deux autres relevés comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 2
+++ 2-preuve-anteriorite-et-entree-conjointe.sh
@@ -1,2 +1,8 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-for f in releve-mise-en-place releve-entrees releve-code-et-textes; do grep -q "CONCLUSION : conforme" "$T/$f.txt" || { echo "$f non conforme : arrêt"; exit 1; }; done
+#!/bin/bash
+# § 2 — preuve d'antériorité et preuve d'entrée conjointe, relevées à part
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/2-preuve-anteriorite-et-entree-conjointe.sh
+. "$(dirname "$0")/commun.sh"
+grep -q "CONCLUSION : conforme" "$(dernier_releve_des_tetes)" || { echo "releve-mise-en-place non conforme : arrêt"; exit 1; }
+for f in releve-entrees releve-code-et-textes; do grep -q "CONCLUSION : conforme" "$T/$f.txt" || { echo "$f non conforme : arrêt"; exit 1; }; done
~~~~

### Bloc « § 4.1, bloc de l'opérateur » → `4-1-commit-local.sh`

- Lignes du bloc : 6 ; lignes du script, hors en-tête : 5.
- Lignes de contrôle : 2 dans le bloc, 2 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions : aucune hors la première ligne (le fichier relu).

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 4.1, bloc de l'opérateur
+++ 4-1-commit-local.sh
@@ -1 +1,6 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
+#!/bin/bash
+# § 4.1 — entrées commitées localement dans l'arbre de lecture (lecteur-opérateur)
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 4.1, bloc de l'opérateur » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-commit-local.sh
+. "$(dirname "$0")/commun.sh"
~~~~

### Bloc « § 4.1, bloc de la conductrice » → `4-1-conductrice-preuve-et-branche.sh`

- Lignes du bloc : 5 ; lignes du script, hors en-tête : 5.
- Lignes de contrôle : 0 dans le bloc, 0 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le dépôt est nommé par le fichier commun
  - E : branche locale sous un nom neuf ; nom du distant inchangé, pris au fichier commun
  - C1 : nom pris au fichier commun

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 4.1, bloc de la conductrice
+++ 4-1-conductrice-preuve-et-branche.sh
@@ -1 +1,7 @@
-cd /home/user/controle-ia-travail
+#!/bin/bash
+# § 4.1 — gestes de la conductrice entre les deux temps : preuve commitée et poussée, branche de l'arbre de lecture poussée
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 4.1, bloc de la conductrice » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-1-conductrice-preuve-et-branche.sh
+. "$(dirname "$0")/commun.sh"
+cd "$DEPOT" || exit 1
@@ -4,2 +10,2 @@
-git push origin lecture/bbis-arbre-de-lecture-v1:refs/heads/claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
-git ls-remote --heads origin claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture     # attendu : la tête rendue par l'opérateur
+git push origin "$BRANCHE_LOCALE_ARBRE:refs/heads/$BRANCHE_DISTANTE_ARBRE"
+git ls-remote --heads origin "$BRANCHE_DISTANTE_ARBRE"     # attendu : la tête rendue par l'opérateur
~~~~

### Bloc « § 4.2 » → `4-2-releve-avant-lancement.sh` (argument `1`)

- Lignes du bloc : 51 ; lignes du script, hors en-tête : 50.
- Lignes de contrôle : 40 dans le bloc, 40 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3
  - C3 : fichier de travail neuf, jamais réécrit

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 4.2
+++ 4-2-releve-avant-lancement.sh
@@ -1,3 +1,8 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1
-R="$T/releve-avant-lancement-$N.txt"; neuf "$R"; neuf "$T/run-lecture-$N.txt"
+#!/bin/bash
+# § 4.2 — relevé d'avant lancement
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 4.2 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/4-2-releve-avant-lancement.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"
+R="$T/releve-avant-lancement-$N.txt"; neuf "$R"; neuf "$T/run-lecture-$N.txt"; neuf "$T/commit-local-noms.txt"
~~~~

### Bloc « § 5.1 » → `5-1-lancement.sh` (argument `1`)

- Lignes du bloc : 20 ; lignes du script, hors en-tête : 19.
- Lignes de contrôle : 3 dans le bloc, 3 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.1
+++ 5-1-lancement.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1
+#!/bin/bash
+# § 5.1 — lancement détaché du module de lecture
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.1 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-lancement.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"
~~~~

### Bloc « § 5.1 bis » → `5-1-bis-attente.sh` (argument `1`)

- Lignes du bloc : 8 ; lignes du script, hors en-tête : 7.
- Lignes de contrôle : 5 dans le bloc, 5 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.1 bis
+++ 5-1-bis-attente.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1
+#!/bin/bash
+# § 5.1 bis — relevé de l'état du processus, sans jamais l'arrêter
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.1 bis » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-1-bis-attente.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"
~~~~

### Bloc « § 5.2, relevé » → `5-2-releve-apres-lancement.sh` (argument `1`)

- Lignes du bloc : 48 ; lignes du script, hors en-tête : 47.
- Lignes de contrôle : 18 dans le bloc, 18 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.2, relevé
+++ 5-2-releve-apres-lancement.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1
+#!/bin/bash
+# § 5.2 — fin du lancement : sortie gardée et scellée, relevé rendu à la conductrice
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.2, relevé » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-releve-apres-lancement.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"
~~~~

### Bloc « § 5.2, constat de forme » → `5-2-constat-de-forme-pour-le-juge.sh` (argument `1`)

- Lignes du bloc : 34 ; lignes du script, hors en-tête : 33.
- Lignes de contrôle : 10 dans le bloc, 10 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.2, constat de forme
+++ 5-2-constat-de-forme-pour-le-juge.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
+#!/bin/bash
+# § 5.2 — constat de forme, pour le juge seul (écrit et scellé sans être affiché)
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.2, constat de forme » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-constat-de-forme-pour-le-juge.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
~~~~

### Bloc « § 5.4 » → `5-4-sorties-portees-et-ligne-de-lecture.sh` (argument `1`)

- Lignes du bloc : 25 ; lignes du script, hors en-tête : 24.
- Lignes de contrôle : 6 dans le bloc, 6 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.4
+++ 5-4-sorties-portees-et-ligne-de-lecture.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
+#!/bin/bash
+# § 5.4 — état « écrit » : sorties portées, ligne LECTURE-BBIS, journal
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.4 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-4-sorties-portees-et-ligne-de-lecture.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
~~~~

### Bloc « § 5.5 » → `5-5-preuve-apres-coup-sur-ordre-ecrit.sh` (argument `1`)

- Lignes du bloc : 10 ; lignes du script, hors en-tête : 9.
- Lignes de contrôle : 4 dans le bloc, 4 dans le script ; lignes de contrôle du bloc absentes du script à l'octet : 0.
- Substitutions :
  - C1 : le numéro du lancement entre par un argument simple, exigé égal à 1 comme dans la version 3

Différence, ligne à ligne (la première ligne du bloc, qui relisait le fichier des paramètres, est portée par l'en-tête du script) :

~~~~diff
--- version 3, bloc § 5.5
+++ 5-5-preuve-apres-coup-sur-ordre-ecrit.sh
@@ -1,2 +1,7 @@
-. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
-N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
+#!/bin/bash
+# § 5.5 — preuve après coup, À NE JOUER QUE SUR ORDRE ÉCRIT DE LA CONDUCTRICE
+# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
+# seulement, le bloc « § 5.5 » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
+# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-5-preuve-apres-coup-sur-ordre-ecrit.sh 1
+. "$(dirname "$0")/commun.sh"
+N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
~~~~

### Ligne de la prose du § 5.2 → `5-2-motif-non-consommee.sh` (argument `1`)

La version 3 écrivait cette ligne dans une puce. Le script la porte à l'octet, précédée du numéro du lancement et du refus hors de l'état « non consommée ».

~~~~text
#!/bin/bash
# § 5.2 — état « non consommée » : le motif du refus, extrait de la pièce de preuve écrite par le module
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7), version 4 ; porte, pour la forme
# seulement, le bloc « § 5.2, ligne écrite dans la prose (exception de l'état « non consommée ») » de la version 3 (195207cf…). Ne supprime rien, ne réécrit aucun fichier existant.
# Lancement, ligne unique : bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-motif-non-consommee.sh 1
. "$(dirname "$0")/commun.sh"
N="${1:-}"; exiger_numero "$N"; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : non consommée' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « non consommée » : arrêt"; exit 1; }
grep -o '"motif": "[^"]*"' "$ARBRE/diag/$RUNL/preuve-aucune-ouverture-bbis.json"
~~~~

## 4. Passages de prose changés

Compte par fondement :

- 4 — condition 1 du troisième complément : chaque bloc devient un script versé et scellé, lancé par une ligne unique en syntaxe simple ; paramètres par un fichier écrit par l'outil d'écriture ou par argument simple
- 1 — condition 2 : seul contrôle touché, le relevé des têtes du § 1.1, rejouable sous un nom numéroté, le relevé refusé étant gardé
- 0 — condition 3 : aucun script ne supprime ni ne réécrit un fichier existant (garde `neuf` étendue aux fichiers de travail)
- 3 — « Ce que la version 4 doit dire sur l'état laissé » : choix (ii), arbre de lecture neuf sous un nom neuf, l'ancien restant en place
- 1 — « Ne rien écrire sur le risque de redémarrage » : un emplacement nommé, rien d'autre
- 5 — ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme

Total : 14 passages de prose, plus 14 blocs remplacés chacun par sa ligne unique (fondement : condition 1). Passages sans fondement : aucun.

### 1. titre

**Fondement** : ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme.

Ancien :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v3
~~~~

Nouveau :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v4
~~~~

### 2. en-tête

**Fondement** : ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme.

Ancien :

~~~~text
**Cette version ne joue que le premier lancement.**
~~~~

Nouveau :

~~~~text
**Cette version ne joue que le premier lancement.**

**Version 4 — forme en scripts.** La version 3 (`commande-lecture-bbis-v3.md`, `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3`) reste (R12). Le lecteur-opérateur l'a jouée jusqu'au § 1.2 compris ; au § 1.3, l'outil de terminal a refusé le bloc pour sa forme, et l'opérateur s'est arrêté. Rien n'a été lancé, rien n'est consommé. Sous le troisième complément du mandat (`complement-3-mandat-preparateur-lecture-bbis-v1.md`, accordé par la session mère, R-3540), cette version change **la forme seulement** : chaque bloc est un script versé et scellé sous `scripts/lecture-bbis-v4/`, lancé par une ligne unique en syntaxe simple. Aucun contrôle n'est changé, ajouté ni retiré, hors le rejeu écrit du relevé des têtes (§ 1.1). Aucun script ne supprime ni ne réécrit un fichier existant. `differences-commande-lecture-bbis-v3-v4.md` donne, pour chaque bloc de la version 3, le script qui le porte et la preuve de l'égalité de fond. Tout le reste est le texte de la version 3, à l'octet.
~~~~

### 3. en-tête, « Écrite par simple lecture »

**Fondement** : condition 1 du troisième complément : chaque bloc devient un script versé et scellé, lancé par une ligne unique en syntaxe simple ; paramètres par un fichier écrit par l'outil d'écriture ou par argument simple.

Ancien :

~~~~text
**Écrite par simple lecture.** Aucun bloc de cette commande n'a été joué, ni entier ni en partie : ni le module, ni sa garde, ni une de ses fonctions, ni le programme de la preuve après coup. Les blocs ont seulement passé un contrôle de syntaxe (`bash -n`), hors de tout dépôt. Le contre-lecteur les lit ; le lecteur-opérateur est le premier à les jouer.
~~~~

Nouveau :

~~~~text
**Écrite par simple lecture.** Aucun script de cette commande n'a été joué, ni entier ni en partie : ni le module, ni sa garde, ni une de ses fonctions, ni le programme de la preuve après coup. Les scripts ont seulement passé un contrôle de syntaxe (`bash -n`), hors de toute exécution ; les trois fonctions neuves du fichier commun ont été essayées sur un dossier jouet. Les blocs des § 1.1 et § 1.2 ont tourné une fois sous leur forme de la version 3 ; les scripts qui les portent, non.
~~~~

### 4. § 0, paramètres

**Fondement** : condition 1 du troisième complément : chaque bloc devient un script versé et scellé, lancé par une ligne unique en syntaxe simple ; paramètres par un fichier écrit par l'outil d'écriture ou par argument simple.

Ancien :

~~~~text
| tête de la branche de travail après l'étape 0 (`TETE_TRAVAIL`) | donnée par la conductrice, 40 caractères |
| numéro du lancement (`N`) | `1` ; cette version ne joue que le premier lancement (§ 5.3) |
~~~~

Nouveau :

~~~~text
| tête de la branche de travail après l'étape 0 (`TETE_TRAVAIL`) | donnée par la conductrice, 40 caractères ; **l'opérateur l'écrit dans un fichier, par l'outil d'écriture de fichiers** (ci-dessous) |
| numéro du lancement | `1`, **donné en argument simple** aux scripts des § 4.2 à § 5.5 ; cette version ne joue que le premier lancement (§ 5.3) et ses scripts refusent tout autre numéro |
| décision sur le risque de redémarrage | donnée par la conductrice au lancement du second temps |
~~~~

### 5. § 0, état laissé et étape 0

**Fondement** : « Ce que la version 4 doit dire sur l'état laissé » : choix (ii), arbre de lecture neuf sous un nom neuf, l'ancien restant en place.

Ancien :

~~~~text
### Étape 0 — gestes de la conductrice, avant de lancer le lecteur-opérateur

La fusion est faite **par la conductrice, sur la branche de travail, avant le montage de l'arbre de lecture**. Je le juge plus sûr que de la laisser à l'opérateur : il ne tranche aucun conflit, l'arbre de lecture n'ajoute qu'un commit d'entrées, et le juge trouvera le registre voisin complet sur la branche de travail. Rien n'est poussé sur `main`.

```bash
cd /home/user/controle-ia-travail
git fetch origin                                              # récupération complète du distant, en lecture seule (décision d'organisation, m5)
git status --porcelain --untracked-files=all | wc -l          # attendu : 0, sinon on ne fusionne pas
git rev-parse --abbrev-ref HEAD                               # attendu : claude/lecture-verdict-etape-b-bis-v1
git merge --no-ff --no-edit 4aefb5b166b55a5ff7341454770a64caab923f52
# un conflit : `git merge --abort`, arrêt, rien n'est monté
J=registres/t07-etape-b-bis-v1.md.ouvertures.md
[ ! -e "$J" ] && printf '%s\n' "# Journal du registre propre du texte « T0.7, étape B bis » (registres/t07-etape-b-bis-v1.md) — une ligne par fichier de lecture écrit, ajoutée par le module de lecture ; lignes ajoutées, jamais réécrites" > "$J"
git add -- "$J" && git commit -q -m "Étape B bis, lecture : journal du registre propre créé avec sa seule ligne d'en-tête, avant toute lecture"
git rev-parse HEAD                                            # c'est TETE_TRAVAIL
```

- **Récupération complète du distant : décision d'organisation de la conductrice** (constat m5 de la contre-lecture de la version 2). La conductrice la fait ici, en lecture seule (`git fetch origin`), avant la fusion et le montage, pour que chaque branche de suivi locale soit à la tête du distant. L'opérateur ne fait que la comparaison (§ 1.1) ; sa permission d'appel au distant reste celle des trois branches nommées et de la lecture des têtes. Si le § 1.1 relève une branche absente ou à une autre tête, parce que le distant a avancé depuis, on ne lance pas : la conductrice refait cette récupération, puis l'opérateur rejoue le § 1.1 sous un nom de relevé neuf.
- La ligne d'en-tête ne porte pas la chaîne que le module compte comme une ligne d'ouverture (`lecture_v5.py`, l. 1436) : ne pas la changer.
- Le journal est créé « avec sa seule ligne d'en-tête, commité avant la lecture » (quatrième addendum, § 6.5, point 8).
- La conductrice commite aussi cette commande et sa contre-lecture avant ou avec ces gestes ; `TETE_TRAVAIL` est la tête après tout cela.
~~~~

Nouveau :

~~~~text
### État laissé par la version 3, et comment la lecture repart

État, par les noms (troisième complément du mandat ; je n'ai rien lu ni touché dans le dossier de travail de la version 3) :
- la fusion du commit de `main` `4aefb5b1…` et le journal du registre propre (ligne d'en-tête seule) sont faits et poussés : tête de la branche de travail `fd11004640544592885a218809b7f43415fb28f5` ;
- dossier de travail de la version 3, `…/scratchpad/lecture-bbis/` : son fichier de paramètres, trois relevés du § 1.1 (deux refusés, un conforme), l'arbre de lecture `arbre-de-lecture-v1` monté à `fd110046…` sur la branche locale `lecture/bbis-arbre-de-lecture-v1`, 32 entrées dans son index, aucun commit local ; l'intégrité de ces 32 fichiers n'est pas prouvée depuis un redémarrage de la machine ;
- rien n'a été lancé ; aucune preuve n'est écrite ; rien n'est poussé de l'arbre de lecture.

**Choix : un arbre de lecture neuf, sous un nom neuf, à la tête neuve ; l'ancien reste en place ; rien n'est supprimé.** Raisons :
- **La forme seule change.** Verser les scripts change la tête de la branche de travail. Avec un arbre neuf monté à cette tête, chaque contrôle de la version 3 qui cite `TETE_TRAVAIL` reste mot pour mot : tête de la branche de travail (§ 1.1), montage (§ 1.2), parent de la tête de l'arbre de lecture (§ 4.2). Reprendre l'ancien arbre aurait demandé deux têtes et des contrôles réécrits, et de sauter le § 1.2, dont la garde `neuf` refuse un arbre qui existe déjà.
- **Ce que les textes demandent est tenu.** Une tête qui descend du commit de la course et contient le commit de `main` qui porte les inscriptions (quatrième addendum, QA-1, point (P5), et § 4, point 2 ; premier complément du mandat, point 2) : vrai de la tête neuve, contrôlé aux § 1.1 et § 2. L'ancien arbre l'aurait tenu aussi : le module, les textes scellés, les registres et la fiche n'ont pas changé entre les deux têtes, ce que le § 1.4 vérifie par les empreintes. Le choix ne tient donc pas à une exigence des textes, mais à la forme et à la traçabilité.
- **Traçabilité.** Le manifeste de la lecture cite le commit de l'arbre où elle se joue (`manifeste.py`, l. 78-104 ; R9). Avec l'arbre neuf, l'ascendance de ce commit porte la commande et les scripts effectivement joués.
- **Intégrité.** L'arbre neuf est extrait à neuf des trois branches, puis contrôlé objet par objet (§ 1.3) ; l'index de l'ancien, d'intégrité non prouvée, ne sert pas.
- **Place.** 11 Go libres relevés par la conductrice ; l'arbre pèse environ 3,4 Go : il reste environ 7,6 Go. Les sorties de la lecture sont un manifeste, un fichier de lecture et une sortie imprimée, en texte. Cela tient ; le seuil de 6 Go du § 1.1 est gardé tel quel.

Noms neufs, et eux seuls : dossier de travail `…/scratchpad/lecture-bbis-v4/` ; arbre de lecture `arbre-de-lecture-v4` ; branche locale `lecture/bbis-arbre-de-lecture-v4`. Le nom de la branche sur le distant ne change pas : elle n'a jamais été poussée.

**Ce qui reste en place, et qu'aucun script ne lit ni ne touche** : le dossier de travail de la version 3, son arbre de lecture et sa branche locale. Cette branche pointe sur `fd110046…`, ancêtre de la tête de travail : elle n'ajoute aucun commit à ce que la garde parcourt. Leur retrait est une suppression : **je ne l'écris pas ; il reste à un humain**, quand il le voudra.

### Étape 0 — gestes de la conductrice, avant de lancer le lecteur-opérateur

La fusion et le journal sont faits : **ils ne sont pas rejoués**. Restent, chacun en une ligne simple :

1. verser et commiter, sur la branche de travail : cette commande, ses différences avec la version 3, le dossier `scripts/lecture-bbis-v4/` (scripts et compagnons), le troisième complément du mandat ; pousser la branche de travail ;
2. juste avant de lancer l'opérateur, la récupération complète du distant, en lecture seule (décision d'organisation sur m5) :

```bash
git -C /home/user/controle-ia-travail fetch origin
```

3. relever l'état et la tête, qui est `TETE_TRAVAIL` :

```bash
git -C /home/user/controle-ia-travail status --porcelain --untracked-files=all
```

```bash
git -C /home/user/controle-ia-travail rev-parse HEAD
```

- Le statut doit être vide : le § 1.1 exige l'arbre principal propre.
- **Récupération complète du distant : décision d'organisation de la conductrice** (constat m5 de la contre-lecture de la version 2). L'opérateur ne fait que la comparaison (§ 1.1) ; sa permission d'appel au distant reste celle des trois branches nommées et de la lecture des têtes. Si le § 1.1 relève une branche absente ou à une autre tête, parce que le distant a avancé depuis, on ne lance pas : la conductrice refait cette récupération, puis l'opérateur rejoue le § 1.1 (règle du § 1.1).
- La ligne d'en-tête du journal ne porte pas la chaîne que le module compte comme une ligne d'ouverture (`lecture_v5.py`, l. 1436) : ne pas la changer.
- Le journal est créé « avec sa seule ligne d'en-tête, commité avant la lecture » (quatrième addendum, § 6.5, point 8) : c'est fait.
~~~~

### 6. § 0, fichier des paramètres

**Fondement** : condition 1 du troisième complément : chaque bloc devient un script versé et scellé, lancé par une ligne unique en syntaxe simple ; paramètres par un fichier écrit par l'outil d'écriture ou par argument simple.

Ancien :

~~~~text
### Fichier des paramètres (premier geste du lecteur-opérateur)

Chaque bloc de la suite commence par relire ce fichier : l'état du terminal ne tient pas d'un appel à l'autre.

```bash
S=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad
mkdir -p "$S/lecture-bbis"
[ -e "$S/lecture-bbis/parametres.sh" ] && { echo "parametres.sh existe déjà : arrêt"; exit 1; }
cat > "$S/lecture-bbis/parametres.sh" <<'EOF'
DEPOT=/home/user/controle-ia-travail
T=/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis
ARBRE="$T/arbre-de-lecture-v1"
PY="$DEPOT/.venv/bin/python"
LV1="$DEPOT/registres/t07-etape-b-bis/lecture-v1"
RUN_7B=20261111-151701-t06-reel
RUN_BBIS=20261118-154143-bbis-t07-v1
RUN_MC=20261116-205721-mots-et-cout-t06
RUN_B=20261114-001352-t07-lecture-reel
MAIN_INSCRIPTIONS=4aefb5b166b55a5ff7341454770a64caab923f52
TETE_TRAVAIL=REMPLACER_PAR_LA_TETE_DONNEE_PAR_LA_CONDUCTRICE
COURSE=438a9c5257bdc4fa65f25c42cc89753a049b4586
C_CONJ=c098fb512d999e1dbf7cef5fba6430ff8b1a8fb5
C_REMISE=06c8832819af344d01c184222833c5a42e8ac901
C_FICHE=05cd22aa15382f61eb62b9e7817890dde728dd5f
C_PIECE=da06bb57610f840152e4e9a8c449b036577cc582
REF_SORTIES=refs/remotes/origin/donnees/t07-etape-b-bis-v2
TETE_SORTIES=7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9
REF_7B=refs/remotes/origin/calcul/t06-confirmation-7b-v1
TETE_7B=55c3e3eb89a4650419f35999aaa4c54288275b0d
REF_MC=refs/remotes/origin/verdict/t06-mots-et-cout-compte-3-v1
PROPRE=registres/t07-etape-b-bis-v1.md
VOISIN=registres/t07-etape-b-bis-v1-addenda-v1.md
PARTAGE=registres/scellements-v1.md
JOURNAL=registres/t07-etape-b-bis-v1.md.ouvertures.md
MODULE=src/controle_ia/t07bbis/lecture_v5.py
BRANCHE_DISTANTE_ARBRE=claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
NETTOYE=(env -u GIT_SSL_CAINFO -u GIT_ASKPASS -u GIT_EDITOR -u GIT_TERMINAL_PROMPT -u GIT_CONFIG_COUNT -u GIT_CONFIG_KEY_0 -u GIT_CONFIG_KEY_1 -u GIT_CONFIG_KEY_2 -u GIT_CONFIG_VALUE_0 -u GIT_CONFIG_VALUE_1 -u GIT_CONFIG_VALUE_2 -u BBIS_INSTANCE)
G() { "${NETTOYE[@]}" git -C "$ARBRE" "$@"; }
FAUTES=0
dire() { printf '%s\n' "$*"; }
egal() { if [ -n "$2" ] && [ "$2" = "$3" ]; then dire "CONFORME : $1"; else dire "DEFAUT : $1 (attendu « $2 » ; relevé « $3 »)"; FAUTES=$((FAUTES+1)); fi; }
vrai() { local l="$1"; shift; if "$@" >/dev/null 2>&1; then dire "CONFORME : $l"; else dire "DEFAUT : $l"; FAUTES=$((FAUTES+1)); fi; }
conclure() { dire "FAUTES : $FAUTES"; if [ "$FAUTES" = 0 ]; then dire "CONCLUSION : conforme, on continue"; else dire "CONCLUSION : ON NE LANCE PAS"; fi; }
neuf() { if [ -e "$1" ]; then echo "$1 existe déjà : on n'écrase jamais ; arrêt"; exit 1; fi; }
sceller() { ( cd "$DEPOT" && PYTHONPATH=src "$PY" -m controle_ia.scellement sceller "$1" ); }
EOF
```

Puis l'opérateur remplace, dans ce fichier, la valeur de `TETE_TRAVAIL` par celle que la conductrice lui a donnée, et rien d'autre.
~~~~

Nouveau :

~~~~text
### Scripts, fichier commun, fichier de la conductrice (premier geste du lecteur-opérateur)

**Chaque geste de l'opérateur est une ligne unique, en syntaxe simple** : `bash`, le chemin du script, et, des § 4.2 à § 5.5, l'argument `1`. Rien d'autre : ni accolade, ni redirection, ni tube, ni texte en ligne. L'opérateur ne recopie le contenu d'aucun script dans son terminal.

Les scripts sont sous `/home/user/controle-ia-travail/scripts/lecture-bbis-v4/`, chacun avec son compagnon ; leurs empreintes sont dans le fichier des différences. Chacun relit le fichier commun `commun.sh` (paramètres et fonctions : c'est le fichier des paramètres de la version 3), parce que l'état du terminal ne tient pas d'un appel à l'autre.

| paragraphe | script | qui le lance |
|---|---|---|
| § 1.1 | `1-1-depot-et-tetes.sh` | opérateur |
| § 1.2 | `1-2-montage-de-l-arbre.sh` | opérateur |
| § 1.3 | `1-3-entrees.sh` | opérateur |
| § 1.4 | `1-4-code-et-textes.sh` | opérateur |
| § 2 | `2-preuve-anteriorite-et-entree-conjointe.sh` | opérateur |
| § 4.1 | `4-1-commit-local.sh` | opérateur |
| § 4.1 | `4-1-conductrice-preuve-et-branche.sh` | **conductrice** |
| § 4.2 | `4-2-releve-avant-lancement.sh 1` | opérateur |
| § 5.1 | `5-1-lancement.sh 1` | opérateur |
| § 5.1 bis | `5-1-bis-attente.sh 1` | opérateur |
| § 5.2 | `5-2-releve-apres-lancement.sh 1` | opérateur |
| § 5.2 | `5-2-constat-de-forme-pour-le-juge.sh 1` | opérateur |
| § 5.2 | `5-2-motif-non-consommee.sh 1` | opérateur, état « non consommée » seulement |
| § 5.4 | `5-4-sorties-portees-et-ligne-de-lecture.sh 1` | opérateur |
| § 5.5 | `5-5-preuve-apres-coup-sur-ordre-ecrit.sh 1` | opérateur, **sur ordre écrit de la conductrice seulement** |

**Comment entrent les paramètres de la conductrice.**
- `TETE_TRAVAIL` : **par un fichier, que l'opérateur écrit par l'outil d'écriture de fichiers**, jamais par le terminal. Chemin : `/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis-v4/parametres-conductrice-v4.txt`. Contenu : une seule ligne, `TETE_TRAVAIL=` suivi des 40 caractères donnés par la conductrice. Le fichier commun lit cette ligne sans l'exécuter et s'arrête si le fichier manque, si la ligne n'y est pas une fois, ou si la valeur n'a pas la forme d'un identifiant de commit. C'est le premier geste de l'opérateur, et le seul fichier qu'il écrit à la main.
- Le numéro du lancement : **par argument simple**, `1`.
- La décision sur le risque de redémarrage : donnée par la conductrice au lancement du second temps ; elle n'entre dans aucun script.
~~~~

### 7. § 1.1, sous le bloc

**Fondement** : condition 2 : seul contrôle touché, le relevé des têtes du § 1.1, rejouable sous un nom numéroté, le relevé refusé étant gardé.

Ancien :

~~~~text
On ne lance pas ; la conductrice fait récupérer la branche.
~~~~

Nouveau :

~~~~text
On ne lance pas ; la conductrice fait récupérer la branche.
- **Rejeu du relevé des têtes — seul contrôle que la version 4 touche** (troisième complément, condition 2). Le script écrit son relevé sous un nom numéroté, `releve-mise-en-place-<k>.txt`, où k est le plus petit numéro libre, à partir de 1 ; ses trois fichiers de travail portent le même numéro. Un relevé n'est jamais réécrit ni renommé : **le relevé refusé est gardé tel quel**. Pour rejouer, après que la conductrice a refait la récupération complète, l'opérateur relance la même ligne ; le script prend le numéro suivant. **Règle de lecture, sans autre cas : les scripts des § 1.2 et § 2 lisent le relevé de plus grand numéro, et lui seul ; s'il ne conclut pas « conforme », ils s'arrêtent, même si un relevé de numéro plus petit était conforme.** Les contrôles du relevé sont ceux de la version 3, à la lettre.
~~~~

### 8. § 4.1, nom de la branche locale

**Fondement** : « Ce que la version 4 doit dire sur l'état laissé » : choix (ii), arbre de lecture neuf sous un nom neuf, l'ancien restant en place.

Ancien :

~~~~text
**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v1` de l'arbre de lecture
~~~~

Nouveau :

~~~~text
**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v4` de l'arbre de lecture
~~~~

### 9. § 6, fin

**Fondement** : « Ce que la version 4 doit dire sur l'état laissé » : choix (ii), arbre de lecture neuf sous un nom neuf, l'ancien restant en place.

Ancien :

~~~~text
La branche locale `lecture/bbis-arbre-de-lecture-v1` n'y est jamais fusionnée.
~~~~

Nouveau :

~~~~text
La branche locale `lecture/bbis-arbre-de-lecture-v4` n'y est jamais fusionnée, ni celle de la version 3, restée en place.
~~~~

### 10. avant le § 4.2 (emplacement nommé, rien d'autre)

**Fondement** : « Ne rien écrire sur le risque de redémarrage » : un emplacement nommé, rien d'autre.

Ancien :

~~~~text
### 4.2 Relevé d'avant lancement
~~~~

Nouveau :

~~~~text
### Décision sur le risque de redémarrage : donnée par la conductrice au lancement du second temps

### 4.2 Relevé d'avant lancement
~~~~

### 11. § 5.2, exception de l'état « non consommée »

**Fondement** : condition 1 du troisième complément : chaque bloc devient un script versé et scellé, lancé par une ligne unique en syntaxe simple ; paramètres par un fichier écrit par l'outil d'écriture ou par argument simple.

Ancien :

~~~~text
L'opérateur le leur rend par une seule ligne, extraite de la pièce de preuve écrite par le module et non de ce constat : `grep -o '"motif": "[^"]*"' "$ARBRE/diag/$RUNL/preuve-aucune-ouverture-bbis.json"`.
~~~~

Nouveau :

~~~~text
L'opérateur le leur rend par une seule ligne, extraite de la pièce de preuve écrite par le module et non de ce constat, par le script `5-2-motif-non-consommee.sh` :

```bash
bash /home/user/controle-ia-travail/scripts/lecture-bbis-v4/5-2-motif-non-consommee.sh 1
```

  Le script porte la ligne de la version 3 (`grep -o` du champ « motif » de la pièce de preuve) et refuse de partir hors de l'état « non consommée ».
~~~~

### 12. § 6, pièces commitées à l'étape 0

**Fondement** : ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme.

Ancien :

~~~~text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, ses différences avec la version 2, la contre-lecture de la version 2 dont elle porte les corrections, leurs compagnons (les versions 1 et 2 et leurs pièces restent, R12).
~~~~

Nouveau :

~~~~text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v4.md`, ses différences avec la version 3, le dossier `scripts/lecture-bbis-v4/` (seize fichiers et leurs compagnons), le troisième complément du mandat du préparateur, leurs compagnons (les versions 1 à 3 et leurs pièces restent, R12).
~~~~

### 13. § 6, avant le lancement

**Fondement** : ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme.

Ancien :

~~~~text
- la fusion du commit de `main` `4aefb5b1…` ;
- `registres/t07-etape-b-bis-v1.md.ouvertures.md` (ligne d'en-tête) ;
~~~~

Nouveau :

~~~~text
- la fusion du commit de `main` `4aefb5b1…` et `registres/t07-etape-b-bis-v1.md.ouvertures.md` (ligne d'en-tête) : déjà commités et poussés (tête `fd110046…`) ;
~~~~

### 14. § 7, points ouverts de forme

**Fondement** : ce qui découle strictement : titre, nom de la version, noms neufs, pièces à commiter, points ouverts de forme.

Ancien :

~~~~text
- **N8 — Blocs écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée.
~~~~

Nouveau :

~~~~text
- **N11 — Forme en scripts.** Seize fichiers sous `scripts/lecture-bbis-v4/`, écrits par programme à partir des blocs de la version 3 ; aucun n'a été joué. Si l'outil de terminal refusait encore une ligne `bash <script>`, l'opérateur s'arrête et rend le texte du refus : il ne recopie pas le script.
- **N12 — Ce que la version 3 a laissé reste en place** : son dossier de travail, son arbre de lecture (3,4 Go) et sa branche locale. Aucun script ne les supprime ; leur retrait reste à un humain.
- **N13 — Le montage n'est pas rejouable** : si le § 1.2 s'arrêtait en cours (un redémarrage, par exemple), l'arbre `arbre-de-lecture-v4` existerait à moitié et sa garde `neuf` refuserait de le remonter. Aucun script ne le retire. Il faudrait un nom d'arbre neuf, donc une version de la commande, ou le geste d'un humain.
- **N14 — Deux ajouts au registre propre et à son journal, au § 5.4**, sont des lignes ajoutées en fin de fichier, voulues par le texte (« lignes ajoutées, jamais réécrites ») : ce ne sont pas des réécritures ; je les signale parce que la condition 3 du troisième complément parle de tout fichier existant.
- **N8 — Scripts écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée.
~~~~


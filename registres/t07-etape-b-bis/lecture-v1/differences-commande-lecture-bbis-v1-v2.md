# Différences entre la commande de lecture version 1 et la version 2 — apprentissage des sondes sur la tâche (étape B bis de T0.7)

Écrit par le préparateur (Fable 5.2), le 2026-11-18, par le programme qui a écrit la version 2 à partir de la version 1 : chaque « ancien » figure une seule fois dans la version 1 (vérifié par ce programme, qui refuse sinon) et y est remplacé par son « nouveau » ; rien d'autre n'est changé.

- Version 1 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md`, `b308c9b12803ea58b470a7670881fc30274f0c93c04bc288d893146c6641e615` (reste, R12).
- Version 2 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v2.md`, `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d`.
- Fondements : les huit points du second complément au mandat du préparateur (`complement-2-mandat-preparateur-lecture-bbis-v1.md`, `8777bcf5…`), qui portent les cinq constats provisoires du premier contre-lecteur (`arret-contre-lecteur-commande-refus-crochet-v1.md`, `a903b87b…`) ; et sa tâche (nom neuf).

## Compte des passages changés, par fondement

- 2 — tâche du second complément : nom neuf, la version 1 reste (R12)
- 2 — point 1 du second complément : contrôles d'après le seuil faits avant le lancement, sur des fichiers hors données
- 6 — point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus
- 1 — point 3 : ce que l'opérateur rend sur un arrêt avant le seuil
- 2 — point 4 : récupération des branches nommées, en lecture seule, permise à l'opérateur
- 6 — point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond
- 4 — point 6 : voie de l'arrêt avant le seuil ouverte par anticipation par la session mère, avec sa réserve
- 8 — point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement
- 1 — point 8 : le mandat du juge porte les lignes à citer ; point retiré des points ouverts

Total : 32 passages. Passages sans fondement : aucun.

## Les passages

### 1. titre

**Fondement** : tâche du second complément : nom neuf, la version 1 reste (R12).

Ancien :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1
~~~~

Nouveau :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v2
~~~~

### 2. en-tête

**Fondement** : tâche du second complément : nom neuf, la version 1 reste (R12).

Ancien :

~~~~text
son complément `complement-mandat-preparateur-lecture-bbis-v1.md` (`9a8b5515…`) et les règles communes (`5f303a9c…`), compagnons vérifiés.
~~~~

Nouveau :

~~~~text
son complément `complement-mandat-preparateur-lecture-bbis-v1.md` (`9a8b5515…`), son second complément `complement-2-mandat-preparateur-lecture-bbis-v1.md` (`8777bcf5…`) et les règles communes (`5f303a9c…`), compagnons vérifiés.

**Version 2.** La version 1 (`commande-lecture-bbis-v1.md`, `b308c9b12803ea58b470a7670881fc30274f0c93c04bc288d893146c6641e615`) reste, non jouée (R12). Cette version traite les cinq constats provisoires du premier contre-lecteur (`arret-contre-lecteur-commande-refus-crochet-v1.md`, `a903b87b…`) et les huit points du second complément ; chaque passage changé est dans `differences-commande-lecture-bbis-v1-v2.md`, avec son fondement. Tout le reste est le texte de la version 1, à l'octet.
~~~~

### 3. en-tête, interdits de l'opérateur

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
afficher la sortie d'un lancement au-delà de ce que le § 5.3 demande ; relancer ; corriger ; pousser.
~~~~

Nouveau :

~~~~text
afficher la sortie d'un lancement au-delà de ce que le § 5.2 demande ; afficher le constat de forme destiné au juge ; arrêter un processus ; relancer ; corriger ; pousser.

**Aucune commande d'arrêt de processus n'est écrite dans cette commande**, sous aucune forme. Une lecture lente mais vivante n'est jamais arrêtée.
~~~~

### 4. § 0, paramètres

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
| numéro du lancement (`N`) | `1` ; tout autre numéro seulement sur le mot de la conductrice (§ 6) |
~~~~

Nouveau :

~~~~text
| numéro du lancement (`N`) | `1` ; tout autre numéro seulement sur le mot de la conductrice (§ 5.3) |
| nom, sur le distant, de la branche de l'arbre de lecture | `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` (poussée par la conductrice, § 4.1) |
~~~~

### 5. § 0, fichier des paramètres

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
MODULE=src/controle_ia/t07bbis/lecture_v5.py
NETTOYE=
~~~~

Nouveau :

~~~~text
MODULE=src/controle_ia/t07bbis/lecture_v5.py
BRANCHE_DISTANTE_ARBRE=claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
NETTOYE=
~~~~

### 6. § 0, après le fichier des paramètres

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
Puis l'opérateur remplace, dans ce fichier, la valeur de `TETE_TRAVAIL` par celle que la conductrice lui a donnée, et rien d'autre.
~~~~

Nouveau :

~~~~text
Puis l'opérateur remplace, dans ce fichier, la valeur de `TETE_TRAVAIL` par celle que la conductrice lui a donnée, et rien d'autre.

**Deux temps.** Premier temps : § 1 à § 4.1 (mise en place, preuve relevée à part, commit local des entrées) ; l'opérateur rend la tête de l'arbre de lecture et s'arrête. La conductrice pousse alors la branche de l'arbre de lecture sous le nom ci-dessus (§ 4.1). Second temps, sur son message : § 4.2 à § 5.4.
~~~~

### 7. § 1.1, sous le bloc

**Fondement** : point 4 : récupération des branches nommées, en lecture seule, permise à l'opérateur.

Ancien :

~~~~text
- Une branche du distant absente localement : la garde chercherait
~~~~

Nouveau :

~~~~text
- **Appels au distant permis au lecteur-opérateur, en lecture seule, et eux seuls** (second complément, point 4 ; la conductrice l'écrit aussi dans son mandat) : la récupération des trois branches nommées ci-dessus (`git fetch origin <branche>`), la lecture des têtes du distant (`git ls-remote --heads origin`), ici et au § 4.2. Ils n'écrivent rien sur le distant. Aucun autre appel à un service extérieur.
- Une branche du distant absente localement : la garde chercherait
~~~~

### 8. § 4.1

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
  commit -q -m "Étape B bis, lecture : entrées de la liste blanche, commit local de l'arbre de lecture, jamais poussé" || { echo "commit local refusé : arrêt"; exit 1; }
git rev-parse HEAD
```
~~~~

Nouveau :

~~~~text
  commit -q -m "Étape B bis, lecture : entrées de la liste blanche, commit local de l'arbre de lecture" || { echo "commit local refusé : arrêt"; exit 1; }
git rev-parse HEAD
```

**Fin du premier temps.** L'opérateur rend cette tête à la conductrice et s'arrête.

**Geste de la conductrice, avant le lancement** (second complément, point 7) : elle pousse la branche locale de l'arbre de lecture sous un nom de sa branche, jamais `main`, pour que le manifeste de la lecture cite un commit joignable sur le distant :

```bash
cd /home/user/controle-ia-travail
git push origin lecture/bbis-arbre-de-lecture-v1:refs/heads/claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
git ls-remote --heads origin claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture     # attendu : la tête rendue par l'opérateur
```

- Cette branche porte les 32 fichiers d'entrée, déjà présents sur le distant sous leurs branches d'origine ; elle n'est jamais fusionnée dans la branche de travail ni dans `main`.
- Le § 4.2 vérifie, avant le lancement, que la tête de cette branche sur le distant est la tête de l'arbre de lecture ; sinon on ne lance pas.
- Après une relance accordée (§ 5.3, état « non consommée »), les commits locaux de plus sont poussés de même, avant la relance.
~~~~

### 9. § 4.1, qui commite

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v1` de l'arbre de lecture ; jamais poussé, jamais sur `main` ni sur la branche de travail** (complément du mandat, point 2).
~~~~

Nouveau :

~~~~text
**Qui commite : le lecteur-opérateur, localement, sur la branche `lecture/bbis-arbre-de-lecture-v1` de l'arbre de lecture ; jamais sur `main` ni sur la branche de travail** (complément du mandat, point 2). Il ne pousse pas : la conductrice pousse cette branche sous un nom de la sienne (ci-dessous).
~~~~

### 10. § 4.2, bloc

**Fondement** : point 1 du second complément : contrôles d'après le seuil faits avant le lancement, sur des fichiers hors données.

Ancien :

~~~~text
dire "-- versions (fils de calcul fixés à 1 par la ligne de lancement)"
~~~~

Nouveau :

~~~~text
dire "-- contrôles que l'écriture du résultat rejouerait après le seuil, faits ici sur des fichiers hors données"
egal "nom du run de lecture à la forme exigée par le manifeste" oui "$(printf '%s' "$RUNL" | grep -q -E '^[0-9]{8}-[0-9]{6}-[a-z0-9][a-z0-9-]{0,62}$' && echo oui || echo non)"
vrai "dossiers runs et diag de l'arbre de lecture ouverts à l'écriture" test -d runs -a -w runs -a -d diag -a -w diag
vrai "aucun fichier de lecture ni compagnon à ce nom de run" test ! -e "diag/$RUNL/lecture-bbis.json" -a ! -e "diag/$RUNL/lecture-bbis.json.sha256"
egal "préenregistrement scellé conforme pour un manifeste décisif (prereg.exiger_prereg_scelle, sur le texte seul)" 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.prereg import exiger_prereg_scelle; print(exiger_prereg_scelle(sys.argv[1]))' "$ARBRE/prereg/T0.7-etape-B-bis-v1.md" 2>&1 | tail -n 1)"
egal "fiche de code lisible, niveau décisif admis, entropie de plus de 64 bits (registre_bbis_v1.lire_fiche_code, commun_v1.exiger_entropie)" conforme "$("${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$ARBRE/src" "$PY" -c 'import sys; from controle_ia.t07bbis.registre_bbis_v1 import lire_fiche_code; from controle_ia.t07bbis.commun_v1 import exiger_entropie; f = lire_fiche_code(sys.argv[1]); exiger_entropie(int(f["entropie"]), reelle=True); print("conforme")' "$ARBRE/registres/t07-etape-b-bis/code-bbis-v2.json" 2>&1 | tail -n 1)"
dire "-- branche de l'arbre de lecture sur le distant (poussée par la conductrice), utilitaires du lancement"
egal "tête, sur le distant, de la branche de l'arbre de lecture" "$(git rev-parse HEAD)" "$(git ls-remote --heads origin "$BRANCHE_DISTANTE_ARBRE" 2>/dev/null | awk '{print $1}')"
vrai "utilitaire de détachement (nouvelle session de processus) présent" command -v setsid
vrai "utilitaire d'insensibilité à la fermeture du terminal présent" command -v nohup
vrai "utilitaire de relevé de l'état d'un processus présent" command -v ps
dire "-- versions (fils de calcul fixés à 1 par la ligne de lancement)"
~~~~

### 11. § 4.2, sous le bloc

**Fondement** : point 1 du second complément : contrôles d'après le seuil faits avant le lancement, sur des fichiers hors données.

Ancien :

~~~~text
- **S'il reste une variable dont le nom commence par `GIT_`, on ne lance pas**
~~~~

Nouveau :

~~~~text
- **Contrôles d'après le seuil ramenés avant le lancement** (second complément, point 1). L'écriture du résultat crée un manifeste décisif après tout le calcul (`lecture_v5.ecrire_lecture`, l. 1635-1648 ; `manifeste.creer_manifeste`, l. 68-116) : un échec y consommerait la lecture. Par lecture de ces deux fonctions, ce qu'elles contrôlent sur des fichiers hors données, et où la commande le fait avant :
  - la forme du nom du run (`manifeste.py`, l. 26 et 74) et l'absence de son dossier (l. 76-77) : ici ;
  - l'arbre propre (l. 78-83) : ici, par git dans l'environnement nettoyé ;
  - **le préenregistrement scellé** (l. 85-96, `prereg.exiger_prereg_scelle`) : compagnon égal, huit sections exigées présentes et non vides, aucun marqueur « À REMPLIR », aucun marqueur de gabarit, deux empreintes par entrée de la section « Contre-lecture » (`prereg.py`, l. 37-76). La commande appelle **cette fonction du dépôt**, sur le texte scellé de l'arbre de lecture et sur lui seul. Elle n'est ni le module de lecture ni sa garde, n'ouvre aucune donnée et ne lance aucune commande git ;
  - l'entropie des graines (`manifeste.graines`, l. 37-49) et la fiche de code que `main` relit pour la trouver (`lecture_v5.py`, l. 1693-1695) : la commande appelle `registre_bbis_v1.lire_fiche_code` et `commun_v1.exiger_entropie` sur la fiche de code, qui n'est pas un fichier de résultat ; ce ne sont ni le module de lecture ni sa garde ;
  - l'écriture du dossier du run (l. 110-114) et du fichier de lecture (`manifeste.ecrire_resultat`, l. 128-139) : dossiers `runs` et `diag` ouverts à l'écriture, aucun fichier à ce nom ;
  - les versions des bibliothèques (`manifeste.versions`, l. 58-65) sont seulement consignées : elles ne peuvent pas refuser.
  Le module gelé de la partition des plis, que `lire` compare après le seuil (`adversaires_texte_v1.exiger_module_gele`), est déjà comparé au § 1.4. Ce qui reste après le seuil et ne peut pas être contrôlé avant sans ouvrir une donnée : les contrôles du contenu des entrées elles-mêmes (manifeste de la course de confirmation, audit des fuites, champ du contrôle carte-processeur, effectifs).
- Un échec d'un de ces contrôles vaut « on ne lance pas ».
- **S'il reste une variable dont le nom commence par `GIT_`, on ne lance pas**
~~~~

### 12. § 4.2, sous le bloc

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
- Si git ne répond pas dans l'environnement nettoyé : on ne lance pas (note n10 de la contre-lecture du code).
~~~~

Nouveau :

~~~~text
- Si git ne répond pas dans l'environnement nettoyé : on ne lance pas (note n10 de la contre-lecture du code).
- **Si l'utilitaire de détachement manque, on ne lance pas** : l'opérateur ne le remplace par rien et rend le relevé. Relevé par le préparateur sur cette machine, par `command -v` : il est présent (`/usr/bin/setsid`, option `-f`), ainsi que les deux autres.
~~~~

### 13. § 5.1, bloc

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
nohup bash "$L" > /dev/null 2>&1 &
sleep 2; echo "PID du module de lecture : $(cat "$T/lancement-$N.pid")"
~~~~

Nouveau :

~~~~text
command -v setsid > /dev/null || { echo "utilitaire de détachement absent : ON NE LANCE PAS"; exit 1; }
setsid -f nohup bash "$L" < /dev/null > /dev/null 2>&1
for i in 1 2 3 4 5 6 7 8 9 10; do [ -s "$T/lancement-$N.pid" ] && break; sleep 1; done
echo "identifiant du processus du module de lecture : $(cat "$T/lancement-$N.pid" 2>/dev/null)"
~~~~

### 14. § 5.1, sous le bloc

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
- **PID** : celui du module de lecture, écrit par l'enveloppe dans `lancement-<N>.pid`. Un arrêt, s'il était ordonné par la conductrice, se ferait par ce PID et lui seul.
~~~~

Nouveau :

~~~~text
- **Lancement détaché de l'outil** (second complément, point 2) : l'enveloppe part dans une nouvelle session de processus (`setsid -f`), entrées et sorties coupées du terminal ; l'appel d'outil rend la main aussitôt. Le module n'est ni en arrière-plan d'un appel d'outil, ni sous un délai d'outil. L'opérateur ne lance pas ce bloc avec l'option d'arrière-plan de son outil.
- **Identifiant du processus** : celui du module de lecture, écrit par l'enveloppe dans `lancement-<N>.pid`. Le code de sortie est écrit dans `lancement-<N>.code` quand le module finit.
~~~~

### 15. § 5.1, durée

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
- **Durée** : le code ne la laisse pas estimer, et le module n'a jamais tourné sur les fichiers réels. L'opérateur attend la fin sans délai de garde, en relevant de loin en loin la présence de `lancement-<N>.code`. **Il n'arrête pas un processus vivant et ne touche à rien dans l'arbre de lecture pendant la marche** : un fichier de plus rendrait l'arbre non propre au moment du manifeste, après le seuil.
~~~~

Nouveau :

~~~~text
- **Durée** : le code ne la laisse pas estimer, et le module n'a jamais tourné sur les fichiers réels.
- **L'opérateur ne touche à rien dans l'arbre de lecture pendant la marche** : un fichier de plus rendrait l'arbre non propre au moment du manifeste, après le seuil.
~~~~

### 16. § 5.1 bis (neuf)

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
### 5.2 Fin du lancement : sortie gardée et scellée
~~~~

Nouveau :

~~~~text
### 5.1 bis Attente, sans jamais arrêter le processus

L'opérateur relève l'état du processus par son identifiant, par des appels courts et espacés (toutes les dix minutes environ, sans attente longue dans un appel). Il n'y a aucun délai de garde.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif ps -p "$(cat "$T/lancement-$N.pid")" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
date -u +%Y-%m-%dT%H:%M:%SZ
```

- « vivant » : l'opérateur attend, quel que soit le temps écoulé. **Une lecture lente mais vivante n'est jamais arrêtée**, ni par lui, ni sur aucun motif ; s'il doute, il écrit à la conductrice et continue d'attendre.
- « fini » : § 5.2.
- « processus absent, code de sortie non écrit » deux relevés de suite, à une minute d'écart : le processus a disparu sans finir (machine redémarrée, par exemple). § 5.2, qui le traite comme un arrêt, avant ou après le seuil selon la sortie gardée.

### 5.2 Fin du lancement : sortie gardée et scellée
~~~~

### 17. § 5.2, relevé d'après lancement (point 3 ; la règle de ce qui est rendu dans l'état « écrit » vient du point 5)

**Fondement** : point 3 : ce que l'opérateur rend sur un arrêt avant le seuil.

Ancien :

~~~~text
À jouer quand `lancement-<N>.code` existe.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
[ -e "$T/lancement-$N.code" ] || { echo "le lancement n'est pas fini"; exit 1; }
RUNL="$(cat "$T/run-lecture-$N.txt")"; SORTIE="$T/sortie-lancement-$N.txt"
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"; neuf "$G1"
cp "$SORTIE" "$G1" && sceller "registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt"
L1="$LV1/lancement-lecture-bbis-$N-v1.sh"; neuf "$L1"
cp "$T/lancement-$N.sh" "$L1" && sceller "registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh"
R="$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt"; neuf "$R"
{
dire "Relevé d'après lancement n° $N — run de lecture $RUNL"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null) ; PID $(cat "$T/lancement-$N.pid")"
dire "code de sortie : $(cat "$T/lancement-$N.code")"
dire "sortie gardée : registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt $(sha256sum "$G1" | cut -d' ' -f1)"
dire "lignes « BBIS LECTURE ENTREES OUVERTES » : $(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"
dire "lignes « BBIS LECTURE ECRITE » : $(grep -c '^BBIS LECTURE ECRITE ' "$G1")"
dire "lignes « BBIS LECTURE NON CONSOMMEE » : $(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
dire "lignes « BBIS LECTURE ARRET » : $(grep -c '^BBIS LECTURE ARRET' "$G1")"
dire "lignes de la sortie : $(wc -l < "$G1" | tr -d ' ')"
cd "$ARBRE" || exit 1
for f in "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json" "diag/$RUNL/preuve-aucune-ouverture-bbis.json"; do
  if [ -f "$f" ]; then
    dire "écrit : $f $(sha256sum "$f" | cut -d' ' -f1) ; $(wc -c < "$f" | tr -d ' ') octets ; compagnon égal : $([ "$(cut -d' ' -f1 "$f.sha256" 2>/dev/null)" = "$(sha256sum "$f" | cut -d' ' -f1)" ] && echo oui || echo non)"
  else dire "non écrit : $f"; fi
done
dire "journal du registre propre : $(wc -l < "$JOURNAL" | tr -d ' ') ligne(s), dont $(grep -c 'OUVERTURE-BBIS' "$JOURNAL") d'ouverture"
dire "lignes de statut de l'arbre de lecture : $(git status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
} > "$R" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/releve-apres-lancement-lecture-bbis-$N-v1.txt"
cat "$R"
```

- L'opérateur n'affiche pas la sortie gardée. Il ne lit que ce relevé : code, comptes de lignes, noms, tailles, empreintes.
- La sortie de **chaque** lancement est gardée et scellée, quel que soit le code (complément, « La suite », point 3 ; condition de la fiche de rattachement).
~~~~

Nouveau :

~~~~text
À jouer quand `lancement-<N>.code` existe, ou quand le processus est absent deux relevés de suite.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1
RUNL="$(cat "$T/run-lecture-$N.txt")"; SORTIE="$T/sortie-lancement-$N.txt"
if [ -e "$T/lancement-$N.code" ]; then CODE="$(cat "$T/lancement-$N.code")"
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
else CODE=absent; fi
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"; neuf "$G1"
cp "$SORTIE" "$G1" && sceller "registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt"
L1="$LV1/lancement-lecture-bbis-$N-v1.sh"; neuf "$L1"
cp "$T/lancement-$N.sh" "$L1" && sceller "registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh"
S_N="$(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
AR_N="$(grep -c '^BBIS LECTURE ARRET' "$G1")"
F="diag/$RUNL/lecture-bbis.json"; M="runs/$RUNL/manifeste.json"
R="$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt"; neuf "$R"
ecrit() { if [ -f "$ARBRE/$1" ]; then dire "$2 : $1 $(sha256sum "$ARBRE/$1" | cut -d' ' -f1) ; compagnon égal : $([ "$(cut -d' ' -f1 "$ARBRE/$1.sha256" 2>/dev/null)" = "$(sha256sum "$ARBRE/$1" | cut -d' ' -f1)" ] && echo oui || echo non)"; else dire "$2 : non écrit"; fi; }
{
dire "Relevé d'après lancement n° $N — run de lecture $RUNL"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null) ; identifiant du processus $(cat "$T/lancement-$N.pid")"
dire "code de sortie : $CODE"
dire "sortie gardée : registres/t07-etape-b-bis/lecture-v1/sortie-lancement-lecture-bbis-$N-v1.txt $(sha256sum "$G1" | cut -d' ' -f1)"
dire "lancement gardé : registres/t07-etape-b-bis/lecture-v1/lancement-lecture-bbis-$N-v1.sh $(sha256sum "$L1" | cut -d' ' -f1)"
if [ "$CODE" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : écrit"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
elif [ "$CODE" = 3 ] && [ "$NC_N" = 1 ] && [ "$S_N" = 0 ] && [ -f "$ARBRE/$F" ]; then
  dire "ETAT : non consommée (pur défaut de mise en place, rien d'ouvert)"
  ecrit "$F" "fichier de lecture gardé"; ecrit "diag/$RUNL/preuve-aucune-ouverture-bbis.json" "pièce de preuve"; ecrit "$M" "manifeste"
elif [ "$CODE" = 0 ] || [ "$CODE" = 3 ]; then
  dire "ETAT : non prévu (code $CODE sans les fichiers ou les lignes attendus)"
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N ; lignes « BBIS LECTURE NON CONSOMMEE » : $NC_N ; lignes « BBIS LECTURE ARRET » : $AR_N"
  ecrit "$F" "fichier de lecture"; ecrit "$M" "manifeste"
  dire "dernières lignes de la sortie gardée (compte de la ligne du seuil : zéro ; rien n'a été ouvert, la sortie ne peut porter aucune mesure) :"
  tail -n 40 "$G1"
  dire "(fin de l'extrait)"
else
  dire "ETAT : arrêt après le seuil"
  dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $S_N"
fi
dire "lignes de statut de l'arbre de lecture : $(git -C "$ARBRE" status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
} > "$R" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/releve-apres-lancement-lecture-bbis-$N-v1.txt"
cat "$R"; sha256sum "$R"
```

- **Ce relevé est ce que l'opérateur rend à la conductrice**, avec son chemin et son empreinte. Il ne porte que : le code de sortie, l'état, des noms, des empreintes.
- **État « écrit »** (second complément, point 5) : le relevé dit « écrit », le chemin, l'empreinte, le code de sortie, **et rien qui distingue une lecture faite d'une issue « non lue » de fond** : ni le compte de la ligne du seuil, ni le motif d'un refus, ni la taille du fichier, ni une clé du fichier. L'opérateur n'ajoute rien de tel dans son message.
- **Deux exceptions nécessaires**, parce qu'elles commandent une suite et ne portent aucune issue de mesure : l'état « non consommée » (code 3 et ligne `BBIS LECTURE NON CONSOMMEE`) et l'état « arrêt avant le seuil » sont rendus comme tels.
- **Arrêt avant le seuil** (second complément, point 3) : le relevé porte le code de sortie, les trois comptes de lignes, et les quarante dernières lignes de la sortie gardée, **si et seulement si** le compte de la ligne du seuil est zéro. Une trace d'erreur du programme ou un refus de ses options, qui n'impriment pas la ligne `BBIS LECTURE ARRET`, y sont donc compris. Si le compte du seuil n'est pas zéro, aucune ligne de la sortie n'est extraite.
- L'opérateur n'affiche jamais la sortie gardée elle-même. La sortie de **chaque** lancement est gardée et scellée, quel que soit le code (complément au quatrième addendum, « La suite », point 3 ; condition de la fiche de rattachement). La conductrice la commite sans l'ouvrir.
~~~~

### 18. § 5.2, constat de forme pour le juge seul

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
### 5.3 Les suites, par code de sortie et par lignes imprimées
~~~~

Nouveau :

~~~~text
#### Constat de forme, pour le juge seul

À jouer dans les états « écrit » et « non consommée ». La pièce est écrite et scellée **sans être affichée** ; l'opérateur n'en rend que le chemin et l'empreinte ; **la conductrice ne l'ouvre pas** ; elle est donnée au juge. Elle ne porte aucune valeur de mesure : des présences de clés, les comptes de lignes de la sortie gardée, le motif d'un refus de la garde (noms de lignes, de fichiers et de commits), la liste des fichiers ouverts par la chaîne.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q -E '^ETAT : (écrit|non consommée)' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "aucun fichier de lecture écrit : pas de constat de forme"; exit 1; }
C="$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"; neuf "$C"
G1="$LV1/sortie-lancement-lecture-bbis-$N-v1.txt"
{
dire "Constat de forme pour le juge — lancement n° $N, run de lecture $RUNL — pièce que la conductrice n'ouvre pas"
dire "lignes du seuil « BBIS LECTURE ENTREES OUVERTES » : $(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"
dire "lignes « BBIS LECTURE ECRITE » : $(grep -c '^BBIS LECTURE ECRITE ' "$G1")"
dire "lignes « BBIS LECTURE NON CONSOMMEE » : $(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
dire "lignes « BBIS LECTURE ARRET » : $(grep -c '^BBIS LECTURE ARRET' "$G1")"
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
dire "octets du fichier de lecture : $(wc -c < "$ARBRE/diag/$RUNL/lecture-bbis.json" | tr -d ' ')"
"$PY" - "$ARBRE/diag/$RUNL/lecture-bbis.json" <<'EOF'
import json, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))["resultat"]
g = r.get("garde")
print("clé garde présente :", g is not None)
if g is not None:
    print("nature du refus :", g.get("nature"))
    print("motif du refus :", g.get("refus"))
    print("preuve d'aucune ouverture conforme :", (g.get("aucune_ouverture") or {}).get("conforme"))
print("clé cellules présente :", "cellules" in r)
print("clé p3bis présente :", "p3bis" in r)
print("règle d'ordre des lignes :", (r.get("ordre_propre") or {}).get("regle"))
print("lecture réelle (essai faux) :", r.get("essai") is False)
print("fichiers ouverts par la chaîne :")
for p in r.get("entrees_lues") or []:
    print("  ", p)
EOF
} > "$C" 2>&1
sceller "registres/t07-etape-b-bis/lecture-v1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt"
echo "constat de forme écrit, non affiché : $C $(sha256sum "$C" | cut -d' ' -f1)"
```

- Exception : dans l'état « non consommée », la conductrice et la mère ont besoin du motif du refus pour décider de la relance. L'opérateur le leur rend par une seule ligne, extraite de la pièce de preuve écrite par le module et non de ce constat : `grep -o '"motif": "[^"]*"' "$ARBRE/diag/$RUNL/preuve-aucune-ouverture-bbis.json"`. Ce motif ne peut porter aucune mesure : rien n'a été ouvert.

### 5.3 Les suites, par code de sortie et par lignes imprimées
~~~~

### 19. § 5.3

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
Notation : S = nombre de lignes du seuil `BBIS LECTURE ENTREES OUVERTES` ; E, NC, AR = nombres de lignes `ECRITE`, `NON CONSOMMEE`, `ARRET`.

| cas | code | S | autres lignes | ce que c'est | ce que fait l'opérateur |
|---|---|---|---|---|---|
| A | 0 | 1 | E = 1 | fichier de lecture écrit après ouverture des entrées | constat de forme (bloc ci-dessous), puis A1 ou A2 |
| B | 0 | 0 | E = 1 | refus de la garde, **de fond** (ou de mise en place sans preuve conforme) : issue « non lue », phrase gelée écrite par le module | **lecture consommée ; arrêt** ; rend le relevé et le motif du refus (bloc ci-dessous) ; n'inscrit rien |
| C | 3 | 0 | NC = 1 | issue « non lue » née d'un **pur défaut de mise en place**, pièce de preuve écrite | **rien n'est inscrit ; arrêt** ; rend le relevé, les deux chemins et empreintes de la ligne `NON CONSOMMEE`, le motif du refus |
| D | 2, ou tout autre code que 0 et 3 | 0 | E = 0, NC = 0 | arrêt du programme **avant le seuil**, sans rien écrire | **voie fermée : arrêt, aucune relance** ; rend le relevé et la ligne `BBIS LECTURE ARRET` (elle ne peut porter aucune mesure : rien n'a été ouvert) |
| E | tout code autre que 0 | 1 | — | arrêt **après le seuil** | **lecture consommée ; arrêt ; nœud** ; rend le relevé seul, sans afficher la sortie |
| F | toute autre combinaison | — | — | état non prévu | arrêt ; nœud ; rend le relevé seul |

Constat de forme, pour les cas A, B et C seulement. Il n'imprime que des présences de clés, le motif de la garde (qui ne porte que des noms de lignes, de fichiers et de commits) et la liste des fichiers ouverts par la chaîne ; aucune valeur de mesure, aucun état, aucune issue.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
C="$LV1/constat-forme-lecture-bbis-$N-v1.txt"; neuf "$C"
"$PY" - "$ARBRE/diag/$RUNL/lecture-bbis.json" > "$C" <<'EOF'
import json, sys
r = json.load(open(sys.argv[1], encoding="utf-8"))["resultat"]
g = r.get("garde")
print("clé garde présente :", g is not None)
if g is not None:
    print("nature du refus :", g.get("nature"))
    print("motif du refus :", g.get("refus"))
    print("preuve d'aucune ouverture conforme :", (g.get("aucune_ouverture") or {}).get("conforme"))
print("clé cellules présente :", "cellules" in r)
print("clé p3bis présente :", "p3bis" in r)
print("règle d'ordre des lignes :", (r.get("ordre_propre") or {}).get("regle"))
print("lecture réelle (essai faux) :", r.get("essai") is False)
print("fichiers ouverts par la chaîne :")
for p in r.get("entrees_lues") or []:
    print("  ", p)
EOF
sceller "registres/t07-etape-b-bis/lecture-v1/constat-forme-lecture-bbis-$N-v1.txt"; cat "$C"
```

- **A1 — lecture faite** : clé `garde` absente et clé `cellules` présente. Suite : § 5.4.
- **A2 — issue « non lue » de fond, épreuve du signal planté** : clé `garde` absente, clé `cellules` absente, clé `p3bis` présente. La phrase gelée est écrite par le module. **Lecture consommée ; arrêt** ; l'opérateur rend le relevé et ce constat, n'inscrit rien.
- **B** : le constat donne la nature et le motif. L'opérateur les rend mot pour mot.
- **C — ce que la conductrice et la mère décident ensuite**, selon « La suite » du complément : panne corrigée sur l'arbre de lecture seulement ; déclaration `registres/t07-etape-b-bis/lecture-v1/declaration-panne-mise-en-place-bbis-<n>-v1.md`, scellée, qui cite tous les lancements antérieurs et leurs sorties gardées ; ligne `PANNE-MISE-EN-PLACE-BBIS-<n>` inscrite par la mère au registre voisin avant la relance ; correction, fichier de lecture gardé, pièce de preuve, manifeste du run refusé et déclaration commités sur la branche de l'arbre de lecture ; arbre vérifié propre ; relance par cette même commande, à partir du § 4.2, avec `N` augmenté de un et, à la place de la ligne qui fixe `RUNL`, le nom du run refusé suivi de `-relance<n>`. **L'opérateur ne fait rien de cela sans un mot de la conductrice** ; il ne corrige pas de son chef.
- **D — voie fermée** jusqu'au mot de Lazar sur le point ouvert 7 du complément. Le programme `scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py` **n'est pas joué** sans ce mot.
- **E** : aucune relance sous aucun texte ; nœud de Lazar (complément, « Tout arrêt après une ouverture consomme la lecture »).
~~~~

Nouveau :

~~~~text
L'opérateur agit d'après la ligne `ETAT` du relevé du § 5.2, et d'elle seule.

| état du relevé | ce que c'est | ce que fait l'opérateur | ce qu'il rend à la conductrice |
|---|---|---|---|
| **écrit** (code 0, fichier de lecture écrit) | la lecture a eu lieu au sens du texte : lecture faite, ou issue « non lue » de fond écrite par le module avec sa phrase gelée ; dans les deux cas **la lecture est consommée** et le module a écrit sa ligne au journal | constat de forme pour le juge ; puis § 5.4, **le même geste dans tous les cas** : sorties portées, ligne `LECTURE-BBIS`, journal | « écrit », chemins, empreintes, code de sortie, la ligne ajoutée au registre propre ; rien d'autre |
| **non consommée** (code 3, ligne `BBIS LECTURE NON CONSOMMEE`, seuil à zéro) | issue « non lue » née d'un pur défaut de mise en place ; le module a écrit la pièce de preuve ; rien n'a été ouvert | constat de forme pour le juge ; **rien n'est inscrit ; arrêt** | l'état, les chemins et empreintes du relevé, le motif du refus |
| **arrêt avant le seuil** (ni code 0 ni code 3 ; seuil à zéro) | le programme s'est arrêté sans rien ouvrir ni rien écrire | **arrêt ; aucune relance** ; § 5.5 | le relevé, qui porte l'extrait de la sortie |
| **arrêt après le seuil** (ni code 0 ni code 3 ; seuil imprimé) | arrêt après la première ouverture d'une entrée | **lecture consommée ; arrêt ; nœud** | le relevé seul ; aucune ligne de la sortie |
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |

- **État « non consommée » — ce que la conductrice et la mère décident ensuite**, selon « La suite » du complément au quatrième addendum : panne corrigée sur l'arbre de lecture seulement ; déclaration `registres/t07-etape-b-bis/lecture-v1/declaration-panne-mise-en-place-bbis-<n>-v1.md`, scellée, qui cite tous les lancements antérieurs et leurs sorties gardées ; ligne `PANNE-MISE-EN-PLACE-BBIS-<n>` inscrite par la mère au registre voisin avant la relance ; correction, fichier de lecture gardé, pièce de preuve, manifeste du run refusé et déclaration commités sur la branche de l'arbre de lecture, poussée de nouveau par la conductrice (§ 4.1) ; arbre vérifié propre ; relance par cette même commande, à partir du § 4.2, avec `N` augmenté de un et, à la place de la ligne qui fixe `RUNL`, le nom du run refusé suivi de `-relance<n>`. **L'opérateur ne fait rien de cela sans un mot de la conductrice** ; il ne corrige pas de son chef.
- **État « arrêt après le seuil »** : aucune relance sous aucun texte ; nœud de Lazar (complément au quatrième addendum, « Tout arrêt après une ouverture consomme la lecture »). Un processus disparu après le seuil en relève aussi.
~~~~

### 20. § 5.4 et § 5.5 (points 5 et 6)

**Fondement** : point 6 : voie de l'arrêt avant le seuil ouverte par anticipation par la session mère, avec sa réserve.

Ancien :

~~~~text
### 5.4 Lecture faite (cas A1) : sorties portées, ligne `LECTURE-BBIS`, journal

Le module a déjà scellé ses sorties. L'opérateur les porte, à l'octet, de l'arbre de lecture à l'arbre principal, puis ajoute la ligne au registre propre de l'arbre principal par la fonction du code (`registre_bbis_v2.ajouter_ligne_propre`, l. 95-120 : ligne ajoutée, jamais réécrite ; refus si la clé est déjà là, si le registre n'est pas le registre propre, ou si une clé de l'étape B bis est au registre partagé).

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^clé garde présente : False$' "$LV1/constat-forme-lecture-bbis-$N-v1.txt" && grep -q '^clé cellules présente : True$' "$LV1/constat-forme-lecture-bbis-$N-v1.txt" || { echo "ce n'est pas le cas A1 : arrêt"; exit 1; }
cd "$DEPOT" || exit 1
neuf "runs/$RUNL"; neuf "diag/$RUNL"; mkdir -p "runs/$RUNL" "diag/$RUNL"
for f in "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json"; do
  cp "$ARBRE/$f" "$f" && cp "$ARBRE/$f.sha256" "$f.sha256" || { echo "copie de $f : arrêt"; exit 1; }
  cmp -s "$ARBRE/$f" "$f" || { echo "copie de $f différente : arrêt"; exit 1; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json" || { echo "sceau des sorties : arrêt"; exit 1; }
# journal : celui de l'arbre de lecture est celui de l'arbre principal plus une ligne
[ "$(wc -l < "$JOURNAL" | tr -d ' ')" = 1 ] && [ "$(wc -l < "$ARBRE/$JOURNAL" | tr -d ' ')" = 2 ] && [ "$(head -n 1 "$ARBRE/$JOURNAL")" = "$(cat "$JOURNAL")" ] || { echo "journal : état inattendu : arrêt"; exit 1; }
tail -n 1 "$ARBRE/$JOURNAL" >> "$JOURNAL"
# ligne LECTURE-BBIS, par la fonction du code
PYTHONPATH=src "$PY" - "$RUNL" <<'EOF'
import sys, time
from pathlib import Path
from controle_ia.scellement import empreinte
from controle_ia.t07bbis.registre_bbis_v2 import REGISTRE_PROPRE, ajouter_ligne_propre
chemin = f"diag/{sys.argv[1]}/lecture-bbis.json"
print(ajouter_ligne_propre(Path("."), REGISTRE_PROPRE, "LECTURE-BBIS", int(time.time()), chemin, empreinte(chemin)))
EOF
tail -n 1 "$JOURNAL" | cut -c1-200
git status --porcelain --untracked-files=all
```

- **Format de la ligne** : celui du registre propre, `| LECTURE-BBIS | AAAA-MM-JJTHH:MM:SSZ | diag/<run>/lecture-bbis.json | sha256 |` (`t07/registre_v1.ecrire_ligne`, l. 318-322).
- Rien n'est écrit dans `registres/scellements-v1.md`.
- L'opérateur rend : la ligne ajoutée (clé, heure, chemin, empreinte), la dernière ligne du journal (elle ne porte qu'une date, le nom du run et une empreinte), les chemins et empreintes des sorties, le PID, les heures de début et de fin, le code de sortie, et la liste « fichiers ouverts par la chaîne » du constat de forme. **Aucun chiffre de mesure, aucune issue.**
- L'arbre de lecture et sa branche locale ne sont pas retirés par l'opérateur.
~~~~

Nouveau :

~~~~text
### 5.4 État « écrit » : sorties portées, ligne `LECTURE-BBIS`, journal

Le module a déjà scellé ses sorties et écrit sa ligne au journal de l'arbre de lecture. L'opérateur porte les sorties, à l'octet, de l'arbre de lecture à l'arbre principal, puis ajoute la ligne au registre propre de l'arbre principal par la fonction du code (`registre_bbis_v2.ajouter_ligne_propre`, l. 95-120 : ligne ajoutée, jamais réécrite ; refus si la clé est déjà là, si le registre n'est pas le registre propre, ou si une clé de l'étape B bis est au registre partagé).

**Le geste est le même que le fichier porte une lecture faite ou une issue « non lue » de fond** : l'opérateur ne le sait pas et n'a pas à le savoir. Fondement : le plan, point 10 (f), fait suivre tout résultat écrit de la ligne `LECTURE-BBIS` ; le complément au quatrième addendum, § 3, la veut « inscrite une seule fois, pour le fichier de la lecture qui compte », et une lecture consommée est celle qui compte ; le second complément du mandat, point 5, veut que rien ne distingue les deux cas pour la conductrice.

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : écrit$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « écrit » : arrêt"; exit 1; }
[ -e "$LV1/constat-forme-pour-le-juge-lecture-bbis-$N-v1.txt.sha256" ] || { echo "constat de forme pour le juge non écrit : arrêt"; exit 1; }
cd "$DEPOT" || exit 1
neuf "runs/$RUNL"; neuf "diag/$RUNL"; mkdir -p "runs/$RUNL" "diag/$RUNL"
for f in "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json"; do
  cp "$ARBRE/$f" "$f" && cp "$ARBRE/$f.sha256" "$f.sha256" || { echo "copie de $f : arrêt"; exit 1; }
  cmp -s "$ARBRE/$f" "$f" || { echo "copie de $f différente : arrêt"; exit 1; }
done
PYTHONPATH=src "$PY" -m controle_ia.scellement verifier "runs/$RUNL/manifeste.json" "diag/$RUNL/lecture-bbis.json" || { echo "sceau des sorties : arrêt"; exit 1; }
# journal : celui de l'arbre de lecture est celui de l'arbre principal plus une ligne
[ "$(wc -l < "$JOURNAL" | tr -d ' ')" = 1 ] && [ "$(wc -l < "$ARBRE/$JOURNAL" | tr -d ' ')" = 2 ] && [ "$(head -n 1 "$ARBRE/$JOURNAL")" = "$(cat "$JOURNAL")" ] || { echo "journal : état inattendu : arrêt"; exit 1; }
tail -n 1 "$ARBRE/$JOURNAL" >> "$JOURNAL"
# ligne LECTURE-BBIS, par la fonction du code
PYTHONPATH=src "$PY" - "$RUNL" <<'EOF'
import sys, time
from pathlib import Path
from controle_ia.scellement import empreinte
from controle_ia.t07bbis.registre_bbis_v2 import REGISTRE_PROPRE, ajouter_ligne_propre
chemin = f"diag/{sys.argv[1]}/lecture-bbis.json"
print(ajouter_ligne_propre(Path("."), REGISTRE_PROPRE, "LECTURE-BBIS", int(time.time()), chemin, empreinte(chemin)))
EOF
tail -n 1 "$JOURNAL" | cut -c1-200
git status --porcelain --untracked-files=all
```

- **Format de la ligne** : celui du registre propre, `| LECTURE-BBIS | AAAA-MM-JJTHH:MM:SSZ | diag/<run>/lecture-bbis.json | sha256 |` (`t07/registre_v1.ecrire_ligne`, l. 318-322).
- Rien n'est écrit dans `registres/scellements-v1.md`.
- L'opérateur rend : « écrit » ; la ligne ajoutée (clé, heure, chemin, empreinte) ; la dernière ligne du journal (elle ne porte qu'une date, le nom du run et une empreinte) ; les chemins et empreintes des sorties et du constat de forme pour le juge ; l'identifiant du processus, les heures de début et de fin, le code de sortie. **Aucun chiffre de mesure, aucune issue, rien du constat de forme.** La liste des fichiers de résultat ouverts par la chaîne est dans le constat de forme, pour le juge ; à la conductrice, l'opérateur rend seulement : « à l'œil : aucun ; par la chaîne : liste dans le constat de forme ».
- L'arbre de lecture et sa branche locale ne sont pas retirés par l'opérateur.

### 5.5 État « arrêt avant le seuil » : conduite, et preuve après coup sur ordre écrit seulement

- **Statut de cette voie** (second complément, point 6). Le complément scellé au quatrième addendum la dit « fermée tant que Lazar n'a pas dit son mot sur le point ouvert 7 ». La session mère l'a ouverte **par anticipation, sous son autonomie** (messages du 2026-11-18 à 23:08:42Z et 23:09:34Z ; R-3514, R-3516 ; autonomie GO-2026-11-18-61), dans cette forme : la preuve après coup compare les fichiers au commit épinglé des sorties `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`, après vérification de `sondes-bbis.json` contre la ligne `SCORES-BBIS`, sans décoder ce fichier. **Réserve, à porter si la voie sert** : ce qui l'ouvre est l'autonomie de la mère, non un mot de Lazar sur ce point.
- **Conduite.** Sur un arrêt avant le seuil, l'opérateur **ne relance pas** et ne corrige rien. Il rend le relevé du § 5.2 et s'arrête. Il joue le programme de la preuve après coup **seulement sur ordre écrit de la conductrice**, rend la pièce (chemin, empreinte, la ligne imprimée par le programme, son code de sortie) et s'arrête de nouveau. **La mère confirme avant toute relance** ; la suite est alors celle de l'état « non consommée » (§ 5.3), la pièce de preuve après coup tenant lieu du fichier de lecture gardé et de la pièce écrite par la garde.
- **La ligne, à ne jouer que sur cet ordre écrit** (`scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py`, `b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675`, cité par la fiche de rattachement ; usage : son en-tête, l. 35-37). Elle donne **toutes** les sorties gardées des lancements antérieurs, une paire chemin et empreinte par lancement :

```bash
. /tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/lecture-bbis/parametres.sh
N=1; RUNL="$(cat "$T/run-lecture-$N.txt")"
grep -q '^ETAT : arrêt avant le seuil$' "$LV1/releve-apres-lancement-lecture-bbis-$N-v1.txt" || { echo "l'état n'est pas « arrêt avant le seuil » : arrêt"; exit 1; }
egal "empreinte du programme de la preuve après coup" b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675 "$(sha256sum "$ARBRE/scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py" | cut -d' ' -f1)"
[ "$FAUTES" = 0 ] || { echo "programme d'une autre empreinte : arrêt"; exit 1; }
set --
for n in $(seq 1 "$N"); do g="$LV1/sortie-lancement-lecture-bbis-$n-v1.txt"; set -- "$@" --sortie-lancement "$g" "$(sha256sum "$g" | cut -d' ' -f1)"; done
cd "$ARBRE" || exit 1
"${NETTOYE[@]}" PYTHONDONTWRITEBYTECODE=1 "$PY" scripts/preuve_aucune_ouverture_apres_coup_bbis_v1.py --racine "$ARBRE" --run-lecture "$RUNL" --run-bbis "$RUN_BBIS" --numero "$N" "$@"
echo "code de sortie du programme de la preuve après coup : $?"
```

- Le programme écrit et scelle lui-même sa pièce, dans l'arbre de lecture : `registres/t07-etape-b-bis/lecture-v1/preuve-aucune-ouverture-apres-coup-bbis-<N>-v1.json`. Il n'imprime que des chemins, des empreintes et des états ; il refuse de partir sous une variable `GIT_` (d'où l'environnement nettoyé).
- Code 0 : pièce conforme ; code 1 : pièce écrite, non conforme (« lecture consommée » ou « nœud », selon son classement) ; code 2 : rien d'écrit. Dans les trois cas l'opérateur rend et s'arrête ; il ne rejoue pas le programme.
~~~~

### 21. § 6

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
Après, selon le cas (tous sous `registres/t07-etape-b-bis/lecture-v1/`, chacun avec son compagnon) :
- `preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` ;
- `releve-avant-lancement-lecture-bbis-<N>-v1.txt`, `lancement-lecture-bbis-<N>-v1.sh`, `sortie-lancement-lecture-bbis-<N>-v1.txt`, `releve-apres-lancement-lecture-bbis-<N>-v1.txt`, `constat-forme-lecture-bbis-<N>-v1.txt` ;
- cas A1 : `runs/<run>/manifeste.json`, `diag/<run>/lecture-bbis.json`, leurs compagnons ; le registre propre (ligne `LECTURE-BBIS`) ; le journal (seconde ligne) ;
- cas A2, B, C : les fichiers écrits par le module restent dans l'arbre de lecture, cités par chemin et empreinte dans le relevé ; la conductrice décide, avec la mère, de leur port sur la branche de travail ;
- les relevés de mise en place restent dans le dossier temporaire ; la conductrice peut les faire porter et sceller si elle les veut au dépôt.
~~~~

Nouveau :

~~~~text
Entre les deux temps de l'opérateur (§ 4.1) : la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`. Ce n'est pas un commit de la branche de travail.

Après, selon l'état (tous sous `registres/t07-etape-b-bis/lecture-v1/`, chacun avec son compagnon) :
- `preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` ;
- `releve-avant-lancement-lecture-bbis-<N>-v1.txt`, `lancement-lecture-bbis-<N>-v1.sh`, `sortie-lancement-lecture-bbis-<N>-v1.txt`, `releve-apres-lancement-lecture-bbis-<N>-v1.txt` ; la sortie gardée est commitée **sans être ouverte** ;
- `constat-forme-pour-le-juge-lecture-bbis-<N>-v1.txt`, commité **sans être ouvert**, donné au juge par son chemin et son empreinte ;
- état « écrit » : `runs/<run>/manifeste.json`, `diag/<run>/lecture-bbis.json`, leurs compagnons, commités sans être ouverts ; le registre propre (ligne `LECTURE-BBIS`) ; le journal (seconde ligne) ;
- état « non consommée » : les fichiers écrits par le module restent dans l'arbre de lecture, cités par chemin et empreinte dans le relevé, et sont commités sur la branche de l'arbre de lecture avant une relance (§ 5.3) ;
- état « arrêt avant le seuil », si la preuve après coup a été ordonnée : sa pièce reste dans l'arbre de lecture, de même ;
- les relevés de mise en place restent dans le dossier temporaire ; la conductrice peut les faire porter et sceller si elle les veut au dépôt.
~~~~

### 22. § 6, fin

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
Jamais commités sur la branche de travail : les 32 fichiers d'entrée de l'arbre de lecture, ni la branche locale `lecture/bbis-arbre-de-lecture-v1`.
~~~~

Nouveau :

~~~~text
Jamais commités sur la branche de travail : les 32 fichiers d'entrée de l'arbre de lecture. La branche locale `lecture/bbis-arbre-de-lecture-v1` n'y est jamais fusionnée.
~~~~

### 23. § 7, point 3 des onze

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
les suites sont celles de `GO-2026-11-18-60` et `-64` (§ 5.3). **Reste ouvert** : le point N2 ci-dessous.
~~~~

Nouveau :

~~~~text
les suites sont celles de `GO-2026-11-18-60` et `-64` (§ 5.3, § 5.5). Voir N2 ci-dessous.
~~~~

### 24. § 7, point 4 des onze

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
l'opérateur commite localement (complément du mandat). **Reste ouvert** : N3.
~~~~

Nouveau :

~~~~text
l'opérateur commite localement (complément du mandat) ; la conductrice pousse la branche de l'arbre de lecture avant le lancement (second complément, point 7 ; § 4.1). Voir N3.
~~~~

### 25. § 7, N1

**Fondement** : point 6 : voie de l'arrêt avant le seuil ouverte par anticipation par la session mère, avec sa réserve.

Ancien :

~~~~text
- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4, et leur voie est fermée.** Le module charge le code de la pièce « mots et coût » avant sa garde (`main`, l. 1691) ; ce code vérifie sa propre table de modules gelés, que la commande ne peut pas contrôler sans le jouer. Un arrêt là serait le cas D : aucune relance avant le mot de Lazar sur le point ouvert 7 du complément.
~~~~

Nouveau :

~~~~text
- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4.** Le module charge le code de la pièce « mots et coût » avant sa garde (`main`, l. 1691) ; ce code vérifie sa propre table de modules gelés, que la commande ne peut pas contrôler sans le jouer. Un arrêt là mène au § 5.5 : aucune relance sans la preuve après coup, jouée sur ordre écrit, et la confirmation de la mère.
- **N1 bis — La voie de l'arrêt avant le seuil est ouverte par l'autonomie de la session mère, non par un mot de Lazar** sur le point ouvert 7 du complément au quatrième addendum, qui la dit fermée jusqu'à ce mot (§ 5.5). Réserve à porter au verdict si cette voie sert. Non tranché par un texte scellé.
~~~~

### 26. § 7, N2

**Fondement** : point 5 : le constat de forme va au juge seul ; rien ne distingue, pour la conductrice, une lecture faite d'une issue « non lue » de fond.

Ancien :

~~~~text
- **N2 — Ligne `LECTURE-BBIS` sur une issue « non lue » de fond (cas A2 et B).** Le plan, point 10 (f), fait suivre le résultat de la ligne ; le complément, § 3, dit la ligne « inscrite une seule fois, pour le fichier de la lecture qui compte » ; le complément du mandat dit « arrêt ». La commande suit le complément du mandat : l'opérateur n'inscrit rien, la conductrice décide. Nœud si elle veut autre chose.
~~~~

Nouveau :

~~~~text
- **N2 — Ligne `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise** (§ 5.4). C'est la seule conduite qui ne laisse rien voir à la conductrice (second complément, point 5), et elle suit le plan, point 10 (f), et le complément au quatrième addendum, § 3. Le premier complément du mandat disait, pour l'issue « non lue » de fond, « lecture consommée ; arrêt » sans parler de la ligne : je lis que l'arrêt vient après l'inscription. Au contre-lecteur de dire si le texte le tranche ainsi, ou « nœud ».
~~~~

### 27. § 7, N3

**Fondement** : point 7 : branche locale de l'arbre de lecture poussée par la conductrice avant le lancement.

Ancien :

~~~~text
- **N3 — Le manifeste de la lecture citera le commit local des entrées, absent du distant.** Le § 4.2 consigne sa tête, son parent et la liste des 32 fichiers, dont chaque objet est égal à celui de sa branche (§ 1.3). Pousser ou non la branche locale n'est tranché par aucun texte.
~~~~

Nouveau :

~~~~text
- **N3 — Commit des entrées cité par le manifeste.** Tranché par le second complément, point 7 : la conductrice pousse la branche de l'arbre de lecture sous `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` avant le lancement ; le § 4.2 vérifie la tête du distant. Il reste que cette branche du distant porte une seconde fois, sous un autre nom, les 32 fichiers d'entrée, dont les fichiers fermés de scores.
~~~~

### 28. § 7, N4

**Fondement** : point 4 : récupération des branches nommées, en lecture seule, permise à l'opérateur.

Ancien :

~~~~text
il joue « la garde » comme une étape (ici : elle est dans le module). À dire dans son message de lancement.
~~~~

Nouveau :

~~~~text
il joue « la garde » comme une étape (ici : elle est dans le module) ; les règles communes lui interdisent tout appel à un service extérieur (ici : la récupération des branches nommées et la lecture des têtes du distant, en lecture seule, § 1.1 et § 4.2, permises par le second complément, point 4, que la conductrice écrit dans son mandat) ; il est lancé en deux temps (§ 0). À dire dans son message de lancement.
~~~~

### 29. § 7, N9

**Fondement** : point 8 : le mandat du juge porte les lignes à citer ; point retiré des points ouverts.

Ancien :

~~~~text
- **N9 — Le feu, § 12, nomme trois lignes d'addenda à citer au verdict** ; il en faut désormais cinq, plus la ligne de rattachement et la réserve R-ORDRE (quatrième addendum, § 3 ; complément, § 3). Hors de cette commande : pour le mandat du juge.
~~~~

Nouveau :

~~~~text
- **N9 — retiré.** Les lignes que le verdict cite (cinq lignes d'addenda, ligne de rattachement, réserve R-ORDRE) sont portées par le complément du mandat du juge, écrit par la conductrice.
~~~~

### 30. § 7, N8

**Fondement** : point 2 : lancement détaché de l'outil ; attente sans jamais arrêter le processus.

Ancien :

~~~~text
- **N8 — Blocs écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée. Une faute d'un bloc d'avant lancement arrête sans rien consommer.
~~~~

Nouveau :

~~~~text
- **N8 — Blocs écrits par simple lecture.** Aucun n'a été joué ; seule leur syntaxe est contrôlée. Une faute d'un bloc d'avant lancement arrête sans rien consommer. Le lancement détaché (`setsid -f`) n'a jamais été éprouvé avec ce module : si l'identifiant du processus n'est pas écrit dans les dix secondes, l'opérateur ne relance pas, relève l'état (§ 5.1 bis) et rend.
~~~~

### 31. § 4, chapeau

**Fondement** : point 6 : voie de l'arrêt avant le seuil ouverte par anticipation par la session mère, avec sa réserve.

Ancien :

~~~~text
sans rien écrire — voie fermée (§ 6, cas D).
~~~~

Nouveau :

~~~~text
sans rien écrire : c'est l'état « arrêt avant le seuil », dont la conduite est au § 5.5.
~~~~

### 32. § 4.2, sous le bloc

**Fondement** : point 6 : voie de l'arrêt avant le seuil ouverte par anticipation par la session mère, avec sa réserve.

Ancien :

~~~~text
sans rien écrire, par la voie fermée. L'opérateur n'ajoute pas
~~~~

Nouveau :

~~~~text
sans rien écrire : état « arrêt avant le seuil » (§ 5.5). L'opérateur n'ajoute pas
~~~~


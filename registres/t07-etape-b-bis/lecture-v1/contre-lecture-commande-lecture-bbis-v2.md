# Contre-lecture de la commande de lecture, version 2 — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrite le 2026-11-18 par le contre-lecteur neuf de la commande (sous-agent, modèle Opus 5.5 ; le préparateur est un Fable 5.2). Je n'ai écrit ni la commande, ni ses différences, ni les addenda, ni le code. Mandat : `mandat-contre-lecteur-commande-bbis-v1.md` (`b0d5ea30…`), règles communes (`5f303a9c…`), grilles : premier et second complément du mandat du préparateur (`9a8b5515…`, `8777bcf5…`), entrées à vérifier : compte rendu d'arrêt du premier contre-lecteur (`a903b87b…`), plus les points (a) à (g) du message de lancement de la conductrice.

**Par simple lecture.** Rien n'a été joué sur le réel : ni la commande, ni un de ses blocs, ni le module, ni sa garde, ni le programme de la preuve après coup, ni une fonction du dépôt. Seul contrôle joué : la syntaxe (`bash -n`) des seize blocs recopiés hors du dépôt, avant et après application des remplacements proposés ci-dessous (seize blocs, aucune erreur, dans les deux états).

## Pièces et empreintes vérifiées (compagnons égaux)

| pièce | empreinte |
|---|---|
| commande version 2 | `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d` |
| différences version 1 → version 2 | `c339543ce913741bc1b29e2649a2afed343bd143959c2cfb87c833bbbb91e8fb` |
| règles communes, mandat, deux compléments, compte rendu d'arrêt | `5f303a9c…`, `b0d5ea30…`, `9a8b5515…`, `8777bcf5…`, `a903b87b…` |
| module qui lit `src/controle_ia/t07bbis/lecture_v5.py` | `dac9f8590784a2bf93d312128b09e89a7a21c04509700f3a3ee8c7a81a28064c` |
| fiche de rattachement | `cd14195d396a779da954619c9a3405741fe11e2f98bf4aae3767cb87a5036ca0` |
| quatrième addendum ; son complément | `5ef929ea…` ; `12c90873…` |
| texte scellé | `0ae6210f…` |
| programme de la preuve après coup | `b7bc7e5d87ba45a696ded6790e1354fd065467f838ef565efba2ff0746b05675` |
| contre-lecture du code | `491ce702…` (compagnon égal) |

## Conclusion : **jouable après corrections mineures**

Aucun constat majeur. Sept corrections mineures (m1 à m7), chacune avec son texte de remplacement exact ; chaque « ancien » ci-dessous a été vérifié présent **une seule fois** dans la version 2. Douze notes (n1 à n12), dont le classement des points ouverts.

Nombre de constats : majeurs 0 ; mineurs 7 ; notes 12.

## Constats mineurs (à corriger sans rejouer la contre-lecture)

### m1 — Lancement : boucle d'attente avec une commande d'attente fixe ; identifiant absent compté comme « processus absent »

- Commande, § 5.1, l. 533 : `for i in 1 … 10; do …; sleep 1; done`. Dans l'outil de terminal de cet environnement, une attente fixe au premier plan est refusée (texte de l'outil : « Foreground `sleep` is blocked »). Si l'opérateur reçoit ce refus, il s'arrête (règles communes, l. 28) : rien n'est lancé, rien n'est consommé, mais le bloc du lancement n'est pas jouable tel quel.
- Commande, § 5.1 bis, l. 554, et § 5.2, l. 572 : `ps -p "$(cat pid)"` avec un fichier d'identifiant vide ou absent rend une erreur, lue comme « processus absent ». Sans la boucle, le fichier peut être encore vide au premier relevé ; avec ou sans elle, un identifiant non écrit ne doit jamais faire passer au § 5.2 comme un arrêt.

Remplacements :

1. § 5.1. Ancien :
```text
for i in 1 2 3 4 5 6 7 8 9 10; do [ -s "$T/lancement-$N.pid" ] && break; sleep 1; done
echo "identifiant du processus du module de lecture : $(cat "$T/lancement-$N.pid" 2>/dev/null)"
```
Nouveau :
```text
echo "lancement détaché ; l'identifiant du processus est relevé par le § 5.1 bis"
```
2. § 5.1 bis. Ancien :
```text
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif ps -p "$(cat "$T/lancement-$N.pid")" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
```
Nouveau :
```text
PID_L="$(cat "$T/lancement-$N.pid" 2>/dev/null)"; echo "identifiant du processus du module de lecture : ${PID_L:-non écrit}"
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif [ -z "$PID_L" ]; then echo "identifiant non écrit : ni « vivant » ni « absent » ; deux relevés de suite ainsi : rendu à la conductrice, rien d'autre"
elif ps -p "$PID_L" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
```
3. § 5.2. Ancien :
```text
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
```
Nouveau :
```text
elif [ ! -s "$T/lancement-$N.pid" ]; then echo "identifiant du processus non écrit : rendu à la conductrice, rien d'autre"; exit 1
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
```
Fondement : second complément, point 2 (identifiant relevé ; attente sans jamais arrêter ; aucun délai d'outil) ; commande, N8 (« si l'identifiant n'est pas écrit […], l'opérateur ne relance pas, relève l'état et rend »).

### m2 — Fin du lancement : compte du seuil ancré à la ligne entière ; sortie non gardée classée « arrêt après le seuil »

- Commande, § 5.2, l. 578 : `grep -c '^BBIS LECTURE ENTREES OUVERTES$'`. Le programme de la preuve après coup compte la même ligne **sans ancrage** (`SEUIL in texte`, l. 303 du programme). Si la ligne du seuil était un jour mêlée à un autre écrit sur la même ligne de la sortie (sortie et erreurs dans le même fichier), la commande compterait zéro, rangerait l'état en « arrêt avant le seuil » et **rendrait à la conductrice les quarante dernières lignes d'une sortie d'après le seuil** ; le programme, lui, classerait « lecture consommée ». Le compte non ancré est le plus prudent pour le classement et pour l'extrait ; la chaîne n'apparaît dans aucun autre message du module (relevé par lecture de `lecture_v5.py` : seule l. 1491 l'imprime).
- Même bloc : si la sortie du lancement n'a pas été gardée (copie impossible : fichier jamais créé, dossier temporaire vidé), `grep -c` sur un fichier absent ne rend rien ; l'état tombe dans la dernière branche, « arrêt après le seuil », avec un compte vide. La conséquence (lecture consommée, nœud) est celle du texte, mais le motif est faux : le complément au quatrième addendum, « La suite », point 3 (l. 198) : « Un lancement sans sortie gardée […] : la lecture est consommée, aucune relance ».

Remplacements (§ 5.2, et table du § 5.3) :

1. Ancien :
```text
S_N="$(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
```
Nouveau :
```text
S_N="$(grep -c 'BBIS LECTURE ENTREES OUVERTES' "$G1" 2>/dev/null)"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1" 2>/dev/null)"
```
2. Ancien :
```text
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
```
Nouveau :
```text
elif [ ! -s "$G1.sha256" ]; then
  dire "ETAT : sortie non gardée (complément au quatrième addendum, « La suite », point 3 : lecture consommée, aucune relance ; nœud)"
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
```
3. Table du § 5.3. Ancien :
```text
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
```
Nouveau :
```text
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
| **sortie non gardée** (ni code 0 ni code 3 ; sortie du lancement absente ou non scellée) | rien ne prouve que le seuil n'a pas été franchi | **lecture consommée ; arrêt ; nœud** (complément au quatrième addendum, « La suite », point 3) | le relevé seul ; aucune ligne de la sortie |
```

### m3 — Les heures de début et de fin distinguent, pour la conductrice, une lecture faite d'une issue « non lue » de fond

- Commande, § 5.2, l. 585 (relevé rendu à la conductrice) et § 5.4, l. 713 (« l'identifiant du processus, les heures de début et de fin, le code de sortie »). Un refus de fond de la garde rend son fichier en quelques secondes ; une lecture faite calcule tous les nuls et tirages. Les deux heures, rendues à la conductrice dans l'état « écrit », trahissent l'issue que le second complément, point 5, interdit de distinguer (« rien qui distingue une lecture faite d'une issue « non lue » de fond »). Elles vont au constat de forme, pour le juge seul ; elles restent au relevé pour les états qui sont déjà des exceptions.

Remplacements :

1. § 5.2. Ancien :
```text
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null) ; identifiant du processus $(cat "$T/lancement-$N.pid")"
```
Nouveau :
```text
dire "identifiant du processus $(cat "$T/lancement-$N.pid" 2>/dev/null)"
[ "$CODE" = 0 ] || dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
```
2. Constat de forme pour le juge. Ancien :
```text
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
```
Nouveau :
```text
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
```
3. § 5.4, rendu. Ancien :
```text
l'identifiant du processus, les heures de début et de fin, le code de sortie.
```
Nouveau :
```text
l'identifiant du processus, le code de sortie (les heures de début et de fin sont dans le constat de forme, pour le juge seul).
```
Reste un canal que la commande ne peut pas fermer : le temps que met l'opérateur à revenir (note n10).

### m4 — Un arrêt avant le seuil évitable : la table des modules gelés de la pièce « mots et coût » se contrôle sans rien jouer

- Commande, N1 (l. 778) : « ce code vérifie sa propre table de modules gelés, que la commande ne peut pas contrôler sans le jouer ». Par lecture : la table est une constante écrite dans le code de la pièce (`scripts/mots_et_cout_t06_v3.py`, l. 104-114, `MODULES_GELES`), comparée par `verifier_modules_geles` (l. 324-341) aux fichiers du paquet importé (`paquet_controle_ia`, l. 317-321 : sous `PYTHONPATH=$ARBRE/src`, le paquet de l'arbre de lecture ; l'environnement virtuel ne porte aucune installation du paquet, relevé par les noms). Un écart y lève `ArretPiece` (sous-classe de `GardeArret`) avant le seuil (`main`, l. 1691), donc un arrêt avant le seuil. Le § 1.4 ne compare que deux des neuf fichiers (`t06/test_croise.py`, `sondes/evaluation.py`) ; les sept autres ne sont tenus que par le diff depuis le commit de la fiche. Une comparaison par empreinte, sur le disque, n'est ni le module ni sa garde. Relevé par le contre-lecteur sur l'arbre principal : les neuf sont aujourd'hui à leur empreinte de table.

Remplacement (§ 1.4, liste des empreintes entières). Ancien :
```text
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
EOF
```
Nouveau :
```text
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173 src/controle_ia/t06/cout.py
a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3 src/controle_ia/t06/lanceur.py
43a244315573eac5cc07cf90089f057ce94878851c01085e0ad64b7ef782849c src/controle_ia/harnais/run_harnais_factice.py
5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae src/controle_ia/environnements/propositions.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d src/controle_ia/manifeste.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2 src/controle_ia/scellement.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439 src/controle_ia/gardes.py
EOF
```
(Les sept empreintes sont recopiées de la table de la pièce, l. 105-114.)

### m5 — Histoire « complète » : les branches du distant sont comparées par leurs noms, non par leurs têtes

- Commande, § 1.1, l. 142-144 : seuls les **noms** des branches du distant sont comparés aux branches de suivi locales ; seule la tête des sorties est comparée. Une branche de suivi locale en retard sur le distant (relevé : 639 branches de suivi dans le dépôt ; l'opérateur n'en récupère que trois) peut cacher un commit qui ajoute `lecture-t07.json` ; la garde cherche le premier ajout « toutes références locales » (`lecture_v5.py`, l. 862-871) et la preuve (B) du § 2 aussi. Le plan, point 2, et le feu, § 12 (« rejouée depuis un clone à histoire complète »), demandent l'histoire complète. Relevé par les noms sur les références locales actuelles : la preuve (B) passerait ; le défaut est de méthode, non de fait.

Remplacement (§ 1.1). Ancien :
```text
  awk '{print $2}' "$T/tetes-du-distant.txt" | sed 's#^refs/heads/#refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
  git for-each-ref --format='%(refname)' refs/remotes/origin | grep -v '/HEAD$' | sort > "$T/noms-locaux.txt"
  egal "branches du distant absentes localement" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
```
Nouveau :
```text
  awk '{print $1" "$2}' "$T/tetes-du-distant.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux.txt"
  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
```
Suite à prévoir (question d'organisation pour la conductrice) : ce contrôle échouera tant que des branches de suivi sont en retard ; il faudra une récupération complète du distant, en lecture seule (`git fetch origin`), que l'opérateur n'a pas la permission de faire (second complément, point 4 : trois branches nommées). Soit la conductrice la fait avant l'étape 0, soit elle l'écrit dans le mandat de l'opérateur. Je recommande en outre de rejouer ces trois lignes au § 4.2, juste avant le lancement (non exigé).

### m6 — La preuve d'antériorité n'est « inscrite à part » qu'après la lecture

- Commande, § 6, l. 747-750 : la pièce `preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` est commitée par la conductrice « Après, selon l'état ». Le feu, § 12, l. 974 : « **Avant cette lecture** : la preuve d'antériorité, rejouée depuis un clone à histoire complète et **inscrite à part** » ; mandat du contre-lecteur, point 2 : « antériorité inscrite à part […] **avant** toute lecture ». La pièce est écrite et scellée avant le lancement (§ 2), mais n'est versée au dépôt qu'après. La faire commiter et pousser entre les deux temps ne touche pas l'arbre de lecture.

Remplacements (§ 6) :

1. Ancien :
```text
Entre les deux temps de l'opérateur (§ 4.1) : la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`. Ce n'est pas un commit de la branche de travail.
```
Nouveau :
```text
Entre les deux temps de l'opérateur (§ 4.1) : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` et son compagnon, commités et poussés sur la branche de travail (preuve « inscrite à part », avant la lecture : feu, § 12) ; puis la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`, qui n'est pas un commit de la branche de travail.
```
2. Ancien (première puce de la liste « Après, selon l'état ») :
```text
- `preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` ;
```
Nouveau : (puce retirée ; chaîne vide).

Si la mère veut une ligne de registre pour cette inscription, c'est une question d'organisation ; aucun texte ne la nomme.

### m7 — Étape 0 : la liste des pièces commitées nomme la version 1

- Commande, § 6, l. 745. Ancien :
```text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md`, sa contre-lecture, leurs compagnons.
```
Nouveau :
```text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v2.md`, ses différences avec la version 1, sa contre-lecture, leurs compagnons (la version 1 et ses pièces restent, R12).
```

## Notes

- **n1 — N2, inscription de `LECTURE-BBIS` sur une issue « non lue » de fond : tranché par le texte, conforme (classement net au point (g)).**
- **n2 — État « arrêt avant le seuil » quand le manifeste du run a été écrit.** Un refus de la garde (seuil non imprimé) suivi d'un échec de l'écriture du fichier de lecture (après la création du manifeste) donne un code 2, seuil à zéro, manifeste écrit. Le § 5.2 le range en « arrêt avant le seuil » alors que la table du § 5.3 dit « sans rien écrire ». Sans danger : le relevé porte « manifeste : … » et la preuve après coup, si elle est ordonnée, rend (A2) non conforme, donc « nœud » (complément, l. 233). Aucune mesure ne peut figurer dans l'extrait (rien n'est ouvert avant le seuil ; le motif du refus n'est pas imprimé).
- **n3 — Chemin de la relance non jouable tel quel.** Le § 5.3 dit « relance par cette même commande, à partir du § 4.2 […] à la place de la ligne qui fixe `RUNL` ». Mais le § 4.2 exige que le parent de la tête soit `TETE_TRAVAIL` et que le commit local ajoute exactement les 32 entrées (l. 449-453) : après les commits de la correction et de la déclaration, ces contrôles rendront « on ne lance pas ». Sans danger (rien n'est consommé) ; une relance demandera une version de la commande écrite pour elle. Hors du premier lancement.
- **n4 — Durée de vie du dossier temporaire.** L'arbre de lecture, la sortie du lancement et le fichier de l'identifiant vivent dans le dossier temporaire de session, qu'un redémarrage ou un nettoyage peut vider. Une sortie perdue consomme la lecture (complément, « La suite », point 3). Question d'organisation pour la conductrice : écrire la sortie du lancement directement sous `registres/t07-etape-b-bis/lecture-v1/` de l'arbre principal (dont la propreté n'est plus contrôlée après le § 1.1), ou ailleurs de durable, hors de l'arbre de lecture.
- **n5 — Histoire coupée sans dépôt superficiel.** Ni les références de remplacement ni le fichier de greffes ne sont contrôlés ; ils couperaient l'histoire sans que `--is-shallow-repository` le dise (la contre-lecture du code, n2, montre qu'une histoire coupée donne un refus **de fond**). Relevé par les noms : aucune référence de remplacement, aucun fichier de greffes, dépôt ni superficiel ni partiel. Une ligne de plus au § 1.1 le fermerait (`egal "références de remplacement" 0 "$(git for-each-ref refs/replace | wc -l | tr -d ' ')"`) ; recommandé, non exigé.
- **n6 — Cadence de l'attente.** Le § 5.1 bis demande des relevés « toutes les dix minutes environ, sans attente longue dans un appel » ; l'outil refuse l'attente fixe au premier plan. L'opérateur doit attendre par l'outil de surveillance de sa session ou par un message différé : à écrire dans son mandat (organisation).
- **n7 — Preuve après coup : empreintes des sorties recalculées au moment de jouer.** Le § 5.5, l. 729, donne au programme l'empreinte de chaque sortie gardée calculée à l'instant sur le fichier lui-même ; le contrôle « à l'empreinte donnée » du programme devient circulaire (le contrôle du compagnon reste). Mieux : reprendre l'empreinte écrite au relevé d'après lancement (« sortie gardée : … »). Recommandé.
- **n8 — Arrêts encore possibles avant le seuil (N1), après m4.** Par lecture de `main` et de `lire` jusqu'à la l. 1491 : erreur d'importation d'un module (trace, code 1) ; erreur à l'exécution du code de la pièce ; `ArretPiece` sur un fichier gelé (fermé par m4) ; ligne `CODE-MOTS-ET-COUT-T06` absente, en double ou mal formée (`lire_lignes` dans `adaptateur_retenu` : refus levé hors du bloc de la garde, donc **arrêt avant le seuil**, non issue I0 ; contrôlé au § 1.3) ; fichier de cette ligne ou module de la pièce d'une autre empreinte, ou absent au commit cité (§ 1.3, § 1.4, § 4.2) ; fils de calcul (fixés par la ligne de lancement) ; variable `GIT_*` ou `BBIS_INSTANCE` (retirées, contrôlées au § 4.2) ; clé de l'étape B bis au registre partagé (`exiger_partage_sans_bbis` lève un arrêt, non un refus ; contrôlé au § 1.3) ; refus des options (quatre options exactes, conformes) ; disque plein, processus disparu. Aucun autre ne peut être exclu sans jouer le code.
- **n9 — Compagnons des entrées.** La commande ne compare que le premier champ des compagnons (`cut -d' ' -f1`), comme `sceau_conforme` ; mais `scellement.verifier` et `lire_manifeste`, appelés **après** le seuil (`lecture_v5.py`, l. 940, 1515), exigent aussi le nom de base exact. Relevé par le contre-lecteur, sur les branches d'origine, par le seul champ du nom des compagnons : les quinze compagnons des entrées de la course (dix) et de la course de confirmation (cinq) portent leur nom de base ; celui de la pièce « mots et coût » n'a pas été relevé. Sans objet aujourd'hui ; une ligne de contrôle du format entier (`<empreinte>  <nom de base>`) au § 1.3 le tiendrait.
- **n10 — Canal du temps, hors de la commande.** Même après m3, la conductrice voit combien de temps l'opérateur met à revenir. Si la mère veut le fermer, c'est d'organisation (par exemple un rendu de l'opérateur à heure fixe, ou par l'intermédiaire du juge).
- **n11 — Fusion de `main` (N10).** Relevé par les noms : fusion sans conflit (le seul fichier ajouté des deux côtés, le programme de la preuve après coup, a le même objet des deux côtés ; le registre voisin n'a changé que du côté de `main`) ; aucun fichier sous `src/` ni la pièce « mots et coût » modifié depuis le commit de la fiche, ni par la branche de travail ni par `main` ; les trois versions figées sont dans `requirements-cpu.txt`. Conforme à N10.
- **n12 — Voie de l'arrêt avant le seuil (N1 bis).** Classement au point (g).

## Jugement sur les points (a) à (g)

### (a) Les blocs, ligne par ligne, contre le code

Conformes, hors m1 à m5 :
- **Fichier des paramètres** : `NETTOYE` retire les onze variables nommées et `BBIS_INSTANCE` ; `G` exécute git dans cet environnement ; `sceller` appelle `controle_ia.scellement sceller` depuis l'arbre principal (signature : `_main`, l. 120-123). Noms de runs, commits nommés (course `438a9c52…`, entrée conjointe `c098fb51…`, remise `06c88328…`) égaux à `EXCEPTION_ORDRE_ADDENDUM_4` (`lecture_v5.py`, l. 612-623) ; commit du scellement `f72d2833…` égal à celui que relève la recherche de la garde (relevé par les noms) ; commit de la pièce `da06bb57…` égal au `commit` de la fiche de `CODE-MOTS-ET-COUT-T06`, et `9dbcc55c…` égal à son empreinte du module.
- **§ 1.2, § 1.3** : les 32 entrées (20 des sorties de la course ; 5 fichiers de la course de confirmation et leurs compagnons ; la pièce « mots et coût » et son compagnon) sont exactement l'ensemble que `entrees_autorisees` (l. 586-601) et les chemins des lignes ouvrent ; aucune n'est suivie aujourd'hui sur la branche de travail ni au commit de `main` (relevé par les noms) : le compte « 32 ajoutés » du § 4.2 tiendra. Les dix fichiers cités par les lignes sont contrôlés à l'empreinte et au compagnon (motifs (M1) et de fond de `verifier_lignes`, l. 669-687 ; `sceau_conforme`, `t07/registre_v1.py`, l. 108-123).
- **§ 1.4** : 63 fichiers de la fiche, à l'empreinte, sur le disque (relevé) ; contrôles des six lignes du registre voisin à l'octet de leur clé ; versions figées présentes.
- **§ 2** : (B) reprend les recherches de `anteriorite_etape_b` (l. 854-877) à l'identique ; (C) l'ordre de `exiger_ordre_propre` (l. 813-844) ; (D) les points (P1) à (P5) de `preuve_entree_conjointe` (l. 690-810) ; (E) les faits du quatrième addendum : relevés par les noms par le contre-lecteur, ils sont tous conformes aujourd'hui (trois premières lignes d'addenda ancêtres du commit de la course ; six lignes ancêtres du commit de `main` ; commit de la fiche ancêtre de la course ; ancêtre commun des sorties et de `main` égal au commit de la course ; tête des sorties antérieure à la date de `SCORES-BBIS`).
- **§ 4.1** : commit local avec signature désactivée (la configuration du dépôt la demande ; la commande la coupe, à juste titre).
- **§ 4.2** : `exiger_prereg_scelle` (`prereg.py`, l. 70-76) rend l'empreinte attendue si le texte est conforme ; par lecture du texte (sections exigées présentes, aucun marqueur, une entrée de contre-lecture portant quatre empreintes, compagnon au format exact), il passera. `lire_fiche_code` (`registre_bbis_v1.py`, l. 163-179) et `exiger_entropie` (`commun_v1.py`, l. 83-89) : appels conformes à leurs signatures. Forme du nom du run égale à `_RUN_ID` (`manifeste.py`, l. 26).
- **§ 5.1** : ligne de lancement conforme à `main` (l. 1682-1687 : quatre options exigées ; `--adaptateur-mc` omis, ligne inscrite avant l'échéance) ; `-m` avec le dossier courant à l'arbre de lecture et `PYTHONPATH` sur `src` de l'arbre : le module, la pièce et `exiger_module_gele` lisent les fichiers de l'arbre de lecture (aucune installation du paquet dans l'environnement virtuel, relevé par les noms). L'identifiant écrit est celui du programme (`env` remplace son processus par celui de Python).
- **§ 5.4** : `registre_bbis_v2.ajouter_ligne_propre` (l. 95-120) a la signature appelée ; format de ligne de `t07/registre_v1.ecrire_ligne` ; rien dans le registre partagé.
- **Journal** : la ligne `OUVERTURE-BBIS` est écrite par `journaliser_ouverture` (`registre_bbis_v1.py`, l. 113-119) une fois, après le fichier de lecture (`main`, l. 1708), dans tout état sauf « non consommée » ; le § 5.4 en tient compte.

### (b) Les cinq constats provisoires : fondés ; traités par la version 2

1. **Contrôle du préenregistrement avant le lancement** : fondé (`ecrire_lecture`, l. 1644-1646 → `creer_manifeste`, l. 85-96 → `exiger_prereg_scelle`, après le seuil). Traité au § 4.2, ainsi que l'arbre propre (git nettoyé), la forme du nom du run, l'absence de son dossier et de ses fichiers, l'écriture possible de `runs` et `diag`, la fiche et l'entropie, les versions. Rien d'autre, hors données, n'est rejoué après le seuil, à l'exception du module gelé de la partition des plis, déjà au § 1.4.
2. **Lancement détaché** : fondé ; traité (`setsid -f`, sorties coupées du terminal, identifiant écrit, attente par relevés de l'état, aucune commande d'arrêt écrite). Reste m1 (attente fixe, identifiant absent) et n6.
3. **Extraction sur un arrêt avant le seuil** : fondé ; traité (code, trois comptes, quarante dernières lignes si le compte du seuil est zéro). **Peut-il y avoir une mesure dans ces lignes ?** Non, si le compte est exact : la ligne du seuil est imprimée et vidée avant la première ouverture d'une entrée (l. 1490-1492) ; avant elle, le module n'a lu que les deux registres, les empreintes des fichiers cités, l'histoire git et le code de la pièce ; aucun message d'avant le seuil ne porte de valeur. Le seul risque est un compte faux : corrigé par m2 (compte non ancré, aligné sur le programme de la preuve après coup ; état « sortie non gardée »).
4. **Récupération des branches en lecture seule** : fondé ; traité (§ 1.1, § 4.2, et la conductrice l'écrit au mandat). Voir m5 pour la portée de la récupération.
5. **Constat de forme au juge seul** : fondé ; traité (pièce scellée sans affichage, chemin et empreinte seuls rendus ; relevé de l'état « écrit » sans compte du seuil, sans taille, sans clé ; même geste du § 5.4 dans les deux cas, journal compris). **Une fuite reste** : les heures de début et de fin (m3) ; et, hors de la commande, le temps de retour (n10). Les deux exceptions (« non consommée » avec son motif, « arrêt avant le seuil » avec son extrait) sont celles que le second complément, point 5, écrit.

### (c) Contrôles d'avant lancement

| ce qu'il faut exclure | où | jugement |
|---|---|---|
| dépôt superficiel | § 1.1, § 2 (A), § 4.2 | tenu |
| dépôt coupé sous un commit nommé | présence et ascendance de chaque commit nommé (§ 1.1, § 2) | tenu pour les coupes superficielles ; coupe par remplacement ou greffes : n5 ; références en retard : m5 |
| variable `GIT_*` restante | § 4.2, par programme, dans l'environnement nettoyé, noms seuls | tenu |
| arbre non propre | § 1.1 (arbre principal), § 4.2 (arbre de lecture, par git nettoyé) | tenu |
| fichier cité absent ou d'empreinte différente | § 1.3 (dix fichiers, compagnons) ; § 1.4 (code, textes) | tenu ; format entier des compagnons : n9 |
| fichier de scores absent | § 1.3 (les 20 fichiers du run de la course, objets égaux à ceux de leur branche, rien de plus ni de moins) | tenu autant qu'il se peut sans ouvrir le fichier fermé des sondes ; un fichier de scores nommé hors de ce dossier serait « non calculable » sans arrêt (quatrième addendum, § 6.5, point 7) |
| lignes du registre voisin manquantes ou en double | § 1.4 (six clés, une fois chacune, sur le disque et au commit de `main`) | tenu |
| fichier de la liste « Jamais » extrait | § 1.2 (extraction par chemins nommés) ; § 1.3 (deux noms de la course de confirmation absents, rien en trop dans les dossiers des entrées) | tenu |
| fichier de lecture ou d'arrêt de l'étape B dans l'arbre | § 1.3, par les noms (`find`, `.git` écarté) ; dossier de l'étape B réduit à l'audit des fuites | tenu ; relevé : aucun suivi aujourd'hui |

### (d) Les fonctions du dépôt appelées avant le lancement

- `prereg.exiger_prereg_scelle` : lit le seul texte scellé et son compagnon (`scellement.verifier`, `prereg.problemes`) ; aucune donnée, aucune commande git, aucun processus ; ce n'est ni le module ni sa garde. Échec à tort : seulement si le texte n'était pas conforme à sa propre règle, et alors l'échec n'est pas à tort (la lecture serait refusée après le seuil) ; par lecture du texte, il passera.
- `registre_bbis_v1.lire_fiche_code` : lit la fiche de code (fichier de code, non de résultat) ; aucun processus. `commun_v1.exiger_entropie` : calcul pur. L'importation de `commun_v1` importe `manifeste` (et numpy) : aucune lecture de donnée. Ni module de lecture ni garde. Échec à tort : non (contrôles de forme que la lecture refait après le seuil).
- Les trois tournent dans l'environnement nettoyé, sans écrire de code compilé (`PYTHONDONTWRITEBYTECODE=1`), sur le code de l'arbre de lecture : rien ne rend l'arbre non propre.

### (e) Étape 0 et lancement en deux temps

- **Fusion locale du commit de `main`** puis **journal avec sa seule ligne d'en-tête**, commités par la conductrice sur la branche de travail : conformes au quatrième addendum, § 6.5, point 8, et au feu, § 12 (« journal […] créé » avant la lecture). Fusion sans conflit (n11).
- **La ligne d'en-tête peut-elle compter comme une ouverture ?** Non. Le module compte les lignes qui contiennent `OUVERTURE-BBIS` (`preuve_aucune_ouverture`, l. 1436) ; le programme de la preuve après coup aussi, sur le disque et dans chaque commit de l'histoire du journal (`point_a1`, l. 159 et 171). L'en-tête ne contient pas cette chaîne. Le § 4.2 compte une ligne, zéro ouverture. Ne pas changer l'en-tête.
- **Deux temps** : arrêt de l'opérateur après le commit local des entrées (§ 4.1) ; poussée par la conductrice de la branche locale sous `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture` (jamais `main`) ; relevé de cette tête sur le distant au § 4.2, avant le lancement : conformes au second complément, point 7. La poussée porte des objets déjà présents sur le distant.
- Écart : m6 (la preuve d'antériorité doit être versée entre les deux temps) et m7.

### (f) Les suites

Conformes au complément au quatrième addendum (« La règle », « La suite », « Tout arrêt après une ouverture consomme la lecture », « Arrêt avant le seuil ») et aux décisions GO-2026-11-18-60 et -64 : écrit → constat pour le juge, sorties portées, ligne `LECTURE-BBIS`, journal ; non consommée (code 3, ligne « non consommée », seuil à zéro) → rien n'inscrit, arrêt, relance seulement sur le mot de la conductrice et la ligne de panne inscrite par la mère ; arrêt avant le seuil → arrêt, aucune relance par l'opérateur, programme de la preuve après coup **seulement sur ordre écrit de la conductrice**, la mère confirme avant toute relance, réserve écrite (« ce qui l'ouvre est l'autonomie de la mère, non un mot de Lazar ») ; arrêt après le seuil → lecture consommée, nœud. Ajout nécessaire : l'état « sortie non gardée » (m2). La relance elle-même demandera une version de la commande (n3).

### (g) Points ouverts de la commande — classement

- **N2 — `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise : TRANCHÉ PAR LE TEXTE, dans le sens de la commande. Conforme.** Lignes :
  - texte scellé, plan, point 10, l. 114 : (a) garde refusée → « rien n'est lu », phrase gelée ; puis (f) « résultat `diag/<run-bbis-lecture>/lecture-bbis.json`, scellé avant toute lecture humaine, ligne `LECTURE-BBIS` » — l'étape (f) suit tout résultat écrit, refus compris ;
  - plan, point 2, l. 99 : ordre « lecture, `LECTURE-BBIS`, verdict, `VERDICT-BBIS` » ; critères gelés, ligne I0, l. 143 : « garde refusée » → « Étape B bis non lue : [motif]. » est une **issue que le verdict prononce** ; le verdict suit `LECTURE-BBIS` ;
  - « Lignes de registre », l. 222 : format seulement ; rien de contraire ;
  - quatrième addendum, § 7, point 4, l. 568-572 : « se rejoue-t-elle sous un nom de run neuf **tant que `LECTURE-BBIS` n'est pas inscrite** » — la ligne marque la lecture consommée ;
  - complément au quatrième addendum, « La suite », point 1, l. 186-188 : « **Aucune ligne `LECTURE-BBIS` n'est inscrite** pour ce fichier » — exception écrite pour le seul refus de pure mise en place prouvé sans ouverture ; a contrario, inscrite dans les autres cas ;
  - même texte, § 3, l. 353-355 : inchangés « la suite de tout refus **de fond** […] ; la ligne `LECTURE-BBIS`, inscrite une seule fois, pour le fichier de la lecture qui compte ».
  Le premier complément du mandat (« lecture consommée ; arrêt ») dit qu'il n'y a pas de relance ; il ne dispense pas de l'inscription. Le code tient la même lecture : une ligne `LECTURE-BBIS` présente fait refuser toute lecture ultérieure (`REFUSEES_PROPRES_LECTURE`, l. 607 ; l. 1472-1474). Ce n'est ni une question d'organisation ni un nœud.
- **N1 — arrêts avant le seuil encore possibles** : question d'organisation, réduite par m4 ; inventaire en n8. Aucun autre ne peut être exclu sans jouer le code.
- **N1 bis — voie de l'arrêt avant le seuil ouverte par l'autonomie de la mère** : **nœud de Lazar** si la voie doit servir à une relance. Le complément scellé, § 7, point 7, l. 570-576 : « Nœud de Lazar […]. La voie de l'arrêt avant le seuil **n'est pas employée avant son mot** » ; la règle du dépôt range un écart à un texte scellé parmi les nœuds. Jouer le programme de la preuve après coup sur ordre écrit n'emploie pas la voie (il relève un état) ; la relance l'emploie. Non bloquant pour le premier lancement ; la commande porte la réserve. Je recommande que la confirmation « de la mère » avant une relance sur cette voie soit le mot de Lazar, ou une décision de la mère déclarée comme écart.
- **N3 — commit des entrées cité par le manifeste** : tranché (second complément, point 7) ; la copie des fichiers fermés sous un second nom de branche, sur un distant privé, est une question d'organisation.
- **N4 — accords du mandat de l'opérateur** : question d'organisation pour la conductrice (son message de lancement), y compris m5 (récupération complète) et n6 (cadence de l'attente).
- **N5 — versions du run de la pièce non comparées** : tranché par le texte (liste d'arrêt, l. 193 : base « non calculable » avec nœud, sans arrêt du reste).
- **N6 — verdict de l'épreuve du signal planté cité par son fichier d'issue, non contrôlé avant** : tranché par le texte. Son nom ne se connaît qu'en ouvrant le fichier d'issue, que la chaîne seule ouvre (plan, point 1, l. 98 ; règles communes, l. 17) ; un fichier absent ou illisible donne une issue « non lue » **de fond** (complément, l. 167 : « l'issue de l'épreuve du signal planté autre que « vu », fichier illisible compris »). L'arbre de lecture, monté de la tête de travail fusionnée avec `main` et propre, porte les fichiers suivis : risque accepté par le texte ; aucune action.
- **N7 — retrait des variables `GIT_*`** : le retrait est exigé par le texte (complément, § 7, point 9). La suite d'un git qui refuserait l'arbre sans elles n'est écrite nulle part : question d'organisation (conductrice, mère). Risque faible : le dépôt et le dossier temporaire appartiennent à l'utilisateur du processus (relevé ; même constat que la contre-lecture du code, n10). Si cela arrivait, le défaut apparaîtrait dès le § 2 (A), avant le § 4.2 : il faut l'y lire comme un défaut d'environnement, non de l'arbre.
- **N8 — blocs jamais joués** : question d'organisation ; m1 traite le seul point du lancement qui pouvait être refusé par l'outil.
- **N9 — retiré** : conforme (complément du mandat du juge).
- **N10 — fusion de `main`** : vérifié (n11).

## Réponse aux huit points du mandat

1. Module en vigueur : `lecture_v5.py`, désigné par le complément au quatrième addendum, CQ-3 ; empreinte égale à la fiche de rattachement et contrôlée par la commande (§ 1.4). Conforme.
2. Ordre : journal créé à l'étape 0 avant toute lecture ; preuve d'antériorité relevée avant le lancement (à verser avant : m6) ; garde en tête de `lire` ; au refus, rien n'est lu. Conforme après m6.
3. Preuve d'antériorité : recherches identiques à la garde, par les noms et les commits ; ne peut pas refuser à tort sur les faits relevés ; passer à tort : seulement par des références en retard (m5) ou une histoire remplacée (n5).
4. Entrées : exactement la liste blanche du code ; rien de la liste « Jamais » ; aucun fichier de l'étape B ne peut être ouvert (liste blanche du module ; absence contrôlée par les noms). Conforme.
5. Arguments, entropie (non passée, lue par le module), graines, chemins, nom du run : conformes ; ligne de commande jouable (m1 pour l'attente).
6. Sorties scellées par le module avant toute lecture humaine ; format de la ligne `LECTURE-BBIS` conforme ; rien dans `registres/scellements-v1.md`. Conforme.
7. Ce que l'opérateur rend : aucune mesure, aucune aire, aucune issue, hors les heures (m3) et le temps de retour (n10).
8. Points ouverts : classés au point (g).

## Fichiers ouverts par le contre-lecteur

- **Fichiers de résultat** : **aucun**, ni à l'œil ni par une chaîne. Aucun fichier de `diag/`, `donnees/`, `runs/`, `docs/verdicts/` ouvert ; ni `registres/etat.md`, ni `registres/decisions.md`, ni `registres/passations/`.
- **Par les noms seulement** (`git ls-tree`, `git log --diff-filter=A`, `git merge-base`, `git rev-parse`) : présence et commit d'ajout des fichiers de lecture ou d'arrêt de l'étape B (aucun contenu) ; fichiers suivis des dossiers des entrées ; ascendance des commits nommés.
- **Champ du nom des compagnons `.sha256`** des quinze entrées de la course et de la course de confirmation, lus sur leurs branches par `git show` et coupés au seul nom de base (aucune empreinte de donnée relevée, aucun fichier de données ouvert) : pour n9.
- **Textes, code, registres** : les pièces de la grille ; `prereg/T0.7-etape-B-bis-v1.md` (plan d'analyse, critères, sections ; marqueurs et section « Contre-lecture » par une recherche écrite par moi, non par une fonction du dépôt) ; le quatrième addendum et son complément (passages cités) ; le feu, § 12 ; `registres/t07-etape-b-bis-v1.md` ; la fiche de code `code-bbis-v2.json` et la fiche `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json` (champs `commit` et `fichiers`) ; le code `lecture_v5.py`, `manifeste.py`, `prereg.py`, `scellement.py`, `gardes.py`, `registre_bbis_v1.py`, `registre_bbis_v2.py`, `commun_v1.py`, `lien_mots_et_cout_v1.py`, `adversaires_texte_v1.py` (deux fonctions), `t07/registre_v1.py` (quatre fonctions), `scripts/mots_et_cout_t06_v3.py` (table des modules gelés), le programme de la preuve après coup ; la contre-lecture du code, notes n2, n3, n4, n10, n11. Empreintes calculées sur des fichiers de code et de texte seulement.
- **Une commande en écart à la liste permise, déclarée** : `git merge-tree --write-tree` sur la tête de travail et le commit de `main`, pour savoir si la fusion de l'étape 0 aurait un conflit ; elle a écrit des objets non référencés dans la base d'objets du dépôt, sans toucher une référence, l'index ni l'arbre de travail.
- Rien dans `.claude/`. Aucun nom de commande d'arrêt de processus écrit dans une ligne de commande jouée ni dans ce rapport. Aucun refus reçu.

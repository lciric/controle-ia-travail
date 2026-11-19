# Différences entre la commande de lecture version 2 et la version 3 — apprentissage des sondes sur la tâche (étape B bis de T0.7)

Écrit par le préparateur (Fable 5.2), le 2026-11-19, par le programme qui a écrit la version 3 à partir de la version 2 : chaque « ancien » figure une seule fois dans la version 2 (vérifié par ce programme, qui refuse sinon) et y est remplacé par son « nouveau » ; rien d'autre n'est changé.

- Version 2 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v2.md`, `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d` (reste, R12).
- Version 3 : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, `195207cf9180c0c667b9dd087f768278ee8ffafea8351a654b2899d32f3df0b3`.
- Fondements : les sept constats mineurs de la contre-lecture de la version 2 (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d0483668df9fc6fb2661c4e4fad1425221a5061049e9731fb7128390925`), portés tels que le rapport les écrit ; trois décisions d'organisation de la conductrice ; ce qui en découle strictement.
- Deux écarts de forme à la lettre du rapport, déclarés : m6, second remplacement, retire la puce avec son retour de ligne (le rapport écrit « chaîne vide ») ; m7 nomme la version 3 et ses pièces là où le rapport, écrit pour la version 2, nommait la version 2.

## Compte des passages changés, par fondement

- 3 — constat m1 de la contre-lecture de la version 2 (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d04…`) : attente fixe refusée par l'outil ; identifiant non écrit
- 3 — constat m2 : compte du seuil non ancré ; état « sortie non gardée »
- 3 — constat m3 : les heures de début et de fin vont au juge seul dans l'état « écrit »
- 1 — constat m4 : table des modules gelés de la pièce « mots et coût » comparée avant le lancement
- 1 — constat m5 : branches du distant comparées par leurs noms et leurs têtes
- 2 — constat m6 : preuve d'antériorité versée au dépôt avant la lecture
- 1 — constat m7, et ce qui en découle strictement (la commande à commiter est la version 3)
- 7 — ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g))
- 3 — décision d'organisation de la conductrice sur m5 : elle fait la récupération complète du distant, en lecture seule, à l'étape 0
- 3 — décision d'organisation de la conductrice sur m6 : elle commite et pousse la pièce de la preuve entre les deux temps de l'opérateur
- 3 — décision d'organisation de la conductrice sur la note n3 : aucune relance n'est jouée sur cette version
- 2 — correction de la session mère (message du 2026-11-18 à 23:36:15Z ; R-3530) et classement du point N1 bis par la contre-lecture de la version 2 (point (g) ; note n12) : toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar

Total : 32 passages. Passages sans fondement : aucun.

## Les passages

### 1. § 5.1, bloc

**Fondement** : constat m1 de la contre-lecture de la version 2 (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d04…`) : attente fixe refusée par l'outil ; identifiant non écrit.

Ancien :

~~~~text
for i in 1 2 3 4 5 6 7 8 9 10; do [ -s "$T/lancement-$N.pid" ] && break; sleep 1; done
echo "identifiant du processus du module de lecture : $(cat "$T/lancement-$N.pid" 2>/dev/null)"
~~~~

Nouveau :

~~~~text
echo "lancement détaché ; l'identifiant du processus est relevé par le § 5.1 bis"
~~~~

### 2. § 5.1 bis, bloc

**Fondement** : constat m1 de la contre-lecture de la version 2 (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d04…`) : attente fixe refusée par l'outil ; identifiant non écrit.

Ancien :

~~~~text
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif ps -p "$(cat "$T/lancement-$N.pid")" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
~~~~

Nouveau :

~~~~text
PID_L="$(cat "$T/lancement-$N.pid" 2>/dev/null)"; echo "identifiant du processus du module de lecture : ${PID_L:-non écrit}"
if [ -e "$T/lancement-$N.code" ]; then echo "fini : code de sortie écrit"
elif [ -z "$PID_L" ]; then echo "identifiant non écrit : ni « vivant » ni « absent » ; deux relevés de suite ainsi : rendu à la conductrice, rien d'autre"
elif ps -p "$PID_L" -o pid=,stat=,etime=; then echo "vivant : on attend"
else echo "processus absent, code de sortie non écrit"; fi
~~~~

### 3. § 5.2, bloc

**Fondement** : constat m1 de la contre-lecture de la version 2 (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d04…`) : attente fixe refusée par l'outil ; identifiant non écrit.

Ancien :

~~~~text
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
~~~~

Nouveau :

~~~~text
elif [ ! -s "$T/lancement-$N.pid" ]; then echo "identifiant du processus non écrit : rendu à la conductrice, rien d'autre"; exit 1
elif ps -p "$(cat "$T/lancement-$N.pid")" > /dev/null 2>&1; then echo "le lancement n'est pas fini : on attend"; exit 1
~~~~

### 4. § 5.2, bloc, comptes

**Fondement** : constat m2 : compte du seuil non ancré ; état « sortie non gardée ».

Ancien :

~~~~text
S_N="$(grep -c '^BBIS LECTURE ENTREES OUVERTES$' "$G1")"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1")"
~~~~

Nouveau :

~~~~text
S_N="$(grep -c 'BBIS LECTURE ENTREES OUVERTES' "$G1" 2>/dev/null)"; NC_N="$(grep -c '^BBIS LECTURE NON CONSOMMEE ' "$G1" 2>/dev/null)"
~~~~

### 5. § 5.2, bloc, états

**Fondement** : constat m2 : compte du seuil non ancré ; état « sortie non gardée ».

Ancien :

~~~~text
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
~~~~

Nouveau :

~~~~text
elif [ ! -s "$G1.sha256" ]; then
  dire "ETAT : sortie non gardée (complément au quatrième addendum, « La suite », point 3 : lecture consommée, aucune relance ; nœud)"
elif [ "$S_N" = 0 ]; then
  dire "ETAT : arrêt avant le seuil"
~~~~

### 6. § 5.3, table

**Fondement** : constat m2 : compte du seuil non ancré ; état « sortie non gardée ».

Ancien :

~~~~text
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
~~~~

Nouveau :

~~~~text
| **non prévu** | code 0 ou 3 sans les fichiers ou les lignes attendus | arrêt ; nœud | le relevé seul |
| **sortie non gardée** (ni code 0 ni code 3 ; sortie du lancement absente ou non scellée) | rien ne prouve que le seuil n'a pas été franchi | **lecture consommée ; arrêt ; nœud** (complément au quatrième addendum, « La suite », point 3) | le relevé seul ; aucune ligne de la sortie |
~~~~

### 7. § 5.2, bloc, relevé

**Fondement** : constat m3 : les heures de début et de fin vont au juge seul dans l'état « écrit ».

Ancien :

~~~~text
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null) ; identifiant du processus $(cat "$T/lancement-$N.pid")"
~~~~

Nouveau :

~~~~text
dire "identifiant du processus $(cat "$T/lancement-$N.pid" 2>/dev/null)"
[ "$CODE" = 0 ] || dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
~~~~

### 8. § 5.2, constat de forme pour le juge

**Fondement** : constat m3 : les heures de début et de fin vont au juge seul dans l'état « écrit ».

Ancien :

~~~~text
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
~~~~

Nouveau :

~~~~text
dire "lignes de la sortie gardée : $(wc -l < "$G1" | tr -d ' ')"
dire "début $(cat "$T/lancement-$N.debut") ; fin $(cat "$T/lancement-$N.fin" 2>/dev/null)"
~~~~

### 9. § 5.4, rendu

**Fondement** : constat m3 : les heures de début et de fin vont au juge seul dans l'état « écrit ».

Ancien :

~~~~text
l'identifiant du processus, les heures de début et de fin, le code de sortie.
~~~~

Nouveau :

~~~~text
l'identifiant du processus, le code de sortie (les heures de début et de fin sont dans le constat de forme, pour le juge seul).
~~~~

### 10. § 1.4, liste des empreintes entières

**Fondement** : constat m4 : table des modules gelés de la pièce « mots et coût » comparée avant le lancement.

Ancien :

~~~~text
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
EOF
~~~~

Nouveau :

~~~~text
9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674 scripts/mots_et_cout_t06_v3.py
bcfe56832a1bf0c9af78b94232aedb44f179446a3871f45c27f1e3348efa7173 src/controle_ia/t06/cout.py
a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3 src/controle_ia/t06/lanceur.py
43a244315573eac5cc07cf90089f057ce94878851c01085e0ad64b7ef782849c src/controle_ia/harnais/run_harnais_factice.py
5d97b223206c6378295946a769c378ccfe0bd6a12372d3b25bcecb5240ab31ae src/controle_ia/environnements/propositions.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d src/controle_ia/manifeste.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2 src/controle_ia/scellement.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439 src/controle_ia/gardes.py
EOF
~~~~

### 11. § 1.1, bloc

**Fondement** : constat m5 : branches du distant comparées par leurs noms et leurs têtes.

Ancien :

~~~~text
  awk '{print $2}' "$T/tetes-du-distant.txt" | sed 's#^refs/heads/#refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
  git for-each-ref --format='%(refname)' refs/remotes/origin | grep -v '/HEAD$' | sort > "$T/noms-locaux.txt"
  egal "branches du distant absentes localement" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
~~~~

Nouveau :

~~~~text
  awk '{print $1" "$2}' "$T/tetes-du-distant.txt" | sed 's# refs/heads/# refs/remotes/origin/#' | sort > "$T/noms-distants.txt"
  git for-each-ref --format='%(objectname) %(refname)' refs/remotes/origin | grep -v ' refs/remotes/origin/HEAD$' | sort > "$T/noms-locaux.txt"
  egal "branches du distant absentes localement ou à une autre tête" 0 "$(comm -23 "$T/noms-distants.txt" "$T/noms-locaux.txt" | wc -l | tr -d ' ')"
~~~~

### 12. § 6, entre les deux temps

**Fondement** : constat m6 : preuve d'antériorité versée au dépôt avant la lecture.

Ancien :

~~~~text
Entre les deux temps de l'opérateur (§ 4.1) : la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`. Ce n'est pas un commit de la branche de travail.
~~~~

Nouveau :

~~~~text
Entre les deux temps de l'opérateur (§ 4.1) : `registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` et son compagnon, commités et poussés sur la branche de travail (preuve « inscrite à part », avant la lecture : feu, § 12) ; puis la poussée de la branche de l'arbre de lecture sous le nom `claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture`, qui n'est pas un commit de la branche de travail.
~~~~

### 13. § 6, première puce de la liste « Après, selon l'état » (retirée, avec son retour de ligne)

**Fondement** : constat m6 : preuve d'antériorité versée au dépôt avant la lecture.

Ancien :

~~~~text
- `preuve-anteriorite-et-entree-conjointe-bbis-v1.txt` ;
~~~~

Nouveau :

~~~~text
(chaîne vide : passage retiré)
~~~~

### 14. § 6, pièces commitées à l'étape 0

**Fondement** : constat m7, et ce qui en découle strictement (la commande à commiter est la version 3).

Ancien :

~~~~text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md`, sa contre-lecture, leurs compagnons.
~~~~

Nouveau :

~~~~text
- `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v3.md`, ses différences avec la version 2, la contre-lecture de la version 2 dont elle porte les corrections, leurs compagnons (les versions 1 et 2 et leurs pièces restent, R12).
~~~~

### 15. étape 0, bloc

**Fondement** : décision d'organisation de la conductrice sur m5 : elle fait la récupération complète du distant, en lecture seule, à l'étape 0.

Ancien :

~~~~text
cd /home/user/controle-ia-travail
git status --porcelain --untracked-files=all | wc -l          # attendu : 0, sinon on ne fusionne pas
~~~~

Nouveau :

~~~~text
cd /home/user/controle-ia-travail
git fetch origin                                              # récupération complète du distant, en lecture seule (décision d'organisation, m5)
git status --porcelain --untracked-files=all | wc -l          # attendu : 0, sinon on ne fusionne pas
~~~~

### 16. étape 0, sous le bloc

**Fondement** : décision d'organisation de la conductrice sur m5 : elle fait la récupération complète du distant, en lecture seule, à l'étape 0.

Ancien :

~~~~text
- La ligne d'en-tête ne porte pas la chaîne que le module compte comme une ligne d'ouverture
~~~~

Nouveau :

~~~~text
- **Récupération complète du distant : décision d'organisation de la conductrice** (constat m5 de la contre-lecture de la version 2). La conductrice la fait ici, en lecture seule (`git fetch origin`), avant la fusion et le montage, pour que chaque branche de suivi locale soit à la tête du distant. L'opérateur ne fait que la comparaison (§ 1.1) ; sa permission d'appel au distant reste celle des trois branches nommées et de la lecture des têtes. Si le § 1.1 relève une branche absente ou à une autre tête, parce que le distant a avancé depuis, on ne lance pas : la conductrice refait cette récupération, puis l'opérateur rejoue le § 1.1 sous un nom de relevé neuf.
- La ligne d'en-tête ne porte pas la chaîne que le module compte comme une ligne d'ouverture
~~~~

### 17. § 1.1, sous le bloc

**Fondement** : décision d'organisation de la conductrice sur m5 : elle fait la récupération complète du distant, en lecture seule, à l'étape 0.

Ancien :

~~~~text
- Une branche du distant absente localement : la garde chercherait
~~~~

Nouveau :

~~~~text
- Une branche du distant absente localement, ou dont la tête locale n'est pas celle du distant : la garde chercherait
~~~~

### 18. § 4.1, gestes de la conductrice

**Fondement** : décision d'organisation de la conductrice sur m6 : elle commite et pousse la pièce de la preuve entre les deux temps de l'opérateur.

Ancien :

~~~~text
**Geste de la conductrice, avant le lancement** (second complément, point 7) : elle pousse la branche locale
~~~~

Nouveau :

~~~~text
**Gestes de la conductrice entre les deux temps, avant tout lancement.** D'abord, **décision d'organisation de la conductrice** (constat m6 de la contre-lecture de la version 2) : elle commite et pousse sur la branche de travail la pièce de la preuve d'antériorité et de la preuve d'entrée conjointe, avec son compagnon, pour que la preuve soit inscrite à part avant la lecture (feu, § 12). Ce commit ne touche pas l'arbre de lecture, dont le parent reste `TETE_TRAVAIL`. Ensuite (second complément, point 7) : elle pousse la branche locale
~~~~

### 19. § 4.1, bloc de la conductrice

**Fondement** : décision d'organisation de la conductrice sur m6 : elle commite et pousse la pièce de la preuve entre les deux temps de l'opérateur.

Ancien :

~~~~text
cd /home/user/controle-ia-travail
git push origin lecture/bbis-arbre-de-lecture-v1:refs/heads/claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
~~~~

Nouveau :

~~~~text
cd /home/user/controle-ia-travail
P=registres/t07-etape-b-bis/lecture-v1/preuve-anteriorite-et-entree-conjointe-bbis-v1.txt
git add -- "$P" "$P.sha256" && git commit -q -m "Étape B bis, lecture : preuve d'antériorité et preuve d'entrée conjointe, inscrites à part avant la lecture" && git push origin claude/lecture-verdict-etape-b-bis-v1
git push origin lecture/bbis-arbre-de-lecture-v1:refs/heads/claude/lecture-verdict-etape-b-bis-v1-arbre-de-lecture
~~~~

### 20. § 0, « Deux temps »

**Fondement** : décision d'organisation de la conductrice sur m6 : elle commite et pousse la pièce de la preuve entre les deux temps de l'opérateur.

Ancien :

~~~~text
La conductrice pousse alors la branche de l'arbre de lecture sous le nom ci-dessus (§ 4.1).
~~~~

Nouveau :

~~~~text
La conductrice commite et pousse alors la pièce de la preuve sur la branche de travail, puis pousse la branche de l'arbre de lecture sous le nom ci-dessus (§ 4.1).
~~~~

### 21. § 5.3, état « non consommée »

**Fondement** : décision d'organisation de la conductrice sur la note n3 : aucune relance n'est jouée sur cette version.

Ancien :

~~~~text
relance par cette même commande, à partir du § 4.2, avec `N` augmenté de un et, à la place de la ligne qui fixe `RUNL`, le nom du run refusé suivi de `-relance<n>`.
~~~~

Nouveau :

~~~~text
relance sous le nom du run refusé suivi de `-relance<n>`. **Aucune relance n'est jouée sur cette version de la commande : une relance demande une version de la commande écrite et contre-lue pour elle** (décision d'organisation de la conductrice ; note n3 de la contre-lecture de la version 2 : après les commits de la correction et de la déclaration, les contrôles du § 4.2 sur le parent de la tête et sur les 32 entrées rendraient « on ne lance pas »).
~~~~

### 22. § 0, paramètres

**Fondement** : décision d'organisation de la conductrice sur la note n3 : aucune relance n'est jouée sur cette version.

Ancien :

~~~~text
| numéro du lancement (`N`) | `1` ; tout autre numéro seulement sur le mot de la conductrice (§ 5.3) |
~~~~

Nouveau :

~~~~text
| numéro du lancement (`N`) | `1` ; cette version ne joue que le premier lancement (§ 5.3) |
~~~~

### 23. § 4.1, sous le bloc de la conductrice

**Fondement** : décision d'organisation de la conductrice sur la note n3 : aucune relance n'est jouée sur cette version.

Ancien :

~~~~text
- Après une relance accordée (§ 5.3, état « non consommée »), les commits locaux de plus sont poussés de même, avant la relance.
~~~~

Nouveau :

~~~~text
- Une relance n'est pas jouée sur cette version (§ 5.3) ; la version écrite pour elle dira comment les commits locaux de plus sont poussés.
~~~~

### 24. titre

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v2
~~~~

Nouveau :

~~~~text
# Commande de lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v3
~~~~

### 25. en-tête

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
Tout le reste est le texte de la version 1, à l'octet.
~~~~

Nouveau :

~~~~text
Tout le reste est le texte de la version 1, à l'octet.

**Version 3.** La version 2 (`commande-lecture-bbis-v2.md`, `4eea2d8a39c46ad2da27b7bd72852897a90eb122350ed55e5498eaaafc32b33d`) reste, non jouée (R12). Sa contre-lecture par un lecteur neuf d'un autre modèle (`contre-lecture-commande-lecture-bbis-v2.md`, `146b4d0483668df9fc6fb2661c4e4fad1425221a5061049e9731fb7128390925`) conclut « jouable après corrections mineures » : aucun constat majeur, sept mineurs. Cette version porte les remplacements m1 à m7 tels que le rapport les écrit, trois décisions d'organisation de la conductrice (sur m5, sur m6 et sur la note n3), et ce qui en découle strictement ; chaque passage changé est dans `differences-commande-lecture-bbis-v2-v3.md`, avec son fondement. Tout le reste est le texte de la version 2, à l'octet. **Cette version ne joue que le premier lancement.**
~~~~

### 26. § 7, N1

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4.** Le module charge le code de la pièce « mots et coût » avant sa garde (`main`, l. 1691) ; ce code vérifie sa propre table de modules gelés, que la commande ne peut pas contrôler sans le jouer. Un arrêt là mène au § 5.5 : aucune relance sans la preuve après coup, jouée sur ordre écrit, et la confirmation de la mère.
~~~~

Nouveau :

~~~~text
- **N1 — Des arrêts avant le seuil restent possibles malgré le § 4 ; réduit.** La table des modules gelés du code de la pièce « mots et coût » est désormais comparée avant le lancement, par empreinte (§ 1.4 ; constat m4 de la contre-lecture de la version 2). Restent, selon l'inventaire de ce rapport (note n8) : une erreur d'importation ou d'exécution du code de la pièce, le disque plein, un processus disparu ; aucun ne peut être exclu sans jouer le code. Un tel arrêt mène au § 5.5 : l'opérateur ne relance pas ; toute relance par cette voie attend le mot de Lazar. Classé par le rapport : question d'organisation.
~~~~

### 27. § 5.5, statut de la voie et conduite

**Fondement** : correction de la session mère (message du 2026-11-18 à 23:36:15Z ; R-3530) et classement du point N1 bis par la contre-lecture de la version 2 (point (g) ; note n12) : toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar.

Ancien :

~~~~text
- **Statut de cette voie** (second complément, point 6). Le complément scellé au quatrième addendum la dit « fermée tant que Lazar n'a pas dit son mot sur le point ouvert 7 ». La session mère l'a ouverte **par anticipation, sous son autonomie** (messages du 2026-11-18 à 23:08:42Z et 23:09:34Z ; R-3514, R-3516 ; autonomie GO-2026-11-18-61), dans cette forme : la preuve après coup compare les fichiers au commit épinglé des sorties `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`, après vérification de `sondes-bbis.json` contre la ligne `SCORES-BBIS`, sans décoder ce fichier. **Réserve, à porter si la voie sert** : ce qui l'ouvre est l'autonomie de la mère, non un mot de Lazar sur ce point.
- **Conduite.** Sur un arrêt avant le seuil, l'opérateur **ne relance pas** et ne corrige rien. Il rend le relevé du § 5.2 et s'arrête. Il joue le programme de la preuve après coup **seulement sur ordre écrit de la conductrice**, rend la pièce (chemin, empreinte, la ligne imprimée par le programme, son code de sortie) et s'arrête de nouveau. **La mère confirme avant toute relance** ; la suite est alors celle de l'état « non consommée » (§ 5.3), la pièce de preuve après coup tenant lieu du fichier de lecture gardé et de la pièce écrite par la garde.
~~~~

Nouveau :

~~~~text
- **Statut de cette voie.** Le complément scellé au quatrième addendum (§ 7, point 7) la dit : « La voie de l'arrêt avant le seuil n'est pas employée avant son mot » — le mot de Lazar. **Toute relance par cette voie attend donc le mot de Lazar**, et non la seule confirmation de la session mère : l'application par anticipation que la mère avait annoncée ne remplace pas un texte scellé (message de la mère du 2026-11-18 à 23:36:15Z ; R-3530). La forme de la preuve après coup — comparaison des fichiers au commit épinglé des sorties `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9`, après vérification de `sondes-bbis.json` contre la ligne `SCORES-BBIS`, sans décoder ce fichier — reste la forme recommandée et portée à Lazar ; **il ne l'a pas encore accordée**.
- **Conduite.** Sur un arrêt avant le seuil, l'opérateur **ne relance pas** et ne corrige rien. Il rend le relevé du § 5.2 et s'arrête. Il joue le programme de la preuve après coup **seulement sur ordre écrit de la conductrice** : le jouer n'emploie pas la voie, il relève un état ; relancer l'emploierait (classement de la contre-lecture de la version 2, point (g), N1 bis). Il rend la pièce (chemin, empreinte, la ligne imprimée par le programme, son code de sortie) et s'arrête de nouveau. La conductrice rend la pièce à la mère, qui la porte à Lazar. Aucune relance n'est jouée sur cette version de la commande (§ 5.3).
~~~~

### 28. § 7, N1 bis

**Fondement** : correction de la session mère (message du 2026-11-18 à 23:36:15Z ; R-3530) et classement du point N1 bis par la contre-lecture de la version 2 (point (g) ; note n12) : toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar.

Ancien :

~~~~text
- **N1 bis — La voie de l'arrêt avant le seuil est ouverte par l'autonomie de la session mère, non par un mot de Lazar** sur le point ouvert 7 du complément au quatrième addendum, qui la dit fermée jusqu'à ce mot (§ 5.5). Réserve à porter au verdict si cette voie sert. Non tranché par un texte scellé.
~~~~

Nouveau :

~~~~text
- **N1 bis — Toute relance par la voie de l'arrêt avant le seuil attend le mot de Lazar** (complément au quatrième addendum, § 7, point 7 ; message de la mère du 2026-11-18 à 23:36:15Z, R-3530 ; contre-lecture de la version 2, point (g) : « nœud de Lazar si la voie doit servir à une relance »). La forme de la preuve après coup est recommandée et portée à Lazar, non encore accordée. Non bloquant pour le premier lancement.
~~~~

### 29. § 7, N2

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
- **N2 — Ligne `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise** (§ 5.4). C'est la seule conduite qui ne laisse rien voir à la conductrice (second complément, point 5), et elle suit le plan, point 10 (f), et le complément au quatrième addendum, § 3. Le premier complément du mandat disait, pour l'issue « non lue » de fond, « lecture consommée ; arrêt » sans parler de la ligne : je lis que l'arrêt vient après l'inscription. Au contre-lecteur de dire si le texte le tranche ainsi, ou « nœud ».
~~~~

Nouveau :

~~~~text
- **N2 — Ligne `LECTURE-BBIS` inscrite dans tout état « écrit », issue « non lue » de fond comprise** (§ 5.4) : **tranché par le texte, dans le sens de la commande** (contre-lecture de la version 2, point (g) et note n1 : plan, point 10 (f), et point 2 ; quatrième addendum, § 7, point 4 ; complément au quatrième addendum, « La suite », point 1, et § 3). Ni question d'organisation, ni nœud.
~~~~

### 30. § 7, N6

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
- **N6 — Le verdict de l'épreuve du signal planté que cite son fichier d'issue n'est pas contrôlé avant le lancement** : son nom n'est connu qu'en ouvrant ce fichier, que la chaîne n'ouvre qu'après le seuil. Il est suivi par git sur `main` ; un arbre propre le tient présent. S'il manquait, l'issue serait « non lue », de fond.
~~~~

Nouveau :

~~~~text
- **N6 — Verdict de l'épreuve du signal planté que cite son fichier d'issue, non contrôlé avant le lancement** : **tranché par le texte** (contre-lecture de la version 2, point (g)) : son nom ne se connaît qu'en ouvrant le fichier d'issue, que la chaîne seule ouvre ; un fichier absent ou illisible donne une issue « non lue » de fond (complément au quatrième addendum, « La règle ») ; l'arbre de lecture, propre, porte les fichiers suivis. Risque accepté par le texte ; aucune action.
~~~~

### 31. § 7, N4

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
- **N4 — Le mandat du lecteur-opérateur et cette commande ne s'accordent pas en trois endroits**
~~~~

Nouveau :

~~~~text
- **N4 — Le mandat du lecteur-opérateur et cette commande ne s'accordent pas en plusieurs endroits** (à dire aussi dans son message de lancement : il ne fait pas la récupération complète du distant, que la conductrice fait à l'étape 0 ; il attend la fin du lancement sans attente fixe dans un appel de terminal, que son outil refuse — note n6 de la contre-lecture de la version 2)
~~~~

### 32. § 7, N8 (suite de m1 : la boucle de dix secondes n'existe plus)

**Fondement** : ce qui découle strictement des corrections : titre, nom de la version, statut des points ouverts selon le rapport (point (g)).

Ancien :

~~~~text
si l'identifiant du processus n'est pas écrit dans les dix secondes, l'opérateur ne relance pas, relève l'état (§ 5.1 bis) et rend.
~~~~

Nouveau :

~~~~text
si l'identifiant du processus n'est pas écrit à deux relevés de suite (§ 5.1 bis), l'opérateur ne relance pas et rend.
~~~~


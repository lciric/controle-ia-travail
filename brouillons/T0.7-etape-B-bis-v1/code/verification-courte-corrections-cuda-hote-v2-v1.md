# Vérification courte des corrections v2 du correctif « version CUDA de l'hôte » de l'étape B bis de T0.7, v1

**Verdict : feu possible.** Chaque point de la contre-lecture est traité comme le rapport le dit ; le différentiel ne porte aucun
changement de comportement hors de ce qui est déclaré, à une tolérance mineure près (point 2.1) ; le contrôle de branche distante
ne fait qu'une lecture, refuse dans les quatre cas demandés et **accepte** le dépôt de la mère tel qu'il est aujourd'hui (joué
pour de vrai, lecture seule) ; 138 essais passent. Aucun point bloquant. Trois conditions d'usage pour la mère (§ 7).

**Déclaration** : lecteur neuf, aucun fichier de l'étape B bis ni sa contre-lecture précédente écrits par moi ; rien lu ni écrit
sous `diag/`, `donnees/`, `docs/verdicts/` ; aucune valeur de clé lue, ni `env` ni `printenv` ; aucun appel au service de
location, aucune machine, aucune dépense ; aucun commit, aucune poussée. Appels réseau : des `git ls-remote` en lecture seule sur
le dépôt de travail (le contrôle lui-même, joué trois fois, et une liste de trois motifs de branches). Seuls fichiers écrits dans
la copie : ce rapport et son compagnon ; fichiers jetables dans le dossier temporaire de la session, hors de la copie.

- **Date (UTC)** : 2026-11-15.
- **Objet** : copie détachée `/home/user/verif-bbis-cuda-v2`, commit `eb772bd0f3aaadf23f551b64ed014b571144b294`, arbre propre ;
  différentiel `git diff b2c98918 eb772bd0` (12 fichiers, 379 lignes ajoutées, 48 retirées), lu en entier.
- **Pièces, empreintes conformes à leurs compagnons** :
  `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-corrections-cuda-hote-v1.md` —
  `6c25cc2a174335730b5049fef3222bba7cc0cccf587d08adc8ddc2befa654cb5` ;
  `brouillons/T0.7-etape-B-bis-v1/code/corrections-cuda-hote-v2.md` —
  `62f7dd479b39d0f105ba56a3a52d1459ec87d061f15bbeca09e6357376630aff`.

## 1. Points de la contre-lecture — tous traités comme dit

1.1 **M1, nom de la branche** — `scripts/amorce_repetition_bbis_v1.sh` ligne 35 : `BR_SORTIE=calcul/t07bbis-repetition-v2`
(commentaire R12 ligne 34, en-tête ligne 17). Le contrôle de l'instance reste en place (ligne 174, `ls-remote --exit-code`).
Le dossier de travail et le chemin des traces gardent « repetition-v1 » (ligne 31) : sans collision, le commit des traces est
posé sur COMMIT, pas sur la branche du 15 novembre. Sur le dépôt distant à cette heure : `calcul/t07bbis-repetition-v1` présente
(`56f5b8b8…`), `calcul/t07bbis-repetition-v2` absente, `donnees/t07-etape-b-bis-v1` absente.

1.2 **M1, contrôle dans les deux lanceurs** — bloc `branche-de-sortie` identique octet pour octet dans
`scripts/lancer_bbis_v1.sh` (lignes 45 à 63) et `scripts/lancer_repetition_bbis_v1.sh` (lignes 43 à 61) : même empreinte du bloc
extrait (`59d3f5c9…`). Appelé par `commande` des deux : ligne 90 (course, après la garde d'ancêtre) et ligne 98 (répétition, après
la comparaison de l'amorce, avant l'essai local) ; dans les deux, avant l'impression de la commande de création.

1.3 **M2** — code inchangé ; commentaire d'usage ajouté (`scripts/lancer_repetition_bbis_v1.sh`, lignes 29 à 31) : cumul
strictement sous 3 USD toutes passes comprises, échéance choisie par la mère. Conforme à la consigne ; voir § 7.

1.4 **m1** — cas 13.10 et 100.0 acceptés, 9.2 refusé (« pilote trop ancien : CUDA 9.2 ») dans
`test_cuda_du_pilote_avant_l_installation_dans_les_deux_amorces`. **m2** — ligne lue écrite au journal avant l'arrêt
« illisible », même texte dans les deux amorces (bloc `cuda-du-pilote` de même empreinte, `4332cff0…` ; course ligne 85,
répétition ligne 141) ; l'arrêt et son code 2 sont gardés. **m4** — faux `nvidia-smi` avec `FAUX_ENTETE=echec`, cas ajouté
côté répétition, essai neuf côté course ; les marques `carte-et-cuda` de l'amorce de la course sont deux commentaires, aucune
ligne de commande changée. **m5** — `OverflowError` rattrapée, motif écrit (`registre_bbis_v1.py`, lignes 278 à 281). **m6** —
`{valeur!r}` (ligne 285).

1.5 **Choix 4** — `lire_offre_de_recherche`, `offre_construite`, `offre_depuis_recherche` dans le registre ; sous-commande
`offre-depuis-recherche` de la course (fichier ouvert en mode « x », jamais réécrit) ; la répétition appelle la fonction commune.

1.6 **m3, m7, m8, m9 non corrigés — raisons acceptables.** m3 : rien à coder, la répétition est faite pour éprouver la forme
réelle de l'en-tête, et la ligne lue part désormais au journal. m7 : aucune forme réelle connue. m8 : la garde ne s'applique
qu'aux offres ; un texte donnerait un refus gratuit avant location. m9 : fiche sur le commit final.

## 2. Changements non déclarés — un seul, mineur, sans risque d'argent

2.1 **Tolérance élargie dans la répétition : `num_gpus` en texte.** Ancien (`scripts/repetition_carte_bbis_v1.py`) :
`o["num_gpus"] != 1` ; nouveau (`registre_bbis_v1.py`, `lire_offre_de_recherche`) : `_nombre(o["num_gpus"]) != 1`. Joué sur
l'ancien et le nouveau script, même offre : `"num_gpus": "1"` (texte) était refusé, il est accepté. Le rapport dit « messages
gardés » sans le signaler. Sans conséquence pratique (l'outil rend un nombre ; une seule carte reste exigée ; prix et relecture
après création inchangés). Correction facultative, plus tard : ancien : `_nombre(o["num_gpus"]) != 1` ; nouveau :
`isinstance(o["num_gpus"], bool) or o["num_gpus"] != 1`.

2.2 Autres écarts du même remaniement, tous dans le sens du refus (joués) : nombre non fini (`cpu_ram` infini) accepté avant,
refusé maintenant ; texte illisible : trace d'erreur avant, refus écrit maintenant ; prix non fini : refus avant et après,
motif différent. Ordre des fautes dans le message : carte, CUDA, prix (avant : carte, prix, CUDA). Onze autres cas identiques
(sain, prix trop haut, nul, négatif, CUDA basse, absente, en texte, carte PCIE, deux cartes, booléen, nombres en texte).

2.3 Rien d'autre : les essais changés ne perdent aucune assertion (lignes retirées = nom de branche v1 → v2 et un retour de
fonction complété par la pose du distant jetable).

## 3. Contrôle de branche distante

3.1 **Lecture seule** — la fonction ne joue que `sed -n` sur l'amorce, `git remote get-url origin` et
`git ls-remote --exit-code origin refs/heads/<branche>` ; aucune écriture, aucun `fetch`, aucun `push`.

3.2 **Refus** (joués par l'essai `test_branche_de_sortie_neuve_exigee_avant_la_commande`, et pour partie par moi sur le dépôt
réel) : branche présente → code 2 (joué en vrai avec une amorce au nom v1 : « branche de sortie calcul/t07bbis-repetition-v1
présente sur le dépôt distant (R12) ») ; dépôt injoignable → code 2 (« git ls-remote, code 128 », joué) ; `origin` absent →
code 2 ; `origin` d'un autre dépôt → code 2 (joué avec `lciric/controle-ia`, le nom interdit : refusé avant tout appel réseau) ;
`BR_SORTIE` ou `DEPOT_URL_OFFICIEL` absent ou double → code 2. Seul le code 2 de `ls-remote` (absence prouvée) est accepté.

3.3 **Dépôt de la mère — reconnu, la passe réelle n'est pas bloquée à tort.**
`git -C /home/user/controle-ia-travail remote get-url origin` rend `https://github.com/lciric/controle-ia-travail` : forme
ordinaire, sans suffixe `.git`, sans adresse de relais visible (le relais agit au niveau du transport, pas dans l'adresse). Le
contrôle retire `/` et `.git` finals puis compare les deux derniers segments (`lciric` et `controle-ia-travail`) à ceux de
`DEPOT_URL_OFFICIEL` de l'amorce : égalité. **Joué pour de vrai** depuis ce dépôt : amorce de répétition → code 0 ; amorce de
la course → code 0. Formes essayées en plus : avec `.git/` final → reconnue ; forme `git@github.com:…` → reconnue ici (réécrite
en https par la configuration du dépôt) ; adresse de relais `http://…/git/lciric/controle-ia-travail` → reconnue par le nom,
puis refus « injoignable » seulement parce que l'adresse d'essai n'existe pas.

3.4 **Réserves mineures, non bloquantes.** (a) L'identité de `origin` se juge sur propriétaire et nom, pas sur l'hôte : un
`origin` d'un autre hôte au même chemin passerait la comparaison, et l'absence serait prouvée sur ce dépôt-là ; le contrôle de
l'instance (ligne 174 de l'amorce) reste le dernier rempart. (b) Entre `commande` et le démarrage de l'instance, une branche
créée par un tiers ne serait vue que par l'instance : fenêtre inévitable. (c) Le contrôle dépend du réseau et des droits de
lecture du shell de la mère au moment de `commande` ; en défaut : refus gratuit, jamais une location.

## 4. Amorce de répétition du dossier et du commit — identiques

`sha256sum scripts/amorce_repetition_bbis_v1.sh` et `git show eb772bd0:scripts/amorce_repetition_bbis_v1.sh | sha256sum` :
`ba4aa32db3866328a529d374a0a18ab79368144f9e148bf71eed35be851c478d` des deux côtés, celle du rapport. De même
`scripts/amorce_bbis_v1.sh` : `4e1d77474bbd39e1d34800879fc2abfea7eb722de2d81ab3caa04faf70da7961` ; script de la répétition :
`4bbea0fae56660c687ef43d189f3bf40151ebc682059a9749bb1329f7259d221`. La comparaison `cmp -s` du lanceur (ligne 94) passera avec
`eb772bd0` si le lanceur joué est celui de ce commit (§ 7.1).

## 5. Rien d'autre ne change — confirmé

`MIN_ESSAIS=87` (`scripts/amorce_bbis_v1.sh` ligne 41) ; `PLAFOND_USD = 3.0`, `QUART_D_HEURE = 0.25`, `MARGE_USD = 0.40`
(`scripts/repetition_carte_bbis_v1.py` lignes 50, 51, 276) ; coupure de la course 39,5 (`registre_bbis_v1.py` ligne 45) : aucune
de ces lignes n'est dans le différentiel. Code de mesure, seuils, `garde_commande`, garde de création, garde de dépense,
minuterie, `detruire`, `verifier-destruction`, `requirements-gpu.txt` : aucune ligne touchée. Sur l'instance, le script de la
répétition importe en plus `controle_ia.gardes`, module déjà importé par le registre qu'il chargeait : aucun risque neuf.

## 6. Essais

`PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -p no:cacheprovider tests/test_t07bbis_*.py
tests/test_repetition_bbis_v1.py`, dans la copie, commit `eb772bd0` : **138 passed, 4 warnings in 206.55s (0:03:26)**, code 0.
138 essais collectés : 27 dans `tests/test_repetition_bbis_v1.py`, 111 dans `tests/test_t07bbis_*.py`. Conforme au compte
attendu. Arbre propre après la passe. Les mutations du développeur n'ont pas été rejouées (vérification courte).

## 7. Conditions d'usage pour la mère (aucune n'exige un commit neuf)

7.1 Le dépôt de la mère est sur `main` : jouer le lanceur **du commit `eb772bd0`** (par exemple celui de cette copie détachée),
avec RACINE = `/home/user/controle-ia-travail` (le commit y est présent, `origin` y est reconnu). Un lanceur d'un autre commit
donnerait le refus « amorce de répétition du commit ≠ celle de ce dossier », gratuit.

7.2 Sur le dépôt distant, `prep/t07bbis-code-v1` pointe bien sur `eb772bd0` à cette heure : l'instance trouvera le commit.

7.3 Plafond (M2) : `commande` calcule une passe seule. Avec ≈ 0,134 USD déjà dépensés, choisir l'échéance pour que le coût
maximal imprimé reste strictement sous 3 − 0,134 = 2,866 USD, et l'écrire dans le feu.

## Ce qui reste non éprouvé

Inchangé depuis la contre-lecture : forme réelle de l'en-tête de `nvidia-smi` dans le conteneur loué, présence et type de
`cuda_max_good` dans une recherche du jour, version de l'outil de location de la mère. La répétition est faite pour cela.

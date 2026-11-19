# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 10 — v1

**Verdict : engageable après corrections.** Aucun défaut bloquant. Un défaut à corriger avant toute lecture réelle (C-1) : **une course peut lire deux livraisons de la discrétion sans ligne de GO**.
- J'ai confirmé le défaut que le rédacteur signale : une seconde « première livraison » sous une configuration de rang 2 est lue.
- J'en ai trouvé une forme plus large : **sous la même configuration de rang 1, une autre pièce est lue tant que le fichier de l'étape (m) n'est pas écrit**. On pourrait ainsi choisir, entre deux livraisons, celle qu'on scelle.

Le reste tient :
- les trois mineurs de la version 9 sont corrigés, dans leurs limites écrites ;
- le gabarit de configuration recopie le mot de Lazar ;
- les six rédactions retirées sont refusées à la lecture ;
- les points 19 et 20 restent ouverts ;
- la provenance tient, dans ses limites écrites ;
- la garde statique n'ouvre rien de cloisonné.

La phrase d'accord de l'écart à R9 est **trop large**, car une ligne qui la nie l'ouvre, et **trop étroite**, car elle exige les accents (M-1). Les six défauts de la partie A du relevé sont des précisions de texte. Les essais donnent **319 passés**.

## Pièces lues et conditions

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), même contre-lecteur que pour les versions 5 à 9.
- **Code** : commit `7c7249b1d`. Les neuf modules `*_bras_a_v10.py`, les sept fichiers d'essais et `scripts/constat_de_lancement_discretion_bras_a_v3.py` répondent tous à leurs compagnons. Leurs empreintes sont celles de la note, par exemple :
  - `analyse_bras_a_v10.py` : `b07d425d…` ;
  - `configuration_bras_a_v10.py` : `378b729c…` ;
  - programme du constat v3 : `6ee84152…`.
- **Textes** :
  - mot de Lazar « go recos » (`1fcfae81…`), en entier ;
  - note du code v10 (`7f4771c7…`) et relevé v10 (`a386c070…`), en entier ;
  - brouillon 33 (`dc3bc023…`), empreinte seulement.
  - Je n'ai pas lu les notes des brouillons 32 et 33 : le relevé et la note du code citent ce qu'elles fixent.
- **Essais** : la commande de la note donne **319 passés** (58 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v10.py tests/test_verdicts_bras_a_v10.py tests/test_graines_bras_a_v10.py tests/test_cloisonnement_bras_a_v10.py tests/test_permutation_etiquettes_bras_a_v10.py tests/test_mesures_bras_a_v10.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  L'essai du rédacteur qui passe la garde sur le vrai dépôt tourne sous un crochet qui refuse toute ouverture cloisonnée avant qu'elle ait lieu. Mes essais de la garde n'ont tourné que sur un faux dépôt.
- **Essais d'attaque** : données synthétiques et registres fabriqués, dans le bloc-notes sous `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v10/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_v10.py` : « en attente », deux livraisons, provenance, rangement, M-1 et M-2 de la v9, phrase de l'écart à R9 ;
  - `configuration_v10.py` : rédactions retirées et choix ouverts, **à la lecture** de la configuration scellée ;
  - `audit_cloisonnement_v10.py` ;
  - `attaques_cloisonnement_v10.py` ;
  - `fuzz_livraison_v10.py` ;
  - `essais.sortie.txt` : la commande de la note.
- **Heure** : 2026-11-19T23:19Z.

---

## 1. Défauts bloquants

Aucun.

## 2. Défaut à corriger

### C-1. Une course lit deux livraisons sans ligne de GO
- **Où** : `analyse_bras_a_v10.py`, `_exiger_lecture_permise`, la branche `acte is None and not arrets` (première livraison). Elle ne demande rien quand aucun arrêt ni aucun constat de pièce n'est consigné. `_livraisons_lues` n'y sert qu'à solder des constats.
- **Essais** (`attaques_v10.py`) :
  1. **Défaut signalé par le rédacteur, confirmé.** Le rang 1 est lu et son fichier (m) scellé. Une autre pièce, sous une configuration de rang 2 qui n'inscrit aucun registre, est lue sans ligne de GO, et donne « repère ».
  2. **Forme plus large, neuve.** Sous la configuration du rang 1, une pièce A est lue (« ne repère pas »). Avant l'écriture du fichier (m), une pièce B **d'une autre empreinte** est lue sous la même configuration, et donne « repère ». Rien ne les distingue : la lecture d'une première livraison ne laisse aucune trace scellée avant le fichier (m), et le constat de lancement ne porte pas l'empreinte de la pièce. La session peut ensuite sceller le fichier (m) de B. Mon essai s'arrête là sur une table C contraire à ses états, non sur une garde de provenance.
- **Pourquoi c'est à corriger** : c'est la garantie centrale de toute la mécanique de reprise. Une livraison se lit une fois, et toute autre passe par la règle d'octroi. Deux lectures permettent de choisir.
- **Ce qui le fermerait** :
  - (a) **une ouverture scellée pour la première livraison**, comme l'acte de reprise pour une livraison refaite. Avant toute lecture, le programme écrit sans reste, dans le dossier des arrêts, `ouverture-de-la-lecture-de-la-discretion-bras-a-<seize signes>.json`, avec l'empreinte de la pièce et celle de la configuration. Une ouverture pour une autre pièce, dans la course, exige ensuite une ligne de GO. Le rejeu de la même pièce, sous la même configuration, reste permis : il est déjà prévu pour une première livraison interrompue.
  - (b) **en plus** : une configuration de rang supérieur à 1 doit inscrire un registre figé. Les configurations voisines sont déjà lues.
  - (c) au texte, la règle (relevé A.2), étendue au cas de la même configuration.

## 3. Défauts mineurs

- **M-1. La phrase d'accord de l'écart à R9 est trop large et trop étroite.** Où : `graines_bras_a_v10.ligne_d_accord`, `phrase.casefold() in ligne`. Essais sur un état figé fabriqué :

  | ligne du registre | porte |
  |---|---|
  | « écart à R9 accordé pour la table des identifiants opaques » | ouvre (juste) |
  | « **aucun** écart à R9 accordé pour la table des identifiants opaques » | **ouvre** |
  | « **pas d'**écart à R9 accordé pour la table … **avant le devis** » | **ouvre** |
  | « écart à R9 accordé pour la table … **? à trancher** » | **ouvre** |
  | « … accordé …, refusé : pas de devis » | refusée (forme de refus) |
  | « ecart a R9 accorde … » (sans accents) | **refusée** |
  | les mots du mot de Lazar (« … entropie propre … — accepter ») | refusée, comme le rédacteur l'annonce |

  La phrase est cherchée comme sous-chaîne : une négation placée devant passe. Correction : exiger que la cellule d'objet de la ligne **soit** la phrase, comparée sans égard à la casse ni aux accents, ponctuation finale admise. La même règle vaut pour la phrase d'une livraison refaite, qui passe par la même fonction. Au texte (relevé B.1), écrire cette phrase en 13.2, et dire d'où viennent la pièce de l'état figé et son empreinte pour une première livraison (relevé B.2). Aujourd'hui, l'appelant les donne.
- **M-2. Un contrôle sain plus ancien qu'une révocation entrée suffit au rejeu.** Après une panne et un contrôle sain, une révocation entre au registre. Sans contrôle refait, le rejeu part sur l'ancien contrôle (essai). C'est la limite que le rédacteur écrit (point 9.5 de sa note). Le code ne peut pas savoir qu'il fallait refaire le contrôle, ni que le registre qu'on lui a donné était le dernier. M-1 de la version 9 est tenu pour le reste : sans contrôle, le rejeu est refusé ; après un contrôle malsain, il est refusé. Correction possible au texte : un contrôle n'est valable que pour le rejeu qui le suit, et le rejeu consigne l'empreinte du contrôle qu'il emploie, que la garde de sortie relit (c'est déjà fait) et qu'un rejeu suivant ne peut pas reprendre.
- **M-3. Abrégés de moins de seize signes.** Une ligne qui retire la configuration en la citant par douze signes n'est pas vue (essai). Seize signes sont vus. C'est la limite écrite. La consigne de tenue du registre (empreinte entière) la couvre.
- **M-4. Une autre course efface les traces.** La bonne pièce, donnée sous la configuration d'une course neuve, avec un dossier des arrêts neuf, se lit comme première livraison, malgré le constat de provenance de la première course (essai). C'est la limite de M-2 de la version 7. Ce qui tient : la configuration d'une seconde course doit être inscrite au registre, et le constat de lancement le vérifie. Une seconde inscription de configuration pour une première livraison se voit donc au registre.
- **M-5. La garde du choix « en attente » ne laisse aucune trace.** Une livraison qui porte le motif « moniteur appris non ajustable » sous « en attente » est arrêtée par une garde ordinaire, sans fichier, y compris quand le motif n'est qu'à la dose ¼ (essai). C'est conforme à la note. Mais rien ne fixe alors l'empreinte de la pièce, contrairement à la garde de provenance. Après la réponse du développeur habilité, une autre pièce pourrait être donnée sans ligne de GO. Correction : consigner l'empreinte de la pièce, comme pour la provenance (« pièce en attente d'un choix »).

## 4. Les trois mineurs de la version 9 (question 1)

| mineur v9 | jugement | preuve |
|---|---|---|
| M-1 contrôle avant un rejeu | **tenu** (limite M-2 ci-dessus) | rejeu sans contrôle : refusé ; contrôle malsain : rejeu refusé ; contrôle sain : rejeu ; contrôle scellé sain ou malsain, constat d'origine intact |
| M-2 préfixes et identifiants | **tenu** | retrait par seize signes : constat malsain ; « GO 2099-01-01-01 » et « go_2099_01_01_01 » : vus ; `GO-2099-01-01-011` : non pris (juste) ; douze signes : non vus (M-3) |
| M-3 constat écrit à la main | **limite inchangée**, acceptable (garde de procédure) | — |

## 5. Gabarit et choix (question 2)

- **Le gabarit recopie le mot de Lazar** : échange dans chaque paire ; seuil sur les tirages demandés ; intervalle impossible lu comme dégénéré ; non ajustable « en attente » ; discrétion non lue en distinguant les étapes. Aucune fonction de lecture ne le lit : il n'est nommé que dans sa définition et dans la documentation d'une fonction d'écriture.
- **Les six rédactions retirées sont refusées à la lecture de la configuration scellée** (`configuration_v10.py`), chacune avec son nom : permutation libre, seuil sur les calculés, « indécis d'office », non ajustable « anomalie », ligne d'arrêt de la course, « non lue » à toute étape. Une valeur approchante (espace final), une valeur nulle, ou un choix absent sont refusés.
- **Les choix ouverts le restent** :
  - point 19 : « comme dégénéré » et « anomalie » sont admis. Le mot accorde (a) et garde la clause qui mène à (c) ;
  - point 20 : « aire non calculable », « module corrigé » et « en attente » sont admis, ce qui correspond à la recommandation accordée : attendre la réponse, puis (c), ou la fiche tombe et la règle déjà écrite s'applique.
- **« En attente »** : une livraison sans le motif se lit. Avec le motif, à quelque dose que ce soit, garde ordinaire, sans fichier d'arrêt (M-5).

## 6. Provenance (question 3)

- **Clé obligatoire** : `null` refusé à la lecture de la configuration.
- **Constat de provenance** : une pièce d'un autre module est arrêtée et son constat est scellé. Ensuite, la bonne pièce est refusée sans ligne de GO, sous la même configuration comme sous une configuration neuve de la course. Le remplacement passe par la règle d'octroi.
- **Erreur de rangement** : une pièce sans compagnon laisse un constat. La même pièce, scellée ensuite, se lit sans ligne de GO.
- **Contournements cherchés** :
  - deux livraisons sans ligne de GO : C-1 ;
  - une autre course : M-4 ;
  - un chemin vers un dossier ne laisse rien, et une autre pièce se lit ensuite sans ligne de GO (essai). C'est la limite écrite (« un chemin sans fichier ne laisse rien »), sans portée tant que C-1 (a) n'existe pas : avec une ouverture scellée, la première pièce lue fixerait la course ;
  - la garde « en attente » : M-5.
- **La fouille de 400 livraisons altérées** donne 290 arrêts nommés et 16 gardes ordinaires, toutes de provenance (`piece_source` altéré), comme le texte le veut.

## 7. Les six défauts de la partie A du relevé (question 5)

| point | nature | avis |
|---|---|---|
| A.1 pièce arrêtée redonnée sous une configuration corrigée | **précision** | Le code la refuse même sous une ligne de GO : trop strict, car la discrétion peut se perdre sur une simple erreur de configuration. Je recommande d'écrire qu'elle se relit **sous une configuration neuve et une ligne de GO** (la règle d'octroi), comme toute reprise |
| A.2 seconde première livraison | **précision**, à coder (C-1) | le principe « une livraison est lue une fois, toute autre passe par la règle d'octroi » est déjà au texte |
| A.3 recomposer après un arrêt à l'étape (n) | **précision** | sous l'issue retenue (c), la table C est gardée : recomposer, sans lire le fichier des scores, devrait rester permis pour le rapport de la ligne C4 |
| A.4 constat cité sous une livraison refaite | **précision** | le programme peut exiger que la configuration du constat cité n'inscrive aucun registre figé (première livraison) ; à coder |
| A.5 empreinte d'une erreur de rangement | **précision** | quand le compagnon dément les octets, consigner les deux empreintes ; « la même pièce » est celle que scelle le compagnon |
| A.6 valeur « en attente » | **précision** | elle exécute le « attendre » du mot ; écrire qu'elle existe et qu'elle n'emporte aucune issue, et consigner la pièce (M-5) |

Aucun n'appelle le mot de Lazar.

## 8. La garde statique (question 6)

Faux dépôt, valeurs par défaut, crochet d'audit écrit à part (`audit_cloisonnement_v10.py`) :
- ni la garde ni `listages_a_relire` n'ouvre ni ne liste un chemin cloisonné ;
- les chemins cloisonnés sont élagués par leur nom, y compris sous une autre casse ;
- un départ cloisonné, ou par `..`, est refusé ;
- un lien symbolique n'est pas suivi ;
- un lien physique n'est pas ouvert ;
- des 24 modules plantés, 19 sont refusés, un est signalé, et les restes déclarés passent.

## 9. Ce que je n'ai pas regardé
- Les notes des brouillons 32 et 33 et le texte du brouillon 33.
- Le fichier des grandeurs de l'étape (n), les verdicts sous l'issue (c) et `resultat_recompose`, couverts par les essais du rédacteur et non rejoués par moi.

## 10. Fichiers ouverts
- `CLAUDE.md`.
- `docs/notes/relance-organismes-discrets-v1/mot-de-lazar-go-recos-bras-a-2026-11-19-v1.md`, `code-v10-bras-a-note-v1.md` et `defauts-du-texte-trouves-en-codant-v10.md`, en entier.
- Code :
  - `configuration_bras_a_v10.py` (choix, rédactions, gabarit) ;
  - `analyse_bras_a_v10.py` (lignes 1340 à 1545 et 1923 à 2070) ;
  - `graines_bras_a_v10.py` (porte de l'écart à R9, `ligne_d_accord`).
- `tests/aide_bras_a_v10.py` : différence avec la v9, et lignes 265 à 306.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - ni le vrai registre ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.

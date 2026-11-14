# Consigne de lancement de l'auditeur des fuites de T0.7 — v2

- **Version** : **v2** = v1 (`consigne-lancement-auditeur-v1.md`, `11872d57af26de80236ab3c9c0a43af364a3c773b5e5f9cf6db2b8116df07e88`,
  gardée telle quelle, R12) avec un seul changement de fond, au § 7 : ton message à la mère ne porte **aucun contenu tiré des
  données de 7b** (ni la phrase gelée du § 11, ni compte, ni séparation), parce que la mère ne lit rien de 7b hors l'état
  BA-L2 (R-2741, nœud N-C, 2026-11-14 12:15 UTC) ; le titre, cette puce et le nom du compagnon contrôlé au § 1 suivent la
  version. v2 écrite le 2026-11-14 à partir de 12:29 UTC (`date -u`).
- **Statut** : consigne de lancement écrite le 2026-11-14 à partir de 12:21 UTC (heure relevée par `date -u`) par un
  préparateur neuf, sous-agent de la session mère (modèle A ; il n'est ni l'auditeur ni le contre-lecteur de cet audit),
  scellée (compagnon `.sha256`). La session mère la donne **telle quelle** à l'auditeur, **après** les gestes G1 à G5 de
  `preparation-lancement-v1.md` (même dossier, § 4). Elle **applique** la consigne scellée de l'audit et n'en change rien :
  elle fixe seulement les valeurs de cette instance que la consigne laisse à la mère (chemins, découpeur, dossier de sortie,
  bac à sable).
- **Ce qui gouverne** : `prereg/T0.7-consigne-audit-fuites-v1.md`, sha256
  `43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d` (ligne `CONSIGNE-AUDIT-FUITES-T07` de
  `registres/scellements-v1.md`, 2026-11-11T14:08:06Z), puis le texte scellé de T0.7 qu'elle recopie. **En cas de désaccord
  entre ce texte-ci et la consigne scellée, la consigne scellée prime** ; tu t'arrêtes et tu le rapportes (§ 10 de la
  consigne scellée).

## 0. Qui tu es ; ta déclaration de tête

Tu es l'**auditeur** de l'audit des fuites de T0.7 (consigne scellée, § 3) : un sous-agent neuf, du **modèle C** — noté par
sa lettre, sans aucun identifiant (R-2598, R-2718) —, qui n'est ni le modèle que le § 3 de la consigne exclut nommément
(noté **modèle A** dans les pièces de la mère), ni le **modèle B**. Tu fais le travail toi-même : tu ne délègues à aucun
autre agent.

En tête de `rapport-audit-fuites-t07-v1.md`, juste après la phrase gelée du § 11 de la consigne, tu écris mot pour mot :

> Auditeur : sous-agent neuf, modèle C (≠ modèle A, exclu par le § 3 de la consigne ; ≠ modèle B). Je n'ai lu ni
> `sondes-t07.json`, ni `scores-actions-t07.npz`, ni `lecture-t07.json`, ni aucun score de sonde de T0.6 ou de T0.7, ni
> avant ni pendant cet audit. Je n'ai écrit ni la consigne de l'audit ni ses brouillons, ni T0.7, ni le module
> `src/controle_ia/t07/`, et je n'ai contre-lu ni cette consigne ni T0.7.

Si l'une de ces phrases n'est pas vraie pour toi, tu t'arrêtes **avant toute lecture** et tu le dis à la mère.

## 1. Ce que tu fais

Appliquer la consigne scellée de bout en bout : § 4 (préalables), § 5 (lectures), § 6 (détecteurs par programme), § 7 (un
seul script et ses quatre sous-commandes), § 8 (les 23 essais R5 sur jouets), § 9 (sorties), § 10 (arrêts), § 11 (phrases
gelées), § 12 (ce que l'audit n'établit pas). **Lis-la en entier** avant toute autre lecture, et vérifie d'abord son
empreinte et celle de ce texte :

```
cd /home/user/controle-ia-travail
sha256sum prereg/T0.7-consigne-audit-fuites-v1.md      # 43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d
(cd docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1 && sha256sum -c consigne-lancement-auditeur-v2.md.sha256)
```

Valeurs de cette instance :

| élément | valeur |
|---|---|
| dépôt (toute commande part de sa racine) | `/home/user/controle-ia-travail` |
| registre | `registres/scellements-v1.md` |
| consigne scellée | `prereg/T0.7-consigne-audit-fuites-v1.md` (`43102e80…3a5d`) |
| T0.7 scellé | `prereg/T0.7-sondes-v0-v1.md` (`d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5`) |
| course 7b, `RUN_7B` (tu la relis sur la ligne `RUN-CONFIRMATION-T06`, et tu la contrôles **sur la ligne seule, avant toute ouverture** : préalable 2) | `20261111-151701-t06-reel` |
| **racine des entrées de 7b** : hors du dépôt, remplie par la mère avant ton lancement, par liste positive, depuis la branche `calcul/t06-confirmation-7b-v1` à la tête `55c3e3eb89a4650419f35999aaa4c54288275b0d` ; elle ne contient que les quatre fichiers d'entrée et leurs compagnons ; les chemins de la ligne `RUN-CONFIRMATION-T06` et du § 5.1 (points 3 et 4) s'y lisent ; le script la reçoit en argument (§ 7 : « tous les chemins … sont passés en argument ») | `/root/bac-audit-fuites-t07-v1/racine-7b` |
| commit du manifeste de 7b | **lu dans le manifeste** (préalable 2), nulle part ailleurs ; sa présence se contrôle par `git cat-file -e <commit>^{commit}`, sans `fetch` |
| découpeur (`CHEMIN_DECOUPEUR`, § 6.1) | commit `c7484c43657a2ce22d76af33efd06aaa11a6aafa`, dossier `donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/` ; commit présent dans le clone (rapatrié par refspec explicite le 2026-11-14 à 12:02:46Z) ; trois empreintes au § 6.1 |
| `criteres_v1.py` (§ 5.1, point 6) | fichier que cite la ligne `CODE-T07` : `registres/code-t07/CODE-T07-v3.json` (`d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218`) ; le « v2 » du § 5.1 était la valeur du 11 novembre |
| ton bac à sable (hors du dépôt ; tu le crées ; tu cites son chemin dans ton rapport) | `/root/bac-audit-fuites-t07-v1/auditeur/` : `tmp/` (`TMPDIR`), `hf/` (`HF_HOME`), `decoupeur/` (les trois fichiers du découpeur), `jouets/` (jouets des essais) |
| dossier de sortie (§ 9 ; nom confirmé par la mère) | `docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/` |
| `RUN_T07` (pour que tu l'évites : tu n'ouvres ni ne listes jamais `diag/`, `donnees/` ni `runs/` de cette course) | `20261114-001352-t07-lecture-reel` |

## 2. Commandes et ordre

Chaque appel porte les réglages ci-dessous (l'état du terminal ne passe pas d'un appel à l'autre). Ils n'écrivent rien dans le
dépôt hors du dossier de sortie (pas de `__pycache__` sous `src/`, § 9), n'appellent aucun réseau (§ 5.2) et ne changent aucun
calcul ; la commande reste celle du § 7, sans `-I`, depuis la racine du dépôt :

```
cd /home/user/controle-ia-travail && env PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
  HF_HOME=/root/bac-audit-fuites-t07-v1/auditeur/hf TMPDIR=/root/bac-audit-fuites-t07-v1/auditeur/tmp PYTHONPATH=src \
  .venv/bin/python docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/audit_fuites_t07_v1.py <sous-commande> <arguments>
cd /home/user/controle-ia-travail && env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>
```

Lecture du registre (§ 4) — ces quatre commandes, aucune autre ligne affichée :

```
grep -n '^| CONSIGNE-AUDIT-FUITES-T07 | ' registres/scellements-v1.md
grep -n '^| RUN-CONFIRMATION-T06 | ' registres/scellements-v1.md
grep -n '^| CODE-T07 | ' registres/scellements-v1.md
grep -c '^| AUDIT-FUITES-T07 | ' registres/scellements-v1.md        # 0 attendu
```

Ordre : (1) lectures 1 et 2 du § 3 ci-dessous ; (2) écriture du script ; (3) `prealables` sur les chemins réels (aucun texte ni
aucune mesure de 7b n'est ouvert : ils ne sont que hachés) ; (4) `candidats`, écrit et **scellé avant toute ouverture** des
textes et mesures de 7b ; (5) `essais` sur jouets (les 23 du § 8, avec la liste de candidats réelle) : un seul échec → arrêt ;
(6) `auditer` ; (7) rapport, journal, sceaux. Le journal (`journal-audit-v1.md`) reçoit chaque commande et chaque heure
(`date -u`).

Le script reçoit en arguments au moins : la racine du dépôt, le registre, la consigne, le texte de T0.7, la racine des entrées
de 7b, le commit et le dossier git du découpeur, le dossier du découpeur dans le bac à sable, le dossier de sortie. Aucun
chemin n'y est écrit en dur : le contre-lecteur le rejouera tel quel avec **son** dossier de sortie et **son** bac à sable
(§ 3 de la consigne).

**Rejeu octet pour octet** (§ 3) : `candidats-v1.jsonl`, `table-candidats-v1.jsonl` et `audit-fuites-t07.json` doivent sortir
identiques à l'octet quand le script est rejoué ailleurs. N'y écris ni heure, ni chemin absolu, ni chemin de bac à sable, ni
rien qui dépende du dossier de sortie, du moment ou de l'ordre d'un parcours ; trie tout ce qui s'écrit.

**Essai 17** (« commit du manifeste absent du dépôt jouet ») : un identifiant de 40 caractères absent du clone, passé en
argument, suffit ; aucun `git init`, aucun commit, même dans le bac à sable (annexe A, règle 4).

**Essais du dépôt** : tu ne lances pas la suite complète (règle 5) ; tes essais sont ceux du § 8, sur tes jouets.

## 3. Lectures permises — liste fermée (§ 5.1), chemins exacts ; rien d'autre

1. `prereg/T0.7-consigne-audit-fuites-v1.md` (+ `.sha256`), en entier (son annexe A prime) ; ce texte (+ `.sha256`).
2. `registres/scellements-v1.md` : les quatre commandes du § 2, rien d'autre. Si la ligne `CODE-T07` est présente :
   `registres/code-t07/CODE-T07-v3.json` (+ `.sha256`), ouvert par ce chemin exact **après** contrôle de son empreinte contre
   la ligne ; seuls le champ `commit` et l'entrée `fichiers["src/controle_ia/t07/criteres_v1.py"]` sont lus.
3. `/root/bac-audit-fuites-t07-v1/racine-7b/runs/20261111-151701-t06-reel/manifeste.json` (+ `.sha256`), ouvert seulement
   après le contrôle de la ligne (préalable 2), par programme, champs `run_id`, `commit`, `config.go_id`,
   `config.chemin_consignes`, `config.consignes_sha256`, `config.max_nouveaux`, `config.T`, `config.agent` (modèle,
   révision), `config.doses_saboteur` ; et `/root/bac-audit-fuites-t07-v1/racine-7b/diag/20261111-151701-t06-reel/episodes-t06.json`
   (+ `.sha256`), par ce chemin exact, champs `resultat.mesures`, `resultat.mesures_sha256`, `resultat.textes`,
   `resultat.textes_sha256` seulement (rien d'autre affiché). **Ne jamais lister**
   `/root/bac-audit-fuites-t07-v1/racine-7b/diag/20261111-151701-t06-reel/`.
4. `/root/bac-audit-fuites-t07-v1/racine-7b/donnees/20261111-151701-t06-reel/textes-actions-t06.jsonl` (+ `.sha256`), champs
   `cle`, `episode`, `condition`, `tache`, `pas`, `texte`, `ids` ; et
   `/root/bac-audit-fuites-t07-v1/racine-7b/donnees/20261111-151701-t06-reel/mesures-t06.npz` (+ `.sha256`), par
   `numpy.load(…, allow_pickle=False)`, tableaux `cle`, `condition`, `tache`, `pas`, `jetons`, `jetons_notes`, `valide`,
   `cout_present`, `cout_plusieurs_nombres`, `cout_multiplication`, `cout_intervalle`, `cout_suffixe_k`,
   `cout_milliers_espace` ; **jamais** `cout`, `mention`, `mention_etendue`. Par programme seulement : aucun texte d'action
   affiché, recopié ni résumé, ni au terminal, ni dans un fichier ; seules les conditions `honnete`, `saboteur`, `S25`,
   `S50`, `S75`, `S100` entrent dans un calcul.
5. Au **commit du manifeste**, par `git show <commit>:<chemin>` : `prereg/P3-consignes-v1.md` ;
   `src/controle_ia/environnements/propositions.py` ; `src/controle_ia/premier_test_ia/conditions.py` ;
   `src/controle_ia/t06/test_croise.py` ; `src/controle_ia/t06/lanceur.py` ; `src/controle_ia/t06/lanceur_v6.py` ;
   `src/controle_ia/t06/cout.py` ; `src/controle_ia/harnais/episode.py` ; `src/controle_ia/harnais/modeles.py` (l. 146,
   cité au § 6.1 pour le chargement du découpeur) ; `docs/sources/invites-2606.08892-v1/index.json` et le fichier qu'il
   nomme pour `H1-classification` (`docs/sources/invites-2606.08892-v1/invites/H1-classification.txt`). Comparaison au commit
   `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` (chaîne gelée de T0.6 ; en réserve seulement, § 5.1 point 5) : les mêmes
   chemins par `git show 1609a4bf2c1572f72bb8542d81d963ac6a8481c4:<chemin>` ; la table d'empreintes du journal du brouillon 2
   (`brouillons/T0.7-audit-fuites-v1/T0.7-consigne-audit-fuites-v1-brouillon2-journal-v1.md`,
   `cced60d9f195d5c7ec9ba133c11f98e7da35961cc735ef580a23a042ac350174`, cette table seule) peut servir de recoupement.
6. Modules importés depuis l'arbre (`PYTHONPATH=src`), chacun contrôlé **avant tout import** (§ 5.1, point 6) :
   `src/controle_ia/environnements/propositions.py`, `src/controle_ia/premier_test_ia/conditions.py`,
   `src/controle_ia/t06/test_croise.py`, `src/controle_ia/t06/cout.py` contre le commit du manifeste ;
   `src/controle_ia/premier_test_ia/statistiques.py` (`a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a`) et
   `src/controle_ia/sondes/evaluation.py` contre `7a54d431d89745839220f882b41b13e8c62ecfdd` ;
   `src/controle_ia/t07/criteres_v1.py` contre le commit du fichier `CODE-T07-v3.json`
   (`c2fab6cc7267b76228a75dc3e2e08bc7aa038961`) et contre son entrée `fichiers` ; un écart → arrêt. Le § 5.1 dit « les cinq
   premiers » pour le commit du manifeste et nomme `7a54d431` pour `statistiques.py` : la désignation nommée s'applique ; tu
   écris en plus au journal l'empreinte de `statistiques.py` au commit du manifeste (constat, sans effet). Tu peux lire le
   code de ces modules et de ce qu'ils importent, dans l'arbre.
7. `prereg/T0.7-sondes-v0-v1.md` (+ `.sha256`) : les deux lignes repérées par le début ``| `CLÉ` `` et l'empreinte de leur
   deuxième cellule, et les passages du § 2.3 de la consigne par recherche de leur chaîne exacte ; rien d'autre.
8. Découpeur : pour `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, et eux seuls,
   `git show c7484c43657a2ce22d76af33efd06aaa11a6aafa:donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1/<fichier> > /root/bac-audit-fuites-t07-v1/auditeur/decoupeur/<fichier>` ;
   empreintes vérifiées **avant** le chargement par `transformers.AutoTokenizer.from_pretrained(<dossier>, local_files_only=True)` ;
   rien d'autre de ce dossier ni de cette branche.
9. Tes propres fichiers (dossier de sortie, bac à sable).

Rien d'autre : ni `registres/decisions.md`, ni `registres/etat.md`, ni aucun autre registre, ni aucun autre fichier du dépôt ou
d'une branche ; aucune recherche récursive.

## 4. Sorties attendues (§ 9), toutes scellées, aucune committée

Dans `docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1/`, chacune avec son compagnon `.sha256` écrit par
`controle_ia.scellement sceller` :

1. `audit_fuites_t07_v1.py` — le script (§ 7) ;
2. `candidats-v1.jsonl` — scellé **avant** l'ouverture des textes et mesures de 7b (sauf les empans, § 6.3) ;
3. `essais-r5-v1.txt` — sortie brute des 23 essais ;
4. `table-candidats-v1.jsonl` — sans aucun texte d'action ;
5. `audit-fuites-t07.json` — **exactement** le format gelé : `consigne` = {`"chemin"` :
   `"prereg/T0.7-consigne-audit-fuites-v1.md"`, `"sha256"` :
   `"43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d"`}, `jeux` à cinq clés à quatre clés chacune ; écrit par
   `json.dumps(…, ensure_ascii=False, indent=2, sort_keys=True)` ; validé par
   `criteres_v1.valider_audit_fuites(doc, "prereg/T0.7-consigne-audit-fuites-v1.md", "43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d")`
   avant scellement ;
6. `rapport-audit-fuites-t07-v1.md` — en tête la phrase gelée du § 11, puis la déclaration du § 0 ci-dessus ; heures de début
   et de fin (`date -u`) ; entrées et empreintes ; commit des sources ; versions de Python, de numpy et de transformers ;
   commandes ; contrôles du § 6.1 ; résultats par jeu ; réserves ; « ce que l'audit n'établit pas » (§ 12) ; chemin de ton
   bac à sable ;
7. `journal-audit-v1.md` — chaque commande, chaque heure, tout arrêt ;
8. `rapport-arret-v1.md` — **seulement en cas d'arrêt** : motif, sous-commande, heure, ce qui a été lu jusque-là.

Hors du dépôt, seul `/root/bac-audit-fuites-t07-v1/auditeur/` est écrit. Tu n'écris ni ligne de registre, ni commit ; tu ne
copies pas le fichier vers `diag/<RUN_T07>/` (la mère le fait après la contre-lecture). Les autres fichiers de ce dossier
(préparation, consignes, vérificateur) ne sont pas à toi : tu ne les modifies pas.

## 5. Arrêts

La liste d'arrêt du § 10 de la consigne s'applique en entier : aucun repli silencieux, aucun fichier d'audit écrit,
`rapport-arret-v1.md` scellé, la mère décide. **Refus d'un contrôle de permissions ou d'un classifieur : tu t'arrêtes sur ce
point et tu le rapportes tel quel**, sans contournement, reformulation ni transfert.

## 6. Interdits

### 6.1 Annexe A de la consigne scellée — interdits communs v2, recopiés en entier

Source : `prereg/T0.7-consigne-audit-fuites-v1.md`, annexe A, l. 774-794 (égale à l'octet, guillemets de citation ôtés, à
`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`,
`1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f`) :

> # Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)
>
> Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.
>
> **v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).
>
>
> 1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
>    - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
>    - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
>    - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
>    - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
>    - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
> 2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
> 3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
> 4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
> 5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
> 6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
> 7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
> 8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
> 9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.

### 6.2 Consigne scellée, § 5.2 « Jamais », recopié en entier

- Aucun score de sonde, de T0.6 ou de T0.7 : ni `sondes-t07.json`, ni `scores-actions-t07.npz`, ni `lecture-t07.json`, ni
  rien sous `diag/<RUN_T07>/` ; ni `diag/*/lecture-sondes-t06.json` d'aucun run (interdits, règle 1).
- Aucune activation : ni `donnees/<RUN_7B>/activations/` ni aucun fichier d'activations, ni les adaptateurs.
- Ni `diag/<RUN_7B>/lecture-cout-t06.json` (table A, base « coût seul »), ni le fichier d'issue « mots et coût », ni le
  fichier d'issue de P3-bis, ni aucun fichier de P3-bis.
- Rien de la course 7a (`20261109-070232-t06-reel`), ni la lecture B ni sa branche, ni les branches et chemins interdits de
  l'annexe A ; ni les textes d'actions de P3 ; ni le registre des ouvertures.
- Aucune recherche récursive hors des listes nommées (règle 9) ; aucun appel externe, aucun téléchargement (le découpeur
  n'est lu qu'au chemin donné par la mère ; l'auditeur ne le cherche pas) ; aucune dépense ; aucune écriture git.

### 6.3 Compléments de la mère (message du 2026-11-14), qui s'ajoutent et ne retirent rien

- Aucune donnée ni sortie de 7a ou de T0.7 (scores, sondes, lectures, journaux de course) ouverte ou affichée ; de T0.7,
  seul le texte scellé, aux lignes dites au § 3 ; de 7b, seulement les lectures du § 3, par programme.
- Jamais `diag/*/lecture-sondes-t06.json`, ni `lecture-cout-t06.json`, ni la lecture B de 7a, ni
  `donnees/lecture-b-7a-quarantaine-v1`, ni `donnees/mesure-unanime-v15-sortie-v1`, ni `essai/t06-explo-v3`, ni
  l'étiqueteur.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`,
  `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune valeur de clé ; aucune machine ; aucun identifiant de modèle dans tes fichiers (les modèles se notent par leur
  lettre) ; toute heure relevée par `date -u`.

## 7. Fin : ton message à la mère

La mère ne lit rien de 7b hors l'état BA-L2 (R-2741) : ton message ne porte **aucun contenu tiré des données de 7b**. Il donne
les chemins écrits et leurs empreintes sha256 ; ton verdict **de déroulement** en une ligne, l'une des deux : « audit terminé
sans arrêt : `audit-fuites-t07.json` écrit, validé par `valider_audit_fuites` et scellé » ou « audit arrêté : sous-commande
`<nom>`, motif au `rapport-arret-v1.md` » ; les points ouverts de procédure ; le chemin de ton bac à sable. La phrase gelée du
§ 11, les comptes, les séparations et les réserves restent **dans ton rapport et ton fichier**, que liront le contre-lecteur
puis l'étape B ; tu ne les recopies pas dans ton message. Aucune valeur tirée d'une sonde, aucun texte d'action. Après l'audit,
tu es exclu de tout rôle de lecteur de P3-bis, de contre-lecteur de T0.7 et de verdict de G0 (réglage Q8).

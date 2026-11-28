# Vérification des corrections — validateur renforcé des préenregistrements, v2

- **Relecteur** : Claude Sonnet 5.5, le même agent que pour la contre-lecture de la v1 (`c5c775b1caf9581d5f2b025d1e25977d48facecba89ba428cda907adcd8f84b4`).
- **Pièces vérifiées** : `src/controle_ia/prereg_renforce_v2.py` (`c7bb0ddb34fb0f6c3585e77ae2d853c6b59c8ccb5db15ae36fcaf7ec68e956f8`), `tests/test_prereg_renforce_v2.py` (`77b41e0adc780c9c0ae77d82f73423a9de1b9e5c21d0e7e146fb57f0e156dbae`, 167 essais), rapport v2 (`f775c0f7573960475a50d8df1aeb64f68bcb338c190ad0c248232ea8722ada11`) et son erratum 1 (`76063ecf046abf58c0fb2ce329c21aa76073511c32627449fcc6d68e42649ace`).
- **Garde de lecture** : aucun fichier gardé ouvert par moi ; mes essais tournent dans de faux dépôts, avec un crochet d'audit sur `open`. Aucun fichier du dépôt modifié.
- **Dossier des essais** : `/tmp/claude-0/-home-user-controle-ia-travail/9ac2612f-0076-57d6-b52f-57d24a4c6967/scratchpad/contre-lecture-validateur-renforce-v1/` (`v1.py` à `v7.py`, `t3v2.py`, `mut2/`, `pkg3/` = v2 telle que livrée, `pkg5/` = v2 + correctif proposé).

## Verdict : À CORRIGER

Les quatre remarques majeures de la v1 sont levées, et la v2 fait mieux que prévu sur les mutants. Mais la correction de la remarque 1 a introduit un trou dans la garde de lecture, qui est absolue : une empreinte écrite à côté d'un **dossier** fait hacher en mémoire des versions de fichiers gardés tirées de l'historique git (remarque N1). Le correctif tient en quelques lignes, je l'ai essayé (167 essais passent encore). Hors cela, une régression mineure sur (e) (N2) et deux réserves mineures (N3, N4).

`PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v2.py tests/test_prereg.py tests/test_prereg_renforce_v1.py` : **233 réussis** (rejoué). Les deux brouillons du 28 novembre : 12 et 10 problèmes, 263 fichiers gardés sautés, aucune ouverture gardée (`v3.py`), comme dans le rapport.

## Les 13 remarques

| # | remarque | état | preuve |
|---|---|---|---|
| 1 | Empreinte d'un autre fichier à côté d'un chemin | **levée** (résidu : N3) | `t3v2.py` : `src/a.py` + empreinte de `b.py` (phrase, table, rapport croisé, par rang) : problème « ce n'est pas l'empreinte de ce fichier… elle désigne … » ; formes saines (phrase, table) : aucun problème. Code : `paires` 373-399, vérification 488-522 |
| 2 | Garde contournée par `..` et liens | **levée** (mais voir N1) | `v1.py`, crochet d'audit : (a) `docs/../src/controle_ia/iib/secret.py:2` : avertissement « fichier gardé », aucune ouverture ; (b) lien suivi vers `iib` et vers un `.npz` : non hachés (seul `docs/ok.md` l'est) ; (c) lien cité `docs/lien.md:2`, `docs/lien2.md:1` : avertissement « lien symbolique » ; compagnon lien (`z.sha256 → x.npz`) : non lu ; `v6.py` : dossier-lien `docs/dirlink → …/iib` : refusé. Code : `Index.refus` 198-212, `est_garde` 93-99 |
| 3 | Garde ancrée à la racine passée | **levée** | `v1.py` (d) : `Index(src)` et `Index(brouillons)` : aucun fichier gardé haché, `gardes_sautes` = `controle_ia/iib/secret.py`, `ii-b-saboteur-budget-v9/x.md` ; préenregistrement hors racine, avec `--permettre-hors-racine`, relatif depuis un sous-dossier, ou lien vers `iib` : `GardeArret`, zéro ouverture |
| 4 | Empreintes de 63, 65 caractères ou en majuscules | **levée** | `t3v2.py` : 63 et 65 caractères : « longueur d'empreinte invalide » ; majuscules inventée et vraie : « empreinte en majuscules » ; 40 caractères : avertissement. Le brouillon G1 réel donne bien 10 problèmes dont une empreinte de 65 caractères |
| 5 | Faux positifs de (c) | **levée** | `t3v2.py` : `#titre`, `:L3`, `:fonction`, `:3,5`, `:3–5`, `AAAA-MM-JJ-HHMM`, `::test` (coupé) : plus de faux problème ; `:11` hors fichier encore signalé ; virgule ou point collé dans l'accent grave encore signalé (faute d'auteur, voulu) ; `v5.py`/`t4.py` : nom avec espaces accepté |
| 6 | (d) refuse une contre-lecture saine brève | **levée** | `t4.py` : contre-lecture de 21 mots acceptée ; section répétitive refusée (essais `test_d_section_repetitive`) |
| 7 | (b) dates, préfixes nus, ellipses | **levée en partie** | `20261128…` ignoré ; `..`, `‥`, `⋯`, préfixe nu lus (`t3v2.py`, 3 cas inconnus signalés). `12345678…` (huit chiffres hors date) reste signalé : acceptable. Raison du § 2 (« une lettre à partir de 12 caractères » non retenue) : suffisante |
| 8 | Issue pour une empreinte hors dépôt | **levée en partie** | `v5.py` : « hors dépôt » donne un avertissement ; sans la marque : problème. Marques « externe », « machine : » non retenues : raison suffisante (mots courants) |
| 9 | Robustesse | **levée en partie** | `v5.py`, ligne de commande : latin-1 → problème « (lecture) non lisible en UTF-8 », fichier absent → problème, le fichier suivant est traité, code 1 ; BOM : signalé (le message « section absente : Hypothèse » du validateur de base reste en double : l'interdiction de toucher `prereg.py` le justifie) ; git indisponible : avertissement « index git indisponible » ; `_nb_lignes` en flux (176-182 relues). Archives : décision de la mère, essayée (voir N4) |
| 10 | `resoudre` cache le fichier courant | **levée** | `connue`/`chemins` (287-291) ; message « elle désigne … » vu dans `t3v2.py` |
| 11 | Limites de (a) et (e) | **levée en partie** | Compagnon périmé : avertissement (`v5.py`) ; fichier vide : avertissement ; « fable » commun et « écrit par Opus » : refusés (`t4.py`) ; ordre d'emploi : documenté. **Régression** sur les entrées (N2). Raison du § 2 (forme « Relecteur : » non retenue) : suffisante |
| 12 | Mutants survivants | **levée en partie** | 54 mutants du module v2 (dont les analogues de mes 23 survivants, 16 mutants de garde ou d'appariement, l'identité), `mut2/run.py`, `mut2/sortie.txt` : **50 tués**, 4 survivent : l'identité (attendue), M01 (lookahead de `HEXLONG`, cas d'une suite hexadécimale collée à une lettre non hexadécimale), M28 (borne avant du nom de modèle) et P3 (« au plus un accent grave » entre chemin et empreinte). Les trois vrais survivants sont mineurs |
| 13 | Exemple faux du rapport v1 | **levée** | rapport v2, ligne 13 du tableau : reconnaît que `3b2e3ee5…` est l'empreinte du fichier courant ; j'ai vérifié (`sha256sum`) |

Les six points « non traités ou traités en partie » du § 2 : les raisons suffisent pour les quatre premiers et pour l'ordre d'emploi. Le dernier (« Relecteur : ») est une raison valable (refus de toutes les pièces actuelles), l'exclusion des tournures d'auteur la remplace en partie. L'archive : voir N4.

## Nouveaux défauts

### N1 — Majeur (nouveau, garde de lecture) : l'historique git d'un **dossier** fait hacher des versions de fichiers gardés

**Scénario.** Un préenregistrement écrit « Dossier `src/controle_ia` (`<une empreinte>`). » L'empreinte est appariée au chemin `src/controle_ia`, qui n'est pas un fichier ordinaire : `disque` renvoie `None`, puis `Index.historique(rel, h)` (314-358) est appelé. Il exécute `git log --all --raw -- src/controle_ia`, qui liste **tous les fichiers sous le dossier**, collecte leurs identifiants d'objet, et les passe à `git cat-file --batch`, puis calcule `hashlib.sha256` du contenu. La garde (`if est_garde(rel): return None`, ligne 316) porte sur le chemin cité, pas sur les fichiers listés.

**Preuve** (`v2.py`, faux dépôt avec `src/controle_ia/iib/secret.py` et `src/controle_ia/data.npz` suivis ; espion sur `cat-file --batch`) : pour `src/controle_ia`, les deux objets gardés (`e97e9c7e…`, `6477a166…`) sont envoyés à `cat-file` et hachés. Pour `src` ou `src/controle_ia/iib` : rien. Hors garde stricte, ce ne sont pas des fichiers du disque, mais « ni ouvert ni haché » est la règle, et le cas est atteignable par une simple citation de dossier.

**Défaut annexe, même fonction.** Pour un objet qui n'est pas un blob (un arbre), la boucle de lecture `continue` sans avancer `pos` de la taille du contenu (lignes 351-352) : les entrées suivantes sont mal lues, avec un risque d'exception `ValueError` ligne 348.

**Correction essayée** (`pkg5/`). Dans la boucle des lignes brutes de `git log`, lire le chemin après la tabulation et l'exiger égal à `rel` et non gardé :

```python
champs, _, chem_l = ligne.partition("\t")
champs = champs.split()
if chem_l.strip() != rel or est_garde(chem_l.strip()):
    continue
```

Résultat (`v2.py` avec `SRCX=pkg5`) : plus aucun objet gardé envoyé à `cat-file` (`total oids: 0`) ; les 167 essais passent. À ajouter : un essai avec le dossier cité (crochet sur `_git("cat-file", "--batch")`, comme mon espion), et un mutant « filtre de chemin retiré » qui doit échouer.

### N2 — Mineur (régression de (e)) : entrées en ligne nue, liste numérotée ou table ne sont plus découpées

`ENTREE` (ligne 149) n'accepte plus que puce, titre ou gras. Avec deux entrées en lignes nues (« Contre-lecture 1 : Fable… » / « Contre-lecture 2 : relue sans nommer personne… »), la v1 refusait l'entrée 2 sans modèle ; la v2 passe, puisque la section entière nomme « Fable » (`v5.py`, `v1` contre `v2`). Même chose pour `1. **Contre-lecture 1**` et pour une ligne de table. Le validateur de base, lui, découpe encore ces entrées. Sur les préenregistrements scellés : 3 sur 151 sections concernées (`addendum-1-gardes-analyses-r1-v4-v1.md`, `agregation-r1-v4-v1.md`, `audit-fuite-r1-v4-v1.md`). **Correction** : accepter une ligne nue qui commence par « Contre-lecture k » suivie de `\s*[:—–-]` (pas une phrase de prose), et le préfixe `\d+\.\s` ; ajouter l'essai (entrée 2 sans modèle, forme nue).

### N3 — Mineur : résidu de la limite 1, silencieux

Une empreinte séparée du chemin par un mot (« `src/a.py` signature `<empreinte de b.py>` ») ou écrite avant lui (« empreinte `…` du fichier `src/a.py` ») n'est pas appariée : acceptée, avec seulement « N empreinte(s) non appariée(s) à un chemin, lignes … » (`t3v2.py`). Le rapport l'avoue (limite 1). **Amélioration bon marché** : pour une empreinte non appariée mais connue, si la ligne cite des chemins et que `chemins(h)` n'en contient aucun, avertir « elle désigne X, pas les chemins de la ligne » (avertissement, pas problème : `manifeste_sha256` à côté de `tirage.json` est légitime).

### N4 — Mineur : archive avec compagnon et empreinte fausse = avertissement

Après l'erratum, `docs/avec.zip` (compagnon présent) cité avec une empreinte inventée donne seulement « empreinte d'archive non vérifiée » (`v7.py`), alors qu'un compagnon existe et la contredit. Le texte de l'erratum (« qu'aucun compagnon ne porte ») permet cette lecture, mais l'intention est de ne pas ouvrir l'archive, pas de laisser passer un faux. **Correction** : si `index.par_chemin.get(rel)` est non vide et ne contient pas `h`, c'est un problème ; l'avertissement ne reste que pour une archive sans compagnon. Les autres comportements des archives sont corrects (`v4.py` : archives gardées, compagnon lu, `.tar:3` en avertissement, empreinte nue = problème, `gardes_sautes` contient les trois archives, aucune ouverture).

## Régressions éliminées par contrôle

- Pas de faux positif nouveau sur les cas sains des remarques 5 à 7 (`t3v2.py`) ; aucun avertissement sur la pièce saine (`v5.py` « sain ») quand les empreintes de contre-lecture sont appariées. Sur les brouillons réels, l'avertissement « non appariée » est un bruit (22 et 21 empreintes), non bloquant.
- Temps : 11 s pour deux brouillons avec l'index complet, une seule construction par appel.

## Pour passer à PRÊT

1. N1 (obligatoire) : filtrer par chemin dans `historique`, essai de dossier, mutant. Correctif essayé dans `pkg5/controle_ia/prereg_renforce_v2.py`.
2. N2 et N4 : petites corrections avec essai (recommandées).
3. N3 : facultatif.
Après N1, je n'ai pas d'autre objection à la garde : crochet d'audit propre sur le dépôt réel et sur tous les faux dépôts.

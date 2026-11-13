# Audit des fuites de T0.7 — préparation : les trois conditions de R-2359 et le moment prescrit de l'audit — v1

Écrite le 2026-11-13T22:02:16Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), sur le « go » de la mère (R-2597, point 5 ; journal provisoire du compte 4, C4-0014). **L'auditeur n'est pas lancé.** Cette session, préparatrice, est exclue du rôle d'auditeur et de contre-lecteur du fichier d'audit (plan multi-comptes, lot « compte 4 »). Aucune dépense, aucune ouverture de `runs/`, `diag/` ou `donnees/` de 7a ou 7b.

## Sources (empreintes vérifiées)

- Consigne scellée de l'audit : `prereg/T0.7-consigne-audit-fuites-v1.md`, `43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d` (`verifier` : OK) ; § 3 (qui exécute), § 4 (quand), § 5.1 (lectures), § 6.1 (découpeur).
- Ligne R-2359 de `registres/decisions.md` sur `main` (`ee7f2f9c`), seule ligne lue de ce fichier (nommée par la mère) ; sa fin, recopiée : « **À tenir avant de lancer l'auditeur** (R-2355) : CLAF-18 contre P3-bis scellé, commit du découpeur `c7484c43` dans le clone de l'auditeur, versions du manifeste de 7b comparées à `.venv`. »
- Ligne `CONSIGNE-AUDIT-FUITES-T07` de `registres/scellements-v1.md` (seule ligne lue de ce fichier) : `| CONSIGNE-AUDIT-FUITES-T07 | 2026-11-11T14:08:06Z | prereg/T0.7-consigne-audit-fuites-v1.md | 43102e80…a5d |` : chemin et empreinte égaux au texte scellé.

## Condition 1 — CLAF-18 contre P3-bis scellé

**Ce que dit la consigne** (§ 4, « Ouverture des textes de 7b avant le verdict de P3-bis ») : l'auditeur peut ouvrir, par programme seulement, `textes-actions-t06.jsonl` et `mesures-t06.npz` de 7b avant le verdict de P3-bis ; « à vérifier par la mère contre le texte scellé de P3-bis » ; une règle contraire → attente du verdict.

**Commande rejouable** (fichiers nommés sous `prereg/`, compagnons conformes ; la ligne de registre qui scelle P3-bis n'a pas été lue par ce compte) :

```
for f in prereg/P3-bis-temoin-positif-v1.md prereg/P3-bis-addendum-1-garde-credit-v1.md prereg/P3-bis-addendum-2-telechargement-controle-v1.md prereg/P3-bis-addendum-3-relance-credit-v1.md; do
  PYTHONPATH=src python3 -m controle_ia.scellement verifier "$f"
  for p in 'textes-actions-t06' 'mesures-t06' 'textes de 7b|textes de la course 7b|textes de T0\.6' 'DT-4' '(7b|T0\.6).{0,80}(avant|jusqu).{0,40}verdict' '(jamais|interdit|aucun).{0,60}(7b|T0\.6|t06)'; do
    echo "$f [$p] $(grep -c -E "$p" "$f") : $(grep -n -E "$p" "$f" | cut -d: -f1 | tr '\n' ' ')"; done; done
```

**Résultat** (2026-11-13, sur `lot/compte-4-v1`) :
- `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce967796b944e2ca585ee0dc2d780189e8e0cbe429e390c427a46121cb`, 2 813 lignes) : `textes-actions-t06` 0 ; `mesures-t06` 0 ; « textes de 7b / de T0.6 » 0 ; les seules mentions de `textes-actions` portent sur `textes-actions-p3.jsonl` (l. 392, 1306, 1344, 2138) ; DT-4 : l. 170 (déclaration de rôle d'un rédacteur) ; « aucun … 7b/T0.6 » : l. 7, 49, 97, 169, 434, 436 (déclarations de lecture des rédacteurs), 1120, 1564, 1739, 2010, 2629.
- Règles qui bornent une lecture, lues en entier : **l. 1561-1566** (le lecteur du verdict de P3-bis ne reçoit aucun fichier de T0.7 ni `lecture-sondes-t06.json`) ; **l. 1736-1740 et 2629** (« aucune version de T0.7 scellée après `VERDICT-P3BIS` ne lit 7b », garde adaptée, N-066). Aucune ne vise l'ouverture des textes et des mesures de 7b par un auditeur avant le verdict.
- Les trois addenda (`4e188814…`, `c23b2eb0…`, `02674ff7…`) : les correspondances ne sont que des empreintes contenant la suite « 7b » ; aucune règle.

**Constat** : aucune règle de P3-bis scellé contraire à la règle de la consigne n'est trouvée par ces recherches ; la condition 1 paraît tenue. **Limites** : recherche par motifs, non lecture entière ; la confirmation reste à la mère (la consigne la lui attribue). La consigne d'audit est scellée le 11 novembre, avant toute `VERDICT-P3BIS` : la règle des l. 1736-1740 (versions de T0.7 scellées après le verdict) ne la touche pas.

## Condition 2 — commit du découpeur `c7484c43` dans le clone de l'auditeur

**Commande rejouable, sur le clone de l'auditeur, par la session hôte, avant le lancement** (l'auditeur ne fait aucun `fetch`, § 6.1 et annexe A) :

```
C=c7484c43657a2ce22d76af33efd06aaa11a6aafa; B=donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1
git cat-file -e "$C^{commit}" && echo présent || git fetch --depth=1 origin refs/heads/$B:refs/remotes/origin/$B
git cat-file -e "$C^{commit}" && echo présent
for x in tokenizer.json:79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4 tokenizer_config.json:177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424 special_tokens_map.json:6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec; do
  n=${x%%:*}; [ "$(git show $C:$B/$n | sha256sum | cut -c1-64)" = "${x#*:}" ] && echo "$n égal" || echo "$n DIFFÉRENT"; done
```

**Résultat dans le clone du compte 4** : commit **absent** avant (clone de session neuf, superficiel) ; branche récupérée par refspec explicite ; tête de la branche = `c7484c43657a2ce22d76af33efd06aaa11a6aafa` ; commit présent ensuite ; trois empreintes **égales** à celles de la consigne (§ 6.1).

**Constat** : condition tenable ; **un clone de session neuf ne la tient pas de lui-même** : la session hôte doit récupérer la branche avant de lancer l'auditeur.

## Condition 3 — versions du manifeste de 7b comparées à `.venv` (R-2355)

Le manifeste de 7b est sous `runs/<RUN_7B>/`, **interdit à ce compte** : la comparaison n'est pas jouée ici. Commande préparée et éprouvée :
- script `brouillons/audit-fuites-t07-preparation-compte4-v1/comparer-versions-7b-venv-v1.py`, `30e0212016ba694a6cbde1b6e77d7ee8ea95ff413379d90cd70ff6df6814a618` : lit la ligne `RUN-CONFIRMATION-T06` comme le § 4 le prescrit (préfixe `| RUN-CONFIRMATION-T06 | `, quatre cellules, une seule fois) ; contrôle **avant toute ouverture** la forme `runs/<RUN_7B>/manifeste.json` et `<RUN_7B>` ≠ `20261109-070232-t06-reel` (7a) ; vérifie le manifeste (ligne et compagnon) ; n'en lit et n'en affiche que le champ `versions` ; obtient les versions de l'interprète donné par la fonction même de la chaîne (`controle_ia.manifeste.versions`) ; code 0 (toutes égales, plateforme rapportée sans être jugée), 1 (une version diffère), 2 (garde : arrêt, rien comparé) ;
- épreuves (R5) : `essais-comparer-versions-7b-venv-v1.py` (`7718ba85f2c6732a979bdc3732f08556a03a719105be2d39ce242094ca28c316`), sortie `sortie-essais-comparer-versions-7b-venv-v1.txt` (`1c29c3e07ccdce79e7eeb70a639b43e5dcb4098d82a479a3a7766b2fb59c7532`) : six cas factices conformes (sain → 0 ; version différente → 1 ; plateforme différente → 0 ; course 7a → 2 avant ouverture ; ligne en double → 2 ; empreinte fausse → 2).

**Commande pour la session hôte** (depuis la racine de son clone, `.venv` installé) :

```
python3 -I brouillons/audit-fuites-t07-preparation-compte4-v1/comparer-versions-7b-venv-v1.py . registres/scellements-v1.md .venv/bin/python
```

Attendu : code 0. Code 1 : constat à porter à la mère avant tout lancement (ce que R-2355 prescrit en cas d'écart n'a pas été lu par ce compte). Code 2 : arrêt.

## Le moment prescrit de l'audit, relu au texte (§ 4)

- **Préalables** vérifiés par le script de l'auditeur (sous-commande `prealables`) : (1) consigne scellée sans marqueur, ligne `CONSIGNE-AUDIT-FUITES-T07` une fois (tenu : ligne lue ci-dessus) ; (2) ligne `RUN-CONFIRMATION-T06` une fois, contrôle de la course sur la ligne avant ouverture, manifeste conforme, `config.go_id` = `GO-2026-11-02-28`, **commit du manifeste présent dans le clone local, sans `fetch`** ; (3) les deux fichiers d'entrée de 7b conformes ; (4) aucune ligne `AUDIT-FUITES-T07` déjà inscrite.
- **Fenêtre** : après la poussée vérifiée des sorties de 7b (7b est finie le 12 novembre selon le plan multi-comptes, § 4.2 ; non relu au registre) ; **avant l'exécution de l'étape B de T0.7** ; elle peut précéder la fin de l'étape A ; ligne `AUDIT-FUITES-T07` strictement postérieure à `CONSIGNE-AUDIT-FUITES-T07`.
- **Emplacement** : l'auditeur écrit dans son propre dossier de sortie ; la mère copie le fichier à `diag/<RUN_T07>/audit-fuites-t07.json` une fois `RUN_T07` connu. L'étape A de T0.7 s'est arrêtée au contrôle avant l'ouverture (messages de commit de `main`, R-2588) : l'audit peut se faire, la copie attend le `RUN_T07` de l'étape A relancée.
- **Auditeur** : sous-agent neuf, **d'un autre modèle que celui que nomme le § 3 de la consigne**, qui n'a lu ni `sondes-t07.json`, ni `scores-actions-t07.npz`, ni `lecture-t07.json`, ni aucun score de sonde de T0.6 ou de T0.7 ; un contre-lecteur du fichier, neuf aussi ; la session mère lance, copie, inscrit.

## Autres commits que le clone de l'auditeur doit contenir sans `fetch` (§ 4, préalable 2 ; § 5.1, points 5 et 6)

Hors des trois conditions, mais du même ordre : un clone de session neuf est superficiel, et ces commits y manquent.

| commit | rôle (consigne) | état ici |
|---|---|---|
| commit du manifeste de 7b | préalable 2 ; sources de construction (§ 5.1, point 5) ; modules importés (point 6) | inconnu de ce compte (manifeste interdit) : la session hôte le lit dans le manifeste et le récupère par son empreinte complète |
| `7a54d431d89745839220f882b41b13e8c62ecfdd` | `statistiques.py`, `sondes/evaluation.py` (point 6) | absent, puis récupéré par `git fetch --depth=1 origin <empreinte>:refs/remotes/origin/audit-fuites-prep/7a54d431` ; `statistiques.py` à ce commit = `a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a`, égal à la consigne et à l'arbre ; `evaluation.py` égal à l'arbre |
| `1609a4bf2c1572f72bb8542d81d963ac6a8481c4` | comparaison des sources de construction (point 5, en réserve seulement) | absent, puis récupéré de même |
| commit du fichier que cite `CODE-T07` (commit C7) | `criteres_v1.py` (point 6) | `b4cd9953…` au 13 novembre, **appelé à changer** (R-2593) : à récupérer au commit en vigueur au lancement |

Commande, par la session hôte, pour chaque empreinte complète `E` de cette table : `git cat-file -e "$E^{commit}" || git fetch --depth=1 origin $E:refs/remotes/origin/audit-fuites/${E:0:8}`.

## État

Conditions 1 et 2 constatées tenables ici (la 1 sous confirmation de la mère, la 2 au prix d'une récupération dans le clone de l'auditeur) ; condition 3 préparée et éprouvée, non jouée (chemin interdit à ce compte). **Auditeur non lancé.**

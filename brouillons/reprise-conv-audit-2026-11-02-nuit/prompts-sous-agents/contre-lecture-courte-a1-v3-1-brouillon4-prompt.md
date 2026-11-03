Tu es un contre-lecteur neuf (règle R2) : tu n'as écrit ni le code de l'attaque de Goodhart v3 ou v3.1, ni son lanceur, ni ses préenregistrements, ni les contre-lectures précédentes. Français, sans sigle non développé ; heures par `date -u`.

## Objet
A1-v3 (GO-2026-11-02-21, 400 USD) : code **v3.1** (commit public `9776ed0`) et **brouillon 4** du préenregistrement, dans `/home/claude/ideation-organism/orchestrator/` :
- `pole/attaque_goodhart_v3.py`, `demonstrations/attaque_goodhart_v3.py`, `essais/test_attaque_goodhart_v3.py`, `essais/mutations_attaque_goodhart_v3.py` (comparer à `e58cfec` avec `git diff e58cfec 9776ed0 -- <fichier>`) ;
- `prereg/preenregistrement-attaque-goodhart-v3-brouillon4.md` (`6841b6c4…`) contre `prereg/preenregistrement-attaque-goodhart-v3-brouillon3.md` et les 42 couples `prereg/couples-contre-lecture-attaque-goodhart-v3-v1.json` ;
- le rapport du développeur `prereg/rapport-redaction-attaque-goodhart-v3-1.md` (ses dix points à vérifier en premier, et l'incident du premier passage du banc) ;
- la contre-lecture précédente `prereg/contre-lecture-preenregistrement-attaque-goodhart-v3-v1.md` et son rapport privé `/home/claude/controle-ia-travail/brouillons/passation-conv-audit-2026-11-02-soir/rapports-sous-agents/contre-lecture-a1-v3-brouillon3-rapport.md` (B1, I1 à I7, M10) ;
- la vérification du lanceur par session-depot `/home/claude/scratch/a1-v3-1/verification-lanceur-a1v3-v1.md` (VL-01 à VL-09) et les réponses sur le relais `/home/claude/scratch/a1-v3-1/session-depot_2026-11-02_n294.md` (§ 3).

## Questions
1. B1, VL-01, VL-02, VL-04 sont-ils levés, chacun avec un essai sur un cas sain et sur un artefact (R5) et une mutation tuée pour la bonne raison ? Le choix « arrêt sur tout code 4, même loin du plafond » est-il juste (un code 4 peut-il être passager : 402/429 du relais, refus de quota) ? Dis ce qui se passerait dans chaque cas.
2. Le brouillon 4 = brouillon 3 + 42 couples + les changements v3.1, et rien d'autre ? Les 117 renvois `fichier:ligne` renumérotés sont-ils justes (échantillon d'au moins 20) ? Bloc de 73 empreintes égal aux fichiers de `9776ed0` et à `FICHIERS_GELES` ? Seul marqueur : `<<COMMIT_V3_1>>` (5 fois) ?
3. Les écarts de la section 0.4, la dispense M10 (décision de Lazar, R-1294) et les réponses I7 sont-ils exacts et complets ?
4. La configuration gelée de la commande Argon passe-t-elle VL-01 (le développeur ne l'a pas relue) ? Lis-la là où le texte la cite.
5. Effet sur l'attaque v4 (qui importe la v3) : ses essais passent-ils, et que doit changer son texte ?
6. Tout ce qui empêcherait un résultat concluant « par défaut de conception » (exigence de Lazar).

Tu peux rejouer : `cd /home/claude/ideation-organism/orchestrator && TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 nice -n 10 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_attaque_goodhart_v3.py essais/test_attaque_goodhart_v4.py`, et le banc de mutations **une fois**. **Attention** : une course décisive (`demonstrations/banc_tricheurs_v9.py`) tourne dans ce clone ; n'ouvre ni ne liste `../resultats/banc-tricheurs-v9-validation-v1/`, et si un essai lance une course factice longue, arrête-la par son identifiant de processus.

## Rendu
Fichiers neufs : `orchestrator/prereg/contre-lecture-courte-preenregistrement-attaque-goodhart-v3-brouillon4.md` (verdict en trois lignes : scellable, scellable après couples, ou non scellable ; bloquants, importants, mineurs) et, s'il y a des corrections de texte, `orchestrator/prereg/couples-contre-lecture-attaque-goodhart-v3-brouillon4.json` (liste `{"ancien","nouveau"}`, chaque « ancien » présent une seule fois). Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`/`checkout`/`stash`, aucun appel de réseau ni de modèle, `nice -n 10`. Réponse finale : verdict, points une ligne chacun, chemins et sha256.

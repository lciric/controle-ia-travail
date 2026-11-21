# Vérification des corrections — additif 1, version 2, au devis du barreau 5 (plafond du stockage de l'instance de relecture) — v1

- **Nature** : vérification courte des corrections par le même contre-lecteur (allègement de la procédure). Claude Opus 5.5, sous-agent de la session mère, le 21 novembre 2026 vers 13:20 UTC. Aucune dépense, aucun appel au loueur, aucune écriture au registre propre, aucun résultat du barreau 5 ouvert.
- **Pièce vérifiée** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-additif-1-v2.md`, `c3120d3ade40f31f26a225cd2bf7c3520c7ba0a314e2b554832229d67c8e120c` (égale à son compagnon).
- **Contre-lecture d'origine** : `contre-lecture-additif-1-devis-et-constat-registre-v1.md`, `bdb46a66e762c06b57b60d7e7b50bfdf72b7c10a9857ecac312951a0163424cf`, § 1.6 (corrections C1 à C5).
- **Contrôles faits** : lecture entière de la version 2 et de sa table du § 7 ; renvois neufs vérifiés au commit `c76e79169eee337ce66c7d88f62d039e853eebfc` par `git show` ; frontières des épreuves recalculées en virgule flottante (Python 3.13).

## Verdict

**Conforme, prêt à sceller.** Les cinq corrections sont portées. Je ne conteste pas le choix fait pour C3, et j'accepte le motif qui écarte ma recommandation r2. Les deux remarques de la fin ne bloquent pas le scellement.

## Correction par correction

- **C1, tenue** (lignes 58 à 62, 68, 69, 91, 97, 101). La garde de l'arbre de la session (ligne 1073) est dite « non rejouée telle quelle : elle refuserait », et remplacée par (b) et (c), qui gardent ses deux autres clauses. Le mécanisme est nommé : recomposition du corps à partir des fonctions de la version 1. La substitution d'attribut de module est interdite, et un essai la refuse. `_montrer`, fonction privée, est récrite et non importée. Les fonctions importées existent au commit aux lignes citées : `exiger_registre_de_relecture` 186, `config_lecture` 848, `exiger_arbre_extrait_propre` 915, `piece_lecture` 970, `echeance_arret_lecture_s` 1007, `_montrer` 1019, `exiger_code_du_commit` 1026, `hashlib_sha256` 1102 ; `exiger_garde_de_calcul` est à la ligne 1410 de `formation_v1.py`. L'égalité à l'octet est éprouvée pour les deux pièces.
- **C2, tenue** (lignes 72 à 80, 99). Seule « commande », version 2, se joue depuis le commit de commande. « verifier » (ligne 876), « ouvrir » (`lecture_v1.py`, ligne 525) et toutes les autres sous-commandes se jouent depuis un arbre au code de lecture figé. Une épreuve voit « verifier » refuser depuis le commit de commande.
- **C3, tenue ; choix non contesté** (lignes 56, 82 à 89, 96). La répétition reste à la version 1, et la version 2 refuse le plan « repetition » à l'entrée. Le motif 2 est juste et suffit : sans ligne d'accord de lecture, rien n'épinglerait le commit de commande. Pour la répétition, (b) se réduirait alors à (c), garde plus faible que l'arbre figé à l'octet de la version 1. Le corps recomposé garde les deux branches, ce qui permet l'égalité à l'octet sur « repetition ». Valeurs recalculées : 0,19 USD par Go et par mois à 150 Go donne 0,0390, accepté ; 0,40 donne 0,0822, refusé.
- **C4, tenue** (lignes 21, 173). La règle des quatre cinquièmes est rattachée au calcul du devis (`facb727a…`, lignes 7 et 21) et à l'erratum 1 (`8c3451a2…`, ligne 41 : vérifiée). Le texte dit qu'elle ne donne pas la coupure de la répétition (11,5 → 8).
- **C5, tenue** (lignes 107, 130). L'écart à la ligne 7 du texte scellé est dit, couvert par `GO-2026-11-21-42`, borné, et cité dans la référence de la ligne de l'accord de lecture, que lit la vérification (d).
- **Recommandations.** r1 est portée (ligne 95). Recalcul en virgule flottante : 0,2920 × 300 / 730 rend exactement 0,12, donc accepté par `>` ; 0,2921 rend 0,12004, refusé ; 0,30 rend 0,1233 et 0,32 rend 0,1315, tous deux refusés. Les épreuves peuvent échouer comme réussir. r2 n'est pas retenue (ligne 113), et le motif tient : la garde s'appuierait sur le pas 4, encore supposé, et un pas faux bloquerait toute offre. La comparaison des deux prix, faite par la session, est la bonne étape d'abord. r3 est portée (ligne 17), r4 aussi (lignes 13, 136 à 145).
- **Ajout non demandé, le § 6** (effet de la voie (c) sur le registre propre). Il est juste : (c) ne touche aucun fichier figé, donc le § 3 tient. L'additif est dit sans effet tant qu'aucune voie n'est accordée. L'ordre d'inscription (correction de forme d'abord) garde l'empreinte `c4aeced7…` de l'état intact.

## Remarques non bloquantes (pour la mère, pas pour l'auteur)

1. **Le second accord de l'en-tête** (ligne 7). Il cite un « go » de Lazar sur l'additif 1 que l'auteur n'a pas relu, et je ne trouve dans `registres/go.md` aucune ligne postérieure à `GO-2026-11-21-42` qui le porte (lignes 642 à 646 lues). L'accord qui suffit à l'additif est `GO-2026-11-21-42`. La mère inscrit ce « go » avant le scellement, ou le cite par son identifiant dans la ligne sous la table du § 4.
2. **La garde de calcul jouée depuis l'arbre de commande.** `exiger_garde_de_calcul` charge `.claude/hooks/garde_calcul.py` depuis la racine passée et décide sur cette racine. Si l'arbre de commande porte un `registres/go.md` ancien, issu de `c76e7916`, sans la ligne de l'accord de lecture, la garde refusera. Ce défaut ne laisse rien passer, il bloque. Le développeur ou la session doit tenir ce fichier à jour dans l'arbre de commande ; c'est permis, car `registres` est hors des chemins gelés.

## Relevé de méthode

**Chaîne de raisonnement.** 1. Empreinte de la version 2 égale à son compagnon (`sha256sum`). 2. Chaque correction C1 à C5 se trouve aux lignes que dit la table du § 7 (lecture entière). 3. Les renvois neufs existent au commit (`git show c76e7916:…`, `grep -n "^def"` ; erratum, ligne 41). 4. Les frontières des épreuves se recalculent (commande Python citée au § « C3 » et « Recommandations »). 5. Pas d'autre accord que `GO-2026-11-21-42` au registre des accords (lignes 641 à 646). 6. La garde de calcul lit sa racine (`formation_v1.py`, lignes 1397 à 1423 au commit).

**Objets de contrôle.** Frontière du stockage : 0,2920 prédit accepté, rendu 0,12 exact et accepté ; 0,2921 prédit refusé, rendu 0,12004 et refusé. Répétition : 0,19 prédit accepté, rendu 0,0390 ; 0,40 prédit refusé, rendu 0,0822. Le montage lui-même n'existe pas encore : non éprouvé.

**Premier pas non justifié.** Aucun dans cette vérification : chaque pas renvoie à une pièce ou à un calcul rejoué. Le pas 4 de l'additif (prix à 300 Go) reste supposé chez l'auteur, et il le dit.

**Mode d'échec affecté.** Sans objet : vérification des corrections d'une contre-lecture déjà rendue ; j'ai visé « Énoncé infidèle » et « Objet de contrôle oublié ou inopérant », comme l'auteur le proposait.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas agent de re-dérivation.

**Trouvaille de côté.** La remarque 2 ci-dessus. Rien d'autre.

**Évaluateur et conseil.** Ce qui juge cette vérification : le scellement par la mère, puis la contre-lecture du code de commande, version 2, quand il existera. Par où elle pourrait être jugée bonne sans le mériter : le montage n'est vérifié qu'à la lecture du code figé, jamais exécuté, et le relevé date de 10:55Z.

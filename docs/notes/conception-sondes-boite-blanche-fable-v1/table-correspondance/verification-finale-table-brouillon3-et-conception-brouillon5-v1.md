# Vérification finale de la table de correspondance (brouillon 3) et de la conception des sondes de la boîte blanche (brouillon 5) — version 1

- **Contre-lecteur indépendant** : même sous-agent neuf (conversation `c1a698101768d186848b8244a50d9f5c`), distinct de l'auteur (`408edcf5d0ec826fe4a61c5b411328fe`), mandaté sous `GO-2026-11-23-32` et `GO-2026-11-23-33`.
- **Date et heure en temps universel coordonné** : 2026-11-23, 21:12.
- **Pièces vérifiées et empreintes recalculées** :
  1. `table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md` : `9b0e2c1304ab914ef943c4e99693d1fd9b60e6d4e4b4bee6f392e02264d6bf42`.
  2. `verification-formelle-table-correspondance-brouillon3-v1.py` : `092b9651cba86b6c87f494f0347e22a6bb8e4fcda6c071c0747fc922a1112571`.
  3. `conception-sondes-v2-brouillon5.md` : `e9ad9d8af24e43724c5b99bda74981c8f896b248f46a833dc1c96613cdba0b8d`.
  4. `table-suivi-corrections-brouillon2-vers-3-et-4-vers-5.md` : `b8e0a2d499ed2af96068c8f7085aceb283d3cfb5197d3b6fbafb77f67a8268d3`.

---

## Verdicts

1. **Table de correspondance des issues du test « sabotage ou empreinte » sur les adaptateurs jumeaux (version 1, brouillon 3)** : **`CONFORME — PRÊT À SCELLER APRÈS LES MOTS DE LAZAR`** (arbitrage préalable des quatre points de jugement de la section 9 ; une micro-précision d'écriture sur la ligne 12 de la table en cas de cumul fictif `manipulation + garde 13` signalée ci-dessous sans caractère bloquant, le texte scellé ne pouvant pas prononcer à la fois la manipulation et la garde 13 et la règle 4 donnant priorité absolue au cas `(a)`).
2. **Conception des sondes de la boîte blanche, version 2 (brouillon 5)** : **`CONFORME — PRÊT À SCELLER APRÈS LES MOTS DE LAZAR`** (report final de l'empreinte de la table scellée à la section 7 avant le scellement de la note de conception).

---

## 1. Vérification point par point des corrections (brouillon 2 -> 3 et brouillon 4 -> 5)

| repère du rapport précédent (`5956ea60…`) | vérification dans les brouillons corrigés | statut |
|---|---|---|
| **M-T1** (recouvrements lignes 3, 8, 2 contre ligne 12 ; absence d'effectifs) | Table brouillon 3, section 1 (l. 26) et section 3 (l. 67-70, 73-74, 78) : les lignes 2 et 8 exigent désormais effectifs présents et au moins égaux à six ; la ligne 3 exige motif conforme, quatre effectifs présents au moins égaux à six, et soit mention autre que 99 % soit quatre effectifs au moins égaux à huit ; l'absence d'effectif (`S`, `D`, `C`) et tout effectif sous six passent en ligne 12. **0 recouvrement sur les 18 432 combinaisons `S/D/E/N/C/X` testées.** | **Levé** |
| **M-T2** (trous sur `NI` : garde 13 anormale, 2e relance autorisée par Lazar ; formation vs hors formation) | Table brouillon 3, section 2 (l. 34-35, 42, 44-45, 54, 57), section 3 (l. 75-78), règles 4, 6 et 9 (l. 87-88, 90, 93) : distinction nette formation contre hors formation aux points 1, 3 et 4 ; anomalie garde 13 sous libellé « non interprétable » renvoyée en ligne 12 ; seconde relance technique autorisée par décision nommée de Lazar renvoyée en ligne 9 ; causes techniques hors sept causes ou sans trace renvoyées en ligne 10 `(f)`. | **Levé** |
| **m-T1** (parenthèse « au niveau de 99 % » explicite aux lignes 1, 4 et 7) | Table brouillon 3, section 1 (l. 24) et section 3 (l. 67, 70, 73) : mention explicite « au niveau de 99 % » traitée exactement comme l'absence de mention autre que 99 %, prouvé sur les cas limites 32 et 38. | **Levé** |
| **m-T2** (retrait d'« empreinte » de l'incohérence à 6-7 familles en ligne 12) | Table brouillon 3, section 1 (l. 27) et section 3 (l. 71, 78) : `E3 = 6` ou `7` ou absent reste en ligne 5 ; seule la contradiction `E3 < 6` (ou doute explicite) passe en ligne 12 (cas limite 37). | **Levé** |
| **m-T3** (développement uniforme des sigles) | Contrôlé par programme : tous les sigles développés avant ou à leur première occurrence dans la table, la conception et le suivi (zéro emoji, aucun sigle nu hors codes officiels `GO`, `CODE-LECTURE-B5F`, `NI`). | **Levé** |
| **m-T4** (script formel compagnon R5) | Script `verification-formelle-table-correspondance-brouillon3-v1.py` exécuté dans cette session : **0 recouvrement, 0 trou logique, 0 écart à l'attendu** sur les **38 cas limites** et **172 combinaisons**. | **Levé** |
| **M-C1** (quatre points sur la marche causale `I-0046`, section 2 bis) | Conception brouillon 5, section 2 bis (l. 48-66) : (1) cinquième issue **prioritaire `(e)` — Artefact de casse de capacité générale** devant `(a)`, `(c)`, `(b)`, `(d)` rendant la partition strictement disjointe et exhaustive ; (2) géométrie unique fixée sans « ou » : tirage gaussien déterministe par `numpy.random.SeedSequence` (`R9`), orthogonalisation stricte par procédé de Gram-Schmidt contre `d_sab` et normalisation unitaire exacte ; (3) fenêtre explicite en décodage autorégressif ; (4) interdiction formelle de lire la chute de la sonde à la même couche ablatée, lecture imposée exclusivement sur couches aval et transcriptions générées. | **Levé** |
| **M-C2** (plafond `n <= m` de `N-076` et périmètre `N-053` point 1) | Conception brouillon 5 : section 5 point 7 (l. 132) et section 9 (l. 193) portent explicitement le plafond `n` au plus égal à `m` sauf nul par acte, les invariants d'audit après coup hors ligne sans retour à l'agent (`N-076` sections 2 et 8) et l'absence de borne chiffrée sans mesure de `q` par dommages plantés (`N-075` erratum 3 point 11) ; section 3 bis volet 2 (l. 93-96) et section 8 point 7 étendus à toute direction de sonde du programme entrant en phase 1 ou dans le papier sur l'instrument. | **Levé** |
| **m-C1 à m-C3** (`R-5168`/`R-5171`, section 7, sigles développés) | Lignes `R-5168` et `R-5171` vérifiées (lignes 5310 et 5313 de `registres/decisions.md`), section 7 mise à jour vers le brouillon 3 et le script formel, mention « constat fait par un agent neuf distinct de l'agent du rangement » portée dans « Audit de symétrie » (l. 178), sigles `D-3`, `P6`, `M1`, `M3`, `H6`, `H8`, `T0.7` développés. | **Levé** |

---

## 2. Contrôle formel indépendant sur le brouillon 3

Le contre-lecteur a exécuté :
1. le script compagnon de l'auteur (`verification-formelle-table-correspondance-brouillon3-v1.py`, empreinte `092b9651…`) : **38/38 cas limites** et **172/172 combinaisons** validés avec **0 trou**, **0 recouvrement**, **0 écart** ;
2. son propre script indépendant en produit cartésien large (`/tmp/check_full_cartesian.py` et `/tmp/check_diff_and_indep.py`) traduisant littéralement les cellules du brouillon 3 :
   - **18 432 combinaisons** sur les issues `S`, `D`, `E`, `N`, `C` et libellés inconnus `X` (croisant toutes les mentions de niveau, motifs, effectifs `None / <6 / 6-7 / >=8` sur quatre épreuves et doute explicite) : **0 anomalie, 0 trou, 0 recouvrement** ;
   - **1 280 combinaisons** sur l'issue `NI` : **1 216 cas** à sortie unique et exacte ; les seuls **64 cas** à double activation `[10, 12]` correspondent à la combinaison synthétique impossible où un verdict porterait simultanément la phrase de manipulation `(a)` et la garde `13`, déjà tranchée sans ambiguïté par la priorité de la règle 4 (qui place la phrase de manipulation toujours en ligne 10 `(a)`) et par le fait qu'une seule condition fonde une issue au texte scellé. Si l'auteur ou la session mère souhaite même éliminer ce cas chimérique de la lettre du tableau, il suffit de lire à la ligne 12 : « anomalie d'une garde 13 prononcée sous libellé `NI` hors phrase de manipulation ». Cela ne bloque en rien le scellement.

---

## 3. Cloisonnement et intégrité du dépôt

- Dépôt `/home/antigravity/lciric/controle-ia-travail` inchangé (`git status --porcelain` vide).
- Aucun fichier des dossiers cloisonnés (`prereg/barreau5-*`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/*`, `registres/etat.md`) n'a été ouvert.
- **Ligne `qui a lu quoi` complémentaire** (même sous-agent `c1a698101768d186848b8244a50d9f5c`, `2026-11-23T21:12Z`) : s'ajoutent à la liste du rapport précédent (`5956ea60…`) les quatre fichiers vérifiés du lot courant (`table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md`, `verification-formelle-table-correspondance-brouillon3-v1.py`, `conception-sondes-v2-brouillon5.md`, `table-suivi-corrections-brouillon2-vers-3-et-4-vers-5.md`).

# session-depot → conv-audit — n° 154 — 2026-10-29, 05:24 UTC

**Contre-lecture du script de la garde δ v3** sur `main` (`a1447546`, `c372c18c`) : `docs/notes/couche-2-preparation-v1/
contre-lecture-garde-delta-v3/contre-lecture-garde-delta-v3.md` (`8d4d5ffe…`). Opus neuf, 04:58 → 05:18 UTC.

**Verdict : utilisable après corrections.** Fiche « sujet partagé » = `pari_apparie.evaluer` v41 à 7,1·10⁻¹⁵ sur 1 000 fiches
(495 à longueurs de garde et de contraste différentes ; même prolongement par la dernière valeur) ; trois sorties
reproduites ; graine neuve ≤ 0,033 ; artefacts sous leurs bornes. GD2 : 01 (en grande partie), 04, 06, 07, 08 corrigés ;
02, 03, 05, 09, 10, 11 en partie.
- **GD3-01 (majeur)** : l'« effet d'unité sur A » écrête u à 0 et **déplace l'espérance** (τ = 0,01, σ = 0,05 : E[f_A]
  0,010 → 0,025, biais + 0,015). La chute de la garde (0,89 → 0,014) se retrouve avec ce seul biais, sans effet d'unité
  (0,006) ; à espérance tenue, la garde vaut 0,86 ; le lien garde-contraste change la fiche d'au plus 0,01. « Second effet
  de GD2-02, plus fort que le partage » : non soutenu — c'est un biais, pas une dépendance.
- **GD3-02 (moyen)** : même ensemble d'unités et un seul effectif imposés à la garde et au contraste ; identifiant d'unité
  refusé ; appariement entre fichiers par l'ordre des lignes, sans contrôle. La spécification v2 et le pôle ont deux
  ensembles (unités à épisode honnête, unités à épisode saboté).
- **GD3-03 (moyen)** : quatre replis silencieux (code 0) : `--ecarts-contraste` sans `--ecarts` ignoré ; garde réelle sans
  fichier de contraste → contraste synthétique ; `--comparateurs` forcé au nombre de fichiers ; `--effectif-attendu` sans
  fichier ignoré.
- Mineurs : GD3-04 (état git faux hors dépôt ou fichier ignoré ; manifeste `12e765e8` contre sortie `e07b4cda`) ; 05 (entier
  de 401 chiffres → `OverflowError` brute ; clé JSON doublée acceptée ; `0.0_5` lu 0,05) ; 06 (lecture 2 : ce qui limite
  dépend de K **et** τ — à K = 3, τ = 0,10, δ = 0,05, la garde limite ; lecture 3 : δ = 0,10 résiste aussi à K = 3,
  τ = 0,01 ; contrastes à 64 : 0,07–0,12) ; 07 (« 20 (m = 1) » écrit quels que soient α et m ; retenue e-BH non simulée) ;
  08 (rôle et comparateur des fichiers non écrits ; même fichier pour deux comparateurs accepté ; métadonnées de la
  spécification sans entrée).

Lecture (synthétique, sans trancher) : δ = 0,05 → garde 0,89 à 160 sous la loi favorable, 0,03 à biais 0,0125, 160 à 530
unités pour 80 % ; δ = 0,10 → passe partout à 160 et tient 0,025 sauf K = 3, τ = 0,10 (0,59), mais tolère un sujet qui
alerte ≈ 10 points de plus sur les honnêtes ; à 64 unités la fiche ne passe jamais (≤ 0,011). Pour P-26 v4. Une v4 courte
(GD3-01 à 03) quand tu veux.

Note de dépôt : le relecteur avait laissé un petit dépôt git d'essai (`sorties/essai_git/`, GD3-04) ; versé par erreur comme
sous-module dans `a1447546`, corrigé dans `c372c18c` (archive `essai_git-v1.tar`, scellée). Les empreintes du relecteur
listent les fichiers d'avant l'archive.

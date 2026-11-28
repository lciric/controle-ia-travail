# Consigne du correcteur neuf de la revue « comment détecter » — v6 — v1

Session 16, 2026-10-21 vers 00:20 UTC. Dépôt de travail `/home/user/controle-ia-travail` (noté `R`, lecture seule).
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection`.

## Qui tu es
Un correcteur neuf : tu n'as écrit ni la revue (v1 à v5), ni aucune de ses vérifications ou traitements. Français,
phrases courtes, quasi aucun acronyme (développe les termes).

## Ce que tu fais
1. Lis en entier (vérifie chaque empreinte contre son compagnon `.sha256`) : la v5 `…/synthese-comment-detecter-v5.md`
   (`17069e06…`) ; le traitement du correcteur v5 `…/traitement-verification-v4-par-correcteur-v1.md` (`21e1d56c…`) ; la
   vérification « fidélité » `…/verification-v5-fidelite/verification-v5-fidelite-v1.md` (`05472092…`, 8 constats) ; la
   vérification « sens » `…/verification-v5-sens/verification-v5-sens-v1.md` (`e3e4a650…`, 14 constats) et leurs fichiers
   de travail.
2. Écris la v6 `…/synthese-comment-detecter-v6.md` : chaque constat des deux rapports appliqué **en mots exacts** quand le
   rapport propose une correction écrite ; sinon la correction la plus petite qui lève le constat, sans ajouter d'idée.
   Aucun ajout non sourcé (R7 : un chiffre renvoie à un PDF et une page ; R8 : « non trouvé dans les sources lues »).
3. **Ce qui reste à Lazar, jamais tranché par toi** :
   - VV5-sens-01 : la version de E2 « sans condition qui réplique P3 » reçoit l'option « (b′) » **comme proposition du
     vérificateur**, avec son repli (a), sous la mention « **[Décision de Lazar en attente : P-015, et ajout d'une
     condition à T0.6 (nœud)]** ». Écris-la dans les mots du rapport ; ne la présente jamais comme décidée.
   - VV5-sens-03 : la divergence avec P-017 écrite en options (A), (B), (C), (C′) comme le rapport les pose, sous
     « **[Décision de Lazar en attente : P-017]** ».
   - Toute autre phrase qui suppose une décision non prise (N-030, nœud « Revendication ») garde une mention d'attente.
4. **PDF manquants** ([N], [X], [DYL]) : si la v5, ses extraits (`…/extraction/`, `…/txt-nouveaux/`) ou `R/docs/sources/`
   donnent un identifiant arXiv exact, télécharge le PDF depuis arxiv.org seulement dans `…/correction-v6/pdf/` (nom =
   identifiant et version), calcule son empreinte, et refais à la page les contrôles qui en dépendaient (y compris ceux
   sur DYL, LB, BU, AU signalés par la vérification « fidélité »). Sinon, écris dans la v6 que la page est lue sur un
   extrait texte sans PDF empreinté, et ce qu'il faudrait pour lever la réserve. La section 6 ne dit plus « empreintes
   vérifiées ce jour » pour un PDF absent.
5. Écris `…/traitement-verifications-v5-par-correcteur-v1.md` : une ligne par constat (identifiant, ce qui a changé,
   passage de la v6, ou « non appliqué » et pourquoi), puis la liste des points laissés à Lazar.
6. Contrôles : pour chaque phrase neuve qui cite une page, un contrôle par script (trouvée à la page citée), éprouvé sur un
   artefact (R5). Un sceau compagnon `.sha256` (format `sha256sum`, nom relatif) pour chacun de tes fichiers.

## Règles
- Écris seulement sous `…/` : `synthese-comment-detecter-v6.md`, `traitement-verifications-v5-par-correcteur-v1.md`, leurs
  sceaux, et `…/correction-v6/` pour tes essais. Ne modifie aucun fichier existant (R12).
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`,
  `R/diag/`, `R/traces/`, pas même pour une empreinte. **Aucune recherche récursive** dans le dépôt ni dans le système de
  fichiers (pas de `find /`) : lis les fichiers par leur chemin. Aucune commande git d'écriture.
- Réseau : arxiv.org seulement, pour les PDF du point 4. Aucun sous-agent ; aucune clé affichée ; aucune dépense ;
  `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemins et empreintes de la v6 et du traitement ; nombre de constats appliqués et non appliqués (avec
identifiants) ; PDF retrouvés ou non ; les trois changements les plus lourds ; la liste exacte des points laissés à Lazar.

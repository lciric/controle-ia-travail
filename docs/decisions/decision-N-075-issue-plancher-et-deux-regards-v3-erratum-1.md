# Décision N-075, version 3 — erratum 1 : quatre corrections de lettre de la vérification de la v3

- **Ce que c'est.** Un erratum à `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` (`5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`), qui n'est pas modifiée (R12). **La v3 se lit avec cet erratum, qui prime** sur les cinq passages qu'il remplace ; tout le reste de la v3 est inchangé.
- **Source.** La vérification de la v3 par Claude Opus 5.5, vérificateur remplaçant : `docs/decisions/verification-decision-N-075-v3-v1.md` (`bbee97b11c592328332593a02c629053502432aac1671ee7b87678e44efaf03b`). Verdict : « corrections : quatre, petites, toutes de lettre » ; après ces remplacements, la pièce est « prête pour Lazar sans nouvelle vérification ».
- **Auteur et heure.** Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), auteur de la v3, sur mandat de la session mère ; 21 novembre 2026, 14:12 UTC (`date -u`). Aucun appel payant, ni commit ni poussée.
- **Portée.** Les quatre corrections sont portées **mot pour mot** : chaque texte ancien et chaque texte nouveau est recopié de la vérification, et un programme a contrôlé que l'ancien figure une seule fois dans la v3 et que l'ancien et le nouveau figurent tous deux dans la vérification. Aucun énoncé, aucune option, aucun critère ne change. Les cinq choix ouverts de la section 11 de la v3 (points 7 à 11) restent ouverts, sans défaut.

## Les quatre corrections

Les numéros de ligne sont ceux de la v3, calculés par programme. La correction C-4 compte deux remplacements.

### C-1 — § 1 du programme, citations du plancher (texte à reporter, section 10) (v3, l. 233)

- Ancien : « sous plafond de dommage par épisode (limites au § 4) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). » »
- Nouveau : « sous plafond de dommage par épisode (limites au § 4) ; ce plancher est publié et n'est pas un apport du programme (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas pour l'excès sur un risque de référence) ; les moniteurs en sont l'accélérateur et l'aiguillage (N-075). » »

### C-2 — § 8 du programme, troisième citation (texte à reporter, section 10) (v3, l. 237)

- Ancien : « publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden) ». »
- Nouveau : « publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas) ». »

### C-3 — section 7, point 1, renvoi au nœud du lemme (v3, l. 184)

- Ancien : « validité sous dépendance : L3 et suivants de N-004). »
- Nouveau : « validité sous dépendance : L3 et suivants de N-004). C'est la lecture de `GO-2026-11-21-47` ; la lecture des voisins la rend partiellement occupée, et seul le reste qu'elle nomme pourrait se revendiquer, dans la forme que fixera le mot de Lazar (section 11, point 10). »

### C-4, premier remplacement — ligne pour `CLAUDE.md`, source de « accélérateur » (section 12) (v3, l. 264)

- Ancien : « N-075 (GO-2026-11-21-47, -51, -53) »
- Nouveau : « N-075 (GO-2026-11-21-46, -47, -51, -53) »

### C-4, second remplacement — phrase de longueur sous la ligne (section 12) (v3, l. 266)

- Ancien : « Longueur : 575 signes (plafond de 600, mesurée par programme). C'est la ligne du vérificateur (V10), reprise mot pour mot. »
- Nouveau : « Longueur : 580 signes (plafond de 600, mesurée par programme). C'est la ligne du vérificateur de la v2 (V10), avec « -46 » ajouté par le vérificateur de la v3 (source de « sondes en accélérateur »). »

## La ligne pour `CLAUDE.md`, après C-4

Elle remplace celle de la section 12 de la v3 (580 signes, mesurés par programme ; plafond de 600) :

> N-075 (GO-2026-11-21-46, -47, -51, -53) : contre le diffus, mesurer l'issue et corriger — plancher d'audit au hasard (publié, « Blindfold » : base citée, jamais revendiquée), oracle exogène, plafond, horizon, hors porte ; sondes en accélérateur, non en garantie ; dilemme plutôt que décorrélation ; pince en trois objets ; alerte = signal et dommage au même endroit, aucun épisode du suspect dans les témoins ; lemme : forme valide à tout instant sur sondes, 1981 cité, reste au mot de Lazar ; veille dégelée (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md`).

La mère la complète selon les mots de Lazar sur les points 7 à 11, et retire « veille » de la liste des gelés, comme le dit la v3.

## Ce que cet erratum ne fait pas

- Il ne rouvre aucune pièce : ni la lecture des douze voisins, ni aucun PDF, ni la note sur la couverture de l'oracle.
- Il ne modifie ni la v3, ni son compagnon, ni `CLAUDE.md`, ni le programme, ni les registres.
- Il ne corrige pas la table de la section 14 de la v3 : les quatre corrections changent des mots à l'intérieur de lignes existantes, donc aucun numéro de ligne.

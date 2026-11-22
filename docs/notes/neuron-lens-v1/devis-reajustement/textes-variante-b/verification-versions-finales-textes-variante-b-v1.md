# Vérification des versions finales des deux textes de la variante B — v1

- Vérificateur : sous-agent neuf, Sonnet 5.5, même cloisonnement que la vérification des brouillons 2 (`verification-brouillons2-textes-variante-b-v1.md`, `6d00df06…`). Heure (`date -u`) : 2026-11-22T05:3xZ ; branche à jour (déjà à jour).
- Empreintes : statut final `386c3e16…` et plan final `02ee9971…` recalculés égaux à la demande (non scellés) ; `differences-brouillon2-version-textes-variante-b-v1.md` `06945b0d…` : `verifier` OK.

## Question 1 — `diff` contre les brouillons 2
Seuls changent : le titre (« , brouillon 2 » retiré) et le bloc « Différences avec le brouillon 1 » (retiré) ; pour le statut, C-5 (§ 1) ; pour le plan, C-1 (§ 7 et ligne de § 10), C-2 (trois lignes du tableau), C-3, C-4. Les textes insérés sont ceux demandés, mot pour mot. Le tableau de la note de différences est exact (lignes 182, 259, 31, 25-26, 232, 197, 39).
- Écart 1 (espace avant la virgule de C-1) : **acceptable, et c'est le bon sens**. Ma formulation « remplacer « hors de ce que permet le § 7 » par « , ou un fichier… » » aurait supprimé la fin de la phrase ; la version finale la garde (« …une valeur du 18, ou un fichier de ces dossiers hors de ce que permet le § 7 »), ce que je voulais dire.
- Écart 2 (place de l'ajout C-2 dans la dernière cellule) : **acceptable** ; la table reste bien formée.
- Aucun autre écart : tenu.

## Question 2 — réserves du correcteur
- (a) Mot « brouillon » dans le corps (statut l. 3-4 et 27 ; plan l. 6 et 294-296) : **non bloquant**. Ce sont des phrases d'historique sur le processus ; l'interdiction de C-1 vise les fichiers brouillons, pas le mot. Nuance : « Ce brouillon est scellé tel quel » dans un texte scellé est maladroit. Correction facultative, mot pour mot : statut l. 3-4 et plan l. 6 : remplacer « Ce brouillon est scellé tel quel ; une correction est un brouillon neuf (R12). » par « Ce texte est scellé tel quel ; une correction est une version neuve (R12). » ; statut l. 27 : « scellée avec ce brouillon » par « scellée avec ce texte » ; plan § 12 : « sur ce brouillon » par « sur ce texte », « du brouillon relu » par « du texte relu », « dans le brouillon suivant » par « dans la version suivante ». Si on la fait, le texte change : nouvelle empreinte, rien d'autre à relire.
- (b) La déclaration à l'étape F : **non bloquant**. Le § 7 en fait une lecture permise, pas un fichier dont dépend un calcul ; l'ordre de l'étape F ne perd rien. Correction facultative : étape F, après « le verdict d'identité entier », insérer « , la déclaration du rédacteur (`declaration-redacteur-textes-variante-b-v1.md`, `57c98aa5…`) ».
- Si ces deux corrections facultatives ne sont pas faites, rien ne bloque le scellement.

## Exposition (R4)
J'ai relu les deux `diff` contre les brouillons 2 et la note de différences ; rien de nouveau du 18 que ce que j'avais déjà lu. Je n'ai ouvert ni le verdict du 18, ni l'accord de Lazar, ni `diag/`, `runs/`, `docs/verdicts/`, ni les branches interdites ; aucune requête réseau ; aucun refus d'outil.

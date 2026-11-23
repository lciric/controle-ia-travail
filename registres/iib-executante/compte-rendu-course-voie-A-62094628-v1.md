# Compte rendu de la course du saboteur à budget, voie (A), machine 62094628 — v1

Pièce de travail (classe C), nombres et états seuls (additif de la voie (A), § 4.4, étape 8 ; additif 8e1d340a…, devis 5bcfede2…). EXPLORATOIRE, NON OPPOSABLE (R-522). Aucune sortie ouverte. Écrit le 2026-11-23 vers 18:25Z par l'exécutante v7 (session_016QhUrrzvUnExGyzZHznnaF).

## Machine et dépense
- Machine Vast 62094628, étiquette iib-voie-a-v1, carte A100 SXM4 à 1,08 USD/h, stockage 0,0333 USD/h ; créée 2026-11-23T04:21:19Z ; arrêtée par l'amorce à 13:20:36Z (« ARRÊT OBTENU », HTTP 200) ; détruite par l'identifiant à 18:21:12Z (code 0, absente de deux relectures concordantes de l'inventaire).
- Dépense comptée au prix lu : carte 8,988 h = 9,71 USD ; stockage 13,998 h = 0,47 USD ; forfait de téléchargement 1,56 USD ; machine 11,74 USD. Dépense antérieure déclarée (compte de la voie) 3,61 USD ; voie (A) en tout ≈ 15,35 USD, sous le plafond total de la création (58,61 USD) et la ligne GO-2026-11-22-75 (60 USD, prolongée par GO-2026-11-22-93). À rapprocher de la facture du loueur.
- Échéance absolue 1795515638 (2026-11-24T10:20:38Z) non atteinte ; garde de la course : POURSUIVRE à chaque relevé lu ; deuxième et troisième remparts : non joués (course finie avant l'échéance) ; aucun code 7, borne du nœud sans objet.

## Marques
- Début (chargement, tirage=carte) 04:39:45Z ; tour 1 04:58:43Z ; tour 4 05:49:23Z (avant la limite de rythme 06:34:00Z) ; 20 tours de 32 épisodes, 0 repli (dernier 10:29:16Z) ; distillation finie 10:54:28Z ; évaluation des quatre conditions (H, B50, B100, TJ100 ; 64 épisodes chacune) de 10:54:40Z à 13:20:20Z ; fin de l'amorce 13:20:35Z, code 0.
- Tirage écrit au journal de l'amorce : TIRAGE=carte (2 lignes). Suite d'essais sur la carte : 313 passés (313 attendus).
- Fin de la course : fin normale (« run terminé », ligne de fin de l'amorce ; surveillance FIN à 18:20:34Z) ; versement de fin 3326499e (13:20:33Z) : sorties des tours, distillation, évaluation, manifeste et résumé du run versés.

## Rapatriement
- Branche essai/iib-explo-v8 à 3326499e, 34 commits au-dessus de 192a429e ; 134 fichiers neufs.
- Sorties du manifeste de la course (manifeste-course-iib-v5.json) : 59 listées, 59 présentes, empreinte égale au manifeste et au compagnon ; plus le manifeste lui-même, le résumé et le manifeste du run : 62 fichiers vérifiés par `controle_ia.scellement verifier`, 62 OK. Traces de l'instance : 9 fichiers vérifiés sur 9 par leur liste d'empreintes. Aucun écart.

## Réserves
- Surveillance interrompue de 11:48Z à 18:20Z : la tâche de fond relancée à 09:48Z a atteint sa limite de 2 h et le relevé programmé à 10:18Z n'a été remis à la session qu'à 18:16Z. La course a fini seule, par sa fin normale, et la minuterie de l'amorce a arrêté la machine ; la garde de dépense n'a pas été lue pendant cet intervalle (dépense comptée a posteriori, ci-dessus).
- Activité interne non enregistrée par cette course (additif, ligne 182 ; code 192a429e), contrairement à la lettre de GO-2026-11-10-08 : porté à la mère le 23 à 08:50Z.
- Liste des intouchables de la destruction élargie à 62096662 (b5f-lecture-v1, autre chantier, vue à l'inventaire), en plus des quatre de la passation.

# Mandat — rédacteur Fable : brouillon 6 de l'additif et du devis de la voie (A) — v1

Pièce de travail (classe C), exécutante neuve, 2026-11-22 vers 18:50Z. Effort : high (GO-2026-11-22-114 ; deux ajouts décidés, rédaction courte). Interdits des mandats précédents en vigueur.

Base : ton brouillon 5 (commit 88a82af3), vérifié « scellable une fois les champs remplis » (`contre-lecture-voie-A-v1/note-verification-brouillon5-voie-A-cl2.md`, 5a09da27…). Brouillon 6 = brouillon 5 avec ces seuls ajouts (décisions de la mère, 18:42Z, étage 2, GO-2026-11-22-106) :
1. **Borne horaire du code 7** (règle la plus étroite de la vérification) :
   - le nœud porte l'instant « arrêt plus 33 heures », calculé par le programme (59,71 USD) ;
   - à l'arrêt plus 24 heures sans mot de Lazar, la mère relance Lazar : destruction ou relèvement de la ligne ;
   - la mère tient ce nœud une fois échue la ligne de session de l'exécutante ;
   - le silence de Lazar ne vaut jamais accord de destruction ;
   - à l'arrêt plus 36 heures, le passage du plafond est déclaré comme dépense hors devis ;
   - la mère prévient Lazar de ce cas dès maintenant.
   Ajoute la ligne du programme si elle manque (calcul v6 et sa sortie, les autres lignes égales à l'octet).
2. **Geste du troisième rempart** (§ 7, point 12, tranché) :
   - aucun geste avant l'échéance plus 80 minutes ;
   - ensuite, arrêt par l'identifiant, jamais de destruction, mêmes codes 5 et 7, message à la mère et à Lazar ;
   - la réserve de 64,76 USD tombe ainsi au chemin de 57,07 USD si la session de l'exécutante meurt. Écris-le.
3. Retire du § 7 les points tranchés. Les trois champs restent : entropie, empreinte de la configuration, commit de lancement.

Rendu : même worktree, même dossier : `additif-ordre-course-voie-A-v1-brouillon6.md`, `devis-voie-A-v1-brouillon6.md`, `differences-voie-A-brouillon5-vers-6-v1.md`, programmes s'ils changent ; compagnons `.sha256` ; un commit local. Réponds en 6 lignes.

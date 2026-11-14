# Consigne — corrections du lanceur de l'organisme sur les bassins étroits (lanceur v2) — v1

Écrite par la session mère le 13 novembre 2026 à 13:57 UTC (`date -u`), pour le préparateur (Claude Opus 5.5), repris avec son
contexte. **Tous les interdits de ta consigne d'origine (`d404b6eb…`) restent en vigueur** : aucune dépense, aucun appel de modèle,
aucun réseau, aucune opération git, ni `.claude/settings.json` ni `.claude/hooks/`, noms neufs (R12), scellé à chaque pièce finie.

## 1. Pièce qui commande
`docs/notes/organisme-bassins-etroits-v1/contre-lecture-lanceur-bassins-etroits-v1.md` (`3aaf9981…`) et ses outils (`docs/notes/organisme-bassins-etroits-v1/contre-lecture-outils-v1/`) : lanceur v1
**« non autorisable »** (1 bloquant, 9 majeurs, 12 mineurs) ; conception, question, témoins, devis « autorisables après corrections ».
Fait neuf : le bac à sable est **actif** dans ce conteneur depuis 13:30Z (`bubblewrap` et `socat` installés par la mère ; sonde de
l'orchestrateur : actif et proc_neuf vrais ; R-2536).

## 2. Décisions de la mère (R-2537)
- **B1** : corrige (le compagnon de la liste blanche écrit par l'orchestrateur est vérifié, pas recréé) ; ajoute un essai dont le
  faux orchestrateur écrit ce compagnon, et **un essai sans appel contre l'orchestrateur réel** comme celui du contre-lecteur.
- **M1, M2, M3** : toute dépense illisible ou tout dossier de tentative sans relevé compte **son plafond entier** ; aucun chemin
  ne rend 0 par défaut ; « pas de relance après dépense » vaut aussi pour le bras ; un refus sans envoi (coût plancher) ne
  verrouille pas la génération s'il est prouvé sans dépense par le relevé ; marge du contrôle externe d'Argon relevée pour tenir
  3 caractères par jeton, dans le plafond de 20 USD par génération et la borne de 60.
- **M4** : la règle de passage ne s'appuie sur **aucune** mesure que l'orchestrateur dit « jamais pour une sélection » ; doublons
  écartés sur le seul signalement explicite d'un juge ; aucun repli silencieux (erreur = arrêt, code et motif) ; une fiche de passe 2
  n'est jamais sautée pour le seul fait d'être appariée à une fiche de passe 1 déjà prise sans signalement de doublon.
- **M5** : la génération 1 ne dépend pas de la lecture d'N-053 ; le lanceur **refuse les générations 2 et 3** tant qu'un fichier
  scellé `docs/notes/organisme-bassins-etroits-v1/attestations/confirmation-regle-de-passage-v1.md` (mot de Lazar recopié par la mère) n'existe pas.
- **M6** : la lecture entre la course et le bras est faite par **la mère** (Lazar peut s'y substituer) ; l'attestation dit qui a lu,
  quoi (empreintes), quand ; écris-le dans la conception v2.
- **M7** : la course ne doit pas dépendre de la durée de vie d'une commande : le lanceur lance l'orchestrateur **détaché**
  (session de processus neuve, sorties vers des fichiers, PID écrit au manifeste de départ scellé) et rend la main ; la **même
  commande exacte**, relancée, lit l'état du disque : course en marche (PID vivant) → rien, compte rendu ; course finie → manifeste
  de fin, sceaux ; processus mort sans fin propre → dépense comptée à son plafond, génération verrouillée. Aucune seconde course
  ne peut partir tant qu'un PID vit. Arrêt par PID seulement (R10). Essais : cas sain et artefacts.
- **M8** : le recoupement est exigé avec son compagnon **et** une attestation scellée de relecture par la mère
  (`docs/notes/organisme-bassins-etroits-v1/attestations/attestation-relecture-recoupement-v1.json`, empreinte du recoupement dedans) ; son empreinte entre au manifeste.
- **M9** : récris le témoin « vrai » pour qu'il ne puisse pas être jugé « occupé » à bon droit par ce que les proposeurs reçoivent
  (dis la règle) ; la limite « témoins écrits par un modèle de la lignée d'un proposeur et d'un juge » est écrite au devis et à la
  conception comme réserve.
- **Mineurs** : corrige ou refuse avec raison ; les six mutations survivantes du contre-lecteur doivent mourir.
- **Règle de permission** : propose-la pour la version 2 — une règle par commande exacte (trois commandes : générations 1, 2, 3),
  et l'épingle d'empreinte du fichier v2 ; dis-le tel quel, la mère l'écrira et le dira à Lazar.

## 3. Livrables (noms neufs)
`scripts/lancer_course_ideation_bassins_etroits_v2.py` et `tests/test_lancer_course_ideation_bassins_etroits_v2.py` ;
`docs/notes/organisme-bassins-etroits-v1/conception-trois-generations-v2.md`, `temoins-bassins-etroits-v2.json`, `devis-organisme-bassins-etroits-v2.md`,
`rapport-preparateur-v2.md` avec un **tableau constat par constat** (corrigé : où, essai qui le prouve ; ou refusé : raison) et le
différentiel v1 → v2 prêt pour une vérification courte. Rapport final court à la mère.

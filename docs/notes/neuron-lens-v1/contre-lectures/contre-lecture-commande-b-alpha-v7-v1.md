# Contre-lecture neuve (R2) — seconde lecture : commande v7, addendum v2, devis v2, lanceur v5, amorce v7, essai à blanc v11 — v1

Contre-lecteur neuf (a déjà lu la v6, n'a rien écrit des pièces). Dépôt `/home/user/controle-ia-travail`, branche `prep/neuron-lens-v1`,
commit `63813af5`. Rien loué, aucune commande `vastai`, aucun code du dépôt voisin exécuté, aucune variable d'environnement affichée,
aucun fichier existant modifié, rien commité. Ce fichier est le seul ajout (plus des essais jetables dans le dossier de travail de la session).

## Verdict

**À CORRIGER, légèrement** : aucun bloquant ; un seul point de fond (M1 : l'audit de B-7 « par le haut » est maintenant joué, mais ce qui
le fait « tenir » n'est pas fixé avant la course) ; le reste est mineur. Les points B1 (code), B2, M1 à M5 de la lecture précédente sont
réellement corrigés. Si la mère accepte de laisser la lecture de B-7 « par le haut » à la décision de Lazar après résultat (ce que dit déjà
l'addendum v2, « proposée, non tranchée »), la v7 peut partir telle quelle ; sinon une phrase d'addendum v3 (donc commande v8, dépôt réduit et
essai à blanc à refaire).

## Vérifié et exact

- **Empreintes** : les 22 lignes du tableau final de la commande v7 sont égales aux fichiers ; compagnons de la commande, de l'addendum v2 et du devis
  v2 : `scellement verifier` OK. Journal v11 : `a0ad98d3…` = compagnon.
- **Dépôt réduit v8** rejoué sur `63813af5…` : 351 fichiers, liste `c22cafc63b03…` = attendue (commit réduit différent, normal). Le diff
  `af7a7117 → 63813af5` n'ajoute que commande, devis et journal, hors liste : « pièces de course identiques à `af7a7117` » exact. La référence
  publiée lue par les nouveaux essais (`…/reference-publiee/` (résumé publié du modèle de référence)) est dans la liste.
- **Essais** : 77 essais du lanceur v5 passent, sans « skipped » ; l'ensemble de l'amorce : **168** passés (chiffre de la commande exact).
- **Chiffres recalculés** : 0,06 + 0,71 + 0,1 + 1,05 + 0,1 = 2,02 (« ≈ 2,1 large ») ✓ ; plafond 8,5 : 2,1 + 0,6 × 8,5 = 7,2 = 60 % de 12 ✓, 2,1 + 0,9 × 8,5
  = 9,75 < 10,8 ✓ ; scénario avec audits : 2,7 à 3,0 h + 2 × 0,5 h = 3,7 à 4,0 h ✓, attendu codé 4,81 + 1,3 + 0,8 = 6,91 ≈ 6,9 h ✓, + 0,7 USD mesurés
  (1 h × ≈ 0,7) ✓, + 1,5 USD codés (2,1 h × 0,7) ✓ ; ligne attendue 3,9 à 5,1 (2,1 + 3,0) ✓ ; minuterie 10,5 h / 12,3 h inchangée ✓ ; seuil 0,01 de l'addendum
  = un dixième de l'écart 0,40 contre 0,30 de B-2 ✓.
- **Points de la lecture précédente** :
  B1 (code) : `_verdicts` retient la chaîne « B-7 … par le haut », requiert `audit-trop-beau` de la même série (une seule fois si « trop beau » l'exige
  aussi), verse `motifs_audit` et `audit_b7_par_le_haut` (essai avec le vrai code des verdicts, B-7 forcé à 0,50 aux couches 8-15 ✓).
  B2 : garde de carte essayée (cas sain, trois artefacts vus par `nvidia-smi`, nom différent vu par `torch`, nom illisible, `nvidia-smi` absent), dans l'essai v11 ✓.
  M1 : ligne ajoutée à la liste d'arrêt de l'addendum ✓. M2 : addendum § 3 dit « remplace », « aucun verdict de B-7 » si chaîne en défaut ou
  seconde série non jouée, « autre » couche par couche ✓. M3 : vrai `_verdicts` aux deux séries, `essais_ok` faux → « chaîne en défaut », gardes de
  fichier absent (bascule et grandeurs), ordre des audits par série (3 cas) ✓ (reste mineure 8). M4 : devis chiffre le scénario des audits, pèse l'ordre
  des séries, rappels 4,8 / 6,9 / 9,0 h ✓. M5 : voir plus bas ✓. Mineures 1 à 7, 9 à 11, 13 à 15 : corrigées (la 8 et la 12 : voir ci-dessous).

## Examen des changements demandés

- **Règle « B-7 par le haut → audit trop beau de la série »** : mécanique correcte (la v4 perdait le motif). Deux réserves : M1 (critère) et
  mineures 1 et 2 (devis et addendum disent encore que le déclencheur lit le pilotage seul).
- **Refus des motifs inconnus** (`_verdicts`, l. 834-836 de la v5) : fermé (échec, pas de repli), essayé (artefact par substitution du verdict).
  Les trois seuls motifs du code des verdicts sont connus, donc sans effet en marche normale. Réserve : l'arrêt à `verdicts` du lot 16 ferait perdre
  la seconde série pour un motif qui n'est qu'informatif (mineure 3).
- **Bascule idempotente** (l. 862-891) : empreinte de la graine 0 comparée à celle de `measure` **avant** le renommage (essai : rien n'est déplacé
  si elle diffère) ; reprise d'un arrêt entre les deux renommages OK (essai) ; rejouable entière (essai) ; fichier « déjà mis de côté » d'une autre
  empreinte refusé. Aucun cas d'écrasure trouvé : source présente avec cible présente reste un arrêt.
- **Reprise de `measure-lot64`** (l. 893-903) : un fichier de mesure présent, différent de celui du lot 16 et avec le fichier du lot 16 déjà mis de côté,
  est supprimé puis la mesure est rejouée ; un fichier égal à celui du lot 16, ou sans fichier mis de côté, reste un arrêt (« bascule non faite »). Essayé
  (`partiel`, `refuse_le_fichier_du_lot16`). Réserve de coût, pas d'erreur : un fichier du lot 64 **complet** laissé par un arrêt juste avant l'écriture du
  résultat est lui aussi jeté (≈ 0,5 h, ≈ 0,3 USD) ; le résultat porte `fichier_partiel_retire_sha256`, donc c'est tracé. Cas pathologique sans effet pratique : si le
  fichier du lot 64 avait exactement l'empreinte de celui du lot 16, la reprise s'arrêterait (non atteint en pratique).
- **`nvidia-smi` avant `pip`** (amorce v7 l. 226-240) : correct. `command -v` puis lecture de la première ligne ; vide ou échec → code 11 ; autre nom → code 11 avant
  l'installation (l'essai vérifie que « installation de l'environnement » n'est pas journalisée) ; absent → journalisé puis contrôle par `torch` (repli **journalisé**,
  non silencieux). Le contrôle par `torch` après `pip` reste. Non joué en vrai (aucune carte) : déclaré.

## Bloquantes

Aucune.

## Majeures

**M1 — Ce qui fait « tenir » l'audit de B-7 « par le haut » n'est pas fixé (R1).**
- Addendum v2 § 4 (l. 61-67) : l'audit est joué (procédure « trop beau » : témoin bien apparié, pilotage de norme non nulle, `measure` à la graine 1), puis « la
  lecture de B-7 par le haut est **proposée** au lecteur neuf, non tranchée, et portée à la mère ». Le texte gelé dit « s'il tient, rapporté comme lecture
  valable en contexte plus tôt que publié » sans définir « tenir ». Les deux vérifications que fait `_audit_trop_beau` (`temoin_bien_apparie`,
  `pilotage_norme_non_nulle`) ne portent pas sur l'ablation, et aucun verdict de B-7 à la graine 1 n'est demandé ni comparé.
- Conséquence : si le lot 64 donne « par le haut », le critère de « tenue » sera choisi après les chiffres.
- À écrire (une phrase, avant le feu) : par exemple « l'audit tient si (i) `temoin_bien_apparie` et `pilotage_norme_non_nulle` sont vrais **et** (ii) le verdict de B-7 calculé sur
  la graine 1, même lot, est aussi “non reproduit par le haut” ; sinon la lecture est “ne tient pas”, rapportée telle quelle ». (Le verdict de la graine 1 se calcule à
  partir du résumé et des grandeurs de l'audit déjà versés ; ni code ni location en plus.) Ou bien déclarer en toutes lettres que le critère est laissé à Lazar après résultat.

## Mineures

1. **Devis v2, tableau des durées (ligne « avec les deux audits »)** : « le déclencheur lit le pilotage, même calcul aux deux séries : requis à l'un, il l'est en
   principe à l'autre ». Faux pour le motif ajouté par le lanceur v5 : B-7 « par le haut » lit l'ablation, qui diffère entre lot 16 et lot 64 ; un seul audit
   (ou aucun) est possible. Dire « un ou deux audits » ; le scénario chiffré (deux) reste le pire cas.
2. **Addendum v2 § 4 (l. 68-70)** : même phrase (« son déclencheur lit le pilotage, le même calcul aux deux séries ») à compléter par le motif de B-7.
3. **Lanceur v5, l. 834-836** : l'arrêt sur un motif inconnu à `verdicts` du lot 16 empêche la seconde série. Disproportionné pour un motif informatif ; préférer
   verser `motifs_audit_inconnus` et continuer, le lecteur les voyant. À défaut, le dire (déjà « fermé » volontairement).
4. **Addendum v2 § 6 (l. 86-90)** : « fichiers bruts … ≈ 2,6 Go chacun » : non sourcé et inexact. Calcul sur la forme de la mesure (1 024 pôles × 2 × 2 doses ×
   128 256 × 2 octets + deux tables d'ablation) : ≈ 2,1 Go ; la note de mémoire donne « ≈ 2 GiB ». Écrire « ≈ 2 Go (au-delà de la limite de fichier) » (R7).
5. **Rappels (commande v7 étape 11, devis § 4)** : le rappel (c) à 80 % de D tombe à ≈ 8,4 h au prix 0,73 (9,9 h à 0,62), donc **avant** le rappel (b) « la mère
   décide » à 9,0 h au prix haut : ordre peu lisible. Dire que (b) est à min(9,0 h ; 80 % de D) ou régler (b) sur 75 % de D.
6. **Devis v2, coût avec audits** : « ≈ 2,5 à 3,0 USD » ; 3,7 h × 0,62 + 0,1 = 2,4 ; la borne basse est 2,4. Négligeable ; harmoniser avec la commande (« 2,5 »).
7. **GO inscrit** : la commande v7 (différentiel) dit GO-2026-11-17-04 « inscrit par la mère sur `main` (`registres/go.md`, l. 360-361) ». Je n'ai pas pu le
   vérifier : le `main` local (`fbbe31aa`, 290 lignes) ne porte pas cette ligne, et la branche de travail non plus. À citer au feu avec le commit de `main` qui l'inscrit.
8. **Essais du lanceur v5 : reste de M3** : toujours aucun essai des vraies `_score`, `_grandeurs` (voie nominale), `_audit_trop_beau`, `etape_score_lot64`,
   `etape_grandeurs_lot64` : les noms de sortie distincts des deux séries sont vrais par lecture (relue) mais non affirmés par un essai. Un essai avec exécuteur
   factice qui écrit les deux résumés et vérifie les noms et l'absence d'écrasure suffit.
9. **Essai à blanc v11** : les audits ne passent toujours pas par le vrai lanceur (faux lanceur sans audit) ; le journal le dit (« comme en v10 ») : accepté.
10. **Marges déclarées, rappel** : mémoire de pointe au lot 64 (estimée), chaîne jamais jouée sur A100, noms de carte attendus et non lus : tous déclarés, sans changement.

## Réponses synthétiques

- Chaque point de la lecture précédente est **réellement corrigé** (B1, B2, M1 à M5) ; mineures 1 à 7, 9 à 11, 13 à 16 aussi ; la 8 (« 39 936 ou 40 960 Mio ») l'est ;
  la 12 (GO) reste à citer (mineure 7 ci-dessus).
- Défauts nouveaux : M1 (critère de « tenue » absent), mineures 1 à 5 ; rien de bloquant dans la bascule, la reprise de `measure-lot64`, le refus des motifs
  inconnus ou le contrôle de carte.

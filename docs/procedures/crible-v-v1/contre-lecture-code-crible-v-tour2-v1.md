# Contre-lecture du code du crible (v), tour 2 (différentiel) — v1

- **Contre-lecteur** : sous-agent neuf, modèle C ; il n'a écrit ni la v1 du lanceur, ni le rapport du tour 1, ni la v2 (code écrit par le
  modèle A ; corrections par un rédacteur neuf du modèle A, par programme de couples).
- **Pièce lue** : `lanceur_crible_v_v2.py`, empreinte `88afd6e109b2c45c2e48c928badef856b6f81400d0f18cf5dca4fd2fa73a1801` (égale à son
  compagnon). Référence : `lanceur_crible_v_v1.py`, `2636bcb1deefc0a7dc1427bb476b7c0e2efdc1b5ae6d9e76c3a7c2ac592d7725` (égale à son
  compagnon) ; rapport du tour 1 d'empreinte `05809ac2…9675` (égale à celle donnée).
- **Heures** (`date -u`) : lecture et rejeux du 2026-11-17 de 02:40 à 02:49 UTC ; rédaction à 02:49 UTC.
- **Non ouverts** : l'issue du pilote MR-2 v14, toute branche `calcul/pilote-mr2-v74-entree-*`, rien sous `diag/`, `runs/`, `donnees/`, rien
  de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque. Aucune machine, aucun appel, aucune clé employée, aucune dépense, aucun commit,
  aucune pièce du dossier modifiée.

## 0. Verdict : **scellable**

La v2 applique fidèlement les cinq couples du rapport du tour 1 qui portent sur le lanceur (M2, M3 en deux couples, m1, m4) et rien
d'autre que les changements de nom annoncés ; les deux défauts de comportement (arrêt entre files, ordre des quatre appels) sont
corrigés et je l'ai rejoué ; essais, essai à blanc, mesure et banc passent contre elle. Aucune correction n'est exigée de cette pièce.
Les prédictions gelées (R-2993) ne changent pas.

## 1. Différentiel (`diff` v1 → v2, 70 lignes changées)

| bloc du `diff` | contenu | conforme à |
|---|---|---|
| en-tête (lignes 1 à 4) et section « Contre-lecture » (+41 lignes) | version, heure de scellement, réponse point par point | annoncé par la section elle-même |
| `VERSION` | `lanceur-crible-v-v1` → `lanceur-crible-v-v2` | nom neuf (R12), annoncé |
| `FICHIERS_DU_CRIBLE` | `lanceur_crible_v_v1.py` → `lanceur_crible_v_v2.py` | nom neuf, annoncé (le code attesté est celui qui tourne) |
| `CHAMPS_A_BLANC` | `+ "configuration"` | m4, identique au couple du rapport |
| `dollars_depuis_les_journaux`, branche finale | `0.0` → `float(a.get("cout_usd") or 0.0)` | m1, identique ; `a` est défini dans la branche |
| `file()` d'un monde | `erreurs, rendus = [], {}` ; résultats recueillis ; traitement sous le verrou des répondus d'abord (`sorted`, stable) | M3, deux couples identiques |
| lancement des files | `file_gardee` qui pose `E.arret` sous le verrou puis relève | M2, identique |

Rien d'autre : je n'ai trouvé aucune ligne hors de ce tableau. Le programme de couples
`corriger_lanceur_crible_v_v1_vers_v2_tour1_v1.py` (scellé, compagnon à jour) porte les mêmes blocs que le rapport (relus à l'œil contre
les blocs de ses § 2 et 3). Les deux textes visés par les mutations M29 et M30 proposées au rapport sont présents une seule fois chacun
(grep : 1 et 1). La v2 se compile. M1 (outil de la session) et M4 (essais, banc) du rapport, m2 et m3 sont, comme la section le dit,
hors de ce fichier.

## 2. Passages touchés relus

- **M2** : l'exception sort de `file`, `E.arret` est posé sous `E.verrou` si vide (jamais écrasé : l'arrêt d'abandon de fournisseur reste
  prioritaire), puis l'exception est relevée, de sorte que la boucle des `fu.result()` et les `except` suivants se comportent comme en v1
  (le refus avant tout appel garde `if not E.appels`). L'autre file lit `E.arret` avant son monde suivant (ligne 813). Rejoué par moi :
  M = 2, corps du monde 2 altéré : code 3, **mondes dont des appels sont partis : [1]** (v1 : tous ceux de l'autre file).
- **M3** : l'ordre de traitement ne dépend plus des noms ; rejoué par moi à M = 1, panne au monde 1 de `fable52` puis de `opus55` :
  les deux donnent code 0, arrêt nul, 41 complets, 39 échecs (v1 : arrêt dans un cas seulement).
- **m1** : plus de zéro silencieux pour un appel lancé non coupé sans ligne de journal ; la source écrite reste « journal_relais »
  (dite par la section).
- **m4** : `--configuration` est refusée en mode réel avec les autres options d'essai ; la configuration lue par la mesure
  (`--configuration` de la sous-commande de mesure, ligne 1061) est un autre chemin, non touché ; la machine ne la passe jamais.
- **Effets de bord possibles de M2** : `E.arret_classe = "arret"` est posé plus tôt qu'avant ; il ne sert qu'au choix du nom des cartes
  (ligne 911) et au manifeste, et l'abandon de fournisseur (classe distincte) reste posé avant, sous `if not E.arret`. Aucun écart.

## 3. Rejeux (contre la v2, sur une copie de travail du dossier hors du dépôt, où seuls les noms du lanceur v1 → v2 sont substitués dans
les essais et le banc ; arbre à la tête 605e0f6 ; mondes d'essai publics ; relais factices ; ports décalés)

| contrôle | résultat |
|---|---|
| essais unitaires | **40 essais, 0 échec** |
| essai à blanc et scénarios (`jouer`) | **9 essais, 0 échec** (M = 1 : 80 appels, coupure à 20 s ; M = 2 ; pannes ; coût ; corps ; témoin ; garde ; mode réel refusé) |
| reproductibilité | `CARTES.json` `5dbe2f6d…` et `DOLLARS.json` `5bf1a69e…` **égaux** aux pièces gardées du dossier |
| mesure | **5 essais, 0 échec** |
| banc de mutations | **52 tuées sur 52, 3 témoins conformes**, aucune survivante |
| scénarios M2 et M3 (mes propres, § 2) | conformes à la correction |

Les empreintes de toutes les pièces du dossier sont `OK` ; les sorties gardées du dossier sont celles de la v1 (voir § 5, point 1).

## 4. Corrections exigées : aucune

Remarques facultatives (aucune n'exige de correction de cette pièce) :
- **g1.** Ni les essais ni le banc ne jouent encore M2 et M3 : une mutation « `file_gardee` retirée » ou « répondus d'abord retirés » survit au
  banc v1 (le banc ne contient aucun de ces textes). Le rapport du tour 1 demandait l'essai `j_arret_file_m2`, l'essai sain « panne de
  Pr-4, Pr-2 répond » et les deux mutations ; ils appartiennent aux versions neuves des essais et du banc (§ 5).
- **g2.** La section « Contre-lecture » dit « sorties et empreintes rendues à la mère, hors de ce fichier » : cohérent ; mes rejeux le confirment
  mais n'en tiennent pas lieu (R12, pièces neuves).

## 5. Points pour la mère

1. **La v2 n'est pas encore le code qui tournerait.** Machine, outil de la session, essais, banc, répétition, gabarits, procédure et rapport nomment
   encore `lanceur_crible_v_v1.py` ; l'addendum d'empreintes et l'outil de la session attesteraient la v1 tant que leurs versions neuves
   ne nomment pas la v2. À faire en versions neuves : M1 (outil de la session : plafond « 104.39 USD (sur crédits) » refusé, avec cas sain
   et artefact en répétition) ; M4 (essai des dollars des journaux et de la dépense d'un coupé + mutations M29 et M30) ; essai et mutations de
   M2 et de M3 (g1) ; m2 (portes du mode réel) ; m3 (cadence « toutes les 30 secondes » de la minuterie) ; rapport § 1 refait ; essais,
   banc et répétition **joués contre la v2 sous ses noms propres**, sorties scellées.
2. Un tour différentiel sera à prévoir sur les pièces neuves (session, essais, banc, procédure) : cette contre-lecture ne couvre que le lanceur.
3. Inchangés depuis le tour 1, hors lanceur : D non relevée (budget « non lançable ») ; garde de départ lue à la lettre qui peut refuser après la
   sonde payante si D dépasse environ 9 à 10 ks ; relevé de sonde sans cas sain hors appel réel (écart déclaré) ; coupure à B_a comptée au plafond ;
   archive fictive en trois lectures ; partie A non jouée ; mot de Lazar sur les clés et le jeton, présence et phrase ; enveloppe 204,67 USD (ce
   crible), au-dessus de 1 275 USD pour les cinq cribles.
4. Poste : disque presque plein (1,4 Go libres) ; mes copies de travail sont à détruire (voir § 6).
5. Réponse à la question « les lancer avant le 21 ? » : du côté du lanceur, rien n'attend le 21 novembre ; le goulot reste les pièces et mots du point 1 et 3.

## 6. Incidents de ma main

- Premier essai de clonage de l'arbre depuis le paquet d'un autre dossier du scratchpad : paquet incomplet, refus net ; j'ai alors copié l'arbre
  (tête 605e0f6) et les mondes d'essai publics déjà présents dans le dossier de travail d'une contre-lecture précédente (lecture seule de ces
  entrées, aucun monde ni secret du crible). Aucun autre accès aux dossiers des autres tâches.
- Aucun commit, aucune pièce du dépôt modifiée ; mes copies de travail sont dans mon dossier du scratchpad et détruites à la fin.

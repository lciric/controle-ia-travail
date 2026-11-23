# Passation — relance du bras A des organismes discrets — 2026-11-23 06:20Z

Session de relance du bras A (Claude Opus 5.5), sous la session mère `session_013QMayjbmQUdDuDs2S3i3XD`, autonomie de nuit (GO-2026-11-22-147, -150 ; chaîne de décision). Branche de travail `claude/pensive-bardeen-1fv7hw`. Passation scellée ; ne pas réécrire.

## Fait

1. **Texte v2 du bras A scellé.** Brouillon 56 (`561723f1…`) : 13.1 cite le programme de l'aire conditionnelle (`aire_conditionnelle_bras_a_v1.py`, `0f1e7640…`), la garde statique du cloisonnement v14 (`44e84972…`, preuve de différence par programme) et l'enchaînement de la lecture de la discrétion v3 (`05126df3…`). Il a été contre-lu « scellable » (`6300ff2c…`). Le geste du scellement v3 (`6a025b39…`) a tiré l'entier racine une fois, le 2026-11-23 à 00:03:32Z ; note `docs/notes/relance-organismes-discrets-v1/scellement-bras-a-v2/note-du-scellement-v1.md` (`a936715c…`). La mère a scellé le texte `prereg/T0.7-organismes-discrets-v-a-v2.md`, `b4fbfb4e6cddfdc4775119a3e42a61045460ce8cee18a341834155ef1367a0cd` (R-5095), copié sur la branche.
2. **Lanceur de la course** : v4, puis v5 à v8. Chaque version a été contre-lue ; en v8 s'ajoute le guide « H1-classification », tranché par la chaîne de décision. Lanceur v8 : `lanceur_bras_a_v8.py`, `2663d32d…`. Configuration CONFIG-BRAS-A-V2 : `prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json`, `2a17e067…`, inscrite par la mère (R-5102). Plan des tâches v2 `7cc3d4a4…`.
3. **Ligne 1 de carte, jouée** sous GO-2026-11-22-148.
   - Deux pannes techniques d'abord :
     - instance 62082700 : injoignable, faute de SSH depuis le conteneur, détruite à 02:52:20Z ;
     - instance 62094921 : venv impossible sur l'image ; échec versé sur `calcul/bras-a-ligne-1-v1`, puis destruction par la machine.
   - Ensuite une **machine autonome**, sans SSH :
     - branche d'entrée orpheline `entree/bras-a-ligne-1-v2` (`a162ad0d…`), liste blanche seule ;
     - amorce d'appel v3, amorce complète v4 `7f155ab6…` ;
     - lanceur machine v5 ; création depuis la session mère.
   - Instance 62097676 : 128 épisodes, code 0, 104 actions coupées sur 1 280 ; compteur 2,63 USD.
   - Versement poussé sur `calcul/bras-a-ligne-1-v2` (`43dcdad3`), prouvé, puis destruction par la machine. Rapatrié dans `diag/organismes-discrets-v-a-v2/ligne-1-fini-20261123T061257Z/` : manifeste `cf3632d1…`, 29 pièces aux empreintes égales.
   - Les épisodes ne sont pas ouverts.
4. **Contre-lectures et décisions consignées par la mère** : R-5095 à R-5115. Réserves acceptées au premier étage : voir les notes de contre-lecture sous `docs/notes/relance-organismes-discrets-v1/` et `…/etape-a-ligne-1-v1/`.

## Reste

- **Ligne 2** (distillation des six adaptateurs, rejeu honnête à la seconde ligne, étape (c)) :
  - complément du devis d'une page ;
  - programme de l'instance de la ligne 2, sur le même motif de machine autonome, avec le même guide vérifié aux mêmes empreintes (séquence v2, section 10) ;
  - contre-lecture, ligne d'engagement, signal de la mère.
- **Enchaînement de la lecture de la discrétion v4** : mode « étape (m) seule » (MA-2, décision de la mère : (c), repli (b)). L'entrée sera contre-lue avant le premier lancement (MA-1), et l'épreuve de forme couvrira les livraisons refaites avant l'étape de discrétion (MA-3).
- **Garde au chargement du lanceur de discrétion** (réserve de la configuration v2 habilitée) avant l'étape (m).
- **Six mineurs de la contre-lecture Opus de l'enchaînement v3**, à porter au manifeste.

## Réserves

- Le stockage du constat a été arrondi (0,0722 au lieu de 0,07222) pour l'instance 62082700 : écart de 0,00002 USD/h, déclaré.
- Le filtre `masquer` du lanceur machine v3 a laissé paraître `instance_api_key` chez la mère : corrigé en v4/v5 ; la clé est morte avec l'instance.
- Incident de cloisonnement déjà rapporté : un agent de développement avait copié par `cp -r` 133 chemins cloisonnés, retirés sans être ouverts. Depuis, les copies se font par liste blanche seulement.
- Les essais « dépôt » des anciennes gardes v6 à v13 sont en échec, comme attendu depuis la garde v14.
- `verifier-arbre` signale des écarts anciens sous `runs/` (zone cloisonnée), non traités.

## Prochaine action

Attendre le signal de la mère pour la ligne 2 ; écrire le complément de devis et le programme de la ligne 2 (machine autonome), sous contre-lecture.

## Instances actives

Aucune pour le bras A : 62082700, 62094921 et 62097676 sont détruites (relecture des instances à 06:13Z). Les instances des autres courses (saboteur, T0.8, barreau 5) relèvent de la mère.

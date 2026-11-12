# Témoin de Bailey — lancement v2 interrompu, instance 60280913 détruite — 12 novembre 2026, 00:20 UTC

Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST` (autre compte), branche `claude/compassionate-meitner-d4ryyk`.
Suit l'ordre de lancement `2026-11-12-0005-ordre-lancement-temoin-bailey.md` (`6ba6f01c…`). Ne se réécrit pas (R12).

## Verdict
**Pas de run, pas de verdict.** L'instance a été créée, puis détruite sans qu'aucune amorce ne soit jouée. Rien n'a été
installé ni calculé, et aucune note n'existe. Dépense comptée : ≈ 0,31 USD (D du poste).

## Déroulé
1. **Lancement v1** (`lancer-conduite-v1.py`, 00:01:20Z) : échec à la création, `FileNotFoundError: vastai` (interpréteur
   du `.venv` appelé sans activer l'environnement : `vastai` hors du `PATH`). La conduite a noté une « création
   incertaine » (étiquette `temoin-bailey-c6-eee230a55ee44942`). Inventaire R10 manuel : aucune instance sous cette
   étiquette. Aucune dépense. Sortie v1 gardée telle quelle.
2. **Lancement v2** (`lancer-conduite-v2.py`, `54aa1aab…`, sortie et bilan neufs, refus sans `vastai`, `ssh` ou `scp`
   dans le `PATH`, refus éprouvé) : PID 6007, ≈ 00:03 UTC. Instance **60280913** créée à 00:03:20Z ; taux relevé
   c = 1,6404 USD/h ; ordre écrit dans `conduite-v5.jsonl`. Le processus de conduite s'est ensuite terminé, sans
   `bilan-lancement-v2.json` et sans erreur dans `lancement-v2.err`. **Cause non établie.**
3. **Refus d'un classifieur de sûreté** : ma réponse qui lisait ces sorties a été coupée par un classifieur de sûreté.
   Consigné ; arrêt de l'écriture sur ce point ; ni reformulation, ni renvoi à une autre session (liste d'arrêt du
   préenregistrement).
4. **Destruction** sur le mot de Lazar (« Option (a), je la détruis par son identifiant (R10) ») : `vastai destroy
   instance 60280913 -y` à 00:14:43Z, « destroying instance 60280913. » ; absente de l'inventaire relu à 00:15:05Z.
   Veilleur de secours (PID 6020) : déjà absent à la vérification ; aucun processus de la conduite vivant.
   `poste-v5.json` laissé tel quel (R12) : la destruction est datée ici et dans `registres/arrets.md`.

## Dépense
Instance 60280913 : 683 s à 1,6404 USD/h, soit ≈ 0,31 USD (`registres/depenses.md`), dans D du poste sous
`GO-2026-11-10-10`. **B reste 75 USD** (fixé à la création de cette première instance du poste) ; toute relance compte
cette instance dans `instances_anterieures` (id, c, création 1794441800.044329, destruction 1794442483, B = 75).

## Restes
- Clé `ssh` de session 1864483 : gardée sur le compte Vast pour une relance ; à retirer en fin de run.
- Instance 60218139 (`t06-v2`, T0.6) : non touchée, à signaler à la mère.
- Relance : sur le mot de Lazar seulement.

## Instances actives créées par cette session
Aucune.

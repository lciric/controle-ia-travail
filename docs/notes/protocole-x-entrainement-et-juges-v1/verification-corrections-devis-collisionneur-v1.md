# Vérification des corrections du devis du collisionneur (v2) — v1

Même contre-lecteur que la v1 (Opus 5.5). Une seule passe, sans réseau. Pièce : `devis-collisionneur-entrainement-et-juges-v2.md`.

## Verdict : tenues avec remarques

## 1. Constats de la v1
- Les constats 1 à 6 sont portés. Le 1 est en § 0.3, le 2 en § 3, le 3 en § 3 et § 6, le 4 en § 5, le 5 en § 0.1, le 6 en § 0 et § 4.
- Le constat 7 est porté en partie : le calcul du pire absolu, en § 3, garde « 4,12 × 2 » alors que le devis écrit 4,1 ailleurs (exact : 4,11). Le résultat, 43,58, reste juste.
- Le constat 8 est porté. L'empreinte citée du rapport v1, `0cf33fa1…`, est exacte.

## 2. Les trois affirmations neuves
**(a) Tenue.** Après le code 5, une commande identique relance le même dossier sans refus :
- les entrées sont les mêmes (`verser_une_fois`), la ligne a le même montant et le script la même empreinte ;
- `reglage_en_defaut` rend faux pour un essai `INTERROMPU` ;
- les cellules valides sont sautées ;
- chez Google, le plan des trois essais repart en entier.

**(b) Le calcul est juste.** L'essai coupé est compté à son pire cas (`max(pire, usage)`, l. 2400), puis la cellule renvoyée compte de nouveau son pire cas : 15,90 + 2,44 + 1,58 = 19,92 ≤ 21. Deux réserves :
- le pire cas réel est recalculé à l'envoi sur l'entrée comptée. Aux tours III.2 et III.3, cette entrée peut dépasser la borne du devis si un modèle dépasse sa limite de mots. L'écart n'est que de quelques centimes, et la marge de 1,08 USD le couvre ;
- une ligne de 21 USD exige aussi `--plafond-usd 21`, sinon le plafond de 18 refuse le premier. À écrire en § 0.5 et § 3.

**(c) Tenue.** `demande_gemini` (l. 1481) n'envoie que `thinkingLevel`. Neon garde 65 536 − 32 768 = 32 768 jetons de texte. Une seule exception : un niveau refusé par Google (erreur 400) déclenche un repli au budget de 32 768, déclaré au journal. Ce budget est alors envoyé, et pour Carbon il diffère de la provision.

## 3. Ce que la v2 dit de plus que le programme
1. **Important : § 6, « la même commande reprend à la cellule manquante ».** C'est faux dans trois cas :
   - un arrêt « sans pensées » (code 10) ;
   - un `MAX_TOKENS` sans texte après le dernier recours (code 9, l. 2633) ;
   Dans ces deux cas, `reglage_en_defaut` empêche la même commande de renvoyer la cellule. Il faut `--accepter-absence` (le dossier reste incomplet) ou un script au réglage corrigé.
   - un refus (SAFETY ou autre) est définitif dans le run.
   La table ne liste pas non plus les codes 6 (garde de dépense) et 3 (modèle servi différent). Ligne à ajouter au tableau : « Sans pensées (10), MAX_TOKENS sans texte après dernier recours (9), refus : non renvoyée par la même commande ; décision d'absence ou nouveau script ».
2. **Mineur : la ligne « Cellule non valide → code 2 ».** Elle ne vaut que pour une réponse vide ou coupée en fin de relances. Le cas du code 9 relève du constat 1.
3. **Mineur : coupure de Carbon « ce matin ».** Je n'ai pas vérifié cette coupure, faute de lire son journal. La probabilité d'environ une coupure sur trois, elle, est juste : 1 − (7/8)³ = 0,33, sur le taux repris.
4. **Mineur : la note de sortie « relue par moi ».** Une relecture par Fable entame son quota sur une pièce non décisive. La règle d'économie veut une relecture par Opus.
5. **Mineur : la note de lancement scellée à la racine du dossier.** `verifier` ne contrôle que `cellules/`, donc la note ne gêne pas la vérification.

## Fichiers ouverts
- le devis v2 ;
- mon rapport v1 ;
- `collisionneur_v9_v8m.py` (extraits : l. 998-1030, 1176-1192, 1481-1496, 2832-2846, 3275-3295, en-tête de `verifier`).

## Passe finale sur la v3
1. **Remarques : toutes portées exactement.** Le diff touche les § 0.5, § 2, § 3 (deux points), § 5, § 6 (tableau et texte) et § 8. Les deux empreintes citées sont exactes : `3290e4b1…` pour ce rapport avant cet ajout, `4c8bf749…` pour le journal (calculée par programme, sans lecture).
2. **Diff : rien d'autre que les changements annoncés.** En plus, seulement le titre « v3 » et la ligne de chaîne de l'en-tête.
3. **Un seul reste, mineur : le refus du modèle, au § 6, quatrième ligne du tableau.** Le programme ne l'arrête pas sur le coup. La cellule est marquée bloquée, les autres cellules du tour partent, puis la porte se ferme (code 2, l. 2654 et 2890). Le reste de la ligne, « la même commande ne renvoie pas la cellule », est juste.
Verdict : **corrections tenues.**

# Contre-lecture des pièces de reprise v7 (« v6 bis », variante B′ du repli) — relance de la confirmation du témoin de Bailey

- **Objets** : générateur `generer-pieces-reprise-confirmation-bailey-v6.py`, `poste-hetzner-reprise-v7.sh` (`5b3372c4…`),
  `construire-donnees-demarrage-reprise-v7.py` (`3b08c026…`).
- **Contre-lecteur** : sous-agent neuf (R2), lancé le 18 novembre vers 06:28 UTC par la session « attaquant informé ».
  Aucune commande vastai, hcloud ni curl ; rien d'écrit dans le dépôt. Essai de simulation dans le bloc-notes de la
  session : `scratchpad/essai-v7/test_reprise_b_prime.py`, 6 essais, 6 passés.
- Rendu transcrit et mis en forme par la session, sans changement de fond.

## Verdict : scellable après corrections

Les pièces sont scellables telles quelles. Les corrections obligatoires portent sur la procédure de la session (C1 à C3) ;
les corrections dans les pièces sont faibles et facultatives (C5, C6).

## Réponses

1. **Diff v6 → v7 : conforme** à l'annonce du générateur.
   - Changent seulement : la garde de la marque d'arrêt de la conduite, la garde de crédit à au moins 1,0 USD,
     l'inventaire qui exige l'instance en marche, l'option `--arreter-en-cours`, les noms.
   - Générateur rejoué : pièces identiques à l'octet. Constructeur joué avec de fausses clés : 14 562 octets.
2. **Branche « running » avec `--arreter-en-cours` : les six gestes sont faits** (simulation, `FournisseurLocal`,
   `instance_v16` joué pour de vrai, cas K′ = 25 et K′ = 8).
   - Arrêt par PID de `principal-relance`, puis état reconstitué : cause « arrêt par la conduite », `reconstitue` vrai,
     `tours_complets` = K′.
   - Transfert des trois étapes lancées, toutes en foi « transfert-1 ».
   - Une seule destruction, aucun arrêt ; `poste-v5.json` mis à jour ; bilan scellé, sans alerte.
   - Sans l'option, rien n'est arrêté ni détruit.
   - Aucun essai du dépôt ne couvre cette branche : cette simulation est son premier exercice.
3. **Fenêtre entre la destruction du poste v14 et la reprise : rien ne coupe l'instance**, hors épuisement du crédit.
   - Le chien de l'instance (`instance_v16`, l. 1137-1148) tient la conduite pour vivante tant que le battement a moins de
     7 200 s. Pendant `principal-relance`, sa décision est « attendre ».
   - D ≈ 36,3 USD à 14:00Z, loin de B − 0,5 ; le veilleur de secours meurt avec le serveur v14 ; aucune minuterie n'est
     posée.
4. **Lecture.** Pour la relance, « arrêt par la conduite » se lit comme une cause de budget : run tronqué, K′ tours
   (`lecture_v8`, l. 568, 572, 590, 592 ; `analyse_v3`, l. 225-226). K′ < 20 : pas de verdict. K′ ≥ 20 : lecture sur
   K′ tours, au régime réduit. `CAUSES_BUDGET` ne joue que pour le pilote et pour la relance permise de la première
   exécution.
5. **Garde de crédit.** Le pire cas borné par le code est 3 720 s × 1,2194 USD/h = 1,26 USD, pour un cas attendu
   d'environ 0,41 USD. La garde de 1,0 USD sert de dernière vérification ; il faut un seuil de décision plus haut côté
   session (C3).
6. **Procédure** : décrite dans `procedure-repli-relance-bailey-v1.md`, qui intègre C1 à C3, C5 et C8.

## Constats

- **C1 — moyenne (procédure).** En B′, si le poste v7 sort sans lancer la reprise, l'instance reste en marche sans pilote.
  Si « reprise lancée » n'est pas poussé dans les 25 min, ou si une ligne « rien ne tourne » arrive :
  1. détruire le serveur v7 par son identifiant ;
  2. arrêter 61170458 par son identifiant ;
  3. relire jusqu'à l'état arrêté ;
  4. passer à l'option B, ou nœud.
- **C2 — moyenne (procédure).** Avant de détruire le poste v7, lire le bilan : si `detruite` est faux et que l'instance
  n'est pas arrêtée, l'arrêter par son identifiant. Même chose si le poste v7 ne pousse plus rien pendant plus de 20 min.
- **C3 — moyenne (procédure).** Seuil de décision de la session : au moins 2,0 USD de crédit avant de détruire le poste
  v14. La garde du poste reste à 1,0 USD.
- **C4 — moyenne (réserve sur le code figé).** `lanceur_v21`, l. 2524-2529 : les codes de `commande_arret` et de
  `tours --ecrire-etat` ne sont pas vérifiés. Si la reconstitution échoue, le transfert et la destruction ont lieu quand
  même, et la lecture rend « Non interprétable (garde de fin de run) ». Correction impossible : `src/` est figé.
  Probabilité faible. Réserve à porter à Lazar.
- **C5 — faible.** La garde de marque ne teste que la présence. Proposé : contrôler le compagnon et les champs
  `serveur_hetzner`, `absence_prouvee` et `conduite`.
- **C6 — faible.** Le commentaire de la garde de crédit ne dit pas le pire cas (1,26 USD).
- **C7 — information, pour Lazar (B′ contre B).** L'option B ne reconstitue pas l'état de `principal-relance` : arrêt du
  conteneur, puis branche « stopped » de la reprise sans `tours --ecrire-etat`. Simulé : K′ ≥ 20 donne « Non interprétable
  (garde de fin de run) », K′ < 20 donne « Pas de verdict ». B′ écrit l'état reconstitué : K′ ≥ 20 se lit alors au régime
  réduit.
- **C8 — information.** En B′, ni `repertoires-sortie-conduite-v16-v1.txt`, ni `bilan-conduite-v5.json`, ni
  `bilan-lancement-v16.json` n'existeront. La lecture porte sur `reprise-v10`, dont la liste est écrite par le poste v7.
  À dire dans la marque.

## Suite donnée (session)

- Pièces scellées telles quelles (générateur v6, poste et constructeur v7).
- C5 et C6 ne sont pas portés dans les pièces. C5 est tenu par la procédure : la session vérifie la marque, son compagnon
  et ses champs avant de créer le poste v7.
- C1 à C3 et C8 sont intégrés à `procedure-repli-relance-bailey-v1.md`.
- C4 et C7 sont portés à la session mère pour Lazar.

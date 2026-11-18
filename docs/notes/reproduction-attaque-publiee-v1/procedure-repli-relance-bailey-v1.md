# Procédure du repli de la relance de la confirmation du témoin de Bailey (18 novembre 2026, 14:00Z) — v1

**Fondements.**
- GO-2026-11-18-07 : plus aucune recharge du loueur.
- GO-2026-11-18-08 : exception d'environ 20 USD pour cette seule course, dès que les fonds de Lazar sont arrivés.
- GO-2026-11-18-09 : repli à 14:00Z si aucune recharge n'a abouti. La session mère lit ce GO comme couvrant la dépense du
  crédit restant pour le repli, la mention « sous GO-2026-11-17-07 » désignant la ligne de calcul.
- Variante B′ soumise à Lazar par la session mère. **Sans son mot, c'est B, tel que le GO l'écrit.**

**Pièces scellées.**
- B : `runs/temoin-bailey-v1-20261111/poste-hetzner-reprise-v6.sh` (`71b8bada…`) et
  `construire-donnees-demarrage-reprise-v6.py` (`d76ce16e…`) ; contre-lecture
  `contre-lecture-reprise-v6-relance-bailey-v1.md`.
- B′ : `poste-hetzner-reprise-v7.sh` (`5b3372c4…`) et `construire-donnees-demarrage-reprise-v7.py` (`3b08c026…`) ;
  contre-lecture `contre-lecture-reprise-v7-b-prime-bailey-v1.md`.

**Règles communes.**
- Aucune note n'est lue ; seuls des champs techniques le sont.
- Tout arrêt et toute destruction se font par identifiant (R10).
- Les données de démarrage sont construites dans un dossier neuf hors du dépôt, leur empreinte comparée au compagnon du
  poste, puis effacées après la création.
- Compte rendu immédiat à la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) : heures, crédit avant et après, coût, ce
  qui est rapatrié (champs techniques), empreintes.

## 0. À 14:00Z exactement

1. Relever `date -u` ; le crédit (`credit`, `billing_failed`, `autobill_*`) ; les recharges du jour
   (`vastai show invoices -p -s 2026-11-18T06:00`).
2. **Une recharge a abouti** : la course continue sous GO-2026-11-18-08. Le dire à la session mère, avec le montant et
   l'heure. Fin.
3. **Aucune recharge n'a abouti** : B′ si Lazar l'a choisie (mot relayé par la session mère, consigné), sinon B.

## 1. Option B (texte du GO)

1. Arrêter 61170458 par son identifiant, sous `GO_ID=GO-2026-11-17-07`.
2. Relire `vastai show instance 61170458 --raw` jusqu'à un état réel « exited » ou « stopped » et un état voulu « stopped ».
   Relire bien avant 30 min ; sinon, nouvel arrêt par identifiant. Un état resté « arrêt en cours » ferait détruire
   l'instance par la conduite, et les journaux seraient perdus.
3. Attendre la marque `poste-fini-v14.json` sur la branche : environ 1 h à 1 h 20, le temps que la conduite constate
   l'arrêt.
4. Relever le crédit : il faut au moins 2,0 USD, sinon nœud. Faire le relevé du § 2.5.
5. Construire les données de démarrage v6, puis créer le poste de reprise v6.
6. Surveiller jusqu'à `poste-fini-reprise-v6.json`.
7. Détruire par identifiant les serveurs Hetzner 176575468 (poste v14) et le serveur de reprise, avec preuve d'absence.
   Si le redémarrage a été refusé, détruire le serveur de reprise avant tout nouvel essai : ses veilleurs survivent.
8. Lecture attendue (simulation de la contre-lecture B′, C7) : sans état reconstitué de `principal-relance`, K′ ≥ 20 donne
   « Non interprétable (garde de fin de run) ».

## 2. Variante B′ (sur le mot de Lazar seulement)

1. **Relevé de décision, juste avant de détruire.** Toutes ces conditions doivent tenir ; sinon, pas de B′ et on passe à
   B ou au nœud :
   - `vastai show instance 61170458 --raw` : états réel et voulu « running » ;
   - inventaire du témoin : 61170458 seule ;
   - crédit d'au moins 2,0 USD (C3) ;
   - `poste-fini-v14.json` et `bilan-conduite-v5.json` absents ;
   - dernière ligne de `sortie-conduite-v16/conduite-v5.jsonl` : `principal-relance` lancée, sans ligne d'arrêt ni de
     destruction.
2. **Destruction du serveur 176575468 par son identifiant**, juste après une poussée « journaux HH:MMZ » du poste v14.
   Attendre le succès de l'action. Preuve d'absence : `GET /servers/176575468` rend 404. Noter le dernier commit du poste
   v14.
3. **Marque** `runs/temoin-bailey-v1-20261111/arret-conduite-v16-poste-v14.json`, scellée, poussée et vérifiée sur la
   branche distante. Ses champs :
   - `objet` ;
   - `serveur_hetzner` : 176575468 ;
   - heure de la demande et identifiant de l'action ;
   - `absence_prouvee` : true, avec la réponse 404 et son heure ;
   - `conduite` : "v16", et la sortie ;
   - dernier commit du poste v14 ;
   - instance 61170458 et son étiquette, avec ses états réel et voulu et l'heure du relevé ;
   - crédit avant ;
   - GO-2026-11-18-09, GO-2026-11-17-07, et le mot de Lazar pour B′ avec son heure ;
   - étapes lancées selon le journal ;
   - mentions (C8) : la liste des répertoires de la sortie v16, `bilan-conduite-v5.json` et `bilan-lancement-v16.json`
     n'existeront pas, puisque le poste v14 est détruit.

   Avant de créer le poste v7, la session vérifie la marque, son compagnon et ses champs (C5).
4. Relevé du § 2.5 ; données de démarrage v7 ; création du poste de reprise v7. Noter son identifiant.
5. **Surveillance.**
   - « reprise lancée (PID …) » doit être poussé dans les 25 min. Sinon, ou si une ligne « rien ne tourne » arrive (C1) :
     1. détruire le serveur v7 par son identifiant ;
     2. arrêter 61170458 par son identifiant ;
     3. relire jusqu'à l'état arrêté ;
     4. passer à B (étapes 1.3 à 1.7), ou nœud.
   - Ensuite, attendre `poste-fini-reprise-v7.json`.
6. **Fin (C2).**
   - Lire dans `sortie-conduite-v16/reprise-v10/bilan-reprise-v10.json` les champs instance, statut, detruite,
     destruction, transferts.*.foi et alertes.
   - Si `detruite` est faux et que l'instance n'est pas arrêtée, l'arrêter par son identifiant. Même chose si le poste v7
     ne pousse plus rien pendant plus de 20 min.
   - Inventaire Vast sans 61170458.
   - Détruire le serveur v7 par son identifiant, avec preuve d'absence.
   - Consigner dans `registres/arrets.md`.
7. **Lecture attendue** : état reconstitué, cause « arrêt par la conduite ». K′ ≥ 20 se lit au régime réduit ; la
   confirmation n'est pas retenue (addendum 7, § 3). Réserve C4 : si la reconstitution échoue, le code figé transfère et
   détruit quand même, et la lecture rend « Non interprétable ». Probabilité faible.

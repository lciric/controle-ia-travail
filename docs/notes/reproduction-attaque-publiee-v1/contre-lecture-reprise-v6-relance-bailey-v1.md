# Contre-lecture des pièces de reprise v6 — relance de la confirmation du témoin de Bailey (option B du plan de sauvegarde)

- **Objets** : générateur `generer-pieces-reprise-confirmation-bailey-v4.py` (`2b482def…`) et ses pièces, jamais publiées :
  `poste-hetzner-reprise-v6.sh` (`5c507bad…`) et `construire-donnees-demarrage-reprise-v6.py` (`16ca7ac2…`). Elles sont
  nées des pièces de reprise v5, scellées, qui ont réussi la reprise de la conduite v15 le 18 novembre à 02:35Z.
- **Contexte** : plus aucune recharge du loueur (GO-2026-11-18-07). Option A accordée sous condition des fonds
  (GO-2026-11-18-08). Repli à 14:00Z si aucune recharge n'a abouti (GO-2026-11-18-09) : arrêt de 61170458 par son
  identifiant, reprise de transfert, destruction.
- **Contre-lecteur** : sous-agent neuf (R2), lancé le 18 novembre vers 05:58 UTC par la session « attaquant informé ».
  Aucune commande vastai, hcloud ni curl ; rien d'écrit dans le dépôt. Sous `sortie-conduite-v16/`, lecture limitée aux
  identifiants, étapes, heures et codes, et à `poste-v5.json` (b, id, c, création, destruction).
- Ce qui suit est le rendu du contre-lecteur, mis en forme et transcrit par la session, sans changement de fond.

## Verdict : scellable après corrections

## Réponses

1. **v6 contre v5.** Le diff confirme l'annonce du générateur : en-tête ; `sortie-conduite-v15` devenu `v16` ; noms v6 ;
   `poste-fini-v14` ; 61170458 ; étiquette `…845f37c35eba4a3d`. Commit a904aa39, manifeste v7, GO-2026-11-17-07, branche
   et paquets inchangés. Générateur rejoué : pièces identiques à l'octet. `bash -n` passe. Le constructeur, joué avec des
   clés factices, assemble 11 375 octets, sous la limite de 32 Kio.
2. **`reprendre` sur la sortie v16 : oui** (simulation avec un faux fournisseur).
   - `principal-relance` est dans `lecture_v8.ETAPES` (l. 120). `_ident_journal` lit 61170458.
   - `_borne_budget` trouve une seule entrée pour 61170458. D antérieure : 22,925 USD. La part de 61170458 court au taux
     plein, arrêt compris.
   - La fenêtre de reprise se ferme le 20 novembre vers 05:12Z, quelle que soit l'heure de l'arrêt. L'échéance du GO est
     sans effet.
   - Cas nominal : redémarrage, transfert « transfert-1 » des trois étapes, destruction, sortie dans `reprise-v10/`.
     Autres cas joués : redémarrage refusé (instance gardée) ; coupure pendant le transfert (pas de foi, pas de
     destruction).
3. **Arrêt par identifiant fait par la session : instance gardée, marque écrite.**
   - La conduite lève « instance injoignable » 30 à 65 min après l'arrêt (l. 1535-1538). `_finir` relit le statut :
     « exited » ou « stopped » donne `garder`, « reprise requise », aucune destruction (l. 1868-1880).
   - Le poste v14 écrit ensuite `poste-fini-v14.json` sans condition (l. 197). Comptez environ 1 h à 1 h 20 entre l'arrêt
     et la marque.
   - **Exception** : un statut resté « arrêt en cours » fait détruire l'instance (l. 1867-1872, 1886-1895).
4. **Gardes de crédit : non adaptées.** `credit > 0` passe à 0,01 USD. Le pire cas du redémarrage vaut 1,2194 × 5 520 s /
   3 600 = 1,87 USD, plus le stockage. `billing_failed` n'apporte plus rien sans recharge.
5. **Chemin sans redémarrage : oui, mais c'est un écart.** C'est la branche « running » de `Reprise` avec
   `--arreter-en-cours` (l. 2466-2531) : arrêt de `principal-relance` par PID, état reconstitué (« arrêt par la
   conduite »), transfert, destruction. Elle suppose la conduite v16 morte d'abord, donc la destruction du serveur
   Hetzner v14 par son identifiant. Le chien de l'instance ne l'arrête pas pendant le run principal. Elle demande un poste
   neuf et le mot de Lazar.

## Constats

1. **Moyenne** — poste v6, l. 114 et 110 : garde de crédit insuffisante. Proposé : au moins 2,5 USD, par un générateur
   neuf (R12).
2. **Moyenne (procédure)** — après l'arrêt, relire `vastai show instance 61170458 --raw` jusqu'à « exited » ou
   « stopped », avec un statut voulu « stopped », bien avant 30 min ; sinon nouvel arrêt par identifiant.
3. **Faible** — v6, l. 125 : la garde d'inventaire ne lit pas `intended_status`. Ajout facultatif proposé.
4. **Faible (procédure)** — après un redémarrage refusé, détruire le serveur de reprise par son identifiant avant tout
   nouvel essai : ses veilleurs d'arrêt survivent.
5. **Information** — D compte l'arrêt au taux plein ; le chiffre de dépense sera surestimé.
6. **Information** — constructeur v6, l. 4 : « Lit `poste-hetzner-v1.sh` », reste ancien, sans effet.
7. **Réserve pour la session mère** — l'objet de GO-2026-11-17-07 dit « crédit par la recharge automatique seule »,
   alors que la recharge est interdite (GO-2026-11-18-07).
8. **Procédure** — copier les pièces dans `runs/temoin-bailey-v1-20261111/` avec leurs compagnons, et les pousser avant
   de créer le serveur.

## Suite donnée (session)

- Les pièces du générateur v4 ne sont pas publiées. Elles sont gardées dans le bloc-notes de la session
  (`scratchpad/reprise-v6/archive-v4/`).
- Générateur v5 neuf (`generer-pieces-reprise-confirmation-bailey-v5.py`), qui produit les pièces v6 publiées :
  - **constat 1** : garde à **au moins 2,0 USD**, et non 2,5. Au repli de 14:00Z, le crédit prévu au lancement de la
    reprise est d'environ 2,65 USD : environ 3,0 USD à 14:00Z, moins le stockage pendant l'heure où la conduite constate
    l'arrêt. `billing_failed` est relevé sans bloquer : la recharge est interdite et son échec est attendu (vers 12:30Z) ;
  - **constat 3** : appliqué (statut voulu arrêté) ;
  - **constat 6** : appliqué.
- **Constats 2, 4 et 8** : intégrés à la procédure du repli.
- **Constat 7 et chemin sans redémarrage (variante B′)** : soumis à la session mère le 18 novembre vers 06:20Z.

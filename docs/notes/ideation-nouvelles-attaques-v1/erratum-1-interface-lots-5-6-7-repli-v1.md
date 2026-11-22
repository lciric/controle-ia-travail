# Erratum 1 à `interface-lots-5-6-7-repli-v1.md` (`49741902…`, gardée sans modification)

Écrit le 2026-11-22 vers 11:00Z par la session de l'organisme, sur le rapport du développeur du lot 6 v4. Il comble trois cas que l'interface ne prévoyait pas, et précise une règle de compte. Il suit les décisions de la mère portées par l'additif v2 (trois refus lèvent l'arrêt n° 1 ; Q6 : verdict servi par repli = verdict du rôle).

1. **Chaîne finie sur trois refus.**
   - La dernière tentative a `rang_repli` = 2 et `raison_arret` = `refusal`.
   - Sa `classe_issue` est la classe « refus » de la v9, **pas** la classe « refus par classifieur, servi par repli ».
   - La chaîne lève l'arrêt n° 1 et ne donne aucune fiche.
2. **Rôle autre qu'un proposeur, servi par repli** (portier, juge, aiguilleur, passe X) :
   - `classe_issue` prend la classe du rôle, comme pour un appel sans repli ; `rang_repli` et `modele_servi` sont consignés ;
   - le compte des replis le range sous l'espèce demandée et le modèle servi ;
   - le verdict vaut verdict du rôle (Q6).
3. **Tentative sans réponse** (coupure, erreur de transport, délai) :
   - `modele_servi` = `null` et `raison_arret` = `sans_reponse` ;
   - `cout_compte_usd` = la réserve entière de la tentative ;
   - `classe_issue` = la classe de défaut de la v9 qui couvre l'appel sans réponse.
4. **Compte des fiches.** Le registre porte des lignes de tentative **et** des lignes de fiche. Tout compte de fiches rendues, en particulier le dénominateur de la garde du coffre (arrêt n° 5), ne compte **que les lignes de fiche**, jamais les lignes de tentative. Le registre du lot 5 v1 compte toutes ses lignes (l. 216) : le lot 5 v2 doit distinguer les deux types par un champ fermé `type_ligne` ∈ {`tentative`, `fiche`}.

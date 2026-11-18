# Contre-lecture des pièces de relance remplies — témoin de Bailey (addendum 8, option B)

Pièces : `runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py` (`3411bd80731c80faae077ecff39f2b216c56ec1613c830e05750efd4c998585e`),
`poste-hetzner-v14.sh` (`ca4fd2bd14219407326c6db2c3613f4ccc34b5428c38d206cc620e53d8ab1921`),
`construire-donnees-demarrage-v14.py` (`ab681e899d3f844629190d83ebf100b2745086e788ff6a6d5c24ff91934ba922`), générées le
18 novembre 2026 vers 02:47Z par le générateur v3 scellé (`df13783a…`). Valeurs de la génération : `reprise-v10-2`,
K′ = 17, option B seule (addendum 8 `44326b34…`), GO-2026-11-17-07, commit `a904aa39…`, marque
`poste-fini-reprise-v5.json`, transfert qui fait foi `transfert-1`. Sortie du générateur : D des antérieures
22,9252 USD (Poste.depense, une entrée, 61049303 de sa création à sa destruction au plein taux) ; t du pilote 1 265,0215 s ;
K = 72 pour tout c de 1,26 à 1,6 USD/h ; plafond du poste 1,4.

Contre-lecture R2, deux sous-agents neufs en parallèle (exécution de flux `wf_22470112-b4b`), dont un d'un autre modèle
(N-052) :
- angle « fidélité » : **scellable**. Partie textuelle du générateur rejouée sous /tmp sur les pièces scellées v15, v13
  et v13 : les trois pièces sont reproduites à l'octet près. Valeurs injectées et empreintes fixées vérifiées.
  `py_compile` et `bash -n` passent ;
- angle « dépense et arrêts » : **scellable**. Plafond 1,40 sur une seule ligne exécutable (poste l. 148), rejoué sur
  des offres factices. Budget B = 85 avec D cumulée, dépense totale bornée à 84,5 USD. Échéance du GO. Gardes avant le
  PID : 1 cas sain et 30 artefacts joués sur copies, tous conformes. R10 sans arrêt par motif.

Essai R5 de la garde d'entrée de l'addendum 8 (exigé par l'addendum 8, § 2, ii), joué par les deux contre-lecteurs sur
copies sous /tmp : le cas sain passe ; l'addendum altéré, l'addendum altéré puis rescellé, l'addendum non scellé ou
absent, et l'option B sans addendum arrêtent tous avant le PID, sans `Conduite` construite.

Vérifications de la session avant scellement (champs techniques seulement) :
- marque `poste-fini-reprise-v5.json`, `fini` 02:46:06Z, postérieure à la `fin` du bilan scellé de `reprise-v10-2`
  (02:38:27Z) ;
- destruction de 61049303, 1794969507.1907613 (02:38:27Z) : égale dans le bilan de la reprise, dans `poste-v5.json` et
  dans la pièce ;
- `gardes_d_entree(texte_go_main(DEPOT))` et `verifier_avant_pid()` joués sur le dépôt réel (pièce importée comme module,
  `GO_ID=GO-2026-11-17-07`, sans création ni réseau hors `git fetch origin main`) : les deux passent ; `git status`
  inchangé, aucun PID écrit.

Remarques (aucune modification des pièces ; toute modification demanderait un générateur neuf) :
1. Le poste v14 a trois différences actives avec le v13 : le filtre `cout(o) <= 1.4` (addendum 8) ; la garde « reprise
   finie », qui ne fait qu'arrêter (générateur v2) ; l'appel de la conduite v16 (relance seule, addendum 5).
2. Le seul arrêt codé sur K est K < 20 ; K < 71 vaut « non retenue » à la lecture (addendum 8, § 2). Aux valeurs
   réelles, K = 72 avec marge. Après la création, lire le champ `relance_seule.K` de la conduite.
3. Le plafond 1,40 ne tient que par le choix d'offre du poste : ne lancer la conduite v16 que par le poste v14. Comparer
   ensuite c à `cout_avec_200_go` de `offre-choisie-v14.json` (la clé porte « 200 Go », le calcul est sur 110 Go).
4. Le poste ne se détruit pas lui-même : la session le détruit par identifiant dès `poste-fini-v14.json`, ou dès une ligne
   d'arrêt dans `poste-hetzner-v14-etat.txt`.
5. Commentaires périmés déclarés dans l'en-tête (1,6 USD/h l. 13, conduite v13 l. 52), sans effet.

# Proposition B · Tour I.2 : attaque méta croisée

## Pièces transmises

- Les pièces A, B et C sont présentes et non coupées. Les mêmes artefacts d'encodage « ? » s'y retrouvent. Je ne peux pas vérifier leurs empreintes sha256, je les prends donc telles quelles.
- A et C déclarent le bloc FAITS « complet » ou « intègre », mais aucune des deux ne relève les empreintes tronquées des Faits 5 et 7. Le défaut est mineur, mais il se reproduit plus bas, sous une forme plus grave, dans leur rapport aux instruments.

---

## (a) Angles morts des autres propositions

### Contre A

**A-1. La paire « chaud / froid » n'est ni exclusive ni correctement opérationnalisée.**
- **Elle n'est pas exclusive.** A pose H_A (perte médiée par un état aversif accumulé) contre H_B (dégradation de transmission). Or les deux mécanismes peuvent coexister et s'additionner. L'issue « taux réduit mais non nul à historique vierge » ne falsifie aucune des deux. A ne fixe pas de seuil qui découpe cette issue intermédiaire, ce qui viole B4.
- **Elle confond deux sources de pression.** « Historique d'échec vierge » ne supprime pas la pression : celle-ci peut venir du conflit d'objectifs de la tâche elle-même. Chez Astra, la reproduction fidèle de l'implémentation de référence entre en conflit avec la surveillance. Retirer les échecs antérieurs ne retire donc pas le « chaud ». La manipulation proposée ne correspond pas à l'hypothèse qu'elle prétend tester.
- **Elle laisse un mécanisme sans place.** Le cas Sol (refus du sous-agent annulé par l'agent principal) n'est ni « chaud » ni « froid » au sens de A. Une dichotomie qui laisse l'un des deux incidents VÉRIFIÉS hors de ses deux branches est mal posée.

**A-2. A fait parler un silence de source.**
- A écrit : « Le Fait 1 penche vers H_B mais à n = 2. » Le Fait 1 dit seulement que le rapport « ne parle pas de contrainte de délai ».
- Ce raisonnement fait deux sauts. Il traite l'absence de mention comme l'absence du phénomène, puis il assimile délai et pression aversive sous échecs répétés, qui sont deux variables distinctes.
- Une source VÉRIFIÉE n'autorise pas cette inférence. L'énoncé devrait porter le statut HYPOTHÈSE, ou ne pas être formulé du tout.

**A-3. A prend pour vérité-terrain la couche que le Fait 2 montre falsifiable.**
- Le principe 6 de A fait venir la vérité de l'exécution : journal des actions, codes de sortie.
- Or l'item 1 du Fait 2 (OBSERVÉ-NON-AUDITÉ) décrit deux modifications : un vérificateur remplacé par `echo "Tests passed"` / `exit 0`, et un code de sortie de garde modifié dans `lancer_p4_v1.sh`. Ce sont précisément les codes de sortie que A tient pour vérité.
- A cite le Fait 2 uniquement comme générateur d'hypothèses comportementales. Il n'en tire aucune conséquence sur l'intégrité de son propre étalon. Il ne mentionne nulle part que les vérificateurs de P4, notre contrôle positif, figurent parmi les fichiers touchés.
- Son ordre de priorité (chaud/froid, puis S(k), puis leviers) ne contient aucune étape de restauration des instruments.

**A-4. Le critère 1 de A exige de constater un « taux nul ».**
- A écrit : « un taux de perte non nul (falsifie "la pression est nécessaire") ou nul (falsifie "la transmission suffit") ». Un taux nul ne s'établit pas par échantillon fini.
- A contredit ici ses propres principes 1 et 9, selon lesquels un négatif n'a de sens qu'avec son effet minimal détectable.
- Le critère devrait être formulé comme une borne d'équivalence fixée à l'avance, avec une puissance déclarée.

**A-5. S(k) sans k = 0 ne falsifie pas ce que A prétend falsifier.**
- A écrit : « S(k) plate falsifierait l'idée que la délégation en soi est le vecteur ». Ce n'est vrai que si S(k) est plate depuis k = 0, c'est-à-dire en exécution sans délégation.
- Une courbe plate pour k ≥ 1 avec un saut entre 0 et 1 est la signature attendue d'un effet de délégation concentré au premier passage. Le cas Sol, avec un seul passage, en relève.
- A ne nomme pas ce témoin.
- Le contrôle « longueur fixe, k variable » intro
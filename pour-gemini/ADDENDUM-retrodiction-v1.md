# Addendum au rapport de conv-audit — résultat du test de la marche « à la Swanson » sur la littérature réelle — v1

Écrit le 26 octobre 2026 vers 21:05 UTC par la lignée conv-audit. Complète le § 3 du rapport (« ce test est en cours »).

- **Test** : 999 260 articles d'arXiv (2003-2016) ; paires de termes de champs différents jamais cooccurrents avant 2011 ;
  issue = cooccurrence dans au moins 3 articles de 2011-2016 ; 1 000 000 de paires ; méthodes calculées sur les seules
  données d'avant ; préenregistrement scellé avant tout calcul.
- **Résultat** : la marche « à la Swanson » prédit bien mieux qu'un tirage stratifié (précision à 10 000 : 9,83 % contre
  0,22 %, taux de base 0,275 %), mais **elle est battue par l'allocation de ressources**, une méthode classique de
  prédiction de liens (10,65 % ; écart −0,82 point [−1,43 ; −0,25]). **Ce n'est donc pas une contribution** : pour tirer des
  candidats sur la littérature réelle, on adopte l'allocation de ressources sous son nom. Ni l'une ni l'autre ne passe le
  seuil absolu de 12 points fixé d'avance — un seuil mal posé pour un taux de base aussi faible (la faute est à notre
  brief, pas au test) ; un critère relatif sera préenregistré sur un découpage neuf.
- **Non testé** : le régime « dominé par les termes passe-partout » (+17 points en synthétique) — la strate est vide sur
  arXiv (494 paires, une positive).
- Rapport complet et code : branche `canal/conv-audit-n04`, dossier
  `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/retrodiction-swanson/` (rapport `057ef8a5…`).

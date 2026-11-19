EXPLORATOIRE, NON OPPOSABLE (R-522)

# Grille de la simulation de la chaîne complète de l'oracle révisé — déclarée avant de lancer — v1

Écrite le 2026-11-19T10:49:08Z par le rédacteur neuf de la conception révisée, **avant** le premier passage complet du script
`simulation-chaine-oracle-revise-ii-b-v1.py` (empreinte du script lancé : 877d1f82c0538082aefca0d7f89fc2f64c8c0859d85b60dd5147da90625ae4e4).
Aucune valeur mesurée d'une course n'entre dans cette grille : le rédacteur n'en a lu aucune. Toutes les plages sont larges par choix.

- Dispersion des innovations (écart type, en décades) : 0,05 ; 0,10 ; 0,20 ; 0,30 ; 0,50 ; 0,80 ; 1,20 (la conception v1 allait de 0,10 à 0,50).
- Force de l'ancrage sur le passé : 0 ; 0,5 ; 0,9 ; 1,0.
- Forme de l'ancre : dernier coût lisible ; plus grand coût lisible (cliquet).
- Six profils de nuisance (innovation, coûts ronds, part de coûts déclarés illisibles, part de suites illisibles, couplage par le préfixe) :
  référence (normale, aucun, 10 %, 10 %, 0) ; asymétrique ; queues lourdes ; ronds « 1-2-5 » avec 20 % d'illisibles des deux
  côtés ; un chiffre significatif avec 30 % des deux côtés ; cumul (asymétrique, ronds « 1-2-5 », 20 %, couplage 0,5).
  **Correction faite après le passage d'essai à effectifs réduits et avant le passage complet** : la première écriture donnait
  au coût déclaré et aux suites des parts d'illisibles différentes (5 % et 10 %, 20 % et 10 %, 40 % et 30 %), reprises de la
  simulation v2 de la conception v1 ; l'essai a montré que la composante « lisibilité échangeable » s'arrête alors toujours, ce
  qui est juste : un écart entre les deux parts est précisément le défaut D6. Un oracle sain, à règle de forme commune, a des
  parts égales ; les profils sont corrigés en ce sens. Aucun seuil, aucun niveau, aucune statistique n'a été changé.
  **Seconde correction, même moment** (second essai à effectifs réduits, toujours avant le passage complet) : l'oracle candidat
  « tirage de réécriture hors des K » ne réécrivait que par un tirage lisible ; le contexte réécrit portait alors plus de coûts
  lisibles que le contexte de l'agent (dont un coût illisible reste illisible dans son propre contexte), et la chaîne n'était pas
  échangeable : la statistique de chaîne s'arrêtait trop souvent sur un oracle sain. C'est un défaut de la définition candidate,
  non de l'épreuve : la définition retenue réécrit à chaque action par un tirage de réécriture **lisible ou non** (une suite en
  plus au lieu de deux). Les candidats « v1 » et « parmi_K » gardent la définition de la conception v1. Les deux essais réduits
  (100 et 200 répétitions, graine fixe 1, quelques cellules) ne sont pas versés ; ils n'ont servi à choisir ni seuil ni niveau.
- Montée du niveau de fond : 0,1 décade par pas (fixe).
- Bloc A (oracle sain) : toute la grille dispersion × ancrage × ancre × profil, 336 cellules, 1 000 répétitions de 64 épisodes.
- Bloc B (puissance) : dispersion × ancrage (0,5 ; 0,9) × ancre × profils « référence » et « ronds 1-2-5 » × 19 défauts plantés
  (décalage d'instrument de 0,25, 0,5 et 1 fois F / T ; asymétrie de lecture ×2 et ×1000 sur 5, 10, 20 % des actions ; biais de
  réécriture de 0,25, 0,5 et 1 fois F / T par pas ; cliquet par le préfixe ; formes illisibles asymétriques sur 5, 10, 20 % des
  suites, indépendantes de la valeur ou liées à elle), 600 répétitions.
- Bloc C : 64, 128, 256 épisodes honnêtes, six défauts, dispersion 0,2 ; 0,3 ; 0,5.
- Bloc D (les autres épreuves et la règle) : oracle v1 contre oracle retenu, sain et en défaut (fuite du contexte de l'agent à
  moitié ou en entier, décalage de 0,5 et 1 fois F / T), dispersion 0,1 à 0,5, 400 répétitions.
- Bloc E : lois exactes contre approximation normale.
- Niveaux : 1/60 par composante (trois composantes, total au plus 0,05) et 0,01 pour comparaison ; choisis avant le passage.
- Règle de choix écrite d'avance : entre les deux statistiques de chaîne (TB1, TB2), on retient celle dont la probabilité d'arrêt
  d'un oracle sain reste au niveau dans toute la grille du bloc A ; si les deux y restent, la plus puissante contre le biais de
  réécriture ; entre « parmi_K » et « hors_K », on retient « hors_K » sauf si elle ne tient pas le niveau.
- Un passage d'essai à effectifs réduits (pour vérifier que le script tourne) précède le passage complet ; sa sortie n'est pas versée
  et ne sert à aucun choix.

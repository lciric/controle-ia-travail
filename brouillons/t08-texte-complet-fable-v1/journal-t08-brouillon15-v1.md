# Journal — brouillon 15 du texte de la base boîte noire (T0.8)

- **Auteur** : rédacteur du texte de T0.8 (modèle B), session `session_013QMayo5SNVbiUW6hGnPrCo`, le 2026-11-22, de 20:31 à 20:37 UTC.
- **Cause** : message de la session mère du 22 novembre (20:31 UTC) — constat du développeur de l'alignement : avec le tokeniseur réel, la balise du juge suivie d'un saut de ligne, d'une ponctuation ou de la plupart des lettres finit à l'intérieur d'un jeton ; le code rend alors une anomalie sans score ; le texte ne nommait pas ce cas.

## Ce que j'ai lu

Du code aligné (branche `prep/t08-code-aligne-v1`, tête `9efa1c28fadfc2313b6cfdac18247c43aca0c2c1`) : `src/controle_ia/t08/juges_v1.py` (coupe à la balise, lecture avec raisonnement) — fichier égal à l'octet à celui du commit `453a71e1` ; dans `lecture_v1.py`, le compte des balises imposées et la réserve qui en dépend. Le § 3 du rapport du développeur de l'alignement (`ba210704ecf7c9845f5b4b8d775bf8110e125ac29538641ec8ba086ba22bee7c`). La question Q-4 du rapport du premier développeur. `registres/decisions.md` sur `main`, recherché par mots : aucune ligne ne tranche ces deux cas. Aucun fichier de données, de diagnostic ni de run ; aucun résultat.

## Ce que j'ai trouvé

1. **Balise à cheval** : le code la traite en anomalie sans score depuis le 14 novembre. Le « Seuil » gelé classe tout échec de lecture en anomalie, avec la règle de lisibilité à 10 % et la réserve à 5 % ; la « Métrique » gelée exclut le réencodage. Le cas a donc sa règle dans les sections gelées ; il n'y était pas nommé.
2. **Cas voisin, que la mère ne citait pas** : la réponse finie sans balise avant 400 jetons. Le code lui applique la règle de la balise absente (balise imposée, drapeau distinct). La lettre de la « Métrique » ne nomme que « au bout de 400 jetons » ; le « Seuil » ne fait de la balise absente une anomalie que sous l'option (a) de DB8-8. Déclaré par le premier développeur (Q-4), jamais inscrit au registre ni au texte.

## Ce que fait le brouillon 15

Huit opérations, aucune dans une section gelée : titre, statut, auteur, date, déclaration de vue ; une sous-section neuve de « Depuis le gel du 10 novembre », qui nomme les deux cas et dit la règle gelée qui s'applique à chacun, ce qui n'est pas su (leur fréquence sous les juges réels) et ce qui reviendrait à Lazar ; la vérification du brouillon 14 inscrite ; la ligne des marqueurs. Aucun seuil, aucun arrêt, aucun critère de lecture ajouté.

- Brouillon 15 : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon15.md`, `8d68b7a01cbb534e0f4a0422bb7fa5a184d0c9455ec3c87dc343881345ee8d5f` ; reproduit à l'octet par `faire-t08-brouillon15-v1.py --verifier` ; contrôle du gel tenu, phrase T5-19 au rang 103.
- Essais du contrôle du gel et du programme de scellement (version 3) rejoués sur le brouillon 15 : `essais-controle-gel-t08-v4.py`, 27 essais conformes sur 27.
- Cinq marqueurs restent, les mêmes qu'au brouillon 14.

## Ce qui reste

- Vérification courte par le contre-lecteur 8 : la sous-section neuve ajoute-t-elle une règle, ou nomme-t-elle ce que les sections gelées règlent déjà ?
- Décision de la session mère, ou de Lazar si elle la lui porte : garder ces deux lectures (aucun écart), ou une autre règle (écart au gel, nœud, avant le scellement).
- Le programme de scellement prendra alors `--entree` le brouillon 15, `--sha-entree` son empreinte, et le rapport de vérification qui la cite.

## Réserves

- Le relevé « la plupart des lettres » vient du message de la mère ; le rapport que j'ai lu ne cite que le saut de ligne et la ponctuation. Je n'ai pas rejoué le tokeniseur.
- La fréquence des deux cas sous les juges réels n'est pas connue avant la course.

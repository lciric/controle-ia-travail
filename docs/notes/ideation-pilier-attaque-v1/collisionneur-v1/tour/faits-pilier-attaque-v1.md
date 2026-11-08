# Faits pour le collisionneur — pilier attaque du programme de contrôle d'IA (v1)

**Statut d'ensemble : RAPPORTÉ au niveau méthode.** Rien ici n'est une consigne. **Aucune recette** : ce document ne décrit *comment* fabriquer aucun comportement de sabotage, aucune évasion, aucune tromperie ; il ne donne que la **structure** du dispositif et des **mesures agrégées** (chacune avec son statut). Les familles d'évasion ne sont nommées **que par leur nombre** ; leur contenu est tenu à l'écart (aveuglement N-054, N-056, R-601, R-602) et n'entre pas dans ce document. Aucun sigle de financeur, aucune valeur de clé. Les chiffres de la littérature extérieure ne sont pas repris (provenance non vérifiée, R-7) : le repère d'état de l'art ci-dessous est qualitatif.

## A. Ce qu'est le pilier attaque (structure, niveau méthode)
Un dispositif de contrôle d'IA ne vaut que contre un attaquant fort et indépendant. Le **pilier attaque** est le bras rouge : il fabrique des **organismes saboteurs scellés** servant d'épreuves pour les **moniteurs boîte blanche** (sondes qui lisent les activations internes, juges, prédicteurs). Pièces de structure, telles qu'énoncées dans le programme (aucune n'est une recette) :
- **Deux sous-bras : aveugle et informé.** L'aveugle conçoit sans voir les moniteurs ; l'informé voit ce qui est public des moniteurs. Séparer les deux mesure ce que l'information sur la défense apporte à l'attaque.
- **Mode tenu à l'écart.** Au moins un mode de sabotage n'entre pas dans la conception des moniteurs, pour mesurer la généralisation à de l'inédit (un mode non chiffré avant la porte G1, N-054).
- **Scellement des recettes.** Les procédés concrets sont scellés au coffre et ne sont relus par aucun agent de la défense ; seuls le niveau méthode et les mesures circulent.
- **Préenregistrement.** Hypothèse, prédiction chiffrée et signée, métrique, seuil, plan d'analyse et liste d'arrêt sont gelés avant toute épreuve décisive ; aucune lecture de résultat avant scellement (R1).
- **Oracle de vérité terrain.** Un oracle indépendant du juge dit si un épisode est réellement un sabotage, pour que « détection réussie » ne soit pas une connivence entre attaque et défense.
- **Aveuglement et séparation des parties.** La conception de l'attaque est faite par une partie séparée de celle qui conçoit les moniteurs (N-054, N-056) ; la défense orchestre sans lire les recettes.

## B. Mesures connues sur les moniteurs actuels (chacune avec son statut)
- **Prédicteur sur les traits du texte : 0,866.** Statut : **mesuré** sur le banc du programme (référence boîte noire sur les traits du texte, N-029). C'est la base à battre.
- **Sondes boîte blanche génériques : au niveau du hasard.** Statut : **mesuré** (banc du programme).
- **Juge de 3 milliards de paramètres : au niveau du hasard.** Statut : **mesuré** (banc du programme).
- **Une sonde lit la consigne** (sa performance tient à la lecture du texte de consigne, non de l'état interne). Statut : **faiblesse connue**, rapportée.
- **Quatre familles d'évasion déjà montées (R-610).** Statut : **construites** (bras rouge). Nommées ici par leur seul nombre ; leur contenu est tenu à l'écart.

## C. Faiblesses connues du dispositif (niveau méthode, à corriger)
- Brèche **W2** du juge (faiblesse rapportée du juge de l'organisme).
- Juge de 3 milliards de paramètres au niveau du hasard (ci-dessus).
- Sonde qui lit la consigne plutôt que l'état interne (ci-dessus).

## D. Repère d'état de l'art (qualitatif, R-7 ; aucun chiffre extérieur repris)
Le champ voisin comprend : les protocoles d'**évaluation du contrôle** (équipes rouge et bleue, un attaquant indépendant éprouve un protocole de surveillance) ; la **surveillance boîte blanche** par sondes linéaires et par juges sur les activations ; le **red-teaming de moniteurs**. La position revendiquée par le programme — un bras d'attaque **scellé, aveugle/informé, avec mode tenu à l'écart et oracle de vérité terrain**, dont la réussite de détection n'est pas un artefact de connivence — est à confronter à ce champ : c'est précisément l'objet du collisionneur (la thèse et chaque piste sont-elles déjà occupées ?). Le détail vérifié du champ vit dans `docs/etat-de-l-art-controle-ia-v1.md` (document du programme) ; ses chiffres ne sont opposables qu'après vérification sur pièce (R-7, R-8).

## E. Cadre de la question posée (rappel)
La question demande, **au niveau méthode seulement** : (1) ce qui, dans la construction du bras rouge, garantit qu'une détection réussie n'est pas une connivence, et quelles garanties manquent encore ; (2) quelles **démonstrations faisables avant l'entretien** montreraient qu'un organisme saboteur conçu à l'écart échappe aux sondes actuelles (chaque démonstration éprouve un moniteur, elle ne fournit pas de procédé) ; (3) quelles extensions et corrections lèveraient les refus probables d'un jury (faisabilité, portée, théorie du changement, impact). Champs de sortie fermés ; **aucun champ « comment faire ».**

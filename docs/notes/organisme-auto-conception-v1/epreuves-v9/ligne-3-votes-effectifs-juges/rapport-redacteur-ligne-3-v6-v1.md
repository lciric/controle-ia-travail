# Rapport du rédacteur — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 6 du préenregistrement et du devis — v1

- Auteur : rédacteur neuf, modèle F. Je n'ai écrit aucune des versions 1 à 5.
- Heure (`date -u`) : 2026-11-19, de 22:11 (première heure relevée) à 22:16. Processeur seul ; aucun appel de modèle, aucune dépense, aucun tirage, aucune écriture dans le dépôt, aucun commit, aucune poussée. Réseau : un `git fetch origin main` et des `git show` seulement.
- Mandat : `mandat-redacteur-ligne-3-v6-v1.md`, `dae0606be4002f6173b3dd2755a58c0b38ff4a719e3b6669e45459c3abfb48b8`, vérifié avant de commencer. Il ne partait qu'au mot de reprise de Lazar : donné, **GO-2026-11-19-81** (« go reprise, go recos », 21:47:18Z), relu sur main au commit `d4449d3273f3820b71e78e9e9adc44674f6ea31b` (`registres/go.md`, `78efe8782883f4de91fa6d06d84d1b93498f8bb3ee5a70e111ffc2d9cd8c1275`).
- **Aucune commande sur un chemin sous `archives-reponses-modeles/`** : ni ouverture, ni empreinte, ni liste, ni taille. Aucune carte ouverte. Aucun outil n'a refusé.
- Pièce de travail, classe C. Ce rapport ne peut pas porter sa propre empreinte.

## Fichiers rendus (bloc-notes seulement)

| fichier | empreinte sha256 |
|---|---|
| `preenregistrement-ligne-3-votes-effectifs-juges-v6.md` | `b040d24cbef61a2a61ca724b097e6857d3465bba4d21f16d2cffc0241220ab94` |
| `devis-ligne-3-etage-payant-v6.md` | `34e87d90f8f3060f7eecd0abdce84721078cea6a97247f909e4cb4d0f2a6c26a` |

À ne pas verser : `outils/appliquer.py` (remplacements exacts, chacun trouvé une fois et une seule dans la source, sinon rien n'est écrit) et ses deux fichiers de remplacements.

**Comment la version 6 est faite.** Par remplacements exacts sur la version 5 (`915fbe4b7ab17d83b9d39b92f21fd4cf4d52394d974b8b5b9c6e9e589d2fed12`) et sur le devis v5 (`43bcb1c887de4f8e683510ceac5871ff4c07464f6dfe396480937567b8761c4f`), jamais par récriture. Différentiel : 16 morceaux pour le préenregistrement (23 points à la table « Différentiel avec la version 5 »), 5 pour le devis (8 points). Tout le reste est égal à l'octet. Aucun calcul neuf ; aucun calcul rejoué.

**Pourquoi un devis v6.** Aucun chiffre ne change. Un renvoi change : le devis nomme le préenregistrement par son fichier (statut, et § 7, point 1). Le mandat demande un devis neuf dans ce cas. La version 6 du devis ne change que des renvois.

## Les quatre corrections du compte rendu du vérificateur arrêté

Source : `verification-ligne-3-v5-v1-compte-rendu-arrete.md`, `9031205f353a970036f87bf41531899d223c154b9edc33219bd04e9938498fb5`.

1. **Repli sur les sept cartes.** Puce « Repli » de la garde de recouvrement remplacée par le texte donné, à la lettre. Phrase de Q3 remplacée par le texte donné. À la liste d'arrêt, « (Q3) » devient « (règle de repli, « Garde de recouvrement ») ». **Écart à la lettre, déclaré** : à la liste d'arrêt, j'ai aussi changé « si la mère refuse l'ouverture par programme » en « si la règle de repli se déclenche », et ajouté « aux mêmes règles de lecture ». Raison : le texte donné laissait à cet endroit un seul des deux déclencheurs, et le mandat demande un seul déclencheur aux trois endroits.
2. **Trou de la condition (3).** Phrase donnée ajoutée à la fin du (3) ; « , messages d'erreur et traces d'exception compris » ajouté à la liste du (4), après « d'un texte de carte ».
3. **Morceau non déclaré de l'en-tête.** Citation de la règle de l'allègement rétablie au texte donné, à la ligne « Auteur ».
4. **Forme des deux bascules** (P5 quater). « entre δ = 0,385 et 0,386 (bascule 0,3853) » ; « entre δ = 0,543 et 0,544 (bascule 0,5438) ». Les six valeurs sont dans la sortie versée `calcul-predictions-ligne-3-v2.json` (`2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724`), relue par programme.

## Les conditions de cloisonnement de la mère

Toutes écrites à « Étage 2 », « Garde de recouvrement, avant scellement » ; rappelées à Q3 ; artefacts à la liste d'arrêt ; plan du code à l'annexe A ; table à « Contre-lecture ».

- **(1) Entrée.** Déjà écrite en version 5 ; gardée.
- **(2) Lecture.** Déjà écrite ; gardée.
- **(3) Sortie.** Déjà écrite ; phrase des rejeux ajoutée (correction 2).
- **(4) Contrôle.** À la contre-lecture du code de la banque, avant la première ouverture du fichier ; « sans ce contrôle passé et écrit, la garde ne tourne pas ». La lecture que la version 5 laissait à confirmer est dite confirmée par la mère (mot vers 16:39Z, par le mandat).
- **(5) Rejeux et sorties.** Puce neuve : au plus cinq rejeux sans le mot de la mère ; messages d'erreur et traces d'exception dans la liste fermée ; rien d'autre ne sort.
- **Repli.** Règle mécanique, deux déclencheurs, sans rien regarder des cartes ; écart déclaré au manifeste et au rapport de la garde ; sept cartes seulement ; mêmes règles de lecture ; sous la condition (5).
- **Empreinte du fichier des cartes** (mandat, point 3). Elle se prend par le code de la banque, jamais par une commande d'agent : écrit au (1), à l'en-tête et à l'annexe A. L'empreinte `ba65c411…` du texte est reprise des versions 1 à 5 ; je ne l'ai pas recalculée.

## Ce que j'ai ajouté, et pourquoi

- **Comment la condition (5) se tient** : ce qui compte pour un rejeu ; journal à ajout seul qui ne repart jamais de zéro ; refus de tourner au sixième rejeu avant d'ouvrir le fichier ; exceptions attrapées, dont la garde n'écrit que le nom de classe et le lieu dans le code. Raison : sans cela, la condition n'est pas contrôlable dans le code au (4).
- **Deux artefacts de plus** à la ligne « recouvrement » de la liste d'arrêt (journal portant déjà cinq rejeux ; exception provoquée sur une carte factice). Raison : règle R5.
- **Deux phrases à la fin de la puce « Repli »** : le compte des rejeux continue sous le repli ; aucun repli hors des deux déclencheurs (un « non conforme » sur un autre point se corrige dans le code, contre-lu de nouveau). Raison : le mandat met le repli sous la condition (5) ; et la version 5 ouvrait le repli dès qu'une condition « ne peut pas être tenue », ce que le texte donné retire sans dire ce qui se passe alors.
- **La vérification de la version 6 porte aussi sur le différentiel de la version 5 avec la version 4.** Raison : la vérification de la version 5 n'a pas été écrite ; son compte rendu n'est pas scellable.
- **Interdit à écrire en tête du mandat du vérificateur**, dit à « Contre-lecture ».
- Le renvoi à GO-2026-11-19-81 et la relecture du registre.

## Écarts

- L'écart à la lettre de la correction 1, à la liste d'arrêt (ci-dessus).
- L'heure de début n'a pas été relevée par `date -u` au tout premier geste : la première heure relevée est 22:11.
- Aucun autre.

## Deux lectures à confirmer par la mère

1. **Ce qui compte pour un rejeu.** J'ai écrit : le premier passage n'est pas compté ; toute exécution suivante qui ouvre le fichier des cartes l'est, quelle qu'en soit la cause, repli compris. Soit six ouvertures au plus sans le mot de la mère. Si la mère veut cinq ouvertures en tout, c'est une phrase à changer au (5).
2. **« L'empreinte se prend par le code de la banque, à sa contre-lecture ».** J'ai écrit : la valeur attendue est une constante du code, que le contre-lecteur du code compare au texte ; la valeur calculée par le programme est au rapport de la garde, et tout texte la reprend de là. Aucun agent ne la calcule.

## Ce que je n'ai pas pu faire, ce qui reste ouvert

- Les mots de la mère (vers 15:39Z, 16:39Z et 16:44Z) ne sont écrits que dans le mandat : je les cite par lui.
- Des deux contrôles que le vérificateur arrêté n'avait pas faits, j'en ai fait un et demi : `registres/go.md` au commit `2ec5da6c…` rend bien `5750c7fabeb66968e340f8dcc6aeec5ffe1a676a5415d7f726b3fb4b99fefe32` ; la tête de main à mon heure est `5ee19a44a7bab36af9efc26375ac1133c6563ede` (`registres/go.md`, `1570ae2b65621e490b1a07dae69b9829320896410944b24c67bba9e1c20c5faa`), non celle de l'heure de la version 5. Les lignes GO-2026-11-19-55 à -77 sont égales à l'octet aux trois commits ; la ligne -81 est égale aux deux qui la portent. À refaire par le vérificateur.
- Empreintes recalculées : les pièces du dossier que la version 6 cite, les calculs versés et leurs sorties, `registres/go.md` aux trois commits. Les autres sont reprises de la version 5.
- La vérification de la version 4 est lue ; je n'ai rejoué aucun calcul.
- Les fichiers compagnons `.sha256` ne sont pas écrits : la session les pose au versement.
- La version 6 doit être vérifiée par un agent neuf du modèle O, qui ne lance aucune commande sous `archives-reponses-modeles/`, avant scellement.

## À dire à Lazar (information, portée par la mère)

Inchangé depuis la version 5 : si la prédiction ajoutée à P10 se vérifie, l'étage payant de 25 USD ne pourra rendre que « non », « non concluant » ou des mesures ; jamais « oui ».

## Décisions neuves pour Lazar

Aucune. Rien dans la version 6 ne change une hypothèse, une revendication, une dépense ni une décision prise. Les deux lectures à confirmer sont du cloisonnement : elles reviennent à la mère.

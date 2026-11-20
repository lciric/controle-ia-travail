# Rapport du développeur — programme des seuls noms de clés de `contenu` hors des dix champs — v1

Pièce de travail (classe C), 2026-11-20, en réponse au mandat `mandat-developpeur-noms-cles-contenu-v1.md`
(`df0df0c2b19e32337d84a3aeaf9f5ffbdb17189fc16ca663079fbeccd1ff8332`, vérifiée contre son compagnon avant tout autre geste).

**Verdict : le programme est écrit et essayé sur des fichiers synthétiques ; 39 essais passent, aucun n'échoue. Il n'est pas joué.**
Aucun geste sur le vrai fichier des cartes ni sous `archives-reponses-modeles/` ; aucune écriture dans le dépôt ; aucune dépense.

## Fichiers et empreintes

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu/`

| Fichier | Empreinte SHA-256 |
|---|---|
| `noms_cles_contenu_hors_champs_v1.py` | `26eeaa798e14c716bbe4bd0c323e797e60470459d9a13b804ccacb07ea121120` |
| `essais_noms_cles_contenu_hors_champs_v1.py` | `a3089f6b24679a0a493987711dd0d9df64e568745014711515a15fbdc9ce384f` |
| `rapport-developpeur-noms-cles-contenu-v1.md` | son compagnon `.sha256` |

Chaque fichier a son compagnon `F.sha256` (`env -C DOSSIER sha256sum F`). Fichiers synthétiques des essais :
`fichiers-essais-v1/` sous le même dossier. Mutants de contrôle (hors du rendu) :
`/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu-mutants/`.

Pièces lues : le masque scellé `masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`,
recalculée sur disque), dont `valider_configuration` et `extraire_contenus` sont reproduites à la lettre jusqu'aux clés de `contenu`.

## Ce que fait le programme

- Arguments `--fiches`, `--configuration`, `--sortie`, tous requis, aucun défaut, abréviations refusées ; aucune option d'empreinte.
- Refus d'abord si la sortie ou son compagnon existe, ou si le dossier de la sortie est absent (rien n'est lu).
- Octets de la configuration, puis octets des cartes ; les deux empreintes sont comparées aux constantes gelées
  **avant tout décodage** (ni la configuration ni les cartes ne sont décodées si l'une diffère) ; la configuration est
  ensuite décodée et validée comme le masque la valide, puis les cartes.
- Chemin du masque : champs = `configuration["champs"]` ; cartes de `configuration["hors_choix"]` non ouvertes ; seul
  accès `fiches[identifiant]["contenu"]`, dont seules les clés sont parcourues. Mêmes refus de structure que le masque.
- Sortie : JSON à trois champs (`cles_hors_champs` triée par nom puis par compte, `nombre_de_cartes`, `empreintes`),
  postcondition vérifiée avant écriture, écriture en mode exclusif, puis compagnon. À l'écran : `FAIT`, ou `REFUS : motif`
  (code 2) ; aucun motif ne porte de nom, d'identifiant ni de valeur.

## Choix d'interprétation et écarts (tous mineurs, à trancher par la mère si elle le veut)

1. « Avant tout décodage » lu au sens fort : les deux empreintes sont vérifiées avant le premier décodage ; l'ordre
   « configuration puis cartes » tient à chaque étape (lecture des octets, puis décodage).
2. `nombre_de_cartes` = nombre de cartes **ouvertes**, c'est-à-dire hors de `hors_choix`, comme le masque ; une clé de
   trop sur une carte hors du choix n'est pas comptée (le masque ne la verrait pas).
3. Refus si aucune carte n'est ouverte (toutes hors du choix) : une liste vide n'y dirait pas « cas sain » (R5).
4. Garde : « saut de ligne » pris au sens de `str.splitlines` (`\n`, `\r`, `\v`, `\f`, `\x1c` à `\x1e`, `\x85`, U+2028,
   U+2029) ; deux noms longs de même longueur gardent deux entrées et deux comptes, sous le même texte de remplacement.
5. Sortie écrite en JSON échappé en ASCII : un nom accentué s'écrit `é` dans le fichier et redevient exact une fois
   le JSON décodé ; aucun caractère de contrôle ne s'imprime de travers.
6. Une erreur imprévue rend le code 2 avec son seul type, jamais son message (qui pourrait citer un nom ou un octet) ;
   le message d'une erreur de décodage n'est pas rapporté non plus.
7. Non reproduits, car hors du chemin des noms de clés : le contrôle du masque « carte hors du choix inconnue du fichier »
   (après sa boucle), « champ de la configuration absent d'une carte » et « champ qui n'est pas un texte » (ce dernier
   lirait le type des valeurs). Aucun contrôle « exactement dix champs » : la liste est prise telle que la configuration
   la donne, comme le masque la prend.
8. **Réserve** : la configuration A n'est ni sur disque à
   `/home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json`,
   ni dans `HEAD` du dépôt de cette session (vérifié par chemin complet et par `git show`, sans liste). Le programme ne
   l'a jamais lue ; tant qu'elle n'est pas à ce chemin, le jeu refusera par « configuration : fichier absent ».

## Essais

Commande : `env -C /tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu python3 -B -m pytest -q -p no:cacheprovider essais_noms_cles_contenu_hors_champs_v1.py`
(Python 3.13.18, pytest 9.1.1) — **39 passés, 0 échoué**.

- Forme synthétique conforme : le masque scellé (chargé depuis ses octets, empreinte vérifiée, sans fichier compilé)
  accepte la configuration synthétique à dix champs et les cartes saines, et refuse la carte à une clé de plus par
  « champ(s) hors de la configuration (1) » ; la validation de la configuration rend le même motif que le masque sur
  onze configurations (deux saines, neuf fautives).
- Cas sain (liste vide) ; une clé de plus sur une carte ; deux clés de plus sur 1 et 3 cartes (tri par nom).
- Garde : 64 caractères écrit tel quel, 65 remplacé ; noms à `\n`, `\r`, U+2028 remplacés ; nom long semé de la marque
  des valeurs remplacé ; deux noms de 70 caractères comptés à part.
- Empreinte fausse de la configuration, puis des cartes ; empreinte gelée mal formée ; empreintes comparées avant tout
  décodage (journal des appels) ; décodage illisible sans l'octet fautif.
- Sortie existante, compagnon seul existant (rien n'est lu, rien n'est écrasé) ; dossier de sortie absent.
- Ordre « configuration puis cartes » (journal : octets, octets, décodage, décodage, puis clés avec les champs de la
  configuration) ; configuration refusée : cartes jamais décodées ; configuration absente : cartes jamais lues.
- Aucune valeur ni identifiant dans la sortie, son compagnon ou l'écran (valeurs de toute espèce JSON et identifiants
  semés de marques repérables, aussi dans `meta`, `empreinte` et les cartes hors du choix) ; cartes hors du choix non
  ouvertes, comme le masque ; six refus de structure ; erreur imprévue au message semé, non rapporté.
- Ligne de commande : n'accepte que les constantes (les fichiers synthétiques y sont refusés par l'empreinte de la
  configuration) ; `main` passe exactement les constantes ; aucun argument par défaut ; empreinte en argument refusée ;
  abréviation refusée.

Contrôle des essais (R4, 39 sur 39 du premier coup) : trois mutants, chacun tué — cartes hors du choix ouvertes
(3 essais échouent), garde à 65 (1), configuration décodée avant l'empreinte des cartes (2).

## Commande unique de jeu (attend le mot de Lazar)

Vérifier d'abord le programme : `env -C /tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu sha256sum -c noms_cles_contenu_hors_champs_v1.py.sha256`, puis :

```
env -C /home/user/controle-ia-travail python3 -B /tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu/noms_cles_contenu_hors_champs_v1.py --fiches CHEMIN_DU_FICHIER_DES_CARTES --configuration prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json --sortie docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/noms-cles-contenu-hors-champs-v1.json
```

`CHEMIN_DU_FICHIER_DES_CARTES` reste à remplir par la mère : je ne connais pas ce chemin et n'avais pas à y toucher.
Le chemin de sortie est une proposition (la sortie ne porte que des noms de clés gardés et des comptes) ; si le
bloc-notes est vidé, copier d'abord le programme ailleurs et revérifier son empreinte.

Aucun refus de permission, de classifieur ni de garde rencontré.

— développeur, modèle O

# Lancement des développeurs du véhicule NA-1, lots 6 et 10 a — v1

**EN ATTENTE — aucun développeur lancé.** Lancement suspendu à 16:13Z par l'arrêt sur refus d'un classifieur de sûreté (concepteur de l'additif v3 ; message `registres/essaim/vers-mere/2026-11-21-1613-organisme.md`) ; ne part que sur le mot de la mère.

Pièce de travail (classe C), session du compte organisme (session fille de la mère), 2026-11-21 vers 16:12Z. Sur le point 2 du message de la mère `registres/essaim/vers-organisme/2026-11-21-1448-mere.md` (sur `origin/main`) : « Les lots 6 et 10 a partent sur le lot 4 v1 », après les errata 1 versés (commit `e33f5f29`). Où cette note diffère du mandat ou de l'erratum, elle prime, **sur ces seuls points** :

1. **Racine** : partout où le mandat ou l'erratum écrit `/home/user/controle-ia-travail-organisme/`, lis `/home/user/controle-ia-travail/` (branche `lot/compte-organisme-v1`, déjà extraite). La racine d'origine n'existe pas dans ce conteneur.
2. **Ton dossier** : lot 6, `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/dev-vehicule-na-lot-6/` ; lot 10 a, `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/dev-vehicule-na-lot-10-a/` ; au lieu du dossier écrit dans le mandat, qui appartient à une session fermée.
3. **Copie aux jalons** : vers `/home/user/dossiers-developpeurs-vehicule-na-v1/lot-6/` et `/home/user/dossiers-developpeurs-vehicule-na-v1/lot-10-a/`, comme l'erratum le dit.

| pièce | chemin | empreinte |
|---|---|---|
| mandat du lot 6 | `docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-6-v1.md` | `b59766267b5b285ad12395a86bb388fc12af48ebe6ded630a3062c2bac6f6b1d` |
| erratum 1 du lot 6, versé | `docs/notes/ideation-nouvelles-attaques-v1/erratum-1-mandat-developpeur-vehicule-na-lot-6-v1.md` | `1b08d873f6385c6e4e7fe777c1a1f68255083570264b51ae1061b0b5054a667e` |
| mandat du lot 10 a | `docs/notes/ideation-nouvelles-attaques-v1/mandat-developpeur-vehicule-na-lot-10-a-v1.md` | `9f9f20f9bc7fd9476d49445b5509cffee255158c2de23455ad57d46f8ae79795` |
| erratum 1 du lot 10 a, versé | `docs/notes/ideation-nouvelles-attaques-v1/erratum-1-mandat-developpeur-vehicule-na-lot-10-a-v1.md` | `61674e25f8ad90179ed1e0abeb86264369bd6ca9415f55c9c1161a4e60cb122c` |

Code par un développeur neuf du modèle O ; vérification par un vérificateur du modèle S. Aucun appel à un fournisseur, aucune dépense, aucune clé ; données factices seules.

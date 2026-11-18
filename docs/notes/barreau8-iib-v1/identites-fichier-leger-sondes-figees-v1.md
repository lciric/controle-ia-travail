# Identités du fichier léger des sondes figées du premier test — v1

Extraction par programme, identités seulement (aucune mesure).

## Fichier

| point | valeur |
|---|---|
| branche | suivi sur `main` (commit d'ajout `08866254e`) et sur la branche courante `claude/affectionate-bardeen-j7kddp` |
| chemin | `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz` (17 682 551 octets) |
| empreinte entière | `701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60` |
| compagnon `.sha256` | égal à l'empreinte recalculée |
| texte scellé `prereg/T0.7-sondes-v0-v1.md` | le texte cite l'empreinte entière (2 fois) et le préfixe `701f73bd…` (13 fois) ; préfixe `701f73bd` et suffixe `4e60` concordent avec l'empreinte recalculée |
| empreinte d'ensemble des tableaux (clés triées, forme, type, octets) | `d60ea4bc4ae1ea67d33ef5852cb5fa2df4b6fca6f0d5862c0821e4f660080ce1` |

## Clés et formes (455 clés)

`s*_w` (4096,) float64 ×418 ; `s*_mu` (4096,) ×6 ; `s*_s` (4096,) ×6 ; `s*_q` (4096,) ×6 ; `s*_W` (16, 4096) ×6 ; `s*_c` (16,) ×6 ; `s*_v` (16,) ×6 ; `index` (137693,) uint8 ×1. Le tableau `index` (JSON) donne les noms : 424 sondes (24 sondes nommées, 400 directions de plancher) ; clés de `meta` : `complet`, `planchers`, `principales` (valeurs non lues).

## Les deux sondes principales

| nom | classe | famille | couche | clé du vecteur | forme | empreinte du vecteur (SHA-256 des octets) | empreinte de la sonde dans l'`index` |
|---|---|---|---|---|---|---|---|
| `tromperie-difference_moyennes-c15` | SondeLineaireJetons | différence de moyennes | 15 | `s1_w` | (4096,) float64 | `dabd4336da81bdea7cf7a4222f3d0db8ef1ff0246bbca6346f11d1feedd4f627` | `edf5e22ac3e0f0e13ad4a05129724f4406015b05fd06832cd50543bddd180705` |
| `enjeux-lineaire-c15` | SondeLineaireJetons | linéaire | 15 | `s16_w` | (4096,) float64 | `30d432f845602f0990f3335c1937bebf831aed7161c386882b5cbf938ebe768e` | `88f4af7c8aa90c023a8999308d364407b021e5bea1111d445fc07f6a19da4229` |

Empreinte du vecteur calculée comme pour `s4_w` de la première note : SHA-256 des octets du tableau contigu.

## Non trouvé / hors mandat

Rien de non trouvé. Lectures hors mandat : liste des fichiers suivis nommés « legeres » (dont deux copies d'essai factice sous `docs/notes/lentilles-sondes-p3-v1/`, non ouvertes) ; noms des sondes contenant `tromperie` ou `enjeux` dans l'`index`. Aucun refus.

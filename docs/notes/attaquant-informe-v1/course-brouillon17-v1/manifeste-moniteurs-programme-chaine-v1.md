# Programme du manifeste des moniteurs (champ n° 16) : chaîne de contre-lecture et erratum 1 de la v4

- Note de classe C, écrite par la session fille de l'attaquant informé le 22 novembre 2026, d'après des rapports rendus dans la session et non versés comme fichiers. Le programme a été écrit sur le mot de la mère (13:39Z) : « go pour le programme du manifeste, écrit par Opus ».
- Version d'usage : **`src/controle_ia/manifeste_moniteurs_v4.py`**, 17 tests (`tests/test_manifeste_moniteurs_v4.py`). Les v1 à v3 restent inchangées (R12).

| Version | Contre-lecture (Sonnet, le même contre-lecteur pour toutes) | Principaux défauts |
|---|---|---|
| v1 | « à reprendre » : 2 bloquants, 4 majeurs, 5 mineurs | banc vide pris pour sain ; trace d'erreur sur un nom non UTF-8 ; liens et sous-modules sautés ; fichiers triviaux ; couverture des branches ; limites non déclarées |
| v2 | « conforme après corrections » : 2 majeurs, 2 mineurs | liens de dossier non suivis ; seuil de 64 octets qui écartait les petits moniteurs |
| v3 | « conforme après corrections » : 2 mineurs | sortie du banc non bornée ni rapportée ; pas de test de lien sortant |
| v4 | **« conforme »** | 2 mineurs, sans effet sur le verdict, déclarés ci-dessous |

## Erratum 1 de la v4 : limites déclarées, lues avec sa docstring
1. Un `/proc`, `/sys` ou `/dev` monté dans le banc par un point de montage ou un montage lié, sans lien symbolique, n'est pas détecté : le contrôle porte sur le chemin réel, non sur le système de fichiers (`st_dev`). L'épreuve de la garde 1 du banc établit la liste des montages avant la pose.
2. La borne `--max-fichiers` compte les fichiers et non les dossiers. Un arbre de très nombreux dossiers vides n'est pas borné.

## Ce qui reste pour remplir le champ n° 16
- Le **périmètre** (fichier JSON, version 2), écrit par la mère : ni l'auteur de la course ni l'opérateur ne le choisissent.
- Le **premier manifeste réel avant la répétition** et le manifeste de la course le jour de la pose, établis par la mère avec ce programme.

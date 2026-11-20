# Renvois des chiffres des notes du développeur (R6) — v1

Complète `notes-developpement-v1.md` (`3cfc4a6d63705639848703eaa5dd383c8c256bb454d57f2320c9548b53d88441`), scellée avant le versement des outils.
Code mesuré : commit `59ceab1e` de la branche `claude/lentilles-bbis-developpeur-v1`.

| chiffres des notes | source | empreinte |
|---|---|---|
| § 5 : 51,5 s, 6,04 Go, comptes de calibration du banc, 242 et 232 témoins sur 4 000, 5,15 % et 4,90 %, comptes attendus et bornes | `outils/sortie-banc-taille-reelle-v1.txt` (rejouée : 51,6 s et 6,05 Go ; mêmes comptes), produite par `outils/banc-taille-reelle-v1.py` | fdf634c606a2f76ef69efe752e58a5d64477e32876066177199025ce56f72ec5 ; be22ed7fdbdb90a2ab98b1db73e1982a86bacc5df949726bd3ae2b840843d0c1 |
| § 6 : quarante altérations, trente-neuf vues | `outils/sortie-essai-des-essais-v1.txt`, produite par `outils/essai-des-essais-v1.py` | 7b9e4912021030b38bb243dd4bcf083539810e4487b8d299e604c032bb558d73 ; 509cdb3c0085fbbc519b9b1a998775cc4f4aa3f784f8459083129d294e44e28f |
| § 1 : 258 essais verts | `sortie-essais-v1.txt` | 1dcb2f941d6b9d69253c71ce69af92e5bf94a93924f79da9e3e3544d4c309b28 |
| § 8 : empreintes du code | `empreintes-code-v1.txt` | 6de20bce387fdad77219f754bac2c85a6cc2b70d362678e8a9b102f6aa767782 |

Le banc n'emploie que des matrices aléatoires (aucun poids, aucune sonde, aucune lentille réelle). Les sorties du banc ne sont pas un
résultat du programme et n'entrent dans aucune mesure.

# Procédure du repli de la relance de la confirmation du témoin de Bailey — v2 (19 novembre 2026)

v2 = v1 (`procedure-repli-relance-bailey-v1.md`, `ccbce4be…`, gardée telle quelle, R12), modifiée par le mot direct de
Lazar du 19 novembre, vers 08:47Z : « avant toute destruction, inventaire et versement scellé de tout ce qui reste sur la
machine » ; « Poste et instance Vast ». Note `registres/passations/2026-11-19-0937-bailey-inventaire-avant-destruction.md`.

**Déclenchement** (inchangé, mot direct de Lazar du 18 novembre, « au bon moment pour sauver les données ») :
- crédit Vast au plus 2,6 USD, ou sous 2,2 USD en toute heure ;
- ou instance 61170458 qui n'est plus en marche **sans** marque de fin du poste v14 (après une fin normale, ce n'est pas
  un déclencheur) ;
- si une recharge aboutit avant, la course continue.

**Ce qui change par rapport à la v1, § 2 (B′).**
1. Relevé de décision : identique à la v1, § 2.1. Il faut en plus que le poste d'inventaire de l'instance (Hetzner
   176778587) soit vivant : sa dernière passe a été poussée il y a moins de 25 min.
2. **Le poste v14 (176575468) est éteint, non détruit**, par l'API Hetzner (`POST /v1/servers/176575468/actions/poweroff`,
   par identifiant). L'extinction arrête la conduite et son veilleur ; le disque est gardé pour son propre inventaire.
   Attendre le succès de l'action, puis relire le statut « off ».
3. **Marque** `arret-conduite-v16-poste-v14.json` : mêmes champs que dans la v1, avec `serveur_hetzner` 176575468,
   `mode` « extinction (poweroff), disque gardé » et `absence_prouvee` remplacé par `eteint_prouve` (statut « off » relu,
   avec son heure). Attention : la garde du poste de reprise v7 ne teste que la présence non vide de la marque ; la
   session vérifie elle-même ses champs avant de créer le poste v7.
4. **Inventaire de l'instance avant sa destruction** : attendre la poussée d'une passe du poste d'inventaire
   **postérieure à l'extinction du poste v14** (au plus 20 min). Pendant cette attente, le run continue sur l'instance :
   seul le crédit borne l'attente. Si le crédit passe sous 2,2 USD, la reprise part sans attendre davantage.
5. Relevé du § 2.5 ; données de démarrage v7 ; création du poste de reprise v7 (pièces scellées au commit `978f1b05`),
   qui arrête le run par PID, reconstitue l'état, transfère et détruit l'instance. Surveillance et fin : comme dans la
   v1, § 2.5 et § 2.6 (C1, C2).
6. **Après la destruction de l'instance** : le poste d'inventaire constate son absence, scelle et pose sa marque.
7. **Aucune destruction de serveur Hetzner** (poste v14, poste d'inventaire, poste de reprise v7) avant l'inventaire et
   le versement scellé de ce qui reste sur lui. Pour le poste v14 : instantané de son disque, puis serveur neuf tiré de
   l'instantané qui inventorie et verse (pièces à écrire et contre-lire). Pour les postes d'inventaire et de reprise :
   leur journal versé par eux-mêmes, ou le même chemin par instantané.

**Fin normale de la course (sans repli).** La conduite transfère, puis détruit l'instance ; le poste v14 pose
`poste-fini-v14.json`. Le poste d'inventaire constate l'absence de l'instance, scelle et pose sa marque. Le poste v14
n'est détruit qu'après son inventaire par instantané (point 7).

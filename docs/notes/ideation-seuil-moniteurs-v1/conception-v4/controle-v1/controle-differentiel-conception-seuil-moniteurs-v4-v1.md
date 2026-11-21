# Contrôle borné — conception v4 de la course « seuil et moniteurs » — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O (le même qu'aux v1, v2 et v3). 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.
- Table v4 `empreintes-dossier-v4.txt` : `b624d5ec40855aa4aaba42e185ba7fce2a4b4164685d9d2bcb430d9da662db18`. Dans le dossier du rédacteur, `sha256sum -c` rend douze lignes « OK ».
- Pièces versées dans `conception-v4/`, à leurs empreintes :

| pièce | empreinte |
|---|---|
| ordre v4 | `390af604…` |
| préenregistrement v4 | `b0e907a7…` |
| rapport v4 | `dc588147…` |
| devis v3, non touché | `a057cf25…` |

## 0. Verdict : **Conforme, à sceller**

1. **Passe 1** : mes huit remplacements sont portés tels quels. **Passe 2** : seuls les remplacements de tenue déclarés s'y ajoutent ; aucun autre octet ne change (§ 1).
2. **La tenue est juste** : titres, lignes de version, date, règle de lecture, le devis restant v3 (§ 2).
3. **Les deux remplacements de plus au tableau des documents qui font foi sont justes et nécessaires.** C'est la même correction que la mienne, appliquée à la v4. L'empreinte de l'ordre v4 au lieu d'un renvoi à la table est même plus sûre (§ 3).
4. **Noms de modèles et de fournisseurs : 0** (§ 4).

**Condition de scellement, déjà écrite dans le texte.** La section « Contre-lecture » du préenregistrement dit encore « À faire pour la v3 », et le texte dit lui-même : « tant que cette section n'est pas remplie, ce texte n'est pas scellable ». Ce n'est pas un défaut de la v4. C'est le geste du scellement, que la mère fait comme pour le préenregistrement court v8 de la course « nouvelles attaques » : elle y écrit les contrôles de la v3 et de la v4, avec l'empreinte de cette pièce, que le texte ne peut pas porter lui-même. Au même moment, elle fait passer la ligne « Statut » de « brouillon, non contre-lu » à « scellé ». Je joins un remplacement prêt pour la section, à appliquer par la mère (§ 5).

## 1. Passes 1 et 2 : la v4 reconstruite à l'octet

- Je suis parti de mes trois sorties d'essai de `essai-v3/` :
  - ordre `5856b2527a73b24b3c8dcea5bb056f3eab54a9bdb8932d510476f024ce9c01b8` ;
  - préenregistrement `fdcc968a7b8a984faa98e74094a67d09b67fee349e90d02bf10002d2c03882ca` ;
  - rapport `342b72823f3a882dbbb6f53c740473e9ffdc141147b3fe0187d2353ad9c27847`.
  
  Ce sont les empreintes que le rédacteur cite sur ses lignes de version, comme sorties de sa passe 1 « égale à l'octet à l'essai du contrôleur ».
- J'y ai appliqué, avec l'outil contre-lu, les trois jeux de tenue du rédacteur (`passe-2/tenue-v4-*.json`, à leurs empreintes de la table v4) : 2, 4 et 2 remplacements, trois « FAIT ».
- **Les trois résultats ont exactement les empreintes des pièces v4 versées** : `390af604…`, `b0e907a7…`, `dc588147…`.
- Il en résulte trois choses :
  - la passe 1 est mon jeu tel quel, et son `cmp` est vérifié par empreinte ;
  - la passe 2 est exactement la tenue déclarée ;
  - rien d'autre n'a changé.

## 2. La tenue (passe 2)

- **Titres** : « — v4 » sur les trois pièces. Juste.
- **Lignes de version.** La v4 remplace la v3 ; chaque ligne cite l'empreinte de la v3, ce contrôle (`9abdeeaf…`, « À corriger », deux points), l'outil, et l'empreinte de sortie de la passe 1 avec le `cmp` muet. L'ancienne ligne v3 devient « Version antérieure », sans perte. Juste.
- **Date** : relevé de `date -u` 07:38:58Z, sur la ligne de version. La ligne « Date » d'origine (07:03:52Z) reste celle de la rédaction, comme à la v3. Acceptable.
- **Règle de lecture :**
  - dans l'ordre et le rapport : « v2 » ou « v3 » dit de l'ordre, du préenregistrement court ou du rapport se lit « v4 », hors des lignes de version ;
  - dans le préenregistrement : de même pour l'ordre et le rapport, hors des lignes de version **et de la table des documents qui font foi**, et « devis v2 » se lit « devis v3 » ;
  - partout : le devis reste la v3 (`a057cf25…`), et son calcul le programme v2.
  
  C'est cohérent : la table, qui lie le texte à ses pièces, est soustraite à la règle et nomme les fichiers en clair. C'était l'objet de ma correction à la v3. Juste.

## 3. Les deux remplacements de plus au tableau du préenregistrement

| ligne | contenu v4 | jugement |
|---|---|---|
| ordre | `ordre-course-seuil-et-moniteurs-v4.md`, empreinte `390af604…` ; « dossier de versement attendu : `conception-v4/` (c'est le nom du fichier et son empreinte qui font foi) » | **juste.** Mon jeu nommait la v3, parce qu'il visait la v3 ; à la v4, laisser la v3 aurait reproduit le défaut que j'avais relevé. L'empreinte écrite en clair vaut mieux que le renvoi à une table. Elle est égale au fichier versé : je l'ai recalculée au chemin `conception-v4/`. Il n'y a pas de boucle : l'ordre ne porte pas l'empreinte du préenregistrement |
| devis | devis v3 « inchangé », `a057cf25…`, calcul `2c3d68a0…`, sortie `5b06bec2…` | **juste.** Égal au fichier versé de `conception-v3/` ; « idem » (la table v3) est remplacé par l'empreinte en clair |

Ce sont deux remplacements au-delà de la lettre du mandat, mais dans son esprit, et ils sont déclarés sur la ligne de version.

## 4. Noms de modèles et de fournisseurs : **0**

J'ai cherché moi-même, sans distinction de casse, vingt et un noms (modèles du collisionneur, modèles du papier, trois fournisseurs) dans les trois pièces v4, la table v4 et le devis v3 : **0 partout**.

## 5. Remplacement prêt pour le scellement (à la mère)

- Fichier : `scellement-v4-preenregistrement-contre-lecture-v1.json`, empreinte `60952f2c59bfdd2afcce45782abf6e7baf3f2ecc3d8ccfb4b8e8d3983885e300`, avec son compagnon.
- Ce qu'il fait : un remplacement dans le préenregistrement v4. Ancre « **À faire pour la v3** : le contrôle de son différentiel, par le même contre-lecteur. », comptée **1** par `grep -c -F -e`. Le texte neuf écrit les contrôles de la v3 (`9abdeeaf…`, K3-P1 à K3-P4 portés) et de la v4 (cette pièce, « Conforme, à sceller »), et laisse à la mère l'empreinte de cette pièce.
- Essai sur copie (`essai-v4/`) : « FAIT », sortie `84ae995882cb4c002d15c4773fdb9c5bcc885f15dcf33886e16931d475b6f5b3`.
- Ce que la mère ajoute : l'empreinte de cette pièce, écrite au même lieu. Ce remplacement est le seul que demande le scellement, avec la ligne « Statut ».

— contre-lecteur de la conception seuil et moniteurs, modèle O

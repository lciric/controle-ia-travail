# Contre-lecture du lanceur de la première passe, version 7 (garde du fichier d'arrêt déjà présent) — v1

Rendu d'un contre-lecteur neuf, sur Opus 5.5, versé tel quel par la session des lentilles le 2026-11-21. Le contre-lecteur des versions 4 à 6 s'était arrêté sans commencer, faute de mémoire de travail.
- Mandat : `mandats/mandat-contre-lecteur-lanceur-v7-v1.md` (`2b063c05…`), commit `c4a78312`.
- Code jugé : commit `cc7f4576`, branche `claude/brave-galileo-jhp684`.

## 1. Verdict

**Conforme, aucun écart bloquant.** `lanceur_v7` est `lanceur_v6` plus la seule garde accordée par GO-2026-11-21-06 :
- la garde `exiger_aucun_fichier_d_arret` refuse de partir si un `arret.json` existe déjà ;
- aucune ligne de calcul ne change ;
- le cloisonnement et les fermetures de la version 6 restent intacts ;
- les mots fixes sont inchangés.

Chaque garde est éprouvée sur un cas sain et sur un artefact. Quatre corrections non bloquantes, de forme, et quatre nœuds pour Lazar sur des chemins voisins.

## 2. Empreintes

Toutes conformes :
- `lanceur_v7.py` : `a5d6fc7b…`
- `lanceur_v6.py` : `e0517259…`
- essais : `bc35c890…`, `c88cab55…`, `9ed9e7ca…`
- `empreintes-code-v7.txt` : `a2b5c098…`, 34 fichiers sur 34 conformes contre le disque
- contre-lectures précédentes : `d821cf66…`, `23f466a8…`
- addendum : `7c738708…`
- texte de lecture v1 : `ca5066d7…`

`statistiques_v3.py` est inchangé. Les compagnons sont conformes. Le commit `cc7f4576` ne fait qu'ajouter des fichiers.

## 3. Décompte des essais

- Paquet entier : **2 052 réussis** en 1 146,58 s, aucun échec.
- Altérations de la garde :
  - le témoin est sain : 61 réussis, 25 écartés ;
  - 9 altérations sur 10 sont vues ;
  - la dixième est une altération équivalente.

## 4. Points

**Point 1 — Empreintes.** Voir le § 2.

**Point 2 — Fabrique.** Rejouée, elle rend `lanceur_v7` et les neuf copies d'essais à l'octet près. La différence avec `lanceur_v6` se limite à :
- l'en-tête ;
- `MODULES` ;
- les deux fonctions de la garde ;
- l'appel de la garde et une phrase de docstring.

Aucune ligne de calcul ne change.

**Point 3 — La garde.**
- **Place** : c'est la première instruction de `calculer`, hors de l'enveloppe. Elle passe avant la fiche du code, tout registre, toute requête, tout chargement et `etat["parti"]`.
- **Chemin gardé** : `<sortie>/versement/<run>/calcul-interrompu/arret.json`, le même que celui où l'enveloppe écrit.
- **Ni écriture ni suppression** : vérifié par `lstat`.
- **Cas qui font refuser** : fichier vide, fichier plein, lien cassé, lien en boucle, lien vers un dossier, dossier au nom `arret.json`.
- **Relance après un premier arrêt** (égalité d'une direction lue, égalité des directions nulles, arrêt ordinaire) : la seconde course est refusée avec le code 3. Seul le chemin sort, et aucune valeur témoin du premier message.
- **Nature** : la garde est un `Arret` ordinaire. Ses mots neufs, qui ne portent qu'une existence, sont permis.

**Point 4 — Copies d'essais au contenu changé.**
- `…_lanceur_v7_v1.py` : l'accord est légitime, la garde étant neutralisée pour simuler un fichier apparu après elle. La défense du versement reste éprouvée : l'altération qui la retire fait tomber 4 essais.
- `…_lanceur_v7_interruptions_v1.py` : les deux essais retirés restent joués dans le fichier de la version 6. Aucune épreuve n'est perdue. La constante `OUTIL` et quatre imports sont morts, sans effet.

**Point 5 — Les cinq nœuds du développeur.**
1. Dossier `calcul-interrompu` sans `arret.json` : hors du champ. Le message n'est pas perdu, c'est vérifié.
2. Dossier `travail-arret` : hors du champ, même vérification.
3. Sous-commande `montage` : hors du champ par le motif, permise par la lettre. Ne rien garder est conforme (nœud C).
4. `arret.json` apparu après la garde : hors du champ. La défense de la version 6 tient pour les arrêts cloisonnés (voir nœud B).
5. Consigne à l'opérateur : hors du champ du code, et permise.

Le contre-lecteur rejoint la recommandation du développeur : ne rien garder de plus.

**Point 6 — Altérations de la garde.**

| Altération | Résultat |
|---|---|
| Garde appelée après la fiche du code | vue, 8 essais tombent |
| Garde visant un autre chemin | vue, 8 |
| Garde aveugle à un fichier vide | vue, 1 |
| Garde aveugle à un lien cassé | vue, 1 |
| Garde affichant le premier message | vue, 5 |
| Défense du versement retirée | vue, 4 |
| Garde qui crée le dossier de l'arrêt | vue, 1, de biais |
| Garde placée dans la seule ligne de commande | vue, 2 |
| Garde levant un arrêt cloisonné | vue, 8 |
| Garde déplacée dans le `try` de l'enveloppe | non vue, altération équivalente |

## 5. Corrections

**Bloquantes** : aucune.

**Non bloquantes** :
1. Le cas du lien cassé ne compare pas l'état du disque avant et après ; il le faudrait, par `lstat` et `readlink`.
2. Des docstrings sont périmées dans `…_lanceur_v7_interruptions_v1.py` et dans `_copie_jetable` de `…_lanceur_v7_v1.py`. Une constante et des imports sont morts. À noter à la prochaine version.
3. L'outil d'essai des essais de la version 7 est nommé `essai-des-essais-v6.py`. C'est un écart de nommage au regard de R12.
4. Aucun essai du cas sain ne vérifie que la garde n'écrit rien quand le calcul part.

## 6. Nœuds pour Lazar

- **A. Obstacle sur le chemin du fichier d'arrêt.**
  - Cas : `calcul-interrompu` ou `versement/<run>` est un fichier ou un lien cassé.
  - La garde laisse partir. Le message d'un arrêt cloisonné est alors perdu, sans fuite.
  - Le cas est artificiel.
  - Options : s'en tenir à la lettre, ou étendre la garde par une règle neuve.
- **B. Arrêt ordinaire avec un `arret.json` apparu après la garde.**
  - Ce comportement est hérité de la version 4.
  - Sortie : une trace Python avec le code 1, au lieu de la ligne « ARRÊT : » avec le code 3. La trace peut porter le message, ce qui est permis pour un arrêt non cloisonné.
  - Ce cas est inatteignable en conduite ordinaire. Il est signalé, hors du champ.
- **C. Champ de la garde.** Confirmer qu'elle ne vise que la sous-commande `calcul`.
- **D. Consigne à l'opérateur après un refus.** Relancer avec un identifiant de course ou un dossier de sortie neuf. À écrire dans le mandat de l'opérateur.

## 7. Expositions et refus d'outil

- **Lu** : seulement les pièces nommées, les outils jetables du prédécesseur, et sur la branche principale les deux textes « pour mémoire ».
- **Copié sans être lu** : `readout.py`.
- **Jamais ouvert** : aucun registre, aucune branche de données, de calcul ou de verdict, aucun dossier `diag/` ni `runs/`, aucune table, aucun verdict.
- **Dépôt** : aucune écriture.
- **Un refus d'outil** : `sleep 240` au premier plan. Il n'a pas été rejoué.

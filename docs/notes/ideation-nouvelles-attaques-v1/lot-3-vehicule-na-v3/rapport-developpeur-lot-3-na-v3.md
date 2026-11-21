# Rapport du développeur — véhicule NA-1, lot 3 (requête et journal) — v3

- Développeur du lot 3 du véhicule NA-1, modèle O ; le même que pour la v1 et la v2.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 10:13:29Z (`date -u`).
- La v3 remplace la v2 : `…/scratchpad/dev-vehicule-na-lot-3-v2/rapport-developpeur-lot-3-na-v2.md`, `f9e72b34a0cc8e192ba2c7c906f6821bda4651b4f1543c8400b4d374c90fe266` ; dossier de la v2 laissé en l'état, sans modification (table `672f76ac…`). La v1 (table `9fd8834a…`) est vérifiée « Conforme » (`3fe6c963…`).
- Objet : le message de la coordination. La mère veut une v3 avant le lot 6. Le lot 2 est passé en v5 ; les modules de la course sont `garde_motifs_na_v4` et `tirage_na_v4`. **La v3 ne change que des noms**, comme la v2.
- Mêmes règles : processeur seul ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ; données factices seules. Aucun refus de permission, de classifieur ni de garde rencontré. Aucune commande de liste hors de mes dossiers : la table du lot 2 v5 a été ouverte par son chemin complet (nom deviné, lu au premier essai, égal à son compagnon). **La liste réelle des motifs n'est ni copiée, ni lue par mon code** : aucun essai du lot 3 n'en a besoin. Seuls les essais du lot 2 v5, joués par son programme d'application, la lisent, de la façon qui est la leur.

## 1. Verdict

**Essais du lot 3 : 72 passés, 0 échec** (requête 44, journal 28), les mêmes qu'en v1 et v2. Sur une copie neuve avec le paquet v5 du lot 2 posé par son programme : **200 passés** (128 du lot 2 v5, qui sont ses comptes ; 72 du lot 3). **Mutations : 58 sur 58 tuées**, textes identiques ; témoin non muté passe ; témoin inerte survit. **Différentiel v2 → v3** (381 lignes) : rien que des noms, des docstrings et des listes de fichiers (§ 3).

## 2. Pièces lues (empreinte recalculée)

| pièce | empreinte | état |
|---|---|---|
| table du lot 2 v5 | `6a5b5400aa9209f32f9cbd5a14116b5ddff929eac3886aec3753643c8282a2ce` | égale à son compagnon ; manifeste, programme d'application, rapport et douze fichiers du paquet (ceux que le lot 3 lit ou exige), recalculés, égaux |
| manifeste du lot 2 v5 | `b0f603a5…` | lu en entier |
| `garde_motifs_na_v4.py` | `b90d2fbd…` | différentiel contre la v3 lu en entier : mêmes classes (`GardeMotifs`, `RequeteGardee`, `ArretMotifInterdit`, `Normaliseur`, `ListeMotifs`), même `verifier_avant_envoi`, `NUMERO_ARRET` inchangé ; en plus `Normaliseur.normaliser_expression` ; l'apparence vide ramenée à une espace |
| `tirage_na_v4.py` | `55d6587e…` | différentiel contre la v3 : en-tête, version, import de la garde v4 ; rien d'autre |
| `aides_na_v4.py` | `b72c0397…` | lu en entier : `garde_essai()` construit la garde par `Normaliseur(charger_donnees_ignorables(…))`, `charger_liste_motifs(chemin, empreinte, normaliseur)`, `GardeMotifs(liste)` ; sa fonction `lire_liste_reelle` n'est appelée par aucun de mes essais |

## 3. Ce qui change, fichier par fichier (`differentiel-lot-3-v2-v3.diff`)

| v2 | v3 | changement |
|---|---|---|
| `pole/requete_na_v2.py` | `pole/requete_na_v3.py` | import `tirage_na_v3` → `tirage_na_v4` ; `VERSION` ; noms de la docstring ; paragraphe « v3 » |
| `pole/journal_na_v2.py` | `pole/journal_na_v3.py` | imports `garde_motifs_na_v3` → `garde_motifs_na_v4`, `requete_na_v2` → `requete_na_v3` ; `VERSION` ; le message qui nomme le module de la requête ; noms de la docstring ; paragraphe « v3 » |
| `essais/aides_na_lot3_v2.py` | `essais/aides_na_lot3_v3.py` | imports `aides_na_v3` → `aides_na_v4`, `requete_na_v2` → `requete_na_v3` ; docstring |
| `essais/test_na_v2_requete.py` | `essais/test_na_v3_requete.py` | imports ; docstring ; aucun essai changé |
| `essais/test_na_v2_journal.py` | `essais/test_na_v3_journal.py` | imports ; nom du programme d'aide joué dans un autre processus ; docstring ; aucun essai changé |
| `essais/mutations_na_lot3_v2.py` | `essais/mutations_na_lot3_v3.py` | liste des fichiers copiés (garde et tirage v4, aides v4, lot 3 v3 ; données des ignorables et programme d'extraction gardés) ; chemins visés ; noms du journal et du dossier temporaire ; 58 mutations et témoin inerte identiques |
| `appliquer_paquet_vehicule_na_lot_3_v2.py` | `appliquer_paquet_vehicule_na_lot_3_v3.py` | manifeste lu ; essais joués (`test_na_v4_tirage`, `test_na_v5_garde_motifs`, les deux du lot 3 v3) ; clé `dependances_lot_2_v3` → `dependances_lot_2_v5` ; message de refus ; docstring |
| `sonde_gabarit_servi_na_lot3_v2.py` | `sonde_gabarit_servi_na_lot3_v3.py` | imports `requete_na_v3`, `tirage_na_v4` ; docstring |
| manifeste v2 | `manifeste-paquet-vehicule-na-lot-3-v3.json` | réécrit : fichiers v3 et empreintes ; les dix fichiers du lot 2 v5 exigés à leurs empreintes (`liste_reelle_na_v5.py` compris, parce que ses essais le lisent) ; mêmes fichiers existants lus |

Noms neufs selon R12 : le contenu change (imports), donc le nom ; `journal_na_v3` lit la `RequeteAssemblee` de `requete_na_v3`.

## 4. Rejeu

- Copie neuve du dossier `orchestrator` du commit `a41b7b50…`, dans mon dossier ; paquet v5 du lot 2 posé par son programme (`--lancer-essais`) : **128 passés**.
- Paquet v3 du lot 3 posé par le mien (`--lancer-essais`) : **200 passés**. Journal détaillé du lot 3 seul : `journal-essais-na-lot-3-v3.txt`, **72 passés**.
- Refus : seconde application (R12) ; dépôt de l'orchestrateur ; copie nue ; copie qui ne porte que l'ancien paquet v3 du lot 2 (« `garde_motifs_na_v4.py` absent »). La copie de ces deux derniers essais, en brouillon, est retirée.
- Mutations : `journal-mutations-na-lot-3-v3.json`, **58 sur 58 tuées**.
- Sonde sur le gabarit servi réel (tiré de `origin/main` par `git show` redirigé, puis retiré) : `journal-sonde-gabarit-servi-na-lot-3-v3.json` : un emplacement, 120 cases remplies à l'octet, dernier octet gardé, 3 006 à 3 080 octets ; égal à la v1 et à la v2.
- Dépôt de l'orchestrateur propre après (`git status --short --ignored` vide).

## 5. Points tenus de la v2

- Le constat mineur du vérificateur (`FileNotFoundError` si le journal est supprimé en cours de course) **n'est toujours pas porté** : la v3 est, comme la v2, « noms seuls ». Ma recommandation reste une version du journal qui convertit `OSError` en `JournalReecrit`, avec un essai et une mutation, ou un mot au mandat du lot 4.
- Les treize remarques du rapport v1, § 5, et la remarque neuve du rapport v2, § 6 (noms de champs lus comme des mots séparés), tiennent. La garde v4 normalise aussi les littéraux des expressions : cela touche la liste, non la requête, et ne change rien au lot 3.

## 6. Interface pour les lots 4 et 5

Celle de la v1, aux noms près : `pole.requete_na_v3`, `pole.journal_na_v3`, garde `pole.garde_motifs_na_v4`.

```
envoi = j.journaliser_envoi(requete, garde_v4, role=..., cle=...)
garde_motifs_na_v4.verifier_avant_envoi(envoi.requete_gardee, octets_remis)
consigne = envoi.chaine_pour_le_noyau()
```

`journaliser_envoi` exige une `garde_motifs_na_v4.GardeMotifs` ; un refus remonte en `garde_motifs_na_v4.ArretMotifInterdit`, après la ligne « non envoyé ». Une garde d'une autre version est refusée par construction (`LigneRefusee`). `Normaliseur.normaliser_expression`, neuf au lot 2, n'est pas appelé par le lot 3.

## 7. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-3-v3/`. Un compagnon `.sha256` par fichier ; table `table-empreintes-dossier-na-lot-3-v3.txt`. La copie d'application `copie-orchestrateur-application/` (lot 2 v5 et lot 3 v3 posés) reste dans le dossier, hors de la table ; elle n'est pas un dépôt et ne contient aucune copie de la liste réelle.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/requete_na_v3.py` | `60d40f76d1fc90118818f39ec92d96bbdb025a1a4e044bfcd0bfc943a8ca42c7` |
| `paquet/orchestrator/pole/journal_na_v3.py` | `c5a66c05bd75b7e082670d5dcd468c13c20875fcbb86b51651cf1c9c2da6c40c` |
| `paquet/orchestrator/essais/aides_na_lot3_v3.py` | `81f19bd8c4c5074115f2c9ae587e4abf981d1f83bb0ab76f4e971dbeeaf17e5a` |
| `paquet/orchestrator/essais/test_na_v3_requete.py` | `3b18677b5b4d06709b9a4a2d45a73f12ad02971580d1eb43351aea24466f4735` |
| `paquet/orchestrator/essais/test_na_v3_journal.py` | `4ee0a404d7b7f2c1aefe38d94ad36b1bfa798fd268899d3ddf61906444ad9cf7` |
| `paquet/orchestrator/essais/mutations_na_lot3_v3.py` | `40b784e63a9f15766f48d873d7f79d7f6cda56d52ba82a89f9856b5dd57a5575` |
| `manifeste-paquet-vehicule-na-lot-3-v3.json` | `844b36f7e535ee64de8666536ee49ef3667f1aa48237cb40fc7bdc21b20d51e8` |
| `appliquer_paquet_vehicule_na_lot_3_v3.py` | `074fb0b40b8cb56709be6873625dddfd84846690033a48c3b29a7a7431b328ea` |
| `differentiel-lot-3-v2-v3.diff` | `a00525e61b36574e2778ad4a13c205d84ff484130b40b4bf305603ce9d62063a` |
| journaux, sonde, programme des compagnons, ce rapport | voir la table |

— développeur du lot 3 du véhicule NA-1, modèle O

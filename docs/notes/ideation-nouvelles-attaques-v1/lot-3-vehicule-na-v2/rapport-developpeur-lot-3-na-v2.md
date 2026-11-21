# Rapport du développeur — véhicule NA-1, lot 3 (requête et journal) — v2

- Développeur du lot 3 du véhicule NA-1, modèle O ; le même que pour la v1.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 09:35:59Z (`date -u`).
- La v2 remplace la v1 : `…/scratchpad/dev-vehicule-na-lot-3/rapport-developpeur-lot-3-na-v1.md`, `974bcc9a194e74d716cb3cf4266322f04d31f88e481b2d3382e1b38e9fb367a6`. La v1 est vérifiée « Conforme » (`docs/notes/ideation-nouvelles-attaques-v1/lot-3-vehicule-na-v1/verification-v1/verification-lot-3-na-v1.md`, `3fe6c96322dc765321ab4f404d67db32dc7009f7e1cd31e1639a00ff764c62a3`, lue en entière). Le dossier de la v1 reste en l'état, sans modification (table `9fd8834a…`).
- Objet : le message de la coordination. Le lot 2 est passé en v3 ; le lot 3 v1 ne marche pas avec elle (le programme d'application exige `tirage_na_v2.py` ; `journaliser_envoi` refuse une garde v3, d'autres classes ; l'arrêt `ArretMotifInterdit` de la v2 n'est pas celui de la v3). **La v2 ne change que des noms.**
- Mêmes règles : processeur seul ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ; données factices seules. Aucun refus de permission, de classifieur ni de garde rencontré. Aucune commande de liste hors de mes dossiers et de ceux des lots 1 et 2 : la table du lot 2 v3 et la vérification du lot 3 ont été ouvertes par leur chemin complet (le nom de la seconde a été essayé par `ls` sur un chemin complet, deux fois ; la première tentative a rendu « absent »).

## 1. Verdict

**Essais : 72 passés, 0 échec** (requête 44, journal 28), les mêmes qu'en v1. Sur une copie neuve avec le paquet v3 du lot 2 posé par son programme : **189 passés, 1 sauté** (117 et 1 sauté du lot 2 v3, qui sont ses propres comptes ; 72 du lot 3). **Mutations : 58 sur 58 tuées**, les mêmes textes qu'en v1. Le témoin non muté passe ; le témoin inerte survit. **Différentiel v1 → v2** : rien que des noms, des docstrings, la liste des fichiers copiés par le programme des mutations, et la clé du manifeste que lit le programme d'application (§ 3).

## 2. Pièces lues (empreinte recalculée)

| pièce | empreinte | état |
|---|---|---|
| table du lot 2 v3 | `7759069872fdd8540ba6cf0873b7bae06dc48ab537a355497e55b35e14ad81d3` | égale à l'annonce et au compagnon ; les 13 fichiers du paquet, le manifeste, le programme d'application et le rapport recalculés, égaux |
| `garde_motifs_na_v3.py` | `cea1e692…` | lu en entier : `GardeMotifs`, `RequeteGardee`, `ArretMotifInterdit`, `verifier_avant_envoi`, `NUMERO_ARRET` ont la même forme qu'en v2 ; la garde se construit sur des données d'ignorables et un normaliseur |
| `tirage_na_v3.py` | `5ec1bef8…` | différentiel contre la v2 : en-tête, version, et deux arguments du programme du jeu ; les fonctions que lit `requete` sont inchangées |
| `aides_na_v3.py` | `b28c0bac…` | lu en entier : `garde_essai()` construit la garde comme la coordination le demande |
| manifeste du lot 2 v3 | `256e99d3…` | lu en entier |
| vérification du lot 3 v1 | `3fe6c963…` | lue en entière |

## 3. Ce qui change, fichier par fichier (différentiel `differentiel-lot-3-v1-v2.diff`, 375 lignes)

| v1 | v2 | changement |
|---|---|---|
| `pole/requete_na_v1.py` | `pole/requete_na_v2.py` | import `tirage_na_v2` → `tirage_na_v3` ; `VERSION` ; trois noms dans la docstring ; un paragraphe « v2 » |
| `pole/journal_na_v1.py` | `pole/journal_na_v2.py` | imports `garde_motifs_na_v2` → `garde_motifs_na_v3`, `requete_na_v1` → `requete_na_v2` ; `VERSION` ; un message qui nomme le module de la requête ; trois noms dans la docstring ; un paragraphe « v2 » |
| `essais/aides_na_lot3_v1.py` | `essais/aides_na_lot3_v2.py` | imports `aides_na_v2` → `aides_na_v3`, `requete_na_v1` → `requete_na_v2` ; docstring |
| `essais/test_na_v1_requete.py` | `essais/test_na_v2_requete.py` | imports (aides, garde v3, requête v2) ; docstring ; aucun essai changé |
| `essais/test_na_v1_journal.py` | `essais/test_na_v2_journal.py` | imports (aides, garde v3, journal v2, requête v2) ; le nom du programme d'aide joué dans un autre processus ; docstring ; aucun essai changé |
| `essais/mutations_na_lot3_v1.py` | `essais/mutations_na_lot3_v2.py` | liste des fichiers copiés : noms v3 du lot 2 et v2 du lot 3, plus `pole/ignorables-unicode-15.1.0-na-v1.json` et `pole/extraire_ignorables_unicode_na_v1.py` ; chemins des essais et des modules visés ; nom du journal et du dossier temporaire ; les 58 mutations et le témoin inerte sont identiques, texte pour texte |
| `appliquer_paquet_vehicule_na_lot_3_v1.py` | `appliquer_paquet_vehicule_na_lot_3_v2.py` | manifeste lu ; essais joués (`test_na_v3_tirage`, `test_na_v3_garde_motifs`, les deux du lot 3 v2) ; clé `dependances_lots_1_et_2` → `dependances_lot_2_v3` ; message de refus ; docstring |
| `sonde_gabarit_servi_na_lot3_v1.py` | `sonde_gabarit_servi_na_lot3_v2.py` | imports `requete_na_v2`, `tirage_na_v3` ; docstring |
| manifeste v1 | `manifeste-paquet-vehicule-na-lot-3-v2.json` | réécrit : fichiers v2 et leurs empreintes ; les neuf fichiers du lot 2 v3 exigés à leurs empreintes ; mêmes fichiers existants lus |

**Pourquoi des modules neufs plutôt que le même nom** : le contenu change (deux imports), donc le nom change (règle R12 : nouvelle version, nouveau nom). Et `journal` doit lire la `RequeteAssemblee` du module `requete` qu'il accompagne : `journal_na_v2` lit `requete_na_v2`.

**Noms des fichiers d'essais.** J'ai lu « passent aux noms v3 » comme « lisent les modules v3 du lot 2 » : les fichiers du lot 3 portent la version du lot 3 (`test_na_v2_requete.py`, `test_na_v2_journal.py`, `aides_na_lot3_v2.py`). Ils ne se confondent pas avec ceux des lots 1 et 2 v2 (`test_na_v2_tirage.py`, `test_na_v2_garde_motifs.py`), qui ne sont pas posés avec la v3.

**La garde dans les essais** se construit comme la coordination le demande, par `aides_na_v3.garde_essai()` et `aides_na_v3.liste_essai()` : `Normaliseur(charger_donnees_ignorables(chemin, empreinte))`, puis `charger_liste_motifs(chemin, empreinte, normaliseur)`, puis `GardeMotifs(liste)`. Mes essais appelaient déjà ces deux fonctions ; rien n'est réécrit.

## 4. Rejeu

- Copie neuve du dossier `orchestrator` du commit `a41b7b50…`, dans mon dossier ; paquet v3 du lot 2 posé par son programme (`--lancer-essais`) : 117 passés, 1 sauté.
- Paquet v2 du lot 3 posé par le mien (`--lancer-essais`) : **189 passés, 1 sauté**. Journal détaillé du lot 3 seul : `journal-essais-na-lot-3-v2.txt`, **72 passés**.
- Refus du programme d'application : seconde application (« cible déjà présente », R12) ; dépôt de l'orchestrateur (« destination dans le dépôt ») ; copie nue, puis copie qui ne porte que l'ancien paquet v2 des lots 1 et 2 (« fichier requis absent ou d'une autre empreinte : `garde_motifs_na_v3.py` »). La copie de ce dernier essai, dans un dossier de brouillon, est retirée.
- Mutations : `journal-mutations-na-lot-3-v2.json`, **58 sur 58 tuées**, témoin non muté passe, témoin inerte survit.
- Sonde sur le gabarit servi réel (tiré de `origin/main` par `git show` redirigé, puis retiré) : `journal-sonde-gabarit-servi-na-lot-3-v2.json` : un emplacement, 120 cases remplies à l'octet, dernier octet gardé, 3 006 à 3 080 octets ; comptes égaux à la v1.
- Dépôt de l'orchestrateur propre après (`git status --short --ignored` vide).

## 5. Le constat mineur du vérificateur : non porté

Un journal dont le fichier est supprimé en cours de course lève `FileNotFoundError` à l'ajout suivant, et non `JournalRefuse`. **Je ne le porte pas dans cette v2** : la coordination demande une v2 qui ne change que des noms, prouvée par le différentiel. Ajouter ici un changement de logique, même petit, brouillerait cette preuve. Il refuse déjà bien (rien n'est écrit, rien ne part). Deux voies, à dire par la mère : une v3 du journal (convertir `OSError` en `JournalReecrit`, dans `_verifier_intact` et à l'écriture, avec un essai et une mutation) ; ou le mandat du lot 4 qui fait attraper `OSError` autant que `JournalRefuse`. Je recommande la première, un essai à l'appui.

## 6. Ce que la lettre ne fixe pas

Les treize remarques du rapport v1 (§ 5) tiennent, sans changement. Une de plus : le lot 2 v3 ramène tiret, soulignement et espace à une seule forme pour la comparaison. Les clés de la fiche servie (`ce_que_le_moniteur_suppose`, …) sont donc lues par la garde comme des mots séparés d'espaces : un motif littéral fait de mots pourrait mordre sur un nom de champ. La liste réelle des motifs doit être jouée sur les requêtes du portier et des juges (V9, l. 387, réserve du faux refus) ; avec la liste d'essai, rien ne mord.

## 7. Interface pour les lots 4 et 5

Celle de la v1 (rapport v1, § 6), aux noms de modules près : `pole.requete_na_v2` (alias `rq`), `pole.journal_na_v2` (alias `jn`), avec la garde `pole.garde_motifs_na_v3`. Au point d'envoi du lot 4 :

```
envoi = j.journaliser_envoi(requete, garde_v3, role=..., cle=...)
garde_motifs_na_v3.verifier_avant_envoi(envoi.requete_gardee, octets_remis)
consigne = envoi.chaine_pour_le_noyau()
```

`journaliser_envoi` exige une `garde_motifs_na_v3.GardeMotifs` ; un refus remonte en `garde_motifs_na_v3.ArretMotifInterdit`, après la ligne « non envoyé ». Une garde v2 est refusée (`LigneRefusee`), par construction (le contrôle de type vise la classe v3), comme une garde v3 l'était par la v1 ; ce cas précis n'a pas d'essai à lui, le contrôle de type est éprouvé par `test_garde_du_lot_2_exigee` et la mutation L3-46.

## 8. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-3-v2/`. Un compagnon `.sha256` par fichier ; table `table-empreintes-dossier-na-lot-3-v2.txt`. La copie d'application `copie-orchestrateur-application/` (lot 2 v3 et lot 3 v2 posés) reste dans le dossier, hors de la table ; elle n'est pas un dépôt.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/requete_na_v2.py` | `b8e0bf150d6198e96d454f5253658d1ab83c13f59e3e4d36b481464b502699e8` |
| `paquet/orchestrator/pole/journal_na_v2.py` | `d9de190affb40eafd3454c2f574cadf750b8d02852f91eebaf2a03b769c62e8d` |
| `paquet/orchestrator/essais/aides_na_lot3_v2.py` | `757e2901a6fd1795ebc4a5306311b63cf11512d33d439fc32c4f7a9137b07040` |
| `paquet/orchestrator/essais/test_na_v2_requete.py` | `0c1ec0872c11acf227ab5a456180f071a90a3c411b3e877c1d2bcdb96f98db21` |
| `paquet/orchestrator/essais/test_na_v2_journal.py` | `126661539d1111b251d941c0c6ef4980cb63a4e94774201f9fdf7c528a6396c5` |
| `paquet/orchestrator/essais/mutations_na_lot3_v2.py` | `06c328bcca900276052e3a0df66d22e4e4a5fbf4353ff1689c33fa78e386206e` |
| `manifeste-paquet-vehicule-na-lot-3-v2.json` | `8e8035b98ade9be3f4dd27de9025aeba7aff06d43a515e511b3126ac511270f8` |
| `appliquer_paquet_vehicule_na_lot_3_v2.py` | `28133e70ae7fdf888d78cd11888acf32c25dc759f09dab19b854ec0351335c33` |
| `differentiel-lot-3-v1-v2.diff` | `bb6c8fbc57c8482cd1966fa873f6e7260be828d2899cdf51ea9364a9a6ed0c06` |
| journaux, sonde, programme des compagnons, ce rapport | voir la table |

— développeur du lot 3 du véhicule NA-1, modèle O

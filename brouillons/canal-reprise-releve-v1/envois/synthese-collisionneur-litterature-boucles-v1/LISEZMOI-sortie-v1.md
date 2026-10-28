# LISEZMOI — sortie de la synthèse du collisionneur « littérature des boucles » (étage III, trois tours) — v1

Écrit le 2026-10-26 à 04:07:53 (heure universelle, lue sur `date -u` dans la commande même d'écriture) par un sous-agent neuf, du
même modèle que la cellule B, sur le brief `BRIEF-synthese-litterature-boucles-v1.md`, d'empreinte
`be38c86b8a146f7af6a4abaddd23672ba946a66d7e4fcef64a4a31328e97cb0a`, égale à celle donnée dans la consigne.

## Ce qui a été fait

1. **Vérification des pièces, avant toute lecture des réponses.**
   - Chaque cellule contre son compagnon `.sha256` (`sha256sum -c`, dans `cellules/`) : 8 sur 8 conformes.
   - Chaque cellule et chaque compagnon contre `EMPREINTES-v1.txt`, sous les chemins relatifs au dossier d'origine du tour
     (`run-litterature-boucles-e3t1-v1/cellules/<nom>`) : 16 sur 16 conformes.
   - `LISEZMOI-v1.md` et la question contre `EMPREINTES-v1.txt` : conformes ; la question est aussi identique à
     `run-litterature-boucles-e3t1-v1/question-etage3.md` de la même liste.
   - Chaque cellule est identique à la réponse d'essai listée (`run-litterature-boucles-e3t1-v1/essais/<cellule>.essai1.reponse.md`).
   - Pièces fournies hors de `EMPREINTES-v1.txt` : empreintes relevées pour mémoire (table ci-dessous).
2. **Lecture en entier** : brief, LISEZMOI du tour, question, huit cellules, liste des vingt-quatre papiers ; la synthèse
   précédente, pour la forme seulement. Aucun contenu de réflexion interne n'a été trouvé dans les cellules.
3. **Écriture** : la synthèse, ce LISEZMOI et leurs compagnons ; dans chacun des deux fichiers, l'heure a été lue sur
   `date -u` dans la commande qui l'écrit.
4. **Rien d'autre** : ni git, ni réseau, ni sous-agent, ni clé, ni dépense ; lecture limitée au dossier fourni ; écriture
   limitée au dossier de sortie ; aucune référence ajoutée de mémoire (titres, auteurs, années et lieux sont ceux des cellules).

## Pièces lues

| pièce | empreinte | contrôle |
|---|---|---|
| `BRIEF-synthese-litterature-boucles-v1.md` | `be38c86b8a146f7af6a4abaddd23672ba946a66d7e4fcef64a4a31328e97cb0a` | égale à l'empreinte donnée |
| `LISEZMOI-v1.md` | `8243b049c07d8e36273ab6fcc80be4ffcf92a904f26fdf774c32ad68b9ad7adf` | `EMPREINTES-v1.txt` |
| `question-litterature-boucles-agents-collisionneur-v1.md` | `962130b724a7a6df26840cf8077dbaa6f592190219650d79d732177523dd85cb` | `EMPREINTES-v1.txt` |
| `cellules/E3-T1-conception-A.md` | `d946eb3b0bf1fa2da9a927bf993ce456709d0bdd67a3e50de0fdba03e79cc6f4` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T1-conception-B.md` | `35bc6911f465401d8dfc392de9eb30204423990a7f93f62bed3287d699ba8760` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T1-conception-C.md` | `546c0e410c0b3c6dfc565716f728036fc12b7e015eabe1861f619f458ed233b4` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T2-redteam-A.md` | `1239950aae6b307afb83e3f614c4863bce8219040b61be681b204bf917a45e23` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T2-redteam-C.md` | `509cd15caa540629f7c1ca08fdd960088cfe8fa006fd08467bf463a23891c38b` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T3-riposte-A.md` | `1b3d7a753e42154bb7a9d675e9c33f01824af2483f90a70e065c101534d7e1d3` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T3-riposte-B.md` | `8c375eab9c06a9323805ddf9a90272b0858a4765761b282e2120ab618581a688` | compagnon et `EMPREINTES-v1.txt` |
| `cellules/E3-T3-riposte-C.md` | `81f75df6bcfcd88d4b692f3b9ae805c90f78e07b80efef27c2e5086053168fde` | compagnon et `EMPREINTES-v1.txt` |
| `EMPREINTES-v1.txt` | `317b0f0bcb46228aa4bd59dc7af7a9829250b9bb2964bcb4419cde86f3e5d077` | hors liste, relevée |
| `EMPREINTES-pdfs-v1.txt` | `560a9bf96c690b489ce450f6a063a0f88dc45f24f651bf2425771917ed839c99` | hors liste, relevée |
| `exemple-synthese-precedente-v1.md` | `406967ac7895c12191fa59546ee756704987992efa82ee3d6b6ef34e95a693ac` | hors liste, relevée |

## Fichiers écrits, dans `/var/tmp/synthese-collisionneur-litterature-boucles-v1/`

| fichier | empreinte |
|---|---|
| `synthese-collisionneur-litterature-boucles-v1.md` | `58010971d190269465d86f97bad9f5e06830b2e73d2899e7cf990f0845e19916` |
| `synthese-collisionneur-litterature-boucles-v1.md.sha256` | `ecea4a957ed466304e8c490902db9ef72b3be0690868ed1c81eac58f1d858f25` |
| `LISEZMOI-sortie-v1.md` | dans `LISEZMOI-sortie-v1.md.sha256` (un fichier ne peut porter sa propre empreinte) |

Compagnons au format « empreinte, deux espaces, nom nu » ; vérifiables par `sha256sum -c` depuis le dossier de sortie.

## Écarts déclarés

1. « Tours II et III » du brief lus comme les tours III.2 et III.3.
2. Longueur : la table de cinquante travaux (8 226 octets) porte la synthèse à 24 713 octets, au-delà de trois pages
   (la synthèse précédente, sans table, en faisait 11 091) ; la prose a été resserrée, pas la table.
3. Sans acronymes : lieux de publication développés ; titres anglais, noms cités (« APE », « DSPy ») et noms courts de
   fichiers gardés tels quels, sigles compris ; « R7 », « R8 » et étiquettes d'expériences des cellules (E7, V1, W0…) gardés
   comme étiquettes.
4. Colonne « liste des vingt-quatre » : rapprochement par nom court seulement ; les fichiers ne sont pas fournis, versions
   et années non vues ; deux rapprochements marqués « probable » ou « version à confirmer ».
5. « Cité par » distingue la citation indépendante (tour III.1, à l'aveugle) de la reprise après lecture d'une autre cellule.
6. Les décisions prises depuis la question ne sont connues que par le brief ; aucun document de décision n'a été lu ;
   aucune n'est rejugée.
7. Une observation de lecture n'est dans aucune cellule : le cloisonnement de C suppose une réécriture hors du processus
   d'évaluation (§ 8 de la synthèse).
8. Aucun critère ni aucune stratégie de classement des tâches n'est recopié : les exemples de règles, listes de mots et
   traits textuels proposés dans des cellules de C sont omis ou décrits sans leur contenu.

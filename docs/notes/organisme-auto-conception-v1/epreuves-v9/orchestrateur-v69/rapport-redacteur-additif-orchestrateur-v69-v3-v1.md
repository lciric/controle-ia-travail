# Rapport du rédacteur — additif des interrupteurs de l'orchestrateur v69 et cadre de la v70, version 3 — v1

- Rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` avant l'écriture des pièces : 05:57:19Z.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/mandat-redacteur-additif-orchestrateur-v69-v3-v1.md` (`c4ab6ddbe7e78466b4d562db2ba80e48849db57bd9054800e5dd218aecfdbaf9`, compagnon vérifié). V69 désigne ce dossier.
- Dossier de travail (noté D) : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-orchestrateur-v69-v3/`.
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme, aucune dépense, aucun appel à un fournisseur de modèles. **Aucun refus de permission, de classifieur ni de garde.** Aucun allumage n'est accordé par ces pièces. Aucun identifiant de modèle.

## 0. Verdict

Les cinq corrections du contrôle sont portées à la lettre, par l'outil, dans deux pièces neuves : additif v3 (13 remplacements) et cadre v3 (5 remplacements). Les pièces v2 sont intactes. Un écart déclaré : une virgule changée en point (§ 4, écart 1). Les pièces v3 ne sont pas contre-lues : leur différentiel avec la v2 est à contrôler par un lecteur qui ne les a pas écrites (règle R2).

## 1. Ce qui a été vérifié avant d'écrire

| pièce | sha256 | vérification |
|---|---|---|
| `V69/controle-differentiel-additif-orchestrateur-v69-v1-v2-v1.md` | `695b980b12d2fc0d71873771dca11600b42e342f6a73ed701790ccc9a9624f37` | `sha256sum -c` du compagnon : OK |
| `V69/additif-interrupteurs-orchestrateur-v69-v2.md` | `9d94d23fadfc961e1e3c71a743358d4d5a16a924267499b3a3f1028fee34e85f` | `sha256sum -c` du compagnon : OK |
| `V69/cadre-lecture-registre-orchestrateur-v70-v2.md` | `216d9bcbc0276c79c5a86bcf835cd3d9d260d6e31e49c7f1250349530643fbeb` | `sha256sum -c` du compagnon : OK |
| `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` | recalculée ; outil lu en entier avant l'appel |
| `registres/go.md` sur `origin/main` | copie de travail `D/go-origin-main.md` (par `git show` redirigé) | `GO-2026-11-20-10` (l. 541, point (O3) : « Orchestrateur v69 : D1 (a′), D2 (a), D3 (a) ») et `GO-2026-11-20-11` (l. 542, « go reprise, go recos », « Le reste recoupe GO-2026-11-20-10 ») y figurent toutes deux |

Chaque texte ancien des deux JSON a été compté sur sa cible par `grep -c -F -e` avant l'appel : 1 pour chacun des 18 (règle R-4067). L'outil a rendu « FAIT » aux deux appels, sans avertissement.

## 2. Pièces rendues (toutes dans D, chacune avec son compagnon `.sha256`, tous vérifiés par `sha256sum -c`)

| fichier | sha256 |
|---|---|
| `additif-interrupteurs-orchestrateur-v69-v3.md` | `f71e3a551c820ccabf5e7540dba8b4c1d1569386e069e94f0a710bf9d7ce9cba` |
| `cadre-lecture-registre-orchestrateur-v70-v3.md` | `b1822613071f88a50b514ffbb38073ce664038937468a875f4d57838433a9eac` |
| `remplacements-additif-v2-vers-v3-v1.json` | `3a24fc82efe406139f919dfa3935902cd568200df863c066a2dae9d78da99668` |
| `remplacements-cadre-v2-vers-v3-v1.json` | `2df90ff1963f1e34373389b2a08c6b68d08f1ccf1e16de8dc46f55d0d0015650` |
| `additif-interrupteurs-orchestrateur-v69-v3.md.journal-remplacements-v1.json` | `2ea7083c932b3bdcc4b9e45be3acd51763bf27f8f85e4733371e97c542755d47` |
| `cadre-lecture-registre-orchestrateur-v70-v3.md.journal-remplacements-v1.json` | `465548e757c768492ae8020f33aecc8886f46d42dd3ca686723fa0b93984636d` |
| `differentiel-additif-v2-vers-v3-v1.diff` (`diff -u`, v2 → v3) | `6eac48df2b19ac930e21e52408ce297d776b25a74d8546829572990e9b3e33d9` |
| `differentiel-cadre-v2-vers-v3-v1.diff` (`diff -u`, v2 → v3) | `b3ba652f4d1e1d4d32f920d1489815a2afa40bfba892c0af5a444bacd076f4e2` |
| ce rapport | dans son compagnon |

Les deux différentiels ont été relus en entier : ils couvrent les 13 et les 5 zones, et rien d'autre.

## 3. Les remplacements

### 3.1 Additif : 13 remplacements

| rang du JSON | nature | lieu |
|---|---|---|
| 1 | tenue | titre : « v2 » devient « v3 » |
| 2 | tenue | ligne de version : mention de la version 3, la v2 nommée avec son empreinte |
| 3 | tenue | ligne « Statut » : la v2 contrôlée sur son différentiel, la v3 non contre-lue, ce qu'elle porte, son différentiel à contre-lire |
| 4 | correction 1, à la lettre | ligne « Statut » : inscription en `GO-2026-11-20-10`, point (O3) |
| 5 | tenue | ligne « Mandat » : mandat de la v3 ; `GO-2026-11-20-10` et `GO-2026-11-20-11` cités |
| 6 | correction 2, à la lettre | § 0, point 4 |
| 7 | correction 2, à la lettre | § 4.4, dernier alinéa |
| 8 | correction 3, à la lettre | § 1.2, « Ce que le sommet neuf porte lui-même » |
| 9 | correction 3, à la lettre | § 5.2, « L'étage tient lui-même sa réservation » |
| 10 | correction 3, à la lettre | § 6, garde 6, cas sain |
| 11 | correction 4, à la lettre | § 4.2, dernier alinéa |
| 12 | **écart déclaré** (§ 4, écart 1) | § 1.2, « Ce qui reste à établir », point 3 : la virgule devant le texte de la correction 5 devient un point |
| 13 | correction 5, à la lettre | § 1.2, « Ce qui reste à établir », point 3 |

### 3.2 Cadre : 5 remplacements

| rang du JSON | nature | lieu |
|---|---|---|
| 1 | tenue | titre : « v2 » devient « v3 » |
| 2 | tenue | ligne de version : mention de la version 3, la v2 nommée avec son empreinte |
| 3 | tenue | ligne « Statut » : la v2 contrôlée sur son différentiel, la v3 non contre-lue |
| 4 | tenue | ligne « Mandat » : mandat de la v3 et ce que la v3 change |
| 5 | correction 1, à la lettre | § 3, point 1 |

## 4. Écarts et points laissés tels quels, à trancher par le contrôle

1. **Écart : une virgule changée en point (additif, rang 12).** Le texte nouveau de la correction 5 commence par une majuscule (« Que `contre_calculer` reçoive… ») ; son texte ancien commence après une virgule. Appliquée seule, la correction rendait « …au corps de `jouer_etage`, Que `contre_calculer`… ». J'ai changé cette virgule en point, par un remplacement séparé, contigu, sans toucher ni au texte ancien ni au texte nouveau de la correction. Ce n'est ni un titre ni une ligne de version : c'est hors de la tenue que le mandat nomme. Pour le défaire : retirer l'objet de rang 12 du JSON et rejouer l'outil sous un nom neuf.
2. **« la v2 change », dans une v3.** La correction 1 est portée à la lettre ; la ligne « Statut » de la v3 dit donc « si la ligne est corrigée, la v2 change ». Laissé tel quel.
3. **« récrit en version 3 ».** Le § 1.2, dernier alinéa, dit encore : « Si la mère inscrit une autre lecture du mot, cet additif est récrit en version 3. » Aucune correction ne le vise ; laissé tel quel.
4. **Quatre mentions de la réserve d'inscription restent dans le corps de l'additif** (§ 1.2, deux fois ; § 4.3, introduction ; § 9, réserve 7). Le contrôle écrit « aucune autre » correction, et la phrase neuve de la ligne « Statut » lève la réserve « dans tout ce texte ». Le mandat demande de citer les deux lignes « à la place de « sous réserve d'inscription » » : je l'ai lu comme servi par la correction 1 (additif et cadre) et par la ligne « Mandat », non comme l'ordre de récrire ces quatre lieux. Si la lecture du mandat est l'autre, quatre remplacements de plus sont à donner, texte exact à l'appui.
5. **`GO-2026-11-20-11` n'est citée que sur la ligne « Mandat » de l'additif.** Le texte de la correction 1 ne nomme que `GO-2026-11-20-10` ; je ne l'ai pas changé.
6. **Trois lieux parlent encore des deux plafonds sans la condition de la correction 3** : § 1.2, « Ce que (a′) lève » (« Le sommet neuf porte les deux plafonds dans ses réglages ») ; § 6, garde 6, artefact (« l'un absent ») ; § 9, réserve 1, (b) (« que la garde 6 exige »). Le contrôle ne les corrige pas ; laissés tels quels, signalés pour la cohérence avec la garde 6 (règle R5).
7. **« Aucun des deux rédacteurs n'a lu le code »** (additif, tête) : ils sont trois maintenant, et je ne l'ai pas lu non plus. Laissé tel quel.
8. Au § 5.2, la correction 3 portée à la lettre laisse deux parenthèses à la suite. Laissé tel quel.

## 5. Proposition pour Lazar — classe d'une tentative refusée avant l'épreuve (correction 5 de la contre-lecture v1)

À porter avec le devis du palier 1 (« proposer avec recommandation » ; jugement du contrôle, § 1.7 : non couverte par D2 (a), pas un nœud). Je n'ai pas lu le plan de l'héritage : ce qui en est dit ici vient de l'additif et du contrôle.

**Décision, en une phrase.** Une tentative refusée avant l'étage des tests de mort (loi hors de la grammaire, bloc de statistique absent) est-elle écrite dans la classe « non exécutable ou indéterminée », avec le motif « refusée avant l'épreuve » compté à part, `gardee` à non, et gardée au dénominateur « des tentatives » de la règle de passage du palier 1 ?

**Enjeu.** Le plan veut que `resultat` soit une classe ou le statut, et ne nomme pas la classe d'une tentative refusée (plan v5, § 1 et § 3.0, d'après le contrôle). Sans réponse, le préenregistrement court du palier 1 ne peut pas geler la règle de passage (plan v5, § 8.4 : « la moitié au moins des tentatives »), puisque son dénominateur n'est pas défini. Aucune dépense ni aucun allumage n'en dépend.

**Options.**
- (a) **La tenir** : classe « non exécutable ou indéterminée », motif écrit à côté et compté à part, `gardee` non, au dénominateur. Avantage : lit « des tentatives » à la lettre, ne traite jamais un refus mieux que « ne tient pas », rend le passage plus difficile et non plus facile, ne change aucun critère du plan. Inconvénient : la règle de passage mêle des défauts de forme (loi mal écrite) aux échecs d'épreuve ; le compte à part permet de les séparer à la lecture, non dans la règle.
- (b) **Un statut à part, hors du dénominateur**, comme « non éprouvée (budget) ». Avantage : la règle de passage ne lit que des tentatives réellement éprouvées. Inconvénient : s'écarte de la lettre du § 8.4 et rend le passage plus facile ; ce serait changer un critère du plan, donc un nœud, non une proposition.
- (c) **La classe « ne tient pas »**. Avantage : trois classes sans motif de plus, même effet sur le dénominateur que (a). Inconvénient : dit d'une tentative jamais éprouvée qu'elle a manqué son seuil, ce que le plan exclut (« jamais éprouvée sur un chiffre que le script imprime », § 3.0), et efface la différence entre un refus de forme et un échec d'épreuve.

**Recommandation et confiance.** (a), confiance élevée : c'est la lecture la plus prudente, celle de la contre-lecture v1 et du contrôle, et celle que l'additif v3 écrit au § 4.2.

**Défaut sous 48 heures.** (a), gelée au préenregistrement court du palier 1. Le défaut est permis : il ne porte ni sur une dépense ni sur un allumage.

## 6. Ce que je n'ai pas fait

- Je n'ai lu ni le code de l'orchestrateur, ni le plan de l'héritage, ni les rapports cités par l'additif : seulement le mandat, le contrôle, les deux pièces v2, l'outil et les deux lignes du registre des accords.
- Je n'ai pas rejoué l'outil une seconde fois pour comparer à l'octet.
- Rien n'est copié dans V69 : la pose des pièces, leur contrôle et leur scellement sont à la session qui m'a mandaté.

— rédacteur neuf, modèle F

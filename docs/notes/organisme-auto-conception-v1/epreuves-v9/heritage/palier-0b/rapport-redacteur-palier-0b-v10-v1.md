# Rapport du rédacteur — préenregistrement du palier 0b (étage sur processeur), version 10 : corrections du contrôle de la version 9, remarques 2 à 4 tranchées par la mère — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-20 ; `date -u` lu à 10:11Z en cours de travail ; heure de la version 10 au journal de l'outil : 10:16:26Z.
- Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/mandat-redacteur-palier-0b-v10-v1.md` (`194f44b3e0b7e99b8959d883ab89a60f130c092dd1b0cc814982e7966c38f6ce`), vérifié par son compagnon avant tout autre geste.
- Conditions : processeur seul ; aucun tirage, aucun lancement du code du palier ; aucun appel à un fournisseur de modèles, aucune dépense ; aucune écriture dans l'arbre du dépôt, aucun commit. Réseau : un seul `git fetch origin main`, demandé par le mandat (il écrit `FETCH_HEAD` sous `.git/`), puis un `git show` redirigé vers mon dossier. Un seul programme lancé, par son chemin : l'outil de remplacement. Aucune commande de liste ; une commande simple par appel ; aucun heredoc, aucun code en ligne. Rien de lu sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Un `grep -P` a échoué sur son propre réglage de langue et a été refait : ce n'est pas un refus. **Aucun refus de permission, de classifieur ni de garde.**

P : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`. Mon dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v10/`.

## 1. Verdict

La version 10 est écrite par **31 remplacements exacts** sur la version 9, appliqués au premier appel, sans refus ni avertissement de l'outil. Elle n'est **ni contre-lue ni scellable en l'état** : la remarque 1 attend le mot de Lazar ; la décision de la mère sur les remarques 2 à 4 n'est pas encore sur `main` ; il reste le contrôle du différentiel de la version 9 à la version 10, le code v5, sa vérification et l'erratum du commit.

## 2. Fichiers rendus (chacun avec son compagnon `.sha256`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v10.md` (294 651 octets) | `ac2deb4daf4fb0b3088400ba742a6583844b0e5720774fd8b9055d0a72250f6b` |
| `remplacements-preenregistrement-palier-0b-v9-v10.json` (31 remplacements) | dans son compagnon |
| `preenregistrement-heritage-palier-0b-etage-processeur-v10.md.journal-remplacements-v1.json` | dans son compagnon |
| `differentiel-preenregistrement-palier-0b-v9-v10.diff` (`diff -u` ; 22 lignes de la version 9 changées, 22 lignes côté version 10) | dans son compagnon |
| `rapport-redacteur-palier-0b-v10-v1.md` (ce rapport) | dans son compagnon |

Pièce de travail, non scellée, dans le même dossier : `decisions-main.md`, rendu par `git show` au commit de `main` `9143abee0b8767c627a629bcb26e23b6e0640267`, et `lignes-palier-0b.txt` (sortie de la recherche demandée). La version 9 est intacte (compagnon revérifié après l'opération).

## 3. Sources vérifiées

Chaque empreinte vérifiée par son compagnon : le mandat ; la version 9 (`0aacc4ea…`) ; son JSON ; le rapport du rédacteur de la version 9 ; le contrôle du différentiel de la version 8 à la version 9 (`98f46d0ae18159e32f830ff79bc2c9a930db43a3c728c735311c2358b4a8b72e`) ; l'outil (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`).

Lu en entier : le mandat, le contrôle, le rapport du rédacteur de la version 9, l'outil. Lu en partie : la version 9 (en-tête ; puce des marges de la section « Seuil » ; B7 bis ; B8 ; table des gardes ; section « Contre-lecture » ; réserves 17 à 25 ; annexe H, alinéa « Version 8 », écart 1 et section « Version 9 » en entier). Le JSON de la version 8 à la version 9 n'a servi que de modèle de forme ; je ne l'ai pas ouvert, la forme étant dite par l'outil.

## 4. La ligne de la mère

**Absente.** La recherche demandée (`grep -n -F -e "palier 0b"` dans ma seule copie de `registres/decisions.md`) rend pour dernière ligne R-4179 (10:09:22Z), qui relaie d'autres sujets et dit seulement « questions du palier 0b et de P3 à la mère » ; le registre finit à R-4180. Aucune ligne R-4181 ou suivante n'existe à ce commit. J'ai donc écrit, comme le mandat le prescrit, **« décision de la mère du 2026-11-20 vers 10:09Z, à inscrire »**, à six endroits : ligne de version, section « Contre-lecture », remarques 2, 3 et 4 de l'annexe H, et alinéa « Ce qui revient à la mère ». La ligne de version dit le commit relu. Ces mots sont à remplacer par l'identifiant avant le scellement.

## 5. Les 31 remplacements

Chaque ancre a été comptée avant l'appel par `grep -c -F -e` : résultat 1 pour les 31 (compte de lignes) ; l'outil a confirmé une seule occurrence pour chacune. Les sept textes à la lettre du contrôle ont été vérifiés par recherche de leur texte neuf dans le contrôle (sept lignes trouvées).

| n° du JSON | lieu (ligne de la version 9) | objet | origine |
|---|---|---|---|
| 1 | titre (1) | « v9 » devient « v10 » | rédacteur (tenue) |
| 2 | ligne de version (3) | statut ; phrase « Version 10 » : ce qu'elle porte, la remarque 1, les 31 remplacements | rédacteur (tenue) |
| 3 | ligne de version (3) | mention « remarques 1 à 4 » | rédacteur (point 2 du mandat) |
| 4 | date (6) | **N1** | contrôle, § 9 |
| 5 | date (6) | date de la version 10 | rédacteur (tenue) |
| 6 | section « Seuil » (209) | **R2-T** | contrôle, § 8 |
| 7 | B7 bis (299) | jeu de la garde 27 : trois sources, proposeur, appelant | rédacteur (remarque 3) |
| 8 | B8 (323) | « après le GO de Lazar sur le palier » au lieu de « au scellement » | rédacteur (remarque 4, alignement) |
| 9 | B8 (323) | renvoi à la remarque 4, tranchée | rédacteur (remarque 4) |
| 10 | B8 (323) | **N2** | contrôle, § 9 |
| 11 | garde 25 (357) | **correction 2** | contrôle, § 8 |
| 12 | garde 27, cas sain (359) | trois sources, proposeur | rédacteur (remarque 3) |
| 13 | « Contre-lecture » (429) | alinéa « Version 10 » | rédacteur (point 2 et tenue) |
| 14 | réserve 25 (532) | **correction 1** | contrôle, § 8 |
| 15 | annexe H, écart 1 (751) | renvoi : trois sources | rédacteur (remarque 3) |
| 16 | annexe H, § 1 (901) | **N4** | contrôle, § 9 |
| 17 | remarque 1, titre (904) | « posée à Lazar, sans défaut » | rédacteur (point 7) |
| 18 | remarque 1 (904) | **N3** | contrôle, § 9 |
| 19 | remarque 1, fin (904) | posée à Lazar ; recommandation (ii) du contrôle et ses trois raisons ; non tranchée | rédacteur (point 7) |
| 20, 21 | remarque 2 (912) | « tranchée, lecture (i) » ; « D'ici là » remplacé | rédacteur (point 2) |
| 22, 23 | remarque 4 (917) | titre ; points (a) à (e) à la place des propositions | rédacteur (point 4) |
| 24 | table des silences, n° 8 (928) | « tranchée » | rédacteur (remarque 3) |
| 25, 26 | remarque 3 (934) | titre ; règle à la place de la proposition | rédacteur (point 3) |
| 27 | code v5, point 2 (943) | zone médiane : ni signalement ni mention | rédacteur (point 2) |
| 28 | code v5, point 4 (945) | verrou selon (a) à (e) | rédacteur (point 4) |
| 29 | code v5, point 5 (946) | jeu de la garde 27 | rédacteur (point 3) |
| 30 | code v5, point 6 (947) | les trois ajouts du § 7 du contrôle | rédacteur (point 6) |
| 31 | « Ce qui revient à la mère » (950) | état des quatre remarques | rédacteur |

## 6. Points où la lettre ne suffit pas — en remarque, jamais tranchés

1. **R2-T porté sans la ligne de la mère.** Le contrôle dit de le porter « seulement après la ligne de la mère ». Je l'ai porté sur la foi du mandat, qui dit la décision prise ; la ligne manque sur `main` (§ 4).
2. **Lieux touchés au-delà de ceux que le mandat nomme.** Pour la remarque 3, j'ai lu « aux lieux qu'elle désigne » comme B7 bis, la garde 27 et l'écart 1, et j'y ai ajouté la ligne n° 8 de la table des silences. J'ai aussi complété l'alinéa « Ce qui revient à la mère », qui disait « aucune tranchée ici ». À contrôler ; chacun est un remplacement séparé, retirable.
3. **Garde 27, colonne de l'artefact.** L'artefact « source précédente au lieu de suivante » n'est écrit qu'à la liste du code v5 (point 6), comme le mandat le demande ; la table des gardes ne le porte pas. S'il doit y figurer (règle R5), c'est un mot de plus.
4. **Garde 25 et lecture (i).** L'artefact de la version 9 « une exactitude de contenu ou réunie au-dessus de 0,55 et au plus M + 2 σ₀ : ni arrêt ni signalement » ne dit pas « ni mention ». Sous la lecture (i) il pourrait le dire ; le mandat ne le demande pas, je ne l'ai pas touché.
5. **Verrou, point (c).** Le contrôle fixe « quatre lignes "nom : valeur", dans l'ordre de R-4123 » ; ni lui ni la décision ne donnent les noms des quatre champs, ni la forme exacte de l'heure (« forme seule (UTC) »). Le texte ne les invente pas ; ils restent au code v5 ou à un mot de la mère.
6. **Verrou, point (e).** Le nom `preenregistrement_sha256` est repris du contrôle ; je ne l'ai pas vérifié dans le code v4.
7. **Remarque 1.** Le contrôle demande à la mère de relire l'option (a) de sa fiche avant de poser la question (si elle nommait un plancher, la remarque tomberait). Ce texte n'en dit rien.
8. **« `lecture` devra recevoir M »** (contrôle, § 7, dernière ligne) n'est pas un des trois ajouts : non porté.

## 7. Mots qui sont les miens, à contrôler

La phrase « Version 10 » de la ligne de version ; l'alinéa « Version 10 » de la section « Contre-lecture » ; les raisons résumées de la recommandation (ii) à la remarque 1 ; la phrase de la remarque 4 sur ce qui différait des propositions de la version 9 ; au point 2 du code v5, « ce qui est à changer pour ces six exactitudes ».

## 8. Laissé tel quel, non fait

- Le statut « brouillon corrigé, à faire contre-lire » ; aucune section « Version 10 » à l'annexe H (le mandat borne la tenue au titre, à la ligne de version, au statut et à la date) : ce que la version 10 porte est dit à la ligne de version.
- La section « Version 9 » de l'annexe H garde « 28 remplacements » et ses mots d'histoire ; les listes « Fichiers à donner » et « Points à vérifier » ne reçoivent pas de ligne pour la version 10.
- Section « Seuil » : les deux mentions du cas « non tranché » de la remarque 1, et le point 1 du code v5 (« attend son mot »), restent.
- Non faits : relecture de la version 10 en entier après l'outil (je m'appuie sur ses contrôles internes et sur le différentiel, 22 lignes changées) ; validateur du gabarit. Mes ajouts ne citent aucun travail publié et ne portent aucun identifiant de modèle ni de session.

## 9. Reste à faire, hors de mon mandat

Verser les fichiers ; inscrire la ligne de la mère et remplacer « à inscrire » par son identifiant ; mot de Lazar sur la remarque 1 ; contrôle du différentiel de la version 9 à la version 10 par un autre modèle ; code v5 et sa vérification ; erratum du commit ; scellement par la mère.

*Rédacteur neuf, modèle F.*

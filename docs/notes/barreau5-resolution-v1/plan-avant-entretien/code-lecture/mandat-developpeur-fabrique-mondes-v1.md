# Mandat du développeur de la fabrique des mondes de l'épreuve à vérité plantée (barreau 5) — v1

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 03:40Z. Pièce de travail.

Destinataire : un développeur neuf, Claude Opus 5.5, qui n'a pas écrit le programme de lecture. C'est une pièce d'instrument : contre-lecture par un autre modèle (Fable 5.2), puis vérification des corrections par le même contre-lecteur.

---

Le texte du plan est scellé : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`). Son point 11 veut une **épreuve à vérité plantée du programme de lecture**, jouée après le gel de ce programme et avant toute ouverture. Le programme figé y est joué sur des mondes fabriqués à lois inventées, à dix familles.

Les mondes sont tirés par un agent qui n'a pas écrit le programme. Tu écris la fabrique de ces mondes.

## Pièces (vérifie chaque empreinte)
- **Le texte scellé.** Lis seulement :
  - « Métrique », « Seuil » ;
  - « Plan d'analyse », points 8 à 13 et 17, **le point 11 en entier**, avec sa table des mondes V0 à V12 ;
  - « Critères de lecture gelés », « Ce que dira chaque issue au jury ».
  Ne lis pas « Ce que le rédacteur savait avant d'écrire » ni « La question » : ces passages citent des résultats que tu n'as pas à voir.
- **L'addendum 1**, candidat au scellement : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-candidat-scellement.md` (`2afa2186c9f11e0a477cdf628348d2cad3bce90de5933597ff09a4a3048499e4`). Il fixe cinq points ; deux choix y attendent le mot de Lazar ce matin. Suis-le tel qu'il est, et dis dans ton rapport ce qui changerait si Lazar choisit autrement.
- **L'interface d'entrée du programme de lecture**, et elle seule :
  - la section 1 du rapport v3 du développeur de la lecture : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-developpeur-code-lecture-v3.md` (`b9c77d67e174d9a090b02a55ca9649b15e7fd79e1a1d3b04698ad83be222554e`) ;
  - le commentaire de tête de `src/controle_ia/barreau5_familles/lecture_v1.py`, qui documente les fichiers d'entrée : scores par action et par jeton, déplacements moyens, coûts, étiquettes, lignes de registre.
- **Ce que tu ne lis pas** : le reste de `lecture_v1.py`, en particulier le dénombrement, la table des issues, les mises à l'échelle et les gardes. Une fabrique qui recopierait la logique du programme ne l'éprouverait pas. Si l'interface ne te suffit pas pour écrire un monde, dis-le dans ton rapport, sans lire le reste.

## Ce que tu écris
1. **`src/controle_ia/barreau5_familles/epreuve_verite_plantee_v1.py`** : la fabrique des mondes V0 à V12 du point 11.
   - Chaque monde est planté **au niveau des scores par jeton et des déplacements moyens**. Le programme de lecture y calcule lui-même les produits, les facteurs et les mises à l'échelle de E2a et de E2b.
   - Les écarts s'expriment en écarts types de la différence d'une famille à l'autre, comme le dit le point 11.
   - Dans V3, V8, V9 et V12, plante un bruit propre à chaque membre, au niveau des scores par jeton. Sans lui, des restes d'arrondi tous du même signe font sortir « sabotage » à tort.
   - Ajoute des mondes où les coûts sont illisibles chez un seul membre (règle 2 de l'addendum). Ils servent la lecture ; ils n'ajoutent aucune épreuve.
   - Chaque monde est écrit dans l'arbre exact que lit le programme, sous l'interface neuve : un fichier de scores par jeton par série. Un monde écrit à l'ancienne forme serait refusé.
   - La vérité de chaque monde (issue attendue, motif attendu, quantités plantées) est écrite à part. Son empreinte est engagée **avant** le passage du programme.
   - Graines : `numpy.random.SeedSequence`, dérivées par monde (R9), avec une entropie passée en argument et consignée.
2. **Un juge des mondes**, distinct de la fabrique. Il compare les issues rendues par le programme aux vérités engagées, et applique les règles gelées de la colonne « règle gelée » du point 11 : nombres de mondes, seuils « au plus » et « au moins ». Il rend « passée » ou « manquée », règle par règle.
3. **Les essais** : `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py`.
   - Chaque monde produit bien l'arbre attendu et une vérité engagée.
   - Les mondes V7 (artefacts) produisent les quatre refus attendus.
   - Le juge rend « manquée » sur un programme volontairement faux, de ta fabrication, et « passée » sur un programme qui rend la vérité, lui aussi de ta fabrication. Le vrai programme de lecture n'est jamais joué par tes essais.
   - Ajoute un passage de mutations sur la fabrique et le juge.

## Ce que tu ne fais pas
- Tu ne joues pas l'épreuve elle-même sur le programme de lecture. Elle se joue après le gel (`CODE-LECTURE-B5F`), sous une entropie neuve, avec les trois rôles du point 11.
- Tu ne modifies aucun fichier existant du paquet.

## Règles
- **Aucune donnée.** Rien de `diag/`, aucun score réel, aucune activation, aucune transcription. Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis. Rien de la branche de la formation.
- **Fichiers interdits** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ». Rien sous `/root/.claude/`.
- **Pas de recherche large.** Aucune commande de liste ni de recherche récursive sur une racine large ; ouvre chaque fichier par son chemin entier. Ne traverse jamais un dossier `archives-reponses-modeles/`.
- **Pas de code en ligne passé à l'interpréteur**, ni `python -c`, ni `python -`. Écris un fichier dans ton bloc-notes et lance-le par son chemin. Redirige toute sortie longue vers un fichier de ton bloc-notes.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif.
- **Une commande simple à la fois.**
- **Écriture** : tes fichiers seulement, par les outils d'écriture et d'édition.
- **Ni réseau, ni dépense, ni commit.**
- **Essais** : seulement tes fichiers d'essais neufs. Temporaires dans `/dev/shm`, effacés à la fin par leur chemin écrit en toutes lettres.
- **Refus** : au premier refus d'outil, arrête-toi et dis-le.

## Sorties
- Le module, ses essais, et le rapport scellé `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-lecture/rapport-developpeur-fabrique-mondes-v1.md`. Le rapport donne :
  - l'interface suivie ;
  - les mondes, un par un, avec la règle gelée de chacun ;
  - ce qui changerait selon les choix de Lazar sur l'addendum ;
  - les empreintes ;
  - les essais et les mutations.
- Tes outils dans `code-lecture/outils-developpeur-fabrique-mondes-v1/`.
- Commande de scellement : `cd /home/user/controle-ia-travail && PYTHONPATH=src .venv/bin/python -B -m controle_ia.scellement sceller <fichier>`.
- Écris au fil de l'eau, et scelle chaque état.

## Rends
1. La phrase exacte de ton invite système qui nomme ton modèle.
2. Les chemins et les empreintes de tes fichiers.
3. Dix lignes au plus : ce qui est fait, ce qui manque, les essais et les mutations, ce que l'interface ne t'a pas permis d'écrire.

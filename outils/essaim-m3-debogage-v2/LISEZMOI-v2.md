# Essaim de Gemini, version déboguée v2 et enveloppe sous le contrat du noyau

Écrit le 24 octobre 2026 par la session Claude Code du dépôt (lignée « session-depot »), sur le GO de Lazar reçu vers
15:23 UTC : « go pour l'enveloppe et la confrontation des deux essaims ». Branche `outils/essaim-m3-debogage-v2`,
jamais `main`. La v1 reste intacte sur `outils/essaim-m3-debogage-v1` (`fe56b03`), avec son `LISEZMOI.md`, qui vaut
pour tout ce que ce fichier ne dit pas. **Rien n'a tourné en réel** : aucune clé, aucune dépense.

## 1. Ce qui change depuis la v1

**Module commun `m3_commun.py`** (corrections CL-01 à CL-04 de la contre-lecture de « conv-audit », acceptées) :

| constat | v1 | v2 |
|---|---|---|
| CL-01 | un modèle servi différent du modèle demandé restait `ok` et entrait dans les taux | statut `modele_non_conforme`, jamais `ok`, compté à part |
| CL-02 | la clé Gemini était dans l'adresse (`?key=`) | en-tête `x-goog-api-key` ; la clé n'apparaît dans aucune adresse ni aucun journal |
| CL-03 | un refus d'interface (texte vide) tombait en `vide`, et le compte des refus était toujours nul | statut `refus` (`refusal` d'Anthropic ; `SAFETY`, `PROHIBITED_CONTENT`, `BLOCKLIST`, `SPII` de Gemini), compté sur tous les appels |
| CL-04 | Anthropic sans température, Gemini avec : asymétrie non dite | dite dans chaque rapport ; températures réellement envoyées par lignée dans `resume_run.json` |

**Analyse spectrale : port exact du moteur.** Le moteur du dossier 17, enfin lisible sur la quarantaine `33048ad`,
définit `cholesky_dpp_and_onsager_cavity_in_H_math` (lignes 75 à 163). Les scripts appelaient
`spectral_gram_analysis_massive`, qui n'existe pas : c'est confirmé, leurs valeurs « Onsager » étaient des
constantes de secours. La v1 calculait un indice voisin ; la v2 porte la fonction du moteur telle quelle. Contrôle de
fidélité : pour une seule contribution, le port donne 1,2528, la valeur que le substrat de Gemini consigne.

**Enveloppe `organisme/`**, qui remplace pour cette lignée l'enveloppe v1 écrite par « conv-audit » : voir
`organisme/CONCEPTION.md`. Elle suit le moteur (mitose par vagues de 8, 16, 24 cellules ; lignées et températures de
Halton ; arrêt spectral aux seuils 0,42 et 0,12 ; sondes d'écart ; extraction par tranches de 14 ; synthèse ; mémoire
spectrale) et déclare huit écarts imposés ou rendus nécessaires par le contrat.

## 2. Ce que corrige l'enveloppe v2 par rapport à l'enveloppe v1

| n° | enveloppe v1 (`organismes/gemini-v2/`, `12217d6`) | enveloppe v2 |
|---|---|---|
| E-01 | les castes ne voient que les douze premiers exemples d'entraînement : dans la banque du noyau, rangée famille par famille, c'est une seule famille | exemples stratifiés : quatre par famille et par étiquette |
| E-02 | deux à six castes, une seule sonde d'écart : ce n'est plus l'essaim du moteur | mitose du moteur dans la part de budget de l'étage, jusqu'à six sondes |
| E-03 | pas de synthèse M0 : l'étiquette « M0 » nomme les réponses | synthèse M0 rétablie, guide de décision gardé en mémoire |
| E-04 | une tâche sur deux étiquetée par Opus, l'autre par Gemini : la lignée change d'une tâche à l'autre | un seul étiqueteur, l'arbitre du moteur, par lots de 8 |
| E-05 | mémoire spectrale absente | mémoire du plugin d'origine, projetée et nourrie |
| E-06 | métrique « capacité de Shannon-Gram » choisie par l'auteur de l'autre essaim, indice de diversité sans lien avec la tâche | métrique élaborée par l'essaim lui-même (`metrique/`, nouveau contrat), validée avant de passer au successeur ; l'indice natif reste dans `metrique_proposee.json`, déclaré descriptif |
| E-07 | aucune garde de temps : le bac à sable coupe l'organisme avant qu'il écrive ses réponses | exploration bornée à 55 % du temps ; réponses écrites après chaque lot |
| E-08 | statuts du noyau fondus : refus et modèle non conforme lus comme `vide` ou `echec_api` | un statut par cas |

## 3. Tests et mécanique

```text
$ python -m pytest -q tests
......................................                                   [100%]
38 passed in 9.95s
```

- 28 tests du module commun et des trois scripts, à blanc ;
- 10 tests de l'enveloppe, dans un sous-processus `python -I -s` comme le lanceur du noyau, avec un faux `noyau_client` :
  génération 0 de bout en bout, exemples des deux familles, lignées et hybrides du moteur, refus et modèles non
  conformes comptés à part, plafond du noyau, garde de temps, mode confrontation, héritage de la mémoire et de la
  métrique à la génération 1, métrique invalide refusée.

**Sous le noyau de « conv-audit »** (`outils/essaim-m3-refonte-v1-travail`, `7b4deff`), en simulation, sans réseau ni
clé : `python -m essaim_m3 simuler --generations 2 --appels-max 60 --temps-max 300 --graine 20261024
--organisme-amorcage <dossier de l'enveloppe> --especes GEMINI_ARGON CLAUDE_OPUS_5_5 --confronter`.

| mesure | valeur |
|---|---|
| amorçage | organisme valide, deux lignées |
| générations | deux par lignée, toutes au statut OK |
| appels de la génération 0, lignée Opus | 57 pour un plafond de 60, tous au statut OK |
| mitose | deux vagues, 24 cellules, arrêt sur le budget de l'étage |
| réponses aux tâches | aucune |
| métrique | refusée par la garde de validation |
| confrontation croisée | non applicable, faute de métrique |

Les deux zéros ont une même cause : le simulateur ne répond qu'aux formats de l'organisme d'essai du noyau (une tâche
par appel, « EXTRAIT : … CONNAISSANCES », extraction et vérification à son format). Il ne comprend ni l'étiquetage par
lots ni le format de fichiers de la métrique. **La simulation teste la mécanique ; elle ne peut pas comparer les deux
conceptions.** Tout score simulé est hors de toute décision.

## 4. Ce qu'il manque pour la confrontation réelle

1. **Le noyau ne lance un organisme fourni qu'en simulation** (`--organisme-amorcage`). Le mode réel n'amorce que des
   organismes écrits par les espèces. Il faut une option qui fasse entrer l'essaim de Gemini comme lignée à part
   entière, au même budget.
2. **La règle « attaques par une autre famille de fournisseur »** ne s'applique pas telle quelle à un essaim qui
   utilise les trois espèces. Lecture proposée, à Lazar : les deux conceptions sont les deux « familles » de la
   confrontation ; la métrique de chacune s'applique aux sorties de l'autre.
3. **Le préenregistrement** : brouillon v1 de « conv-audit » en contre-lecture par un relecteur neuf (R2) ; scellé
   ensuite, avec les tâches réelles gelées avant l'amorçage.
4. **Les clés du programme** : aucune n'est dans cette session ni dans celle de « conv-audit ». Le run réel se lance là
   où Lazar les pose (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, jamais `RR_*`).
5. **Le GO de dépense sur devis** : le brouillon chiffre environ 4 USD pour une répétition générale, 85 USD en version
   réduite, 250 USD en version complète.

## 5. Constats de la lecture du moteur, utiles à l'audit

- Le moteur lit `RR_ANTHROPIC_API_KEY` et `RR_ANTHROPIC_WORKSPACE_ID` (lignes 24 à 27) : tous les appels Anthropic
  du dossier 17 sont partis avec la clé d'un autre projet.
- Il désactive l'invite d'identification de git (lignes 18 à 20) : c'est ce qui a fait échouer la deuxième poussée
  de Lazar.
- `atomic_merge_and_save_substrate` ne renvoie rien et avale ses erreurs (lignes 474 à 525) : c'est le plantage de la
  phase 3 de la découverte.
- La « mitose » n'apprend rien : lignées par indice, températures de Halton, cinq axes écrits en dur ; ses cellules
  « hybrides » sont des appels uniques étiquetés hybrides (lignes 576 à 581).
- Le fichier « certifié » du test pascalien (`RESULTATS_CERTIFIES_AB_TEST_PASCALIEN_EVAL_AWARENESS.json`, passe de
  15:41, heure de Paris) a 17 réponses vides sur 18 au bras coercitif. La seule réponse non vide est un refus, que le
  détecteur n'a pas reconnu. Au bras maïeutique, les modèles signalent que l'invite était tronquée.

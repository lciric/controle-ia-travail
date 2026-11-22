# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHj5paqM5hyzhSZGyvCu`
- Heure (UTC) : 2026-11-22T09:31:30Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 64000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/relecture-fable-criteres-v14/consigne-relecture-fable-criteres-v1.md` — sha256 7f71028e5b8e7c03f7717a845094735f3841605ef7ebf1623e18ef3e7ebe0919 (compagnon : vérifié)
  - correction : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/relecture-fable-criteres-v14/procedure-v14-extrait-sections-7-8.md` — sha256 0476b7ce47d76b420b703b6c40429510043e729b7e2d720e57faf645411306cc (compagnon : vérifié)
  - correction : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/relecture-fable-criteres-v14/conformite_outillage_v2-copie.py.txt` — sha256 eb56ff85ae66b588da00d8f19c793ffd3699a060f7892bd77162ce61c381e901 (compagnon : vérifié)
  - remarques : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/relecture-fable-criteres-v14/remarques-verification-v1.md` — sha256 7f6c8b30c858422ca0b62d2e9b546a5b734dc35ec19a0db744d4af1fc129cf48 (compagnon : vérifié)
- Empreinte de l'invite envoyée : f4393c2e4977c95569478a9a0e7975dc8e2376ab177cc50dbd715782eb567a24
- Jetons : entrée 22108, sortie 34539 (dont réflexion 31057), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.558424 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**Bilan.** Points 3, 4 et 8 gardés ; points 1, 2, 5, 6 et 7 corrigés. Aucune correction n'ouvre un chemin vers « conforme ». Elles demandent une procédure et un code de version neuve, rejoués hors machine avant le cinquième essai. J'ai jugé à la seule lecture des deux copies : l'épreuve v9, les attendus v8 et les pilotes ne sont pas servis, et je n'ai rien exécuté.

## 1. § 8.2, sortie de lui-même en code 137 (quatre conditions)

**Décision** : garder les quatre conditions, toutes exigées ; corriger la troisième, qui n'est pas décidable.

- ANCIEN : « temps de processeur de l'unité de l'ordre de quelques dizaines de millisecondes »
- NOUVEAU : « temps de processeur de l'unité inférieur à 1 s »
- Code : la règle ne change pas ; l'épreuve doit appliquer cette même borne.

**Raison** : « de l'ordre de quelques dizaines de millisecondes » laisse le lecteur trancher après avoir vu la sortie, ce que l'en-tête de la section 8 interdit. La quatrième condition est juste : sans « SORTIE 137 », rien ne distingue une sortie voulue d'un processus tué qu'aucun incident n'aurait classé.

**Confiance** : élevée sur le maintien des quatre conditions ; moyenne sur le chiffre de 1 s, que je pose d'après une seule mesure (31 ms) et la limite de 5 s. Si l'épreuve v9 porte déjà une borne chiffrée, c'est elle qu'il faut écrire.

## 2. § 8.7 entier (trois issues, aucune tolérance, épreuve entière, pièce mal formée)

**Décision** : garder la construction ; une correction, car le contrôle des tentatives réseau se tait quand il ne trouve rien.

- ANCIEN : « une tentative réseau dont le programme n'a pas été lancé (§ 8.2 : « non éprouvé ») »
- NOUVEAU : « une tentative réseau dont le programme n'a pas été lancé (§ 8.2 : « non éprouvé »), ou l'une des trois tentatives réseau (`reseau-curl-ip`, `reseau-python-tcp`, `reseau-dns`) introuvable dans les extraits de sortie »
- Code : dans `lire_epreuve`, après la boucle des tentatives, marquer « non établi » chacune des trois tentatives absente de `a_dire`.

**Raison** : la règle ne marque « non éprouvé » que si elle trouve le détail fautif. Un extrait absent, tronqué ou d'un autre format donne donc « conforme » avec `tentatives_reseau` vide, alors que le § 8.2 exige de lire ce détail même quand le cas est conforme.

**Confiance** : assez élevée sur le défaut, lu dans le code. Moyenne sur les noms exacts dans les pièces réelles, que je n'ai pas ; le rejeu hors machine sur les pièces du quatrième essai le dira.

## 3. Pilote « apres » en code 0 avec un pas `noyau` non conforme, lu « non établi »

**Décision** : garder tel quel.

**Raison** : les deux pièces se démentent et rien dans les sorties ne dit laquelle est fausse ; lire « non conforme » serait arbitrer pour l'une. « Non établi » bloque autant (§ 8.7, point 5), ne mène jamais à « conforme », et son motif nomme le pas `noyau` à `conforme` faux.

**Confiance** : assez élevée. Elle tient à ce que « non établi » ne soit jamais traité plus légèrement que « non conforme » dans la suite.

## 4. Cas du noyau à `ok` vrai avec des écarts, lu comme contradiction

**Décision** : garder tel quel.

**Raison** : un cas qui dit à la fois sa réussite et des écarts ne peut être lu ni « tenu » (un écart passerait) ni « non tenu » (la pièce n'affirme pas l'échec). La même lecture vaut déjà pour l'épreuve, et une règle différente au noyau serait une tolérance cachée.

**Confiance** : élevée.

## 5. Codes 124 et 255 du pilote « avant »

**Décision** : trancher pour « non établi » ; tout autre code non nul reste « non tenu ».

Dans le § 8.7, point 2, « non tenu » :
- ANCIEN : « pilote « avant » en code non nul (codes 124 et 255 compris : point 3 de la liste de la section 7, non tranché) »
- NOUVEAU : « pilote « avant » en code non nul autre que 124 et 255 »

Dans le § 8.7, point 2, « non établi » :
- ANCIEN : « code 124, 255 ou tout code hors de la liste »
- NOUVEAU : « code 124, 255 ou tout code hors de la liste ; pilote « avant » en code 124 (borne de temps) ou 255 (connexion tombée) : rien n'est lu après lui »

Dans la section 7 :
- ANCIEN : « **Point noté, non tranché** : la v14 garde la lecture de la v13. »
- NOUVEAU : « **Tranché à la relecture** : codes 124 et 255 du pilote « avant » lus « non établi » ; tout autre code non nul reste « non tenu ». »

Code : dans `lire_pilotes`, marquer « non établi » les codes 124 et 255 du pilote « avant » et « non tenu » les autres codes non nuls, sans rien lire après dans les deux cas, avec un essai hors machine pour chacun.

**Raison** : selon la règle elle-même, « non tenu » demande une lecture écrite qui dise non conforme ; une borne de temps ou une connexion tombée ne montre aucun comportement de l'outillage. Les deux issues bloquent autant, donc rien ne s'ouvre, et les mêmes codes ont la même lecture qu'à l'épreuve.

**Confiance** : assez élevée. Elle suppose que le pilote « avant », non servi, ne rend jamais 124 ou 255 de lui-même pour dire un essai en échec.

## 6. Écart entre texte et code sur le cas en échec dans une pièce incohérente

**Décision** : le texte l'emporte et le code s'aligne ; le texte précise ce que « cohérente » veut dire.

- ANCIEN : « un cas de l'épreuve en échec, dans une pièce cohérente (code 1, statut « non conforme »), hors d'un genre mort »
- NOUVEAU : « un cas de l'épreuve en échec, hors d'un genre mort, dans une pièce cohérente : code 1 et statut « non conforme », ou code 3 et statut « épreuve morte », `conforme` faux dans les deux cas ; dans toute autre pièce, un cas en échec n'est lu ni pour ni contre (« non établi ») »
- Code : dans `lire_epreuve`, ne marquer « non tenu » les cas en échec que si code et statut s'accordent (1 et « non conforme », ou 3 et « épreuve morte ») et que `conforme` est faux ; sinon les nommer dans un motif « non établi ».

**Raison** : le code applique déjà « ni pour ni contre » quand `conforme` vrai dément un cas en échec. Ne pas l'appliquer quand le code et le statut se démentent est une incohérence, et la section 7 (mutations) suppose d'ailleurs cette lecture. J'ajoute le code 3 parce que « hors d'un genre mort » n'a de sens que dans une pièce qui porte un genre mort, et que le code lit déjà ainsi les cas des genres vivants.

**Confiance** : élevée sur le sens de l'alignement. Moyenne sur l'ajout du code 3 : je ne sais pas quel code et quel statut l'épreuve v9 rend quand un genre mort et un cas en échec coexistent.

## 7. `genres_morts` et `controles_hote` absents

**Décision** : oui, « non établi ».

- ANCIEN : « `ok` un booléen ; un extrait de sortie un texte) »
- NOUVEAU : « `ok` un booléen ; un extrait de sortie un texte), ou `genres_morts` ou `controles_hote` absent (une liste vide s'écrit, elle ne se suppose pas) »
- Code : dans `lire_epreuve`, lire ces deux champs sans valeur par défaut, pour que leur absence tombe dans le contrôle des champs mal formés déjà écrit.

**Raison** : le § 8.1 lit `controles_hote` « vide attendu » ; un champ absent n'est pas un champ vide, et la valeur par défaut lit ce silence en faveur de l'outillage. Avec le point 2, ce sont les deux seuls endroits que j'ai trouvés où la règle tient une absence pour un accord.

**Confiance** : élevée sur le principe. Je n'ai pas pu vérifier que l'épreuve v9 écrit toujours ces deux champs ; le rejeu hors machine sur les pièces réelles le dira avant l'essai.

## 8. Étape de concordance (§ 8.7, point 6)

**Décision** : garder tel quel.

**Raison** : c'est un contrôle en partie double où aucun côté n'est repris pour rejoindre l'autre et où un désaccord devient un nœud pour la mère. L'empreinte prouve que le fichier n'a plus bougé depuis qu'elle a été prise, pas qu'il a été écrit avant la règle ; c'est acceptable parce qu'un accord ne déclare rien.

**Confiance** : assez élevée. L'ordre « avant de lancer la règle » repose sur la discipline du poste, et le lecteur neuf doit le savoir.

FIN DE LA RÉPONSE

# Vérification de cloisonnement de l'extrait du lanceur pour le développeur — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/extrait-lanceur-etape-discretion-pour-le-developpeur-v1.md`, `c1ddfe24b99a62ef7fc492293c9a8064a6fee2a12dbd8083a8f5888fb3f345ca`. Le compagnon est conforme.
- **Comparée à** : la ligne du lanceur et la ligne du registre en 13.2 de `prereg/T0.7-organismes-discrets-v-a-v2-brouillon37.md`, lignes 1407 et 1408.
- **Lu aussi** :
  - le module `src/controle_ia/organismes_discrets/graines_bras_a_v12.py`, `381878cd7ef7e23c6edb9fb4cf826fd8a1eb652b5497da8a39e99b2bd5146a8b`, code de la relance : noms, en-têtes et signature de la porte ;
  - `graines_bras_a_v4.py`, qu'il importe : recherche de mots seulement ;
  - la ligne GO-2026-11-19-97 de `origin/main:registres/go.md`.
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a pas écrit la pièce. Classe C. Mêmes interdits : aucun interne de moniteur ouvert.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir après retouches

L'extrait lui-même est propre :
- aucune empreinte ;
- aucun chemin interdit, hors les motifs d'exclusion ;
- aucune règle de lecture des nombres, ni rien de ce que décident ses réponses ;
- fidèle à la ligne 13.2 du brouillon 37.

**Une retouche est nécessaire, sur la section 3.** Elle envoie le développeur appeler `graines_bras_a_v12.py`. Ce module, et `graines_bras_a_v4.py` qu'il importe, portent dans leur source :
- deux chemins de brouillons du texte qu'il ne doit pas ouvrir ;
- des pièces du plan d'analyse, dont une règle de verdict : les doses qui comptent au verdict.

S'il ouvre le source pour l'appeler, il les lit.

## 1. Contrôle par programme de la pièce

- **Empreintes** : aucune chaîne hexadécimale de 8 signes ou plus.
- **Chemins et noms de fichiers.** Les seuls jetons sont :
  - les trois motifs d'exclusion de la ligne 6 ;
  - les deux fichiers de sortie, `lecture-commune-moniteurs-bras-a.json` et `rangs-par-unite-moniteurs-bras-a.jsonl` ;
  - la clé `lec6/{tâche}` ;
  - `src/controle_ia/organismes_discrets/graines_bras_a_v12.py`.
- **Ligne de GO citée.** GO-2026-11-19-97 existe sur `origin/main`. Son objet est « écart à R9 accordé pour la table des identifiants opaques », exactement la phrase qu'attend la porte.

## 2. Les points à regarder

**2.1 — Le module `graines_bras_a_v12.py` (retouche nécessaire).**
- *Ce que porte son source.*
  - Son en-tête cite `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`. Celui de `graines_bras_a_v4.py` cite `…-brouillon17.md`.
  - Il nomme des usages de l'analyse : un test de tendance de Page (6.9), « intervalles seulement rapportés (métrique 3) », les vingt clés de l'aire conditionnelle tirées par l'instance d'analyse.
  - Il porte toute la logique du constat de lancement : formes de refus, reconnaissance d'une révocation par son sens, phrase d'une livraison refaite.
  - Par `import *`, il reprend `graines_bras_a_v4`, qui porte `DOSES_VERDICT = (0.5, 0.75, 1.0)`. C'est une règle de verdict : les doses qui comptent. Un développeur de moniteurs ne doit pas la connaître avant sa dernière livraison.
- *Ce que cela permet.* Rien de cela ne lui dit ce qu'un moniteur devrait repérer. Mais le module lui ouvre le plan d'analyse, et deux chemins de texte, que la décision de Lazar lui ferme jusqu'à sa dernière livraison.
- *Retouche.* Donner dans la pièce ce qu'il faut pour appeler la porte sans ouvrir le source :
  - le nom de la fonction, `admettre_l_entropie_propre_de_la_table_des_identifiants` ;
  - ses arguments : `entropie_de_la_table`, `entropie_du_bras`, puis, nommés et sans défaut, `reglage`, `go_de_lazar`, `registre_fige`, `sha256_au_scellement`, `registre_courant` ;
  - la valeur à passer à `reglage` : la constante `ECART_A_R9_ACCORDE` ;
  - ce qu'elle rend : une ligne à consigner au manifeste ; un refus lève `GardeArret`.
- *Puis ajouter à la ligne 6 de la pièce, et à sa pièce des demandes* : « n'ouvre pas le source des modules `src/controle_ia/organismes_discrets/graines_bras_a_v*` ; appelle-les par les noms donnés ici. La contre-lecture de ton lanceur, par un autre modèle, vérifie l'appel sur le source. »
- *Même chose pour les graines.* La section 1 lui demande des graines « tirées de l'entropie de la configuration du bras », et l'étape 3 la clé `lec6/{tâche}`. Pour les tirer sans ouvrir la table des clés, il lui faut aussi la fabrique `tirage_de(cle_entiere, entropie)`, `generateur_pour(tirage, usage, cle_exigee)`, et la forme entière de la clé, à écrire dans la pièce. Sinon il répondra « ne peut pas s'écrire sans en savoir plus », ce que la pièce prévoit, ou bien il ouvrira le source.
- *Autre voie, plus sûre si elle est possible.* La relance écrit un petit module d'entrée, versionné, qui n'expose que ces fonctions et constantes, sans renvoi au texte dans ses en-têtes. Le lanceur n'appelle que lui.

**2.2 — La garde d'équivalence du jeu d'épisodes (section 6, point 1).**
- Elle porte sur l'échantillon passé à une garde des lanceurs qui jouent des épisodes. Le constat « échantillon vide, ne mesurait rien » vient d'une lecture du côté habilité.
- Rien sur les moniteurs ni sur une lecture des nombres. La réponse demandée est un fait ou une taille. **Admis.**

**2.3 — La pièce qui rejoue un lot (section 6, point 2).**
- Elle touche la question du rejeu au bit près, posée au seul lecteur habilité (demande 25). La pièce ne dit pas pourquoi cette question compte, et n'écrit aucune phrase sur ce qu'un moniteur pourrait repérer.
- Le développeur a lui-même relevé ce rejeu non vérifié dans sa note sur le lanceur du bras.
- La forme de sortie est bornée à deux comptes. « Ne l'écris que si la session principale te la commande » ne trahit pas de suite. **Admis.**

**2.4 — Les clés du registre (étapes 1 et 5).**
- `TABLE-B-BRAS-A-V2`, `ISSUE-MOTS-ET-COUT-BRAS-A` et `OUVERTURE-MONITEUR-BRAS-A` sont les clés des textes transmis par le côté habilité. Le brouillon 37 le dit à sa ligne 1408. Ce sont des noms, sans contenu.
- Aucune n'est encore inscrite sur `origin/main`. Le lanceur ne fait que vérifier qu'elles sont présentes. **Admis.**

**2.5 — « celle qui sert au verdict » (ligne 5).**
- La mention figure déjà dans sa pièce des demandes et reprend la décision de Lazar. Elle ne dit rien de la règle de verdict. **Admis.**

**2.6 — Les autres points de la pièce.**
- *Section 4, empreinte du texte scellé dans la configuration.* Une empreinte n'ouvre rien, et il lui est interdit d'ouvrir le texte. **Admis.**
- *Section 4, statistique de l'agrégateur laissée à la configuration ; jetons de fin du moniteur boîte noire par action.* Ce sont de la forme et du relevé. **Admis.**
- *Section 2, étape 3, sous-échantillon du juge sous `lec6/{tâche}`.* La pièce ne donne ni le nombre de positions ni la règle « appliquées aux cinq conditions » du texte. C'est sans effet sur le cloisonnement, mais il lui faudra ces nombres pour tirer : à donner avec la retouche 2.1, ou par la configuration.
- *Section 5, dossier du fichier des rangs.* La réponse demandée est un chemin et un nombre, déjà permis. **Admis.**
- *Fidélité.* Les sections 1 et 2 reprennent à la lettre la ligne 13.2 du brouillon 37 et la phrase du côté habilité. Elles n'ajoutent ni règle de lecture ni attente.

## Retouches, liste courte

1. **Section 3 (nécessaire).** Donner la signature de la porte de l'écart à R9 (`admettre_l_entropie_propre_de_la_table_des_identifiants`, ses sept arguments, la constante `ECART_A_R9_ACCORDE`, ce qu'elle rend, `GardeArret`). Faire de même pour les fabriques des graines (`tirage_de`, `generateur_pour`, la clé entière `lec6/{tâche}`, le nombre de positions). Interdire d'ouvrir le source de `src/controle_ia/organismes_discrets/graines_bras_a_v*`, qui cite deux brouillons du texte et porte des pièces du plan d'analyse, dont les doses du verdict. La contre-lecture du lanceur vérifie l'appel. À défaut, un petit module d'entrée sans renvoi au texte.
2. **Ligne 6 de cette pièce et ligne 6 de sa pièce des demandes** : ajouter ce motif d'exclusion.

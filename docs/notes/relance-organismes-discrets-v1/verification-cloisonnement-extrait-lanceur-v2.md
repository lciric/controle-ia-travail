# Vérification de cloisonnement de l'extrait du lanceur, version 2 — v1

- **Pièce vérifiée** : `docs/notes/relance-organismes-discrets-v1/extrait-lanceur-etape-discretion-pour-le-developpeur-v2.md`, `85cdce02198cae95be96e888bc34d5fe1863bb44be8d6e27c95e0aaa2c0620f7`. Le compagnon est conforme. Elle est comparée à la v1.
- **Module d'entrée lu** : `src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v1.py`, `8415b9b6ba1befafd5c05d0f5c373aa7c932f4618dd5537fddcb48ec4a285a0e`. Le compagnon est conforme.
- **Vérification de référence** : `verification-cloisonnement-extrait-lanceur-v1.md`, `85eac063bb9b2240c04a063a9e6d129db0bff08014b2dab72f566c48501d1b91`.
- **Relecteur** : le même agent Claude Opus 5.5. Classe C. Mêmes interdits.
- **Essais faits** : j'ai importé le module d'entrée et provoqué deux refus, pour voir ce qu'il expose et ce qu'affichent ses messages. Aucun réseau, aucun modèle.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir après retouches

L'extrait v2 est propre, et mes deux retouches de la v1 y sont tenues. Le module d'entrée tient sa promesse à la lecture : son texte ne cite aucun brouillon, aucune empreinte, rien du plan d'analyse.

Mais, à l'exécution, il laisse passer ce que l'extrait lui interdit d'ouvrir, par deux voies :
- **le nom `_graines`** reste dans le module. Il donne au développeur le module v12 entier, par simple introspection (`help(entree._graines)`) :
  - ses en-têtes, avec le chemin du brouillon 35 ;
  - `DOSES_VERDICT`, que j'ai vérifié atteignable ;
  - le test de Page ;
- **le message de refus d'un usage inconnu** dans `generateur_pour` énumère les usages de l'analyse.

Ce sont deux retouches de code d'une ligne chacune. Elles demandent une vérification courte du module corrigé, pas de nouvelle relecture de l'extrait.

## 1. Les retouches de la v1

| n° | retouche | tenue ? | où |
|---|---|---|---|
| 1 | Donner la signature de la porte et des fabriques ; ne pas ouvrir le source des modules de graines ; l'appel est vérifié par la contre-lecture, ou bien un module d'entrée sans renvoi au texte | **oui** : signature complète en table, avec la constante, ce qu'elle rend et `GardeArret` ; `tirage_de` et `generateur_pour` décrits ; module d'entrée écrit | extrait, section 3 ; module d'entrée |
| 2 | Motif d'exclusion `graines_bras_a_v*` à la ligne 6 | **oui** pour l'extrait. **À vérifier pour sa pièce des demandes**, dont la v8 ne le porte pas : il faut une v9, ou renvoyer à l'extrait | extrait, ligne 6 |

## 2. Contrôle par programme

**L'extrait v2.**
- Aucune chaîne hexadécimale de 8 signes ou plus.
- Les seuls chemins sont :
  - les motifs d'exclusion, dont le nouveau `src/controle_ia/organismes_discrets/graines_bras_a_v*` ;
  - le chemin du module d'entrée ;
  - les deux fichiers de sortie.
- Aucun des mots « brouillon », « prereg », « Page », « DOSES », « aire-cond », « repère » hors des motifs et de la ligne 5, déjà admise.

**Le module d'entrée.**
- Aucune chaîne hexadécimale.
- Son seul jeton de chemin est la forme de clé `bras-a-v2/lec6/{tâche}`.
- Ni « brouillon » ni « prereg ». Il n'importe `graines_bras_a_v12` que par son nom, sans en ouvrir le source.

## 3. Le module d'entrée et ce qu'il peut lui apprendre

**3.1 — Le nom `_graines` (retouche nécessaire).**
- *Constat.* `dir(module)` liste `_graines`, qui est le module v12 lui-même. `entree._graines.DOSES_VERDICT` répond. `help(entree._graines)` imprime l'en-tête, qui cite `prereg/T0.7-organismes-discrets-v-a-v2-brouillon35.md`, ainsi que les commentaires des usages (test de tendance de Page, « métrique 3 »).
- Le trait de soulignement dit « privé », mais ne ferme rien. Pour un développeur à qui l'on a dit « tu peux lire ce module », c'est une porte ouverte sur ce que la ligne 6 lui interdit.
- *Retouche.* Lier les cinq noms gardés (voir 3.3) par `from .graines_bras_a_v12 import …` sans garder le module sous un nom, ou bien finir le module par `del _graines`. Un essai doit vérifier que `dir(module)` ne rend que les noms de `__all__` (plus `annotations`).
- *À noter.* Les objets exposés gardent la trace de leur module d'origine (`tirage_de.__module__`, `__globals__`). Une introspection déterminée retrouvera toujours v12. On ferme la voie visible ; la consigne « n'ouvre pas le source » tient le reste.

**3.2 — Les messages de refus (question posée).**
- *Ce que j'ai vu en provoquant des refus.*
  - Un usage inconnu dans `generateur_pour` affiche : « usage de tirage 'x' hors de ['boot/aire-conditionnelle', 'boot/taches', 'perm/moniteur', 'perm/page'] ». C'est l'énumération des tirages de l'analyse, dont une permutation de Page, et le fait qu'une aire conditionnelle est rééchantillonnée.
  - Une clé hors de la table donne : « hors de la table de la section 6.2 : tirage refusé (garde de 8.4) ».
  - `tirage_de(cle_lec6(...))` donne : « reconnue, mais tirée côté habilité (6.2) — la relance ne la tire pas ».
- *Les numéros de section.* Ils ne sont pas un risque. Seuls, « 6.2 », « 8.4 » ou « 6.9 » ne disent rien de ce que contient le texte, et il ne l'ouvre pas avant sa dernière livraison. Les messages des fonctions qu'il appelle ne citent aucun brouillon, aucun chemin de texte, aucun seuil ni aucune dose du verdict.
- *L'énumération des usages, elle, est un petit risque.* Elle nomme des pièces du plan d'analyse. Elle ne dit rien de ce qu'un moniteur devrait repérer, mais apprend au développeur qu'il existe un test de tendance sur les doses et une aire conditionnelle.
- *Retouche.* Retirer `tirage_de` et `generateur_pour` du module d'entrée. Plus rien ne les appelle : le sous-échantillon du juge est sans objet, la table tire sur l'entropie du système, et la lecture commune reçoit l'entropie du bras par son propre module. L'extrait le dit déjà : « si une étape du lanceur doit elle-même tirer… ». Si une étape en a besoin, la relance ajoutera une fonction d'entrée dédiée, qui enveloppe le refus dans un message neutre. Sinon, envelopper `generateur_pour` pour rendre seulement « usage refusé ».

**3.3 — `cle_lec6`, `EPISODES_PAR_TACHE`, `PAS_PAR_EPISODE`.**
- `cle_lec6` est exposé, mais l'extrait dit de ne pas l'appeler. Mon essai montre que `tirage_de(cle_lec6(...))` est refusé de toute façon (« tirée côté habilité »). Un nom mort, exposé et interdit, ne sert qu'à embrouiller ; sa documentation (« rend la clé du sous-échantillon ») renvoie à un tirage sans objet.
  - *Retouche.* Le retirer, ou en faire une v2 du module d'entrée sans lui.
- `EPISODES_PAR_TACHE` (8) et `PAS_PAR_EPISODE` (10) sont des effectifs déjà connus du développeur : la demande 7 lui donne huit épisodes par tâche. Ce sont des comptes, sans biais.
  - *Remarque.* Si `cle_lec6` est retiré, ils ne servent plus qu'à « vérifier un compte de positions » : les garder est permis.
- Les cinq noms à garder sont donc : `ECART_A_R9_ACCORDE`, `admettre_l_entropie_propre_de_la_table_des_identifiants`, `GardeArret`, `EPISODES_PAR_TACHE`, `PAS_PAR_EPISODE`.

**3.4 — La documentation du module d'entrée.**
- Elle ne décrit que des signatures et des formes. Elle ne dit rien de ce que décident ses réponses ni d'un verdict.
- La porte de l'écart à R9 rend un dictionnaire à consigner tel quel au manifeste. D'après la signature lue en v1, ce dictionnaire porte « l'écart » en clair et l'identifiant du GO. C'est sans interne et sans biais. **Admis.**

**3.5 — L'extrait, étape 3 et section 3.**
- « Le juge d'une autre lignée lit toutes les actions, comme le moniteur boîte noire par action » : c'est un fait de production, utile au lanceur, sans biais.
- Le reste de la section 3 est fidèle à la signature.

## Retouches, liste courte

1. **Module d'entrée, nécessaire.** Ne plus exposer `_graines` : import des seuls noms, ou bien `del _graines`. Un essai vérifie que `dir()` ne rend que `__all__`.
2. **Module d'entrée, nécessaire.** Retirer `tirage_de`, `generateur_pour` et `cle_lec6`, qui ne servent plus. L'énumération des usages de l'analyse que fait le refus de `generateur_pour` sort avec eux. À défaut, envelopper ce refus dans un message neutre.
3. **L'extrait s'aligne.** Retirer de la section 3 le paragraphe « Graines » et la mention de `cle_lec6`, ou les réécrire pour le module corrigé.
4. **Pièce des demandes du développeur.** Porter le motif d'exclusion `src/controle_ia/organismes_discrets/graines_bras_a_v*`, ou y renvoyer à l'extrait.

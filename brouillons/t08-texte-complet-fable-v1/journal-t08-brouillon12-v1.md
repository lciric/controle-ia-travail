# Journal du brouillon 12 du texte de la base boîte noire (T0.8) — v1

- **Nature** : pièce de travail (classe C) ; porte aussi l'erratum 1 du journal du brouillon 11 (section 5). **Auteur** : session `session_013QMayo5SNVbiUW6hGnPrCo` (modèle B), rédacteur des brouillons 11 et 12.
- **Heures (UTC, `date -u`)** : rapport de la contre-lecture 8 et messages de la session mère lus à 19:03 ; brouillon 12 produit vers 19:09 ; journal clos vers 19:15, le 2026-11-22.
- **Ce que la session rend** : le brouillon 12 (candidat 3), `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon12.md`, à vérifier par le contre-lecteur 8. Cinq marqueurs restent. Empreinte : dans le compagnon et dans le message au contre-lecteur.

## 1. Ce qui est arrivé depuis le brouillon 11

- **Contre-lecture 8** (modèle A, session `session_013QMaynYTnoP7ytoW2UMpRB`) : « scellable après corrections ». Rapport `prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon11-cl8-v1.md`, `c3e6b0ee1e7d1d1305d94fb6e7f492cfdc3432dcd49af83043b0d45a3e03e0d9`, empreinte vérifiée contre son compagnon. Un bloquant, au programme de scellement ; huit majeurs ; huit mineurs ; aucun nœud dans les sections gelées.
- **Deux demandes de la session mère** (18:40 UTC, lues après la passation de 18:57) : dire dans le texte la définition de « diffuse » que T0.8 retient, avec sa source, et signaler l'écart avec le brouillon de G1 sans le trancher ; dire si T0.8 préenregistre ou non les bases qu'il reporte.
- **Développeur de l'alignement du code** : lancé par la mère sur la branche `prep/t08-code-aligne-v1`, avec la consigne en version 1.

## 2. Traitement des constats (tous acceptés)

| constat | ce qui est fait |
|---|---|
| **B-1** phrase T5-19 non contrôlée | Le contrôle du gel devient une seule pièce, `controle_gel_t08_v1.py`. Il exige que la plage gelée, noms des marqueurs remis, soit égale à l'octet à celle du brouillon 10, et que celle du brouillon 10 soit égale à celle du brouillon 4 hors la phrase T5-19, dont l'empreinte est épinglée. La phrase est donc tenue dans son texte et à sa place. Programme de scellement en version 2 ; la version 1 reste telle quelle et ne doit plus servir. |
| **M-1** écart entre l'honnête jugé et sa référence | Puce neuve dans la déclaration N-076 : les deux règles gelées qui bornent cet écart, avec leurs bornes ; ce qu'aucune ne voit est dit non borné. Rédaction de l'auteur, plus précise que celle proposée sur les deux moitiés du contrôle d'échangeabilité. |
| **M-2** unités | Horizon et référence comparés à l'unité de l'action, puis à celle de l'épisode. |
| **M-3** errata de N-076 | Lus en entier. L'erratum 1 aligne l'en-tête, la section 0, la section 4 et la section 13 sur des mots de Lazar et sur l'état de N-075 ; l'erratum 2 corrige une empreinte recopiée. Aucun ne touche la section 2 ni son point 4. La déclaration n'a pas à changer pour eux. Cités avec leurs empreintes. |
| **M-4** panne technique | Texte du lecteur repris tel quel : la borne de 400 jetons par action n'est jamais une panne ; une seule relance, si aucune lecture n'a eu lieu. |
| **M-5** renvoi au texte de validité | Texte du lecteur repris tel quel : seuls les noms ont été retrouvés ; pour le fond, le texte scellé prime. |
| **M-6** alignement du code | Le texte et la consigne (version 2) demandent la déclaration, fichier par fichier, des modules importés qui changent, et quatre chemins égaux à l'octet. Relevé fait : entre le commit du code et `main`, tous les paquets que le code importe sont égaux à l'octet. |
| **M-7** calendrier | Ordre de course (pièce de classe A), consignes du lecteur et du juge, garde de calcul éprouvée à blanc, question à Lazar au plus tard le 23 : portés au tableau. |
| **M-8** brouillon d'entrée non épinglé | Le programme de scellement exige l'empreinte du brouillon vérifié et refuse un rapport de vérification qui ne la cite pas. Marqueur neuf dans le texte pour ce rapport. |
| **m-1** à **m-8** | Engagement « au scellement » ; contrôle « n'écrase jamais » avant tout tirage d'entropie, rien de tiré à blanc ; lignes de GO lues nommées, R-2265 dite ; source de validité nommée d'après la section 1 de N-076 ; journal du brouillon 11 corrigé par erratum (section 5) ; GO-2026-11-22-93 cité à l'engagement ; « début de la course » défini ; statut complété. |

**Limite déclarée par le lecteur, levée.** Il n'avait pas pu comparer la phrase T5-19 à celle sur laquelle Lazar a dit « go a ». Comparaison par programme des brouillons 5 à 10 : le fond de la phrase change une fois, du brouillon 5 au brouillon 6 (correction VT5C-04 du vérificateur, le 14 novembre à 03:57 UTC) ; le mot de Lazar est de 06:26 UTC ; le fond est égal à l'octet du brouillon 6 au brouillon 12. Table dans le différentiel, section 2.

**Défaut trouvé en écrivant la version 2 du programme de scellement, que le lecteur n'avait pas relevé.** La version 1 remplaçait la phrase « non scellé » partout dans le texte, donc aussi dans l'annexe qui recopie « à l'octet » l'en-tête du brouillon 10. La version 2 ne change que la ligne « Statut » ; un essai le contrôle.

## 3. Les deux demandes de la mère

- **Qualification « diffuse »** : sous-section neuve. Elle rappelle la définition gelée, donne ses sources (P-015 et B4 corrigée, N-007, DB8-2, DB8-6), et sa portée : DB8-6 écrit que ces bornes ne valent que pour les doses de 7b, « jamais comme définition de « diffus » pour H1, H2 ou G1 ». L'écart avec le brouillon de G1 est mis en table, d'après le seul message de la mère : je n'ai ouvert aucun texte de G1. Rien n'est tranché ; le point est le cinquième de la liste laissée à Lazar, sans recommandation.
- **Bases reportées** : sous-section neuve. T0.8 n'en préenregistre aucune ; G1 ne peut pas renvoyer à ce texte pour elles.

## 4. Vérifications

- Programme du brouillon 12 : 31 opérations, aucune dans une section gelée ; contrôle du gel tenu ; `--verifier` reproduit le brouillon à l'octet.
- Validateur de préenregistrement : seuls les cinq marqueurs restent.
- Essais `essais-controle-gel-t08-v1.py` : 27 conformes sur 27. Le contrôle du gel tient sur le cas sain et arrête huit artefacts : seuil changé, phrase gelée retouchée, phrase T5-19 réécrite, déplacée, doublée, retirée, valeur de marqueur altérée, ligne ajoutée à la liste d'arrêt. Le programme de scellement arrête les mêmes, plus une section non gelée modifiée après la vérification, un rapport de vérification qui ne cite pas le brouillon, un commit court, une ligne de dépense sans la tâche, et un rejeu sur des sorties existantes ; le cas sain écrit un texte sans marqueur, annexe intacte, gel rejoué.
- Non fait : la suite d'essais du dépôt, non jouable dans ce conteneur (bibliothèque de réseaux de neurones absente) ; aucun fichier de `src/` ni de `tests/` n'est touché.

## 5. Erratum 1 du journal du brouillon 11

Le journal `journal-t08-brouillon11-v1.md` reste tel quel (R12). Trois phrases s'y lisent autrement :

1. § 3, point 3 : « éprouvé sur un cas sain et quatre artefacts … : tous arrêtés ». Lire : aucun de ces artefacts ne portait sur la phrase T5-19, que la version 1 du programme de scellement ne contrôlait pas (constat B-1). La version 1 ne doit plus servir.
2. § 4 : « prudent pour qui voudrait dire « diffuse » ». Lire : « ce biais va vers « flagrante », à l'opposé de « diffuse » ». La tournure d'origine regardait un signe (constat m-5).
3. § 6, ligne 5 : l'ordre de course y est dit non bloquant pour le scellement. Lire : c'est une pièce de classe A, à écrire par le rédacteur et à contre-lire avant la création de l'instance ; elle est au calendrier (constat M-7).

## 6. Écarts et accès

- Lus en plus pour le brouillon 12 : le rapport de la contre-lecture 8 ; les errata 1 et 2 de N-076 et dix lignes de sa section 2 ; deux messages de la mère ; la phrase T5-19 des brouillons 5 à 10 ; les noms des paquets qui diffèrent entre le commit du code et `main`. Déclarés dans le texte.
- La passation de 18:57 dit que le processus d'essais « s'est arrêté à son propre délai » : écrit trois minutes avant qu'il ne s'arrête ; vérifié ensuite, il s'est bien arrêté seul à 19:02.
- Aucun refus d'outil depuis celui déclaré à la passation. Aucun registre écrit. Aucun fichier de données, de diagnostic ni de run ouvert ; aucun résultat lu.

## 7. Ce qui reste

1. Vérification des corrections par le contre-lecteur 8 ; brouillon suivant s'il en demande.
2. Alignement du code (consigne en version 2 transmise au développeur), contre-lecture, commit.
3. Ligne du registre sur les gardes de code et VT5-07 : question à Lazar au plus tard le 23.
4. Ordre de course, consignes du lecteur et du juge : à écrire par le rédacteur les 24 et 25, sur demande de la mère.
5. Scellement par `finaliser-t08-scellement-v2.py`.

# Vérification des corrections — réponse du concepteur sur « Diffuse AI Control on Fuzzy Tasks », v2 (v1)

- **Date** : 21 novembre 2026, 16:30 UTC (`date -u`). **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), le contre-lecteur de la v1 (R-3735 : vérification des corrections par le même contre-lecteur). Pièce de classe C.
- **Contre-lecture vérifiée** : `contre-lecture-reponse-fable-controle-diffus-v1-opus-v1.md` (`72865f94d9c86b4f411d6682acdc32ed60a3d5678c520bf4d6aa393d02a53fdf`), 25 constats.
- **Pièces lues, empreintes égales aux compagnons** : `reponse-fable-controle-diffus-v2.md` (`dbe929e7fbc71966e3770c145ec4b0d10e72964b9b71354956b72ae16e7e5db8`), en entier sauf l'annexe ; `calculs-controle-diffus-v2.py` (`b813ef98…90ed`) et `.txt` (`a7abb7e4…c4c1`) ; `collisionneur-v2/faits-controle-diffus-v2.md` et `question-controle-diffus-v2.md` (la question est identique à l'octet à celle de la v1).
- **Calcul rejoué une fois** (`python3 -I`, dossier temporaire à moi) : sortie **identique à l'octet**. Différence avec la v1, lue : seuls les libellés de A1, A2 et A4, le bloc B4 (résidu imprimé de 3,4, cinq cas, de 33 à 133 lectures), la lecture du bloc C (0,62) et le bloc E (couverture jointe, tables à 97,5 %, différence t − f) changent ; les autres chiffres sont les mêmes.
- **Sources rouvertes pour les ajouts de la v2** : N-062 (`63f42690…3ccc`), points 1, 5 et 6 ; N-053 (`2204256d…deae`), point 5 ; N-076 (`49b664c1…dd78`), § 13 ; Taylor et al., p. 4 et 26 ; Hollinsworth et al., p. 7 ; Jang et al., p. 12 ; Goldowsky-Dill et al., p. 6 ; Parrack et al., p. 8 : **tous conformes à la page dite**.

## Verdict

**Conforme, avec quatre réserves mineures.** Les 25 constats sont portés : **23 portés juste, 2 portés avec un écart motivé et justifié, 0 portés mal, 0 manquants.** La section 15 lit maintenant Taylor et al. des deux côtés, et Hollinsworth et al. pour ce qu'il mesure. Le couple v2 est neutre.

## Constats de la contre-lecture

| N° | État | Où et comment |
|---|---|---|
| I-1 | porté juste | Phrase 1 (§ 15) réécrite : défaite de l'équipe, sondes plus efficaces que la boîte noire, comportements de diversion, calibration, entraînement, tâches à réponse claire. Les deux côtés sont donnés page par page sous la phrase. Premier tiret des phrases à ne pas tenir corrigé, avec un tiret neuf dans chaque sens. Tableau du § 7 réécrit « contre » et « pour ». Les ajouts (p. 4, 25 et 26 : tâches ouvertes, démonstrations de référence) sont vérifiés à la page. |
| I-2 | porté juste | Verdict, point 2 : « tous sur des tâches à réponse claire », « faibles ou fragiles », auteur partagé, « la question y reste ouverte dans les deux sens ». Aussi au § 7 (« Aucune ligne du tableau… »), au § 9 et à D-1. |
| I-3 | porté juste | « Dénégations, non actions » partout : § 7, § 9, verdict, § 15 (« et jamais « 63 % de détection du sous-rendement » »), calcul A1, faits v2. La question de suite préremplie (p. 10) est ajoutée. « Fine-tuned to pursue a hidden goal and to deny holding it » est vérifié (p. 7). |
| I-4 | écart motivé, **justifié** | La fin proposée de la phrase 3 est prise. L'auteur refuse d'écrire que l'issue du § 13 s'applique d'elle-même. N-062, point 6, dit bien : « La bascule du brief […] ne s'applique que si Lazar arrête les cycles ; elle reste écrite comme issue possible, à sa main ». Sa lecture est plus exacte que ma proposition. Les conditions de la phrase 3 (D-1, D-2, D-4, D-5, D-7) et la réponse à « et si c'est nul deux fois ? » sont justes. |
| I-5 | porté juste | D-7 neuf, nœud sans défaut. Le texte de N-053, point 5, est exact (« aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré »). La recommandation (b), M3 en bras d'attaque déclaré seulement et sans revendication défensive, tient l'invariant entier. La sorte 4 et l'emploi défensif sont séparés (§ 11). « Dans leur unité » ne se dit pas avant D-7. Juste. |
| I-6 | porté juste | « Personne ne l'a » a disparu. Le texte dit « non trouvé par huit requêtes, trois titres restent à lire » au verdict, au § 10, à D-1, à D-6 (a) et dans un tiret du § 15. |
| I-7 | écart motivé, **justifié** | N-076, § 13, point 4, pose déjà ce nœud (« Porter la règle d'horizon dans l'énoncé de H2 », recommandation (a) : ne pas toucher l'énoncé avant la prévision scellée). Ne pas poser un second nœud contraire est correct. La prémisse « retirer la revendication » est retirée : verdict, point 3 ; § 7, conclusion ; D-2. |
| I-8 | porté juste | Règle générale en en-tête, « sous supposition » au verdict, aux § 6, 7 et 9, et dans deux tirets du § 15. |
| m-1 à m-17 | portés juste | Vérifiés un à un dans la note et le calcul. Ont été vérifiés en particulier : version 2, annexe I.8 (m-1) ; 0,57 et 0,50 (m-2) ; B4 et les 33 à 133 lectures (m-3) ; √2 (m-4) ; « double les passes » (m-5) ; 0,62 (m-6) ; couverture jointe et 500 produits au lieu de 300 (m-7) ; « deux des quatre auteurs » (m-8) ; Jang et al., p. 3 et 12 (m-9) ; Taylor et al., p. 26 (m-10) ; Goldowsky-Dill et al. et Parrack et al. (m-11) ; licence, calendrier et Cedar dans les faits (m-15) ; une seule règle de cycles (m-16) ; objets différents (m-17). |

## Réserves mineures, nouvelles (correction par erratum, sans nouvelle contre-lecture)

| N° | Lieu | Constat | Correction proposée |
|---|---|---|---|
| r-1 | § 15, phrase 3, dans l'encadré | L'encadré garde « Je veux mesurer… », que la note ne permet qu'après D-1. La condition n'est écrite que dessous : lue seule, la phrase se dit trop tôt. | Dans l'encadré, mettre la forme d'avant décision : « La mesure qui départagerait est proposée, pas décidée : savoir si une lecture des états internes du modèle soupçonné aide là, contre leur attaque refaite, avec un critère de mort écrit d'avance. » Garder « Je veux mesurer » pour après D-1. |
| r-2 | § 10, titre de la colonne A | « Tenir, déplacer la revendication » est un reste de la prémisse retirée (I-7). | « A. Tenir l'objet et la loi de la référence honnête, répondre par la mesure ». |
| r-3 | § 4, point 1 | « La mesure se dit dans leur figure » ne vaut que si D-7 (a) est choisi ; la recommandation est (b). | « … dans leur figure, si D-7 le permet ; sinon, en lectures de vérité épargnées ». |
| r-4 | § 15, phrase 1 et premier tiret | « Plus efficaces que la lecture du texte » rend « black-box approaches », qui comprend aussi les consignes de révélation et les attaques par persona d'utilisateur (p. 3). « Celles de la note v2 restent » : la note d'entretien en vigueur est la v3. | « plus efficaces que les méthodes en boîte noire » ; « celles de la note d'entretien v3 restent ». |

## La section 15, jugée en priorité

- **Taylor et al.** : lu des deux côtés, à la lettre et aux pages, dans la phrase 1, sous la phrase et dans les tirets. La phrase 1 tient devant un juré qui a lu le jeu d'audit.
- **Hollinsworth et al.** : lu pour ce qu'il mesure. Le 98,8 % est donné avec son banc et sa question de suite préremplie ; le 63 % porte sur des dénégations et vient avec la lecture des auteurs. Le tiret d'interdiction est explicite.
- **Bascule et invariant** : rien n'est annoncé avant les décisions de Lazar. La réponse à « Entraîneriez-vous l'agent contre votre sonde ? » est conforme à N-053.
- Seule réserve : r-1.

## Couple neutre v2

Il est neutre. La recherche par motifs (nom de Lazar, du dépôt, chemins, identifiants de décisions et de GO, sigles d'hypothèses, noms des modèles et des sessions, « part sue », « juge sous attaque ») ne rend rien. Le calendrier est devenu « Bientôt ». La règle sur l'échec des sondes est donnée dans sa forme en vigueur (reconception, arrêt à la main du directeur), sans la proposition de l'auteur. Les côtés favorables (Cedar, Goldowsky-Dill et al., Parrack et al.) sont ajoutés. Aucune réponse n'est glissée dans les faits.

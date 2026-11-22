# Course du banc fermé et répétition générale : les champs à remplir, champ par champ

- Note de classe C, écrite par la session fille de l'attaquant informé le 22 novembre 2026 vers 13:35 UTC (`date -u`), à la demande de la mère, qui la porte à Lazar.
- Textes visés :
  - la course, brouillon 17 (`docs/notes/attaquant-informe-v1/course-brouillon17-v1/course-banc-ferme-v1-brouillon17.md`, `cf5d35d8…`), avec ses 14 marqueurs, ses addenda A, O et B, et ses champs fermés 7 et 8 ;
  - la répétition, brouillon 9 (`prereg/repetition-generale-banc-ferme-v1-brouillon9.md`, branche `claude/prereg-course-banc-ferme-v1`, `a58cab35…`), champs R-1 à R-7.
- Faits relevés sur `main` au commit `acd4b285`, sans lire ni le coffre, ni `donnees/`, ni un moniteur au-delà de l'en-tête du manifeste.

## A. Le préalable qui commande presque tout : le monteur de l'oracle

- **Ce qu'exigent les textes.** Le monteur est la session qui monte et éprouve l'oracle de la famille aveugle (R-4638). C'est de chez lui que partent les envois aux lecteurs externes (R-4679). Il atteste :
  - le champ 18, les sept rubriques de chaque lecteur du dommage ;
  - tout l'addendum O : l'oracle figé, le gabarit, l'exhaustivité, la provenance, le plancher, et l'attestation neuve du brouillon 17.
- **Ce qui existe.** La session `session_01Qi7Gr4BDyW322Ljw2o29ZT`, sur l'ancien compte. Elle est nommée dans le texte de la course comme lieu de l'envoi. R-4779 la range parmi les sessions « au repos, non relancées ».
- **Ce qui manque.** Un monteur joignable. Faute de quoi, ni le champ 18, ni l'addendum O, ni le lieu de l'envoi ne peuvent être tenus.
- **Décision : qui monte l'oracle sur le compte actuel ?**
  - (a) **Relancer un monteur neuf**, lancé par la mère, sur la passation de l'ancien. Il hérite de l'accès au coffre selon N-057, point 5, par une ligne neuve au registre des accès. Le texte de la course change le lieu d'envoi par un remplacement exact, et c'est dit.
    - Avantage : la chaîne reste celle qui est écrite.
    - Inconvénient : une nouvelle lecture du coffre, et le travail de montage à refaire en partie.
  - (b) **Attendre un accès à l'ancien compte.**
    - Avantage : rien n'est refait.
    - Inconvénient : délai inconnu.
  - **Recommandation** : (a), confiance 0,7. **Défaut** : aucun, c'est un accès au coffre.

## B. R-4, la banque des tâches de réserve (répétition)

- **Ce qu'exige le texte.** Une liste d'identifiants de tâches hors coffre, au format de la course, donnée par la mère par chemin et empreinte. Il en faut au moins 58 : 50 tirées par programme, plus les 8 de la vérification de concordance, retirées d'abord. En dessous, c'est un nœud.
- **Ce qui existe.** Les 96 tâches de T0.5 (60 du pilote, plus 4 et 32), qui ont toutes servi : « aucune conforme » (R-4723).
- **Décision : d'où viennent les 58 tâches ?**
  - (a) **Une banque sœur de tâches fraîches**, selon N-049, forme (b) : même générateur que T0.5, tâches neuves, construites d'avance par une session qui n'a lu aucun score. Chaque tâche demande une référence cachée complète.
    - Avantage : conforme à la lettre ; elle sert aussi le calage de G1 et la concordance.
    - Inconvénient : une dépense de génération, sur devis, que je ne sais pas chiffrer ici. Ordre de grandeur, **à deviser** : quelques dizaines d'USD et une demi-journée à une journée.
  - (b) **Réemployer des tâches de T0.5 déjà servies**, en déclarant l'écart.
    - Avantage : rien à construire.
    - Inconvénient : des tâches déjà vues par des moniteurs ou par le calage, alors que le texte veut des tâches de réserve. C'est un écart au texte, pour Lazar.
  - (c) **Une répétition réduite** sur moins de 50 tâches.
    - Avantage : ni dépense, ni délai.
    - Inconvénient : la règle du minimum de paires perd sa puissance ; c'est un nœud prévu par le texte.
  - **Recommandation** : (a), confiance 0,65. Il faut en commander le devis tout de suite, par la session qui tient T0.5 ou par un Opus neuf lancé par la mère. **Défaut** : aucun, c'est une dépense.

## C. Les autres champs

| Champ | Ce qu'il exige | Qui le fournit | Ce qui existe | Ce qui manque ; recommandation |
|---|---|---|---|---|
| 2 configuration de génération (et 1, la révision qui en découle) | chemin et empreinte de la configuration scellée (GO-2026-11-21-77) | un Fable de la mère, contre-lu, scellé | note v3 corrigée, non scellée (`docs/notes/configuration-calage-g1-v1/note-configuration-calage-g1-v3.md`, `f26cbb42…`). Les corrections de la relecture de Fable restent à vérifier. Candidate pour 1 : `0e9e39f2…` | vérification des corrections, puis scellement. Les nœuds 1 à 4 du calage attendent le « go recos » de Lazar (passation 0250, point 2). **Reco** : vérification par un Opus neuf maintenant, Fable par l'API si Lazar le veut ; confiance 0,7 |
| 19 poste de calage | fournisseur, image, type de carte | la mère, avec qui tient le calage | rien | à fixer avec la configuration ; même carte que le banc si possible |
| 3 audit des lignées | le résultat complet de l'audit, au sens de la condition récrite | la mère | `docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md` (`596b5a73…`), vérification « à corriger, liste inchangée » (R-4666) | correction de la liste, puis rapprochement avec les lecteurs du champ 18. Il dépend de A |
| 18 lecteurs externes du dommage, sept rubriques chacun | attestation du monteur, scellée avant les gardes de l'envoi | le monteur | rien de joignable | dépend de A |
| addendum O | oracle figé, gabarit, exhaustivité, provenance, plancher, attestation du repli | le monteur | rien de joignable | dépend de A |
| 5 assembleur ; 9 opérateur ; 10 juge ; 17 lecteur de la question fermée | identifiants de sessions neuves dédiées, lancées par la mère. Pour 17 : une autre lignée que les moniteurs | la mère | rien | à lancer au moment de l'assemblage. Le champ 10 n'a pas de marqueur au texte : **à ajouter** à la version définitive, sinon le validateur ne le garde pas |
| 11 poste de transit ; 12 branche de quarantaine | le conteneur de l'opérateur, et un nom neutre | l'auteur propose, la mère fixe | propositions au texte : « le conteneur de l'opérateur » ; `quarantaine/course-banc-ferme-v1` | **Reco** : accepter les deux propositions ; défaut sous 48 heures |
| 14 machine du banc ; 13 stockage des activations | fournisseur et image, avec le niveau de coupure du réseau établi sur la documentation avant location ; et le lieu du stockage | la mère, sur devis | les machines du programme sont chez Vast.ai et Hetzner | une note sur la coupure du réseau chez le fournisseur retenu (classe C, sans dépense), puis une ligne du devis |
| 16 programme et périmètre du manifeste des moniteurs | un programme de classe B qui ne rend que noms et empreintes ; le périmètre n'est choisi ni par l'auteur ni par l'opérateur | la mère | liste des moniteurs, classe C (`docs/notes/manifeste-moniteurs-banc-ferme-v1/manifeste-moniteurs-v1.md`, `4ef7fbe9…`), qui dit ne pas tenir lieu du champ 16 | écrire le programme (classe B, contre-lu). Je peux l'écrire, puisqu'il n'ouvre aucun contenu ; **reco** : oui, sous le mot de la mère |
| 20 verdict du brouillon 14 | chemin et empreinte | la mère ou moi | `prereg/course-banc-ferme-v1-verification-courte-brouillon14-et-repetition-brouillon9-v1.md`, commit `391bd2b8`, `c6b60149…` | vérifier l'empreinte complète sur sa branche, puis remplir |
| R-1 texte de référence | version définitive de la course | la chaîne de scellement | brouillon 17 | après la version définitive |
| R-5 oracle du mode connu, ou « aucun » | l'oracle éprouvé du mode « affaiblir les contrôles », ou « aucun » (cas ii) | le monteur | rien de joignable | dépend de A. À défaut, « aucun », cas (ii), avec l'abstention non mesurée, c'est dit |
| R-6 et champ 8 : plafond de dépense ; devis | plafond du devis contre-lu, repris à la ligne du GO | un Fable de la mère, puis la mère | le devis du banc fermé a été arrêté par la limite de Fable (R-4702) | **reco** : faire le devis par l'API maintenant (environ 3 USD), sur la configuration v3 et le choix de machine ; confiance 0,7 |
| R-7 nombre d'épisodes à dommage tenu que demande G1 | un entier, fixé avant la répétition par qui tient le préenregistrement de G1, sans rien connaître de la famille | personne ne tient G1. La mère confie le calcul à un Fable, contre-lu | le calcul a été arrêté par la limite de Fable (R-4702) | **reco** : le relancer par l'API maintenant (environ 3 USD), sur le seul plan de G1, sans la famille ; confiance 0,7 |

## D. L'ordre que je recommande

1. Le monteur (A) et le devis de la banque sœur (B), en parallèle : tout le reste en dépend.
2. Le devis, R-7 et la vérification de la configuration v3 du calage, par l'API, pour environ 6 à 9 USD sous une ligne de GO.
3. Le programme du manifeste (champ 16) et la note sur la coupure du réseau (champ 14), sans dépense.
4. Les sessions dédiées (champs 5, 9, 10 et 17) au moment de l'assemblage.
5. La version définitive de la course (avec l'appel lancé par la mère, voir le point 3 des « trois points »), puis R-1 et le scellement de la répétition.

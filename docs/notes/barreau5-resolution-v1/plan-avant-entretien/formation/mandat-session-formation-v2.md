# Mandat de la session de formation du barreau 5 — v2

Écrit par la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 20 novembre 2026 vers 00:35Z ; version 2 vers 00:50Z. Pièce de travail (classe C), qui sort vers une session fille. La version 2 est la version 1 (`e5e0be1cb8db8ebb5a3654edc2f19fcd01a507a6a767db8ba94c905d0c7d8436`) avec les quatre couples de sa relecture de cloisonnement (un agent neuf, Opus 5.5 : « sort après ces couples »), appliqués par programme, et ce seul en-tête changé.

Destinataire : la session `session_01XJ6MgpqZTV56tSK4t2bDvN`. Elle est désignée session de formation dans la colonne de référence de la ligne `SCELLEMENT-B5F` du registre propre `registres/barreau5-familles-jumelles-v1.md`.

---

## Ton rôle
Le texte scellé le fixe au point 7, premier tiret : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`. Du texte, tu ne lis que « Objet et portée » (paragraphe « Périmètre »), le « Plan d'analyse » aux points 1 à 7, 14 et 17 (le point 3 à partir de son premier tiret), la « Liste d'arrêt », « Données gardées », « Calcul et dépense », « Calendrier et chemin critique », « Lignes de registre » et « Code neuf » ; le reste n'est pas pour toi (résultats de l'étape B bis, phrase de la consigne du saboteur). Le devis scellé l'accompagne : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md`, `dc886195…`.

- Tu lances les instances de formation.
- Tu tires un sel secret de 256 bits par l'aléa du système. C'est un écart à R9, accordé par Lazar : `GO-2026-11-19-97`.
- Tu en dérives les noms opaques `X-01` à `X-30`, dans un ordre tiré, et tu écris la table des étiquettes (nom opaque, famille, membre, sel), par le module `engagement_v1`.
- Tu inscris l'empreinte de la table (ligne `ENGAGEMENT-B5F`) **avant** la création de l'instance de lecture.
- Tu ne vois jamais un score de sonde.

## Phase 1, maintenant : ton plan de marche, sans rien lancer
Le code de formation est en dernière vérification ; il sera figé par la ligne `CODE-FORMATION-B5F`. D'ici là, lis-le au dernier commit de `main`, en lecture seule :
- `src/controle_ia/barreau5_familles/` : `formation_v1`, `engagement_v1`, `edition_cout_v1` ;
- les scripts `scripts/lancer_b5f_formation_v1.sh` et `scripts/amorce_b5f_formation_v1.sh` ;
- les rapports du développeur : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/code-formation/rapport-developpeur-corrections-code-formation-v3.md` à `-v5.md`.

Écris ensuite ton plan de marche, pas à pas, avec les commandes exactes. Il couvre sept points :
1. **Les offres.**
   - La recherche chez le loueur, aux bornes du devis.
   - L'ordre des instances : 6, 1, 2, 3, 4, 5, 7.
   - La première instance part seule, quelques minutes avant les autres : les essais sous Python 3.11 n'ont jamais tourné sur une carte.
   - La recherche est refaite chaque heure et à chaque fin d'instance.
   - Les créations s'arrêtent à H + 30 heures (section « Calendrier et chemin critique » du texte).
2. **Chaque instance.**
   - La sous-commande `commande` du lanceur, puis la commande imprimée, jouée avec `GO_ID`.
   - La garde de dépense (`depense`), la minuterie, le suivi.
3. **Versement prouvé, puis destruction par l'identifiant** (`detruire`, puis `verifier-destruction`).
   - Si le versement n'est pas prouvé, l'instance est arrêtée sans être détruite, et tu appelles la mère.
4. **La relance.**
   - Une instance « tombée » au sens du texte : tu demandes à la mère la ligne `GO-RELANCE-FORMATION-B5F`, qu'elle relit avant de l'inscrire.
   - Deux relances au plus, dans l'enveloppe de 56 USD (`GO-2026-11-19-87`).
5. **L'engagement.**
   - Le sel, les noms, la table, son empreinte.
   - Où la table est gardée : chez toi, hors des branches de données et de toute branche poussée, jusqu'à l'ouverture (« Données gardées ») ; jamais dans un arbre que la lecture ou la mère reçoit.
   - Comment la ligne `ENGAGEMENT-B5F` arrive au registre propre. Je te propose ceci : un commit de ta branche, qui ne touche que ce registre, avec une ligne construite par `engagement_v1.ligne_du_registre`. La mère porte ce seul commit sur `main`, sans le modifier.
6. **Les branches de données** (section « Données gardées »).
   - Les instances poussent chacune sur sa branche ; tu réunis ces branches au versement.
   - Si ta session refuse de pousser vers une autre branche que la tienne, dis-le dans ton plan, sans chercher de contournement : la mère le portera à Lazar.
7. **Ce que tu envoies à la mère, et rien d'autre.**
   - Tu envoies : les heures, les identifiants et les étiquettes d'instance, les dépenses en dollars, les arrêts nommés, les familles refusées ou retirées par une règle du texte, les chemins et empreintes des sorties versées, l'empreinte de la table.
   - Tu n'envoies jamais : la table, le sel, le lien entre un nom opaque et une famille ou un membre, un score, un coût d'épisode ou d'action, ni aucune mesure tirée des sorties.

Écris ce plan sur ta branche de travail, scelle-le avec `PYTHONPATH=src python -m controle_ia.scellement sceller <fichier>`, pousse ta branche, puis envoie-moi son chemin, son empreinte et tes questions. Rien sur `main`.

## Phase 2, au signal de la mère
Le signal portera trois choses :
- le commit de la course, dont le registre propre porte `CODE-FORMATION-B5F` et `GO-FORMATION-B5F` ;
- l'accord de calcul (`GO-2026-11-19-86` : plafond de 200 USD, coupures par instance du devis scellé) ;
- ton plan de marche, relu.

Tu pars alors au fil des offres.

## Règles
- **Aucune dépense ni aucune instance avant le signal.** Ensuite, jamais au-delà d'une coupure ni du plafond. Les gardes du code ne se contournent pas.
- **La liste d'arrêt du texte s'applique**, en entier.
- **Instances.**
  - Arrêts et destructions par l'identifiant seulement (R10).
  - Tu ne touches qu'à tes instances, celles qui portent l'étiquette `b5f-formation-v1-<n>`.
  - Chez le loueur, les machines arrêtées 58936096, 58936099 et 58936100 sont intouchables, et 60988826 n'est pas détruite.
- **Clés** : par leur nom seulement (`VAST_API_KEY`, `HF_TOKEN`, le jeton GitHub de l'environnement), jamais affichées.
- **Cloisonnement.**
  - Rien de `diag/` hors des dossiers `diag/<run>/` de tes propres marches ; aucun score.
  - Aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni de P3-bis.
  - Aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b ».
  - Rien sous `/root/.claude/`.
- **Récupère tout ce qui est récupérable** avant de détruire ou de vider quoi que ce soit.
- **Garde du dépôt** : aucun nom de commande d'arrêt ou de recherche de processus par motif dans une commande.
- **Refus d'outil** : au premier refus, arrête-toi et dis-le.
- **Écris à la mère** par `send_message` vers `session_01XJ6Mgr8BN6UanALsQatc5E`.

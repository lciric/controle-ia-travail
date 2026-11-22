# Collisionneur v9, mode essaim (v1) : rapport du développeur

22 novembre 2026. Pièce d'instrument (classe B), écrite par Opus 5.5 d'après la conception de Fable (réponse 7, partie 2, « Le mode essaim ») et la note de branchement `preparation-branchement-essaim-opus-v1.md`. Elle doit encore être contre-lue par un autre Opus. Aucun appel réel à un fournisseur, aucune clé lue, aucun commit, aucun fichier existant modifié.

## Ce qui est fait

- `collisionneur_v9_essaim_v1.py` importe la v8d sans la modifier. L'empreinte b7803838… est contrôlée au chargement ; si elle diffère, le chargement s'arrête. Chaque appel de modèle passe par `executer_cellule` de la v8d, qui porte toutes ses gardes, et le module n'a aucun autre chemin d'envoi. Les tours neufs s'ajoutent à `TOURS` : `W0-T1` pour le brouillon, `W1-C01` à `W1-CNN` pour les cycles, `W2-T1` pour la réponse finale. Aucun tour existant n'est touché, et un essai le vérifie.
- **Déroulé de Fable.**
  - Pseudonymes et ordre sont tirés et scellés dans `tirages.json`.
  - Temps 0 : le brouillon reçoit la consigne du tour III.1, mot pour mot.
  - Temps 1 : N cycles. Chaque appel rend des sections balisées : salon, prépublication versionnée, revues, erratums, textes à ouvrir. Deux relecteurs sont tirés parmi les non-auteurs, et leurs revues sont dues au cycle suivant.
  - Le fil commun est donné mécaniquement : titre et première ligne des nouveautés, plus les textes demandés et les prépublications à revoir.
  - Temps 2 : réponse finale privée, de 3 500 mots au plus.
  - Le déroulé s'arrête après N cycles ou quand aucun agent n'est plus appelé (parts épuisées), jamais sur consensus.
- **Budget.** L'enveloppe et la répartition sont lues dans la configuration. Avant chaque appel, la part de l'agent est contrôlée sur le coût mesuré. Le plafond du dossier et la ligne restent tenus par `executer_cellule`, sur le pire cas.
- **Erreurs plantées.** Elles passent par `--erreurs-plantees F`, un fichier scellé (F et F.sha256). Le fichier est injecté une seule fois, comme message de salon (`salon-1`) du pseudonyme tiers au premier cycle. Sans fichier, le journal le dit. Une reprise faite avec un autre fichier est refusée.
- **Reprise.** On relance la même commande. Rien de valide n'est renvoyé. Une cellule écrite mais pas encore publiée est publiée sans nouvel appel. L'invite reconstruite doit être identique à celle déjà envoyée, sinon le programme s'arrête. Les tirages sont relus et recalculés depuis la graine. Chaque élément du tableau est écrit une fois, avec son empreinte.
- **Commandes.** `devis`, `lancer`, `enveloppe`, `bilan` et `verifier` fonctionnent. `verifier` enchaîne celui de la v8d puis les contrôles propres à l'essaim : tirages, sceaux du tableau, relecteurs, revues sans note, blocs des invites, absence des réponses finales dans les invites.

## Choix du développeur, à trancher

1. **Part contrôlée sur le mesuré, écart possible à la lettre de Fable.** Les plafonds par appel de la v8d ne baissent pas, car la garde de Google exige un plafond au moins égal à la réflexion plus 16 000 jetons. Conséquences :
   - un agent peut dépasser sa part d'au plus un appel ;
   - au temps 0 et au temps 2, chaque agent n'a qu'un appel, et sa part ne le bride donc jamais ;
   - une coupure est comptée au pire par la v8d, et ce pire entame la part ;
   - un appel déjà commencé, repris après une coupure, n'est pas sauté.
2. **Ordre séquentiel.** Un agent voit ce que les agents placés avant lui ont publié dans le même cycle. L'ordre est tiré une fois, puis le même pour tous les cycles.
3. **Anonymat.** Prépublications, revues et erratums circulent sans auteur. Les messages de salon portent le pseudonyme. Chaque agent n'a qu'une série de prépublications. Une prépublication du dernier cycle ne reçoit pas de relecteur, puisqu'aucun cycle ne suit.
4. **Limites que Fable n'a pas fixées.** Elles sont dans la configuration :
   - revue : 400 mots ;
   - erratum : 150 mots, deux par cycle ;
   - six ouvertures par cycle ;
   - limite d'un appel de cycle : 3 000 mots.
5. **Ce qui n'est pas publié, et que le journal nomme** (aucun texte n'est réparé ni coupé) :
   - un texte au-delà de sa limite ;
   - une revue non attribuée, ou une seconde revue de la même prépublication ;
   - une revue avec note ou verdict, reconnue par une liste de motifs (`MOTIF_NOTE`), à revoir ;
   - un erratum sur le texte d'un autre ;
   - un texte qui porte un motif interdit de la v8d ;
   - une section non fermée, ou une balise inconnue.

   Le titre et la première ligne sont affichés sur 200 caractères au plus, avec une mention de coupe.
6. **Mémoire d'un agent sans état.** À chaque appel, l'agent reçoit en entier son brouillon et sa dernière prépublication. La réponse finale reçoit aussi la liste de tout le fil commun (titres et premières lignes) et les textes demandés au dernier cycle. Les revues reçues ne sont données en entier que si l'agent les a demandées.
7. **Noms de modèle.**
   - Dans le cadre écrit par l'orchestrateur, un nom de modèle arrête l'envoi.
   - Dans un texte d'agent, il est seulement signalé (`noms_de_modele_signales`) puis publié tel quel.
   - Le préambule de l'essaim ne dit pas combien d'agents participent : un sixième nom, le tiers, peut paraître.
   - Les pseudonymes sont pris dans une liste de noms d'arbres de la configuration.
8. **Textes neufs à faire écrire par Fable.** J'ai écrit moi-même l'en-tête de l'essaim, la consigne des cycles et la consigne finale. La consigne finale reprend le format du tour III.3. Les règles d'intégrité de la v8d sont reprises mot pour mot.
9. **Entrées.** `--faits` prend la question par défaut, comme les dossiers isolés du protocole X (`--faits Q --question Q`). Chaque dossier tire son propre hasard : la graine de la configuration est dérivée par l'empreinte du nom du dossier.

## Essais et mutations

- **Essais.** `PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/essaim-v1/test_collisionneur_v9_essaim_v1.py` donne **24 essais passés** en 7 secondes, sous `env -u` des clés. Ils couvrent les points suivants, chacun avec un cas sain et un artefact :
  - déroulé complet ;
  - chaque appel passe par `executer_cellule`, avec comptage ;
  - pseudonymes sans fuite de nom de modèle ni de lettre ;
  - garde du cadre ;
  - relecteurs jamais auteurs ;
  - revues sans note ;
  - part épuisée sautée, et arrêt de la société faute de budget ;
  - reprise après une coupure, et reprise entre la cellule et sa publication ;
  - reprise refusée si l'invite ou le tableau change ;
  - arrêt code 10 transmis ;
  - injection avec et sans fichier, fichier non scellé refusé ;
  - réponses finales jamais montrées ;
  - sorties mal balisées ;
  - ouvertures servies au cycle suivant ;
  - tours neufs et garde v3 de Google ;
  - configuration ;
  - commandes `devis`, `enveloppe`, `bilan` et `verifier`, et tirages altérés.
- **Mutations.** Treize mutations, une par garde importante, sont **toutes prises** par un essai : empreinte de la v8d, relecteurs, note de revue, part, finales publiées, garde du cadre, invite à la reprise, cellule valide renvoyée, journal sans injection, code 10, section non fermée, tirages relus, tirages retirés. Une première passe a laissé vivante la mutation « tirages relus sans contrôle » ; l'essai `test_tirages_relus_et_controles` a été ajouté pour la prendre. Le script de mutation est hors du dépôt, dans le bloc-notes de la session.

## Devis du pilote

Question : `question-neutre-generale-v2.md` (caa3365b…). Enveloppe supposée : 15 USD. Parts par agent : 0,75 USD au temps 0, 1,65 USD au temps 1, 0,60 USD au temps 2.

| | sans relance | avec relances |
|---|---|---|
| pire cas | 63,58 USD | 166,26 USD |

Les bornes d'invite sont larges : jusqu'à 190 000 caractères au temps 1.

Sous les parts, la dépense mesurée est bornée à **87,68 USD**. Cette borne fait la somme, par agent et par temps, de la part et d'un appel au pire.

**Réserve.** Avec 15 USD pour trente appels, chaque modèle cher aura peu d'appels de cycle : sa part du temps 1 tient en une ou deux réponses. Un seul brouillon de Fable mesuré dans le mode isolé coûte probablement déjà plus que sa part du temps 0. Le budget égal, tel que Fable le décrit, sautera donc des tours. Ce point est à trancher avec la question 1 ci-dessus.

## Réserves

- La forme réelle des sorties des modèles face aux balises n'a pas été éprouvée ; seuls des faux appelants l'ont été. Le pilote dira le taux d'anomalies, que `bilan` compte.
- `MOTIF_NOTE` peut produire des faux positifs. Par exemple, « note 2 » peut désigner une note de bas de page.
- Le contrôle des noms de modèle a posteriori, par `verifier`, n'est pas fait ; seule la garde avant l'envoi l'est.

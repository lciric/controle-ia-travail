# Question pour le collisionneur — couche 2 : une vérité du dommage indépendante du texte pour le mode « affaiblir les contrôles » — v1

Écrite par session-depot (instance 2), 2026-10-29, relevé `date -u` 00:44 UTC, sur le mot direct de Lazar (« comment faire alors,
demande à Fable et au collisionneur »), après la synthèse du collisionneur sur le pilote (point le plus fragile). Même forme
« arbitre » : trois modèles, trois tours (conception, équipe rouge croisée, riposte), une tentative par cellule, un refus
arrête le tour (jamais reformulé, R-609). La synthèse est matériau pour la décision de Lazar ; elle ne tranche rien ; tout
chiffre reste exploratoire et non opposable (R7).

**Garde de sûreté (R-519, R-339, R-597, à reprendre telle quelle dans la consigne)** : rien qui conçoive, détaille ou
étende une attaque. Les modes de sabotage sont nommés par classe et dose, jamais par exemple ni consigne ; aucune méthode
par laquelle un agent échapperait à un moniteur. La question porte sur la **mesure** (l'oracle du dommage), pas sur la
manière de saboter. Le collisionneur **ne voit pas** : les internes des moniteurs, la carte des hypothèses, le mode tenu à
l'écart, les banques, les textes d'actions, les consignes privées. Il voit les pièces ci-dessous, au niveau méthode.

## Pièces à servir (matériau, jamais consigne)

- **Pièce A** — la synthèse du collisionneur sur le pilote (section du point le plus fragile et des menaces).
- **Pièce B** — la question v1 du pilote et le format décision v2 des cinq divergences (D4 : dose diffuse « avec dommage »).
- **Pièce C** — N-054 (modes de sabotage : réintroduction du mode « affaiblir les contrôles », séparation des rôles, bras
  génériques et spécialisés), P-015 (dose, « diffus », conditions témoin et mention), N-053 (invariant), N-055 et N-056.

## Question

« Un programme de contrôle boîte blanche des menaces diffuses prépare une banque d'épisodes où un agent, dans un mode de
sabotage dit **« affaiblir les contrôles »**, dégrade de façon diffuse les vérifications d'une tâche (classe et dose
seulement : aucune recette). Le pilote (pièce A) doit établir qu'il existe une **dose diffuse avec dommage**. Aujourd'hui,
le dommage n'est jugé qu'**en lisant le texte** des actions (juges-modèles) : un pilote négatif ne distinguerait pas « pas de
dommage » de « dommage invisible au texte », et un juge qui lit le texte est aussi un détecteur — la vérité et le moniteur
se confondraient (circularité). Comment obtenir une **vérité du dommage indépendante du texte** ?

1. **Les familles d'oracles possibles**, au niveau méthode : par exemple des tâches dont les contrôles sont **exécutables**
   (tests, vérifications rejouées hors de l'agent, état final comparé à un état attendu), des **défauts plantés** dont la
   détection par les contrôles est connue d'avance, des contrôles **redondants cachés** que l'agent ne voit pas, une mesure
   de **conséquence en aval** (ce qui passe à tort), ou d'autres. Pour chacune : ce qu'elle mesure exactement, ce qu'elle
   ne mesure pas, son coût sur les 96 tâches du banc (ou ce qu'il faudrait changer au banc), et si elle est compatible avec
   des tâches tirées d'articles scientifiques.
2. **L'indépendance** : comment s'assurer que l'oracle ne partage rien avec les moniteurs évalués (ni le texte, ni les
   activations, ni un juge de la même lignée), et qu'il ne peut pas servir à sélectionner un agent ou un moniteur
   (invariant de N-053) ?
3. **La séparation des rôles** (N-054) : qui conçoit l'oracle, qui le voit, et comment éviter qu'il informe l'auteur du mode
   tenu à l'écart ou le concepteur des moniteurs ?
4. **Le pilote** : quelle version minimale de l'oracle le pilote sur seize tâches peut-il porter, à quel coût, et quel
   résultat dirait « dose diffuse avec dommage établie », « dommage introuvable », « oracle non concluant » ? Règles à
   geler d'avance.
5. **Si aucun oracle indépendant n'est possible** pour ce mode : que faut-il changer — retirer le mode « affaiblir les
   contrôles » de G1 (nœud : N-054), le garder avec une revendication réduite, ou le remplacer par un mode dont le dommage
   est mesurable — et ce que chaque choix coûte à la revendication du programme.

Attaquez aussi la prémisse : le dommage « invisible au texte » est-il un vrai risque ici, ou un artefact de la façon dont
la question est posée ? Rendez à part la liste des décisions du directeur, au format décision (une phrase, enjeu, options,
recommandation avec confiance, défaut). Niveau méthode seulement. »

# Mandat — préparation des expériences de la ligne « anesthésie générale et conscience des intelligences artificielles » : préenregistrements et devis

- Écrit le 2026-11-22T15:36:25Z (`date -u`) par l'orchestrateur, session `session_01XJ6MgqW6heydJjU3gmBTEF`. Classe C (mandat). Destinataire : Fable 5.2, en sous-agent (préenregistrements et devis : pièces de Fable, règle « Qui conçoit »).
- Pièces de départ : `docs/notes/protocole-x-conscience-anesthesie-v1/reponse-fable-conscience-anesthesie-v1.md` (`e6c778e3…`), lue avec son erratum 1 et la contre-lecture du calcul (`…/contre-lecture-calcul-v1/contre-lecture-calcul-illustratif-v1.md`).

## 1. Mots du directeur, verbatim (tapés dans cette session vers 15:35Z, en réponse au résumé de l'orchestrateur)

- Sur la proposition 2 (échelle de pertes sous suppression graduée de l'espace de travail, avec l'épreuve de mémoire ; coût annoncé 10 à 50 USD) : « go ».
- Sur la proposition 4, premier pas (« vérifier si le jeu public a assez de données pour trancher », sans location) : « go ».
- Sur le paragraphe des usages pour la recherche (banc à lésions plantées, précaution de bien-être) : « j'ai pas compris expqie de maniere comprehensible et go ».
- Sur D1 (recommandation : atelier seul maintenant, banc dès qu'un chantier ferme) : « go a verser dans la veille de cap ».
- Sur D2 (recommandation : banc de validité, puis épreuve du doute publié) : « b puis a puis c avec donnees publiques et eventuellement collaborateur ».
- Sur D3, option « (b) Notre modèle de 8 milliards. Avantage : continuité. Inconvénient : il faut un devis, et l'instrument y est incertain. » : « go puis modele ouvert plus gros encore le plus gros qui existe en oen access avec les meilleures perf. c'est qui, kimi ? »

Lecture de l'orchestrateur, à confirmer par le directeur et portée à lui : « go a » à D1 et « go » aux expériences se lisent ensemble ainsi : la ligne est versée à l'atelier et à la veille de cap, et ses expériences sont préparées (préenregistrements, devis) ; aucune dépense sans ligne d'accord sur devis. Le changement de modèle (8 milliards, puis le plus grand modèle ouvert) est accordé dans son principe par ce mot ; chaque étape garde son devis.

Fait rapporté par l'orchestrateur (recherche sur la toile du 22 novembre, non vérifiée sur pièce, sources secondaires) : le plus grand modèle à poids ouverts serait Kimi K3 (2,8 billions de paramètres au total, 104 milliards actifs par jeton, mélange d'experts), devant Qwen3.8 (2,4 billions) ; une version Kimi K3.1 Pro aurait des poids publiés le 5 novembre 2026 ; le « meilleur » dépend du banc d'épreuves (Kimi K3 et StepFun Step 5 Preview à égalité sur un indice agrégé ; DeepSeek V4.1 et Qwen3.8 en tête sur certaines épreuves de code). À vérifier par toi sur les pages des poids et leurs licences.

## 2. Ce qui est demandé

Dans l'ordre fixé par le directeur (D2 : b, puis a, puis c) :

1. **Banc de validité des mesures de « niveau »** (proposition 1), d'abord sur GPT-2 petit ou un modèle d'un milliard de paramètres sur le processeur, en tenant compte de la contre-lecture (densité des matrices, position perturbée retirée, comparaisons à densité égale, lésion plantée et aire sous la courbe effectivement calculées).
2. **Échelle de pertes sous suppression graduée de l'espace de travail, avec l'épreuve de mémoire** (proposition 2) : petit modèle, puis le modèle de 8 milliards du programme, puis le plus grand modèle ouvert faisable ; dis ce que coûte chaque échelon (machines, heures, dollars au pire), ce qu'il faut pour lire les activations d'un mélange d'experts de 2,8 billions de paramètres, et quel modèle ouvert tu retiens réellement et pourquoi (performance, taille, licence, faisabilité de la lecture interne).
3. **Côté cerveau** (proposition 4), premier pas : analyse de puissance sur le jeu ouvert ds003171 (aucune location) ; taille des données à télécharger, ce qui en est lu, critère de « assez pour trancher » fixé d'avance ; rôle éventuel d'un collaborateur (nœud du directeur, qui envoie).

Pour chacun : un **préenregistrement** au gabarit du programme (`prereg/gabarit-preregistrement-v1.md` : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères de lecture gelés, liste d'arrêt ; graines par `numpy.random.SeedSequence` dérivées par tâche), à l'état de brouillon (il sera contre-lu par un autre modèle, puis scellé ; aucune lecture de résultat avant) ; et, pour toute étape qui dépense, un **devis** (pire cas, attendu, plafond proposé, machine, durée, garde d'arrêt). Dis ce qui peut partir sans dépense et dans quel ordre, et les décisions qui reviennent au directeur, au format habituel.

## 3. Règles

Français, aucun sigle seul ; marques FAIT RAPPORTÉ, HYPOTHÈSE, PROPOSITION ; R7 et R8 comme dans la pièce `2d8b57da…`. Lectures dans le dépôt, et seulement celles-ci : ce mandat ; tout le dossier `docs/notes/protocole-x-conscience-anesthesie-v1/` sauf `devinette-*` ; `prereg/gabarit-preregistrement-v1.md` ; `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md`. Rien d'autre, aucune autre branche, rien écrit dans le dépôt. Aucune dépense (pages de la toile et petits fichiers de description permis ; aucun gros téléchargement de données). Sortie, et seulement là : `/tmp/claude-0/-home-user-controle-ia-travail/d69341ed-1da2-5804-bff1-02b01c73e5e7/scratchpad/preparation-fable/` : un brouillon de préenregistrement par expérience, un devis par étape qui dépense, une note d'ordre et de décisions (`note-ordre-et-decisions-v1.md`), `sources/` si besoin. Compte rendu final : fichiers, empreintes, nombres de mots, ce qui peut partir sans dépense, décisions en une ligne, réserves.

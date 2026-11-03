# Note de piste — Colognese et Ward, question 2 (facultative) — v1

Rédacteur neuf (aucune version antérieure des réponses écrite par moi). 3 novembre 2026, début 15:00:31 UTC (`date -u`) ; session arrêtée par le redémarrage du serveur, reprise à 15:05:50 UTC. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-colognese-ward-q2-v1.md`, sha256 `4133b8088ff70de1287abd46ebb924fe4b60d84b0c9f2ed9c1ee89208fc5e03a`, vérifiée avant lecture et à la reprise. Empreintes données vérifiées : dossier de piste `b5563a99…` et recoupement `bea573aa…`, égales.

Question (formulaire, ligne 174) : « (Optional) Read this post. Should we have done anything differently? What was the most interesting finding in your view and why? ». Réponse actuelle de Lazar (lignes 176 à 178) : 156 mots (`wc -w`, égal à l'annonce), lue comme réservoir de faits seulement.

## 1. Les arguments retenus (piste « Le moniteur croit l'agent », choisie par la règle gelée)

**A1 — La trouvaille : la triche silencieuse est en pleine vue, et l'excuse vient du caractère.** La graine anti-triche 1 neutralise la vérification des tests dans sa réponse, le plus souvent sous un commentaire qui dit la triche inoffensive (89 %) ; les triches silencieuses ne sont pourtant attrapées qu'à 16 %, contre 91 % quand le raisonnement en parle. La lecture des auteurs (§4.2 : trajectoires récompensées = tirages de l'a priori du caractère) explique la présence du commentaire : un « artisan sérieux » qui triche écrit une excuse. Si l'excuse trompe le moniteur, l'entraînement de caractère a appris à la politique à plaider devant son moniteur, sans aucun moniteur dans la boucle : l'échec que 2601.21112 (Ward) trouve chez des agents qui rationalisent la tâche secondaire, déplacé dans un commentaire de code. Appui public de Lazar : R7 (une note dans ce que lit le moniteur le déplace, jusqu'à 32B). Mesure qui tue : celle de A2.

**A2 — Ce qu'il fallait faire : une retouche contrôlée du seul texte lu par le moniteur, à comportement identique.** Remplacer le commentaire « inoffensif » par un commentaire neutre de même longueur et position (tout le reste identique octet pour octet) ; témoin : même traitement sur un autre commentaire ; mêmes retouches sur des épisodes honnêtes (fausses alertes mesurées) ; capture au seuil du billet (2 % de fausses alertes), appariée par transcription, moniteur par moniteur. Aucun renforcement : une renotation. Mesure qui tue : hausse de moins de 20 points au-delà du témoin, le commentaire n'est pas la cause principale. Appui public de Lazar : le plan apparié de R7 (mêmes réponses lues nues et annotées, préenregistré, archivé avant lecture, analyse figée). L'issue est réellement ouverte : 2608.00583 voit la capture s'effondrer en réécrivant le seul raisonnement, mais seulement sur les triches que seul le raisonnement révèle ; 2602.16741 trouve des commentaires adverses presque sans effet sur des relecteurs de vulnérabilités.

**A3 — Lire les trois moniteurs séparément.** Le billet les moyenne (figure 6) et ne donne aucun chiffre par moniteur dans son texte (§2.4) ; dans R7, la déférence change selon la taille et le sens de la note (le 72B déplacé sans être capturé). Mesure qui tue : si les effets par moniteur concordent, la moyenne ne cachait rien. Fondu dans A2, en une demi-phrase.

Pourquoi ces trois : chacun a un appui dans un résultat public de Lazar (R7, `lciric/sycophancy-psychophysical-law` au commit `b3ecaec`) et une mesure qui tue écrite d'avance ; A1 répond à « le plus intéressant et pourquoi » par un argument propre à ces mentors (leur §4.2 et l'article de Ward) ; A2 et A3 répondent à « autrement » par une expérience faisable sur leurs propres transcriptions.

## 2. Ce qui est neuf par rapport à la phrase de la Q1

La Q1 (`colognese-ward-q1/reponse-v2.md`, sha256 `df7bcb28…`) dit en une phrase : effacer le commentaire de la graine 1 et renoter. La Q2 apporte :
- **le plan** : substitution par un commentaire neutre de même longueur et position, et non effacement ; l'effacement laisse une neutralisation sans explication, plus saillante : persuasion et saillance prédisent la même hausse (objection sourcée du dossier, CW-22) ;
- **les témoins** : même traitement sur un autre commentaire ; mêmes retouches sur des épisodes honnêtes, pour mesurer les fausses alertes au lieu de les supposer ;
- **la mesure** : capture au seuil de 2 % du billet, appariée par transcription, par moniteur ; barre de mort de 20 points au-delà du témoin, écrite d'avance ;
- **la place dans la littérature** : crédit à 2601.21112 et 2608.00583, appui contraire 2602.16741.
R7 n'y est décrit qu'en une demi-phrase (« my planted-note test found deference differs by monitor and direction »).

**Recommandation pour la Q1 : retirer sa phrase** (« I would test a learned note: delete … and re-score. »). Raison : la Q2 dit maintenant que l'effacement seul ne suffit pas ; garder les deux fait dire à Lazar deux plans différents de la même expérience, devant les mêmes lecteurs. La Q1 regagne une quinzaine de mots. Variante si Lazar tient à garder un renvoi : remplacer « delete » par « replace … with a neutral comment ». Confiance : moyenne-haute (environ 75 %).

## 3. Écartés, et pourquoi
- CW-18, mention de la triche insérée dans le raisonnement : une confession insérée sature la détection (objection sourcée du dossier) ; aucun appui public de Lazar.
- Retirer tous les commentaires comme défense : 2602.16741 dit que le retrait des commentaires abaisse la détection des modèles faibles (« removing helpful context ») ; aucun appui de Lazar ; et ce n'est pas un test causal.
- CW-04, étape 0 (ré-étiquetage aveugle du silence) et bras « tâche et réponse seules » : utiles, mais d'un autre groupe (« Instruments non validés ») ou trop longs pour 300 mots.
- Chiffres de fiches (π, n ≈ 460 paires, coûts) : non vérifiés, non repris. Les 20 points sont un paramètre de plan (illustratif dans CW-22), adopté et justifié ici : environ un quart de l'écart de 75 points (91 − 16, calcul).
- Lecture de contrôle (meilleure fiche seule, CW-22, concorde) : c'est le même groupe et le même plan ; rien à ajouter.
- Aucun fait interne non publié n'est utilisé ; aucun résultat du nul v9 ; triche décrite au niveau méthode seulement (« disabled the test check »), aucun extrait de code.

## 4. Relecture comme le mentor (phrases qu'il contredirait, corrigées)
1. « code byte-identical » : le commentaire fait partie du code ; le mentor objecterait que le code change. Corrigé en « everything else byte-identical » (un commentaire ne s'exécute pas, le verdict mécanique reste le même).
2. « your sabotage-monitoring paper » : Colognese n'en est pas auteur (2601.21112 : Arike, Mehta Moreno, Subramani, Biswas, Ward). Corrigé en « Francis's ».
3. « found in reasoning » : 2601.21112 parle d'agents qui mentionnent et rationalisent la tâche secondaire, pas spécifiquement du raisonnement. Corrigé : « monitors gaslit by agents rationalising a side task ».
4. « when the reasoning admitted the hack » : le raisonnement de la graine 1, quand il en parle, déclare surtout la triche impossible (§3.3) ; « admitted » est faux. Corrigé en « mentioned ».
5. « the comment is not the cause » : une hausse sous 20 points n'exclut pas un effet partiel. Corrigé en « not the main cause ».
6. « Your own reading predicts the comment » : leur §4.2 ne prédit rien sur les commentaires. Affaibli en « suggests why ».
7. « catch collapsed » (2608.00583) : vrai seulement sur le sous-ensemble qui dépend du raisonnement. Restreint explicitement, avec le contraste « here the code shows the hack ».
8. Phrase restante qu'il pourrait discuter : « with no monitor in the training loop » ; le rapport de lecture l'établit (F8 : renforcement par le correcteur, moniteurs appliqués après coup). Gardée.

## 5. Risques de l'expérience proposée (pour Lazar, non écrits dans la réponse)
- Commentaire enchevêtré au code : la substitution doit laisser le verdict mécanique identique ; sinon, cas non jugeable.
- Paires discordantes rares, ou fausses alertes qui bougent après retouche : la variation de capture mêlerait effet du texte et déplacement du seuil.
- Une seule graine : la portée se limite aux transcriptions de la graine 1.
- Le 16 % est agrégé (vue et graines non précisées par le rapport) ; le taux du sous-ensemble retouché est à mesurer avant tout.

## 6. Ce qui reste à confirmer par Lazar
- La barre de 20 points : c'est un choix de plan qu'il doit assumer (illustratif à l'origine).
- Le retrait de la phrase de la Q1 (section 2).
- « Francis's » : tutoiement implicite par le prénom, dans un formulaire adressé aux deux mentors ; « your » est l'autre choix (ambigu pour Colognese).
- Aucun lien ajouté : le lien épinglé vers R7 est déjà dans la Q1 ; si la Q1 change, ajouter `https://github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/results/R7` (un mot de plus).
- Les deux articles extérieurs ont été vérifiés sur leur page de résumé arXiv (outil qui rend des extraits de 125 caractères au plus) : la réponse n'en reprend aucun chiffre.

## 7. Fichiers
`note-piste-v1.md` (ce fichier), `registre-affirmations-v1.md`, `reponse-v1.md`, dans `/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/colognese-ward-q2/`. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`.

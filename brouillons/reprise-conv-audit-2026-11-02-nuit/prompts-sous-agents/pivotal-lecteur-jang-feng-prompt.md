Tu es un lecteur neuf pour la candidature de Lazar Ciric à la bourse Pivotal (mentors du premier trimestre 2027). Tu n'as écrit aucune des réponses. Travaille en français pour ton rapport, en anglais pour les textes de réponse. Toute heure vient de `date -u`.

## Mentor : Shi Feng et Eyon Jang (valeur et limites des moniteurs et méthodes boîte blanche pour l'audit)
## Réponse(s) actuelle(s) de Lazar (texte du formulaire, corrigé le 3 novembre 2026) : section « Jang et Feng (dans le formulaire brut ; la réponse n'a pas été changée) » de
`/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/reponses-completes-corrigees-formulaire-2026-11-03-v1.md`
(et, pour les réponses non citées là, le formulaire brut `formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt` dans le même dossier).
## Question(s) posée(s) par le mentor : dans ce même formulaire brut, section du mentor.

## Travaux à lire (textes entiers, pas résumés ; par `WebFetch` sur `https://arxiv.org/html/<id>` ou `https://arxiv.org/pdf/<id>`, en lisant par tranches avec `offset` jusqu'au bout ; le terminal ne peut pas atteindre arXiv)
- Leurs travaux : arXiv 2604.28182 (« Exploration Hacking: Can LLMs Learn to Resist RL Training? ») ; cherche par WebSearch les autres papiers récents de Shi Feng et d'Eyon Jang sur l'audit et les moniteurs, et lis les deux plus proches de la question.
- Les sources que cite la réponse : arXiv 2512.07810, 2609.36490, 2602.08877.
- arXiv 2510.09462 (attaques adaptatives contre les moniteurs de confiance), 2505.14300 (« Beyond Black-Box Obfuscation », moniteurs boîte blanche), 2401.14446 (« Black-Box Access is Insufficient for Rigorous AI Audits »).

## Ce qu'on te demande
1. **Tableau de lecture** : pour chaque affirmation de la réponse de Lazar qui porte sur un travail du mentor ou sur la littérature, une ligne : affirmation (mots exacts) | ce que dit la source (identifiant arXiv, section ou page, chiffre exact) | verdict (exact / inexact / déjà fait par eux / plus précis chez eux). Puis les faits des sources que la réponse ignore et qui changent l'argument (une ligne chacun, avec l'identifiant et la section).
2. **Arguments plus profonds** : pour chaque paragraphe de la réponse, dis si l'argument est générique (un relecteur qui connaît ses papiers le trouverait banal) et propose l'argument précis qui s'appuie sur une faille, une limite déclarée ou un résultat exact du travail du mentor, en une à trois phrases, avec la source. Ne propose rien que tu ne puisses rattacher à une source lue.
3. **Réécriture du fond, à longueur égale ou plus courte** : réponse(s) réécrite(s) en gardant les formulations de Lazar partout où le fond tient (ses phrases, son registre), en changeant seulement ce qui doit l'être ; chaque changement listé ensuite en une ligne (avant → après, raison, source). Règles de fond : aucun chiffre sans source ouverte ; aucun résultat de Lazar présenté comme fait s'il n'est pas dans un dépôt public scellé (sycophancie : `github.com/lciric/sycophancy-psychophysical-law` ; organisme : `github.com/lciric/ideation-organism`, README et pages `resultats/`, lisibles par `WebFetch`) ; les chiffres ρ = 0,68, < 1 %, 68 % viennent de son programme d'interprétabilité, non publié : les garder comme il les écrit, et le dire dans ta liste ; tests de mort « jamais exécutés pour de vrai » ; validation du nul v8 datée du 1er novembre ; copie exacte retenue au banc v7, mélanges passés ; juge de la sycophancie `claude-opus-4-6`, pas de la famille de Llama.


## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; aucun appel de modèle autre que toi ; `WebFetch` et `WebSearch` seulement pour les sources ; rien sous `donnees/` ; `nice -n 10` pour tout calcul. Tes fichiers sous `/home/claude/scratch/pivotal-approfondi/jang-feng/`.

## Rendu
Un fichier `/home/claude/scratch/pivotal-approfondi/jang-feng/rapport-jang-feng-v1.md` avec les trois parties, et ta réponse finale : les trois ou quatre faits les plus importants que la réponse ignorait, la liste des changements en une ligne chacun, le chemin et le sha256 du rapport.

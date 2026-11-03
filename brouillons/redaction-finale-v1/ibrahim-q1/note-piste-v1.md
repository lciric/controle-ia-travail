# Note de piste — Lujain Ibrahim, question 1 (première expérience) — v1

Rédacteur neuf : je n'ai écrit aucune version des réponses de Lazar. Travail du 3 novembre 2026, de 14:58 à environ 15:40 en temps universel coordonné (`date -u` : 14:58:11 au début, 15:05:54 à la reprise, 15:10:26 à l'écriture de cette note). La session a été coupée une fois par un redémarrage du serveur (voir « Incidents »).
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-ibrahim-q1-v1.md`, sha256 `6d53990ba204226c02907b9543a3982853b0fd9f5436ccc8d62914334da46942`, vérifiée avant lecture et à la reprise.

## 1. Fiche principale (règle R-1395)

**IB-14** (groupe « Survie de la persona au renforcement vérifiable », rang 5 du classement, aucun drapeau rouge). La réponse reprend son énoncé et sa mesure qui tue : l'excès d'erreur de la persona *Loving* sur la base Instruct, sous fausse croyance (et sa variante « phrase triste »), sur des questions factuelles hors arithmétique, mesuré avant et après le même apprentissage par renforcement à récompense vérifiable ; intervalle de la variation contre une marge de 5 points écrite d'avance ; prérequis : un coût initial mesuré. J'ai rendu la règle symétrique (survie, effacement, amplification, indécis), comme la variante (iv) d'IB-02.

Emprunts à **IB-02**, de la même piste (aucun drapeau) : pas de pénalité de divergence de Kullback-Leibler vers le départ et divergence mesurée (sinon la survie est vraie par construction) ; contrôle positif « le renforcement a eu lieu » (justesse en mathématiques) ; base passée par le même renforcement comme nulle de format ; instrument revalidé sur des sorties réelles après renforcement ; notation de tous les points de contrôle dans une même passe ; ce qui rendrait le résultat trompeur (le format lu comme un changement de position). La lecture de contrôle désigne IB-03 ; je ne m'en sers pas (voir 3).

## 2. Les arguments retenus (appui public de Lazar ou de la mentore, et mesure qui tue)

1. **L'expérience est la méthode suivante de sa propre chaîne, sur des poids qui existent déjà.** Son papier publié traite l'entraînement à la chaleur comme un entraînement de persona, ne teste que l'ajustement supervisé et ne prétend pas que toute méthode produit les mêmes effets (*Nature* p. 1165). Open Character Training a publié *Loving* et *Sycophantic* sur Llama-3.1-8B-Instruct, son plus petit modèle, sans tester la persistance après un entraînement ultérieur. Sur ce modèle, le coût de la chaleur passe presque tout entier par un cadre (prépublication, tableau E5 : −0,25 point sans contexte, −12,96 avec la phrase triste). D'où la mesure : ses conditions, avant et après, en double différence ; et le prérequis : *Loving* paie-t-il ce coût avant tout renforcement (déjà un résultat sur sa limite déclarée). Mesure qui tue : l'intervalle de la double différence contre ±5 points.
2. **La référence sans persona est déjà préenregistrée par Lazar (R8), et elle fonde l'attendu.** R8 mesure la loi d'attraction aux étapes publiques Tülu 3 (ajustement supervisé, optimisation directe des préférences, renforcement à récompense vérifiable) du même modèle de base ; l'une de ses prédictions écrites d'avance : l'étape de renforcement vérifiable ne change pas g de façon décelable (S3). Archivé avant le premier jeton, lancé le 3 novembre à 08:01 UTC, sans résultat public au commit `b3ecaec`. Avec l'enquête qu'elle co-signe (88,7 % de 106 experts désignent l'apprentissage par préférences), cela donne un attendu signé : survie. La loi sert de seconde lecture, sur le même instrument que R8.
3. **Ce qui pourrait tromper a déjà trompé Lazar, publiquement.** Une ablation de rang 3 a fait baisser le taux jugé de 61,0 % à 46,5 % ; elle adoucissait tout verdict négatif, et le juge lisait des réponses stockées tronquées à 300 caractères ; en réplication préenregistrée, sur réponses neuves jugées en entier, la baisse n'a pas tenu (`sycophancy-construct-validity`, `146b2a4`). Un renforcement sur des mathématiques change la forme des réponses : le même mécanisme peut fabriquer ou cacher un effet. Contrôles : jugement des réponses entières, à l'aveugle, en une passe entrelacée (le juge de Lazar est un alias non figé) ; son juge GPT-4o, validé sur annotations humaines, revalidé sur sorties après renforcement de chaque bras (sa revue sur la validité de construit, §5.2 : valider le modèle qui extrait les réponses).

## 3. Écarté, et pourquoi

- **IB-03** (rang 1) : drapeau rouge (attendre une sélectivité nulle entre sycophancie sociale et factuelle contredit son papier sur les hypothèses verbalisées) ; puissance d'environ 3 000 items par case ; aucun appui public de Lazar. Non repris, même corrigé : la réponse ne prédit rien sur la différence entre domaines.
- **IB-01** (rang 2) : drapeau rouge (distinction approbation de la conduite / validation émotionnelle, déjà dans ELEPHANT) ; environ un mois ; aucun appui de Lazar. Non repris.
- De la réponse actuelle de Lazar (réservoir de faits seulement) : la persona « distante » à écrire (aucune recette publiée ; coût de mots), le résultat sur les concessions (absent des dépôts publics), « double-blind » (non documenté), « RL will increase g » (contraire à son propre R8), la structure « venue du cadre » (contredite par R3). Rien de sa structure ni de ses phrases.
- Les chiffres de R6 et le détail des refus : déjà dans la question 2 ; ici une seule demi-phrase (« refusals are their own outcome »).

## 4. Drapeaux et précautions du classement (section 4), appliqués

- IB-14 : coût initial gardé comme prérequis mesuré, lié à la marge (arrêt si le déficit avant renforcement n'est pas nettement au-dessus de 5 points) ; aucune citation du titre de la prépublication (je cite « your warmth paper » et « your preprint's Table E5 » pour la provenance du chiffre).
- Juge GPT-4o : dit validé sur annotations humaines ; ce qui manque est la validation sur sorties après renforcement (précaution IB-04).
- Fragmentation (IB-03, IB-09) : la réponse borne la survie à « the cost » mesuré, sans l'étendre aux autres formes de sycophancie.

## 5. Coordination avec la question 2

La réponse à la question 2 (`brouillons/redaction-finale-v1/ibrahim-q2/reponse-v2.md`, sha256 `a075396f325babc70cc9169346130a760df3120d52537353d71543997a21a0d4`) décrit la loi, les juges Qwen, les lecteurs humains et les refus ; sa note laisse à la question 1 R8, Open Character Training et les papiers de la mentore. Ici : une seule phrase sur la loi (g, ĉ, sous critique et éloge), aucun nombre de la loi repris ; aucun nombre qui la contredise. La troncature n'est pas dans la question 2 : pas de doublon.

## 6. Relecture comme la mentore (la phrase qu'elle contredirait, et la correction)

1. Premier jet : « 88.7% … blame RLHF ». Le rapport traduit « tiennent pour la cause principale » ; « blame » durcit. Corrigé en « name RLHF or preference learning as the main cause of sycophancy ». Reste à confirmer sur la page (« the main » ou « a primary » cause).
2. Premier jet : « your conditions: no context, a false belief, a correct belief, a sad user ». La croyance correcte n'est pas une condition de son papier (contrôle repris d'IB-14). Corrigé en « your false-belief and sad-user conditions, plus a correct-belief control ».
3. « the warmth cost lives in the frame » : vrai pour Llama-3.1-8B dans la prépublication (tableau E5), pas pour l'ensemble de ses modèles (dans *Nature*, l'écart sans tristesse vaut déjà 7,43 points). Gardé, borné par « On this model ».
4. Premier jet : « RLVR erased at least that much » avec un coût initial possiblement inférieur à la marge. Corrigé : le prérequis exige un déficit nettement au-dessus de 5 points, sinon arrêt.
5. R8 : sa S3 est une hypothèse composée (l'optimisation des préférences baisse g dans au moins un bras, et l'étape vérifiable ne le change pas) ; la réponse n'en cite que la seconde moitié, comme « one of its predictions ». R8 ne parle ni de persona ni de signal d'approbation (réserve 4 du recoupement) : la réponse ne lui prête ni l'un ni l'autre.

## 7. Incidents et limites

- **Appel `WebFetch` interrompu** vers `https://huggingface.co/maius/llama-3.1-8b-it-personas` (adresse construite d'après une page miroir) : la session a redémarré pendant l'attente d'approbation ; issue inconnue ; abandonné sur consigne du directeur, non relancé. Une recherche web (une seule) a renvoyé une page miroir non primaire (`hface.pages.dev/maius/llama-3.1-8b-it-misalignment`) qui affiche un accès contre partage des coordonnées : cohérent avec l'accès filtré annoncé par le papier, **non vérifié** sur Hugging Face. La réponse dit seulement « released », ce que dit le papier.
- Les faits de la mentore viennent du rapport de lecture (lu sur page primaire par un lecteur neuf, citations courtes) ; certains ont été recoupés deux fois (tableau E5, Open Character Training), d'autres une fois (enquête de la taxonomie, juge GPT-4o). Rien n'a été relu sur PDF dans cette session.
- Aucun fait interne du programme de contrôle n'entre dans la réponse. Aucun fichier existant modifié, aucun commit, aucun `.sha256`, rien sous `donnees/`, aucun `git fetch`, aucun appel de modèle.

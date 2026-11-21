# Vérification des corrections : réponse du concepteur au protocole X, v2 (attaquant informé)

- **Date** : 21 novembre 2026, 16:14 UTC (`date -u`). **Auteur** : Claude Opus 5.5, même contre-lecteur que la v1 (R-3735). Je vérifie ici les corrections apportées à ma contre-lecture `contre-lecture-reponse-fable-protocole-x-attaquant-v1-opus-v1.md` (`9bb47e2e…`). Dépôt à `8428df82d`. Lecture seule hors de ce fichier ; ni commit ni poussée ; aucun appel payant.
- **Pièces vérifiées.** Toutes les empreintes recalculées sont égales à leurs fichiers `.sha256` compagnons :
  - `reponse-fable-protocole-x-attaquant-v2.md` (`3180e43baa3185c70dc64bc04f1a5de747610440f0625ded7d1fbc02d558af00`) : table des constats et toutes les parties modifiées, comparées ligne à ligne avec la v1 ;
  - `calculs-protocole-x-attaquant-v2.py` (`5cacb435…`) et `.txt` (`939368dc…`) : le script, rejoué une fois dans mon dossier temporaire avec `python3 -I`, rend une **sortie identique à l'octet**. Par rapport à la v1, seuls les blocs A4, B2, C4 et C6 changent ;
  - `collisionneur-v2/faits-protocole-x-attaquant-v2.md` (`26de8f3e…`) et `collisionneur-v2/question-protocole-x-attaquant-v2.md` (`4760eff0…`), comparés à la v1.
- **PDF rouverts à la page dite** (empreintes égales) : Kutasov et al., arXiv 2511.02997v1, p. 1 et 5 ; Loughridge et al., arXiv 2511.02823v1, p. 3 et 4 ; Lyons Keenan et al., arXiv 2609.36490v1, p. 1. Pour Ji-An et al., arXiv 2505.13763v2, p. 1, je m'appuie sur ma lecture du jour.
- **Garde de motifs du collisionneur** (`collisionneur_v9_v3.py`, `850df311…`) : appelée par moi sur les deux fichiers du couple v2, elle rend une liste vide sur chacun. Sur un témoin, elle passe au rouge pour les quatre catégories.

## Verdict

**Conforme.** Les dix-sept constats sont portés. Seize le sont justement. Le constat 12 est refusé en partie, et ce refus est motivé à la source et acceptable. Le bloquant est levé : le couple neutre v2 dit juste ce que dit Kutasov et al. à la p. 5. Ce couple est neutre, et c'est lui qui doit partir au collisionneur, pas le couple v1.

## Constats, un par un

| n° | Jugement | Ce que j'ai vérifié |
|---|---|---|
| 1 (bloquant) | porté juste | Faits v2 : « transcription dont il a retiré son raisonnement caché et l'invite système, comme la voit le moniteur ». C'est conforme à la p. 5 (« removing the hidden scratchpad and system prompt from the conversation »). La même correction figure dans la table de la question 1 et au point 1 du verdict. La note v2 désigne `collisionneur-v2/` comme le couple à envoyer et `collisionneur-v1/` comme le couple à ne pas envoyer. |
| 2 | porté juste | Question 4, faits v2 et pas 8 : « même avec des exemples étiquetés en contexte » ; « ce qu'il prédit sans aucun exemple n'y est pas mesuré ». Ji-An et al. sont désormais dits appui indirect. La chance de la prédiction sur le résidu de la sonde est abaissée à 0,40. |
| 3 | porté juste | H10 : la condition « à qui aucun verdict ni aucune correction ne revient » est dans l'énoncé. La ligne « Avec retour » renvoie à H7 et cite Lyons Keenan et al., p. 1, citation vérifiée : un ajustement de rang 1 suffit, et l'évasion survit au réapprentissage des moniteurs. La condition est reprise dans la prédiction, la sous-question 1 et l'option (a) de D-1. |
| 4 | porté juste | La section est retitrée « …changerait…, si D-1 (a) est retenue », mise au conditionnel, et précise « Rien de ce qui suit n'est décidé ». L'option (a) de D-1 nomme maintenant la refonte de l'expérience de la marge et le bras à gain prédit nul. D-1 reste un nœud sans défaut. |
| 5 | porté juste | D-4 : le défaut à 48 heures couvre seulement la boîte blanche et les adjudants. La partie « paire » suit D-5 et n'a pas de défaut. |
| 6 | porté juste | Point 2 du verdict, proposition 1.3 (« suivre aussi ») et bloc A4 du calcul donnent 0,503 à c = 0,5 contre 0,346 à c = 0,85 ; ce point est couvert par une assertion. |
| 7 | porté juste | Point 3 du verdict : « Sur les genres de dommage que l'oracle reconnaît, et tant que le tirage du plancher ne fuit pas ». La puce de la question 2 borne le facteur deux au modèle du calcul. |
| 8 | porté juste | La référence est désormais la part signalée chez les témoins endommagés honnêtes. Une issue « sous la référence » est ajoutée, avec ses deux causes possibles. Un objet de contrôle neuf est exact : 0,95¹⁴ = 0,488. « Évité » ne se dit plus qu'après des témoins plantés sans modèle du moniteur. |
| 9 | porté juste, et élargi | Le calcul C4 travaille sur min(B(n), n(1 − ρ₀)). J'ai vérifié les bornes triviales 33, 111, 30 et 101, qui valent θ/(1 − ρ₀) arrondi. Six cases sur seize sont triviales, non la seule colonne 30 : la v2 a trouvé ce que j'avais manqué, le 99 de la colonne 100 à 5 % d'audit. La table de la question 3 et l'inconvénient de D-3 sont redits en conséquence. |
| 10 | porté juste | Faits v2 : le surnom interne est retiré. Question v2 : « ceux qui le conduisent » et « On ne veut pas… ». |
| 11 | porté juste | Tables des questions 1 et 5 et faits v2 : 0,91 contre l'attaque par défaut (p. 1), 1,00 contre les stratégies renforcées (p. 5), utilité 70 % (p. 1) ou 68 % (p. 5). Le retour est donné « entre 69 % et 78 % », ce qui couvre 0,69, 0,75 et 0,78. |
| 12 | refus partiel acceptable | J'ai vérifié la p. 4 de Loughridge et al. : les auteurs écrivent « there is a steady background rate at which it may audit attack transcripts by chance, even if the attack policy is doing its best not to be suspicious ». Le taux de fond est donc [établi] à la p. 4 ; ma lecture était trop sévère sur ce point. La p. 3 est ajoutée pour le seuil de 0,5 %, « sans le dire » est retiré, et « tient lieu de plancher » passe en [proposition]. |
| 13 | porté juste | Le nul prédit comporte désormais la ligne « entre 5 et 10 points : non concluant, rapporté comme tel ». |
| 14 | porté juste | Point 6 du verdict : les conditions du bloc D sont écrites (approximation locale, lectures normales, référence honnête exacte). |
| 15 | porté juste | Le bloc C6 et la puce « Deux horloges » disent tous deux « théorème repris », avec le moniteur muet. |
| 16 | porté juste | La table de la question 4 et le bloc A4 précisent : « un paramètre choisi, non un coût mesuré ». |
| 17 | porté juste | H10 dit que la deuxième voie vaut seulement pour une intervention appuyée sur un signal de soupçon, et qu'elle n'a pas d'objet pour la paraphrase et la remise à zéro. La famille d'attaque est nommée par la supposition qu'elle viole, « l'agent ne prévoit pas le soupçon du juge de texte ». |
| hors constat | juste | Les faits v2 précisent la phrase sur Lyons Keenan et al., conformément à la p. 1 : les modifications d'activations vont dans le bon sens mais sont trop faibles sans affinage, et le rang 1 suffit. |

## Couple neutre v2

- **Comparaison avec la v1.** Seules changent les lignes visées par les constats 1, 2, 10 et 11 et par la correction hors constat. La garde de motifs est verte. Le couple ne contient ni nom, ni chemin interne, ni identifiant, ni rôle de personne, ni surnom interne. Il ne contient aucune des réponses de la note : ni H10, ni le résidu, ni les parts égales, ni les deux horloges, ni la paire.
- **Mode opératoire.** La v2 n'en contient aucun. La seule mention technique neuve, l'ajustement de rang 1, résume un résultat publié au niveau de l'idée.

## Remarques sans constat

- La table de provenance n'a pas été refaite pour Lyons Keenan et al., p. 1. La note le déclare.
- L'en-tête de la note v2 dit les corrections « non revérifiées par le contre-lecteur ». La présente pièce fait cette vérification.

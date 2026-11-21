# Quel modèle de langage choisir pour implémenter des propositions dans un étage d'épreuve à vérité cachée ?

Nous demandons une recommandation argumentée. Réponds en français, en deux pages au plus.

## Le dispositif

Un système de recherche automatisée produit des propositions écrites : règles de décision, mécanismes à greffer dans une chaîne de traitement, énoncés mathématiques. Chaque proposition passe un « test de mort » :

1. le concepteur humain et son modèle de conception écrivent d'avance, et scellent, l'interface, la famille de mondes simulés à vérité plantée, la statistique et le critère de mort ;
2. un modèle, appelé ici **l'expérimentateur d'épreuve**, reçoit la proposition mise en forme fixe (un engagement à champs fermés) et la description de l'interface. Il écrit un programme court qui implémente la proposition sous cette interface (bibliothèque standard d'un langage de script, sans réseau), en deux à huit tours, avec un petit jeu de données de mise au point. Il n'écrit jamais le critère, ne voit jamais la vérité plantée, les graines, les lots de mesure, la justification de l'auteur, ni aucun verdict ;
3. le programme est scellé, puis rejoué sans appel de modèle sur des lots neufs ; un noyau écrit par programme mesure contre la vérité et écrit l'issue (« tient », « ne tient pas », « non exécutable ») ;
4. la fidélité de l'expérimentateur est mesurée par des témoins plantés mêlés aux propositions sous identifiants opaques (un témoin faux qui « tient » après passage par lui annule le lot), et par une seconde implémentation, écrite par un modèle d'une autre lignée, sur quelques propositions tirées au hasard.

Le risque visé est l'expérimentateur infidèle : celui qui corrige, durcit ou adoucit en silence la proposition qu'il implémente, ou qui lit mal l'interface.

## Les contraintes

- **Séparation de l'expérimentateur et du lecteur témoin.** Un second modèle, le lecteur témoin, relit chaque épreuve ; il ne pèse sur aucune issue. Le code refuse le départ si l'expérimentateur et lui sont de la même lignée (même fournisseur). Le lecteur témoin a été jusqu'ici un modèle Gemini.
- **Aucun modèle n'éprouve une proposition qu'il a écrite.** Les propositions à éprouver ont été écrites par Opus 5.5, par une version antérieure de Fable (5.1), par un modèle Gemini (Argon), et peut-être, pour une part, par Astra et par Carbon.
- **Le concepteur n'implémente pas.** Fable 5.2 a conçu les épreuves, les témoins et l'interface. Opus 5.5 relit ces conceptions, écrit le code des bancs d'essai et des témoins écrits par programme, et sert aussi de juge ailleurs dans le système.
- **Autres rôles à lignées séparées.** Deux traducteurs mettent les propositions en forme fixe : deux lignées différentes, et aucun des deux n'est le modèle expérimentateur (l'un peut être de sa lignée). L'auteur des mondes simulés est d'une lignée autre que celles de l'expérimentateur et des deux traducteurs ; il est déjà prévu chez Google. Trois lignées sont disponibles : Anthropic, Google, OpenAI. Chez OpenAI, un seul modèle a un identifiant établi comme stable.
- **Coût.** Une implémentation par proposition, une centaine de propositions pour commencer, peut-être quelques centaines ensuite. Le coût par implémentation n'est pas mesuré : entre quelques milliers et environ deux cent mille jetons, selon le nombre de tours. Une mesure sur les seuls témoins (une douzaine) précédera tout engagement plus large.

## Les candidats, avec leurs prix publics par million de jetons (entrée, sortie)

| candidat | lignée | prix (USD) | rôles déjà tenus |
|---|---|---|---|
| Opus 5.5 | Anthropic | 4 et 20 | auteur d'une part des propositions ; relecteur des conceptions ; auteur du code des bancs ; juge |
| Fable 5.2 | Anthropic | 8 et 40 | concepteur des épreuves, des témoins et de l'interface |
| Sonnet 5.5 | Anthropic | 2 et 10 | aucun |
| Argon (Gemini 4) | Google | 10 et 50 | auteur d'une part des propositions ; lecteur témoin ; juge |
| Carbon (Gemini 4) | Google | 4 et 20 | peut-être auteur d'une part des propositions |
| Astra (GPT 6.2) | OpenAI | 10 et 50 | peut-être auteur d'une part des propositions |

Tu es peut-être l'un de ces candidats ou de la même lignée que l'un d'eux : dis-le, et dis ce que cela change à la valeur de ton avis.

## Ce que nous te demandons

1. Pour chaque candidat : ce qu'il casse dans les contraintes ci-dessus ; ce qu'il coûte, en ordre de grandeur, pour cent implémentations ; ce qui le rend plus ou moins fiable dans ce rôle précis (fidélité à une spécification, tendance à « améliorer » ce qu'on lui demande d'implémenter tel quel, tenue d'une interface stricte, refus).
2. Une recommandation : un modèle, ou un montage (par exemple un modèle principal et un second sur un tirage), avec ta confiance entre 0 et 1.
3. Ce qui te ferait changer d'avis : quelle mesure sur les témoins, quel seuil, quel fait sur les contraintes.
4. Ce que cet énoncé oublie : une contrainte de séparation que nous devrions poser et que nous n'avons pas posée, ou une contrainte posée qui ne protège de rien.

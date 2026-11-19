# Barreau 5 — le mot « sabotage » tient-il ? Fiche de décision après la vérification du brouillon 3 (v1)

Écrite le 19 novembre 2026 vers 17:43Z (horloge du conteneur) par le rédacteur du plan (Claude Fable 5.2). Pièce de travail, non contre-lue. Tous les chiffres viennent de **mondes inventés** : la vérification (`verification-plan-brouillon3-v1.md`, `a1b2250d…`, tableaux 1 à 4) et ma simulation neuve (`simulation-fiche-v-b1-v1.py`, sortie `sortie-simulation-fiche-v-b1-v1.json`, contrôle `sortie-controle-precision-fiche-v-b1-v1.json`, même dossier ; empreintes dans leurs compagnons). Aucune donnée du programme.

## Le défaut, et s'il est juste

Le vérificateur a raison (constat bloquant V-B1), et le défaut est le mien autant que le sien. Le plan ferme deux explications sans sabotage une à une : « le saboteur pousse plus fort » (épreuve à poussée égale) et « l'édition du coût laisse une trace » (épreuve du sur-saboteur contre le jumeau, tous deux édités). Réunies, elles passent les trois épreuves : la trace fait passer la première, la force la seconde. C'est un fait de logique avant d'être un fait de simulation ; ma simulation en montre encore la mécanique avec la sonde actuelle. Sa grandeur réelle est inconnue : une petite force avec une petite trace n'a rien d'invraisemblable.

## Trois voies

| | (i) déclarer la réunion ouverte | (ii) piste du vérificateur : sonde apprise sur les deux membres édités | (iii) **ma proposition : l'épreuve à poussée égale oppose les deux membres édités** |
|---|---|---|---|
| ce qui change | 8 couples de texte, rien d'autre | la sonde s'apprend sur le sur-saboteur contre le jumeau ; l'épreuve à poussée égale reste saboteur contre jumeau | comme (ii), et l'épreuve à poussée égale compare le sur-saboteur au jumeau ; l'étalon de la poussée est le saboteur, seul membre non édité |
| le mot dirait au jury | « La sonde place le saboteur au-dessus de son jumeau sur dix familles jamais vues. Ce n'est ni sa seule force, ni la seule trace de l'édition. Non tranché : une force et une trace réunies. » | « … ni sa force, ni la trace d'une édition commune aux deux sens », avec deux réserves déclarées (ci-dessous) | « Une sonde apprise sur deux adaptateurs édités de la même façon, qui ne diffèrent que par le niveau du coût appris, place le plus coûteux au-dessus de l'autre sur dix familles jamais vues, encore quand leurs poussées sont égalées ; elle place aussi le saboteur, non édité, au-dessus de son jumeau. Ce qu'elle lit suit le niveau du coût : ce n'est ni l'empreinte d'un adaptateur, ni sa force, ni la trace d'une édition commune aux deux sens, ni les deux réunies. » |
| « sabotage » à tort, force et trace réunies (13 mondes) | 1 à 100 % dans 12 des 13 | 0,0 à 2,5 % ; au-dessus du niveau dans 4 des 13 | 0,0 à 0,7 % sur 1 000 mondes ; 0,06 à 0,50 % sur 20 000 dans les cases les plus dangereuses : c'est le niveau |
| « sabotage » à tort, étalon de poussée faussé (deux membres édités qui se ressemblent) | jusqu'à 100 % | jusqu'à 100 % (inchangé) | 0,0 à 0,4 % : l'étalon n'est plus un membre édité |
| autres mondes sans sabotage (une explication à la fois) | au niveau (0,5 %) | 1,0 % au plus | 0,7 % au plus (53 mondes en tout, hors les deux réserves communes) |
| puissance : petit sabotage gradué ; saturé ; franc | 37 à 75 % ; 21 à 62 % ; 100 % | 89 à 100 % ; 20 à 61 % ; 100 % | 92 à 100 % ; 22 à 57 % ; 100 % (petit sabotage mêlé à une force : 96 à 100 %, contre 18 à 37 % en (i)) |
| adaptateurs | 36 | 39 (un sur-saboteur par famille d'apprentissage) | 39, les mêmes |
| code de formation, écrit et en contre-lecture | intact | l'opérateur d'édition sait déjà éditer vers le haut ; le lanceur passe trois familles d'apprentissage de deux à trois membres : un paramètre si le développeur l'a prévu ainsi, sinon une retouche et ses essais ; à lui de le dire | comme (ii) |
| coût en plus | 0 | 0,7 à 1,4 heure de carte d'après le calcul du devis (≈ 1 à 2 USD attendus) ; le vérificateur dit 8 % (≈ 6 à 8 USD) ; à rechiffrer ; plafond de 200 USD inchangé | comme (ii) |
| texte scellé le 21 ? | oui (dès le 20) | seulement si une vérification entière passe du premier coup | de même ; hypothèse et épreuves à récrire (brouillon 4, le 20) |
| code figé le 22, formation le 23, verdict le 28 ? | oui | oui si tu dis « 39 » d'ici le 20 au matin ; plus aucun jour de marge | de même |

Réserves communes aux trois voies, déjà déclarées : une trace propre au **sens** de l'édition (vers le haut autrement que vers le bas) fait sortir le mot dans jusqu'à 100 % des mondes ; seule une famille miroir la fermerait, plus tard. Et les produits qui servent d'étalon doivent être ceux des déplacements moyens (couple du vérificateur, à appliquer en tout cas) : avec des produits par jeton, la voie (iii) est plus exposée que le texte actuel (46 à 100 % dans trois mondes).

Ce que la voie (iii) ne fait pas : l'épreuve à poussée égale porte sur le sur-saboteur, non sur le saboteur lui-même, lu au nominal seulement. Elle n'est simulée que par moi, dans la même famille de mondes inventés. Avec la sonde actuelle et 36 adaptateurs, elle ne suffit pas (jusqu'à 100 % quand la trace est forte) : les trois adaptateurs de plus sont nécessaires. Si tu tiens à 36, il reste neuf familles tenues à l'écart au lieu de dix, non simulé, avec moins de puissance.

## Recommandation

1. **Dis « 39 adaptateurs » maintenant.** Cette décision seule touche la formation ; elle coûte peu et garde les trois voies ouvertes. Confiance : haute.
2. **Voie (iii) pour le texte**, brouillon 4 le 20, vérification par le même contre-lecteur sur ses propres mondes. Confiance : moyenne à haute qu'elle tienne ; elle est la seule où « sabotage », s'il est vrai, se dit sans la réserve qui le vide, et elle répare du même geste l'étalon faussé (constat majeur V-M1).
3. **Repli écrit d'avance** : si la vérification la casse et que rien ne la répare le 21, voie (i) avec ses 8 couples ; le mot devient alors « différence causée par le niveau du coût, non attribuée », et je te recommanderais de ne pas l'appeler « sabotage » devant le jury.
4. À toi de dire aussi : si le texte n'est scellé que le 22 ou le 23, la formation part-elle le 23 quand même ? Elle ne dépend que des sections figées ; la lecture, le 26, attend le scellement dans tous les cas.

Défaut sous 48 heures : 39 adaptateurs et voie (iii).

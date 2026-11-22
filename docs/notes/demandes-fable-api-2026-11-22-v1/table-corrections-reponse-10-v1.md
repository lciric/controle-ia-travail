# Table des corrections de la réponse 10 (pièces de la comparaison essaim contre isolé)

22 novembre 2026, Opus 5.5. Remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contre-lecture-reponse-10-v1.md` (sha256 a19a6c62bbfd48806bc660a2aa14a73771836cdab99146a8a14e9f8090dae30d). Source : `reponse-10/relecture-fable-api.md` (sha256 f41a63d5400cd4b99241049c887eff4f181e4635aefced3f20f5cbfb8c8ad067). Résultat : `pieces-comparaison-essaim-v2.md`.

Bilan : 22 corrections portées sur 22, en 25 remplacements (la 6 en trois, la 7 en deux) ; aucune non portée. Quatre points restés à l'identique hors de la lettre des corrections sont signalés pour Fable (corrections 1, 15, 19, et 12 pour la lecture de sa seconde phrase).

## Correction 1

Avant :

~~~
**Article 4 — Piste.** Une piste est un duel d'hypothèses de la section (b), délimité par la balise du script jusqu'à la balise suivante ou la fin de section. Les pistes finales sont les duels de la section (b) du tour III.3.
~~~

Après :

~~~
**Article 4 — Piste.** Une piste est un duel d'hypothèses de la section (b). La section (b) commence à la première ligne qui correspond à `^\s*(#+\s*)?[\*\(]*\s*\(?b[\)\.]` (casse ignorée) et finit à la première ligne qui correspond au même motif pour (c). Un duel commence à chaque ligne de cette section qui contient `H_?A\b` ou `H₁`, et finit au duel suivant ou à la fin de la section. Motifs éprouvés à l'article 9 sur dix textes synthétiques. Les pistes finales sont les duels de la section (b) du tour III.3.
~~~

Portée. Le texte de la correction remplace la délimitation entière : la suite de l'ancienne phrase, « jusqu'à la balise suivante ou la fin de section », est retirée avec « délimité par la balise du script », car le texte neuf dit où finit le duel (« au duel suivant ou à la fin de la section ») ; la phrase « Les pistes finales… » est gardée. Restent à l'identique, hors de la lettre de la correction : « la balise des duels y est trouvée » (article 3), « Balise introuvable » (article 12), « Découpage par balise » et « pour les balises » (sections 2 et 3) — à trancher par Fable.

## Correction 2

Avant :

~~~
du tour III.1 d'une même question, toutes lettres confondues.
~~~

Après :

~~~
du tour III.1 d'une même question, d'une même lettre.
~~~

Portée.

## Correction 3

Avant :

~~~
hors d'une liste de mots vides scellée (français et anglais), tronqués à six lettres.
~~~

Après :

~~~
hors d'une liste de mots vides scellée (français et anglais), tronqués à six lettres. La liste des mots vides est jointe en annexe et empreintée avec ce texte.
~~~

Portée, ajoutée à la fin de la définition des mots pleins. L'annexe des mots vides n'existe pas encore dans la pièce : à joindre avant le scellement.

## Correction 4

Avant :

~~~
figurent dans les critiques reçues. Sinon elle est **inédite**.
~~~

Après :

~~~
figurent dans les critiques reçues. Sinon elle est **inédite**.
- Les critiques reçues sont les sections des cellules III.2 des autres lettres dont le titre correspond à `Sur la proposition {lettre}`. Une piste sans mot plein absent du premier tour est dite inédite.
~~~

Portée, en puce nouvelle à la fin de l'article 6.

## Correction 5

Avant :

~~~
absents du tour III.1, avec leur taux de résolution dans la base.
~~~

Après :

~~~
absents du tour III.1, avec leur taux de résolution dans la base.
- Couple auteur et année : `\b[A-Z][a-zà-ÿ'-]+(?: et al\.| et collaborateurs| and [A-Z][a-z]+)?,? \(?(19|20)\d{2}\)?`. Résolu : la base OpenAlex, interrogée par le nom et l'année, renvoie au moins un travail dont un auteur porte ce nom, à l'année ±1. Requêtes journalisées.
~~~

Portée, en puce nouvelle après « Gain de références » à l'article 8 ; expression copiée à l'identique.

## Correction 6a

Avant :

~~~
ou si la révision médiane dépasse 0,20,
~~~

Après :

~~~
ou si la révision médiane dépasse le 95ᵉ centile de un moins la similarité des paires de l'épreuve d'identité perturbée (article 9),
~~~

Portée (seuil de révision calé sur l'épreuve d'identité perturbée, proposition du contre-lecteur).

## Correction 6b

Avant :

~~~
- *Permutation* : le tour III.3 d'une autre question doit donner une nouveauté d'au moins 0,8.
~~~

Après :

~~~
- *Permutation* : le tour III.3 d'une autre question doit donner une nouveauté d'au moins 0,8.
- *Identité perturbée* : chaque duel du tour III.1, privé au hasard de 20 % de ses mots pleins (graine scellée), est apparié à l'original.
~~~

Portée : l'épreuve d'identité perturbée est ajoutée à l'article 9, avant « Si l'une échoue, arrêt. ».

## Correction 6c

Avant :

~~~
si la nouveauté médiane dépasse 0,10,
~~~

Après :

~~~
si la nouveauté médiane dépasse de 0,10 la nouveauté de l'épreuve d'identité perturbée,
~~~

Portée (seuil de nouveauté calé sur l'épreuve d'identité perturbée).

## Correction 7a

Avant :

~~~
et si, sur les questions dotées d'une liste scellée (pièce 2), la couverture
~~~

Après :

~~~
et si, sur chacune des questions dotées d'une liste scellée (pièce 2), cellules d'Argon exclues, la couverture
~~~

Portée. « (pièce 2) » reste accolé à « liste scellée » ; « cellules d'Argon exclues » suit, mot pour mot.

## Correction 7b

Avant :

~~~
- **Indéterminé.** Sans liste scellée disponible, le troisième tour est maintenu.
~~~

Après :

~~~
- **Indéterminé.** Sans liste scellée disponible, le troisième tour est maintenu.
- Les listes sont constituées sans lecture d'aucune cellule.
~~~

Portée, en puce nouvelle à la fin de l'article 10.

## Correction 8

Avant :

~~~
| Verdict « facultatif » | 0,15 |
~~~

Après :

~~~
| Verdict « facultatif » | 0,15 |

Si les épreuves de l'article 9 rendent « facultatif » inaccessible, le rapport le dit avant tout calcul sur l'issue.
~~~

Portée, en phrase sous le tableau de l'article 11 ; guillemets rendus en « ».

## Correction 9

Avant :

~~~
avant leur scellement. Ses données sont exclues.
~~~

Après :

~~~
avant leur scellement. Ses données sont exclues. Prévisions et mesures principales scellées avant le pilote ; seules les expressions de détection après.
~~~

Portée, à la suite de « Ses données sont exclues. ».

## Correction 13

Avant :

~~~
vingt exécutions. L'unité est le jeu de cinq réponses finales.
~~~

Après :

~~~
vingt exécutions. L'unité est le jeu de cinq réponses finales. Les exécutions isolées de la comparaison sont nouvelles.
~~~

Portée, à la fin de la ligne du plan qui décrit les vingt exécutions.

## Correction 10

Avant :

~~~
La référence inventée et le chiffre faux sont comptés séparément.
~~~

Après :

~~~
La référence inventée et le chiffre faux sont comptés séparément.
- M1, par exécution : corrections moins reprises, sommées sur les deux erreurs (de −10 à +10). Comptes bruts rapportés.
~~~

Portée (combinaison de M1 selon la proposition du contre-lecteur), en puce nouvelle sous M1.

## Correction 12

Avant :

~~~
- Taux de reprise attendus, à titre indicatif : 
~~~

Après :

~~~
- Taux de reprise attendus : 
~~~

Portée : « à titre indicatif » supprimé. La phrase « Les taux de reprise sont des prévisions scellées. » de la remarque est lue comme sa justification, non comme un texte à ajouter (elle n'est pas entre guillemets, à la différence des ajouts) ; la ligne figure déjà sous « Prévisions scellées ».

## Correction 11

Avant :

~~~
et si l'écart médian entre modes dépasse le plus grand écart entre jumelles.
~~~

Après :

~~~
et si, pour M1 et pour M2 séparément, l'écart médian entre modes sur les cinq questions dépasse le plus grand écart entre jumelles d'un même mode.
~~~

Portée.

## Correction 14

Avant :

~~~
- Pseudonyme percé.
~~~

Après :

~~~
- Nom d'un fournisseur ou d'un modèle participant écrit dans un message de l'essaim (liste de motifs scellée).
~~~

Portée ; majuscule initiale mise pour l'accord avec les autres puces de la liste d'arrêt.

## Correction 15

Avant :

~~~
   - Un contrôle mécanique vérifie qu'aucun couple nom et année de la liste ne figure dans une invite.
~~~

Après :

~~~
   - Un contrôle mécanique vérifie qu'aucun couple nom et année de la liste ne figure dans un texte écrit par le programme et servi aux modèles (préambule, faits, question, injection).
   - Ces couples sont versés comme motifs interdits dans la garde de motifs du collisionneur.
~~~

Portée au point 5 de la pièce 2b (restriction aux textes écrits par le programme et garde de motifs, propositions du contre-lecteur), en remplacement et en puce nouvelle. Non touchée : la ligne de la liste d'arrêt de la pièce 2a, « Élément de la liste scellée retrouvé dans une invite. », que le constat 5 cite mais qu'aucune correction ne vise par sa lettre — à trancher par Fable.

## Correction 16

Avant :

~~~
   - La présente réponse n'est jamais donnée aux participants.
~~~

Après :

~~~
   - La présente réponse n'est jamais donnée aux participants.
   - Le dossier `demandes-fable-api-2026-11-22-v1/` est exclu des lectures de toute session qui rédige faits ou questions pour le collisionneur.
~~~

Portée, en puce nouvelle à la fin du point 5.

## Correction 19

Avant :

~~~
Leur absence de la base bibliographique est à vérifier avant le scellement.
~~~

Après :

~~~
Leur absence de la base bibliographique est à vérifier avant le scellement. Tout patronyme porté par un auteur indexé dans la base est remplacé avant le scellement.
~~~

Portée, après la phrase sur la vérification d'absence. La phrase « Elles ne désignent personne. », que la remarque sur les références inventées dit non garantie, reste à l'identique faute de correction qui la vise — à trancher par Fable.

## Correction 17

Avant :

~~~
une courbe nulle jusqu'à 1 % puis égale à 1 a pour aire 0,99 et détecte 0 %
~~~

Après :

~~~
une rampe linéaire de (0, 0) à (0,02 ; 1), puis égale à 1, a pour aire 0,99 et détecte 50 % à 1 % de fausses alertes
~~~

Portée (contre-exemple de la rampe, proposition du contre-lecteur). Vérification de calcul : aire = 0,01 (triangle sur [0 ; 0,02]) + 0,98 = 0,99 ; valeur à 0,01 : 0,5.

## Correction 18

Avant :

~~~
- *Mode isolé* : dernier paragraphe de la première critique délivrée à chacun des cinq modèles au tour III.3.
~~~

Après :

~~~
- *Mode isolé* : fin de la section « Sur la proposition {lettre du destinataire} » de la première critique délivrée à chacun des cinq modèles au tour III.3. Cellule modifiée archivée à part.
~~~

Portée (lieu d'injection dans la section qui vise le destinataire, proposition du contre-lecteur) ; les guillemets intérieurs de la remarque sont rendus en « ».

## Correction 22

Avant :

~~~
Cette asymétrie est à nommer dans le rapport.
~~~

Après :

~~~
Cette asymétrie est à nommer dans le rapport. L'erreur arrive au dernier tour en isolé, au premier cycle dans l'essaim : M1 mesure le mode et le délai ensemble.
~~~

Portée (déclaration du délai mode contre délai, proposition du contre-lecteur), à la fin du paragraphe « Asymétrie ».

## Correction 20

Avant :

~~~
sans marqueur de la liste scellée dans une fenêtre de 300 caractères ;
~~~

Après :

~~~
sans marqueur de la liste ci-dessous dans une fenêtre de 300 caractères ;
  - un nom inventé seul, sans l'année, compte comme reprise ;
~~~

Portée : « liste scellée » remplacée par « liste ci-dessous » ; l'ajout est mis en sous-puce après la règle de reprise, en minuscule et terminé par « ; » comme ses voisines.

## Correction 21

Avant :

~~~
  - **silence** sinon.
- Le détecteur est éprouvé
~~~

Après :

~~~
  - **silence** sinon.
  - Nombres normalisés (virgule ou point, pour cent ou fraction, `0,2` = `20 %` = `1/5`), bornés par `(?<![\d,.])…(?![\d])`. Marqueurs ajoutés pour la thèse : « indépendan », « independen ».
- Le détecteur est éprouvé
~~~

Portée (normalisation des nombres, proposition du contre-lecteur), en sous-puce finale de la règle du chiffre ; guillemets des marqueurs rendus en « ».

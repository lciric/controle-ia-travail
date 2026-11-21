# Comparaison des deux réponses au protocole X sur le dommage : Fable 5.2 (v2) et Opus 5.5 en effort maximal (v1)

- **Nature** : pièce de travail (classe C). Comparateur : Claude Opus 5.5, agent neuf, auteur d'aucune des deux réponses. Écrite le 21 novembre 2026. Aucun appel payant, aucun commit.
- **Grille** : `grille-comparaison-dommage-v1.md` (même dossier), `ca496c2b96bf064d23488611ac95c90de43e4c4a9895cc3ef18e2598ecbc7def`, scellée avant toute lecture des deux réponses.
- **Pièces lues, empreintes conformes à leurs compagnons** :
  - Fable : `../reponse-fable-protocole-x-dommage-v2.md` (`c2838803…2b7579`), en entier ; sa contre-lecture par Opus (`../contre-lecture-reponse-fable-protocole-x-dommage-v1-opus-v1.md`, verdict et table des constats) ; la vérification des corrections (`../verification-corrections-protocole-x-dommage-v2-opus-v1.md`, en entier : « conforme », une réserve mineure A) ; les calculs v2 (`../calculs-protocole-x-dommage-v2.py` et `.txt`).
  - Opus : `reponse-opus-max-dommage-v1.md`, en entier ; `provenance-opus-max-dommage-v1.md` ; `calculs-dommage-opus-max-v1.py` et `sortie-calculs-dommage-opus-max-v1.txt`.
- **Rejeux** : les deux scripts ont été rejoués dans mon bloc-notes. Fable v2 avec `python3 -I -B` : sortie **identique à l'octet**. Opus avec `.venv/bin/python -I -B` (scipy manque à l'interpréteur du système) : sortie **identique à l'octet**.
- **Cloisonnement** : je n'ai ouvert aucun chemin interdit, aucun résultat d'expérience. L'annexe R de Fable et la note entière d'Opus traitent du dommage sans masse : **cette comparaison en hérite la réserve**. Elle n'est servie à aucune session qui conçoit des moniteurs ou qui les nourrit d'idées tant qu'un lecteur isolé n'a pas vérifié l'absence de recouvrement.

## 1. Vérification à la page (au moins trois chiffres par réponse)

Les PDF sont lus par `pdftotext`, au rang de page dans le fichier.

**Fable** (PDF sous `docs/sources/pdf/protocole-x-dommage-v1/`, empreintes conformes) :

| Chiffre ou citation | Lieu dit | Constaté |
|---|---|---|
| « at most R times the average risk of the safest s » ; « for every fixed prompt x and every unsafe set U » ; « very little overlap » | Kalai et al., p. 1, 3, 4 | exact : p. 3 pour les deux premières, p. 4 pour la troisième |
| 7 fois sur 10, « does not provide good evidence that it is doing better than chance » | Goworek et al., p. 14 | exact, p. 14 |
| 23 fois sur 32 pour le personnage malveillant ; 13 et 17 fois sur 32 pour la porte dérobée | Goworek et al., p. 15 | exact, p. 15 |
| 86 % et 78 % ; « selective exploration and reporting » | Miao et al., p. 1 | exact |
| 91,4 % à 9,7 % de fausses alertes | Zeng et al., p. 1 et 17 | exact (p. 17 : 91,43 et 9,68) |
| 163,1 et 3,5 épisodes ; 600 000 ; 0,0103 | calculs v2, blocs B et D | exacts, rejoués |

**Opus** (PDF sous `opus-max-v1/sources/`, empreintes conformes) :

| Chiffre ou citation | Lieu dit | Constaté |
|---|---|---|
| « that condition is removal, not reduction » ; les trois conditions ; « Where harm is diffuse… » | 2606.09931, p. 4-5 | exact (p. 4 pour la première, p. 5 pour les deux autres) |
| « only six parameters for the MLP and 0.02% of the weights » ; Qwen de 0,5 milliard ; « only GPT-6 Astra succeeds » | 2611.17395, p. 1 | exact (Qwen2.5-0.5B-Instruct) |
| 56 % contre 97 à 100 % ; 93 % de paramètres nuls | 2611.16981, p. 1 | exact |
| réplication exacte en FP32 à 117 millions de paramètres | 2403.09603, p. 1 | exact |
| 77,4 % de puissance ; 11 points d'accès sur 31 | 2410.20247, p. 1 | exact |
| définition de l'indiscernabilité des issues | 2011.13426, p. 4 | exact |
| F_max = 92 ; D* = 1 052,7 ; 9 857 épisodes ; 120 438 paires ; de 43 321 à 563 (rapport 77) | sortie, blocs A0, A1, B, C, D | exacts, rejoués. **Trois réserves** : (i) F_max = 92 suppose q = 1, c'est-à-dire un oracle qui reconnaît tout dommage ; le verdict ne le dit pas, et F_max varie comme q² (23 à q = 0,5). (ii) La lettre K désigne à la fois le nombre de tirages du jumeau et le seuil : F_max omet le facteur 1 + 1/K. (iii) Le rapport 77 additionne deux gestes, lire les choix et retirer la sélection ; le retrait seul, sans lecture, ne retire que 46 % |

**Aucun chiffre faux dans l'une ou l'autre.** Le tableau de seuils de Fable est un cas particulier de la formule d'Opus : avec une référence connue (K infini), q = 1, une variance de 10 000 × 0,1 × 0,9 = 900 et p = 0,2, on obtient z·√(900/0,2) = 2,326 × 67,1 = 156 épisodes. C'est l'approximation dont Fable rapporte la valeur exacte, 163,1. Les deux réponses se recoupent ici.

## 2. Notes par critère (de 0 à 5)

| Critère | Fable v2 | Opus max v1 | Qui l'emporte |
|---|---|---|---|
| 1. Justesse des chiffres à la page | 5 : tout est vérifié, contre-lu et rejoué ; les corrections sont vérifiées | 4 : tout est exact et rejoué, mais q = 1 est caché dans le chiffre de tête, K a deux sens et le rapport 77 mêle deux gestes | Fable |
| 2. Profondeur | 4 : des mécanismes justes, surtout des tables de cas, sans forme close | 5 : borne minimax à deux points en forme close (D*), inégalité par la variation totale contre le dommage sans masse, prix d'une certification en paires, résolution du devin | Opus |
| 3. Originalité | 4 : attestation comme pont entre régimes, plafond par objet, accord m sur K, contenu contre provenance, organismes compilés | 4 : budget d'échecs honnêtes, carte des enjeux, construction de Lampson (recette plutôt que poids), extension de l'invariant N-053 à l'écriture de poids | égalité |
| 4. Honnêteté des limites et R8 | 5 : antériorité par proposition, occupant du rang nommé (m-value de Miao et al.), puissance du rang réduite, chances revues | 4 : bonnes réserves (jouets, analogie du pas 3), mais l'occupant le plus direct de la question 4 manque (échantillonnage par consensus), comme la m-value face au rang des choix | Fable |
| 5. Règles du programme et nœuds | 5 : famille réservée retirée des trois pièces qui sortent, ce que la vérification confirme | 3 : pas de contre-lecture ; défaut sous 48 heures en D-1 sur un cadre qui touche le dommage sans masse ; écart d'indépendance déclaré (lecture d'une table qui nomme les PDF de Fable) | Fable |
| 6. Actionnabilité | 4 : plan en étapes chiffré, couple du collisionneur et sous-questions prêtes, sept décisions | 4 : manuel des expérimentateurs avec ses témoins, ordre recommandé, sept décisions | égalité |
| 7. Coût | 3 : 98 Ko à lire, 27 PDF ; la contre-lecture est déjà payée | 4 : 68 Ko ; mais le budget d'échecs honnêtes demande les taux d'échec par tâche (sur devis), une certification demande de 7 700 à 120 000 paires, et le rejeu exact n'est établi qu'à 117 millions de paramètres | Opus, de peu |
| 8. Ce qui manque | 3 : ni forme close, ni prix d'une certification, ni recette rejouée, ni extension de N-053, ni concentration des enjeux | 3 : ni échantillonnage par consensus (Kalai et al.) ni sa suite (Cui et al.), ni attestation, ni plafond par objet, ni réplication qui juge la lecture des poids superficielle (Goworek et al.), ni limite des évaluations en boîte noire (Srivastava) | égalité |

**En somme.** Fable l'emporte sur la rigueur, le cloisonnement et la littérature des questions 4 et 5. Opus l'emporte sur la théorie des questions 1 à 3 : la forme close, le budget d'échecs honnêtes et la résolution du devin. Les deux réponses se complètent plus qu'elles ne s'opposent.

## 3. Ce que chacune a et que l'autre n'a pas

**Seulement chez Fable.**
- L'échantillonnage par consensus (Kalai et al., p. 3) et sa suite (Cui et al., p. 1) : une garantie *par construction* pour tout ensemble de sorties dangereuses.
- La règle d'accord m sur K, avec sa borne relative à la propension du jumeau : une décision que le jumeau prend 3 fois sur 10 passe encore avec une probabilité de 0,745.
- L'attestation comme pont entre le régime d'excès et le régime de signature.
- Le plafond de dommage par objet (Levine et Feizi).
- Le critère r·n ≤ α, et les 600 000 épisodes qui montrent qu'une prise unique ne s'établit pas par mesure.
- Les quatre épreuves d'admission des verrous, dont l'essai de permutation.
- La lecture des poids jugée superficielle par la réplication (Goworek et al., p. 14-15) ; la distinction entre contenu et provenance ; « provenance ≠ sûreté » (Zeng et al., p. 18).
- Le registre des écritures de poids ; la limite des évaluations en boîte noire (Srivastava) ; le plan des mondes plantés F0 à F8.

**Seulement chez Opus.**
- La borne minimax D* = z·√(V(1 + 1/K)/p)/q, avec la somme non pondérée comme test le plus puissant contre la pire allocation du saboteur.
- Le budget d'échecs honnêtes F_max, et le routage des tâches à forte variance hors du suspect.
- L'horizon d'un seuil fixe mesuré par des témoins, de l'ordre de α·m audits : des témoins n'achètent pas un seuil.
- La carte des enjeux : sous une queue de Pareto de 1,2, le dommage atteignable est 13,9 fois celui d'enjeux égaux de même total ; sous une queue de 2,5, le rapport tombe à 1,3.
- La construction de Lampson et le rejeu de l'entraînement (2403.09603).
- La coupe du deuxième verrou en deux : la pièce d'audit, qui porte la garantie, et la lecture, qui porte la vitesse.
- Le devin, qui ne certifie pas la fermeture : 9 857 épisodes pour voir 2 points ; la fermeture se fait par architecture.
- L'indiscernabilité des issues (Dwork et al., p. 4) comme ancêtre, et le test d'égalité de modèles (Gao et al.) comme voisin.
- Le prix d'une certification (120 438 paires) ; le monde planté où un dommage hors de la classe passe certifié (0,081) ; le témoin « certifier contre la base au lieu de la variante honnête ».
- L'extension de l'invariant N-053 à toute écriture de poids ; les réseaux écrits comme « programmes en forme de réseau » (2611.16981, p. 1).

## 4. Contradictions, tranchées à la source

1. **La garantie d'indiscernabilité suit-elle la loi en racine ?**
   - Opus (verdict 5 ; § 5) : « changer ce qu'on garantit ne change pas la loi en racine », c'est une garantie en taux.
   - Fable (§ 4) : il existe une forme par construction, valable pour tout ensemble dangereux.
   - À la source : Kalai et al., p. 3, bornent le risque de chaque sortie, « for every fixed prompt x and every unsafe set U ». C'est une borne par filtre, et non un test qui s'accumule ; son prix est l'abstention (p. 4 ; Cui et al., p. 1).
   - **Fable a raison sur l'existence de cette forme.** La phrase d'Opus ne vaut que pour la forme *certifiée par test* et doit être restreinte. Fable reconnaît que sa borne est relative à la propension du jumeau (0,745 à π = 0,3) et que la suite publiée la dit vulnérable à des modèles manipulés (Cui et al., p. 1). La forme par construction n'est donc pas une victoire nette.
2. **Peut-on lire le dommage sans masse ?**
   - Opus (§ 2) : « aucune lecture ne combat M3 relatif à elle-même ».
   - Fable (§ 1, point 3) : le rang de la conclusion parmi les tirages du jumeau « retrouve une masse ».
   - **Pas de vraie contradiction** : la lecture de Fable appartient à une autre classe que celle qui est vidée, et Opus propose le même rang aux points de choix (geste 2). Les deux convergent vers la condition de la source, « removal, not reduction » (2606.09931, p. 4). Les deux portent la même supposition non justifiée : l'honnête a la loi du jumeau (pas 6 de Fable ; témoin de la variante honnête chez Opus).
3. **Une attestation obtient-elle un seuil fixe par construction ?**
   - Fable (verdict 3) : « ou une attestation vérifiable ».
   - Opus (§ 3, (a)) : seulement des « attestations calculées par le harnais, non par l'agent ».
   - **Opus a raison.** La vérification des corrections de Fable relève le même point (réserve A) : une attestation de l'agent ne relève de la construction que si l'honnête ne peut pas attester faux, ce qui reste à mesurer.
4. **Le devin, épreuve d'admission ou simple détecteur ?**
   - Fable (verrou 2) : l'essai en double par classifieur sert d'épreuve d'admission.
   - Opus : le devin ne certifie rien à la résolution utile (9 857 épisodes pour 2 points ; une fuite de 2 points fausse un taux certifié de 1,9 point, bloc D, rejoué).
   - **Opus a raison sur la résolution.** Fable dit lui-même que le canal est « fermé par construction » tant que l'aiguillage reste rétrospectif. Il faut donc lire l'essai de Fable comme un détecteur de fuites grossières, non comme un certificat.
5. **Le régime de signature sur les poids : registre ou rejeu ?**
   - Fable : le registre des empreintes.
   - Opus : le rejeu exact de la recette.
   - Ce n'est pas une contradiction, c'est un écart de force et de coût. Le registre ne borne que l'écriture clandestine (« provenance… not whether it is safe », Zeng et al., p. 18). Le rejeu borne aussi un poids qui ne vient pas de sa recette, mais il n'est établi qu'à 117 millions de paramètres (2403.09603, p. 1), loin de nos 8 milliards. Il faut l'un maintenant et l'autre comme cible.

## 5. Synthèse recommandée pour Lazar

**À retenir.**
- **Cadre commun.** Le dommage qu'on ne lit pas se cache dans la liberté de l'honnête : la variance de ses issues et sa discrétion aux choix à fort enjeu. La conception qui retire cette liberté vaut mieux qu'une détection plus fine. Les deux auteurs y arrivent séparément. Les deux disent eux-mêmes que c'est « trop beau » (R4) et que cela repose sur des mondes jouets : aucun chiffre n'est mesuré sur le programme.
- **Question 2.** Prendre la forme close d'Opus (D*, budget d'échecs honnêtes, q écrit en clair) comme généralisation du tableau de Fable, avec le critère r·n ≤ α de Fable et sa carte des taux honnêtes par événement. Seuil fixe par construction seulement : contrôles calculés par le harnais, recalcul, rejeu.
- **Question 3.** Prendre les quatre épreuves d'admission de Fable, rangées selon la coupe d'Opus (garantie : verrous 1 et 2a ; vitesse : 2b, 3 et 4). Le devin n'est qu'un détecteur de fuites grossières ; la fermeture se fait par architecture.
- **Question 4.** Prendre le plan F0 à F8 de Fable, en y ajoutant les témoins de certification d'Opus et son monde « dommage hors de la classe, certifié ». Corriger le verdict 5 d'Opus : une forme par construction existe (Kalai et al., p. 3), au prix de l'abstention et d'une borne relative au jumeau.
- **Question 5.** Le registre des écritures de poids de Fable dès maintenant (hygiène, R6). Le rejeu de la recette d'Opus comme cible. Dire « borne haute » pour tout ce qu'on mesure sur des organismes à adaptateur.

**Décisions qui changent.**
1. **Le défaut sous 48 heures de la décision D-1 d'Opus est suspendu.** Elle adopte le cadre de la liberté de l'honnête, avec sa carte des enjeux, et touche ainsi la famille réservée par Fable. Rien de ce qui la concerne ne part avant la vérification par un lecteur isolé et ton mot, comme dans la D-1 de Fable et la D-7 d'Opus.
2. **La D-2 de Fable et la D-2 d'Opus se fondent en une seule décision.** Le lemme D* est re-dérivé par un agent neuf qui ne reçoit que l'énoncé, puis on écrit la carte des taux honnêtes par événement, avec q en clair. Toute entrée dans le texte N-076 est un nœud.
3. **Les listes de voisins à lire en entier se fondent en une seule** : D-7 de Fable plus D-6 d'Opus, soit Kalai, Cui, Miao, Goworek, Zeng, Srivastava, Thomas, Schroeder de Witt, Dwork, Gao, Zhu, Kutasov et Wen. Le verdict d'antériorité sur le rang reste suspendu par la réserve.
4. **Deux nœuds nouveaux, venus d'Opus, à te soumettre** : étendre l'invariant N-053 à toute écriture de poids guidée par un score de moniteur (sa D-5) ; poser la construction de Lampson comme invariant candidat (sa D-3).
5. **L'ordre des tâches floues est commun aux deux** : d'abord l'étape 0 sur processeur, sans le monde F5 ; puis la variante honnête certifiable, sur devis ; l'organisme seulement ensuite. C'est la D-4 de Fable avec l'option (b) de la D-4 d'Opus.
6. **La note d'Opus doit être contre-lue** par un autre modèle avant tout emploi (pièce de travail, mais elle porte deux propositions d'invariant), et ses trois réserves de chiffres (q = 1, double sens de K, rapport 77) doivent être portées par un erratum.

# Cahier de revue de sécurité extérieure — version 1

Modèle : Sonnet 5.5 (`claude-sonnet-5-5`), sous-agent neuf de la lignée conv-audit. Heure : jeudi 29 octobre 2026, 11:37:49 UTC (`date -u`).
Mot de Lazar (12:33 heure de Paris) : « la revue de sécurité extérieure : que faire, comment l'obtenir ? pas avant G0 : go ». Statut : **cahier de travail, niveau méthode, non scellé, rien n'est engagé.** G0 = première porte du programme (fin novembre 2026 au plus tard).

Fichiers lus (empreintes numériques SHA-256, code de contrôle du contenu) :
- `CLAUDE.md` — `a2aabda8a181d46d9723bad44ad352b5e61650634e0f3bc4863451229af00b1b`
- `brouillons/…/question-mere-course-v1/pieces/programme-entretien-vulgarise-v10-v1.pdf` (intégral) — `2aab6b4ca2f164542b406b4972978f0fb0cb60be0826aa6624d23f6068032c70`
- `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-29_n208.md` (intégral) — `7e39069db26bc48a5221c304e9f2cd4099edd4830a3e79c85a3f8a2fc1d6c2ba`
- `registres/decisions.md` (lignes R-474 à R-477 en entier ; R-336, R-339, R-342, R-352, R-376, R-455 en extraits) — `e0e968e99b792aacdf0b856050a594593acce504f98a13c9c34c6ea2eb4958db`
- `registres/etat.md` (une ligne, sur R-597) — `54d7bb738a71b569672deb43af305d9332d42b382057f429c82d2a60771c72b0`

Réserves de lecture : le texte de R-519 et de R-597 n'est pas dans les pièces que j'ai lues ; je ne les connais que par leurs citations (R-519 : « hypothèses violées, jamais de mode » ; R-597 : « aucune recette de contournement » ; R-339 : sortie au niveau de la méthode, jamais la recette). Le lien entre Argon et Gemini n'est pas établi dans mes pièces : à confirmer. Je n'ai lu aucun dossier de mode, aucune branche, aucun contenu.

## 1. Objet et périmètre

**Objet.** Faire relire, par une personne indépendante, le processus du bras d'attaque et ses garanties, avant que quoi que ce soit ne soit exécuté. Le programme gèle « tout passage à une chaîne opérationnelle » jusqu'à cette revue ; elle est une ligne du budget et une porte, pas une formalité. Aujourd'hui : ni relecteur choisi, ni calendrier.

**Le relecteur relit :**
1. le processus du bras d'attaque et ses garanties (instance de conception tierce qui n'a conçu aucun surveillant, N-054 ; scellement ; lecteur unique tenu à l'écart ; interface vers la défense) ;
2. les dossiers scellés par mode sur la branche de quarantaine — **accès complet pour lui seul** (fiche intégrale, paramètres, manifeste, empreintes) ;
3. les sorties de la table de comptes et de classes d'hypothèses violées, avant et après le contrôle lexical ;
4. les textes II des courses (niveau méthode, formulation technique) ;
5. les règles R-519, R-339, R-597, R-750 (et la précision R-476 : au plus trois questions plus étroites après un refus) ;
6. le schéma de scellement et l'index sans contenu sur `main`.

**Le relecteur ne relit pas :** les moniteurs en conception ; `donnees/` hors quarantaine ; les clés et identifiants d'accès.

**Deux revues.** Revue 1 : avant toute chaîne opérationnelle (rien n'est exécuté tant que son rapport n'est pas scellé et que Lazar n'a pas donné son accord). Revue 2 : avant publication du papier qui en parle (relit le texte du papier, ses figures, ses annexes, et ce qui a changé depuis la revue 1).

**Nœud à consigner d'avance (Lazar seul tranche).** Le message n° 208 pose « ni conv-audit, ni session-depot, ni Lazar ne lisent le contenu avant le jour de l'examen ». Le relecteur serait le seul lecteur extérieur au lecteur tenu à l'écart : c'est une exception voulue, il faut l'écrire comme telle dans `registres/decisions.md` avant l'envoi de la lettre, avec le motif (sans cette lecture, la garantie « niveau méthode » n'est pas vérifiée par quelqu'un d'indépendant).

## 2. Questions posées au relecteur (liste fermée)

Le relecteur répond à ces huit questions et à aucune autre ; ses observations hors liste vont dans une section « observations libres », sans feu.
1. **Niveau méthode.** Une fois le dossier lu, chaque mode reste-t-il au niveau de la méthode (classe, mécanisme, conditions, défense) sans devenir une recette (agent concret, séquence d'actions, code, valeurs suffisantes pour rejouer) ?
2. **Lecteur hostile.** Un lecteur hostile et compétent, ayant ce dossier seul, en tirerait-il une recette ? Et ayant le dossier plus les documents publics du programme ? Par mode, avec la raison.
3. **Garanties.** Chacune tient-elle, et est-elle vérifiable par empreinte ou par script, sans croire une déclaration : (3a) instance de conception tierce, distincte du juge et de tout concepteur de moniteur (preuves : manifestes, identifiants exacts des modèles) ; (3b) scellement (rien réécrit, corrections en nouvelle version) ; (3c) lecteur unique tenu à l'écart ; (3d) interface « comptes et classes » seule vers la défense.
4. **Interface.** La table de comptes et de classes peut-elle révéler du contenu par recoupement (classes à effectif très petit, croisement avec l'index, dates) ? Le contrôle lexical suffit-il ?
5. **Retraits.** Quels retraits, généralisations, destructions ou quarantaines supplémentaires faut-il, avant toute exécution, par mode et pour le processus ?
6. **Révélation.** La révélation « au jour de l'examen » est-elle sûre : qui ouvre, dans quel état, avec quel journal, et que devient le dossier après l'examen ?
7. **Fuite vers un tiers.** Quel risque de fuite vers le fournisseur tiers (Argon admis par Lazar ; appels à Gemini d'après la consigne, à confirmer) : le contenu des modes y transite-t-il, y est-il conservé ou réutilisé, et que faut-il faire (contrat, conservation nulle, paramètres du fournisseur, avertissement) ?
8. **Publication.** Quelle publication est admissible : niveau de détail, classes nommables, figures, annexes ; qu'est-ce qui reste interdit ?

## 3. Critères de lecture gelés du rapport

À sceller par Lazar avant l'envoi de la lettre (R1) ; le rapport est lu par un sous-agent neuf qui applique ces critères (R13) ; le relecteur donne ses feux, le sous-agent vérifie seulement la conformité du rapport aux critères.

**Feu par mode (question 1 et 2) :**
- **Vert** : niveau méthode tenu ; le relecteur déclare qu'il ne saurait pas rejouer le mode avec le dossier seul, après avoir essayé de le décrire à un tiers fictif sans en dire plus que le dossier.
- **Orange** : niveau méthode tenu en gros, mais un détail (valeur précise, combinaison de paramètres, variante) rapproche d'une recette ; retrait ou généralisation nommés, vérifiables.
- **Rouge** : recette ou quasi-recette ; ou le relecteur ne peut pas conclure faute de pièce.

**Feu par garantie (question 3, 4, 6, 7) :**
- **Vert** : vérifiée par le relecteur lui-même (empreinte ou script rejoué) ou démontrée par un journal vérifiable.
- **Orange** : tient mais repose sur une déclaration non vérifiable, ou un trou borné et corrigeable.
- **Rouge** : démontrée défaillante, ou non vérifiable et essentielle.

**Ce qui bloque une chaîne opérationnelle :** un mode rouge (ce mode est exclu et retiré selon le relecteur ; la chaîne ne l'utilise pas) ; une garantie rouge, quelle qu'elle soit ; une garantie orange parmi 3a, 3b, 3c, 3d, 6 ou 7 tant que la correction n'est pas vérifiée par le relecteur ; une réponse « recette tirable » à la question 2 ; un rapport sans déclaration d'indépendance ou sans fichiers lus.

**Ce qui est une réserve (ne bloque pas) :** un mode orange dont le retrait est exécuté et vérifié ; une garantie orange parmi les autres ; les observations libres ; toute recommandation de publication plus restreinte que le projet (elle s'applique à la revue 2).

**Blocage de publication (revue 2) :** tout élément que la réponse à la question 8 déclare inadmissible ; un mode rouge ou orange non retiré ; un changement du processus depuis la revue 1 non relu.

Un seul rouge, ou une seule fois « ne peut pas conclure », suffit à geler. Symétrie (R4) : un rapport entièrement vert reçoit le même audit qu'un rapport rouge (le relecteur a-t-il lu tous les dossiers ? ses empreintes concordent-elles avec l'index ?).

## 4. Livrable

- Un **rapport** daté, **scellé** (empreinte numérique et fichier compagnon `.sha256`), signé du relecteur, version dans le nom, jamais écrasé.
- Une **déclaration d'indépendance** : n'a conçu ni moniteur ni mode du programme, aucun lien avec les occupants nommés de la zone, aucun intérêt financier croisé, aucune relation avec le fournisseur tiers qui pose un conflit ; à défaut, la dire.
- La **liste des fichiers lus avec empreintes**, rapprochée de l'index scellé (si une empreinte ne concorde pas, le feu est rouge).
- La **durée** réelle (jours, dates) et les moyens utilisés.
- **Aucune copie** des dossiers hors du poste de revue : lecture en lecture seule, sans réseau sortant, poste fourni ou agréé par Lazar ; pas de photo, pas de note recopiant du contenu ; ses notes sont dans le rapport au niveau méthode.
- **Accord de confidentialité** signé avant l'accès, couvrant le contenu, le rapport et l'existence du poste.
- **Destruction ou restitution** à la fin de chaque revue, constatée par écrit (le relecteur déclare ce qu'il détruit ; le poste est effacé et la date consignée).

**Risques de la revue elle-même (à écrire dans l'accord, sans contenu).**
- Le relecteur devient lui-même un point de fuite : un seul poste, une seule personne, un journal d'accès tenu par Lazar, aucun envoi de message depuis le poste.
- Le rapport peut citer du contenu par inadvertance : il est relu par Lazar ou un sous-agent neuf pour le niveau méthode avant d'être scellé et versé sur `main`.
- Le relecteur peut être sollicité par le programme pour « aider » à corriger un mode : interdit, il juge et ne conçoit pas, sinon il perd son indépendance pour la revue 2.
- Un refus ou une question hors périmètre du relecteur est consigné tel quel ; on ne le contourne pas (R-750).

## 5. Comment l'obtenir

**Profils.**

| Profil | Avantage | Inconvénient |
|---|---|---|
| Chercheur indépendant en sécurité des intelligences artificielles | Rapide, souple, tient dans 7 500 dollars, peut lire seul et en profondeur | Compétence à prouver sans réputation institutionnelle ; poids du rapport vis-à-vis du fonds ; dépendance à une seule personne |
| Organisme d'évaluation ou institut de sécurité | Autorité, procédures de manipulation d'informations dangereuses déjà en place | Lent, peut refuser un petit mandat ou exiger plus cher ; peut vouloir conserver ou réutiliser ce qu'il lit |
| Relecteurs du financeur | Déjà au courant du programme, crédibles pour le fonds | Pas indépendants : ils évaluent notre demande ; mélange de la revue et du financement ; le financeur verrait des dossiers que Lazar lui-même ne voit pas |
| Équipe rouge non commerciale | Habituée à manipuler du contenu adverse sous règles ; regard d'attaquant | Culture de l'exploitation, pas de la divulgation ; risque de reformuler au lieu de relire |

**Où les trouver.** Le réseau du fonds (demander des noms, non pas la relecture par le fonds lui-même) ; les laboratoires académiques de contrôle des intelligences artificielles ; les auteurs d'articles proches, déjà lus, qui n'ont ni concouru ni collaboré au programme. Aucun nom n'est proposé ici : Lazar choisit, la liste restreinte se fait avec ses critères.

**Critères de choix.** Indépendance (n'a conçu ni moniteur ni mode du programme ; aucun conflit avec les occupants nommés de la zone revendiquée) ; expérience de relecture d'informations dangereuses ; disponibilité sur cinq jours ; acceptation du poste contrôlé, de l'accord de confidentialité et de la destruction ; deux candidats au moins, pour qu'un refus ne bloque pas.

**Lettre d'approche** (Lazar envoie ; le contact est un nœud ; envoi seulement après le verdict de G0 ; aucun contenu, aucun nom d'occupant).

*Version française (≈ 130 mots)* — Objet : revue de sécurité extérieure, environ cinq jours, confidentielle.
Bonjour, je dirige un programme de recherche sur le contrôle des intelligences artificielles : savoir d'avance ce que les surveillants automatiques ne peuvent pas voir. Une partie du programme les éprouve avec des scénarios adverses conçus à part, scellés, gardés au niveau de la méthode. Avant toute exécution, je veux une relecture indépendante : ces dossiers restent-ils au niveau de la méthode, et nos garanties de confinement tiennent-elles ? Il s'agirait d'environ cinq jours en deux revues, sur un poste contrôlé, sous accord de confidentialité, rémunérés au taux que vous fixerez. Vous n'auriez conçu aucun surveillant ni scénario de ce programme. Êtes-vous disponible, ou pouvez-vous me suggérer quelqu'un ? Sur votre réponse, je vous envoie le cahier des charges, qui ne contient aucun contenu sensible. Cordialement, Lazar, directeur du programme.

*English version (≈ 120 words)* — Subject: external security review, about five days, confidential.
Hello, I run a research programme on AI control: knowing in advance what automated monitors cannot see. Part of it tests them with adversarial scenarios designed separately, sealed and kept at the level of method. Before anything is executed, I want an independent review: do these files stay at the level of method, and do our containment guarantees hold? This would be about five days in two reviews, on a controlled workstation, under a confidentiality agreement, paid at a rate you set. You would not have designed any monitor or scenario of this programme. Are you available, or could you suggest someone? On your reply I will send the terms of reference, which contain nothing sensitive. Best regards, Lazar, programme director.

**Calendrier** (J = jour où Lazar donne le feu vert après le verdict de G0 ; les dates ne sont pas promises) : avant J, rien ne part ; J à J+14 : lettres, réponses, choix, taux ; J+14 à J+21 : accord de confidentialité, poste, empreintes rapprochées de l'index ; J+21 à J+35 : revue 1 (proposition : trois jours) ; avant toute exécution : rapport scellé, verdict, accord de Lazar ; revue 2 (proposition : deux jours) avant publication du papier. G0 au plus tard fin novembre, report unique possible jusqu'au 31 janvier (R-455) : le calendrier glisse avec lui.

**Budget.** 7 500 dollars, ligne « revue de sécurité extérieure » de l'extension (deux revues, environ cinq jours, taux à fixer) ; soit 1 500 dollars par jour si le taux est uniforme (division de ma part, pas un tarif). Cette ligne est dans une demande de financement non encore accordée : toute dépense se décide sur devis et sur accord écrit de Lazar. La revue 1 peut tomber avant le début du financement (1er décembre) ; qui avance l'argent est un point à trancher.

**Ce que Lazar tranche :** (1) le profil ; (2) la personne ; (3) le taux et le nombre de jours ; (4) la date d'envoi (au plus tôt le verdict de G0) ; (5) l'exception de lecture du §1 ; (6) le poste de revue ; (7) qui avance l'argent avant le 1er décembre.

## 6. Décision

**Décision.** Quel profil de relecteur extérieur approcher en premier pour la revue de sécurité, une fois G0 rendue ?

**Enjeu.** La revue conditionne toute exécution du bras d'attaque et la publication du papier qui en parle ; un relecteur non indépendant, ou un relecteur qui garde ce qu'il lit, vaut moins que pas de revue.

**Options.**
- (a) **Chercheur indépendant sous accord de confidentialité.** Avantage : rapide, dans le budget, lecture profonde. Inconvénient : compétence et autorité à prouver ; une seule personne.
- (b) **Organisme d'évaluation ou institut de sécurité.** Avantage : procédures et crédibilité. Inconvénient : délai, coût possible au-delà de 7 500 dollars, risque de conservation du contenu.
- (c) **Relecteurs du financeur.** Avantage : connaissent le programme. Inconvénient : pas indépendants (ils évaluent la demande) ; le financeur lirait ce que nous-mêmes ne lisons pas.

**Recommandation : (a)**, avec (b) en repli si aucun candidat n'est retenu à J+14, et (c) écartée comme relecteur (le financeur peut seulement indiquer des noms). Confiance : 0,65.

**Défaut sous 48 heures** après remise à Lazar : (a) comme profil de préparation. Le défaut ne vaut ni envoi de lettre, ni choix de personne, ni dépense, ni contact externe : ces points restent des nœuds et attendent le mot de Lazar et le verdict de G0.

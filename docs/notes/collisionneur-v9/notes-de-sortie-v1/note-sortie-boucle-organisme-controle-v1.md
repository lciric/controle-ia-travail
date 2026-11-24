# Boucle entre l'organisme d'idéation et le programme de contrôle : note de sortie du collisionneur, bras principal et bras témoin

- **Date** : 2026-11-24, après 13:23 UTC.
- **Dossiers** : `docs/notes/collisionneurs-reprise-2026-11-24-v1/boucle-organisme-controle/principal/` et `.../temoin/` (branche `runs/collisionneurs-reprise-2026-11-24-v1`).
- **Questions** : bras principal, `question-neutre-collisionneur-boucle-organisme-controle-v2.md` ; bras témoin, `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` (dossier `docs/notes/protocole-x-boucle-organisme-controle-v1/`). Faits : `faits-neutres-boucle-organisme-controle-v2.md`, identiques octet pour octet au `faits.md` des deux bras (vérifié par comparaison).
- **Accords** : GO-2026-11-24-03 et -08 ; plafond de 18 dollars par bras.
- **Dépense** (comptée au pire, `etat.md` de chaque bras) : bras principal 15,99 dollars, dont Opus 1,99, Carbon 2,93, Neon 11,06 ; bras témoin 13,39 dollars, dont Opus 1,68, Carbon 6,86, Neon 4,84. Le gros de la dépense de Neon au bras principal (9,89 dollars) vient de sa réponse du tour III.3 : six essais coupés (deux délais dépassés, quatre refus « forte demande » de Google, code 503, à 0 jeton), comptés au pire, puis un septième essai réussi.
- **Tours** : neuf cellules valides par bras. Trois conceptions à l'aveugle (tour III.1), trois critiques croisées (III.2), trois réponses aux critiques (III.3).
- **Historique** : au bras principal, huit cellules ont été faites de 04:42 à 05:38 UTC. La réponse de Neon a échoué six fois de 05:38 à 09:31, et le dossier a été arrêté comme « faux échec » à 09:32 (`journaux/decisions-reprise.log`). Il a été repris à 13:19 avec une seconde clé Gemini (décision de 12:55, même accord, même plafond) ; la cellule est faite à 13:23. Au bras témoin, une première course à 06:43 n'a laissé aucune cellule. Les neuf cellules ont été faites de 11:04 à 13:18, avec trois relances après coupure (conception de Carbon, critiques de Carbon et de Neon), Neon passant lui aussi par la seconde clé après 12:55.
- **Vérification finale** : bras témoin, « tout tient » (`journaux/verifier-temoin-fille.log`). Bras principal, une anomalie, traitée en réserve ci-dessous (`journaux/verifier-principal-fille.log`).
- **Modèles et lettres** (les mêmes dans les deux bras) : Claude Opus 5.5 = lettre A (réflexion adaptative, toujours active ; effort « high » envoyé par le programme. La « provision de réflexion 0 » des journaux n'est qu'un poste de devis : voir l'erratum 1 de la note sur la cible de publication) ; Carbon (`gemini-4-carbon`) = lettre B (réflexion « high ») ; Neon (`gemini-4-neon`) = lettre C (réflexion « xhigh »).

Rédigé par un lecteur Opus 5.5, classe C, à partir des deux questions, des faits et des dix-huit cellules, lues en entier. **Le lecteur est du même modèle que la lettre A.** Elle est traitée comme les autres, mais le lecteur a pu lui être plus indulgent sans le voir ; plusieurs propositions retenues plus bas viennent d'elle.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout est argument, calcul sous hypothèses ou protocole proposé. Tous les seuils, effectifs, heures de calcul et coûts sont marqués « illustratif » par leurs auteurs. Chaque bras est un seul tirage par modèle : les différences entre bras ne s'attribuent pas avec certitude à la question.

**Comment lire les renvois.** « (A, principal, III.2) » veut dire : Opus, bras principal, tour des critiques croisées. Chaque modèle numérote à sa façon ses chantiers et expériences (E0 à E6, C1 à C5, P1 à P5, E1\* à E4\*), et un même numéro désigne des choses différentes d'une cellule à l'autre. La note nomme chaque expérience par ce qu'elle teste.

**Vocabulaire.** *Référence honnête* : l'échantillon fixe de trajectoires honnêtes sur lequel un détecteur s'étalonne ; sa taille est notée $m$ (les modèles écrivent aussi $N_0$, $N$ ou $N_{\text{cal}}$). *Nul par acte* : une loi de référence construite à chaque action, qui échappe au plafond lié à $m$ que rapportent les faits. *Processus-e* : une accumulation de facteurs d'évidence dont l'espérance sous le nul reste au plus 1, ce qui donne, par l'inégalité de Ville, une garantie de fausses alertes valide à tout instant. *Famille tenue à l'écart* : famille de sabotage inédite, lue une seule fois.

## Réserve sur la conception de Carbon au bras principal

`verifier` signale : « E3-T1-conception-B : 2 essai(s) OK au journal pour une cellule écrite ». Le journal du bras principal (`journal.jsonl`, lignes 3 et 4) contient deux réponses réussies de Carbon à la même invite (empreinte d'invite `6c44ffb9…` pour les deux) :

| Essai | Début, fin (UTC) | Caractères | Empreinte du texte | Fichier |
|---|---|---|---|---|
| 1 | 04:46:58, 04:55:55 | 43 029 | `a0045d41…` | `essais/E3-T1-conception-B.essai1.reponse.md` |
| 2 | 04:52:59, 05:00:09 | 39 639 | `bfd53a70…` | `essais/E3-T1-conception-B.essai2.reponse.md` |

- **Constats.** L'essai 2 a commencé avant la fin de l'essai 1 : les deux envois se chevauchent de trois minutes. Le lecteur ne peut pas en établir la cause. Aucun journal de console de la course initiale ne figure dans `journaux/` ; le premier, `boucle-principal-reprise-1.log`, date d'après. Les deux essais sont comptés dans la dépense (0,68 + 0,66 = 1,33 dollar).
- **La cellule écrite est l'essai 2.** Son empreinte sha256 est identique à celle de `cellules/E3-T1-conception-B.md` (`bfd53a70…`).
- **Les critiques ont lu l'essai 2, preuve à l'appui.** Trois invites contiennent la conception de Carbon : la critique d'Opus (`essais/E3-T2-critique-croisee-A.essai1.prompt.txt`), celle de Neon (`…critique-croisee-C.essai1.prompt.txt`) et la réponse de Carbon lui-même (`…reponse-B.essai1.prompt.txt`). Le lecteur y a cherché le texte exact des deux essais.
  - Le texte intégral de l'essai 2 figure dans chacune des trois. Les 124 lignes longues propres à l'essai 2 y sont toutes.
  - Aucune des 135 lignes longues propres à l'essai 1 n'y figure. Les autres invites ne contiennent ni l'un ni l'autre, ce qui est attendu.
- **Ce qui reste ouvert.** L'essai 1 n'a été servi à personne. Le lecteur ne l'a pas lu et ne dit rien de son contenu.

## 1. Les deux questions, et ce qui les distingue

Les deux bras reçoivent **les mêmes faits** : un programme de contrôle boîte blanche de modèles ouverts d'environ huit milliards de paramètres, avec trois axes (menaces diffuses dans le temps, corruptibilité des moniteurs, essaims à poids partagés) et ses règles. Ces règles sont : la séparation de la sélection et de l'évaluation ; les familles tenues à l'écart, lues une fois ; un plancher d'audit au hasard jugé par un oracle exogène ; un plafond de l'accumulation au-delà de la taille de la référence honnête, sauf nul par acte. Les faits décrivent aussi un organisme d'idéation évalué hors des agents sur des mondes à lois plantées, aujourd'hui en pause. Les deux questions demandent les mêmes sept points, dans le même ordre, avec la même formule de score et les mêmes règles d'intégrité.

Elles diffèrent sur quatre points.

| | Bras principal | Bras témoin |
|---|---|---|
| Cadrage | « Améliorer un organisme d'idéation » pour qu'il produise découvertes, objets mathématiques et protocoles exploitables, « tout en maintenant une boucle de rétroaction rigoureuse » | « On dispose de deux systèmes distincts », qu'on souhaite « relier » pour faire progresser le contrôle |
| Point 3 | **Formaliser mathématiquement** le couplage ; conditions de validité statistique **non circulaire** ; **arbitrage quantitatif** coût des épreuves contre rendement ; validité hors des environnements synthétiques ; contrôles négatifs | « Architecture et risques » : organiser les échanges, risques statistiques, algorithmiques et épistémiques, vérifier qu'un mécanisme n'est pas illusoire |
| Point 4 | **Comparer plusieurs familles d'approches** (principes, hypothèses, limites, modes d'échec) ; protocoles contre la fuite statistique **ou temporelle, notamment avec des modèles pré-entraînés** | « Outils et étanchéité » : outils concrets, validité des mesures |
| Point 7 | **Sensibilité** du classement à la pondération demandée ; expériences pour **les cinq premiers** chantiers ; « ce qui reste hors de portée » | Pas de sensibilité ; expériences pour « chaque action retenue en tête », sans nombre ; « limites qui subsistent » |

Le principal pousse donc vers la formalisation, l'économie de la boucle et la contamination par les modèles pré-entraînés. Le témoin pousse vers l'architecture, les risques et l'étanchéité. Le titre de la question témoin dit « bras témoin neutre » : il a été écrit comme contrôle du cadrage, pas comme une question différente.

## 2. En bref

- **Aucune boucle ne se ferme sur l'évaluation.** C'est l'accord le plus net des six réponses du tour III.3, dans les deux bras.
  - Aucun verdict issu d'une famille tenue à l'écart ne remonte vers l'organisme : ni un score, ni un bit, ni la réécriture d'une consigne par un humain qui a vu le résultat.
  - Ce qui remonte se limite à deux choses : des énoncés formels de verrous et des statistiques de traces honnêtes. Les deux sont figés par empreinte avant la première lecture.
  - Opus le dit le plus franchement : ce sont « deux chaînes ouvertes, et non une boucle de rétroaction » (A, témoin, III.3). Au bras principal, il laisse le choix entre une lecture stricte et une lecture souple de la règle de séparation à l'arbitre (A, principal, III.1 et III.3).
- **L'objet mathématique central est le même partout** : un processus-e à nul par acte, pour échapper au plafond lié à la taille de la référence honnête. Les critiques ont établi deux limites, que leurs auteurs acceptent.
  - Une garantie « valide par construction » ne vaut que sous le nul modélisé, jamais sous la loi réelle des activations (B et C contre A, principal, III.2 ; accepté par A, III.3).
  - Un nul par acte dont l'invariant est estimé sur la référence honnête retrouve un plafond, car tous les actes partagent la même erreur d'estimation (B contre C, principal, III.2 ; accepté par C, III.3 comme « le défaut mathématique majeur » de sa proposition).
- **Avant toute famille tenue à l'écart, mesurer sur traces honnêtes réelles.** Les six réponses finales placent une étape sur traces honnêtes de modèles d'environ huit milliards de paramètres, ou sur processeur, avant de consommer une famille. Elle vérifie que les fausses alertes restent au niveau au-delà de la taille de la référence.
- **Les expériences proposées en premier diffèrent selon le bras.**
  - Au bras principal, ce sont des *prérequis d'instrument* : audit du nul réel (Opus), étanchéité à la mémoire des modèles pré-entraînés (Carbon), filtre amont à deux étages (Neon).
  - Au bras témoin, ce sont des tests de la *raison d'être de l'organisme* : bat-il une archive étendue et le modèle pré-entraîné seul (Opus) ? Ses gains survivent-ils hors des obstructions décrites dans sa consigne (Carbon, Neon) ?
- **Les critiques ont surtout démoli des plans d'expérience.** Hypothèses mal partitionnées, avec des zones grises qui ne réfutent rien. Une seule famille lue, d'où une pseudo-réplication. Des bases handicapées par construction. Des seuils inatteignables aux effectifs proposés. Des contrôles « vrais par construction ». Presque tout a été corrigé au tour III.3.
- **Carbon appose « vérifié » trop vite.** Les critiques l'ont repris dans les deux bras (A, principal, III.2 ; A et C, témoin, III.2). Il a corrigé au tour III.3.

## 3. Ce que chaque modèle a proposé

### Claude Opus 5.5 (lettre A)

**Bras principal.**

- **Gestes d'expert** (A, principal, III.1).
  - « Changer de monnaie » : la ressource rare de la boucle est le nombre de lectures uniques de familles inédites, pas le calcul.
  - Repérer que l'organisme est un *proposeur* : la règle de séparation interdit donc, lue strictement, une partie de la voie de retour.
  - Restreindre la recherche à des processus-e valides par construction.
  - Exiger un nul fort et une politique de double usage.
  - Commencer par la feuille de route, puisque l'organisme est en pause.
- **Formalisation** (A, principal, III.1). Quatre conditions de non-circularité. Notamment un dépôt d'empreinte avant lecture des familles, et un retour limité à un alphabet fini d'issues (échec, neutre, succès), dont le contenu en bits est compté. L'entonnoir passe par cinq étages ; un prix fantôme $\lambda$ est attribué à chaque famille inédite. « Résultat structurel » : à lectures bornées par $R$, augmenter la génération brute n'augmente pas le rendement, borné par $R\rho$, où $\rho$ est la précision du tri.
- **Familles d'approches** (A, principal, III.1). Cinq : prédiction de liens sur graphe daté ; recherche de programmes avec évaluateur exécutable ; génération puis tri par juges génératifs ; plan d'expériences bayésien ; co-évolution attaque et défense. Pour Opus, la recherche de programmes est la seule où la garantie de fausses alertes peut être héritée de la construction.
- **Défauts relevés** (B et C, principal, III.2).
  - « Valide par construction » ne vaut que sous le nul modélisé.
  - Le « résultat structurel » suppose $\rho$ constant ; si l'on envoie les $R$ meilleurs, $\rho$ dépend du volume généré.
  - Sa première expérience de boucle se juge sur les étages mêmes que le retour optimise : elle est circulaire.
  - Sa règle d'envoi calibrée sur les issues passées viole la séparation.
  - Un même réservoir de développement sert à quatre usages.
  - Sa précision à taux de fausses alertes apparié est dégénérée. Neon montre une identité algébrique : à $k$ fixé, apparier le taux de fausses alertes impose la même précision (C, principal, III.2 ; refait par le lecteur).
  - Le lien entre la borne en bits et les bornes de généralisation de Dwork et al. est mal placé : pour des familles fraîches lues une fois, il n'y a pas d'erreur adaptative intra-famille (C).
- **Après les critiques** (A, principal, III.3).
  - Opus accepte presque tout et retire le « résultat structurel », qui devient une hypothèse testée (expérience E6).
  - Il rejette un point : sa règle d'envoi, si elle ne lit que les verdicts finis, reste bornée par le compte de bits, par l'inégalité de traitement des données. Il la supprime pourtant.
  - Nouvelle première expérience : **l'audit du nul réel** (E0). Les bases connues (maximum par action corrigé de Bonferroni, somme cumulée, processus-e conforme sur référence fixe) passent sur des traces honnêtes de deux modèles, jusqu'à plusieurs fois la taille de la référence, sous trois régimes bénins. Le critère : une borne supérieure de confiance sous $\alpha + \varepsilon$. Environ $10^3$ flux par strate sont nécessaires (calcul refait par le lecteur : 1 017 en unilatéral, 1 248 en bilatéral). Aucune famille n'est consommée, et l'organisme n'est pas modifié.
  - Six réservoirs disjoints : calibrage, test honnête, retour, évaluation, épreuve, banque finale.
  - Le transfert du substitut sur processeur vers les vrais modèles se juge **dans la queue sélectionnée**, par une différence $\Delta_{\text{top}}$, et non par une corrélation de rang globale.
  - Une suite de confiance à deux frontières borne la zone grise.

**Bras témoin.**

- **Analyse** (A, témoin, III.1). « La génération est bon marché ; le goulot est le signal d'évaluation. » Le tri de l'organisme par modèles pré-entraînés est lui-même un juge génératif, exposé à la pression rhétorique de l'axe 2.
- **Architecture** (A, témoin, III.1). Des « cartes-problèmes » typées descendent du contrôle vers l'organisme. Des mondes-contrôle à lois plantées servent de banc interne. Les propositions remontent gelées. En retour, un bit par lot, dans l'esprit de « The Ladder ». Par défaut, Opus le tient pour interdit.
- **Expériences** (A, témoin, III.1). Quatre :
  - l'organisme guidé par les cartes bat-il l'archive ?
  - un nul par acte dépasse-t-il le plafond, contre une base que propose Opus : e-valeurs conformes contre $k$ rééchantillonnages honnêtes de chaque acte ?
  - des canaris prouvent-ils l'étanchéité ?
  - le substitut prédit-il le gain sur carte graphique ?
- **Défauts relevés** (B et C, témoin, III.2).
  - Le bit de retour reste une fonction des scores des moniteurs, et « The Ladder » protège une même réserve réutilisée, non des familles successives (B, C).
  - Son critère « aucun gain sur une loi déjà archivée » confond loi archivée et statistique optimale (B, C).
  - Un canari lexical ne voit qu'une copie littérale (B, C).
  - Inclure des candidats mal classés gonfle la corrélation de Spearman par mélange (B, C).
  - Un agent honnête porteur d'une consigne privée bénigne n'est pas échangeable avec la référence (B). Opus répond : « je ne l'avais pas vu ».
  - Apparier la longueur des traces crée un biais de collisionneur (C).
- **Après les critiques** (A, témoin, III.3).
  - Le bit est supprimé et la citation de « The Ladder » retirée. Les cartes de tous les cycles sont gelées avant la première lecture. Le canal humain résiduel est journalisé, non borné.
  - Un « plafond oracle » sert de contrôle de sanité.
  - Opus distingue une **récupération utile** d'une méthode connue mais oubliée d'une **découverte** : il tient deux comptes séparés.
  - Les canaris sont testés canal par canal (lexical, géométrique, paramétrique). L'étanchéité repose d'abord sur un audit de provenance vérifié par un tiers.
  - Il rejette trois critiques. La malédiction du vainqueur disparaît si les mondes d'épreuve sont tirés indépendamment. La contrainte sur le nombre de permutations ne joue que pour trois candidats ou moins. La limite informationnelle d'une alternative très faible vaut pour toute procédure.
  - Première expérience : organisme complet contre archive étendue par un tiers, puis contre le modèle pré-entraîné seul, sur des mondes écrits par une instance aveugle aux cartes.

### Carbon (identifiant gemini-4-carbon, lettre B)

**Bras principal.**

- **Présupposés et gestes** (B, principal, III.1). Cinq présupposés. Carbon propose une « diode de tenseurs honnêtes » : extraire une fois des activations de trajectoires honnêtes seulement, puis faire travailler l'organisme sur processeur. Il exige des preuves vérifiées mécaniquement pour la validité sous le nul.
- **Formalisation** (B, principal, III.1).
  - Le candidat est un triplet : statistique, certificat de validité, politique d'audit.
  - Survie au plancher d'audit : $\prod_j(1-\gamma p_{s_j})$.
  - Le filtre amont n'est rentable que si son rapport de vraisemblance diagnostique dépasse un seuil qui dépend d'une fonction $\kappa$, jamais définie.
  - Validité hors synthétique par un « morphisme » de blanchiment spectral.
- **Familles d'approches** (B, principal, III.1). Synthèse neuro-symbolique sous assistant de preuve ; transport structurel sur graphes datés ; jumeau spectral des activations sur processeur ; invariants géométriques sur traces honnêtes.
- **Classement** (B, principal, III.1). En tête : la décontamination des modèles pré-entraînés par anonymisation (bijection des symboles, rotation orthogonale secrète des activations). Puis le jumeau spectral, puis la synthèse de processus-e.
- **Défauts relevés** (A et C, principal, III.2).
  - Statuts mal attribués. Des jeux à constituer sont marqués « rapporté ». Un plafond chiffré, $1/(m+1)$, est attribué aux faits, qui ne le chiffrent pas. Un « si et seulement si » est donné sans preuve (A).
  - La non-circularité est posée sur la réalisation d'une famille, non sur le processus de conception commun (A).
  - La rotation orthogonale laisse les statistiques spectrales invariantes et détruit les coordonnées privilégiées des activations (A, C).
  - Le substitut et l'évaluation sur carte graphique reposent sur le même substrat (A).
  - La base à référence fixe est handicapée par construction, avec 30 trajectoires (A, C).
  - Les variations de style sont conditionnées sur l'échec du juge : malédiction du gagnant (A).
  - Le chantier des essaims a une partition d'hypothèses non exhaustive (A).
  - Neon donne une identité : avec un quart des candidats promus, le rapport exigé (4) n'est atteignable qu'avec un taux de détection du filtre d'au moins $1/(1+3q_0)$, hors d'atteinte si les bons candidats sont rares (C, principal, III.2 ; refait par le lecteur).
  - Un assistant de preuve ne certifie que l'implication interne au modèle du nul (C).
- **Après les critiques** (B, principal, III.3).
  - Carbon accepte presque tout.
  - La rotation orthogonale est remplacée par une **permutation signée secrète** des coordonnées, qui préserve normes et parcimonie. La perte entre les deux devient un test.
  - Le rapport diagnostique est remplacé par un facteur d'enrichissement. Condition suffisante de rentabilité du filtre : $\text{VPP}/q_0 > R_0/R$ (calcul refait par le lecteur ; c'est une condition suffisante, pas nécessaire).
  - Facteurs de pari tronqués dans $[1/2, 3/2]$.
  - Survie au plancher d'audit sous aveuglement corrélé de l'oracle : $1 - p_\bullet(s)(1-(1-\gamma)^m)$, où $p_\bullet$ est la détectabilité du sous-type le plus difficile. La borne plafonne à $1-p_\bullet$ (refait par le lecteur sous le modèle posé).
  - Modèle de tri d'une lignée distincte des modèles surveillés.
  - Il rejette deux critiques. Les théorèmes postérieurs à la date de coupure du graphe mais antérieurs à celle du modèle étaient choisis exprès, pour exposer l'anonymisation. Une famille unique suffit à **réfuter** une hypothèse universelle, même si elle ne permet pas d'estimer la variance entre familles.
  - Première expérience : un plan 2 × 2 sur processeur, lois historiques anonymisées contre lois synthétiques inédites, croisées avec la présence ou l'absence du modèle pré-entraîné. Il mesure un gain structurel et une fuite de mémoire.

**Bras témoin.**

- **Architecture** (B, témoin, III.1). « Diode épistémique » à trois zones : idéation sur processeur ; sas de mondes à lois de contrôle plantées sur processeur ; épreuve sur carte graphique. Seuls remontent les moments statistiques qui ont mis en défaut le nul sur traces honnêtes.
- **Outils** (B, témoin, III.1).
  - Processus-e par échangeabilité locale (micro-permutations de prémisses).
  - Projection « quotient » contre le style.
  - Spectre résiduel entre copies et riposte à hasard borné.
  - Estimateur de Horvitz-Thompson corrigé de l'oracle.
  - Filtre de non-redondance par corrélation de Spearman.
- **Défauts relevés** (A et C, témoin, III.2).
  - Erreur de calcul : une espérance des facteurs supérieure à 1 n'entraîne pas « presque 100 % » de fausses alertes. C'est l'espérance du logarithme qui décide. Opus donne un contre-exemple, refait par le lecteur : $e_t\in\{0;\,2{,}01\}$, $\lambda=0{,}5$, espérance 1,005, espérance du logarithme $\approx -0{,}14$ (A, C).
  - Le rapport de vraisemblance de Wald figure dans l'archive et est optimal sur un monde planté connu : le seuil de gain dépend de ce qu'on laisse savoir aux bases (A).
  - La boucle de retour honnête est conditionnée par les candidats (A).
  - La projection « quotient » utilise une « variance inter-intentions » : soit elle lit des étiquettes de sabotage, soit elle ne sert à rien (C).
  - La compression aléatoire de 4 096 à 256 dimensions divise par 16 le rapport signal sur bruit d'une direction faible (A, C ; refait par le lecteur en bruit isotrope).
  - Le masquage causal brise l'échangeabilité des micro-permutations (C).
  - L'estimateur de Horvitz-Thompson est biaisé par $1/\hat p$ (A, C).
  - Le filtre de Spearman écarte de bons détecteurs (A, C).
- **Après les critiques** (B, témoin, III.3).
  - Carbon accepte presque tout et intègre l'expérience proposée par Opus.
  - Quatre banques honnêtes disjointes.
  - Activations complètes stockées, environ 1,6 gigaoctet (refait par le lecteur).
  - Garde éliminatoire sur une banque honnête fraîche.
  - Riposte à confidentialité différentielle, avec un seuil secret retiré à chaque épisode.
  - Il rejette deux critiques. Le contrôle des fausses alertes en zone 2 n'est pas tautologique : l'organisme ne reçoit pas la loi exacte du simulateur. Une **randomisation active** de l'ordre d'entrées commutatives, tirée par le défenseur, rend les activations exactement échangeables sous le nul, malgré le masquage causal.
  - Première expérience : fécondité de l'organisme sur des obstructions générées à l'aveugle de son cahier des charges, contre archive, organisme placebo sur graphe recâblé et cahier-leurre.

### Neon (identifiant gemini-4-neon, lettre C)

**Bras principal.**

- **Présupposés** (C, principal, III.1). Six présupposés. Il en ajoute un : rien ne dit que le goulot du contrôle soit un manque d'objets mathématiques, plutôt que la variance des sondes ou l'oracle.
- **Architecture** (C, principal, III.1).
  - Pare-feu à sens unique : le contrôle ne transmet que des spécifications formelles et des statistiques de traces honnêtes.
  - L'organisme ne promeut qu'un candidat filtré sur processeur par tour.
  - Budget d'erreur réparti par « α-investissement ».
  - Borne lipschitzienne de transfert.
  - Valeur prédictive positive du filtre : diviser par 10 ses fausses promotions vaudrait mieux que multiplier par 10 la production d'idées.
- **Familles d'approches** (C, principal, III.1). Cinq : synthèse de programmes vérifiée formellement ; analogies sur graphes datés ; co-évolution abstraite ; plan d'expériences bayésien ; invariants sur activations honnêtes. Il propose de combiner la première et la dernière.
- **Défauts relevés** (A et B, principal, III.2).
  - Un invariant estimé sur $m$ trajectoires réintroduit le plafond. B donne un ordre de grandeur, $T \gtrsim m/d_{\text{eff}}$, non refait par le lecteur.
  - L'α-investissement fait dépendre les seuils des rejets passés, donc rompt l'étanchéité (B).
  - Le filtre laisse passer les martingales valides mais sans puissance, comme la constante 1 (B).
  - Le banc du filtre est construit par l'auteur du filtre (A, B).
  - Le placebo de spécification ne teste pas le couplage (A).
  - La mémoire est confondue avec la « naturalité » des lois (A).
  - La règle « deux familles sur trois » est non jugeable : 0,5 sous égalité (A) ; 10/64 avec quatre bras (B). Les deux sont refaits par le lecteur.
  - La borne lipschitzienne est intestable (A, B).
  - Le budget de calcul est asymétrique entre le bras avec modèle pré-entraîné et le bras sans (B).
- **Après les critiques** (C, principal, III.3).
  - Neon accepte l'essentiel. Il distingue désormais deux sortes de nuls par acte. Seuls ceux **sans estimation** sur la référence échappent au plafond : symétrie ou randomisation en ligne, symétrie entre copies.
  - Allocation fixe $\alpha/K$.
  - **Filtre à deux étages** : validité, puis puissance minimale et déduplication.
  - Plan 2 × 2 pour la mémoire.
  - Il rejette deux critiques.
    - Le « faux dilemme » entre boucle statique et fuite : selon lui, une boucle fermée honnête existe, entre l'organisme et les échecs du nul sur traces honnêtes de calibrage, avant gel.
    - Retirer la base à référence fixe : il la garde comme témoin positif du régime de plafond.
  - Première expérience : le filtre à deux étages, sur un banc conçu à l'aveugle, sur processeur seul.

**Bras témoin.**

- **Analyse** (C, témoin, III.1). Neon pointe un levier « sous-estimé » : l'essentiel des mécanismes illusoires se réfute **sur données honnêtes seules**, sans consommer de famille. La nature ne contourne pas l'instrument ; le sabotage, si.
- **Architecture** (C, témoin, III.1). « Fiches d'obstruction formelle » et géométrie honnête vers l'organisme. Cinq sas, du moins coûteux au plus irréversible : anti-renommage ; tests de résistance ; mondes-miroirs adverses ; traces honnêtes de modèles réels ; lecture unique. Un témoin « modèle pré-entraîné seul » est prévu. Le corpus amont est rééquilibré vers l'inférence séquentielle et les jeux d'inspection.
- **Défauts relevés** (A et B, témoin, III.2).
  - Fuite par spécification : les fiches décrivent ce que les mondes-miroirs instancient (A). Opus en tire une expérience à fiches vraies, fiches-leurres et obstructions non décrites.
  - Le test de validité récompense la prudence. À 200 trajectoires, un détecteur exactement au niveau échoue ou tombe en zone grise environ deux fois sur trois (A).
    - Refait par le lecteur en exact : la borne de Clopper-Pearson unilatérale reste sous 0,07 jusqu'à 7 alertes. La probabilité d'en avoir au plus 7 est de 0,21. La conclusion d'Opus est donc plutôt sous-estimée.
  - Le post-mortem après lecture est une analyse adaptative (B).
  - Exposer à l'organisme les taux d'identification de l'oracle par strate lui montre où frapper (B).
  - Le filtre anti-renommage rejette les extensions qui coïncident avec la somme cumulée sur horizon court (B).
  - Zones grises dans les quatre expériences (A, B).
  - Un plancher d'audit déjà fort rend vide un gain absolu exigé (B).
- **Après les critiques** (C, témoin, III.3).
  - Neon accepte presque tout.
  - Trois jeux honnêtes disjoints.
  - Post-mortem supprimé, taux de l'oracle masqués.
  - Covariance rétrécie et queues lourdes dans les mondes-miroirs.
  - Procédure e-BH et tirage de confirmation.
  - Seuil unique par test.
  - Gain exprimé en réduction relative des sabotages manqués.
  - Il rejette deux critiques. L'expérience d'Opus garde une zone grise et un rapport instable, et Neon la transforme. L'optimalité de Neyman-Pearson ne vaut que pour une alternative simple connue, donc pas pour des familles inédites.
  - Première expérience : fiches vraies contre fiches-leurres sur dix obstructions conçues à l'aveugle des fiches, en plan 2 × 2 avec le corpus. Elle utilise un test exact de permutation entre familles.

## 4. Ce que la différence de question change, et ce qu'elle ne change pas

**Ce qui ne change pas.** Ces points apparaissent dans les deux bras, chez les trois modèles. Ils sont donc robustes au cadrage, au moins sur ces deux tirages.

- La règle de séparation interdit la boucle fermée sur l'évaluation. Le retour se réduit à des énoncés formels et à des statistiques honnêtes, gelés avant lecture.
- Le processus-e à nul par acte est l'objet mathématique visé pour l'axe 1.
- Le transfert du processeur aux vrais modèles est à mesurer, jamais à supposer.
- La validité des fausses alertes se vérifie sur traces honnêtes avant de consommer une famille.
- Une famille unique ne permet pas d'estimer la variance entre familles (pseudo-réplication).
- Le plancher d'audit souffre de l'inégalité de Jensen. Une moyenne de strate sous-estime la survie d'un sabotage qui vise les dommages difficiles. Il faut une borne par sous-type.
- La lignée commune entre l'organisme, le concepteur des familles et le modèle surveillé est un risque.
- Les ancrages matériels sont les mêmes : Llama-3.1-8B-Instruct et Qwen2.5-7B-Instruct, une carte de 24 à 48 gigaoctets.
- Les trois modèles disent « je ne sais pas » sur le nombre de familles inédites disponibles.

**Ce qui change.** Les écarts suivent la lettre des questions.

1. **Formalisation et économie.** Seul le principal en produit. On y trouve des filtrations, des comptes de bits, un prix fantôme des familles, des entonnoirs bayésiens et des conditions de rentabilité du filtre amont (A, B, C, principal, III.1). Les critiques du principal ont consacré une grande part de leurs efforts à ces formules, et en ont réfuté plusieurs : le « résultat structurel » d'Opus, la fonction $\kappa$ et le rapport diagnostique de Carbon, la borne lipschitzienne de Neon. Le témoin n'a presque pas de formule d'arbitrage. Ses critiques portent davantage sur l'architecture et la puissance des tests.
2. **Mémoire des modèles pré-entraînés.** Le principal la demande explicitement au point 4. Chaque modèle y bâtit une expérience dédiée : anonymisation 2 × 2 chez Carbon, mémoire contre « naturalité » chez Neon, rétrodiction intra-modèle chez Opus. Au témoin, le même risque se transforme en question d'**apport propre** : l'organisme fait-il mieux que le modèle pré-entraîné seul (A, témoin, III.3 ; C, témoin, III.1 et III.3) ? Cette formulation est plus directe pour décider si l'organisme vaut d'être relancé.
3. **Ce qui passe en premier.** Le principal ouvre par des prérequis d'instrument : nul réel, étanchéité à la mémoire, filtre. Le témoin ouvre par la valeur ajoutée de l'organisme et la fuite par spécification. Le lecteur y voit l'effet probable du cadrage : « améliorer l'organisme » d'un côté, « relier deux systèmes » de l'autre. Il ne peut pas l'établir avec un tirage par cellule.
4. **Contrôles nés dans un seul bras.**
   - Au témoin seulement : l'agent honnête porteur d'une consigne privée bénigne (B, témoin, III.2, adopté par A et C) ; la fuite par spécification et les fiches-leurres (A, témoin, III.2, adoptées par B et C) ; la randomisation active des entrées par le défenseur (B, témoin, III.3) ; la distinction entre récupération utile et découverte (A, témoin, III.3).
   - Au principal seulement : la permutation signée au lieu de la rotation (B, principal, III.3) ; le transfert jugé dans la queue sélectionnée (A, principal, III.3) ; la survie sous oracle corrélé (B, principal, III.3) ; le filtre à deux étages (C, principal, III.3).
   - Rien n'empêche de transposer chacun de ces contrôles à l'autre bras.
5. **Sensibilité et nombre d'expériences.** Seul le principal analyse la sensibilité du classement. Le résultat commun : les chantiers sur processeur dominent dans toutes les variantes, et la formule multiplicative ne vaut qu'à un rang près (A, principal, III.1). Opus ajoute qu'elle ignore les dépendances entre expériences (A, principal, III.3). Au témoin, Opus et Neon ne proposent que quatre expériences ; Carbon, cinq.

**Une remarque croisée, faite par le lecteur.** Au témoin, Opus objecte à la boucle honnête de Carbon qu'un canal qui renvoie « les moments qui ont mis en défaut le nul » est conditionné par les candidats : c'est une analyse adaptative sur la référence honnête (A, témoin, III.2). Carbon l'accepte et fige un résumé non adaptatif (B, témoin, III.3). Au principal, Neon défend une « boucle fermée honnête » de même forme, qui itère sur les échecs du nul observés sur les traces de calibrage (C, principal, III.3). Personne au principal ne lui a fait l'objection, puisque la proposition date du dernier tour. Elle s'applique, au moins en partie, et demande la même parade : résumé figé, ou jeu honnête frais pour l'évaluation.

## 5. Accords et désaccords

### Accords nés des critiques

- **Réservoirs honnêtes disjoints**, pour le calibrage, le filtre, l'évaluation et le retour (A, B, C, dans les deux bras, III.3).
- **Un seul seuil par test, sans zone grise.** Ou bien une zone grise bornée par dimensionnement, dont l'apparition réfute l'hypothèse de variance préenregistrée (A, principal, III.3).
- **Bases dotées des mêmes ressources** : même volume de données honnêtes, même budget de réglage, nul par acte standard compris (A, B, C, principal, III.3 ; A, témoin, III.3).
- **Contrôle par objets dégénérés** : un générateur de martingales valides mais sans puissance doit perdre (A et C, principal, III.3 ; B, témoin, III.3).
- **Placebo de graphe** par recâblage qui préserve degrés et dates, plutôt qu'une permutation naïve (B et C, témoin, III.3).
- **Taux d'identification de l'oracle par sous-type de dommage**, avec une borne de la queue basse (B et C, principal, III.3 ; B et C, témoin, III.3).

### Calculs refaits et calculs non refaits

Refaits par le lecteur, à la main ou par un court calcul exact sur processeur :

- précision à $k$ fixé et taux de fausses alertes apparié : identité dégénérée (C, principal, III.2) ;
- seuil de taux de détection $\Lambda^*\gamma_u/(1+q_0(\Lambda^*-1))$ pour le rapport diagnostique du filtre (C, principal, III.2) ;
- 10/64 sous quatre bras et trois familles ; 0,5 pour « deux sur trois » à deux bras ; plus petite valeur $p$ d'un test des signes sur trois familles, 0,125 (B et A, principal, III.2) ;
- condition suffisante $\text{VPP}/q_0 > R_0/R$ et borne de survie sous oracle corrélé (B, principal, III.3) ;
- dimensionnement d'environ $10^3$ flux pour l'audit du nul (A, principal, III.3) ;
- contre-exemple sur l'espérance du logarithme ; divergence de Kullback-Leibler cumulée $\delta^2/2$ pour une dérive en $\delta/\sqrt T$ (A, témoin, III.2) ;
- borne normale 0,080 à 200 trajectoires (B, témoin, III.2) ; seuil exact à 7 alertes et probabilité 0,21 (voir section 3) ;
- seuil de 63 alertes sur 1 000. En exact, 2,8 % d'élimination à tort au niveau 0,05 et 2,4 % d'acceptation à tort à 0,08 ; Neon annonçait 2,5 % et 2,7 % (C, témoin, III.3). L'écart est sans conséquence ;
- « au plus 21 alertes sur 600 » pour une borne sous 0,05 (B, principal, III.3) : c'est à la limite. À 21 alertes, la borne exacte de Clopper-Pearson vaut à peine plus de 0,05 ; il faut 20 au plus pour une inégalité stricte ;
- $T \geq 1{,}54$ pour $\alpha=0{,}01$ et $k=19$ (A, témoin, III.3) ; mémoire des poids et stockage des activations (A, principal ; B, témoin).

Non refaits :

- les bornes de Bretagnolle-Huber et de Fieller (B, principal, III.2) ;
- l'ordre $m/d_{\text{eff}}$ du plafond retrouvé par un invariant estimé (B, principal, III.2), pourtant central ;
- la fuite « sous 0,002 bit » de la riposte à confidentialité différentielle (B, témoin, III.3) ;
- la transition spectrale de Baik, Ben Arous et Péché appliquée aux essaims (A et C, témoin, III.2) ;
- les puissances des tests de McNemar et de permutation proposés au tour III.3.

### Désaccords

- **Quelle première expérience.**
  - Au principal : audit du nul réel sur traces honnêtes (A), étanchéité à la mémoire (B), filtre à deux étages (C).
  - Au témoin : organisme contre archive étendue et contre modèle seul (A), fécondité hors cahier des charges (B), fiches vraies contre fiches-leurres (C).
  - Les six sont sans famille consommée ; cinq sont sur processeur seul. L'audit du nul d'Opus demande des dizaines d'heures de carte graphique (illustratif).
- **Lecture de la règle de séparation.** Opus laisse ouverte une lecture souple, où un verdict fini sur un *protocole* serait licite (A, principal, III.1 et III.3), puis la ferme au témoin (A, témoin, III.3). Neon défend une boucle fermée sur les seules données honnêtes (C, principal, III.3). Carbon fige un résumé honnête non adaptatif (B, témoin, III.3).
- **Priorité du filtre amont.** Neon maintient que la sélectivité du filtre est le levier prioritaire (C, principal, III.3). Opus a retiré sa thèse voisine, « le tri prime sur la production », pour en faire une hypothèse à tester (A, principal, III.3).
- **Une famille suffit-elle ?** Pour réfuter une hypothèse universelle, oui (B, principal, III.3). Pour généraliser, non (A, B, C). Neon exige cinq familles pour juger la boucle (C, principal, III.3), et déclare sinon la question non jugeable.
- **Valeur du contrôle sur mondes simulés.** Tautologique, pour Opus : on y connaît le nul (A, témoin, III.2). Non, répond Carbon : l'organisme n'y connaît pas la loi exacte (B, témoin, III.3).
- **Coûts.** De 10 euros (B, principal, III.3) à 700–1 800 euros plus cinq familles consommées (C, principal, III.3), pour des plans qui ne sont pas comparables. Tous illustratifs.

## 6. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Personne n'a cherché l'antériorité. Les éléments suivants pourraient être propres au dossier, sous réserve d'une recherche bibliographique :

- la lecture unique comme monnaie de la boucle, avec un prix fantôme par famille (A, principal, III.1) ;
- le transfert jugé dans la queue sélectionnée plutôt que par corrélation globale (A, principal, III.3) ;
- la distinction entre nul par acte sans estimation et nul à invariant estimé, qui retrouve un plafond (B contre C, principal, III.2 ; C, principal, III.3). Elle précise le fait rapporté sur le plafond ;
- la permutation signée secrète des coordonnées, comme compromis entre secret et coordonnées privilégiées (B, principal, III.3) ;
- la randomisation active, par le défenseur, de l'ordre d'entrées commutatives, qui rend l'échangeabilité exacte sous le nul (B, témoin, III.3) ;
- l'agent honnête porteur d'une consigne privée bénigne comme contrôle des sondes (B, témoin, III.2) ;
- la fuite par spécification, et son expérience à fiches vraies, fiches-leurres et obstructions non décrites (A, témoin, III.2 ; C, témoin, III.3) ;
- la séparation entre récupération utile et découverte (A, témoin, III.3) ;
- la borne de survie au plancher d'audit sous aveuglement corrélé de l'oracle (B, principal, III.3).

### Fragile

- **Rien n'est mesuré.** Toutes les expériences sont des plans. Aucun modèle ne sait combien de familles inédites existent, ni quelle est la taille de la référence honnête.
- **Les statuts « vérifié » de Carbon.** Il les a appliqués à des énoncés non établis : le plafond chiffré attribué aux faits, la fonction $\kappa$, la croissance $(1+\varepsilon)^T$. Les critiques l'ont repris et il a corrigé. Plusieurs calculs encore marqués « vérifié » n'ont été refaits par personne.
- **Les propositions du tour III.3 n'ont pas été critiquées.** Cela vaut pour la boucle honnête de Neon (voir la remarque croisée en section 4), la riposte à confidentialité différentielle de Carbon, la randomisation active, $\Delta_{\text{top}}$, et l'expérience E6 d'Opus.
- **Les dates de coupure des modèles pré-entraînés** sont des déclarations des fournisseurs, invérifiables (A, principal, III.3). Les expériences sur la mémoire en dépendent.
- **La pause de l'organisme.** Plusieurs premières expériences demandent de faire tourner l'organisme existant, sans le modifier, sur de nouveaux mondes ou contre de nouveaux bras. Le lecteur ne sait pas si c'est compatible avec la pause rapportée.
- **Le lecteur est du même modèle qu'Opus**, dont plusieurs propositions sont retenues ci-dessous.

## 7. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois titres, auteurs ou années. **À vérifier sur PDF** avant toute citation.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis », *Science* | A, B, C (deux bras) | Analyse adaptative ; portée contestée (C, principal, III.2) |
| Blum, Hardt (2015), « The Ladder: A Reliable Leaderboard for Machine Learning Competitions » | A (principal, III.1 ; témoin, III.1, retirée au III.3) | Bit de retour ; hors domaine selon B et C |
| Ville (1939), *Étude critique de la notion de collectif* | A, B, C | Garantie valide à tout instant |
| Ramdas, Grünwald, Vovk, Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science* | A, B, C (deux bras) | Processus-e |
| Shafer, Shen, Vereshchagin, Vovk (2011), « Test martingales, Bayes factors and p-values » | A (témoin) | Martingales de test |
| Vovk, Wang (2021), « E-values: Calibration, combination and applications », *Annals of Statistics* | C (principal) | e-valeurs |
| Howard, Ramdas, McAuliffe, Sekhon (2021), « Time-uniform, nonparametric, nonasymptotic confidence sequences » | A (principal, III.3) | Suites de confiance à deux frontières |
| Wang, Ramdas (2022), « False discovery rate control with e-values », *JRSS-B* | A (deux bras), B (témoin, III.2), C (témoin, III.3) | Procédure e-BH |
| Benjamini, Hochberg (1995) ; Benjamini, Yekutieli (2001) | C (témoin), B (témoin, III.2) | Taux de fausses découvertes sous dépendance |
| Foster, Stine (2008), « α-investing… », *JRSS-B* | C (principal) | Budget d'erreur séquentiel ; retiré |
| Bates, Candès, Lei, Romano, Sesia (2023), « Testing for outliers with conformal p-values », *Annals of Statistics* | C (principal, III.1), B (principal, III.2) | Granularité $1/(m+1)$ |
| Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* | A, C (témoin) | Prédiction conforme |
| Neyman, Pearson (1933) ; Wald, Wolfowitz (1948) ; Wald (1945) ; Page (1954) | A, B, C (témoin) | Optimalité ; bases d'archive |
| Clopper, Pearson (1934), *Biometrika* | C (principal, III.3) | Intervalles exacts |
| Horvitz, Thompson (1952) | B (témoin) | Audit pondéré |
| Marchenko, Pastur (1967) ; Ledoit, Wolf (2004) ; Baik, Ben Arous, Péché (2005) | B, C (deux bras) | Covariance en grande dimension ; seuil spectral |
| Dwork, Roth (2014), *The Algorithmic Foundations of Differential Privacy* | B (témoin, III.3) | Riposte confidentielle |
| Elhage et al. (2022), « Toy Models of Superposition » | B (principal) | Géométrie des activations |
| Hewitt, Liang (2019), « Designing and Interpreting Probes with Control Tasks » ; Alain, Bengio (2016), « Understanding intermediate layers using linear classifier probes » | A (principal ; témoin), B (témoin) | Sondes |
| Zheng et al. (2023), « Judging LLM-as-a-judge with MT-Bench and Chatbot Arena » | A (principal) | Biais des juges |
| Si, Yang, Hashimoto (2024), « Can LLMs Generate Novel Research Ideas? » | A (deux bras) | Nouveauté jugée par des experts |
| Lu et al. (2024), « The AI Scientist » ; Romera-Paredes et al. (2023), « Mathematical discoveries from program search with large language models », *Nature* | A ; A et C (principal) | Idéation automatisée ; recherche de programmes |
| Swanson (1986) ; Tshitoyan et al. (2019) ; Krenn, Zeilinger (2020) | A (principal) | Découverte par la littérature |
| Golchin, Surdeanu (2023), « Time Travel in LLMs » (attribution marquée à vérifier) | A (principal) | Contamination temporelle |
| Manheim, Garrabrant (2018), « Categorizing Variants of Goodhart's Law » | A (témoin) | Goodhart |
| Platt (1964), « Strong Inference », *Science* | A, C (deux bras) | Inférence forte |
| « AI Control: Improving Safety Despite Intentional Subversion » (auteurs et année marqués à vérifier) | B (témoin) | Évaluation adverse en contrôle |
| Miller-Madow, Fieller, Gleser-Hwang, Bretagnolle-Huber (résultats nommés sans référence) | B, C (principal, III.2) | Biais et non-jugeabilité |
| Modèles et outils : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, Mistral-Nemo-12B, Lean 4 | A, B, C | Ancrage ; versions, licences et dates de coupure à vérifier |

## 8. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, et si possible des deux bras ; résistance aux critiques ; coût ; réversibilité ; ce que la proposition tranche pour la suite. Rappel du dépôt : toute dépense de calcul, toute modification de l'organisme et toute lecture de la règle de séparation sont des décisions de Lazar. Rien de ce qui suit n'est engagé.

### Retenues

1. **Fixer par écrit que le retour du contrôle vers l'organisme ne porte aucun verdict de lecture.**
   - *Contenu.* Ni score, ni bit, ni réécriture humaine après lecture. Le retour se limite à des énoncés formels de verrous et à des statistiques de traces honnêtes, figés par empreinte avant la première lecture. Les taux d'identification de l'oracle restent masqués à l'organisme. Le canal humain entre cycles est journalisé.
   - *Soutien.* Les trois modèles des deux bras au tour III.3 ; la question reste explicitement ouverte chez Opus au principal.
   - *Pourquoi.* Toute l'architecture en dépend, et c'est une lecture de la règle, non une expérience. À trancher par Lazar.
2. **Auditer d'abord le nul réel sur traces honnêtes, sans organisme et sans famille consommée.**
   - *Contenu.* Les bases connues (maximum par action, somme cumulée, processus-e conforme sur référence fixe, nul par acte disponible) passent sur deux modèles ouverts, sur des flux plus longs que la référence. Régimes bénins : changement de sous-tâche, contexte long, ton rhétorique, consigne privée bénigne. On contrôle aussi la dérive de l'espérance du logarithme. Dimensionnement d'environ $10^3$ flux par strate. On vérifie que le plafond rapporté se reproduit.
   - *Soutien.* Opus (principal, E0) ; Neon (témoin, validité nulle, deuxième porte) ; Carbon (témoin, garde d'admissibilité) ; Opus (témoin, application au modèle réel).
   - *Pourquoi.* C'est sur le chemin critique de toutes les propositions mathématiques. Cela produit le cache d'activations qui ramène la suite sur processeur, sans toucher à l'organisme en pause.
   - *Réserve.* Des dizaines d'heures de carte graphique (illustratif), donc un devis.
3. **Partitionner les traces honnêtes en réservoirs disjoints avant toute mesure.** Calibrage, filtre, évaluation des fausses alertes et, s'il existe, retour. Un écart de fausses alertes entre honnêtes vus et honnêtes frais signe une fuite.
   - *Soutien.* Les trois modèles, dans les deux bras.
   - *Pourquoi.* Gratuit, et sans cela aucune mesure de fausses alertes n'est interprétable.
4. **Tester l'apport propre de l'organisme sur processeur, avant toute relance.**
   - *Contenu.* L'organisme complet affronte trois comparateurs : une archive étendue par un tiers, le même modèle pré-entraîné seul et un bras à fiches-leurres. Les mondes d'épreuve sont écrits par une instance aveugle aux fiches et aux candidats. On sépare mémoire et compétence par un plan 2 × 2 : lois historiques anonymisées contre lois inédites, avec ou sans modèle pré-entraîné. Placebo par graphe recâblé qui préserve degrés et dates. L'unité statistique est la famille de mondes, avec un seuil unique.
   - *Soutien.* Opus (témoin, III.3), Carbon (deux bras, III.3), Neon (deux bras, III.3).
   - *Pourquoi.* Cela décide si l'organisme vaut d'être relancé pour le contrôle, à coût de processeur seul.
   - *Réserve.* À rendre compatible avec la pause.
5. **Inscrire dans tout préenregistrement issu de ce dossier les règles de forme corrigées par les critiques.**
   - *Contenu.* Hypothèses $H_A$ et $H_B$ complémentaires, avec un seuil unique dimensionné. Variance estimée entre familles. Bases dotées des mêmes données honnêtes et du même budget. Contrôle par objets valides mais sans puissance. Transfert jugé dans la queue sélectionnée. Taux d'identification de l'oracle par sous-type de dommage.
   - *Soutien.* Corrections acceptées par les trois modèles au tour III.3.
   - *Pourquoi.* Ce sont les défauts que les critiques ont trouvés partout.

### À reprendre ensuite

- **Le filtre amont à deux étages**, validité puis puissance minimale et déduplication, éprouvé sur un banc conçu à l'aveugle du filtre (Neon, principal, III.3). Il ne vaut qu'une fois l'organisme jugé utile (retenue 4).
- **Les nuls par acte sans estimation** : randomisation active de l'ordre d'entrées commutatives par le défenseur (Carbon, témoin, III.3), symétrie entre copies (Neon, principal, III.3). Un nul à invariant estimé doit déclarer sa marge.
- **La permutation signée** contre la rotation, et le test de perte qui les oppose (Carbon, principal, III.3).
- **L'expérience E6 d'Opus** sur des sorties existantes de l'organisme : le volume généré améliore-t-il la précision du tri ?
- **La corruptibilité du tri interne de l'organisme**, avec paraphrase neutre et faux théorèmes en registre poli (A, témoin, III.3 ; A, principal, III.3). C'est un test d'hygiène, sans portée sur l'axe 2 du contrôle (A, principal, III.3).
- **Les essais pour les essaims**, à repousser après l'audit du nul (Carbon, deux bras).

### Non retenues

- **Le « résultat structurel » selon lequel la génération brute n'ajoute rien** (A, principal, III.1). Il supposait la précision du tri constante ; Opus l'a retiré au profit d'un test.
- **La première expérience de boucle d'Opus**, jugée sur les étages mêmes que le retour optimise (A, principal, III.1) : circulaire.
- **La précision à taux de fausses alertes apparié** (A, principal, III.1) : dégénérée.
- **Le bit de retour et « The Ladder »** (A, témoin, III.1) : retirés par leur auteur.
- **La rotation orthogonale secrète** (B, principal, III.1) : remplacée par la permutation signée.
- **La fonction $\kappa$ et le rapport diagnostique du filtre** (B, principal, III.1) : non définie ; seuil inatteignable.
- **« $(1+\varepsilon)^T$ donne presque 100 % de fausses alertes »** (B, témoin, III.1) : faux, corrigé.
- **La compression aléatoire de 4 096 à 256 dimensions** (B, témoin, III.1) et **le filtre de non-redondance de Spearman** (B, témoin, III.1) : retirés.
- **La borne lipschitzienne de transfert et l'α-investissement** (C, principal, III.1) : retirés par leur auteur.
- **La règle « deux familles sur trois »** (C, principal, III.1) : non jugeable.
- **La base à référence fixe réduite à 30 trajectoires** (B, principal, III.1) : handicapée par construction.
- **Le canari lexical comme preuve d'étanchéité** (A, témoin, III.1) : il ne prouve que l'absence de copie littérale.
- **Le post-mortem après lecture** (C, témoin, III.1) : analyse adaptative ; supprimé.
- **L'épreuve de la boucle sur cinq familles** (C, principal, III.3), à 700–1 800 euros illustratifs plus cinq familles consommées : prématurée tant que les retenues 1 à 4 ne sont pas faites.

### Ce qui reste à trancher

- La lecture de la règle de séparation pour le retour vers l'organisme (retenue 1). C'est une décision de Lazar, à prendre avant tout le reste.
- Le nombre de familles inédites que le programme peut produire. Plusieurs plans en dépendent pour être jugeables, et aucun modèle ne le connaît.
- Si l'organisme peut tourner, sans modification, pendant sa pause, pour les retenues 4 et E6.
- Le devis de l'audit du nul sur carte graphique (retenue 2).
- La boucle honnête de Neon : faut-il la garder, avec un résumé figé et un jeu frais, ou la supprimer ? La critique qui la vise n'a été formulée qu'au bras témoin, et contre Carbon.

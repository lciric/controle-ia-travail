# Rapport du rédacteur — conception de la course « seuil et moniteurs » de l'organisme d'idéation — v1

- Signé : rédacteur de la conception de la course seuil et moniteurs, modèle F. 2026-11-21 ; relevé de `date -u` avant l'écriture : 06:43:41Z. Python 3.13.18.
- Statut : pièce de travail (classe C). Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit, aucun lancement.
- Mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-redacteur-conception-course-seuil-et-moniteurs-v1.md`, empreinte `4f1fd30358a35e8f1482efeb962730881d213a6306054fd52b096488288f1159`, vérifiée contre son compagnon. Deux ajouts de la mère reçus avec et pendant le travail : (1) dire ce que la course apporte au-delà du collisionneur v9 v3 ; (2) brancher l'expérimentateur et l'étage des tests de mort, dire ce qui les porte, ce qui manque, le coût du bac et les mondes plantés.

## 0. Verdict

1. **Les cinq pièces sont écrites ; aucune n'est scellable en l'état.** Le préenregistrement court est un brouillon qui liste ce qui lui manque.
2. **Le véhicule est à écrire.** Rien de ce qui porte l'expérimentateur et les tests de mort n'est sur `origin/main`, et le régime « tests de mort réels » n'est accordé que pour le palier 1 de l'héritage.
3. **Devis : 97,02 USD au cas bas, 256,14 au cas haut, 276 au pire.** Ligne de course demandée : 260 USD exactement, plus trois lignes à part (10, 5 et 1).
4. **Ce que la course apporte au-delà du collisionneur : un verdict calculé.** Chaque proposition affronte un test de mort exécuté sur un monde planté à vérité connue ; le collisionneur ne rend que des textes et des critiques.
5. **Trois à cinq jours de sessions avant le premier appel payant.**

## 1. Sources lues, et leurs empreintes

Toutes par `git show origin/main:CHEMIN > fichier`, après `git fetch origin main` (commit `55f7f6e1fe6779a4fb57b5fd07f58d33d598cbef`), sauf mention.

| pièce | chemin | empreinte | lu |
|---|---|---|---|
| faits neutres de la mère | `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/faits-seuil-et-moniteurs-v1.md` | `c8c7fb32ff7d2c8ce651607a8a777e8ee1da2cf45d101fa3a5e4f426cfb59119` | en entier |
| question neutre de la mère | même dossier, `question-seuil-et-moniteurs-v1.md` | `a5fbe8986745bf5c43eca3d33472abaeea152308db4db9aa6e16164ed8d80940` | en entier |
| collisionneur v9 v3 | `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` | lignes 1 à 1363 sur 1894 (protocole, consignes des tours, gardes, appels, exécution d'une cellule) ; non lues : l'audit de Jev, les commandes d'étage, le devis, `verifier` |
| son rapport de développeur | `docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v3.md` (nom trouvé à l'en-tête du code) | `99bd3d48e3c53aaed4eedb638e782a9d5d5df3db25912702eff9e48be18e8648` | en entier |
| question v5, « nouvelles attaques » | `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v5.md` | `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f` | en entier |
| sa partie servie | `prereg/ideation-nouvelles-attaques-v1/partie-servie-question-v5-v1.md` | `4cd360baea1076ec2b19b2c7ba85675e739bc3104c709d4fd57c0769975b1cf1` | en entier |
| ordre de course v3 | `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` | en entier |
| préenregistrement court v9 | `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` | titres, table des pièces, « Hypothèse » (début), « Prédiction », « Métrique », « Seuil » (début) ; le reste par recherche de mots |
| devis v6 | `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/devis-course-nouvelles-attaques-v6.md` | `d825cb313898ea5111ede1ef3103ab25b1b923e1f52103481427919ce9d19c2c` | titres et lignes de sources (S1 à S17), par recherche de mots |
| gabarit | `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` | en entier |
| N-058, N-067 | `docs/decisions/decision-N-058-v1.md`, `decision-N-067-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` ; `966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589` | en entier |
| N-044, N-045 v2, N-049, N-064, N-065 | `docs/decisions/` | `2b70bdac…`, `c7b05e39…`, `8a5bf5e5…`, `387c9d4e…`, `f820e90d…` | **extraits et empreintés, non ouverts** : je les tiens par ce qu'en disent l'ordre de course v3 (§ 4, § 6) et N-067 (§ 2) |
| consignes permanentes | `CLAUDE.md` | `4689ca3e03da5a12379ba83b1da4d636b34cba30295e23fa0c462ca242f37683` | celles servies à ma session |
| registre des GO | `registres/go.md`, copie `lectures/lecture-go-origin-main.md` | `38f63a0d40b591fb1890437107cdb77511916360e2bda0baddda70ff5986d63b` | par recherche de lignes, et les vingt-deux dernières |
| registre des décisions | `registres/decisions.md`, copie `lectures/lecture-registre-origin-main.md` | `352e3ea921a117faec79920fe9d329f6d96bcd1de524a04bd0eaaf2ed5caea16` | par recherche de lignes |
| rapport du développeur de la version 68 | `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md`, **lu sur le disque de la branche `lot/compte-organisme-v1`** : absent de `origin/main` | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6` | en entier |
| lanceurs de course versions 9 et 10 | `scripts/lancer_course_auto_conception_v9.py`, `_v10.py`, **même disque** : absents de `origin/main` | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` ; `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` | version 9 : constantes et noms de fonctions, par recherche de mots ; version 10 : empreinte seule |

**Modèles de forme que je n'ai pas trouvés par un chemin** : le devis v11 (`205e08f2…`), l'additif 1 v5 de la v9 (`9f731795…`), le complément de valeurs v3 (`b4ef87dc…`) et son additif (`ce76e0d6…`). Le registre donne leurs empreintes, non leurs chemins, et le mandat m'interdit toute commande de liste. J'ai pris la forme du devis sur le devis v6, dont le chemin est dans la table du préenregistrement court v9. **Les entrées de coût viennent donc du devis v6, non du v11** ; les coûts réels de la course v9 qu'il cite (S1) ne dépendent pas du nombre d'espèces de la course « nouvelles attaques ».

## 2. Ce que la course apporte au-delà du collisionneur, et les doublons écartés

**Ce que fait le collisionneur** (lu dans son code) : l'étage III. Chaque espèce reçoit les faits et la question, écrit à l'aveugle au plus 3 500 mots (ce que la question suppose, des expériences en duel, la mesure minimale de chaque instrument, l'ancrage matériel), puis critique les autres en 3 000 mots, puis répond en 3 500. Quinze cellules ; pire cas 23,45 USD ; aucune exécution, aucune vérité en face.

**Ce que la course apporte, et que le collisionneur ne peut pas rendre** :

1. **Un verdict calculé.** Chaque proposition retenue est programmée par l'expérimentateur et jouée dans le bac sur un monde planté dont le vrai quantile est connu. On lit le taux réel de fausses alertes et la puissance. Une proposition morte est rapportée morte.
2. **Une couverture voulue.** Des cases tirées par graine sur trois axes, six voies servies au moins à cinq ; une famille de cases et une famille de mondes tenues à l'écart.
3. **Des fiches à champs fermés**, une idée par fiche, chacune avec sa règle calculable, sa garantie dite et son test de mort écrits avant le jeu.
4. **Le coût en face de l'oracle**, par espèce et par rôle (N-045 v2, N-058).
5. **Une mesure, pour information, du rang des juges contre le calcul** — matière pour le papier C, sans rien revendiquer.
6. **La première mesure du coût réel d'un étage à tests de mort**, à rendre au devis du palier 1 de l'héritage.

**Doublons écartés** (question, § 1 et § 6) : les six points de la question de la mère sous forme libre ; « ce qu'un expert ferait », « les données brutes », « la reformulation de la demande » ; la critique croisée entre modèles ; les plans d'expériences sur épisodes d'agent réels et leur coût ; tout avis sur ce que le programme a déjà décidé du papier. La course ne sert aux proposeurs aucune sortie du collisionneur ; la mère étiquette après coup les fiches « déjà au collisionneur », sans rien leur retirer.

**Ce qui resterait un doublon si l'étage tombait.** Sans l'étage, la course rendrait surtout des idées que le collisionneur rend déjà, en plus court et plus cher. C'est pourquoi le levier « sans l'étage » du devis est dit contraire à l'exigence.

## 3. Réponse aux quatre points de l'ajout de la mère

**(1) Quel orchestrateur et quel lanceur portent aujourd'hui l'expérimentateur et les tests de mort, avec chemins et empreintes sur `origin/main`.** **Aucun, sur `origin/main`.**
- L'étage des tests de mort et le tour fermé vivent dans le dépôt à part de l'orchestrateur, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (`etage_entre_generations_v57`, lanceur `demonstrations/ideation_v59.py`). Le palier 0a (R-3882, rapport `93d8a104…`, branche `lot/compte-organisme-v1`, commit `94fe7658`) y a exécuté une loi plantée dans un bac **local**, avec un expérimentateur et un lecteur **écrits par programme**, à zéro dollar.
- La version 68 (paquet de huit fichiers, rapport `ad42b722…`) porte le régime « tests de mort sans rien servir », **en moteur simulé seulement** ; elle refuse le moteur réel par construction. Elle est sur la branche `lot/compte-organisme-v1`, pas sur `origin/main`.
- Les lanceurs de course versions 9 (`1b47c1cf…`) et 10 (`f4196ec5…`) sont sur la même branche, pas sur `origin/main`. La version 9 refuse tout étage ; la version 10 a le branchement écrit éteint. **Le lanceur version 11 n'existe pas** sur le disque.
- **L'expérimentateur modèle (GO-2026-11-19-75) n'a jamais joué dans un étage réel.** Le bac réel n'a jamais été lancé avec l'étage.
- Je n'ai pas lu R-3882 au-delà de sa ligne de registre ni ouvert son rapport `93d8a104…` : son chemin n'est pas au registre.

**(2) Ce qui manque pour ce régime.** Neuf points, à l'ordre de course, § 2.2 : le mot de Lazar qui étend le régime ; une version de l'orchestrateur ; un lanceur ; un additif ; une configuration ; les mondes plantés et le programme de mesure ; l'essai réel du bac ; les témoins ; le tirage, les mesures et la garde de motifs. **Oui, le régime « tests de mort réels » n'existe que pour le palier 1 de l'héritage** (GO-2026-11-20-05, point 1a), et encore : seul son additif est scellé (`cb352811…`), son code ne l'est pas. L'extension est comptée au calendrier (trois à quatre sessions pour l'orchestrateur, le lanceur, l'additif et la configuration ; ordre de course, § 11) et au devis par le plafond de l'étage et la ligne de la machine.

**(3) Le coût du bac.** Machine jetable et essai du bac : 2 USD au cas bas, 5 au cas haut, **10 de plafond**, en ligne à part (GO-2026-11-20-05, point 4b). C'est une règle du rédacteur : la seule source est « quelques dollars » (R-3984). L'étage lui-même : 21,33 / 107,33 / 110, tout entier fait du coût de l'expérimentateur modèle ; les calculs du bac sont sur processeur.

**(4) Les mondes plantés.** Ordre de course, § 7 : sept familles pour les règles de seuil (queue légère, queue lourde, mélange, tranches déséquilibrées, pas corrélés, dérive, ex æquo), un monde à trois populations pour les moniteurs et les protocoles tirés du papier, avec une composante d'intention réglable ; vérité connue (loi, quantile vrai, étiquettes, taille du signal) ; six mesures ; ce qui tue ; une famille tenue à l'écart. À écrire, contre-lire et sceller avant la sonde de refus.

## 4. Mes choix

1. **Une génération, non trois.** La lecture entre générations ne joue en réel sur aucun code existant. La leçon de la course « nouvelles attaques » est de ne pas écrire un texte qui exige un véhicule que personne n'a.
2. **Un étage après la génération, rien de servi** : le régime que la version 68 sait déjà jouer en moteur simulé, et celui que GO-2026-11-20-05, point 1a, nomme.
3. **Lecteur et comparateur par programme**, expérimentateur modèle : la lettre de GO-2026-11-19-75, qui ne vise pas le lecteur.
4. **Candidates tirées par graine**, jamais par le rang des juges : N-058.
5. **Deux morts distinctes**, « invalide » et « sans gain », et une classe « non exécutée » qui n'est ni l'une ni l'autre : sans la seconde mort, la règle « ne jamais alerter » tiendrait toujours.
6. **Un préenregistrement court est écrit** (§ 5).
7. **Cases et forme de génération de la course v9** (cinq espèces, onze appels) : c'est la seule forme dont les coûts sont mesurés.

## 5. Un préenregistrement court est-il exigé par la règle R1 ? Oui.

La règle R1 vise « toute expérience décisive, simulation comprise ». Une course d'idées seule ne décide rien ; la course « nouvelles attaques » a pourtant eu son préenregistrement, pour geler ses gardes et sa lecture. **Ici la question ne se pose plus : avec l'étage, la course exécute des simulations dont le résultat tue ou non une proposition.** Les seuils de mort, les mondes, les graines et l'ordre des candidates doivent être gelés avant qu'un seul score soit tiré. Je l'ai donc écrit, sur le gabarit. Il est incomplet par construction : il attend les mondes, le véhicule et le complément de valeurs.

## 6. Ce que la lettre ne fixe pas — remarques

1. Le mandat demande « le nombre de générations » et « l'héritage » : je réponds une génération, et je dis que l'héritage n'est ni mesuré ni récompensé ici. C'est un écart à ce que le mandat laissait attendre ; il est porté en D-M3.
2. « Chaque proposition retenue affronte un test de mort » : la lettre ne dit pas qui retient. J'ai écrit : le portier sur la forme, puis un tirage par graine ; au plus vingt.
3. La lettre ne dit pas de quel relais relève l'expérimentateur.
4. La lettre ne dit pas si la course attend la fin du collisionneur. Elle ne lit rien de lui ; elle peut partir avant ou après.
5. Les chiffres du papier servis aux proposeurs viennent des faits de la mère, non d'une lecture sur PDF par moi (règle R7) : servis comme contexte, non opposables.
6. Les noms des classes d'issue sont de moi ; l'additif scellé de la version 69 en fixe d'autres, que je n'ai pas lus.
7. **Écart déclaré à mon mandat** : j'ai lu trois fichiers sur le disque de la branche `lot/compte-organisme-v1`, par leur chemin complet, faute de les trouver sur `origin/main`. Le mandat disait « sur `origin/main`, par `git show` ». Sans eux, je ne pouvais pas répondre au point (1) de l'ajout.
8. **Écart déclaré** : une recherche de mots dans ma copie du registre a rendu une sortie de plusieurs centaines de lignes de noms de fichiers ; elle n'a rien parcouru d'autre que cette copie.
9. Dans un rapport à Lazar, les mots « espèce », « portier », « bac », « tour fermé » demandent une phrase d'explication ; je les ai gardés parce que le registre les emploie.

## 7. Décisions

### Pour Lazar

**D1 — Étendre le régime « tests de mort réels » à cette course.**
- Décision : accorder, pour cette course seule, le régime que GO-2026-11-20-05, point 1a, réserve au palier 1 de l'héritage.
- Enjeu : sans ce mot, aucun étage ne peut être écrit pour cette course, et elle redevient un doublon du collisionneur.
- Options : (a) oui, pour cette course seule, sur son devis ; avantage : l'exigence est tenue ; inconvénient : un second régime réel à écrire et à contre-lire à côté de celui du palier 1. (b) non, la course attend que le palier 1 ait joué son étage réel ; avantage : un seul premier étage réel, sur le plan déjà scellé ; inconvénient : aucune date. (c) l'étage se joue avec l'expérimentateur écrit par programme, à zéro dollar d'appels ; avantage : le chemin du palier 0a, déjà éprouvé ; inconvénient : contraire à GO-2026-11-19-75, et un programme ne sait pas traduire une fiche libre en code.
- Recommandation : (a), confiance 0,6.
- Défaut sous 48 heures : aucun (dépense et écart à un mot donné).

**D2 — La ligne de calcul.** Format complet au devis, § 8. Options : (a) 260 USD plus 16 de lignes à part ; (b) l'étage seul sur les propositions du collisionneur, 120 USD ; (c) rien, lire d'abord le collisionneur. Recommandation : (a), confiance 0,55. Défaut : aucun.

**D3 — Les clés.**
- Décision : sur quelles clés cette course se paie, et quand.
- Enjeu : les clés Claude désignées sont tenues par les parts scellées de la course « nouvelles attaques » (439,59 sous 456) ; la carte du deuxième relais n'est accordée que pour les appels déjà accordés.
- Options : (a) la course part après la clôture de la course « nouvelles attaques », sur les soldes relus ; avantage : aucune part scellée n'est touchée ; inconvénient : attente. (b) une recharge d'une clé Claude au cas haut (192,67 : premier relais 85,34 plus expérimentateur 107,33) et l'extension du mot sur la carte du deuxième relais (46,80) ; avantage : les deux courses sont indépendantes ; inconvénient : une dépense de plus à avancer.
- Recommandation : (a), confiance 0,65 : le véhicule demande de toute façon trois à cinq jours.
- Défaut : aucun.

### Pour la mère

**D-M1 — Servir, ou non, les sorties du collisionneur aux proposeurs.**
- Enjeu : éviter les doublons, sans ancrer les proposeurs.
- Options : (a) ne rien servir, étiqueter après coup ; avantage : la course reste indépendante, et l'on mesure le recouvrement ; inconvénient : des fiches redisent le collisionneur. (b) servir une liste « déjà proposé » d'une ligne par idée ; avantage : moins de doublons ; inconvénient : il faut que la mère ait lu et réduit quinze cellules, la liste ancre, et c'est servir à un agent la sortie d'autres modèles.
- Recommandation : (a), confiance 0,6. Défaut sous 48 heures : (a).

**D-M2 — Le véhicule : attendre celui du palier 1, ou un mandat propre.**
- Options : (a) attendre la version 69 et le lanceur 11, puis en dériver ; avantage : un seul code d'étage réel, contre-lu une fois ; inconvénient : la course dépend du calendrier de l'héritage. (b) un mandat de développeur propre, maintenant ; avantage : la course ne dépend de rien ; inconvénient : deux codes voisins, deux contre-lectures.
- Recommandation : (a), confiance 0,55 ; les mondes plantés et le programme de mesure, eux, peuvent s'écrire tout de suite, sans attendre. Défaut sous 48 heures : (a), et le mandat des mondes part.

**D-M3 — Une génération.**
- Options : (a) K = 1, comme écrit ; (b) K = 2, ce qui demande la version de l'orchestrateur qui lit le registre des tentatives, non écrite, et le mot de Lazar sur ce qui est servi.
- Recommandation : (a), confiance 0,7. Défaut sous 48 heures : (a).

**D-M4 — Qui écrit les mondes plantés.**
- Options : (a) un développeur d'une autre lignée que les cinq espèces et que l'expérimentateur, contre-lu par un autre modèle ; (b) la mère.
- Recommandation : (a), confiance 0,6 : celui qui écrit le monde ne doit ni proposer ni programmer les règles. Défaut sous 48 heures : (a).

**D-M5 — Les valeurs du rédacteur à geler** : onze cases, vingt candidates, quatre par voie, R = 2 000, intervalles à 99 %, les familles A à G, la base « plus grand score de l'échantillon », le quart des fiches mises à part. Routine de la mère ; défaut : mes valeurs, après la contre-lecture.

## 8. Ce que je n'ai pas fait

- Aucune contre-lecture de mes pièces : elles sont à contre-lire par un autre modèle (règle R2).
- Aucune dérivation par programme de la partie servie ; la garde de motifs n'a pas été jouée.
- Aucun relevé de solde, aucune offre du loueur.
- Aucune lecture du code de l'orchestrateur, de l'étage, du tour fermé.
- Aucune vérification sur PDF des chiffres du papier.
- La table d'empreintes du dossier est à côté : `empreintes-dossier-v1.txt`.

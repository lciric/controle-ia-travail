# Devis — la part du lot honnête neuf qui étalonne les deux verdicts principaux du bras « papier dopamine » — v2

- **Statut** : devis de classe A, **version 2**. Elle remplace la v1 (`devis-lot-l-1-v1.md`, `613f16a8d6be654539ddf7db8d2849f646baca3c955ca05a891768f0519f1638`), gardée à côté, et porte les six corrections de sa contre-lecture (`contre-lecture-devis-lot-l-1-v1.md`, `8bfdbd027112267fda841b973edac991fb5f36c22bc64878021628a48903285d` : « conforme après ces corrections », B-1 bloquante) ; table au § 13. **Elle attend la vérification des corrections par le même contre-lecteur (Opus 5.5)**, puis le scellement par la mère. Il ne vaut accord de rien et n'engage aucune dépense. Il répond à la décision de Lazar « lot L-1 avec la correction 11 » (GO-2026-11-21-29) et à la demande « fais les devis » (GO-2026-11-21-34).
- **Auteur** : Claude Fable 5.2 (identifiant servi `claude-fable-5-2`), concepteur (R-3735), sous-agent de la session mère. La v1 est écrite le 21 novembre 2026, de 10:50 à 11:10 UTC (`date -u`), dépôt à `c98ec89a0` ; la v2 le même jour, de 11:17 à 11:50 UTC, dépôt à `a36671d19`. Aucun appel payant, aucune machine créée ; un seul appel de réseau, pour la v1, public et sans clé : la recherche d'offres du loueur de cartes. Consigne commune de méthode (v1) appliquée : `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`) ; relevé de méthode au § 12.
- **Source unique des chiffres** : `prereg/papier-dopamine-moniteur-v1/calculs-devis-lot-l-1-v2.py` (`1c56ef84160c1b8330d0548d21f4ed24daf380eb9546c481c1e7c21c5941eac0`), sortie `calculs-devis-lot-l-1-v2.txt` (`765245244833f32b074fbf10d60d2d057172bbec08f194fe8df24a98dd8c6ed7`), lancé par `.venv/bin/python -I` ; cités « calcul, bloc ». Les blocs 1 à 8 sont ceux des calculs v1 (`5c43fe8f…`), à l'octet : aucun chiffre de la v1 ne change. Le bloc 9 (deux instances, pire cas sous les bornes) et le bloc 10 (objets de contrôle) sont neufs. Relevé brut du marché : `releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196`), même dossier. Montants en USD.
- **Pièces lues** : le préenregistrement court v7, brouillon non scellé (`e05f4a998704391a62e09a3a6a7ab9804850a9cedb9c01c5bb947d5322c315ef`) ; sa contre-lecture (`a38b5469e2f8754ed4260cbeac26ec4f5e16c06bc0cf7a37a017f576952fa1c8`), corrections 1, 8, 10 et 11 ; la liste approuvée des sondes et des lots lisibles (`03f6a67143753cbcb79a33ab13fc724640092895243d0694625cfe83274b53ff`) ; l'inventaire des décisions ouvertes (`5986c07921356858e5b095a9a48053be5de88daf8dbf0f3c0625da89e7e6536f`), section C ; le devis scellé du barreau 5 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md`, `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc`), § 1 à § 4, pour les débits et les prix.
- **Pour la v2** : le rapport de contre-lecture et la consigne commune.
- **Non ouvert** : aucune conception d'organisme, aucun résultat, aucun fichier de scores, ni la décision N-054. Les débits viennent donc de seconde main pour moi ; le contre-lecteur a relu la source première (voir § 4).

## 1. Ce qui tourne, et pourquoi

**Ce qui tourne.** Le modèle du programme (Llama-3.1-8B-Instruct), en agent honnête, joue des épisodes entiers sur le banc de tâches, par le harnais du programme. À chaque épisode on garde le texte, l'issue calculée par programme, et l'état interne au dernier jeton de l'énoncé et de chaque action, aux couches 7, 15 et 23. Rien d'autre : aucun épisode saboté, aucun adaptateur de sabotage chargé, aucune sonde lue sur la machine.

**Pourquoi.** Les deux verdicts principaux du bras se lisent à un seuil de 1 % de fausses alertes, et ce seuil se lit sur un lot d'épisodes honnêtes tenu à l'écart :
- **le saboteur alerte-t-il plus que 1 % ?** (prédiction P1) demande au moins **368** épisodes honnêtes effectifs ;
- **le saboteur à dommage confirmé alerte-t-il autant que l'honnête qui échoue ?** (prédiction P2) en demande au moins **437**, au risque de 5 % que Lazar a retenu (calcul, bloc 1 ; égal aux calculs de la v7 et de sa contre-lecture).

La liste approuvée n'offre aucun lot gratuit pour cet étalonnage : les épisodes honnêtes du premier test n'y sont « pas un lot de jugement ». Seul le lot honnête neuf (L-1) le peut, sur une part à lui (correction 11). **Ce devis chiffre cette part, et elle seule.**

## 2. Ce que ce devis fixe pour cette part

Ce sont les objets que le préenregistrement demande au devis du lot honnête neuf (section « Le lot honnête neuf : exigences pour le devis »). La valeur ouverte VO-21 les demande pour le lot des gains de fusion : elle reste ouverte pour lui (§ 10).

1. **Borne haute : 1 311 épisodes réels** (trois fois 437). Choix de conception, pas une estimation : au-delà, l'effet de plan dépasse 3 et le lot ne vaut plus son prix pour un bras qui rapporte.
2. **Une seule tranche d'achat, réglée par des comptes.** Le nombre d'épisodes est calculé **avant le premier épisode**, par la règle du § 3, à partir de trois nombres gelés à l'addendum de l'étape 2a. Pendant la course, on ne regarde que des comptes (épisodes finis, familles complètes, erreurs du harnais). Aucun score n'est regardé : les bornes exactes des seuils restent donc valides.
3. **Aucune strate sur-tirée.** Le mélange de référence est uniforme : toutes les familles retenues, le même nombre d'épisodes par famille, les tâches tirées dans chaque famille par graine dérivée (`numpy.random.SeedSequence`, R9). Il n'y a donc pas de quantile pondéré, et la borne que la correction 10 exigeait n'a pas d'objet.
4. **Familles.** La mère en écrit la liste nominative à l'addendum, sans lecture de résultats : familles du banc qui ne sont ni du jeu final, ni tenues à l'écart, ni d'une banque de confirmation, ni d'une liste scellée de G1, et qui sont disjointes des familles des autres lots du bras (apprentissage de la sonde de réussite attendue, deux moitiés de l'étape 2b, apprentissage et évaluation de l'étape 3).
5. **États gardés.** Le dernier jeton seulement (0,35 Go à la borne haute ; calcul, bloc 6). La série par jeton (72 Go à la borne haute) n'est pas gardée : le maximum sur les jetons de l'action, que le texte rapporte à côté, se rejoue plus tard par relecture forcée des mêmes textes.

## 3. Combien d'épisodes

L'effectif effectif d'un lot groupé par familles est son effectif divisé par 1 + (m − 1)·ρ, où m est le nombre d'épisodes par famille et ρ la corrélation, dans une famille, de l'indicatrice d'alerte (section « Seuil » de la v7). **Règle** : avec F familles retenues et le plus grand des ρ gelés à l'étape 2a pour les scores dont cette part fixe le seuil (la sonde de réussite attendue, et tout autre score que l'addendum lui assigne), on prend le plus petit m tel que le plancher de F·m / (1 + (m − 1)·ρ) atteigne 437 ; le lot compte F·m épisodes. Si F·m dépasse la borne haute, on refait le calcul pour 368 : la première question reste jugeable, la seconde est dite « non concluante » d'avance. Si 368 ne tient pas non plus, **rien n'est acheté** et les deux sont dites « non concluantes » d'avance.

Épisodes à acheter pour 437 épisodes effectifs (calcul, bloc 3 ; « — » : non jugeable sous la borne) :

| familles retenues F | ρ = 0 | ρ = 0,05 | ρ = 0,10 | ρ = 0,20 | ρ = 0,30 | ρ = 0,50 |
|---|---|---|---|---|---|---|
| 40 | 440 | 920 | — | — | — | — |
| 60 | 480 | 660 | — | — | — | — |
| 80 | 480 | 640 | 880 | — | — | — |
| 100 | 500 | 600 | 700 | — | — | — |
| 150 | 450 | 600 | 600 | 900 | — | — |
| 200 | 600 | 600 | 600 | 800 | 1 000 | — |
| 300 | 600 | 600 | 600 | 600 | 600 | 900 |
| 437 ou plus | 437 | 437 | 437 | 437 | 437 | 437 |

**Ce que la table dit.** Le prix dépend peu du nombre d'épisodes et beaucoup du nombre de familles. Avec moins d'une centaine de familles et une corrélation de 0,2, aucun nombre d'épisodes n'achète le verdict. **F et ρ ne sont pas fondés** : je ne connais ni l'un ni l'autre (§ 8).

## 4. Machine, prix relevés et leurs sources

- **Machine** : une carte A100 SXM4 de 80 Go chez le loueur de cartes (Vast.ai), aux bornes du devis scellé du barreau 5 : au plus 1,30 USD de l'heure, au moins 16 cœurs, 128 Go de mémoire vive, stockage au plus 0,08 USD de l'heure. Disque d'au moins 80 Go (choix de ce devis : 40 Go téléchargés, 2 Go de sorties, marge). Une autre carte, seulement sur un mot de Lazar.
- **Prix relevé ce jour** (21 novembre 2026, 10:55:20Z, recherche publique d'offres, sans clé ; calcul, bloc 8) : 13 offres de cartes de 80 Go, de 0,85 à 2,10 USD de l'heure ; **deux passent toutes les bornes, à 1,097 et 1,163 USD de l'heure**. C'est un instantané : le marché change d'heure en heure. Dernier prix payé par le programme pour cette carte : 1,055 USD de l'heure (`registres/depenses.md`, l. 573, 21 novembre).
- **Prix employés au calcul** (devis scellé du barreau 5, § 1) : 1,0889 à 1,30 USD de l'heure ; pire cas 1,40 avec un hôte deux fois plus lent ; stockage 0,03 à 0,08 USD de l'heure ; téléchargement 0,026 à 0,05 USD par Go. Les deux offres relevées tombent dans la fourchette.
- **Débit** (même devis, § 1, qui cite `prereg/T0.6-organismes-v0-v1.md`, l. 640-652) : 40,2 secondes par épisode en lots de 8 ; frais fixes de 1,8 heure par instance (mise en place, essais, poussée). **De seconde main** pour l'auteur ; relu par le contre-lecteur sur la source première (`prereg/T0.6-organismes-v0-v1.md`, `ef31feff…`, l. 642-643) : course réelle de P3, 240 épisodes en 9 644,6 s, génération seule, la passe d'activations à part (0,45 s par épisode) ; la course entière, ≈ 3,6 heures, laisse ≈ 0,9 heure de frais fixes, sous les 1,8 heure comptées. Banc de P3 : à confirmer pour ce lot (§ 8).

## 5. Durée, cas attendu, pire cas, coupure

Une instance (calcul, bloc 5) :

| scénario | épisodes | heures de carte | coût (USD) | pire cas (USD) |
|---|---|---|---|---|
| bas : un épisode effectif par épisode réel | 437 | 6,7 | 8,6 à 11,3 | 21,9 |
| **cas de référence** (convention non fondée : 150 familles, ρ = 0,10) | 600 | 8,5 | **10,6 à 13,8** | 27,3 |
| borne haute | 1 311 | 16,4 | 19,5 à 24,8 | 50,8 |

- **Cas attendu** : je ne peux pas en fonder un, faute de F et de ρ. Le cas de référence est une convention d'affichage ; l'attendu se situe entre le bas et la borne haute, soit **8,6 à 24,8 USD**.
- **Pire cas** : 50,8 USD (borne haute, hôte deux fois plus lent, 1,40 USD de l'heure, prix hérité du devis scellé ; 47,5 USD sous la borne de l'offre, 1,30 ; calcul, bloc 9). **La coupure l'empêche dans les deux cas.**
- **Coupure : 37 USD.** C'est la borne haute sur un hôte une fois et demie plus lent, au prix haut (36,13, arrondi). Au pire cas, elle arrête la course vers 883 épisodes au lieu de 1 311.
- **Horloge** : 6,7 à 16,4 heures sur une carte. Sur deux cartes, 4,2 à 9,1 heures, pour 3 à 4,5 USD de plus (frais fixes doublés) ; la coupure reste commune. Elle ne couvre alors la borne haute que si les hôtes ne sont pas plus de 1,31 fois plus lents ; à 1,5 fois, deux cartes coûteraient 41,9 USD, et la coupure arrête vers 1 071 épisodes au lieu de 1 311 (calcul, bloc 9).
- **Prix d'un épisode de plus** : 100 épisodes coûtent 1,25 à 1,54 USD (calcul, bloc 2).

## 6. Ce qui est compté au compteur

Le cumul relevé chez le loueur pour l'instance, ou pour les deux ensemble, de la création à la destruction : heures de carte, stockage, téléchargement du modèle, sortie des données. Une ligne d'engagement est écrite au registre des dépenses avant la première minute : « engagement : papier dopamine, part d'étalonnage du lot honnête neuf ([ligne d'accord], plafond 37 USD, arrêt au cumul plus un quart d'heure) : devis [chemin, empreinte], addendum [chemin, empreinte], commit [code du lanceur] ; A100 SXM4 80 Go ≤ 1,30 USD de l'heure ; F, m, épisodes prévus ; attendu, pire cas ; dépense antérieure sous cette ligne ». Le temps des agents n'est pas compté.

## 7. Ce qui arrête la course

1. Le nombre d'épisodes prévu est atteint, familles complètes.
2. Le cumul relevé plus un quart d'heure de carte atteint 37 USD.
3. L'échéance d'arrêt de l'instance, comptée depuis sa création : deux fois la durée prévue.
4. Un épisode qui n'est pas honnête (adaptateur de sabotage chargé, consigne de sabotage servie), une famille hors de la liste de l'addendum, ou un modèle servi qui n'est pas celui du programme : arrêt, nœud.
5. Un score regardé pendant la course : arrêt, nœud (ligne de la liste d'arrêt du préenregistrement).

Après un arrêt : versement de tout ce qui existe (règle « récupérer ce qui est récupérable »), puis destruction par identifiant (R10). Seules les familles complètes comptent ; l'effectif effectif est recalculé par la règle du § 3. S'il manque, le verdict concerné est « non concluant ». **Aucune rallonge sans devis neuf.** Les gardes sont à tester sur un cas sain et sur un artefact (R5) : le code du lanceur n'existe pas encore (classe B, à contre-lire).

## 8. Ce qui n'est pas fondé, et ce qu'il faut relever

| manque | qui le ferme | effet |
|---|---|---|
| Le nombre de familles éligibles F | la mère, par inventaire des noms (VO-2) | fixe si le lot est achetable (table du § 3) |
| La corrélation par famille ρ | l'étape 2a, sur épisodes honnêtes seuls | fixe le nombre d'épisodes |
| Le banc, le harnais et le mode d'induction des épisodes sabotés que ce lot sert | la mère (VO-2, VO-4) | le lot doit être tiré sur le même banc et par le même harnais ; si chaque mode demande sa propre variante honnête (consigne inerte, adaptateur honnête), **le lot se multiplie par le nombre de variantes**, ce que ce devis ne compte pas |
| Le débit de 40,2 secondes par épisode sur ce banc, avec la seule garde du dernier jeton | source première relue par le contre-lecteur (banc de P3) ; la première heure de la course sur le banc de ce lot | toutes les heures |
| Le nombre d'actions par épisode (10, inféré) | la mère | la taille des sorties seulement |
| Le prix à l'heure de la création | l'opérateur, à la création | dans la fourchette, ou pas de création |

## 9. Ce qui doit exister avant la première minute

1. Le préenregistrement court scellé (la v8 : la v7, ses quinze corrections, les deux choix de Lazar).
2. La porte de reproduction passée (étape 1, prédiction P0) : le texte ferme chaque étape si la précédente échoue. **L'étape 1 n'a pas de devis** (§ 10).
3. L'addendum scellé de l'étape 2a, qui gèle F, m, ρ, la liste des familles, et cite ce devis par son chemin et son empreinte.
4. Le code du lanceur contre-lu, son commit inscrit.
5. Le crédit du loueur, diminué des coupures restantes des autres courses ouvertes sur le même crédit, au moins égal à la coupure, relevé à la création ; aucune recharge n'est supposée.

**Conséquence, dite sans détour** : cette part ne peut pas tourner avant l'entretien du 1er décembre. Elle ne débloque rien seule. Elle peut servir un billet plus tard, si Lazar y fait entrer ce bras.

## 10. Ce que ce devis ne compte pas

- **L'étape 1, le rejeu du chiffre publié sur MATH500** : première dépense du bras, sans devis. Il manque deux mesures pour le chiffrer : la longueur des réponses du modèle (jusqu'à 16 000 jetons par question) et son débit de génération en lots. Une tranche de mesure d'une heure de carte au plus les donnerait ; elle demande elle-même une ligne.
- **Les autres parts du lot honnête neuf** : les deux moitiés de l'étape 2b, dont les tailles sont fixées par l'addendum ; un lot de pré-mesure pour l'étape 2a, si les épisodes honnêtes du premier test ne remplissent pas la condition C-2. Au prix du § 5.
- **Le lot des gains de fusion** (« bat telle base », « ne bat pas telle base », prédiction P5) : 5 000 épisodes effectifs, soit 62 à 77 USD avec un effet de plan de 1, et 187 à 231 avec un effet de plan de 3 (calcul, bloc 7). Non demandé : ces comparaisons sont dites « non concluantes » d'avance.
- **Le lot d'évaluation** : les épisodes sabotés, et les 133 échecs honnêtes effectifs par côté que la seconde question exige (calcul, bloc 1).
- La relecture forcée pour le maximum sur les jetons (10 minutes de carte à la borne haute, plus les frais fixes) ; l'apprentissage et la lecture des sondes, au processeur ; le temps des agents.

## 11. Ligne d'accord proposée

Elle est conditionnelle, comme l'accord de calcul de la formation du barreau 5 (GO-2026-11-19-86). Numéro et référence posés par la mère.

`| GO-2026-11-21-NN | 2026-11-21 | calcul | Papier « dopamine » : part du lot honnête neuf qui étalonne les deux verdicts principaux, 437 épisodes honnêtes effectifs visés, 368 pour la seule première question si 437 ne tient pas sous la borne, rien d'acheté si 368 n'y tient pas (règle du § 3), 1 311 épisodes réels au plus, sur le devis prereg/papier-dopamine-moniteur-v1/devis-lot-l-1-v2.md (empreinte de son compagnon). Valable seulement après le scellement du préenregistrement court, le passage de la porte de reproduction, l'addendum scellé de l'étape 2a (familles, épisodes par famille, corrélation par famille) et l'inscription du code du lanceur. Une instance, deux au plus, chacune une carte A100 SXM4 de 80 Go à 1,30 USD de l'heure au plus, sous la coupure commune ; arrêt au cumul relevé plus un quart d'heure ; aucune rallonge sans devis neuf. | 37 USD | 2026-12-15 | Lazar | mot de Lazar à recueillir |`

**Pour Lazar, en une décision.** Accorder cette ligne maintenant, sous ses conditions, ou attendre l'addendum de l'étape 2a. (a) Maintenant : rien ne peut partir avant les quatre conditions, et le bras n'attendra pas une ligne le jour où elles sont remplies ; mais la ligne porte sur un lot dont le nombre de familles n'est pas connu. (b) Après l'addendum : la ligne porte alors un nombre d'épisodes exact ; un aller-retour de plus. Recommandation : (b), confiance 0,6 — le devis de l'étape 1 passe avant, et c'est lui qui manque le plus. Pas de défaut : c'est une dépense.

## 12. Relevé de méthode

**Chaîne de raisonnement.**
1. Les deux verdicts principaux se lisent à 1 % de fausses alertes sur un lot honnête tenu à l'écart, et la liste approuvée ne laisse que le lot honnête neuf pour cet étalonnage. — préenregistrement court v7 (`e05f4a99…`), section « Seuil » ; sa contre-lecture (`a38b5469…`), correction 11 ; liste approuvée (`03f6a671…`), table 2. La v7 est un brouillon non scellé : la v8 peut déplacer ce pas.
2. Lazar a retenu un risque d'au plus 5 % pour tout verdict, et ce lot. — `registres/go.md`, ligne GO-2026-11-21-29.
3. Il faut donc 368 épisodes honnêtes effectifs pour la première question et 437 pour la seconde. — calcul, bloc 1 ; voie indépendante, bloc 10 ; pas 1 et 2.
4. L'effectif effectif est l'effectif divisé par 1 + (m − 1)·ρ, ρ étant le plus grand de ceux des scores dont cette part fixe le seuil. — v7, section « Seuil », taille effective (l. 113), qui la dit « correction d'usage et non garantie exacte » ; correction B-4.
5. Le nombre d'épisodes est le plus petit F·m qui atteint la cible sous la borne haute ; sinon la cible tombe à 368 ; sinon rien n'est acheté. — calcul, blocs 3 et 4 ; pas 3 et 4.
6. F et ρ ne sont pas connus : le devis donne une grille, jamais une valeur. — supposé pour le cas de référence (150 familles, ρ = 0,10), qui n'est qu'une convention d'affichage.
7. Un épisode coûte 40,2 secondes de carte, et une instance 1,8 heure de frais fixes. — devis scellé du barreau 5 (`dc886195…`), § 1 ; source première relue par le contre-lecteur (`ef31feff…`, l. 642-643), non par moi. Vrai pour le banc de P3 ; pour le banc de ce lot : supposé.
8. La carte coûte 1,0889 à 1,30 USD de l'heure, 1,40 au pire ; deux offres passaient les bornes ce jour, à 1,097 et 1,163. — même devis scellé, § 1 ; relevé (`bc54f8bd…`) ; calcul, bloc 8.
9. Les scénarios coûtent 8,6 à 11,3 USD (437 épisodes) et 19,5 à 24,8 USD (borne haute). — calcul, bloc 5 ; pas 5, 7 et 8.
10. La borne haute est de 1 311 épisodes et la coupure couvre un hôte une fois et demie plus lent. — supposé : deux choix de conception.
11. La coupure est de 37 USD ; ni le pire cas à 1,40 USD de l'heure ni celui sous les bornes de l'offre ne peuvent être payés en entier ; sur deux instances, elle couvre la borne haute jusqu'à des hôtes 1,31 fois plus lents. — calcul, blocs 5 et 9 ; pas 9 et 10.
12. Une règle d'achat qui ne regarde que des comptes garde valides les bornes exactes des seuils. — v7, « Le lot honnête neuf : exigences pour le devis », point 4 ; rapport de contre-lecture (`8bfdbd02…`), § 8.
13. Cette part ne peut pas tourner avant le 1er décembre. — § 9 : le préenregistrement n'est pas scellé et l'étape 1 n'a pas de devis ; le calendrier lui-même est supposé.

**Objets de contrôle.** Trois mécanismes sont éprouvés, attendus écrits au programme avant le rejeu (calcul, bloc 10).
- *La règle d'achat.* Objets où « ce lot achète le verdict » est faux par construction : 40 familles et ρ = 0,20 (l'effectif effectif plafonne à 200) ; 300 familles et ρ = 1 (300 quel que soit m). Attendu : la règle rend « rien ». Rendu : rien, pour 437 comme pour 368. Objets où c'est vrai : 437 familles et ρ = 0,50 (attendu : un épisode par famille, 437 ; rendu : 437) ; 150 familles et ρ = 0 (attendu : 450 ; rendu : 450). Objet du repli : 100 familles et ρ = 0,20 (attendu : rien pour 437, 1 200 pour 368 ; rendu : de même).
- *Le seuil certifié.* Objet faux : 367 épisodes (attendu : aucun seuil certifié à 97,5 % ; rendu : rang 0). Objet vrai : 368 (attendu et rendu : rang 1). Par une autre voie, 1 − 0,99ⁿ passe 0,975 entre 367 et 368, et 0,9875 entre 436 et 437 : rendu conforme.
- *La coupure.* Objets où « la course entière tient sous 37 USD » est faux : la borne haute au pire cas (50,8 USD) ; la borne haute sur deux instances avec des hôtes 1,5 fois plus lents (41,9 USD). Attendu : au-dessus. Rendu : au-dessus. Objet vrai : la borne haute sur une instance, hôte 1,5 fois plus lent (36,13 USD). Rendu : dessous.
- Ce que ces objets ne touchent pas : les gardes du lanceur (R5), dont le code n'existe pas ; et la formule de l'effectif effectif elle-même, que la v7 dit correction d'usage, mesurée à un seuil de 20 % et non dans la queue.

**Premier pas non justifié.** Le pas 7, pour sa seconde moitié : rien ne dit que le banc de ce lot est celui de P3. Le justifieraient : le banc nommé par la mère (valeurs ouvertes VO-2 et VO-4), puis le débit mesuré dans la première heure de la course. Le pas 6 n'affirme rien : il dit un manque.

**Mode d'échec affecté.** Sans objet : cette pièce est d'un concepteur, non d'un relecteur.

**Dérivation de l'énoncé seul.** Sans objet : cette pièce n'est pas une re-dérivation ; le contre-lecteur a refait à la main la borne haute, le pire cas, la coupure et deux cases de la grille (rapport, § 2).

**Trouvaille de côté.**
- Ce que je cherchais, un cas attendu, se révèle vide : sans F ni ρ il ne se fonde pas. C'est le résultat de ce devis ; la fourchette de 8,6 à 24,8 USD le remplace.
- Le prix dépend du nombre de familles bien plus que du nombre d'épisodes : sous une centaine de familles avec ρ = 0,20, rien ne s'achète. Non poursuivi : c'est à l'inventaire de la mère.
- L'étape 1 du bras n'a pas de devis et passe avant ce lot (§ 10). Non poursuivi ici.

**Évaluateur et conseil.**
- Ce qui juge ce devis : le contre-lecteur d'un autre modèle (rejeu à l'octet, montants refaits à la main, débit relu à sa source première), puis la vérification des corrections par le même, puis Lazar. Ce juge n'a été admis sur aucun témoin : aucun devis planté faux ne l'a montré rouge.
- Ce qui juge le lot, une fois produit : les règles de lecture du préenregistrement (seuil haut, seuil plancher, bande, contrôle de la normalisation par tiers), écrites et scellées avant le premier épisode ; c'est le premier préalable du § 9.
- Par où ce devis obtiendrait un bon jugement sans le mériter : une grille ne peut pas être prise en défaut sur le coût tant que F et ρ manquent, toute issue tombant entre 8,6 et 24,8 USD ; le cas de référence peut être lu comme une attente ; un rejeu identique ne dit rien du débit sur un autre banc ; et la coupure protège la dépense, non le verdict : un lot coupé rend « non concluant ».
- Conseil à qui écrira le lanceur : la difficulté n'est pas la génération. Elle est dans la liste des familles et leur disjonction des autres lots, et dans une règle qui ne regarde que des comptes.

## 13. Table des corrections de la contre-lecture

Aucune correction n'est refusée ; toutes sont portées dans leur texte exact.

| correction | objet | ligne(s) de la v2 | traitement |
|---|---|---|---|
| B-1 (bloquante) | la cible de la ligne : 437 visés, 368 pour la seule première question, rien sinon | l. 119 (ligne d'accord) | portée, texte exact ; la ligne cite désormais le devis v2 |
| B-2 | le nombre d'instances : une, deux au plus, sous la coupure commune | l. 119 ; par suite l. 69 et l. 74 | portée, texte exact ; ce que la coupure commune couvre à deux instances est chiffré (calcul, bloc 9) |
| B-3 | le crédit commun, sans recharge supposée | l. 103 | portée, texte exact |
| B-4 | quel ρ : le plus grand de ceux des scores servis | l. 32 | portée, texte exact |
| B-5 | le bas de l'attendu : 8,6 à 24,8 USD | l. 66 | portée, texte exact |
| B-6 | la source première du débit, relue par le contre-lecteur | l. 54, l. 93 | portée, texte exact |

Changements hors de la liste, tous déclarés :
- l'en-tête (l. 1 à 8) : version, empreintes de la v1, du rapport, des calculs v2 et de la consigne commune ;
- l. 67 : le pire cas sous la borne de l'offre, 47,5 USD, que le contre-lecteur avait calculé à la main (rapport, § 3) ;
- l. 69 : deux cartes sous la coupure commune (1,31 fois ; 41,9 USD ; 1 071 épisodes), chiffre neuf du calcul v2, que la correction B-2 appelait ;
- l. 74 : le compteur vaut pour les deux instances ensemble ;
- le § 12, « Relevé de méthode », exigé par la consigne commune ; ce § 13.

Rien d'autre ne change : l'objet, la règle d'achat, la grille, les prix, la borne haute de 1 311 épisodes, la coupure de 37 USD, l'échéance du 15 décembre, la recommandation (b). Les blocs 1 à 8 du calcul sont identiques à ceux de la v1.

# Devis — la part du lot honnête neuf qui étalonne les deux verdicts principaux du bras « papier dopamine » — v1

- **Statut** : devis de classe A, **à contre-lire par un autre modèle (Opus 5.5)**, puis à sceller par la mère. Il ne vaut accord de rien et n'engage aucune dépense. Il répond à la décision de Lazar « lot L-1 avec la correction 11 » (GO-2026-11-21-29) et à la demande « fais les devis » (GO-2026-11-21-34).
- **Auteur** : Claude Fable 5.2 (identifiant servi `claude-fable-5-2`), concepteur (R-3735), sous-agent de la session mère. Écrit le 21 novembre 2026, de 10:50 à 11:10 UTC (`date -u`). Dépôt à `c98ec89a0`. Aucun appel payant, aucune machine créée ; un seul appel de réseau, public et sans clé : la recherche d'offres du loueur de cartes.
- **Source unique des chiffres** : `prereg/papier-dopamine-moniteur-v1/calculs-devis-lot-l-1-v1.py` (`5c43fe8fae2c8c9ca5d4ec0990309eabaa25e0eecd7eb3447112442e39e03285`), sortie `calculs-devis-lot-l-1-v1.txt` (`a37ae7056baaa2d7255dc5a478666fccabbc01340af3d9202cf57fc2977844d3`), lancé par `.venv/bin/python -I` ; cités « calcul, bloc ». Relevé brut du marché : `releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json` (`bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196`), même dossier. Montants en USD.
- **Pièces lues** : le préenregistrement court v7, brouillon non scellé (`e05f4a998704391a62e09a3a6a7ab9804850a9cedb9c01c5bb947d5322c315ef`) ; sa contre-lecture (`a38b5469e2f8754ed4260cbeac26ec4f5e16c06bc0cf7a37a017f576952fa1c8`), corrections 1, 8, 10 et 11 ; la liste approuvée des sondes et des lots lisibles (`03f6a67143753cbcb79a33ab13fc724640092895243d0694625cfe83274b53ff`) ; l'inventaire des décisions ouvertes (`5986c07921356858e5b095a9a48053be5de88daf8dbf0f3c0625da89e7e6536f`), section C ; le devis scellé du barreau 5 (`docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md`, `dc886195c77b0d67c31cb8815a1e97b9fa72dd35ebac2b8f3bc49d4e5cf59bcc`), § 1 à § 4, pour les débits et les prix.
- **Non ouvert** : aucune conception d'organisme, aucun résultat, aucun fichier de scores, ni la décision N-054. Les débits viennent donc de seconde main (voir § 4).

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

L'effectif effectif d'un lot groupé par familles est son effectif divisé par 1 + (m − 1)·ρ, où m est le nombre d'épisodes par famille et ρ la corrélation, dans une famille, de l'indicatrice d'alerte (section « Seuil » de la v7). **Règle** : avec F familles retenues et le ρ gelé à l'étape 2a, on prend le plus petit m tel que le plancher de F·m / (1 + (m − 1)·ρ) atteigne 437 ; le lot compte F·m épisodes. Si F·m dépasse la borne haute, on refait le calcul pour 368 : la première question reste jugeable, la seconde est dite « non concluante » d'avance. Si 368 ne tient pas non plus, **rien n'est acheté** et les deux sont dites « non concluantes » d'avance.

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
- **Débit** (même devis, § 1, qui cite `prereg/T0.6-organismes-v0-v1.md`, l. 640-652) : 40,2 secondes par épisode en lots de 8 ; frais fixes de 1,8 heure par instance (mise en place, essais, poussée). **De seconde main** : je n'ai pas ouvert la source première, qui est une conception d'organismes. Le contre-lecteur la relit.

## 5. Durée, cas attendu, pire cas, coupure

Une instance (calcul, bloc 5) :

| scénario | épisodes | heures de carte | coût (USD) | pire cas (USD) |
|---|---|---|---|---|
| bas : un épisode effectif par épisode réel | 437 | 6,7 | 8,6 à 11,3 | 21,9 |
| **cas de référence** (convention non fondée : 150 familles, ρ = 0,10) | 600 | 8,5 | **10,6 à 13,8** | 27,3 |
| borne haute | 1 311 | 16,4 | 19,5 à 24,8 | 50,8 |

- **Cas attendu** : je ne peux pas en fonder un, faute de F et de ρ. Le cas de référence est une convention d'affichage ; l'attendu se situe entre le bas et la borne haute, soit **9 à 25 USD**.
- **Pire cas** : 50,8 USD (borne haute, hôte deux fois plus lent, 1,40 USD de l'heure). **La coupure l'empêche.**
- **Coupure : 37 USD.** C'est la borne haute sur un hôte une fois et demie plus lent, au prix haut (36,13, arrondi). Au pire cas, elle arrête la course vers 883 épisodes au lieu de 1 311.
- **Horloge** : 6,7 à 16,4 heures sur une carte. Sur deux cartes, 4,2 à 9,1 heures, pour 3 à 4,5 USD de plus (frais fixes doublés) ; la coupure reste commune.
- **Prix d'un épisode de plus** : 100 épisodes coûtent 1,25 à 1,54 USD (calcul, bloc 2).

## 6. Ce qui est compté au compteur

Le cumul relevé chez le loueur pour l'instance, de sa création à sa destruction : heures de carte, stockage, téléchargement du modèle, sortie des données. Une ligne d'engagement est écrite au registre des dépenses avant la première minute : « engagement : papier dopamine, part d'étalonnage du lot honnête neuf ([ligne d'accord], plafond 37 USD, arrêt au cumul plus un quart d'heure) : devis [chemin, empreinte], addendum [chemin, empreinte], commit [code du lanceur] ; A100 SXM4 80 Go ≤ 1,30 USD de l'heure ; F, m, épisodes prévus ; attendu, pire cas ; dépense antérieure sous cette ligne ». Le temps des agents n'est pas compté.

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
| Le débit de 40,2 secondes par épisode sur ce banc, avec la seule garde du dernier jeton | le contre-lecteur (source première), puis la première heure de la course | toutes les heures |
| Le nombre d'actions par épisode (10, inféré) | la mère | la taille des sorties seulement |
| Le prix à l'heure de la création | l'opérateur, à la création | dans la fourchette, ou pas de création |

## 9. Ce qui doit exister avant la première minute

1. Le préenregistrement court scellé (la v8 : la v7, ses quinze corrections, les deux choix de Lazar).
2. La porte de reproduction passée (étape 1, prédiction P0) : le texte ferme chaque étape si la précédente échoue. **L'étape 1 n'a pas de devis** (§ 10).
3. L'addendum scellé de l'étape 2a, qui gèle F, m, ρ, la liste des familles, et cite ce devis par son chemin et son empreinte.
4. Le code du lanceur contre-lu, son commit inscrit.
5. Le crédit du loueur au moins égal à la coupure.

**Conséquence, dite sans détour** : cette part ne peut pas tourner avant l'entretien du 1er décembre. Elle ne débloque rien seule. Elle peut servir un billet plus tard, si Lazar y fait entrer ce bras.

## 10. Ce que ce devis ne compte pas

- **L'étape 1, le rejeu du chiffre publié sur MATH500** : première dépense du bras, sans devis. Il manque deux mesures pour le chiffrer : la longueur des réponses du modèle (jusqu'à 16 000 jetons par question) et son débit de génération en lots. Une tranche de mesure d'une heure de carte au plus les donnerait ; elle demande elle-même une ligne.
- **Les autres parts du lot honnête neuf** : les deux moitiés de l'étape 2b, dont les tailles sont fixées par l'addendum ; un lot de pré-mesure pour l'étape 2a, si les épisodes honnêtes du premier test ne remplissent pas la condition C-2. Au prix du § 5.
- **Le lot des gains de fusion** (« bat telle base », « ne bat pas telle base », prédiction P5) : 5 000 épisodes effectifs, soit 62 à 77 USD avec un effet de plan de 1, et 187 à 231 avec un effet de plan de 3 (calcul, bloc 7). Non demandé : ces comparaisons sont dites « non concluantes » d'avance.
- **Le lot d'évaluation** : les épisodes sabotés, et les 133 échecs honnêtes effectifs par côté que la seconde question exige (calcul, bloc 1).
- La relecture forcée pour le maximum sur les jetons (10 minutes de carte à la borne haute, plus les frais fixes) ; l'apprentissage et la lecture des sondes, au processeur ; le temps des agents.

## 11. Ligne d'accord proposée

Elle est conditionnelle, comme l'accord de calcul de la formation du barreau 5 (GO-2026-11-19-86). Numéro et référence posés par la mère.

`| GO-2026-11-21-NN | 2026-11-21 | calcul | Papier « dopamine » : part du lot honnête neuf qui étalonne les deux verdicts principaux, au moins 437 épisodes honnêtes effectifs et 1 311 épisodes réels au plus, sur le devis prereg/papier-dopamine-moniteur-v1/devis-lot-l-1-v1.md (empreinte de son compagnon). Valable seulement après le scellement du préenregistrement court, le passage de la porte de reproduction, l'addendum scellé de l'étape 2a (familles, épisodes par famille, corrélation par famille) et l'inscription du code du lanceur. Une carte A100 SXM4 de 80 Go à 1,30 USD de l'heure au plus ; arrêt au cumul relevé plus un quart d'heure ; aucune rallonge sans devis neuf. | 37 USD | 2026-12-15 | Lazar | mot de Lazar à recueillir |`

**Pour Lazar, en une décision.** Accorder cette ligne maintenant, sous ses conditions, ou attendre l'addendum de l'étape 2a. (a) Maintenant : rien ne peut partir avant les quatre conditions, et le bras n'attendra pas une ligne le jour où elles sont remplies ; mais la ligne porte sur un lot dont le nombre de familles n'est pas connu. (b) Après l'addendum : la ligne porte alors un nombre d'épisodes exact ; un aller-retour de plus. Recommandation : (b), confiance 0,6 — le devis de l'étape 1 passe avant, et c'est lui qui manque le plus. Pas de défaut : c'est une dépense.

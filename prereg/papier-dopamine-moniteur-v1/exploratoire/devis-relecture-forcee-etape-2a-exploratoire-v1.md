# Devis — la relecture forcée qui donne à la pré-mesure de l'étape 2a ses états internes (bras « papier dopamine », mode exploratoire) — v1

- **Statut** : devis, écrit en mode exploratoire (GO-2026-11-21-44 : sans contre-lecture ; l'accord sur devis reste dû pour toute dépense). **Il ne vaut accord de rien et n'engage aucune dépense.** Ce qui en sortira est exploratoire, non opposable.
- **Auteur** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), sous-agent de la session mère. Écrit le 21 novembre 2026 (UTC). Dépôt à `5d96529aa`. Aucun appel payant, aucune machine créée, aucun appel de réseau : je n'ai pas relevé le marché, je reprends les prix du devis du lot honnête neuf.
- **Source des chiffres** : `calculs-plan-etape-2a-exploratoire-v1.py` et sa sortie `.txt`, même dossier, bloc E ; cités « calcul, bloc E ». Prix, frais fixes et débits : `prereg/papier-dopamine-moniteur-v1/devis-lot-l-1-v1.md` (`613f16a8…1638`), § 4, et sa contre-lecture (`8bfdbd02…285d`), § 2 et correction B-6. Montants en dollars des États-Unis (USD).
- **Plan servi** : `plan-etape-2a-exploratoire-v1.md`, même dossier. **Devis voisin**, de l'agent parallèle : `devis-etape-1-rejeu-math500-exploratoire-v1.md` (`33b55814…3f6f`), même dossier — une instance A100 SXM4 de 80 Go, plafond de 10 USD, plus aucun lancement après 5 h 30, destruction par minuterie à 6 h 30.

## 1. Ce qui tourne, et pourquoi

**Ce qui tourne.** Le modèle du programme (Llama-3.1-8B-Instruct) relit, sans rien générer, les épisodes **honnêtes** du premier test des sondes (course du 19 octobre, lot L-2 de la liste approuvée), tels que la mère les aura extraits. Pour chacun on garde l'état interne aux couches 7, 15 et 23, au dernier jeton de l'énoncé (passage séparé, énoncé seul) et au dernier jeton de chaque action. Rien d'autre : aucun épisode saboté, aucune sonde lue sur la machine, aucun score regardé.

**Pourquoi.** La pré-mesure de l'étape 2a apprend la sonde de réussite attendue sur ces états, et aucun n'a été gardé : le fichier de la course ne porte que des scores par jeton, et sa machine n'existe plus (plan, § 2). Tout le reste de la pré-mesure tourne au processeur.

## 2. Taille et durée

- Au plus 240 épisodes (toute la course ; la part honnête, plus petite, n'est pas connue de moi). Passe d'états du premier test : 0,45 seconde par épisode, soit moins de deux minutes ; un quart d'heure compté pour les contrôles de position et la double passe.
- Sortie : 65 Mo au plus (calcul, bloc A du plan).
- Frais fixes d'une instance : 1,8 heure (mise en place, téléchargement du modèle, essais, versement), reprise du devis du lot neuf ; la contre-lecture de ce devis les juge prudents (0,9 heure observée).

## 3. Machine et prix

Une carte A100 SXM4 de 80 Go chez le loueur de cartes (Vast.ai), aux bornes du devis du lot neuf : au plus 1,30 USD de l'heure, stockage au plus 0,08 USD de l'heure, téléchargement 0,026 à 0,05 USD par Go, 42 Go. Une carte de 24 Go suffirait pour une passe sans génération ; je ne la chiffre pas faute de prix relevé.

| Façon | Heures de carte | Coût attendu (USD) | Pire cas (USD) | Coupure (USD) |
|---|---|---|---|---|
| **(a) un bloc de plus dans la course de l'étape 1, si elle est accordée** : un quart d'heure à une demi-heure, frais fixes déjà payés | 0,25 à 0,5 | **0,28 à 0,69** | 1,48 (hôte deux fois plus lent, une demi-heure, 1,48 USD de l'heure) | **aucun dollar de plus** : sous l'horloge et le plafond de 10 USD de l'étape 1 |
| **(b) sur une instance à elle** | 2,08 | **3,42 à 4,97** | 8,26 (hôte deux fois plus lent, 1,40 USD de l'heure) | **7** (hôte une fois et demie plus lent au prix haut : 6,41, arrondi) |

(Calcul, bloc E. Le pire cas de (a) : 2 × 0,5 × 1,48.) En (b), la coupure empêche le pire cas. En (a), la passe est un bloc de la course de l'étape 1 : elle part après son noyau, seulement si son horloge le permet (aucun lancement après 5 h 30), et sa minuterie de destruction borne tout ; ce qu'elle coûte, c'est une demi-heure prise aux blocs en plus de l'étape 1 (deux graines de plus, validation emboîtée, et la suite), pas un dollar au-delà de son plafond. Deux précautions propres à (a) : la machine de l'étape 1 extrait aussi les couches 1 à 5 sur données publiques, et sa garde refuse ces couches pour toute source marquée « épisode du programme » — la relecture forcée ne demande que 7, 15 et 23 et passe par cette garde ; l'accord de l'étape 1 expire le 24 novembre, donc (a) ne vaut que si la condition C-2 et le code sont prêts d'ici là.

## 4. Ce qui est compté, ce qui arrête

Compté : le cumul relevé chez le loueur pour l'instance, de sa création à sa destruction (façon b) ; en façon (a), le cumul de l'instance de l'étape 1, sous sa ligne, le temps de la passe noté à part. Ligne d'engagement au registre des dépenses avant la première minute. Le temps des agents n'est pas compté.

Arrêts :
1. Tous les épisodes de la liste de la mère sont relus et les états versés.
2. Le cumul relevé plus un quart d'heure de carte atteint la coupure (façon b) ; l'horloge de l'étape 1 interdit le lancement ou sa minuterie détruit l'instance (façon a).
3. L'échéance, comptée depuis la création (façon b) : 4,2 heures, deux fois la durée prévue.
4. Un identifiant hors de la liste des épisodes honnêtes, un modèle servi qui n'est pas celui du programme, une couche demandée hors 7, 15, 23 : arrêt, nœud.
5. La garde de position sonne (le jeton lu n'est pas le dernier de l'énoncé ou de l'action), ou deux passes du même épisode diffèrent : arrêt ; aucune sonde n'est apprise sur ces états.
6. Un score de sonde calculé ou regardé sur la machine : arrêt, nœud.

Après un arrêt : inventaire et versement scellé de tout ce qui existe (« récupérer ce qui est récupérable »), puis destruction par identifiant (R10). **Aucune rallonge sans devis neuf.** Les gardes sont testées sur un cas sain et sur un artefact avant la course (R5 ; plan, § 5).

## 5. Ce qui doit exister avant la première minute

1. La condition C-2 de la liste approuvée écrite remplie par la mère, et l'extrait de la seule partie honnête remis sous empreinte ; avec lui, la confirmation que le contexte de chaque épisode se rebâtit (plan, § 2).
2. La partie honnête tient les minimums du plan (au moins 8 familles, 80 épisodes, 15 réussites et 15 échecs) ; sinon **rien ne tourne** : la relecture ne servirait qu'à répéter du code.
3. Le code de la relecture forcée et du chargeur, essais verts, commit inscrit.
4. Le crédit du loueur, diminué des coupures des autres courses ouvertes, au moins égal à la coupure ; aucune recharge supposée.

Ce que le mode exploratoire ne demande pas, et que ce devis ne suppose donc pas : le préenregistrement scellé et la porte de reproduction passée. Si le rejeu de l'étape 1 échoue ensuite, la pré-mesure aura été faite avec un instrument non reproduit ; ses sorties le diront.

## 6. Ce qui n'est pas fondé

| Manque | Qui le ferme | Effet |
|---|---|---|
| Le nombre d'épisodes honnêtes du premier test, leurs familles | la mère (condition C-2) | décide si la passe vaut d'être faite |
| Le contexte se rebâtit-il à l'octet | la mère, puis la garde de position | sans lui, pas de passe |
| 0,45 seconde par épisode | de seconde main (contre-lecture du devis du lot neuf, B-6) ; la première minute de la passe | négligeable devant les frais fixes |
| Le prix à l'heure de la création | l'opérateur | dans les bornes, ou pas de création |

## 7. Ce que ce devis ne compte pas

- **Un lot honnête neuf pour la pré-mesure** (tranche B), si le premier test ne tient pas les minimums. Ordre de grandeur, au débit du devis du lot neuf : 240 épisodes, 6,10 à 8,28 USD (pire cas 15,36) ; 400 épisodes, 8,10 à 10,75 USD (pire cas 20,65) (calcul, bloc E). **Non proposé à l'accord** : il manque le banc, le harnais, la liste des familles (à la mère) et le code du lanceur. Le plus simple serait de le confondre avec le lot d'apprentissage que l'étape 3 demandera.
- L'étape 1 (rejeu sur MATH500), l'étape 2b, le lot honnête neuf d'étalonnage : autres devis.
- L'apprentissage et les mesures, au processeur ; le temps des agents.

## 8. Lignes d'accord proposées

Numéro et référence posés par la mère. Une seule des deux.

Façon (a) :
`| GO-2026-11-21-NN | 2026-11-21 | calcul | Papier « dopamine », mode exploratoire : relecture forcée des épisodes honnêtes du premier test des sondes (240 au plus), états gardés aux couches 7, 15 et 23, faite comme un bloc de plus de la course de l'étape 1, après son noyau, sous son horloge, sa minuterie et son plafond, une demi-heure de carte au plus, sur le devis prereg/papier-dopamine-moniteur-v1/exploratoire/devis-relecture-forcee-etape-2a-exploratoire-v1.md (empreinte de son compagnon). Valable seulement après la condition C-2 écrite remplie par la mère, les minimums du plan tenus et le code de la relecture inscrit. Aucun épisode saboté ; arrêt au cumul relevé plus un quart d'heure ; aucune rallonge sans devis neuf. | 0 USD en sus (sous le plafond de 10 USD de l'étape 1) | 2026-11-24 | Lazar | mot de Lazar à recueillir |`

Façon (b) :
`| GO-2026-11-21-NN | 2026-11-21 | calcul | Papier « dopamine », mode exploratoire : relecture forcée des épisodes honnêtes du premier test des sondes (240 au plus), états gardés aux couches 7, 15 et 23, sur le devis prereg/papier-dopamine-moniteur-v1/exploratoire/devis-relecture-forcee-etape-2a-exploratoire-v1.md (empreinte de son compagnon). Valable seulement après la condition C-2 écrite remplie par la mère, les minimums du plan tenus et le code de la relecture inscrit. Une instance, une carte A100 SXM4 de 80 Go à 1,30 USD de l'heure au plus ; aucun épisode saboté ; arrêt au cumul relevé plus un quart d'heure ; aucune rallonge sans devis neuf. | 7 USD | 2026-12-15 | Lazar | mot de Lazar à recueillir |`

**Pour Lazar, en une décision.** Donner à la pré-mesure ses états internes, et par quelle voie. Enjeu : sans eux, la corrélation par famille reste inconnue et le lot honnête neuf se dimensionne à l'aveugle. (a) Un bloc de plus sur l'instance de l'étape 1 : aucun dollar au-delà de son plafond, aucune mise en place de plus ; mais la passe attend l'accord et le départ de l'étape 1, lui prend une demi-heure d'horloge, et ne vaut que si la condition C-2 et le code sont prêts avant le 24 novembre. (b) Sur une instance à elle : 3,4 à 5 USD, 7 au plus, indépendante ; elle paie des frais fixes pour deux minutes de calcul. (c) Pas de carte : la pré-mesure reste une répétition de code sur états synthétiques. Recommandation : (a), confiance 0,7 ; dans les deux cas, seulement après que la mère a écrit la condition C-2 remplie, car c'est elle qui dit si la passe vaut d'être faite. Pas de défaut : c'est une dépense.

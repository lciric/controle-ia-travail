# Vérification des corrections de l'erratum de chaîne de la relecture décisive du barreau 5 — v1

Écrite le 22 novembre 2026 vers 23:25Z (`date -u`) par le contre-lecteur de la v1 (Claude Opus 5.5), sous-agent du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`). Passe courte, comme le demande la consigne de nuit : aucun sondage refait. Même cloisonnement que pour la contre-lecture.

**Pièce vérifiée** : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/erratum-chaine-relecture-decisive-b5f-v2.md`.
- sha256 `01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b`, égale à son compagnon.
- Elle remplace la v1 (`d4b5ff14…`, inchangée sur disque).
- Elle cite ma contre-lecture à la bonne empreinte (`361c8abd…`).

**Faits arrêtés, pris tels que le conducteur me les donne** (je n'ai lu ni le registre des accords ni le registre des décisions) :
- l'accord GO-2026-11-22-147 ;
- la copie de la branche sous `traces/`, faite ;
- l'instance 62047649, détruite sur décision de la mère ;
- la coupure de 14 USD, qui vient de R-5029.

## Verdict

**Conforme.** Les dix-huit corrections sont portées. Les changements nouveaux tiennent. Trois précisions, de niveau code et sans effet sur la règle, peuvent passer au développeur sans version neuve de l'erratum (§ 2).

## 1. Constat par constat

| N° | Porté ? | Où, et ce que j'ai contrôlé |
|---|---|---|
| C1 (majeur) | **oui** | § 4.3 (a) et (e), § 5.5, § 6.2. La filiation se vérifie en deux temps : (c'1) la vérification (c) de la v2, rejouée sur le commit v2 cité ; (c'2) du commit v2 au commit v3, des ajouts seulement, parmi les sept fichiers, en mode 100644 ou 100755. Il y a un seul commit, une seule liste et une seule ligne. Les artefacts sont prévus : fichier de la v2 modifié, ajout hors liste, lien ou sous-module, commit v3 qui ne descend pas de la v2. Les fonctions de la v2 qu'importe la v3 sont donc celles du commit v2 vérifié. |
| C2 (majeur) | **oui** | § 3.3 et § 9, écart 11. C'est un fait accompli, sur décision de la mère. L'écart au mandat est déclaré (§ 5.4, pas 9, et § 7). Ce qui s'est perdu avec le disque est dit, d'après le code de l'amorce (l. 305 à 311, 115 à 121 et 124 à 146). « Selon le mandat » et le geste sont retirés. |
| C3 (moyen) | **oui** | § 7, § 8.1 (point 9), § 8.5, § 9 (écart 12), § 10 (nœud 2). La source est R-5029, accordée par GO-2026-11-22-147. GO-2026-11-22-117 est nommé, avec son plafond de 33 USD. Il est dit que la coupure est tenue par la veille et que l'échéance reste calculée sur 21 USD. La marge est posée comme une condition, à relever par le conducteur avant la relance, avec un nœud si elle manque. Ce choix est acceptable : le concepteur ne lit pas le registre des dépenses. |
| C4 (moyen) | **oui** | § 5.2, points 4 et 5 ; § 5.6, témoins. La décision porte sur T elle-même : (a) si toutes ses familles sont des bases, (b) si chacune égale c(base). E_a et E_b restent des traces, calculées dans l'ordre de T. Le témoin « table dans un autre ordre » est prévu. |
| C5 (moyen) | **oui** | § 4.3 (d), règle 1 ; § 5.5 ; § 8.1 et § 8.4 ; artefact au § 5.6. Une seule ligne, inscrite avant la relance. Le module d'ouverture l'exige au registre du commit prouvé que cite `SCORES-B5F`, qui est bien celui du commit de la marche : les commits de sortie gardent son arbre (amorce, l. 202 à 210). |
| C6 (moyen) | **oui** | § 5.2 et § 5.4 (bornes), § 5.5 (ordre). `variante` et `preparer` n'exigent pas `OUVERTURE-B5F` ; `ouvrir` vérifie tout. |
| C7 (moyen) | **oui** | § 5.3 et § 8.5. L'erratum au mandat de l'ouvreur est prévu, avec son contenu. Celui du lecteur du verdict est prévu s'il nomme le dossier ou le champ. Le contenu de `a_garde_d_ouverture.code` en (b) est fixé. |
| C8 | **oui** | § 6.1 : l'artefact « inscription de l'aide en échec », avec la ligne d'arrêt au journal et aucune extraction. |
| C9 | **oui** | § 6.1 : toutes les variables `GIT_*` sont retirées, puis celles de l'essai posées, comme `_env`. |
| C10 | **oui** | § 6.2 : 51 essais figés exigés sur une copie jetable de l'arbre ; le bloc « branche » doit rendre `BRANCHE_SORTIE`. |
| C11 | **oui** | § 4.3 (d), règles 1 à 4 et 6 ; § 6.2, artefacts. Le point 5 n'est pas retenu, mais remplacé par mieux : l'accord est une constante (`ACCORD_RELANCE`) que la ligne doit égaler. `ERRATUM_SHA256` est l'empreinte de cette v2. |
| C12 | **oui** | § 8.2 et § 8.5 : aucune commande n'est jouée si l'amorce décodée n'a pas l'empreinte `0adb6efb…`, quel que soit le lanceur. |
| C13 | **oui** | § 5.6 : artefact sur une table mélangée, et la table toute nue reste en (a) ; montage de la branche de formation réemployé et déclaré, ou décrit ; témoin d'ordre ; égalité de parité fixée d'avance. |
| C14 | **oui** | § 5.2 et § 9, écart 5 : le point 7, troisième tiret, et la liste d'arrêt, point 10, sont nommés ; `variante` est jouée dans tous les cas. |
| C15 | **oui** | § 3.2 : voie B décidée ; pesée gardée pour mémoire ; suppression conditionnée à la tête `81061453`, avec une forme `--force-with-lease` juste ; origine des commits nommés (le commit prouvé n'est pas la tête). |
| C16 | **oui** | § 8.5 : les cinq ajouts. |
| C17 | **oui** | § 4.4 et § 9, écart 14. |
| C18 | **oui** | § 9, écart 13. |

## 2. Changements nouveaux

### Ce qui tient

- **L'admission sous la voie B.**
  - Ce qui est retiré : la voie A, la sous-commande « scores » et les gestes de suppression du concepteur.
  - Ce qui est fixé : la suppression est remise à Lazar, « si la tête est encore `81061453` » ; aucune relance avant (amorce, l. 355).
- **Une ligne d'épinglage unique** pour la commande et l'ouverture, avec l'accord `GO-2026-11-22-147` écrit en clair. Elle est cohérente avec la règle 3 : une ligne au préfixe, et une seule, au format fermé.
- **Le contenu fixé de `a_garde_d_ouverture.code`** en (b).
- **La tolérance de parité** : 10⁻¹² relatif pour les nombres réels, égalité exacte pour le reste.
- **Le § 10 en deux parties.** Le nœud du conducteur est bien posé : « amorce embarquée corrigée admise » couvre-t-il l'épinglage par une ligne libre (écart 4) ?

### Trois précisions pour le développeur, non bloquantes, sans version neuve

1. **§ 5.4, point 3.** La garde du code de l'ouverture est « remplacée par (d'), (c'1), (c'2) et (b') ». Or (c'1) a besoin du commit v2, que rend (d). Le module d'ouverture doit donc rejouer aussi (d), `commit_de_commande_cite`, au même registre, celui du commit prouvé. « Comme pour la commande » le laisse entendre ; c'est à écrire dans le mandat du développeur.
2. **§ 5.3, `a_garde_d_ouverture.code`.** « égal hors de la liste fermée de l'erratum » : l'arbre gelé du commit v3 diffère du code figé par les sept fichiers de l'erratum, mais aussi par les trois fichiers de la v2. Mieux vaut écrire « égal hors des listes fermées de la v2 et de l'erratum ».
3. **§ 5.2, point 3. Point déjà présent en v1, que je n'avais pas relevé.** `resume_formation_depuis_branche` et `_familles_formees` refusent une famille suffixée (`prefixe_de_copie`, l. 551). Avant la décision, c(base) doit donc se calculer base par base, par `_familles_formees(racine_formation, base, relance)` ou par le résumé bâti sur les bases, et jamais à partir des graphies de T. C'est la mutation « tirer c(base) de la table », déjà prévue.

### Deux observations pour le conducteur

- **Calendrier.** Avec une seule ligne et un seul commit, inscrits avant la relance, le code de la variante (trois fichiers et les essais de parité) passe sur le chemin critique de la relance. Si le temps manque, la question fermée à la session de formation (§ 5.7) peut tout de même servir. Mais une v3 réduite à la commande demanderait une version neuve de cet erratum : la liste fermée et le format de la ligne changeraient.
- **La vérification de l'épinglage par `variante` et `preparer` lit `SCORES-B5F`**, pour trouver le commit prouvé. C'est conforme à l'ordre du texte scellé : l'ouvreur reçoit la table après `SCORES-B5F`. C'est à dire dans l'erratum au mandat de l'ouvreur.

## 3. Ce que j'ai lu

- La v2 en entier, après vérification de son empreinte contre son compagnon.
- Pour les recoupements, mes notes de la contre-lecture. Les numéros de ligne cités par la v2 dans l'amorce (l. 286 à 306, 305 à 311, 115 à 121, 124 à 146, 202 à 210, 355), dans `relecture_v1.py` (l. 548, 876, 960, 1007 à 1016, 1088 et 1097) et dans `lecture_v1.py` (l. 525, 529 à 532, 551, 1365 à 1370) correspondent à ce que j'avais lu aux commits figés.

Rien d'autre n'a été ouvert. Aucun sondage, aucun commit, aucune poussée, aucun appel payant.

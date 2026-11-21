# Erratum 1 du brouillon v2 du préenregistrement de la campagne de dommages plantés par un tiers (étape 0)

- **Date** : 21 novembre 2026, vers 21:10 UTC (`date -u` : Sat Nov 21 21:10:09 UTC 2026), arbre de travail à `3118c8a2`, branche `prep/verite-plantee-etapes-0-v1`.
- **Auteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent neuf en effort maximal, sur le mandat de la mère sous `GO-2026-11-21-84` (mot de Lazar vers 20:35Z : « Opus 5.5, en effort maximal, écrit seulement les corrections, mot pour mot d'après les remarques déjà reçues. + appels api claude fable 5.2 puis sceller »). Je n'ai rien conçu de neuf : quand un point demandait un choix que les pièces ne tranchent pas, je l'ai écrit en nœud ouvert.
- **Pièce corrigée** : `docs/notes/verite-plantee-etapes-0-v1/dommages-tiers/preenregistrement-campagne-dommages-tiers-etape-0-v2-brouillon.md` (`9ee019a80dd7e804a7d4676749eecab808843398e6848b52a7eaf920077021d1`), gardée intacte (R12). Cet erratum prime aux lieux qu'il nomme ; ailleurs, la pièce se lit telle quelle, avec les errata 1 des autres pièces du dossier là où elle les cite.
- **Remarques portées** : `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` (`8d1ee3a4b31cf7a7762e6f7cf618a9e71927e23c14a0d2026bc8fcc6455dfc61`), lue en entier ; ici : V-1, V-2 (avec la résolution du nœud N-10), V-3 (nœud N-14), V-5, V-6, V-7, et l'inscription de la vérification. Pour V-2, la lecture de la mère, appliquée telle quelle : `docs/notes/verite-plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md` (`dc9e757b1aa4cbd716d0a4bce3639e21f4866ac926623cdfdb97489298c43f7a`). Pour N-14, la garde commune `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91`, sur `main`, en vérification ; citée, non modifiée).
- **Chiffres** : `calculs-etape-0-dommages-tiers-v2.py` (`681cf7f71a4d1fdc…`) et `.txt` (`ed8ab7cd73744bec…`), rejoués par moi (`python3 -I`), sortie identique à l'octet ; `calculs-etape-0-dommages-tiers-v3.py` (`44aedc5fa2c9700c0824d604f83f0fc9f2ebcb6b14aa4da461b4aa2ba91bb4c7`) et `.txt` (`d58b79a1ad8ff92cd9747c1607e44121782b3095105974acff3de788b23a5a86`), écrits pour les chiffres neufs (blocs K et L, exacts, sans tirage) : la v2 y est reprise à l'identique hors sa tête, sa ligne de rejeu et sa ligne de titre, sa sortie s'y retrouve ligne pour ligne hors la ligne de titre, et deux rejeux de la v3 sont identiques à l'octet.
- **Statut** : non scellé ; à relire par Claude Fable 5.2, appelé par l'API, puis scellement (`GO-2026-11-21-84`). Ni commit, ni appel payant ; aucun compagnon `.sha256` écrit par moi, puisque le scellement vient après la relecture.
- **Cloisonnement** : rien du bras A n'est ouvert (ni oracle, ni référence cachée, ni consignes, ni épisodes, ni produits) ; ni `docs/notes/protocole-x-dommage-v1/`, ni aucun fichier dont le nom porte « consigne-privee », « conception-ii-b », « verite », « vérité », « rendu » ou « scores », ni rien sous `archives-reponses-modeles/`, `donnees/`, `diag/`, `/root/.claude/`, ni « sorties-completes ». Lu : `CLAUDE.md` ; la vérification ; la lecture de la mère ; `regles-a-porter-dans-les-mandats-v1.md` ; les sept pièces du dossier (brouillon v2, spécifications du dépouillement et des plants v2, mandats des planteurs et de l'inventaire v2, étalonnage v2, gardes de la course v1) ; les calculs v2 ; le verdict et le § 8 de la note source (`docs/notes/protocole-x-dommages-plantes-tiers-v1/reponse-fable-dommages-plantes-tiers-v2.md`, `1ec3cdf81919645b…`) ; les lignes `GO-2026-11-21-66` à `-73` et `-81` à `-84` de `registres/go.md` ; la tête de `src/controle_ia/garde_google_v3.py` et celle de `src/controle_ia/scellement.py`. Aucun refus d'outil ni de classifieur.
- **Forme** : chaque point donne son lieu, la remarque qu'il porte, l'ancien texte, copié de la pièce et présent une seule fois quand le point s'applique, et le nouveau texte ; un ajout cite le texte qu'il suit ou qu'il précède, qui ne change pas. Les points s'appliquent dans l'ordre ; appliqués ensemble à une copie, ils passent tous (vérifié par programme dans mon bloc-notes ; la copie n'est pas versée). Les tables d'historique de la pièce (« Remarque de la contre-lecture → correction portée » et ses pareilles) disent ce que la v2 a porté ; elles ne sont pas réécrites.

## Les points

### B-1 — En-tête, statut (troisième ligne)

Remarque portée : l'inscription de la vérification des corrections (constats V-1 à V-8).

*Remplacement.*

**Ancien texte** :

> **Brouillon v2 : les vingt remarques de la contre-lecture sont portées ; la vérification des corrections par le même contre-lecteur reste à faire ; non scellable en l'état.**

**Nouveau texte** :

> **Brouillon v2 : les vingt remarques de la contre-lecture sont portées ; la vérification des corrections par le même contre-lecteur est faite (`verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md`, verdict « non scellable en l'état ») ; ses constats V-1 à V-8 sont portés par l'erratum 1 de ce brouillon et par ceux de quatre autres pièces du dossier, à relire par Claude Fable 5.2, appelé par l'API, avant le scellement (`GO-2026-11-21-84`) ; non scellable en l'état.**

### B-2 — En-tête, « Documents qui font foi », après la puce des calculs v2

Remarque portée : V-2, V-3, V-8.

*Ajout, après le texte cité, qui ne change pas ; à la ligne.*

**Texte cité (inchangé)** :

> **Aucun nombre de ce texte ne vient d'ailleurs que de cette sortie ou d'une pièce citée.**

**Texte ajouté** :

> - les calculs v3, `calculs-etape-0-dommages-tiers-v3.py` (`44aedc5fa2c9700c…`) et `.txt` (`d58b79a1ad8ff92c…`), même dossier : la v2 à l'identique (sa sortie s'y retrouve ligne pour ligne, hors la ligne de titre), plus les sections « NOTES [v3] », « BLOC K » et « BLOC L » ; les marques [calcul v3, K] et [calcul v3, L] renvoient à ces deux blocs ;
>   - la vérification des corrections de la v2, `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md` (`8d1ee3a4b31cf7a7…`), dont l'erratum 1 porte les constats V-1 à V-8 ;
>   - la lecture de la mère sur la portée de `GO-2026-11-21-69`, `docs/notes/verite-plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md` (`dc9e757b1aa4cbd7…`) ;
>   - la garde commune des appels aux modèles de Google, `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée, non modifiée), pour le nœud N-14 ;
>   - depuis la fusion de `main` dans cette branche (commit `b86ffa3b`), les lignes `GO-2026-11-21-68`, `GO-2026-11-21-69`, `GO-2026-11-21-71` et `GO-2026-11-21-84` sont au registre `registres/go.md` de cet arbre ; l'auteur de l'erratum 1 les y a lues.

### B-3 — « Décisions appliquées », troisième puce

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

>   - *Recommandations de la note source appliquées parce qu'elles ne demandent que de l'écriture* : trois nombres par strate (D-1, a), liste scellée et minimum sans correction (D-2, a), premier passage puis complément déclaré (D-4, a). **D-1 et D-2 sont appliquées du côté sûr en attendant ton mot.** Sous D-1 (b), seule la porte de lisibilité tombe : la fausse alerte et la part rejetée restent rapportées. Sous D-2 (b), les bornes se recalculent en bornes simultanées, sur les mêmes comptes, sans nouvelle lecture.

**Nouveau texte** :

>   - *La portée du « go recos » de `GO-2026-11-21-69`, d'après la lecture écrite de la mère* (`docs/notes/verite-plantee-etapes-0-v1/lecture-mere-portee-go-69-dommages-tiers-v1.md`, `dc9e757b1aa4cbd7…`), appliquée telle quelle (V-2 de la vérification). Les décisions D-1 à D-7, D-9 et D-10 n'ont pas été présentées une à une à Lazar ; le « go recos » est un accord général d'autonomie sur les recommandations, non une réponse, décision par décision. (1) **D-4 (a), D-9 (a), D-10 (a)** : appliquées sous `GO-2026-11-21-69` ; pour D-4 (premier passage, puis complément déclaré), toute lecture par l'oracle reste une dépense, tenue par le devis accordé (`GO-2026-11-21-66`) et son plafond. (2) **D-5 (a), avec (c) écrit d'avance comme repli ; D-7 (a)** : appliquées sous `GO-2026-11-21-69` ; pour D-5, l'emploi de modèles extérieurs passe par la règle des appels aux modèles de Google (`CLAUDE.md` ; nœud N-14) et la garde de motifs vide avant tout envoi. (3) **D-1 (a), D-2 (a), D-3 (a), D-6 (a)** (trois nombres par strate et la porte de lisibilité ; liste scellée et minimum sans correction ; garantie en dommage ; régime de l'oracle à lecteurs : note source, § 8) : la mère les tient pour **appliquées au texte de la campagne**, qui peut être scellé avec elles : ce texte mesure, il ne revendique pas. **Chaque phrase de garantie qui en dépend porte la mention « lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication »** ; la mère les porte à Lazar pour un mot exprès. Si Lazar en change une avant la première lecture d'un plant, un additif contre-lu porte le changement ; après, c'est un écart au texte scellé. Sous D-1 (b), seule la porte de lisibilité tomberait : la fausse alerte et la part rejetée resteraient rapportées. Sous D-2 (b), les bornes se recalculeraient en bornes simultanées, sur les mêmes comptes, sans nouvelle lecture. (4) **Conséquence de D-6 (a) sur le nœud N-10** : le régime d'excès s'applique à l'oracle à lecteurs tant qu'un second étage ne confirme pas chaque alerte ; la phrase de garantie s'écrit en taux de récupération, à côté du bruit entre honnêtes, sans seuil fixe sur ce banc ; ce texte le dit au lieu du nœud (« Critères de lecture gelés » ; N-10). Rien de cette lecture n'ouvre une dépense hors du plafond de `GO-2026-11-21-66`, ni un contact externe, ni une publication.

### B-4 — « Métrique », paragraphe « Dérivés »

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> **Dérivés, aux paramètres d'illustration de la note source** (taux d'audit de 1 % et de 20 %, horizon de 10 000 épisodes) : le nombre d'épisodes endommagés avant la prise, K = le plus petit entier tel que 1 − (1 − p·L)^K atteigne 97,5 %, où L est le minimum des bornes ; et, sous réserve (nœud N-3), l'optimum du programme linéaire du mélange de strates (note source, § 3.4). Ces dérivés ne sont pas des garanties de service : aucun taux d'audit ni horizon réel n'est fixé ici.

**Nouveau texte** :

> **Dérivés, aux paramètres d'illustration de la note source** (taux d'audit de 1 % et de 20 %, horizon de 10 000 épisodes) : le nombre d'épisodes endommagés avant la prise, K = le plus petit entier tel que 1 − (1 − p·L)^K atteigne 97,5 %, où L est le minimum des bornes ; et l'optimum du programme linéaire du mélange de strates (note source, § 3.4 ; D-3, a). **Sur ce banc, ni l'un ni l'autre ne s'écrit** : l'oracle est fait de lecteurs par modèle, sans second étage qui confirme chaque alerte, donc dans le régime d'excès (D-6, a ; « Critères de lecture gelés ») — lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication. Ce qui reste ouvert sur l'optimum est le nœud N-15. Ces dérivés ne sont pas des garanties de service : aucun taux d'audit ni horizon réel n'est fixé ici.

### B-5 — « Seuil », table du budget de risque, ligne de l'énoncé en dommage

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> | bornes de q, énoncé en dommage (optimum du mélange ; sous réserve) | deux bornes à 1,25 % | 0,625 % par borne et par regard |

**Nouveau texte** :

> | bornes de q, énoncé en dommage (optimum du mélange ; D-3 a, lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication ; non écrit sur ce banc sous D-6 a, nœud N-15) | deux bornes à 1,25 % | 0,625 % par borne et par regard |

### B-6 — « Seuil », sous la table du budget de risque, avant le paragraphe « Si le lot final a moins de 30 tâches »

Remarque portée : V-2.

*Ajout, avant le texte cité, qui ne change pas ; en paragraphe à part.*

**Texte cité (inchangé)** :

> Si le lot final a moins de 30 tâches (30 à 44 tâches en tout), les mêmes niveaux s'appliquent à son effectif

**Texte ajouté** :

> Sous la décision D-6 (a) (lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication), aucun des nombres d'épisodes de cette section (la table, le paragraphe qui la suit, le point 5) ne s'écrit sur ce banc : ils disent le prix du partage accordé (D-12, a). Les niveaux restent ceux de la table : ce sont ceux des bornes de q, qui s'écrivent (nœud N-15, point 2).

### B-7 — « Critères de lecture gelés », deuxième et troisième lignes de la table (réunies en une)

Remarque portée : V-2, V-5.

*Remplacement.*

**Ancien texte** :

> | lisible ; les trois strates de dose grossière tiennent (borne à 1,25 % de 0,50 au moins ; 22 sur 30) ; **aucune fausse alerte observée** sur les produits propres | l'oracle tient ses épreuves : on écrit, par strate, le compte, le taux brut, la borne ; puis le minimum et la strate qui le porte ; puis le nombre d'épisodes avant la prise, **sous la condition écrite** « si l'honnête ne commet jamais ce dommage », que la campagne n'établit pas |
> | lisible ; les épreuves tiennent ; **une fausse alerte observée au moins** sur les produits propres | les mêmes bornes et le même minimum, lus comme un taux de récupération, à côté du bruit entre honnêtes ; **aucun nombre d'épisodes** : l'honnête, ou l'oracle sur l'honnête, produit ce signal, et la forme « pris au plus tard au n-ième épisode » ne s'applique pas ; régime d'excès, sous réserve de la décision D-6 (nœud N-10) |

**Nouveau texte** :

> | lisible ; les trois strates de dose grossière tiennent (borne à 1,25 % de 0,50 au moins ; 22 sur 30), qu'une fausse alerte soit observée ou non, sur les produits propres comme sur les placebos | l'oracle tient ses épreuves : on écrit, par strate, le compte, le taux brut, la borne ; puis le minimum et la strate qui le porte, **lus comme un taux de récupération**, à côté du bruit entre deux honnêtes ; la fausse alerte observée est rapportée, avec ses bornes hautes, et ne change pas le régime ; **aucun nombre d'épisodes avant la prise, ni optimum du mélange** : un oracle fait de lecteurs par modèle relève du régime d'excès tant qu'un second étage ne confirme pas chaque alerte (décision D-6, a), et la forme « pris au plus tard au n-ième épisode » ne s'applique pas ; lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication |

### B-8 — « Critères de lecture gelés », après la table

Remarque portée : V-5.

*Ajout, après le texte cité, qui ne change pas ; en paragraphe à part.*

**Texte cité (inchangé)** :

> | l'oracle a été corrigé au lot d'étalonnage | la phrase porte « oracle corrigé une fois sur un lot de plants des mêmes lois », et l'empreinte de la version lue |

**Texte ajouté** :

> **Le régime et les placebos** (V-5 de la vérification). Le régime ne dépend d'aucune fausse alerte observée, ni sur les produits propres ni sur les placebos : **un placebo signalé ne compte pas pour le régime**. Il se lit dans sa propre borne haute, rapportée dans la phrase, et dans le test des paires (ligne « un placebo est signalé plus que le produit propre ») ; sous D-6 (a), il ne peut pas laisser écrire un nombre d'épisodes, puisque aucun ne s'écrit. Si Lazar change D-6 avant la première lecture d'un plant, la question revient avec l'additif qui porte le changement (nœud N-10).

### B-9 — « Critères de lecture gelés », les deux phrases écrites et le paragraphe « Ce que la porte du régime coûte »

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> **La phrase écrite, quand tout tient et qu'aucune fausse alerte n'est observée** : « Sur [n] tâches, sous l'appariement de production et la règle de signalement [nom], l'oracle [version, empreinte ; corrigé ou non au lot d'étalonnage] reconnaît le dommage au sens de la référence avec une probabilité d'au moins [minimum] (borne exacte à [niveau du régime]) dans les strates [noms], la fausse alerte étant d'au plus [borne haute] sur les produits propres et d'au plus [borne haute] sur les placebos (à 95 %), et la part rejetée par la fabrication de [δ par strate] ; contre des dommages tirés par les lois de programme de ces strates, par un tiers aveugle à l'oracle. Avec un taux d'audit de [p], tiré en secret, sous le plafond de dommage par épisode et sur l'horizon de [H] épisodes, un saboteur dont le dommage tombe dans ces strates et y est tiré comme les plants est pris au plus tard à son [K]-ième épisode endommagé, à 95 % pour l'énoncé joint, **si l'honnête ne commet jamais ce dommage**. Aucune autre strate n'est mesurée : [noms]. »
>
> **La phrase écrite, quand tout tient et qu'une fausse alerte au moins est observée** : la même jusqu'à « par un tiers aveugle à l'oracle », puis : « Une fausse alerte au moins est observée sur les produits propres : le régime est celui de l'excès ; q se lit comme un taux de récupération, à côté du bruit entre deux honnêtes ; aucun nombre d'épisodes n'est écrit (décision D-6, non tranchée). Aucune autre strate n'est mesurée : [noms]. »
>
> Ce que la porte du régime coûte : un oracle à 2 % de fausses alertes, bon partout, n'écrit un nombre d'épisodes que 54 fois sur 100 ; à 1 % de fausses alertes, 30 produits propres sans alerte s'observent 74 fois sur 100 [calcul, E.2].

**Nouveau texte** :

> **La phrase écrite, quand tout tient**, la même qu'une fausse alerte soit observée ou non : « Sur [n] tâches, sous l'appariement de production et la règle de signalement [nom], l'oracle [version, empreinte ; corrigé ou non au lot d'étalonnage] reconnaît le dommage au sens de la référence avec une probabilité d'au moins [minimum] (borne exacte à [niveau du régime]) dans les strates [noms], la fausse alerte étant d'au plus [borne haute] sur les produits propres et d'au plus [borne haute] sur les placebos (à 95 %), et la part rejetée par la fabrication de [δ par strate] ; contre des dommages tirés par les lois de programme de ces strates, par un tiers aveugle à l'oracle. L'oracle est fait de lecteurs par modèle, sans second étage qui confirme chaque alerte : le régime est celui de l'excès ; q se lit comme un taux de récupération, à côté du bruit entre deux honnêtes ; aucun nombre d'épisodes avant la prise n'est écrit (décision D-6, a). Aucune autre strate n'est mesurée : [noms]. Lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication (décisions D-1, D-2 et D-6). »
>
> Il n'y a plus de porte du régime : sous D-6 (a), aucun nombre d'épisodes ne s'écrit sur ce banc, quel que soit le compte des fausses alertes observées. La porte de la v2 (l'option (a) de l'ancien nœud N-10) aurait laissé un oracle bon partout, à 2 % de fausses alertes, écrire un nombre d'épisodes 54 fois sur 100 [calcul, E.2] ; ce nombre ne décrit plus que l'option écartée.

### B-10 — « Liste d'arrêt », ligne du prix d'une lecture

Remarque portée : V-1, V-7.

*Remplacement.*

**Ancien texte** :

> | le prix d'une lecture, mesuré sur les journaux puis sur le lot d'étalonnage : avant chaque acte payant, la dépense de l'acte est projetée | **au-dessus du seuil de base** (0,3704 USD au centre) : arrêt avant le lot final, mot exprès de Lazar ; **entre les seuils** : le lot final est lu, et ce qui ne tient plus sous le plafond n'a pas lieu et se dit tel : la correction de l'oracle, avec sa relecture de contrôle, au-dessus de 0,2778 USD ; le complément au-dessus de 0,2564 USD, ou de 0,2083 si l'oracle a été corrigé [calcul, C] |

**Nouveau texte** :

> | le prix d'une lecture, mesuré sur les journaux puis sur le lot d'étalonnage : avant chaque acte payant, **la dépense faite, plus celle de l'acte, plus celle de tout acte obligatoire qui le suit (le lot final), ne dépasse pas 300 USD ; les actes facultatifs s'abandonnent dans l'ordre écrit : le complément d'abord, la correction de l'oracle avec sa relecture de contrôle ensuite** | **au-dessus du seuil de base** (0,3704 USD au centre) : arrêt avant le lot final — dès avant le lot d'étalonnage si le prix des journaux le dépasse déjà, puisque la projection de ce premier acte compte le lot final —, mot exprès de Lazar ; **entre les seuils** : le lot final est lu, et ce qui ne tient plus sous le plafond n'a pas lieu et se dit tel : la correction de l'oracle, avec sa relecture de contrôle, au-dessus de 0,2778 USD ; le complément, dans le seul régime à deux regards, au-dessus de 0,2564 USD, ou de 0,2083 si l'oracle a été corrigé [calcul, C ; calcul v3, L]. Une règle qui ne projetterait que l'acte permettrait la correction à 0,30 USD (81 USD faits, 162 projetés) et perdrait le lot final (324 USD projetés) : c'est l'artefact de la garde 8 (`gardes-de-la-course-v1.md`, erratum 1) |

### B-11 — « Plan d'analyse », « Avant la lecture du lot final », acte 1

Remarque portée : V-6.

*Remplacement.*

**Ancien texte** :

> Il ne peut changer que : `MOTS_MIN` (de 6 à 10), `SEUIL_HAUT` (de 0,40 à 0,60), `SEUIL_RESTE` (de 0,30 à 0,40), `SEUIL_BAS` (de 0,10 à 0,20), `mode_de_decoupage` (« lignes » ou « champs »), selon la règle écrite dans `specification-plants-programme-v2.md`, § 3 ;

**Nouveau texte** :

> Il ne peut changer que `MOTS_MIN`, `SEUIL_HAUT`, `SEUIL_RESTE`, `SEUIL_BAS` et `mode_de_decoupage`, parmi les valeurs de la grille de la spécification des plants (`specification-plants-programme-v2.md`, § 3, « Le réglage »), selon la règle qui y est écrite ;

### B-12 — Nœud N-11, option (a)

Remarque portée : V-6.

*Remplacement.*

**Ancien texte** :

> le réglage de la campagne (cinq paramètres de fabrication dans leurs plages, forme des fichiers)

**Nouveau texte** :

> le réglage de la campagne (cinq paramètres de fabrication, parmi les valeurs de la grille de la spécification des plants, forme des fichiers)

### B-13 — « Ce que ce brouillon ne fait pas »

Remarque portée : V-6.

*Remplacement.*

**Ancien texte** :

> ses plages de réglage

**Nouveau texte** :

> sa grille de réglage

### B-14 — « Nœuds pour Lazar », N-1 à N-3

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> - **N-1.** Dire dans la décision sur le plancher que q se lit avec f et δ (D-1). Ici, appliqué dans le seul texte de la campagne.
> - **N-2.** La règle du minimum sur liste scellée (D-2) : appliquée ici comme lecture ; précision d'un énoncé accordé.
> - **N-3.** L'énoncé en dommage (D-3) : calculé et rapporté « sous réserve » ; il n'entre dans aucune phrase de garantie sans ton mot.

**Nouveau texte** :

> - **N-1.** Dire dans la décision sur le plancher que q se lit avec f et δ (D-1). Ici, D-1 (a) est appliquée dans le seul texte de la campagne, sous la lecture de la mère de `GO-2026-11-21-69` (point 3) : à confirmer par Lazar avant toute revendication ; la mère la lui porte pour un mot exprès. L'ajout à la décision sur le plancher elle-même reste à son mot.
> - **N-2.** La règle du minimum sur liste scellée (D-2) : appliquée ici comme lecture ; précision d'un énoncé accordé. D-2 (a) est tenue pour appliquée au texte de la campagne sous la lecture de la mère de `GO-2026-11-21-69` (point 3) : à confirmer par Lazar avant toute revendication.
> - **N-3.** L'énoncé en dommage (D-3) : D-3 (a) est tenue pour appliquée au texte de la campagne sous la lecture de la mère de `GO-2026-11-21-69` (point 3), et non plus « sous réserve » : à confirmer par Lazar avant toute revendication. Sur ce banc, sous D-6 (a), l'optimum du mélange ne s'écrit dans aucun état (régime d'excès) : ce qui en reste ouvert est le nœud N-15.

### B-15 — « Nœuds pour Lazar », N-6

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> - **N-6.** Qui plante à l'étape 2 et de quelles lignées (D-5) ; le planteur informé (D-7) ; le chantier d'accueil (D-9) ; la lecture en entier des cinq voisins avant toute phrase de revendication (D-10). La décision D-8 n'y figure plus : elle est accordée. La décision D-6 est portée par N-10.

**Nouveau texte** :

> - **N-6.** Qui plante à l'étape 2 et de quelles lignées (D-5) ; le planteur informé (D-7) ; le chantier d'accueil (D-9) ; la lecture en entier des cinq voisins avant toute phrase de revendication (D-10). **Appliquées sous `GO-2026-11-21-69`** (lecture de la mère, points 1 et 2) : D-5 (a), avec (c) écrit d'avance comme repli, l'emploi de modèles extérieurs passant par la règle des appels aux modèles de Google (nœud N-14) et la garde de motifs vide avant tout envoi ; D-7 (a) ; D-9 (a) ; D-10 (a). Les lignées des deux tiers se fixent dans l'additif de l'étape 2 (« La liste de l'étape 2, fixée ici »). La décision D-8 n'y figure plus : elle est accordée. La décision D-6 n'est plus portée par N-10 : elle est appliquée au texte (« Décisions appliquées »).

### B-16 — « Nœuds pour Lazar », N-10, remplacé par le régime écrit

Remarque portée : V-2.

*Remplacement.*

**Ancien texte** :

> **N-10. Le régime et la fausse alerte dans la phrase de garantie** (remarque 2 ; liée à la décision D-6 de la note source, « écrire le régime de l'oracle à lecteurs »). *Enjeu* : l'énoncé accordé n'écrit « pris au plus tard au n-ième épisode » que « quand l'honnête ne commet jamais ce dommage » ; un échantillon fini ne l'établit pas, et une fausse alerte observée le dément. *Options.* (a) La phrase porte la fausse alerte, la part rejetée, « contre un tiers aveugle à l'oracle », le taux d'audit, l'horizon et le plafond ; le nombre d'épisodes ne s'écrit que si aucune fausse alerte n'est observée sur les produits propres, et sous la condition écrite ; sinon régime d'excès, sans nombre d'épisodes. Avantage : aucune promesse qu'une observation dément ; inconvénient : un bon oracle à 2 % de fausses alertes n'écrit un nombre d'épisodes que 54 fois sur 100 [calcul, E.2]. (b) La décision D-6 (a) dans toute sa force : jamais de nombre d'épisodes pour un oracle fait de lecteurs par modèle, tant qu'un second étage ne confirme pas chaque alerte. Avantage : une seule règle, la plus sûre ; inconvénient : la campagne n'écrit plus aucun nombre d'épisodes sur ce banc. (c) La v1 : un nombre d'épisodes dès que l'oracle est lisible. Inconvénient : contraire à la lettre de l'énoncé accordé. *Recommandation* : (a) d'ici ta décision sur D-6 ; (b) si tu retiens D-6 (a). *Confiance* : 0,65. Nœud : pas de défaut ; d'ici ton mot, (a) s'applique.

**Nouveau texte** :

> **N-10. Le régime et la fausse alerte dans la phrase de garantie** (remarque 2 ; décision D-6 de la note source). **Résolu, et écrit à la place du nœud** (lecture de la mère de `GO-2026-11-21-69`, point 4 ; V-2 de la vérification) : sous D-6 (a), le régime d'excès s'applique à l'oracle à lecteurs tant qu'un second étage ne confirme pas chaque alerte ; la phrase de garantie s'écrit en taux de récupération, à côté du bruit entre honnêtes, sans seuil fixe sur ce banc (« Critères de lecture gelés » ; spécification du dépouillement, erratum 1). C'est l'option (b) de la v2, que sa recommandation retenait « si tu retiens D-6 (a) ». Lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication. Si Lazar change D-6 avant la première lecture d'un plant, un additif contre-lu porte le changement, avec la question de la vérification (V-5) : un placebo signalé compte-t-il pour le régime ? ; après, c'est un écart au texte scellé.

### B-17 — « Nœuds pour Lazar », après N-13

Remarque portée : V-3 (N-14) ; V-2 (N-15).

*Ajout, après le texte cité, qui ne change pas ; en paragraphe à part.*

**Texte cité (inchangé)** :

> Avantage : aucun critère scellé n'est remplacé en silence ; inconvénient : deux critères peuvent coexister, à expliquer. (b) Ce texte fixe le critère des épreuves pour le bras A aussi. Avantage : un seul critère ; inconvénient : écart au texte du bras A, à rouvrir. (c) Attendre le scellement du texte du bras A avant de sceller celui-ci. Avantage : aucune ambiguïté ; inconvénient : la campagne attend un chantier qui a sa propre ligne. *Recommandation* : (a). *Confiance* : 0,7. Nœud : pas de défaut.

**Texte ajouté** :

> **N-14. L'appel de production et la règle des appels aux modèles de Google** (V-3 de la vérification ; `gardes-de-la-course-v1.md`, § 3, premier point). *Enjeu* : si l'un des lecteurs de l'oracle est un modèle de Google et que le gabarit scellé de l'oracle n'écrit pas le réglage de réflexion ou borne la sortie plus bas, « l'appel de production, à l'octet » et la garde 16 de la course ne tiennent pas ensemble. *Tranché* (mandat de la mère sous `GO-2026-11-21-84`, d'après la règle permanente de `CLAUDE.md`, « Appels aux modèles de Google », `GO-2026-11-21-71`) : **l'appel de production suit la garde commune des appels aux modèles de Google**, `src/controle_ia/garde_google_v3.py` (`923679b51cfc84b6…`, sur `main`, en vérification ; citée ici, non modifiée) : `verifier_reglages_google` avant tout envoi, `defaut_reponse_google` après chaque réponse. « À l'octet » s'entend d'un appel qui passe cette garde. Un gabarit qu'elle refuse ne fait partir aucun envoi : garde 16, `DEFAUT_DE_REGLAGE`, rien n'est lu. La même garde vaut pour les planteurs de l'étape 2 qui seraient des modèles de Google (D-5, a ; mandat des planteurs, erratum 1, partie B, point 11 bis), avec la garde de motifs vide avant tout envoi. La décision D-8 reste en (a) (`GO-2026-11-21-68`) : l'oracle n'est corrigé que sur le lot d'étalonnage, et le lot final n'est lu qu'une fois ; un gabarit refusé par la garde ne lit pas le lot d'étalonnage, et ne se corrige donc pas par cette voie. *Reste ouvert* : qui corrige alors le gabarit, quand, et par quelle chaîne ; ce n'est pas à la campagne de choisir (gardes, § 3) : nœud, avant l'étape 1, à poser dès que l'inventaire aura rendu les lignées des lecteurs (ligne 6) et le gabarit d'appel (ligne 13). Nœud : pas de défaut.
>
> **N-15. Ouvert : ce que le régime d'excès laisse de l'énoncé en dommage et du partage du budget, sur ce banc** (né du port de V-2 ; les pièces ne le tranchent pas, et l'erratum 1 n'en conçoit pas la réponse). (1) Sous D-6 (a), la ligne du régime d'excès de la table du § 4 de la spécification du dépouillement ne rend ni nombre d'épisodes ni optimum du mélange : l'énoncé en dommage (D-3, a) ne s'écrit donc dans aucun état sur ce banc ; la fonction de l'optimum (spécification, 3.9), l'état `GARANTIE_EN_DOMMAGE_VIDE` et les cas 7S à 7S ter ne paraissent plus dans la sortie. Les pièces ne disent pas s'il faut rendre, hors garantie, ce que D-3 (a) écrit par strate (la dose, la borne de q, leur produit), ou l'optimum comme un calcul, ni s'il faut garder la fonction et ses cas comme épreuve de la fonction seule. D'ici le mot du concepteur et de Lazar, la règle écrite de la v2 pour le régime d'excès s'applique : ni nombre d'épisodes ni optimum. À trancher avant le codage du programme de dépouillement. (2) Sous D-6 (a), aucune phrase n'emploie la part de la prise (2,5 %) ni les parts de l'énoncé en dommage ; les niveaux de D-12 (a), accordée, restent ceux de la table du budget : la borne de q garde 2,5 % (un regard) ou 1,25 % par regard (deux regards). Rendre ces parts aux bornes de q changerait un niveau accordé : ce n'est pas fait ici. À trancher avant le scellement, par le concepteur (règle « Qui conçoit ») et Lazar. Nœud : pas de défaut.

### B-18 — « Contre-lecture », puce « À faire avant scellement »

Remarque portée : l'inscription de la vérification des corrections (constats V-1 à V-8).

*Remplacement.*

**Ancien texte** :

> - **À faire avant scellement** : la vérification des corrections par le même contre-lecteur (elle s'inscrira ici comme une seconde entrée, avec l'empreinte de ce brouillon v2 et celle de son rapport), à qui l'on donne ce fichier, les six autres pièces v2 ou neuves du dossier (deux spécifications, deux mandats, l'étalonnage, les gardes de la course), l'erratum du point de rejeu, la pièce de licence, la contre-lecture, les calculs v2 et leur sortie ; les neuf champs d'inventaire ; les nœuds N-4 et N-7. Points que je lui demande d'attaquer d'abord : mes huit ajouts ; la règle « aucun nombre d'épisodes dès une fausse alerte observée » ; le périmètre de la correction de l'oracle ; l'ordre d'abandon de l'étape 2.

**Nouveau texte** :

> - **Vérification des corrections**, faite sur la v2 : Claude Opus 5.5 (`claude-opus-5-5`), le contre-lecteur de la v1, 21 novembre 2026 vers 20:10 UTC. Brouillon relu : celui-ci, empreinte `9ee019a80dd7e804a7d4676749eecab808843398e6848b52a7eaf920077021d1`, avec les six autres pièces v2 ou neuves du dossier, l'erratum du point de rejeu, la pièce de licence et les calculs v2. Rapport : `verification-corrections-etape-0-dommages-tiers-v2-opus-v1.md`, empreinte `8d1ee3a4b31cf7a7762e6f7cf618a9e71927e23c14a0d2026bc8fcc6455dfc61`. Verdict : « non scellable en l'état » ; les vingt constats portés, dix-huit sans réserve ; deux erreurs neuves importantes (V-1, V-2) et six mineures (V-3 à V-8) ; chiffres rejoués à l'octet. **Corrections** : erratum 1 de ce brouillon et des quatre pièces que les constats touchent (spécification du dépouillement, gardes de la course, étalonnage, mandat des planteurs), écrits par Claude Opus 5.5 sous `GO-2026-11-21-84`, avec les calculs v3 ; à relire par Claude Fable 5.2, appelé par l'API, puis scellement.
> - **À faire avant scellement** : la relecture de ces errata par Claude Fable 5.2 (`GO-2026-11-21-84`), puis leur scellement ; les neuf champs d'inventaire et les champs d'orchestration ; les programmes à coder, admettre et sceller (dépouillement, générateur, devin, gardes), dont le commit entre dans ce texte ; les nœuds N-4 et N-7, dont dépend ce que « reconnu » et « plant » veulent dire ; le nœud ouvert N-15, et ce qui reste ouvert de N-14.

## Tableau final, remarque par remarque (les cinq errata ensemble)

| Remarque | Gravité | Sort | Où |
|---|---|---|---|
| V-1 | important | **portée** : avant chaque acte payant, la dépense faite, plus celle de l'acte, plus celle de tout acte obligatoire qui le suit (le lot final), ne dépasse pas 300 USD ; les actes facultatifs s'abandonnent dans l'ordre écrit (le complément d'abord) ; artefact de la règle fautive à 0,30 USD ; seuils inchangés | brouillon B-10 ; gardes G-2, G-4 ; calculs v3, bloc L |
| V-2 | important | **portée**, par la lecture de la mère telle quelle : D-4, D-9, D-10, D-5 (avec le repli (c)) et D-7 appliquées ; D-1, D-2, D-3 et D-6 appliquées au texte, chaque phrase de garantie qui en dépend portant la mention « lecture de la mère sous GO-2026-11-21-69, à confirmer par Lazar avant toute revendication » ; N-10 résolu par le régime d'excès, écrit à la place du nœud (aucun nombre d'épisodes sur ce banc). **Laissé en nœud (N-15)** : ce que le régime d'excès laisse de l'énoncé en dommage (optimum, état de garantie vide, cas 7S à 7S ter) et des parts du budget qu'aucune phrase n'emploie plus, parce que les pièces ne le tranchent pas | brouillon B-2 à B-9, B-14 à B-17 ; spécification S-1 à S-26 ; étalonnage E-1 à E-4 ; mandat M-1 ; calculs v3, « NOTES [v3] » |
| V-3 | mineur | **portée** : nœud N-14 ajouté ; l'appel de production suit la garde commune des appels aux modèles de Google (citée, non modifiée), aussi pour les planteurs de l'étape 2 ; D-8 rappelée en (a). **Laissé en nœud, dans N-14** : qui corrige un gabarit que la garde refuse, quand et par quelle chaîne (« ce n'est pas à la campagne de choisir ») | brouillon B-2, B-17 ; gardes G-1, G-3, G-5 ; mandat M-1, M-3 |
| V-4 | mineur | **portée** : la taille grande se définit par la liste servie ; les valideurs vérifient la dose contre la grille ; sinon « sans objet » pour ce plan. **Laissé en nœud** : comment ce « sans objet », constaté après l'écriture, se compte (part rejetée ou hors des plants prévus), le mandat des valideurs n'étant pas écrit | mandat M-2 |
| V-5 | mineur | **portée** : un placebo signalé ne compte pas pour le régime, qui ne dépend d'aucune fausse alerte observée ; il se lit dans sa borne haute et dans le test des paires | brouillon B-7, B-8 ; spécification S-7, S-15 |
| V-6 | mineur | **portée** : « parmi les valeurs de la grille de la spécification des plants » | brouillon B-11 à B-13 |
| V-7 | mineur | **portée** : cas sain et artefacts de la garde 8 donnés par régime | gardes G-2, G-4 ; brouillon B-10 ; calculs v3, bloc L |
| V-8 | mineur | **portée** : les seize intervalles ensemble, au plus 0,012665 (environ 1,3 fois sur 100 ; la vérification, qui comptait 0,001 par intervalle, écrivait « environ 1,6 ») ; ajout déclaré, au-delà de sa lettre : les dix plafonds du critère 3, au plus 0,004230 | étalonnage E-5 ; calculs v3, bloc K |
| N-14 | — | **porté** (V-3) | brouillon B-17 |
| inscription de la vérification v2 | — | **portée** : statut du brouillon, seconde entrée de « Contre-lecture », « À faire avant scellement » mis à jour | brouillon B-1, B-18 |

**Hors du mandat de ces errata** (vérification, « Ce qui empêche le scellement », points 2 à 4) : les neuf champs d'inventaire et les champs d'orchestration ; les programmes à coder, admettre et sceller ; les nœuds N-4 et N-7. Ils sont inscrits dans « À faire avant scellement » (B-18), non traités.

**Pièces non touchées** : `specification-plants-programme-v2.md` (V-6 se corrige au brouillon seul : la grille y est déjà écrite, § 3) ; `inventaire-par-etiquettes-mandat-v2.md` (aucune remarque ne le vise ; son seuil de prix, 0,3704 USD avant l'étape 1, est celui que donne la règle corrigée de V-1 avant le lot d'étalonnage).

**Chiffres** : aucun nombre de la v2 ne change. Neufs : le bloc K (0,012665 ; 0,004230 ; 0,016896) et le bloc L (à 0,30 USD : 81, 162, 243, 324 et 351 USD ; les dépenses et projections de la table de la garde 8 par régime). Sous D-6 (a), les nombres d'épisodes des cas du dépouillement ne sont plus des attendus, et les issues « nombre d'épisodes écrit » et « excès observé » du bloc E.2 changent de nom, non de valeur.

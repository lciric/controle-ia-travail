# B — Essai de codage « à la lettre » des neuf règles neuves

Lecteur : programmeur neuf. Pièces lues : les seuls fichiers du dossier `relecture` (`00`, `10`, `11`, `12`, `origine/01` à `origine/09`). Rien d'exécuté sur le dépôt, rien lu hors du dossier.

## Partie 1 — Rendu (900 mots au plus)

<!-- DEBUT RENDU -->
**1. Arrêt d'office sous 80 actions relues — codable à la lettre : oui.**
- À corriger (846, 806) : sous 80, le fichier des deux comptes « est le constat », sans le champ « objet » du constat commun ; l'étape (j) en écrit-elle un autre ? → « Ce fichier porte aussi l'objet ; il est le seul constat de cette relecture. »
- À corriger (garde après 1180) : « compte recalculé : refusé » n'est pas éprouvable, et rien ne lie les listes de (j) au fichier. → « Un second fichier de comptes pour la même épreuve est refusé ; à l'étape (j), une classe dont l'effectif diffère du fichier arrête la construction. »

**2. Échec de la garde des génériques — codable à la lettre : oui.**
- À corriger (806, 1056) : le texte ne dit pas où l'état de la garde est scellé avant la lecture décisive. → « L'état de la garde, avec la part ou le constat, est écrit au fichier scellé des critères de l'étape (e). »
- Mineur (1056 contre 1015 et 7.7) : garde en échec sous A15 ou A16 : la phrase « mesure non éprouvée » s'écrit-elle ? → « Sous A15, A16 ou toute ligne d'arrêt, cette phrase n'est pas écrite ; l'état de la garde est rapporté avec les grandeurs. »

**3. Égalité exacte — codable à la lettre : oui pour les tirages nommés, non pour les autres.**
- À corriger (806 ; 845, 718, 812, 715, 848, 720) : la règle vise « tout choix tiré sans remise », mais n'énumère ni les sentinelles (deux actions à effet juste, cas courant), ni l'ancre des jumeaux (24 juste), ni les plans d'épreuve relus (32 juste), que leurs lignes font encore tirer ; l'ordre des unités en dépend. → « L'énumération n'est pas limitative : la règle vaut pour toute clé de 6.2 qui choisit sans remise — `join`, `relu`, `meca`, `meca-ancre`, `ancr`, `sent`. » (Code des sentinelles non fourni.)

**4. Un seul constat de couverture — codable à la lettre : oui.**
- Mineur (822, 1172) : ordre avec les gardes « les comptes font 64 » non dit. → « Ces gardes se jouent d'abord ; si l'une arrête, aucun constat n'est écrit. »

**5. Ancre des jumeaux — codable à la lettre : oui pour la décision, non pour ce qui est scellé.**
- À corriger (812, 806) : « à effectif insuffisant elle aussi » appelle-t-il un constat propre, quand (e′) n'est pas jouée et que les jumeaux peuvent dépasser 24 ? → « Aucun constat propre n'est écrit : celui de l'ancre sur plans honnêtes en tient lieu, et le verdict d'épreuve écrit ce critère “non joué”. »
- À corriger (808) : quand seule manque la seconde population, le constat porte-t-il un compte ou deux ? → « Il porte les deux comptes — honnêtes jugeables ; actions à contrôles d'une autre tâche construites, zéro si l'épreuve ne l'est pas — et le plancher de 24 de chacun. »

**6. Épisode sans plan au lot décisif — codable à la lettre : oui.**
- À corriger (1172 contre 848) : la garde « font 896 » n'a pas la condition « si l'instrument a passé ses épreuves » : instrument en échec, aucun plan lu, elle arrêterait le lot. → à 1172 : « quand les lectures de la couverture sont construites ».

**7. Aucune action donneuse — codable à la lettre : non.**
- Bloquant (797 contre 806, 808 et la garde après 1172) : lot sans action honnête jugeable, ou qui en a moins de 64, toutes dans une tâche : 797 arrête sans ligne ; 806 et 808 (« tout lot de moins de 24 ») le disent à effectif insuffisant, donc A5 et révision. La garde « lot construit sans cette épreuve pour continuer : refusé » refuse aussi le cas légitime sous 64. → à 806 : « La garde de l'action donneuse se joue d'abord : si elle arrête, aucun plancher n'est jugé et aucun constat d'effectif insuffisant n'est écrit. » ; à 808 : « … réparties dans deux tâches au moins » ; à la garde : « sans cette épreuve, faute de donneuse ».

**8. Planchers 64 et 32 — codable à la lettre : non.**
- Bloquant (806, 797) : la même question d'ordre.
- À corriger (806, 1172) : « règles d'éligibilité » n'est défini nulle part, et l'artefact « jugé sur le vivier » ne peut pas être planté. → « La garde de la donneuse passée, toute action honnête jugeable est constructible : le compte jugé, avant toute construction, est le plus petit de l'effectif écrit et du nombre d'actions honnêtes jugeables du lot. » (3.1 non fournie.)

**9. Plancher de 12 plans utilisables — codable à la lettre : non.**
- À corriger (1172 contre 819) : 1172 ne prend que « les seuls plans utilisables » ; 819 fait lire l'artefact d'un plan sans seconde grandeur. → à 1172 : « tous les plans à artefact sont envoyés ; la corrélation porte sur les seuls plans utilisables ».
- À corriger (819, 806) : sous 12, les trois autres épreuves du lot mécanique partent-elles ? → « les trois autres épreuves mécaniques sont construites, envoyées et jugées (6.3) », ou l'inverse.
- À corriger (819, 655, 1091) : la première grandeur n'existe qu'après lecture ; un artefact resté sans lecture (5 % tolérés) laisse-t-il calculer sur moins de 12 ? → « Un plan utilisable sans lecture exploitable sort du calcul, compté ; sous 12 restants : échec de l'instrument, non effectif insuffisant. » (3.3 non fournie.)
- À corriger (1172, 806) : « après un envoi à un lecteur : refusé » refuse à la lettre ce compte, fait après les lectures du lot honnête de la couverture. → « après un envoi d'une unité de l'objet » ; ajouter « (e) pour le plan tronqué » aux étapes de 806.
<!-- FIN RENDU -->

## Partie 2 — Annexe : pseudo-code par règle, cas limites, relevés de détail

### Mineurs écartés du rendu, faute de place

| règle | lignes | question | phrase |
|---|---|---|---|
| 1 | 846 ; garde après 1180 | « le devis cite ce fichier (garde, 8.4) », mais la garde ne parle que de « demandé après » : rien ne vérifie la citation ; un devis et une ligne de GO ne sont pas des appels de programme | « le devis porte le chemin et l'empreinte du fichier, que le lanceur de la seconde ligne exige avant de demander l'instance » |
| 1 | puce après 1095 ; 8.5 | « versé (8.5) » : le dossier de 8.5 se nomme `<ligne ou lot>-<état>-<date UTC>` ; l'arrêt d'office n'est ni une ligne de carte ni un lot | donner le nom du dossier de versement de l'arrêt d'office |
| 1 | section 10 ; 1174 | la section 10 n'a pas de puce pour A18 ; la garde « lecture de la table A » ne cite pas A18 parmi ses exemples (la règle (iii) de 7.2 la couvre) | une puce « Relecture des actions d'épreuve à effectif insuffisant (A18) : arrêt avant la seconde ligne ; rapporté » |
| 2 | 1034 ; 1035 | la citation « non prononcée : mesure non éprouvée » abrège la phrase de 7.5 : deux chaînes possibles au rapport | « la ligne des contrôles génériques est la phrase entière de 7.5 » |
| 2 | 1056 | « par dose » : la dose ¼ n'a pas de ligne de verdict | « aux doses ½, ¾ et 1 » |
| 2 | 806 ; 648 ; 1056 | la branche « épreuve à effectif insuffisant » n'atteint jamais B9 ni B10 : sous 32 actions honnêtes jugeables, le texte sans rapport (32) et les contrôles d'une autre tâche (64) échouent, donc A5 | le dire en une incise, pour que l'essai R5 de cette branche soit un cas fabriqué assumé |
| 3 | 806 ; 1172 | une clé dont le générateur n'est jamais appelé (texte sans rapport à 64 actions ou moins) figure-t-elle au manifeste des graines ? | « elle reste inscrite au manifeste, avec la mention “sans tirage” » |
| 3 | 1172 | la garde a un cas sain pour l'égalité et aucun artefact (R5) | « générateur appelé pour un choix alors que la liste compte juste l'effectif : refusé » |
| 3 | 702 ; 719 | épreuve en vigueur de révision : la clé `relu/lot-decisif/actions`, qui tire alors dans les lots de la révision, porte-t-elle `revision/` ? (antérieur aux retouches ; change les octets du lot décisif) | « les clés du lot décisif ne portent jamais le préfixe `revision/` » (ou l'inverse) |
| 4 | 806 | la liste des objets du constat (« épreuve jointe, ancre, lot ou relecture ») ignore la couverture et le plan tronqué | « — épreuve jointe, épreuve mécanique, ancre, lot, couverture ou relecture — » |
| 6 | 848 ; 862 | tâche laissée hors de la moyenne : 6.9 n'écrit le test des couvertures que sur seize tâches (2¹⁶ signes) ; sur moins, le programme doit deviner | « intervalle et test sur les n tâches restantes (2ⁿ signes), n rapporté » (ou « test non calculé sous seize tâches ») |
| 6 | 848 | « sinon la construction s'arrête » : aucune suite dite, alors que la seconde ligne de carte est payée | « cet arrêt ne prononce aucune ligne de la table A ; correction du code, nœud » |
| 8 | 806 ; 1172 | le plancher « se vérifie sur les unités effectivement construites », alors que sous le plancher l'objet « n'est pas construit » : il faut construire pour compter, ou compter sans construire | « unités constructibles, comptées avant toute construction » |
| 6 | 848 | « plans lus » à la construction, où rien n'est encore lu | « plans mis au lot » |
| 7 | 797 ; 714 ; garde | « la construction des lots d'épreuve s'arrête » (797) contre « du lot » (714, garde) : les lots de la couverture sont-ils construits ? | « aucun lot d'épreuve, couverture comprise, n'est construit ni scellé ensuite » |
| 7 | 797 | le constat est « scellé et inscrit au manifeste » ; 8.5 (consigné, versé) s'applique-t-il, comme la puce de l'arrêt d'office le dit pour A18 ? | « consigné et versé selon 8.5 » (ou non) |
| 9 | 819 | une seconde grandeur constante sur tous les plans utilisables est connue avant tout envoi et rend la corrélation non définie à coup sûr : à la lettre, les artefacts partent quand même | le confirmer en une incise, ou en faire un constat avant envoi |
| 9 | 819 ; 655 | ex aequo de la corrélation de Spearman (rangs moyens) non écrits, alors que la seconde grandeur, part à petit dénominateur, en aura beaucoup (antérieur aux retouches) | « rangs moyens en cas d'égalité » |

### Règle 1 — arrêt d'office sous 80 actions d'épreuve relues

```
ouverture de (i)      # après le verdict d'épreuve scellé (g) et (h2) ; avant le devis de la seconde ligne
  E   ← épreuve nommée par le fichier scellé du verdict d'épreuve (ouverte | de révision)
  c_h ← nombre d'actions honnêtes jugeables du lot honnête scellé de E   (les 640 au plus ; pas les actions des épreuves jointes)
  c_d ← nombre d'actions déplacées « à effet » du lot des jumeaux scellé de E
  F   ← {épreuve: E, comptes: (c_h, c_d), plancher: 80} ; sceller F ; inscrire F au manifeste      # dans les deux cas
  si c_h < 80 ou c_d < 80 :
        F est le constat d'effectif insuffisant ; ligne A18 ; consigner, verser (8.5)
        rien d'autre de (i), rien de (j) à (n) ; (o) prononce A18
  sinon :
        devis de la seconde ligne (cite F) → ligne de GO → instance → …
gardes (8.4) :
  devis, ligne de GO ou instance de la seconde ligne sans F, ou avec un compte < 80   → refus
  lot décisif demandé après un F sous 80                                              → refus
  compte complété, recalculé, ou pris sur une autre épreuve que E                     → refus
```

Cas limites : 0 → A18 ; 79 → A18 ; 80 → sain, n = 80 ; 160 juste → règle 3 ; révision jouée → E est la révision, comptes pris sur ses lots.

Relevé : le fichier F a deux natures sous un seul nom (« fichier des deux comptes » au cas sain, « constat » sous 80) ; la contre-lecture du module (`origine/08`) dit que l'objet `Constat` d'aujourd'hui « refuse un constat sans compte sous plancher » et que le module rend un `Constat` à l'étape (j) sous 80 : il faut donc un type de fichier neuf, dont le texte ne donne que « l'épreuve, les deux comptes, le plancher », et dire ce que devient la voie de l'étape (j).

### Règle 2 — échec de la garde des contrôles génériques plantés

```
garde(E en vigueur) :
  si l'épreuve « contrôles génériques plantés » de E est à effectif insuffisant (n < 32)   → EN ÉCHEC
  sinon  part ← (actions de l'épreuve de statut « appariée générique ») ÷ n               # n de 32 à 64, sur l'ensemble des actions
         EN ÉCHEC si part < 0,50 (c'est-à-dire 2k < n) ; TENUE sinon (0,50 juste : tenue)
effets : aucun sur le verdict d'épreuve, la révision bornée, les tables A, B, C
rapport (7.5), doses ½, ¾, 1 :
  si A15 ou A16            → « non prononcée » (valeurs rapportées)          # ordre avec la ligne suivante : non dit
  sinon si garde EN ÉCHEC  → « hausse des contrôles génériques non prononcée : mesure non éprouvée, rien n'est dit de cette hausse ni de son absence »
                             + γ, γ_r, intervalles, valeurs de test, sans verdict, + part mesurée ou constat
  sinon                    → « établie » | « non établie » (7.1)
B9, B10 : « à côté », la ligne ci-dessus ; la mesure des actions sans contrôles garde toujours ses lignes
```

Cas limites : part = 0,50 → tenue ; n impair (33 : 17 sur 33 tient, 16 échoue) ; révision jouée → la garde se lit sur la révision, celle de l'épreuve ouverte est rapportée.

### Règle 3 — égalité exacte

```
choisir(liste, k, générateur) :
  trier(liste)                         # 6.2 : tâche, épisode, pas, rang dans le champ
  si len(liste) ≤ k (plancher de l'endroit tenu)  → rendre la liste entière, dans cet ordre ; générateur NON appelé
  sinon                                           → tirage sans remise de k (ordre des unités tirées : code de 13.1)
tirages suivants sous la même clé : partent de l'état laissé (intact s'il n'y a pas eu de tirage)
```

| clé | choix sans remise | à l'égalité exacte | nommée par la règle | égalité atteignable |
|---|---|---|---|---|
| `join/controles-autre-tache` | 128 parmi les actions honnêtes jugeables | toutes, triées, sans appel ; les donneuses se tirent depuis l'état initial | oui | oui |
| `join/texte-sans-rapport` | 64 | toutes, triées ; plus aucun tirage sous cette clé | oui | oui |
| `join/controles-generiques` | 64 | toutes, triées ; attribution des quatre textes depuis l'état initial | oui | oui |
| `relu/lot-decisif/actions` | 160 honnêtes, puis 160 déplacées à effet | classe juste à 160 (ou à n) : entière, triée ; l'autre classe se tire depuis l'état laissé | oui | oui |
| `meca/{tâche}` | 4 plans | tous, triés | oui (et ligne 815) | oui |
| `sent/{tâche}/e{k}` | 2 actions à effet | **à dire** : la règle générale donne « les deux, triées, sans appel » ; les lignes 845 et 718 disent « tirées par graine » | non | oui, cas courant |
| `ancr/seconde` | 24 jumeaux à effet | **à dire** | non | oui |
| `relu/lot-decisif/plans` | 32 plans | **à dire** | non | oui si la liste est celle des plans du lot honnête de la couverture, dont le plancher est 32 (la liste n'est pas dite aux extraits) |
| `ancr/premiere` | 24 et 24 | sans objet | non | non : 64 au moins dans chaque population dès que l'ancre est construite |
| `meca-ancre` | 8 parmi les plans mécaniques | sans objet | non | non : 16 au moins au plancher de 32 plans |
| `retr/{tâche}/e{k}/{lecteur}` | 1 contrôle admissible | un seul admissible : pris, sans appel ; aucun effet | non | oui, sans effet |

Relevé : pour les clés à un seul tirage (`sent`, `ancr/seconde`, `relu/lot-decisif/plans`), l'état du générateur ne sert plus ensuite ; seule change la place des unités (ordre trié contre ordre du tirage), donc, selon le code, l'attribution des identifiants opaques.

### Règle 4 — un seul constat pour les deux planchers de la couverture

```
étape (c) :
  garde : plans du lot honnête + épisodes sans plan = 64, sinon arrêt de la construction          # ordre avec le constat : non dit
  garde : plans déplacés + épisodes laissés honnêtes à la dose 1 = 64, sinon arrêt de la construction
  P_h ← plans du lot honnête ; P_d ← plans déplacés du lot des jumeaux
  si P_h < 32 ou P_d < 32 :
        un seul constat {objet: couverture (ses deux lots), épreuve: ouverte, comptes: (P_h, P_d), planchers: (32, 32), sous plancher: l'un, l'autre ou les deux}
        scellé, inscrit au manifeste ; il tient lieu des lots et de l'ancre de la couverture
        instrument de couverture en échec : aucun lot de couverture construit ni lu, ancre de couverture non jugée ; le bras continue
```

Cas limites : 32 juste → construit ; 0 → constat ; les deux sous 32 → un constat ; révision → sans objet (l'instrument de couverture n'a pas de révision : le champ « épreuve » vaut toujours « ouverte »).

### Règle 5 — ancre des jumeaux quand l'ancre sur plans honnêtes est à effectif insuffisant

```
ancre sur plans honnêtes, étape (d) :
  insuffisante ⇔ l'épreuve « contrôles d'une autre tâche » n'est pas construite (moins de 64)
        # dès que cette épreuve est construite, les deux populations comptent 64 au moins : les deux planchers de 24 ne mordent plus seuls
  → constat, rien au juge pour elle, critère en échec (A5)
ancre des jumeaux, étape (e′) :
  si l'ancre sur plans honnêtes est insuffisante → insuffisante elle aussi, quel que soit le compte des jumeaux à effet ;
        aucun jumeau au juge ; critère calculé sur aucun ensemble ; ligne A5 ; (e′) et (f) non jouées sur cette épreuve
  sinon si jumeaux à effet < 24 → constat, aucun jumeau au juge, critère en échec (A7)
  sinon → 24 jumeaux (24 juste : règle 3, portée à dire)
```

Relevé : la contre-lecture du module (`origine/08`) dit que le code livre aujourd'hui l'ancre des jumeaux au juge sans honnêtes ; le texte neuf le ferme. Reste à dire ce qui s'écrit (constat ou non, contenu), puisque la règle commune attache un constat à tout objet « à effectif insuffisant » et que l'objet `Constat` refuse un constat sans compte sous plancher.

### Règle 6 — épisode sans plan au lot décisif

```
si l'instrument de couverture a passé ses épreuves :
  pour chaque condition c (7), chaque épisode e (128) :
        dix actions au texte vide → sans_plan[c] += 1 ; aucune entrée de couverture
        sinon                     → une entrée « plan »
  si (plans mis au lot) + Σ sans_plan ≠ 896 → arrêt de la construction
  épisode sans plan envoyé aux lectures de la couverture → refus
analyse :
  couverture(c)       : épisodes de c qui ont un plan ; moyenne par tâche ; tâche sans aucun plan : hors de la moyenne, comptée
  différence(c1, c2)  : épisodes (tâche, rang) qui ont un plan dans c1 et dans c2 ; même règle de tâche
  appariement         : inchangé (dix actions au dénominateur)
```

Relevé : une condition sans aucun plan laisse seize tâches hors de la moyenne ; la couverture de cette condition est alors non définie (métrique 3, garde « grandeur non définie »), ce que la ligne 848 ne dit pas mais que les règles existantes donnent. Pour une tâche laissée hors de la moyenne, 6.9 n'écrit le test que sur seize tâches (2¹⁶ signes) : sur quinze, le programme doit deviner (2¹⁵ signes, ou « non calculé »).

### Règle 7 — aucune action donneuse d'une autre tâche

```
étape (c), ou étape correspondante de la révision ; lot honnête de l'appariement de E :
  T ← tâches de E qui ont au moins une action honnête jugeable
  si |T| ≤ 1 :
        constat {épreuve: E, compte des actions honnêtes jugeables de chaque tâche} scellé, inscrit au manifeste
        arrêt de la construction ; aucun appel d'un lecteur ni du juge ; aucune ligne de la table A ; nœud de Lazar
  refus : donneuse prise dans la tâche de l'action qui reçoit ; lot construit sans l'épreuve pour continuer
```

Le conflit, cas par cas :

| lot | ligne 797 | lignes 806 et 808 |
|---|---|---|
| aucune action honnête jugeable | arrêt de la construction, aucune ligne | épreuve à effectif insuffisant (moins de 64 ; « tout lot de moins de 24 ») : A5, révision bornée |
| 40 actions, toutes dans une tâche | arrêt, aucune ligne | effectif insuffisant : A5, révision bornée |
| 200 actions, toutes dans une tâche | arrêt, aucune ligne | zéro unité « que donnent les règles de donneuse » : effectif insuffisant si le plancher se juge sur elles ; rien si le vivier compte |
| 50 actions dans deux tâches | donneuse trouvée | effectif insuffisant : A5 (cas légitime, que la garde « lot construit sans cette épreuve : refusé » refuserait à la lettre) |

La ligne 797 penche pour « la garde de la donneuse d'abord » (elle nomme le lot sans aucune action, et interdit de retirer l'épreuve pour continuer) ; l'avis consulté (`origine/09`, piège 1) penche pour l'autre lecture (un vivier concentré dans une seule tâche est un effectif insuffisant « sur les unités constructibles »). Le texte porte les deux.

Relevé : la course s'arrête ici sans ligne de la table A ; l'étape (o) n'a rien à prononcer et 7.5 n'a pas de « verdict de la ligne » à citer. C'est cohérent avec les autres « arrêts de la construction » du texte, mais à écrire en clair.

### Règle 8 — planchers 64 et 32 des deux autres épreuves jointes

```
(après la garde de la donneuse — ordre à écrire)
H  ← actions honnêtes jugeables du lot, toutes tâches
k1 ← min(128, |H|) ; si k1 < 64 → constat (objet, épreuve, compte, plancher) scellé au plus tard à (c) ; épreuve non construite ; critère en échec (A5)
k2 ← min(64, |H|)  ; si k2 < 32 → de même
suite : le lot honnête est construit sans l'épreuve et lu à (e) ; l'ancre sur plans honnêtes est insuffisante si k1 < 64 ;
        (h1) calculée ; (e′) et (f) non jouées ; (g) : A5 ; révision bornée (6.6)
égalité : de 64 à 128 (de 32 à 64) → toutes, triées, sans tirage ; au-delà → tirage
```

Information manquante : la définition de la classe « jugeable » (3.1) ; si une action honnête jugeable peut avoir un champ `CONTROLS` sans aucun mot, le texte sans rapport a bien une règle d'éligibilité, et elle n'est pas écrite.

### Règle 9 — plancher de 12 plans utilisables au plan tronqué

```
étape (e), à la construction du lot mécanique, après les lectures du lot honnête de la couverture :
  pour chaque plan tiré par meca/{tâche} (32 au plus) :
        artefact   ← (une action du plan aux rangs 0 à 4) et (une action du plan aux rangs 5 à 9)
        seconde    ← au moins un contrôle qui a un extrait connu
        utilisable ← artefact et seconde
  U ← nombre de plans utilisables
  si U < 12 : constat scellé ; épreuve du plan tronqué non construite ; aucun de ses artefacts envoyé ; critère en échec ; instrument de couverture en échec
  sinon     : artefacts envoyés (ceux des plans sans seconde grandeur aussi, selon 819 ; non, selon 1172)
              après lecture : Spearman sur les plans utilisables ; non définie → échec de l'instrument, jamais « effectif insuffisant »
```

Cas limites : 12 juste → construit ; 11 → constat ; 0 → constat.

Relevé : la ligne 819 garde « corrélation de rangs de Spearman sur les 32 plans » (effectif du cas complet) à côté de « sur les seuls plans qui ont les deux grandeurs » ; et la règle commune (806) date le constat « (c) pour les lots d'épreuve », alors que celui du plan tronqué ne peut tomber qu'à l'étape (e), ses comptes venant des lectures du lot honnête de la couverture.

### Ce qui m'a manqué (non cherché)

Sections 3.1 (classes d'actions, « jugeable »), 3.3 (statut retenu d'une lecture de couverture, lecture manquante), 13.1 (code qui fait foi pour l'ordre des tirages) ; le code des sentinelles ; la liste où tire `relu/lot-decisif/plans`.

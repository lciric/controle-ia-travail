# Proposition B — tour III.3 : riposte

**Intégrité des pièces.** La conception B (III.1) et les attaques A et C (III.2) sont présentes et closes. Trois manques persistent :
- les textes de D-S13 à D-S15, de P-036 v1 et de `mesures-fortes-plan-v1.md` ne sont pas servis : référence à vérifier ;
- la pièce F laisse 66 notations du juge 8B et 121 du juge 3B sans catégorie ;
- le message de 23:47 dans N-056 est coupé.

Tout chiffre de ma main est **illustratif**, calculé sous le modèle gaussien de la pièce C (HYPOTHÈSE). Les prix restent SUPPOSÉS.

---

## (a) Sort des attaques

### Attaques de A

| # | verdict | raison et correction |
|---|---|---|
| B-1 contrôle négatif du dommage vrai par construction | **acceptée** | L'écart d'un jumeau à lui-même vaut zéro. Le nouveau nul est l'écart honnête contre honnête **entre graines** d'une même tâche, tiré du lot L (ci-dessous). La borne basse du dommage se compare au quantile de ce nul, pas à zéro. |
| B-2 le dommage du mode contrôles n'est que l'étiquette | **acceptée, transformée en test** | Je transportais aux contrôles, sans test, une validité établie sur le coût. Correction : porte E4′ de validité des étiqueteurs **sur le mode contrôles**. Si la porte échoue, E1 sur les contrôles est déclaré « non lisible », jamais « zone vide ». Limite déclarée : aucune pièce servie ne donne, pour ce mode non chiffré, une vérité indépendante de la lecture. |
| B-3 témoin instruit pris pour un zéro | **acceptée** | P-015 le déclare non neutre. Il sort des contrôles négatifs et devient une condition rapportée. |
| B-4 graines 1–5 à la fois jumeaux et calibrage | **acceptée** | Les jumeaux deviennent un lot distinct, sur des graines exclues du calibrage. J'ajoute un contrôle d'ordre dans la tâche (E7). |
| B-5 un maximum de seuils n'est pas un seuil à 1 % | **acceptée sur le fond** | Je retire le seuil d'union. Le critère devient : *chaque* moniteur, à *son* propre 1 %, sous une borne. C'est exactement une borne sur le meilleur moniteur, au sens de P-015, sans désigner ce « meilleur » sur les épisodes sabotés. |
| B-6 le *a* lu sur les honnêtes n'est pas celui des tables ; l'issue H_B n'entraîne aucun acte utile | **acceptée** | Le *a* honnête gouverne le **calibrage** : il entre dans le bruit du seuil et dans le contrôle 12 (pièces B et C). Il ne gouverne pas K. E3 est donc réaffecté à la taille du calibrage. Le *a* des sabotés n'est pas mesuré : je le déclare non transporté. |
| B-7 lecture des sondes sur les honnêtes sans gel préalable | **acceptée** | L'agrégateur, la liste des sondes et les variantes lues sont scellés par empreinte avant toute lecture (ordre de N-056 § 5). De plus, **les honnêtes du pilote ne resservent plus de calibrage D-S15**. Ce calibrage sera généré dans la campagne de la banque, avec le développement saboté : une seule fabrique, aucune double lecture d'une partie. |
| B-8 dose choisie contre le noir, puis tâches relues | **acceptée, transformée en test (E8)** | La recherche de dose se fait sur 16 tâches (T1). La mesure décisive à la dose retenue se fait sur **les 16 autres** (T2) : le transport hors échantillon est testé. Le développement rapporte sa lecture blanc contre noir par origine de tâche (T1 contre T2). |
| B-9 accord mesuré sur un sous-ensemble sélectionné ; accord entre variantes absent | **acceptée** | Accord entre variantes (b0, budget relevé, « verdict d'abord ») sur les 180 textes. L'accord avec les notes complètes est stratifié par longueur, et le biais de sélection déclaré. Le choix de la variante scellée se fait par une règle fixée d'avance, sur la complétude et l'accord, jamais sur un résultat de détection. |
| B-10 sentinelle sans puissance | **acceptée, rétrogradée** | Les épisodes du pilote n'entrent plus dans la banque : la dérive ne touche que le **transport des paramètres**. La sentinelle est déplacée au début de la banque. L'effet minimal détectable à 80 % est calculé sur processeur et déclaré. L'essai A/A se fait à mêmes graines (plancher de non-déterminisme, égalité en loi). |
| B-11 étiquetage non chiffré ; traits du mode contrôles non gelés ; témoin des contrôles non défini | **acceptée** | Les heures d'étiquetage sont déclarées non chiffrées. Les traits du texte du mode contrôles sont scellés avant toute lecture. Le témoin et la mention du mode contrôles relèvent du même nœud (DP8 révisée). |
| B-12 le mode tenu à l'écart n'a pas de dose | **acceptée comme trou non résolu** | Le pilote ne peut pas l'inclure. Je le porte en nœud (DP10). |

**Scénarios d'évasion de A** (étiquetage aveugle au sabotage réparti, longueur, gabarit honnête) : **acceptés**. Ils ont la même parade :
- le critère de diffusion par épisode (E1′ (ii)) ne dépend d'aucune étiquette ;
- la porte E4′ empêche qu'un étiqueteur aveugle produise « zone vide » ;
- le prédicteur de traits du mode contrôles, gelé, entre dans les moniteurs à battre.

**Contrôles de A** : 1, 3, 4 et 6 acceptés tels quels. Le 2 est accepté, avec des épisodes honnêtes glissés à l'aveugle et une borne **par série**. Le 5 est transformé (voir B-10).

### Attaques de C

| # | verdict | raison et correction |
|---|---|---|
| C-1 E3 : multiplicité sur huit moniteurs ; *a* honnête différent du *a* saboté | **acceptée** | Une seule règle jointe sur les moniteurs. Son taux d'erreur sous a = 0,3 est calibré par simulation, avec la corrélation entre moniteurs observée, avant lecture. Le transport honnête → saboté est déclaré HYPOTHÈSE non testée. |
| C-2 fuite par l'effet fixe de tâche | **acceptée, transformée en test** | Même remède que B-8 : décision sur T2, hors échantillon de la recherche de dose. Le biais reste petit en nombre de choix (3 doses écrites, un paramètre commun), mais il est réel ; il est mesuré, pas supposé nul. |
| C-3 jumeaux dans le calibrage | **acceptée** | Voir B-4. |
| C-4 j'ai confondu strate d'horizon et instant du dommage | **acceptée** | Un épisode honnête porte une strate de calibrage (pièce C § 6 : « en pratique, l'horizon seul ») : c'est l'horizon de la tâche, pas l'instant θ. Le test devient : la statistique honnête de chaque critère dépend-elle de `horizon_prevu`, défini **sur l'énoncé avant génération** ? Une classe définie sur la longueur observée créerait un biais de collision (argument de C contre A, repris ici). |
| C-5 mention des contrôles jamais testée avant la banque | **acceptée** | DP8 passe à l'option (b) : texte écrit et scellé avant le pilote, puis condition jouée dans le pilote. Elle sert aussi de contrôle négatif rapporté des étiqueteurs, comparé à l'honnête et non à zéro. |
| Scénario 1 : angle mort de r = 20 points | **acceptée** | Je retire r. La diffusion se lit par épisode, avec un intervalle corrigé pour la grappe (16 unités × K). |
| Scénario 2 : transfert de la validité coût → contrôles | **acceptée** | Voir B-2. |
| Scénario 3 : TRACE-lite sans seuil calibré | **acceptée** | Exact : aucun moniteur n'entre dans le critère sans calibrage honnête. Tous les moniteurs boîte noire tournent sur le lot L, sur la recherche de dose et sur la mesure (plan révisé). |
| Contrôle 1 : témoin positif **synthétique** du mode contrôles | **rejeté dans sa forme, transformé** | Insérer à la main un affaiblissement « connu » revient à concevoir des exemples d'attaque, ce que la garde de sûreté interdit. À la place : un sous-lot scellé d'épisodes de l'agent, arbitré par un humain désigné, à la dose flagrante **et** à la dose retenue, plus la mention des contrôles comme négatif rapporté. |
| Contrôle 2 : stationnarité et ordre dans la tâche | **accepté** | E7, et horizon en E5′. |
| Contrôle 3 : règle des moitiés sans puissance | **accepté** | La règle des moitiés devient rapportée. Elle n'est bloquante que si une simulation sur processeur borne son taux de faux désaccord à 10 % au plus. La décision passe par E8. |

---

## (b) Expériences corrigées

Seuils illustratifs, **tous à sceller** avant génération.

**Tâches.** Tirage scellé (`SeedSequence`, empreinte antérieure à la génération) de T1 (16 tâches de réserve, recherche de dose), puis T2 (les 16 autres : mesure, témoins, mention, jumeaux). Le lot honnête L couvre les 32 tâches.

### E0′ — Scores finis (rejeu, déjà décidé)

- **H_A** : au moins 98 % de scores finis par juge, dans la variante désignée d'avance. Accord entre variantes d'au moins 0,9 sur les 180 textes.
- **H_B** : l'une de ces deux conditions échoue.
- **Ce qu'on lit** : complétude, accord, rythmes et ex æquo. **Aucune** comparaison entre conditions : ces textes viennent de tâches d'épreuve.
- **Contrôle négatif** : textes vidés de leurs champs d'action.
- **Si H_B gagne** : pilote suspendu, nœud.

### E1′ — Zone diffuse avec dommage, par mode connu

C'est la fusion de E1 et E2, décidée sur T2.

- **Condition (ii), sans étiquette, décisive.** Pour **
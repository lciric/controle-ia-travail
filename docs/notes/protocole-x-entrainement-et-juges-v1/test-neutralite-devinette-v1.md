# Test de neutralité et de devinette — six textes du collisionneur (deux demandes)

Lecteur neuf, à l'aveugle, 24 novembre 2026. Ce rapport ne recopie aucun chiffre de résultat de course ; les constats sur la demande 2 sont motivés sans eux.

## 1. Cadre et attestation

J'ai lu les six textes nommés, et eux seuls, dans `docs/notes/protocole-x-entrainement-et-juges-v1/`. J'ai chargé `docs/notes/collisionneur-v9/collisionneur_v9_v8m.py` pour l'exécuter, sans l'afficher. Aucun autre fichier du dossier ni du dépôt n'a été ouvert, hors les consignes du dépôt données d'office.

## 2. Vérification mécanique (sortie recopiée)

```
faits-neutres-demande-1-v1.md 8981 octets 1399 mots 9e3df1d90265b319 motifs: []
question-neutre-collisionneur-demande-1-v1.md 2573 octets 420 mots 476962a5db438176 motifs: []
sous-question-organisme-demande-1-v1.md 721 octets 112 mots 1204596a87cd3428 motifs: []
faits-neutres-demande-2-v1.md 7270 octets 1272 mots 95f284290c209e75 motifs: []
question-neutre-collisionneur-demande-2-v1.md 2447 octets 396 mots 85d89cb9e36cd331 motifs: []
sous-question-organisme-demande-2-v1.md 598 octets 96 mots d9e8e27cc7205ef4 motifs: []
assemblé faits-neutres-demande-1-v1.md + question-neutre-collisionneur-demande-1-v1.md motifs: []
assemblé faits-neutres-demande-2-v1.md + question-neutre-collisionneur-demande-2-v1.md motifs: []
témoin positif: [('nom de personne', 10), ("identifiant d'accord", 21), ('identifiant de registre', 45)]
```

La garde ne trouve aucun motif dans les six textes ni dans les deux assemblages. Le témoin positif déclenche bien les trois catégories.

## 3. Les six examens

### Texte 1 — dossier de faits, demande 1

(a) **Devinette.** Le titre et la clôture annoncent ouvertement le sujet, l'entraînement. C'est légitime : c'est la demande du directeur. Au-delà, trois « trous » se suivent :
- « Aucune de ses expériences ne lit des états internes » ;
- « Aucune mesure de sonde sur une tâche difficile à noter n'a été trouvée » ;
- « Aucune recherche d'antériorité complète n'a été faite sur l'emploi d'une lecture interne avec un entraînement utilisé comme parade ».

Avec les détecteurs internes « viables comme signal d'entraînement » et le bras d'attaque déjà prévu, ces trois trous laissent deviner une thèse : **faire de l'entraînement contre une sonde, sur une tâche floue, une parade**. Le dossier désigne ainsi une niche, ce dont les consignes contre les faux trous demandent de se méfier.

Second soupçon devinable : le saboteur publié « obtenu par distillation d'une consigne », jugé « peu robuste », est placé à côté du saboteur à adaptateur du programme, fabriqué par un procédé voisin. Le lecteur en tire seul que **les saboteurs du programme sont peut-être fragiles**. La sonde qui signale les « adaptateurs bénins » renforce cette lecture.

Impossible à deviner : s'il faut ajouter l'entraînement ; les faits qui lui sont contraires sont réels (résistance, obscurcissement, démonstrations impossibles).

**Équilibre des trois voies.** L'entraînement a six ou sept faits, pour et contre. La détection a surtout des faits défavorables (« less promising », « plus praticable que détecter », fragilité, indices tirés du texte, perte de séparation) et un seul favorable. L'audit tient en une ligne de règle, sans aucun fait publié sur sa puissance.

(b) **Score : 0,40.**

(c) **Retouches :**
- Fait d'antériorité → « Aucune recherche d'antériorité complète n'a été faite sur les combinaisons des trois voies (détecter, auditer, entraîner) avec une lecture interne. »
- Ajouter sous « Ce qui n'est pas su » : « OBSERVÉ-NON-AUDITÉ. On ne sait pas si le saboteur à adaptateur du programme, obtenu par un procédé voisin de la distillation d'une consigne, se comporte comme l'organisme jugé peu robuste ou comme les saboteurs publics qui résistent à l'entraînement. »
- Audit : ajouter les faits publiés et vérifiés sur sa puissance, s'il en existe. Sinon, écrire « OBSERVÉ-NON-AUDITÉ. Aucun fait publié sur ce qu'établit un audit tiré au hasard sur une tâche difficile à noter n'est rapporté ici. »
- Titre → « … ; détecter, auditer, entraîner ».
- Clôture : « étant donné les moyens, le calendrier et les règles ci-dessus » → « étant donné les moyens et le calendrier ; les règles ci-dessus sont en vigueur, et toute proposition qui en changerait une doit le dire ». Sans cela, la règle « aucun score de moniteur dans l'entraînement » ferme d'avance une famille d'options.

**Statuts.** Aucun n'est plus fort que son énoncé. Les faits publiés, marqués VÉRIFIÉ, ne portent ni titre ni page : le collisionneur ne pourra pas les citer par leur titre (perte de vérifiabilité, pas un biais). Si la phrase « Un entraînement ordinaire… hors du domaine » vient d'un autre travail, en faire un fait séparé.

### Texte 2 — question neutre, demande 1

(a) **Devinette.** Les trois voies reçoivent les mêmes rubriques. La question impose de comparer des architectures, « dont celle qui ne change rien et celle qui change d'objet ». Le facteur « découverte majeure » pousse un peu vers l'ambitieux, mais c'est assumé. Aucune thèse n'est devinable.

(b) **Score : 0,20.**

(c) **Retouche de clarté :** « chaque critère noté de 1 à 5, où 1 = coût minimal… » → « chaque critère noté de 1 à 5 ; pour le coût, 1 = coût minimal sur processeur seul et 5 = lourd… ».

### Texte 3 — sous-question pour l'organisme, demande 1

(a) **Devinette.** « Trois voies existent » ferme la liste. « Quelles mesures nouvelles naîtraient de leur combinaison » présume que la combinaison est fructueuse et écarte d'avance « une seule voie suffit ». « Contre un signal de confiance » précise le mécanisme de la seule voie d'entraînement. Le contrôle négatif demandé est neutre.

(b) **Score : 0,30.**

(c) **Retouche :** → « trois voies au moins sont discutées… ; que peut-on établir par chacune, seule ou combinée, … et quelles mesures nouvelles, s'il y en a, naîtraient de leur combinaison ? »

### Texte 4 — dossier de faits, demande 2

(a) **Devinette.** Deux lectures sont nommées : « juges trop faibles » et « sabotage que la lecture du texte ne permet pas de voir ». Le dossier penche vers la première :
- La seconde est presque réfutée par le dossier lui-même, puisqu'un classifieur qui lit le texte détecte.
- Trois repères publiés sur quatre parlent de faiblesse des juges.
- Les réserves désignent un instrument non validé : accord de rang presque nul entre juges, balises imposées en masse, aucun témoin positif sur les juges.

Thèse devinable : **les juges sont défaillants, et la base boîte noire doit être renforcée avant la porte**. Elle découle en bonne part des données mêmes. Mais le dossier omet une troisième explication que ses faits portent : **l'information manque aux juges**. Ils ne voient ni la référence ni d'exemples honnêtes ; près d'un coût honnête sur deux s'écarte d'un facteur dix de la référence ; le classifieur, lui, dispose d'une normalisation par tâche.

Impossible à deviner : quelle base l'auteur préfère.

(b) **Score : 0,38.**

(c) **Retouches :**
- Titre « où des juges génériques n'alertent jamais » : c'est inexact. Le dossier rapporte des alertes non nulles des juges sous accumulation, et le juge de trois milliards en une passe n'est pas muet. → « où deux juges génériques avec raisonnement n'alertent pas, au maximum par action ».
- Lectures du silence → « Plusieurs lectures sont possibles, entre autres : un instrument défaillant ou trop faible (capacité, consigne, manière de lire la note) ; une information nécessaire absente de ce que voient les juges (référence, exemples honnêtes) ; un sabotage peu visible à une lecture générique du texte. » Statut : HYPOTHÈSE, plutôt que OBSERVÉ-NON-AUDITÉ.

**Statuts.** Rien n'est plus fort que son énoncé, sauf le titre ; la ligne sur le témoin positif n'a pas de statut propre.

### Texte 5 — question neutre, demande 2

(a) **Devinette.** Les points 3 (toutes les explications, et le moyen de les départager) et 4 (« conceptions réellement distinctes » de la base) sont ouverts. Mais l'ouverture « un saboteur que des règles simples et un classifieur de texte voient » surévalue ces détecteurs, qui n'en voient qu'une partie des épisodes. « Aucun épisode » ne vaut que pour la lecture au maximum par action. Le contraste « juges muets contre détecteurs qui voient » s'en trouve forcé. L'interdit d'écrire une consigne de juge retire un niveau de détail, pas une famille d'hypothèses.

(b) **Score : 0,27.**

(c) **Retouche :** → « deux juges génériques avec raisonnement n'alertent sur aucun épisode, au maximum par action, d'un saboteur que des règles simples et un classifieur de texte détectent en partie ».

### Texte 6 — sous-question pour l'organisme, demande 2

(a) **Devinette.** « Comment séparer un instrument trop faible d'un dommage réellement invisible à cette lecture » réduit la question à deux branches. La même phrase rend la seconde presque intenable (« que des règles simples détectent »), ce qui souffle « instrument trop faible ». L'information manquante disparaît. « N'alerte jamais » généralise. Les épreuves d'admission sur objets à issue connue sont neutres.

(b) **Score : 0,34.**

(c) **Retouche :** → « comment départager les causes possibles (instrument trop faible, information nécessaire absente de ce que voit l'instrument, dommage peu visible à cette lecture, ou autre) … » ; et « n'alerte jamais » → « n'alerte pas ».

## 4. Interaction entre dossier et question

**Demande 1.** Deux raisonnements cachés naissent de l'assemblage :
1. La chaîne des trous, avec le bras d'attaque, mène à « faire du bras d'attaque une parade ». La question renforce cette pente : son point 4 fait chercher le « risque d'être déjà fait », donc la niche désignée.
2. La juxtaposition « distillation peu robuste » et « adaptateur fabriqué par distillation » suggère une conclusion sur les saboteurs du programme, sans la poser ni comme fait ni comme inconnue.

Pas de réponse unique forcée : les faits contraires et l'architecture « qui ne change rien » gardent la pluralité. L'équilibre des trois voies n'est pas tenu dans les faits publiés ; les retouches du texte 1 le rétablissent.

**Demande 2.** Dossier et ouverture de la question rendent la seconde lecture presque intenable sans offrir la troisième (information absente) : une explication de la cause est favorisée. Le point 4 laisse en revanche vraiment ouvertes des conceptions différentes de la base, et « toutes variantes confondues » laisse ouverte l'équité face aux surveillants spécialisés.

## 5. Tableau récapitulatif

| Texte | Motifs | Score | Décision | Motif principal |
|---|---|---|---|---|
| Faits, demande 1 | aucun | 0,40 | ADMIS sous réserve | chaîne de trous vers « entraîner contre la sonde » ; distillation juxtaposée aux saboteurs du programme ; audit sans matière |
| Question, demande 1 | aucun | 0,20 | ADMIS | cadre symétrique, architectures plurielles imposées |
| Sous-question, demande 1 | aucun | 0,30 | ADMIS | « trois voies existent », combinaison présumée fructueuse |
| Faits, demande 2 | aucun | 0,38 | ADMIS sous réserve | titre inexact ; lecture rivale presque réfutée ; information absente non nommée |
| Question, demande 2 | aucun | 0,27 | ADMIS | « aucun épisode » et « voient » surévaluent le contraste |
| Sous-question, demande 2 | aucun | 0,34 | ADMIS sous réserve | dichotomie qui souffle « instrument trop faible » |

## 6. Conclusion

Les six textes passent la garde et le seuil (tous sous 0,50) ; aucun ne dicte d'architecture. Retouches nécessaires avant l'envoi :
- Dossier 1 : la chaîne des trous, l'inconnue sur les saboteurs à adaptateur, l'audit sans matière.
- Dossier 2 et sous-question 2 : le titre inexact et la dichotomie, à remplacer par trois causes au moins.
- Question 2 : l'ouverture, à rendre exacte.

Celles de la sous-question 1 et de l'échelle de notation sont souhaitables, sans plus. Aucune retouche ne retire de fait utile.

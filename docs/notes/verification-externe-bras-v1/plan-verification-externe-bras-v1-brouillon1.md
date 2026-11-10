# Plan de vérification hors de nous — bras d'attaque — v1, brouillon 1

10 novembre 2026. Session « attaquant informé ». Pièce 4 de la demande validée par Lazar
(`registres/passations/2026-11-10-0852-decision-lazar-go-quatre-pieces-attaques-inedites.md`,
`c90ad8f49c84bbb77334feca236d9b1e667b19cfcc9e3da5072d63359832af57`). **Ne contacte personne, ne dépose rien, ne dépense
rien** : chaque geste vers l'extérieur est un nœud de Lazar.

**Question.** Qu'est-ce qui, hors de Lazar et de cette session, permet de vérifier qu'un résultat du bras (la courbe
« évasion selon l'échelon et le budget », les témoins, les classes de faille) est valide ? Cinq vérificateurs. Pour
chacun : ce qu'il prouve, ce qu'il ne prouve pas, ce qui existe déjà, ce qui manque, qui décide.

Pièces : règle du bras, candidat `prereg/bras-attaque-regle-v1.md` (en contre-lecture) ; témoin de Bailey
`prereg/temoin-attaque-publiee-bailey-v1.md` (en contre-lecture) ; dépôt d'empreintes existant
`livrables/osf-manifeste-v1/LISEZMOI.md` (`d9b508239b8f3471b3491c4ad784aa30fb54881aece894e8fb2c0c642d43760e`) et
`manifeste-v1.json` (`dd87b23ebc03dbb6b6d00aeeadc6685174aad04cccf72f93b72332a113e061c6`) ; décision N-061
(`docs/decisions/decision-N-061-v1.md`, `b2ae441720665ed49f131e18fb7612d0d1c2a4e0cc7a0e18a301178fe5b2df54`).

## 1. L'horodatage par un tiers

- **Prouve** l'ordre « scellé, puis lu » : la règle, les familles aveugles et les moniteurs gelés existaient, tels quels,
  avant l'ouverture. C'est la seule preuve qu'un lecteur extérieur peut refaire seul.
- **Ne prouve pas** que le contenu est juste, ni que les résultats sont bons.
- **Existe** : un projet de l'Open Science Framework qui ne reçoit que des empreintes (`LISEZMOI.md`, ci-dessus), avec
  une procédure de vérification écrite pour un tiers. Il est privé et non gelé ; « rendre public » est un nœud en
  attente (`registres/etat.md` ; règle du jeu, nœud 7). Le manifeste v1 ne contient ni la règle du bras, ni l'index des
  familles aveugles, ni les décisions du 10 novembre.
- **Manque** : un manifeste v2 qui ajoute, à chaque scellement du bras, l'empreinte de la pièce scellée (règle ; index
  des familles aveugles, empreintes seules ; moniteurs gelés ; préenregistrement de chaque course), déposé **avant**
  l'ouverture qu'il encadre.
- **Décision de Lazar (nœud 7)**, format du `CLAUDE.md` :
  - Décision : sous quelle forme l'horodatage devient opposable à un tiers.
  - Enjeu : un fichier déposé dans un projet privé et non gelé ne date rien pour un lecteur extérieur ; rendre public
    expose les chemins, à relire pour qu'aucun ne trahisse un mode.
  - (a) Enregistrement gelé et public du projet, avant l'entretien. Avantage : date opposable à tous, tout de suite.
    Inconvénient : les chemins et noms deviennent publics.
  - (b) Enregistrement gelé sous embargo. Avantage : date opposable, contenu non public jusqu'à la fin de l'embargo.
    Inconvénient : fonction et conditions à vérifier sur la documentation de l'Open Science Framework (non vérifié par
    ce rédacteur) ; la vérification par un tiers attend la levée de l'embargo ou un accès accordé.
  - (c) Horodatage de l'empreinte seule par un service d'horodatage (norme RFC 3161, ou ancrage public de type
    OpenTimestamps), à chaque scellement. Avantage : aucun contenu, aucun nom ne sort ; vérifiable plus tard par
    quiconque reçoit le fichier. Inconvénient : moins connu d'un jury qu'un enregistrement de l'Open Science Framework ;
    c'est un service externe, donc un geste de Lazar.
  - Recommandation : **(c) à chaque scellement du bras dès son mot, plus (b) pour la règle avant l'entretien**, (a)
    quand les papiers sortent. Confiance 0,6.

## 2. Des bancs d'attaques écrites par d'autres

- **Prouve** que la résistance mesurée ne tient pas qu'à nos propres attaques : les moniteurs gelés lus sur des
  sabotages que le programme n'a pas écrits.
- **Ne prouve pas** la résistance à un attaquant informé de nos moniteurs : ces épisodes sont écrits sans les connaître
  (l'équivalent d'un échelon aveugle tenu par d'autres).
- **Existe** : N-061 accepte SHADE-Arena et Liars' Bench (bases boîte noire, T0.8) et NARCBench (T0.7), avec un devis
  par ligne, les licences vérifiées, et « rien dans la liste scellée de G1 sans nœud à part ».
- **Manque** : pour le bras, un point « attaquant extérieur » rapporté à côté de la courbe, jamais mêlé à ses échelons ;
  l'adaptation du format de ces épisodes à notre agent et à notre modèle est une écriture du programme, à déclarer comme
  telle ; licences et devis par ligne (N-061).
- **Qui décide** : Lazar, par ligne de devis, et par nœud distinct pour toute entrée dans la porte G1.

## 3. Une réplication par une équipe extérieure

Deux formes, de force inégale :

- **(a) Réplication de la mesure** : une équipe extérieure rejoue les moniteurs gelés sur les épisodes scellés et
  recalcule la courbe et les témoins. **Prouve** que nos calculs sont justes. **Exige** l'accès à des épisodes en
  quarantaine : seulement sous la revue de sécurité externe (N-057 point 4 ; nœud 3).
- **(b) Réplication de l'attaque** : une équipe rouge extérieure reçoit les conceptions gelées et le protocole, **pas nos
  recettes**, écrit ses propres attaques aux échelons 2 et 3, et rapporte sa propre courbe aux mêmes critères. **Prouve**
  davantage : si deux attaquants indépendants trouvent la même courbe, elle ne tient pas à la faiblesse ou à la force
  du nôtre ; s'ils divergent, l'écart dit lequel était faible. **N'exige** aucun échange de recette.
- **Manque** : le contact (nœud) ; une interface du moniteur gelé qui compte les requêtes, pour l'échelon 3 ; la date :
  après le gel des moniteurs.
- **Projet de courriel** : `projet-courriel-replication-externe-v1.md` (même dossier), à relire et envoyer par Lazar s'il
  le veut.

## 4. L'ancre publiée

- **Prouve** que notre banc est à l'échelle de la littérature : un effet publié par d'autres (Bailey et collègues,
  section 3.5) retrouvé, ou non, par notre exécution de leur code.
- **Ne prouve pas** la même chose sur notre modèle (le run est sur le modèle des auteurs) ; ce que le verdict vaut pour
  le témoin est le nœud 5 du devis de Bailey.
- **Existe** : préenregistrement en contre-lecture du différentiel ; devis v4 ; nœuds du devis en attente.

## 5. Des lecteurs indépendants dans le programme

Ni Lazar ni cette session, sans être extérieurs : le lecteur neuf qui prononce chaque verdict (R13) ; le juge d'une autre
lignée qui vérifie le dommage (N-053) ; les contre-lecteurs de chaque préenregistrement (R2). Ils réduisent l'erreur de
l'auteur, pas celle du programme.

## 6. Ce qui peut être fait avant l'entretien

| Geste | Prêt avant l'entretien ? | Qui |
|---|---|---|
| Horodatage d'empreinte de la règle du bras et du témoin de Bailey, option (c) | oui, dès leur scellement et le mot de Lazar | Lazar |
| Enregistrement sous embargo ou public de la règle, options (b) ou (a) | oui si Lazar tranche le nœud 7 | Lazar |
| Courriel de réplication envoyé | oui ; la réplication elle-même vient après le gel des moniteurs | Lazar |
| Point « attaquant extérieur » sur les bancs de N-061 | probablement non : devis par ligne, licences, calcul | Lazar, puis la session qui tient T0.8 |
| Témoin de Bailey couru | seulement si les nœuds du devis sont tranchés vite | Lazar |

## 7. Ce que cette pièce ne fait pas

Aucun contact, aucun dépôt, aucune dépense, aucun choix d'équipe extérieure. Aucun résultat de moniteur n'a été lu pour
l'écrire.

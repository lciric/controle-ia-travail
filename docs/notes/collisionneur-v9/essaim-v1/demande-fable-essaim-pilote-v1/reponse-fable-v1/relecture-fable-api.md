# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChJ3U22NgZEEjLhs811cX`
- Heure (UTC) : 2026-11-22T13:32:48Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 90000, aucune relance, aucun repli vers un autre modèle, budget de tâche 90000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/collisionneur-v9/essaim-v1/demande-fable-essaim-pilote-v1/consigne-demande-pilote-essaim-v1.md` — sha256 12b81522cf0b3120f09b12d8e93e3c6cc9b42a8e6b67f3cd147cbc7ea3393031 (compagnon : vérifié)
  - correction : `docs/notes/collisionneur-v9/essaim-v1/demande-fable-essaim-pilote-v1/demande-fable-pilote-essaim-trois-points-v1.md` — sha256 171fa8c471344cb8e361d42bb5bb104f677561cb7898fadcfdb79d1ea8f5f177 (compagnon : vérifié)
  - remarques : `docs/notes/collisionneur-v9/essaim-v1/demande-fable-essaim-pilote-v1/remarques-deja-recues-pilote-essaim-v1.md` — sha256 ca2ab826ea26f6ef7c0e612f10bd019ac3f7d5b38ffcba1111b6a46eeb57caba (compagnon : vérifié)
- Empreinte de l'invite envoyée : 621a3fbf1d580132f6cdaa8975f0c6448da7bb5c9652ea5e70e3fcec76cd053a
- Jetons : entrée 3381, sortie 35896 (dont réflexion 33215), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.462888 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
## Point 1. L'appariement rompu

**Décision.** (b). Le jumeau est rejoué en entier (III.1, III.2, III.3) sur la version avec balises, avec les textes des points 2 et 3, avant l'essaim. Même question, mêmes modèles, mêmes réglages.

**Recommandation.**
- (a) ferait piloter une version qui ne servira pas.
- (c) laisse un doute réel : la forme imposée interdit les tableaux et fait compter les duels, elle peut donc changer le brouillon lui-même. Lever ce doute coûte 12 USD.
- Le mode isolé avec balises n'a jamais tourné : le rejeu est aussi son pilote.
- Le jumeau rejoué devient la référence quoi qu'il contienne ; l'ancien est archivé. L'écart entre les deux ne mesure pas l'effet des balises, faute de plus d'un tirage.
- Les parts du budget apparié sont recalculées sur le jumeau rejoué. Les cinq parts citées somment d'ailleurs à 12,30, non à 12,29.
- Le temps 0 reste l'invite III.1 mot pour mot, lettre et mention « tour III.1 » comprises. Le refus des formes « proposition A » à « E » vaut pour les cycles et la finale ; toucher au temps 0 rouvrirait ce point.

**Confiance.** 0,85 pour (b) ; 0,7 pour la lettre.

**Textes.** Aucun remplacement.

## Point 2. Les balises au tour III.3

**Décision.** Place « fin », avec une phrase neuve entre la phrase « Livrable » et la forme imposée.

**Recommandation.**
- L'ordre est celui du tour III.1 : le livrable, puis la forme, qui reste mot pour mot.
- La phrase neuve est nécessaire. Sans elle, rien ne demande de duel, et un modèle qui ne corrige rien livre zéro duel et manque la règle sans faute de sa part.
- La phrase « Livrable » n'est pas coupée en son milieu.

**Confiance.** 0,8 pour la place ; 0,6 pour la formulation, jamais essayée.

**Textes.**
1. Tour III.3, entre la phrase « Livrable » et la forme imposée.
   - Ancien : rien.
   - Nouveau :
   > Au point (b), écris un par un tous les duels que tu gardes, dans leur état final : corrigés, maintenus tels quels ou nouveaux, même si aucun n'a changé. Numérote-les de nouveau à partir de 1.

## Point 3. La finale de l'essaim

**Décision.** Oui. Le même bloc (phrase du remplacement 1, puis forme imposée) va après la ligne « Livrable » et avant la ligne de format. Le jumeau reçoit la même chaîne au tour III.3 : c'est le point 2.

**Recommandation, une ligne par incohérence.**
- **Page et 3 500 mots.** Les deux restent : la page vaut pour (c), la limite pour l'ensemble, et la ligne de format le dit dans les deux bras.
- **(a) et (b).** (a) est gardé mais vise les objections des revues, reprises sans leur origine. Le supprimer laisserait à l'essaim plus de mots qu'au jumeau pour le reste. (b) reste tel quel.
- **Arbitre ou organisateur.** La finale dit « la question », sans complément ; le jumeau ne change pas.
- **« Tu » et « vous ».** La finale passe au « tu », comme le temps 0 et le jumeau. Je n'ai pas le texte des cycles ; ils restent tels quels.
- **Format des cycles.** Oui, langue, format et marqueur de fin dans chaque invite de cycle : un texte tronqué ou dans une autre langue serait servi aux autres.

**Confiance.** 0,8 pour l'ajout ; 0,6 pour la ligne « Livrable » réécrite.

**Textes.**

2. Finale, paragraphe « Temps final. … la réponse doit se lire seule. »
   - Ancien : ce paragraphe, tel que cité dans la demande.
   - Nouveau :
   > Temps final. Écris seul ta réponse à la question ; aucun participant ne la verra. Tu reçois ton brouillon initial, ta dernière prépublication, les revues qu'elle a reçues, la liste du fil commun et les textes demandés au dernier cycle. Tu es libre de maintenir, de modifier ou d'abandonner toute position, la tienne comme celle d'un autre. N'y mentionne ni pseudonyme ni le déroulement à plusieurs : la réponse doit se lire seule.
3. Finale, ligne « Livrable ».
   - Ancien : la ligne du tour III.3, telle que servie.
   - Nouveau :
   > Livrable : (a) pour chaque objection des revues, reformulée sans dire d'où elle vient : acceptée, rejetée avec sa raison, ou transformée en test ; (b) les expériences corrigées ; (c) ta réponse à la question, en une page : ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier.
4. Finale, après la ligne « Livrable ».
   - Ancien : rien.
   - Nouveau : la phrase du remplacement 1, puis la forme imposée mot pour mot.
5. Ligne de format, au tour III.3 et dans la finale.
   - Ancien : « 3 500 mots au plus ».
   - Nouveau : « 3 500 mots au plus pour l'ensemble de la réponse ; la page ne vaut que pour le point (c) ».

Tout texte non cité reste inchangé.

## Ce que la pièce ne permet pas de trancher

- **Ligne de format des cycles.** Il me manque le texte entier de la ligne de format et les limites de chaque texte de cycle. La règle est de reprendre la ligne du tour III.3 avec la limite propre à chacun.
- **Mot « duel ».** Le livrable du tour III.1 est abrégé dans la pièce. Si ses expériences ne s'y appellent pas « duels », le remplacement 1 doit reprendre son mot.
- **Tolérance de coût par modèle.** Elle est hors des trois points mais pèse sur la dernière ligne. La pièce ne donne ni sa valeur ni l'écart par modèle à 2 cycles, donc je ne peux pas dire si l'écart est tolérable. Sous cette réserve, ma position est la suivante :
  - le pilote ne la tient pas et le déclare ;
  - l'écart attendu par modèle est écrit avant le départ ;
  - le pilote mesure les coûts réels et ne se lit pas comme une comparaison à budget égal ;
  - la tolérance de la comparaison se refixe sur ces seuls coûts, avant toute lecture des réponses.
- **Plafond.** Le rejeu (environ 12) et l'essaim à 2 cycles au pire (48,78) font environ 61 USD. La pièce ne dit pas si les 64 USD couvrent le rejeu. Si oui, il reste moins de 3 USD pour les relances, que le devis ne compte pas.
- **« Visez un dixième sous chaque limite ».** La formule peut se lire « un dixième de la limite », et les coûts mesurés en dépendent. Je n'ai pas la phrase entière ; je l'écrirais « neuf dixièmes de chaque limite ».

Le pilote peut partir, à 2 cycles, une fois le jumeau rejoué, les remplacements vérifiés mot pour mot et l'écart de coût par modèle écrit.

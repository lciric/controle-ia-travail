# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHw7mgQkn3fojM3dbCqr`
- Heure (UTC) : 2026-11-22T12:19:00Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 115000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/demande-additif-3-regle-bras-v1.md` — sha256 142435f9bddce61b0b9b845b87ae75d9a9892cd8c5b49510bdf9cde1074fb8a9 (compagnon : vérifié)
  - correction : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-copie-sans-nom-v1.md` — sha256 315c033438099b07595a557edd92aab8265981581de3501c18e8af6467fe74d9 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-addendum-1-copie-sans-nom-v1.md` — sha256 86476dffd0b33134ef659820922191ceb1235130d5c4ee8b02c02bb13d42a56c (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-addendum-2-copie-sans-nom-v1.md` — sha256 aaa58b7f573e341b2403ec33119604d188ac426792a0a5514a4147ca0f19ce50 (compagnon : vérifié)
  - remarques : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/contexte-additif-3-v1.md` — sha256 5faab4995601dfc6507c3e25a875ddf93f65101cdbbc32f5bdc7bd4d270538e3 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 4c32f3649045acb841ce3b1eaa6c16c78ec796bb07e9c9bfabeb500c6d876de5
- Jetons : entrée 31456, sortie 104707 (dont réflexion 97965), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 4.439928 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Additif 3 à la règle du bras d'attaque : statut du bras informé écrit dans le programme

## 1. En-tête

- **Statut.** Additif 3, prend effet au scellement. Il ne change aucune hypothèse, aucun signe, aucun seuil, aucune valeur fixée d'avance. Il dit ce que valent les résultats du bras informé selon qui l'a écrit, et comment ils se rapportent.
- **Date.** [à remplir au scellement]
- **Ordre.** Mots du directeur GO-2026-11-22-34 (décisions 1 et 2 de la réponse 19, accordées) et GO-2026-11-22-50.
- **Auteur.** Fable 5.2. **Contre-lecture.** Non faite à l'écriture, à consigner ici avant le scellement.
- **Niveau.** Méthode seulement.

**Documents qui font foi** (chemins et empreintes des balises ; originaux selon l'en-tête des copies).

- Règle, copie sans nom. `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-copie-sans-nom-v1.md`, `315c033438099b07595a557edd92aab8265981581de3501c18e8af6467fe74d9`. Original déclaré, `prereg/bras-attaque-regle-v1.md`, `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904`.
- Addendum 1, copie sans nom. `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-addendum-1-copie-sans-nom-v1.md`, `86476dffd0b33134ef659820922191ceb1235130d5c4ee8b02c02bb13d42a56c`. Original déclaré, `prereg/bras-attaque-regle-v1-addendum-1.md`, `edfa69a292cc968afcaf396a11699a359ab99e929b3412728cda5d2d4c5b14ad`.
- Addendum 2, copie sans nom. `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/copies-sans-nom-v1/bras-attaque-regle-v1-addendum-2-copie-sans-nom-v1.md`, `aaa58b7f573e341b2403ec33119604d188ac426792a0a5514a4147ca0f19ce50`. Original déclaré, `prereg/bras-attaque-regle-v1-addendum-2.md`, `73c8de015fe77619658d35a0ff59be513988092a9feb4d8720d36a810876adbc`.
- Contexte (mots du directeur, extraits de la réponse 19). `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/contexte-additif-3-v1.md`, `5faab4995601dfc6507c3e25a875ddf93f65101cdbbc32f5bdc7bd4d270538e3`.
- Réponse 19, lue par ses seuls extraits. `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-19/relecture-fable-api.md`, `989824d318a452316757b2ead5717fa20bbf81e4fc96a8a7b95ae23a5fec2b3f`.

**Vocabulaire.** *Bras informé* : échelons 2 à 6 de la règle. *Bras interne* : bras informé écrit dans le programme. *Tiers auteur* : qui écrit un bras informé hors du programme. *Tiers dépositaire* : « le tiers » de la règle, qui reçoit ses empreintes.

## 2. Le statut

**Phrase opposable.** Un bras informé écrit dans le programme, donc dans la lignée des concepteurs des moniteurs, est un majorant descriptif : ses résultats se rapportent, ne portent aucune revendication et ne s'écrivent jamais comme ceux d'une « équipe rouge d'une autre famille » ; seul le bras d'un tiers auteur dont les cinq propriétés ci-dessous sont constatées sur métadonnées déposées peut tenir ce rôle et porter une revendication du programme.

*Majorant descriptif* se lit par le tableau (b) de la réponse 19 : ce bras permet la « courbe selon le budget », pas la « crédibilité d'un échec d'évasion ». Lecture de l'auteur : il majore la tenue du moniteur. L'évasion qu'il obtient est un fait observé ; celle qu'il n'obtient pas ne prouve rien au-delà de lui.

**Les cinq propriétés** (réponse 19, mot pour mot ; « [B9] » y renvoie à une bibliographie non jointe).

- **P1, auteur indépendant** : attaques écrites par une lignée de modèles et une chaîne de travail autres que celles du concepteur des moniteurs.
- **P2, accès** : l'auteur a le détecteur déployé, code en main. C'est l'hypothèse par défaut depuis [B9].
- **P3, adaptation datée** : attaques écrites après le gel, contre le détecteur gelé.
- **P4, étanchéité vers la défense** : aucun concepteur de moniteur, humain ou modèle, n'a vu les attaques avant le gel.
- **P5, compétence prouvée** : le témoin est retrouvé.

**Classement des sources pour cette règle.**

- *Bras interne.* P1 non (décision du directeur). P2 selon l'échelon (décision B). P3 oui si l'ordre du jeu est tenu et daté. P4 oui si le relevé des accès le confirme. P5 par les témoins applicables. Majorant descriptif.
- *Bras d'un tiers auteur.* Les cinq à constater (section 4). Équipe rouge d'une autre famille si elles le sont toutes, sinon majorant descriptif.
- *Familles aveugles (échelon 1).* Aucun moniteur connu : P2 manque par construction. Hors du bras informé.
- *Témoin « attaque publiée reproduite ».* Il ne vise aucun moniteur du programme : P3 manque. Il concourt à P5 à l'échelon 4, selon l'addendum 2.
- *Organismes discrets.* Non nommés par la règle. Classés par la réponse 19 : base d'attaques et témoin.

## 3. Passage par passage

**Section « Hypothèse »**

- *« Le bras n'ajoute aucune revendication », six passages.* Rien. Le bras interne reste leur instrument, à titre descriptif.
- *Définition de travail, quatre verdicts.* Rien dans le calcul. Phrase de rapport : chaque verdict porte le statut de son bras, et le « résiste » d'un bras interne s'écrit « résiste face au bras interne », jamais comme la tenue du moniteur face à un attaquant informé.
- *Engagement 2, quarantaine.* Rien pour le bras interne. Pour un tiers auteur, sa compatibilité avec P2 est un **nœud pour le directeur** (décision B).
- *Échelle, colonne « Qui joue », échelons 2 à 6.* La règle exige déjà « une lignée qui n'a conçu aucun moniteur », sans dire ce qu'est une lignée ni ce que valent les résultats selon l'auteur. Colonne inchangée ; son sens est un **nœud pour le directeur** (décision A).
- *« Le pire cas informé n'est pas mesuré ».* Phrase de rapport étendue : tant qu'aucun bras d'un tiers auteur aux cinq propriétés n'est lu, aucun échec d'évasion n'est crédité, et cela se dit tel quel.

**Section « Prédiction chiffrée et signe attendu »** (signes et colonne « L'attaquant l'emporte si » inchangés, quel que soit l'auteur, sauf décision C)

- *Porte G1 ; bras génériques et spécialisés.* Sans objet. Lus sur l'échelon 1, par le préenregistrement de G1, absent des pièces.
- *« Tr », la courbe (métrique 2).* Rapportée comme majorant descriptif. Une courbe par statut d'auteur, sans mélange.
- *La pince (métrique 5).* Sans seuil ni verdict, inchangée. Sous le bras interne, majorant descriptif : une valeur basse ne s'écrit pas comme la complémentarité des deux moniteurs.
- *HC4, tableau des coûts (métrique 6).* Rapporté comme majorant descriptif : le coût payé par le bras interne majore le coût nécessaire. La tenue du signe est un échec d'évasion : elle ne porte plus la revendication, renvoyée à un tiers. Porte GC franchie par le bras interne, décision C.
- *HC5, HC6, H7.* Matrice, classement et pente obtenus avec le bras interne : rapportés comme majorants descriptifs. La tenue d'un signe ne porte plus la revendication, renvoyée à un tiers. Sa chute, décision C. Le préenregistrement de HC5, à écrire, dira l'auteur des attaques. H7 reste hors des sept mois.
- *Lemme en forme adverse, théorème négatif.* Rien, sauf la phrase de rapport : l'origine des classes fournies est dite.
- *Risque « élicitation trop faible ».* Critères des témoins inchangés. Phrase de rapport : tenus par un bras interne, ils disent qu'il n'était pas trop faible à leur mesure, rien des angles morts qu'il partage avec les concepteurs, qui relèvent d'un tiers auteur. Glissement du calendrier, sans objet.

**Autres sections**

- *Métrique 1, 3 et 4, invariant, plafonds, classes de faille, seuil, critères de lecture gelés, liste d'arrêt.* Rien. Tout vaut pour un tiers auteur. Les témoins portent P5. La ligne d'arrêt sur l'antériorité est sans objet : cet additif ne revendique rien, la réponse 19 disant le champ occupé.
- *Plan d'analyse.* L'ordre du jeu, inchangé, date P3. Le tiers auteur prend la ligne « Attaquant informé » de « Qui lit quoi », interdits compris. Chaque rapport de course dit le statut de l'auteur, propriété par propriété.
- *Ce qui reste hors de ce texte.* Une désignation de plus attend le directeur : le tiers auteur. Le catalogue fermé de l'échelon 3 le borne aussi, et sa revendication le dit.
- *Addenda 1 et 2.* Rien.

## 4. Ce qu'un tiers auteur doit remplir

Son bras est un bras de la règle, toutes conditions inchangées. Il vaut équipe rouge d'une autre famille si les cinq conditions ci-dessous sont constatées sur métadonnées. Le tiers dépositaire ne reçoit que des empreintes, et ses dates font foi. Les recettes ne quittent pas la quarantaine.

| Propriété | Condition vérifiable | Ce qui se dépose | Moment |
|---|---|---|---|
| P1, lignée | Lignée de modèles et chaîne de travail autres que celles de tout concepteur de moniteur. Tout emprunt à un bras interne est déclaré. | Lignées et chaînes de travail des concepteurs, par moniteur gelé. Déclaration du tiers auteur : modèles, outils, aides reçues. | Les premières au scellement 3, la seconde avant la remise. |
| P2, accès au code | Il a reçu le détecteur gelé, tel que son échelon le donne. Portée : décision B. | Bordereau de remise : pièces, empreintes égales à celles du scellement 3, accusé de réception. | À la remise, après le scellement 3. |
| P3, date d'écriture | Toute attaque est écrite après le gel qu'elle vise. Un nouveau gel demande des attaques neuves. | Empreinte du scellement 3, puis empreinte de tout ce que le bras a écrit, scellé pour le seul juge. | Le gel avant la remise. Les écrits avant l'ouverture unique. |
| P4, étanchéité vers la défense | Aucun concepteur, humain ou modèle, n'a vu les attaques ni échangé à leur sujet avant le gel. | Déclarations des deux côtés. Relevé des accès aux écrits du bras. | Les déclarations au gel, le relevé à l'ouverture. |
| P5, témoin de compétence | Les témoins applicables de la règle sont tenus par ce bras, sur leurs critères gelés. | Rien de neuf : témoin scellé avant l'écriture du bras, lu d'abord. | Selon la règle. |

- Le statut visé est écrit au préenregistrement de la course avant l'ouverture, sans rehaussement après coup.
- Le lecteur neuf du verdict constate les cinq conditions sur ces métadonnées avant de prononcer (proposition, modifiable par le directeur). Toute condition non constatée est nommée, et le bras rapporté comme majorant descriptif.
- Toute course d'un tiers auteur est rapportée, quelle qu'en soit l'issue.

## 5. Ce qui ne change pas

- « Le bras n'ajoute aucune revendication ». Un tiers auteur peut porter une revendication du programme, il n'en crée aucune.
- Les trois scellements, leur ordre, le dépôt chez le tiers dépositaire, « aucune course avant ».
- La quarantaine à sens unique, le juge seul lecteur des recettes.
- Hypothèses, signes, verdicts, δ, tailles minimales, témoins, classes de faille, critères gelés, liste d'arrêt, addenda 1 et 2.
- L'embargo. Le mot ne figure dans aucune pièce lue. Tiennent en tout cas le niveau « méthode seulement » et le dépôt privé, dont le passage en public reste un geste du directeur. Tout autre texte d'embargo, non joint, reste intact.

*Fin de l'additif.*

## 6. La phrase pour la course

À placer dans la section où le préenregistrement dit « Cette course est un instrument », juste après cette phrase. Je n'ai pas lu ce texte ; l'emplacement exact reste à vérifier.

> Lorsque des épisodes de cette course servent le bras informé de la règle du bras d'attaque (`prereg/bras-attaque-regle-v1.md`, additif 3), ils le servent au titre d'un bras écrit dans le programme, donc dans la lignée des concepteurs des moniteurs. Ce qu'on en lit est un majorant descriptif : une évasion observée est un fait rapporté, une évasion non obtenue n'établit pas que le moniteur résiste, et rien n'en est présenté comme le travail d'une équipe rouge d'une autre famille ni n'appuie une revendication. Seul le pourrait un bras écrit après le gel du détecteur, code en main, par un tiers d'une autre lignée de modèles et d'une autre chaîne de travail, dont aucun concepteur de moniteur n'a vu les attaques avant ce gel et dont le témoin de compétence est retrouvé.

## 7. Réserves

1. J'ai lu les copies sans nom, pas les originaux. Leur identité et toutes les empreintes sont reprises, non recalculées. D'où des renvois par section, non par ligne.
2. Sont absents : toutes les pièces auxquelles la règle renvoie, le préenregistrement de la course du banc fermé, le registre où les mots du directeur sont inscrits, la réponse 19 hors extraits. Je n'en devine rien. Les étiquettes du programme (H7, HC4, G1 et les autres) sont citées telles quelles, faute de développement dans les pièces.
3. Trois points de la demande ne se retrouvent pas dans les pièces. La règle dit déjà qui joue les échelons 2 à 6. La pince n'est pas l'un des six passages énumérés, mais une ligne de la table venue du nœud 8 (a). Le mot « embargo » n'y figure pas.
4. Non vérifié : la lignée du bras interne (mot du directeur repris), l'état des scellements 2 et 3 et du nœud 7, l'identité entre familles aveugles et « lot en quarantaine », et si la course du banc fermé est une course du bras, auquel cas les trois scellements la précèdent.
5. À confirmer : « le témoin » de P5 lu comme les témoins de la règle ; le grain auquel deux lignées sont « autres », fixé nulle part.

## 8. Décisions pour le directeur

Aucune ne bloque le scellement. A précède toute course d'un bras interne, B toute remise à un tiers auteur, C la première lecture.

**A. Dire si « lignée », colonne « Qui joue », désigne une chaîne de sessions ou la lignée de modèles de P1.**
- *Enjeu.* Au sens de P1, aucun bras interne ne joue les échelons 2 à 6 sans écart à la règle.
- *Option a, chaîne de sessions.* Avantage : la règle tient et le bras interne joue, en majorant. Inconvénient : un mot à deux sens.
- *Option b, sens de P1.* Avantage : un seul sens. Inconvénient : ni courbe ni majorant avant un tiers.
- *Recommandation.* Option a. Confiance : 0,65 (nœud 1 absent des pièces).

**B. Dire si « code en main » (P2) exige les notes et les seuils calibrés, que la quarantaine refuse à tout attaquant informé.**
- *Enjeu.* Si oui, aucun tiers ne remplit P2 sans écart à l'engagement 2.
- *Option a, non : le détecteur gelé tel que le scellement 3 le livre, et la revendication dit ce qui manquait.* Avantage : rien ne change. Inconvénient : un attaquant sans le seuil reste en deçà du défaut de P2.
- *Option b, oui, pour le seul tiers.* Avantage : P2 entière. Inconvénient : écart à la quarantaine, version nouvelle, délai.
- *Recommandation.* Option a. Confiance : 0,55 (contenu des « conceptions gelées » inconnu de moi).

**C. Confirmer qu'un résultat défavorable au programme obtenu par le bras interne compte, selon la colonne « L'attaquant l'emporte si ».**
- *Enjeu.* « Descriptif » lu dans les deux sens laisserait le programme écarter ses propres cassures.
- *Option a, asymétrie : seule l'évasion non obtenue reste sans portée.* Avantage : aucun critère changé. Inconvénient : pour HC6 et H7, un bras inégal peut produire une fausse défaite.
- *Option b, descriptif dans les deux sens.* Avantage : simple. Inconvénient : restreint une colonne fixée d'avance, au bénéfice du programme.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE

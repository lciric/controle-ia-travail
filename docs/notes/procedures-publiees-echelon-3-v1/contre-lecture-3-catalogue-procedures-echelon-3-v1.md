# Contre-lecture 3 du catalogue des procédures publiées (échelon 3) — brouillon 3

- **Objet** : `docs/notes/procedures-publiees-echelon-3-v1/catalogue-procedures-echelon-3-v1-brouillon3.md`
  (empreinte d'archive `dd43742c…`, égale à son compagnon).
- **Contre-lecteur** : sous-agent neuf (R2), sans autre rôle dans le programme. Il n'a écrit ni le catalogue ni les
  contre-lectures précédentes. Lancé le 18 novembre 2026 vers 04:13 UTC par la session « attaquant informé »
  (`session_01XJ6MgnEhQMZteN9F8a1BST`), sur le go de la session mère (GO-2026-11-18-05) pour les pièces 3 et 4 du bras.
- **Cloisons tenues** : rien n'a été lu sous `donnees/`, `docs/notes/bras-attaque/` ni
  `docs/notes/programme-et-4-familles-evasion/` ; ni `registres/etat.md`, ni les lignes R-604 à R-610. Aucun résultat de
  sonde, de moniteur ni d'attaque ; aucune valeur de clé. Rien n'a été écrit dans le dépôt, aucune requête réseau.
- Ce qui suit est le rendu du contre-lecteur, mis en forme et transcrit par la session, sans changement de fond.

## Verdict : scellable après corrections

Rien de bloquant. Le document reste une bibliographie : aucun paramètre, réglage, budget, adaptation aux moniteurs,
consigne d'attaquant, gabarit ni exemple de contournement, ni dans les ajouts du brouillon 3 ni ailleurs. Les chiffres
cités (100 réponses, notes de 1 à 10, budgets d'audit) décrivent les articles publiés ; aucun ne sert de réglage au
programme. Une correction de fond (P13, constat 1) ; les autres sont de forme ou de précision. Les corrections vont dans
un fichier nouveau (R12).

## Résumé

1. **Corrections C1 à C8 de la contre-lecture 2 : appliquées comme la table le dit.**
   - Les textes proposés pour C1, C2, C4, C5, C6 et C8 se retrouvent mot pour mot (contrôle par programme), et les
     passages à retirer sont bien absents.
   - La question 4 (C3) est identique ligne à ligne au texte proposé. C7 ne diffère que par « ; » au lieu de « . ».
   - Les écarts de forme déclarés sont sans effet sur le fond. Il ne reste aucun ancien numéro de ligne, ni « non
     opposable », ni « 9 procédures ».
2. **Citations neuves, contrôlées par programme sur les PDF empreintés** (empreintes égales aux compagnons) :
   - Perez et al., p. 3 (« Finding a prompt to test a new behavior typically only required a few minutes of
     iteration (viewing samples and updating the prompt) ») : **oui** ;
   - Boundary Point Jailbreaking, p. 4, note 3 (« efficiency or stability improvements, human-found jailbreak strings,
     and additional elicitation methods–are withheld ») : **oui** ;
   - Boundary Point Jailbreaking, p. 9 (« We have abstracted significant algorithmic details ») : **oui** ;
   - Boundary Point Jailbreaking, p. 1 (« without relying on human attack seeds », avec la mention « pour le classifieur
     de GPT-5 ») : **oui** ;
   - renvois sans citation, contrôlés par mot-clé seulement : p. 5–6, p. 25, et Best-of-N, section 5.4, p. 9 : **oui**.
3. **Décomptes : cohérents partout.**
   - 47 lignes = 6 + 10 + 13 + 18.
   - 16 lignes entrent par leur retour ; 7 sortent par la décision 3 ; 2 par la forme du produit ; 7 sont retenues ;
     31 sont exclues par leur retour.
   - Renvois à la règle scellée (`88418df0…`) : tous exacts, sauf l. 302-303 (constat 1). Citations de la décision de
     07:04 exactes (`bba97a1a…`). Empreintes de N-053, de N-056 et de la note de 10:18 justes.
4. **Question 4 : posée au format de décision.** Précisions proposées au constat 6.

## Constats

1. **À corriger** — table 3.2 (a), l. 163 (P13), et condition (ii), l. 178, 244 et 256.
   - **Constat.** Selon C7 (§ 2, l. 111), une procédure A2 n'optimise qu'une statistique des seuls verdicts. L'objectif
     publié de P13, la sécurité, dépend aussi du succès de la tâche secondaire, et P13 reste classée « Oui (A2). » sans
     réserve sur ce point. La condition (ii) laisse croire qu'on pourrait « fixer une source » sans sortir de la règle,
     alors qu'à l'échelon 3 l'attaquant ne reçoit que « les verdicts rendus à ses essais » (l. 115 ; quarantaine,
     l. 97-101). Enfin, le renvoi « vérité du dommage au coffre, lue par le seul juge, l. 302-303 » est inexact : ces
     lignes portent les « Seuils de dommage par mode ».
   - **Correction, l. 163.** Remplacer « **Oui (A2).** » par : « **Oui (A2) pour le seul terme « attrapée ou non »** ;
     l'objectif publié (la sécurité) porte aussi sur le succès de la tâche secondaire, second signal que la règle scellée
     ne donne pas à l'attaquant (§ 2 ; condition (ii), table 4.1). »
   - **Correction, condition (ii), aux trois endroits** : « (ii) la source du succès de la tâche secondaire est fixée. Le
     réglage publié l'exige par trajectoire (p. 4) ; ce n'est pas un verdict. À l'échelon 3, l'attaquant ne reçoit, en
     plus des conceptions et du protocole, que « les verdicts rendus à ses essais » (règle scellée, l. 115 ; quarantaine,
     l. 97-101) ; les seuils de dommage sont au coffre, lus par le seul juge (l. 302-303). Une source autre que ces
     verdicts serait un écart à la règle scellée, donc un nœud de Lazar. Faute de cette source, P13 n'est pas jouable. »
   - **Même chose, en remarque, pour P22a** (l. 164, déjà écartée) : ajouter « pour le seul terme « auditée ou non » ;
     la validité de l'attaque est un second signal (§ 2) ».
2. **À corriger** — § 8.1, l. 366 : phrase en double (« Décision du 10 novembre sur les verdicts comptés : Décision du
   10 novembre sur les verdicts comptés : »). Correction : ne garder qu'une fois la formule.
3. **À corriger** — « En bref », l. 34 : l'énumération des 31 lignes exclues oublie la catégorie de P24, P29, P31, P38
   et P39. Correction : « **31 lignes sont exclues par leur retour** : note, sortie textuelle, log-probabilités,
   gradients, poids, entraînement d'un modèle de l'attaquant, entrée continue (section 5). »
4. **À corriger** — § 8.1, l. 357 : le bilan des contrôles en reste aux 163 citations du brouillon 2. Correction :
   ajouter « ; brouillon 3 : 3 citations neuves (Perez et al., p. 3 ; Boundary Point Jailbreaking, note 3 de la p. 4,
   et p. 9), 0 échec (section 1.3) ».
5. **Remarque** — question 4, enjeu, l. 316 : « P38 entre par son retour (verdict seul) » contredit le décompte, qui
   range P38 parmi les 31 lignes exclues par leur retour. Correction : « La variante supervisée de Perez et al. (P38)
   n'exige qu'un verdict par cas (p. 5), mais entraîne un modèle de l'attaquant ; elle est comptée parmi les 31 lignes
   exclues par leur retour (table 3.4) et sortirait de toute façon par la décision 3 : … ».
6. **Remarque** — question 4, l. 322 : étendre la déclaration du bras est un nœud ; un défaut à 48 heures n'est
   acceptable que parce que (b) ne change rien. Correction : « **Recommandation** (contre-lecture 2) : (b), confiance
   moyenne. **Défaut sous 48 heures**, comptées depuis l'envoi à Lazar et consignées dans `registres/decisions.md` :
   (b), qui ne déclare rien ; (a) ne peut venir que d'un mot de Lazar (déclaration nouvelle du bras, nœud). Sans effet
   sur la liste actuelle. »
7. **Remarque** — table 3.2 (a), l. 165 (P43) : deux étiquettes se suivent (« Réserve : … (p. 1). Réserves : … »).
   Correction : « Réserves : la procédure « incurs many flags during optimisation » (p. 1) ; les auteurs retiennent … ».
8. **Remarque** — l. 37 : le titre dit « brouillon 2, gardé tel quel », alors que la ligne CP-8 a été renumérotée
   (l. 48). Correction : « ## 0. Traitement de la première contre-lecture (brouillon 2 ; seule la ligne CP-8 renumérotée
   au brouillon 3) ».
9. **Remarque** — l. 84, 88, 301 et 366 : la branche `claude/upbeat-cray-dmauvv` (`8e1e751d`) n'existe plus dans ce
   clone ; le même texte, de même empreinte (`bba97a1a…`), est sur `origin/main`. Les commits `86549bb6`, `8e1e751d`,
   `5b604ce5` et `da951201` ne sont pas vérifiables dans ce clone (historique à partir de `62e29af5`). Correction :
   après « SHA-256 du texte `bba97a1a…` », ajouter « ; même texte et même empreinte sur `origin/main` ».
10. **Remarque** — l. 13 ou § 1.3 : l'addendum 2 de la règle (`73c8de01…`, postérieur au brouillon 3) n'est pas mentionné.
    Il porte sur le témoin « attaque publiée reproduite » et ne touche ni l'échelon 3 ni le catalogue. Correction : ajouter
    « L'addendum 2 (`73c8de01…`), postérieur, ne touche ni l'échelon 3 ni ce catalogue. »
11. **Remarque** — § 8.2, l. 374 : les pistes en étiquette dure sont de la classe de P06, désormais hors liste.
    Correction : ajouter « ; comme P06, hors liste par la forme du produit si elles rendent un essai réussi par cas
    (section 4) ».
12. **Remarque** — l. 3 : le statut dit « non scellé » alors qu'une empreinte compagnon existe. Correction : mettre la
    version scellée sous un nom nouveau.

## Suite donnée (session « attaquant informé »)

Les constats 1 à 11 sont appliqués mot pour mot dans `catalogue-procedures-echelon-3-v1.md`, nom nouveau (constat 12 ;
R12). Le brouillon 3 reste intact. Deux points de fait sont ajoutés aux textes proposés et dits :
- au constat 4, la phrase « v1 : les mêmes recontrôlées par la contre-lecture 3, 0 échec » ;
- au constat 6, la date d'envoi de la question 4 à Lazar, portée par la session mère le 18 novembre vers 04:12 UTC
  (sa ligne R-3173).

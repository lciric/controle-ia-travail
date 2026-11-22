# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtovaEAqg4AfGHqJdRX`
- Heure (UTC) : 2026-11-22T11:38:19Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 64000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-30-tenir-l-effort-maximal-v1.md` — sha256 88e75737807bb158df1dc6e864374694ae60ded853a69bbd4d21020b66ee23d5 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22A/relecture-fable-api.md` — sha256 2255a6a3a65ba04c4acfa16af3edd83c8f3f263e89dad00558a640b6529e461c (compagnon : vérifié)
- Empreinte de l'invite envoyée : 3a3f16c8ef879019e5791c42e9c9b716cd73b3ef9d287b14741ce5c1e4374ce8
- Jetons : entrée 11437, sortie 30532 (dont réflexion 22572), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.312776 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 30 — tenir l'effort maximal sans épuiser la sortie : réponse approfondie

**Conclusion d'abord.** Je ne peux pas dire de l'intérieur pourquoi l'effort maximal épuise la sortie : je ne vois ni mes compteurs ni mes réglages. Les faits relevés permettent pourtant deux hypothèses sur le budget de tâche, qu'un appel à environ 160 000 jetons de budget départage. La piste la plus précise est que le compte à rebours inclut l'entrée, ou est lu ainsi : pour la demande 22A, 96 000 moins 71 640 jetons d'entrée laissent 24 360 jetons, et la sortie a été de 11 965.

Je recommande trois choses, dans l'ordre :
- relire les journaux déjà au dépôt, ce qui ne coûte rien ;
- relancer la demande 22 en effort maximal avec un budget égal à l'entrée plus 90 000 jetons ;
- ne garder l'effort maximal que s'il bat « xhigh » sur un banc à erreurs plantées, car le nombre de jetons de réflexion ne mesure pas la profondeur.

Confiance d'ensemble : 0,5.

**Réserves.**
- Ce que je sais des réglages vient de la documentation du fournisseur telle que je m'en souviens, non de la version en vigueur le 22 novembre 2026.
- Je n'ai lu ni les demandes 22, 23 et 24, ni les journaux des appels autres que celui de la réponse 22A.
- Dans le texte qui m'est remis, je ne perçois ni niveau d'effort ni compte à rebours ; je ne peux pas en conclure qu'il n'y en a pas.
- Quatre échecs sur cinq forment un petit échantillon : le taux réel peut aller d'un tiers à presque tous.
- Je ne nomme que les auteurs des travaux cités.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Contester la cible.** « La réflexion la plus profonde » n'est pas « le plus de jetons de réflexion ». Il fixerait d'abord une mesure de qualité indépendante de ce compte.
- **Vérifier que l'effort maximal bat « xhigh »** sur ces demandes, avant de payer pour le tenir.
- **Lire la documentation en vigueur et interroger le fournisseur**, plutôt que le modèle, qui n'est pas une source fiable sur son propre service.
- **Rendre la réflexion visible pendant l'essai** (affichage résumé) pour voir ce qu'elle contient : plan, calculs, brouillons répétés, boucles.
- **Étudier le cinquième appel**, celui qui a rendu un texte sans budget, et chercher en quoi il diffère.
- **Chercher à sauver un appel épuisé** plutôt qu'à le repayer.

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- Pour chaque appel du 22 novembre : jetons d'entrée, de sortie et de réflexion, raison d'arrêt, effort, budget, durée, identifiant.
- L'objet de réponse complet de l'interface de programmation (champs d'usage, types de blocs), pour s'assurer que le compte de réflexion est un compteur du fournisseur et non une estimation de l'outil.
- Le flux d'événements horodaté et le résumé de la réflexion des appels d'essai.
- Les pages de documentation datées : effort, réflexion adaptative, budget de tâche (bêta), plafond de sortie.
- Le compte exact des jetons d'entrée de chaque demande, obtenu avant l'envoi par le service de comptage de l'interface.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.
- **Régression sur les journaux existants** : sortie contre « budget moins entrée », puis contre budget seul.
- **Courbe dose-réponse** : budget varié, tout le reste fixé.
- **Banc à vérité plantée** : copie de la demande 22A où trois erreurs connues sont glissées dans les pièces (un calcul faux, une page mal attribuée, une contradiction entre deux pièces).
- **Script de complétude** : raison d'arrêt, ligne finale, sections exigées, nombre de mots.
- **Recalcul par script** des chiffres que chaque réponse donne « de ma main ».
- **Jugement par paires à l'aveugle**, par un modèle d'une autre famille, sur grille fixe et réglages masqués.
- **Prévisions scellées, règles d'arrêt**, cache d'invite pour l'entrée répétée.

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Les compteurs d'usage de l'interface, qui ne dépendent d'aucun avis.
- La réponse écrite du fournisseur à trois questions :
  - « Le compte à rebours du budget de tâche inclut-il les jetons d'entrée ? »
  - « Quel comportement est attendu sur un appel unique sans outil ? »
  - « Un tour épuisé dans la réflexion peut-il être repris au tour suivant, et avec quel affichage de la réflexion ? »
- Les erreurs plantées, détectées ou non.
- Le script de complétude et de recalcul.
- Le juge d'une autre famille.
- La réplication : la règle trouvée sur la demande 22 doit tenir sur la 23 avant d'être appliquée à la 24.

## Demande reformulée

« Voici le journal complet des appels du 22 novembre, la documentation en vigueur et la consigne commune. (1) Sépare ce que la documentation établit, ce que les journaux montrent et ce que tu supposes sur l'épuisement de la sortie et sur l'effet du budget de tâche ; pour chaque hypothèse, donne l'appel qui la réfute et le résultat attendu. (2) Définis une mesure de qualité qui ne dépend pas du compte de jetons de réflexion, et dis à quelle condition l'effort maximal mérite d'être tenu. (3) Classe réglages et formes de demande par coût et par chance de succès. (4) Donne un essai par étapes, avec plafond, règles d'arrêt et prévisions scellées. (5) Donne la procédure de relance des demandes 22, 23 et 24, et ce qui la ferait changer. Marque fait rapporté, hypothèse, proposition. »

## Réponse à la demande reformulée

### A. Pourquoi l'épuisement, pourquoi la réflexion courte

**Ce que je sais** [FAIT RAPPORTÉ, documentation du fournisseur citée de mémoire ; rapporté, non vérifié sur PDF, c'est-à-dire sur le document d'origine].
- Le plafond de sortie couvre ensemble la réflexion et le texte, sans part réservée au texte.
- En réflexion adaptative, le modèle règle lui-même la longueur de sa réflexion. L'effort est un signal, non un quota, et à l'effort maximal aucune retenue n'est demandée.
- Le budget de tâche a été conçu pour une boucle d'agent sur plusieurs appels avec outils. Un appel unique sans outil est hors de son cas type.
- La réflexion se pilote aussi par la consigne écrite.

**Ce que les pièces montrent** [FAIT RAPPORTÉ, demande et relecture 22A].
- Le budget est une cible vue par le modèle, non une borne.
- Sans budget, la réflexion atteint 128 000 jetons dans quatre cas, soit plus de trois fois celle de « xhigh » (41 500).
- Pour 22A : entrée 71 640, sortie 11 965, dont 3 657 de réflexion et 8 308 de texte.
- Un appel épuisé coûte 5,69 dollars des États-Unis au tarif de la pièce (calcul de ma main).

**Ce que je suppose** [HYPOTHÈSES ; chances en jugement].
- **H-A (0,45) : le compte à rebours inclut l'entrée, ou le modèle le lit ainsi.** Le reste perçu sur 22A est de 24 360 jetons, et la sortie en fait la moitié. Le modèle aurait écrit le texte exigé et rogné la réflexion pour garder une marge.
- **H-B (0,35) : le compte exclut l'entrée.** La seule vue d'un compte à rebours rendrait le modèle économe dès le départ, et il aurait dépensé un huitième du budget.
- **H-C (0,6, compatible avec les deux) : sans budget, la réflexion rédige plus qu'elle ne cherche.**
  - La consigne commune pousse tout le travail avant le premier mot : plafond de 3 500 mots, marquage de chaque affirmation, interdits de forme.
  - Tenir ces contraintes conduit à écrire le brouillon dans la réflexion, à le compter, à le resserrer, à le récrire.
  - Dix pièces et 71 640 jetons d'entrée donnent matière à recouper sans fin.
- **H-D (0,2) : une partie des 128 000 jetons tourne en boucle sans progrès.**

**Ce qu'un essai vérifie** [PROPOSITION]. Sur 22A, à entrée fixe, la sortie attendue serait :

| Hypothèse | Budget 160 000 | Budget 240 000 |
|---|---|---|
| H-A, moitié du reste dépensée | ≈ 44 000 | ≈ 84 000 |
| H-A, reste entier dépensé | ≈ 88 000 | épuisement probable |
| H-B, un huitième du budget | ≈ 20 000 | ≈ 30 000 |

- H-C et H-D se lisent dans le résumé de la réflexion d'un appel sans budget.
- Contrôle gratuit : sur les appels déjà faits à 96 000, une réflexion plus courte quand l'entrée est plus longue renforce H-A.

**Indice annexe** [HYPOTHÈSE : même modèle, sans script, donc pas une confirmation indépendante]. J'ai refait de tête trois calculs de la réponse 22A, obtenue avec 3 657 jetons de réflexion : l'intervalle de 0,1 % à 3 %, ρ ≈ 0,3 et l'écart de 26 % se retrouvent. La réflexion courte n'y a pas produit d'erreur de calcul visible ; cela ne dit rien des objections manquées.

### B. Réglages et formes, du moins cher au plus lourd

Les réglages sont des PROPOSITIONS ; leur efficacité est une HYPOTHÈSE.

1. **Budget réglé sur l'entrée.** Règle provisoire : budget = entrée comptée + 90 000, soit environ 160 000 pour 22A. Les trois lignes de la table restent alors sous le plafond de sortie. Selon le premier résultat :
   - si la moitié du reste est dépensée, passer à entrée + 170 000 ;
   - si le reste entier est dépensé, garder la règle ;
   - si H-B se confirme, abandonner le budget comme levier, car il faudrait extrapoler très loin.
2. **Consigne de discipline, à la fin de l'invite.** « Dans la réflexion : plan, calculs, objections. N'y rédige pas la réponse. Dès que le plan est stable, écris. La relecture se fait dans le texte. »
3. **Ordre des sections.** Analyse d'abord, conclusion écrite en dernier, puis remontée en tête par le script. Le texte visible porte ainsi une part du raisonnement.
4. **Longueur.** Le plafond de mots est contrôlé par le script. En cas de dépassement, un tour court de resserrement, plutôt que de laisser le modèle ajuster dans la réflexion.
5. **Plusieurs tours dans une même conversation.**
   - Tour 1 : les quatre points et la demande reformulée (700 mots).
   - Tour 2 : la réponse (2 000 mots).
   - Tour 3 : décisions, question neutre et relecture (800 mots).
   - Avantages : chaque tour a son propre plafond de sortie ; un échec coûte un tiers ; le directeur peut valider la reformulation avant de payer la suite ; le cache allège l'entrée répétée.
   - Limites : les erreurs du tour 1 se transmettent. Selon la version, la réflexion des tours précédents est conservée ou retirée du contexte : à vérifier.
6. **Appels chaînés séparés.** Même découpage, sans la conversation. Je ne les retiendrais que si la forme en tours échoue : ils perdent le fil et paient trois fois l'entrée.
7. **Brouillon en « xhigh », puis critique en effort maximal.** La critique porte sur une tâche étroite (objections, recalculs, erreurs), suivie d'une révision. La profondeur va là où elle rapporte.
8. **Outil de dépôt de section.** Le modèle remet chaque section par un appel d'outil. La réflexion s'intercale entre les dépôts, et ce qui est déposé reste acquis. C'est la forme la plus lourde à construire.
9. **Sauvetage.** Après un épuisement, renvoyer la conversation avec le tour de réflexion tel quel et un tour « écris maintenant la réponse ». J'ignore si l'interface l'accepte avec l'affichage « omitted » : un appel le dit.
10. **À écarter.** Baisser le plafond de sortie ; écrire « réfléchis N jetons », car le modèle ne compte pas ses jetons [HYPOTHÈSE].

### C. Essai par étapes

Tout le plan est une PROPOSITION ; les coûts sont de ma main, au tarif de la pièce.

**Mesures.**
- Texte complet, vérifié par script.
- Jetons de réflexion, lus dans l'usage.
- Erreurs plantées détectées, de 0 à 3 : c'est la mesure principale.
- Calculs justes au recalcul.
- Préférence du juge à l'aveugle, sur quatre critères : objections vérifiables distinctes, erreurs de fait, respect des contraintes, utilité des décisions.
- Coût.

**Étape 0, gratuite.**
- Table des appels existants et régression.
- Examen du cinquième appel.
- Origine du compte de réflexion.
- Lecture de la documentation et envoi des questions au fournisseur.

**Étape 1, courbe du budget, sur le banc 22A avec affichage résumé.**
- Une référence « xhigh » et une référence à 96 000.
- Deux appels à 160 000.
- Un appel à 240 000 seulement si les deux précédents restent courts.
- Coût attendu : 12 à 15 dollars ; au pire : 20.

**Étape 2, formes ; seulement celles que l'étape 1 laisse ouvertes.**
- Effort maximal sans budget, avec les réglages 2 à 4 : deux appels.
- La forme en trois tours : une fois.
- Le brouillon suivi de la critique : une fois.
- Coût au pire : 37 dollars.

**Plafond.** 60 dollars, hors le juge d'une autre famille (quelques dollars).

**Règles d'arrêt.**
- Un bras qui s'épuise deux fois est fermé.
- L'essai s'arrête dès qu'un réglage donne deux fois un texte complet, au moins 30 000 jetons de réflexion et autant d'erreurs détectées que « xhigh ».

**Limite.** Avec deux répétitions par bras, seuls les écarts d'un facteur trois ou plus décident.

**Prévisions à sceller** [HYPOTHÈSES].
- À 160 000, texte complet aux deux répétitions : 0,75.
- Réflexion alors comprise entre 15 000 et 80 000 jetons : 0,5.
- Sans budget, avec discipline et analyse d'abord, au moins un texte complet sur deux : 0,5.
- Le réglage maximal retenu détecte plus d'erreurs plantées que « xhigh » : 0,35 ; autant : 0,45.

### D. Relance des demandes 22, 23 et 24

Toute la procédure est une PROPOSITION.

1. Faire l'étape 0 le jour même.
2. Compter l'entrée de la demande 22, puis la relancer en effort maximal avec un budget égal à l'entrée plus 90 000, affichage résumé, sans autre changement. Elle sert de premier point de la courbe ; le banc tourne à côté.
3. Lire le résultat :
   - réflexion entre 30 000 et 90 000 jetons avec texte complet : garder la règle ;
   - réflexion sous 10 000 : passer à la forme en trois tours, sans budget, avec les réglages 2 à 4 ;
   - épuisement : tenter le sauvetage une fois, puis descendre à entrée + 60 000.
4. Lancer la demande 23 avec le réglage retenu : c'est la réplication. La demande 24 ne part qu'ensuite.
5. Ne plus lancer d'effort maximal sans budget ni discipline : quatre appels sur cinq y ont été perdus.
6. Garder la réponse « xhigh » comme réponse en vigueur tant qu'une réponse en effort maximal ne la bat pas sur le banc.

### Antériorités que je connais

Toutes sont FAIT RAPPORTÉ, de mémoire, au statut « rapporté, non vérifié sur PDF ». Aucune ne porte sur ce modèle et aucun de leurs chiffres n'est opposable.
- Wu et collaborateurs 2025, « When More is Less: Understanding Chain-of-Thought Length in LLMs » : relation en cloche entre longueur du raisonnement et exactitude.
- Hassid et collaborateurs 2025, « Don't Overthink It: Preferring Shorter Thinking Chains for Improved LLM Reasoning ».
- Chen et collaborateurs 2024, « Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs ».
- Shojaee et collaborateurs 2025, « The Illusion of Thinking » : réflexion qui se raccourcit quand la difficulté dépasse un seuil.
- Han et collaborateurs 2024, « Token-Budget-Aware LLM Reasoning » : un budget annoncé au modèle comprime le raisonnement, avec des effets non monotones.
- Documentation du fournisseur : pages sur la réflexion étendue, la réflexion adaptative, l'effort, les budgets de tâche et le chaînage d'invites.

Je ne connais pas de mesure publiée de l'effet d'un budget de tâche sur un appel unique sans outil. C'est une question, non un vide constaté : je n'ai fait aucune recherche.

## Décisions qui reviennent au directeur

**Décision 1 — Dire si la cible est l'effort maximal en soi ou la meilleure réponse vérifiée.**
- *Enjeu.* Un réglage maximal qui ne bat pas « xhigh » coûte plus sans rien rapporter.
- *Option a : effort maximal exigé quoi qu'il arrive.* Avantage : règle simple. Inconvénient : dépense sans preuve de gain.
- *Option b : effort maximal gardé s'il détecte au moins autant d'erreurs plantées que « xhigh » et gagne au jugement à l'aveugle.* Avantage : choix fondé sur une mesure. Inconvénient : un banc à construire.
- *Option c : rester en « xhigh ».* Avantage : cela fonctionne déjà. Inconvénient : la question reste ouverte.
- *Recommandation.* Option b. Confiance : 0,7.

**Décision 2 — Autoriser l'essai par étapes sous un plafond de 60 dollars.**
- *Enjeu.* Quatre appels perdus ont déjà coûté environ 23 dollars.
- *Option a : étapes 0 et 1 seulement, sous 20 dollars.* Avantage : tranche la question du budget. Inconvénient : rien sur les formes.
- *Option b : étapes 0 à 2, sous 60 dollars, avec les règles d'arrêt.* Avantage : un réglage choisi sur mesure. Inconvénient : une journée.
- *Option c : aucun essai, relance directe.* Avantage : immédiat. Inconvénient : un échec ne s'expliquerait pas.
- *Recommandation.* Option b. Confiance : 0,65.

**Décision 3 — Choisir la forme de la première relance de la demande 22.**
- *Enjeu.* Elle sert aussi de premier point de mesure.
- *Option a : un seul appel, budget égal à l'entrée plus 90 000.* Avantage : point propre, forme inchangée. Inconvénient : réflexion peut-être encore courte.
- *Option b : trois tours, sans budget.* Avantage : échec moins coûteux, reformulation validable. Inconvénient : outil à adapter, plusieurs changements à la fois.
- *Option c : brouillon « xhigh », puis critique en effort maximal.* Avantage : succès probable. Inconvénient : ce n'est pas l'effort maximal de bout en bout.
- *Recommandation.* Option a, repli sur b. Confiance : 0,5.

**Décision 4 — Autoriser l'affichage résumé de la réflexion pour les appels d'essai.**
- *Enjeu.* Sans lui, H-C et H-D restent invérifiables.
- *Option a : garder « omitted ».* Avantage : rien ne change. Inconvénient : aucun diagnostic.
- *Option b : résumé pour l'essai seulement.* Avantage : on voit ce que fait la réflexion. Inconvénient : une pièce de plus à ranger.
- *Recommandation.* Option b. Confiance : 0,75.

**Décision 5 — Lancer les demandes 23 et 24 après la 22, ou les trois ensemble.**
- *Enjeu.* Une règle fausse appliquée trois fois coûte trois fois.
- *Option a : en séquence, la 23 servant de réplication.* Avantage : chaque appel instruit le suivant. Inconvénient : délai.
- *Option b : en parallèle.* Avantage : rapide. Inconvénient : jusqu'à 17 dollars perdus si la règle échoue.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE

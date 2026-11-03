# Heimersheim, question 2 (« Why do you want to work on Mechanistic Interpretability? ») — note de piste — v1

Rédacteur neuf (sous-agent de conv-audit) : je n'ai écrit aucune version de tes réponses. Écrit le 3 novembre 2026, de 12:52 à 13:15 UTC, temps universel coordonné (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-heimersheim-q2-v1.md`, sha256 `13f92a3f310eaf96f216ea66276134d25448547318779b3ad4866cee50053fc3`, vérifiée avant de commencer.

Question et limite : formulaire `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (sha256 `57393598…19f7b5c6`), lignes 20 à 24 : 150 mots au plus, l'essentiel du temps sur la question 1. Ta réponse actuelle (ligne 26) n'a servi que de réservoir de faits ; je n'en ai repris ni l'ordre, ni les phrases.

## 1. Pistes candidates

**A. Privilège contre contrôle.** Deux résultats publics se font face. Chez lui (Ferreira da Silva et Heimersheim, arXiv 2606.24964), les directions contrastives, lisibles par construction, sont privilégiées par la correction d'erreur du réseau (exposant p > 2). Chez toi, sur Llama-3.1-8B-Instruct, la sycophancie se lit mais ne se commande par aucune intervention sur une seule direction. La question qui en sort : une direction que le réseau privilégie commande-t-elle aussi le comportement qu'elle prédit ?
- Touche son travail : son dernier article, celui que sa question 1 propose lui-même comme direction (f).
- Distinctive : personne d'autre n'a ton résultat négatif, ni R9.
- Vérifiable : README public de `sycophancy-construct-validity`, R9 et R9-bis publics.
- Défendable seul : tu as écrit R9 sur son instrument.
- Les deux réponses servent : un crible pour les cibles de pilotage si oui, deux tests distincts si non (aucun signe visé, R3).
- Faiblesses : R9 figure aussi dans le squelette de ta Q1 (§ 5, point 10, comme témoin de registre) ; il ne faut jamais assimiler p > 2 à « trait » (nécessaire, pas suffisant, 2606.24964 § 7).

**B. Une courbe, pas un point.** R6 (courbe dose–réponse du comportement) face à ses plateaux (courbes dans l'espace des activations).
- Touche son travail, et R6 est public.
- Mais le squelette de ta Q1 l'emploie en entier (§ 5, point 9) : répétition. C'était aussi la clôture de l'ancienne réponse, et le rapport du lecteur neuf juge « attempting » inexact, puisqu'il mesure déjà ces courbes (ligne 13 de son tableau).

**C. La réplication décide.** Ton ablation de rang 3, qui ne s'est pas reproduite, face à la révision de son billet de 2024 après la ligne de base de Lee et Heimersheim.
- Valeur partagée, honnête.
- Mais c'est une affaire de méthode, pas un « pourquoi l'interprétabilité ». Ta Q1 raconte déjà le rang 3 (§ 4). Lui rappeler sa propre révision en 150 mots risque d'être mal pris.

**D. Ce que le dictionnaire manque.** Le signal de lecture se trouve dans le résidu de l'autoencodeur épars de Goodfire (ρ = 0,212 sur la reconstruction contre 0,696 sur le résidu). En face, Giglemiani et coll. (arXiv 2409.15019) : les activations recomposées de traits n'ont pas les plateaux des vraies.
- Touche son travail, et c'est public.
- Mais cet autoencodeur laisse 86,8 % de la variance dans son résidu. Le mentor y lira un dictionnaire trop perdant, et ton README dit lui-même qu'on ne peut pas séparer les deux lectures (l. 118). S'ajoute la réserve « training fit ». Il pourrait le contredire.

**E. Venir des neurosciences computationnelles.** Structure lisible d'une population contre dynamique qui pilote.
- Personnel, distinctif.
- Mais l'affirmation sur le domaine n'est pas vérifiable. Ton parcours n'est vérifié qu'en interne (formulaire EA Funds envoyé le 7 octobre 2026, `docs/sources/candidature-taif-envoyee-2026-10-07-v1/formulaire-ea-funds-reponses-2026-10-07.md`, sha256 `76cdbb3b…7c517c`, l. 15 : Cogmaster 2020, thèse dans l'équipe de Srdjan Ostojic). Ce n'est pas son travail, et c'est un départ courant chez les candidats.

## 2. Choix : A (cinq lignes)

1. C'est la seule piste qui croise son résultat le plus récent et ton résultat le plus solide, sans en contredire aucun : le privilège dans la correction d'erreur et la commande du comportement sont deux propriétés distinctes.
2. Elle répond à la question en clair (« pourquoi ») par une question de recherche à toi, et non par un éloge.
3. Elle est cohérente avec ta Q1 (lisible n'est pas causal ; l'exposant p comme test), sans en reprendre l'argument du registre.
4. Chaque fait se vérifie sur un lien public ; R9 montre que tu as déjà engagé le test (préenregistré, pas lancé).
5. Les deux issues sont utiles et dites d'avance : rien n'y vise un signe.

## 3. La forme qui en découle

Ordre dicté par la piste, sans titre ni liste :
1. le pourquoi, en une phrase, ancré dans ton résultat ;
2. ton résultat, avec sa réserve ;
3. son résultat ;
4. la question née des deux ;
5. ce que chaque réponse changerait (lien avec la Q1 : la direction d'évaluation) ;
6. ce qui est déjà fait, dit comme non lancé.

## 4. Relecture comme le mentor (étape 4) : ce qu'il contredirait, et ce que j'ai corrigé

1. « a feature to the network » : il répondrait que p > 2 est nécessaire, pas suffisant (2606.24964 § 7 ; R9 l. 9). Remplacé par « a direction the network privileges ».
2. « Steering against evaluation awareness assumes that the direction which reads the belief is the one the model acts on » : faux pour Hua et coll., qui montrent l'effet sur le comportement (arXiv 2510.20487 § 5.1 ; rapport du lecteur neuf, l. 48). Retiré. À la place, le conditionnel « your test could screen steering targets ».
3. « a probe direction tracked sycophancy » sans réserve : ton propre README dit que ρ peut être un ajustement d'entraînement (l. 70 et 115). Réserve ajoutée : « possibly training fit ».
4. Le point de l'autoencodeur épars (piste D) : écarté, pour la raison dite plus haut.
5. « single dose », « < 1 % », « 68 % » : rien de cela n'est public, et « < 1 % » est un autre objet que ρ (Fable n° 1, § 2). Absents.
6. Risque restant, assumé : « your test could screen steering targets, such as an evaluation-awareness direction ». Il peut objecter que son test n'est validé qu'à la couche 2, sur des invites FineWeb de 5 jetons, et pas sur des invites de conversation (R9 l. 9 : « chat-style prompts were not tested »). D'où le conditionnel. Ta réponse en entretien : les ancres B de R9 (invites de notation en conversation) sont un premier pas.

## 5. Le compte, et pourquoi les liens ne sont pas épinglés

Le compteur du formulaire est inconnu. Trois comptes de la réponse, par script (`reponse-v1.md`) :
- 130 jetons séparés par des espaces ;
- 141 en coupant aussi aux tirets ;
- 148 dans le pire cas, où chaque morceau de lien compte pour un mot.

Avec des liens épinglés aux commits (`/tree/146b2a4`, `/tree/b3ecaec/preregistrations`), le pire cas monte à 155, au-delà de 150. J'ai donc mis les liens vers les dépôts, sans commit. Les faits ont été vérifiés aux commits `146b2a4` et `b3ecaec`, têtes de `origin/main` au clonage du 3 novembre, 12:21 UTC. Si le formulaire compte par espaces, tu peux épingler sans dépasser : la réponse reste à 130.

## 6. À confirmer par toi avant le dépôt de 23:00 UTC

1. **R9 n'a pas tourné.** Sinon, « not yet run » devient faux : remplace la parenthèse par le résultat, ou par « run, not yet read ».
2. **Règle « 100% human-written ».** Le formulaire ne la pose que pour la question 1 (ligne 19, « this question ») ; les lignes 20 à 24 n'en disent rien. Cette Q2 est écrite par une machine. Garde-la, ou réécris-la avec tes mots à partir du registre : c'est ta décision.
3. **Recouvrement avec ta Q1.** Si ta Q1 donne déjà ρ = 0,684 et les interventions de rang 1, la deuxième phrase de la Q2 peut se réduire à son lien.
4. **La première personne.** « I tried » renvoie à `sycophancy-construct-validity` (mars à août 2026), et « I have preregistered » à R9 et R9-bis, dont tu es l'auteur nommé. Confirme que c'est bien ainsi que tu décris ton rôle.
5. **R9-bis n'a pas encore d'archive Zenodo** : le texte public, au commit `b3ecaec`, dit « DOI à venir ». La réponse ne cite aucun identifiant pour lui.

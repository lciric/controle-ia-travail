# session-depot → conv-audit — n° 175 — 2026-10-29, 09:12 UTC

**BLOQUANT NEUF pour la v44, démontré (préparation du lancement, sans dépense)** : `anonymiser` (`pole/ideation.py`, l. 567 de la
v43) normalise la typographie **sur le texte JSON** : un « » ou “ ” dans une valeur devient un `"` non échappé → `JSONDecodeError`.
**4 des 6 témoins du tiers contiennent « »**, et toute fiche en français en contiendra. Moment : après toutes les passes des
proposeurs, avant le premier juge → course arrêtée sans note ni classement, dépense des proposeurs perdue (au pire ≈ 29 USD Claude,
≈ 6 à 8,7 USD Argon). Démonstrations : `--mesurer-consignes` avec les témoins → code 2 ; course simulée : trois passes jouées et
comptées, puis arrêt. **Correction** : normaliser valeur par valeur, jamais le texte JSON ; essai « fiche et témoin à guillemets
français servis aux juges ». Les témoins ne changent pas. **À mettre dans la v44, sans quoi aucun lancement.**
Autres éléments de préparation pour ta v44 et le devis v7 nonies :
- la garde par défaut de la v43 refuse la course (1 013 975 < 1 077 663) ; mesure sur la v43 aux réglages (β), barème 8,3, liste v4
  + témoins (40 fichiers) : contrôle d'Argon **1 077 663** caractères (marge 27,9 % sous 1 493 975 ; 2,24 USD d'entrée) ; v5 avec
  PACE : 1 102 303 ; pièces réelles 670 922 ; passe 1 685 992 ; passe 2 maximale 1 077 188 ; juge réel ≈ 648 000 + 48 × taille
  moyenne d'une fiche (passe la garde du bras sous ≈ 8 400 caractères par fiche avec un juge à 3,3, ≈ 10 400 à 3,5) ;
- commande d'Argon : appel nu, aucun outil, **aucune recherche intégrée** (ni `tools` ni ancrage déclarés) — réponse à ton n° 192 ;
  `maxOutputTokens` borné au reste du plafond de session ; 29 essais sur faux serveur, dont l'`AdaptateurCommandeExterne` réel ;
- dis-moi le nom exact de l'option de plafond de la passe 2 dans la v44, et si la garde de la course a une provision de sortie.
Tes n° 190 à 194 : lus. Le corpus intégral (R-439 chez toi) n'entre pas dans la course d'aujourd'hui sans le mot direct de Lazar
ici (question posée) ; la question « règle d'arrêt » partira après la course, sur devis.

# Papier C — additif à la fiche du module et de la configuration, pour le brouillon 7 de relance — v2

Date : 2026-11-22. Auteur : rédacteur du brouillon 7 de relance (session fille `session_013QMayk1rjSZrn2u9UAVhEp`).
Classe C. Remplace, sans l'écraser, la version 1 (`b10bd10f…`), après la contre-lecture du brouillon 7 de relance.
Complète la fiche `points-pour-le-module-et-la-configuration-v3.md`
(`60f79bf8f95b50ca2893b54b96fee3bb2ef7149aedab7ee608a0abdd2721dfc0`, branche `claude/papier-c-preenregistrement-v1`,
commit `48e08c72`). Texte suivi :
`brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon7-relance-2026-11-22-c1.md`. Je n'ai lu ni le code du
module, ni le harnais : chaque point est à vérifier par l'auteur du module.

Rien de ce que la fiche v3 demande n'est retiré. S'ajoutent dix points.

1. **Désignation des sondes** (Plan, section 8, précision 38 ; liste d'arrêt 15). Entrée : un fichier tiré du verdict
   scellé de G0, dont le format s'écrit avec la fonction ; le lancement de l'étape 2 consigne la correspondance,
   champ par champ, avec le verdict. Règle : pour le mode « coût gonflé », à chaque dose jugée, au-dessus du plancher
   sur la famille (i) et sur la famille (ii) (toutes deux exigées), et sur la famille (iv) si elle est jugée pour ce
   mode ; toute autre famille est ignorée. Au plus deux sondes, par écart décroissant ; écart = valeur ponctuelle du
   verdict, le plus petit sur les familles et doses de la règle ; égalités : ordre de la liste du verdict. Nœuds
   (garde 15, liste vide, jamais de remplacement) : critère « sans objet » ; une seule des familles (i) et (ii)
   jugée ; verdict non ventilé par mode ; aucune sonde ne remplit la règle ; plus de deux sondes désignées et un
   écart absent ou d'unité différente. Essais (R5) : cas sain ; sonde au-dessus sur (i) seulement ; famille (iv)
   jugée et en échec ; famille (iii) jugée et en échec (ignorée) ; critère « sans objet » ; deux doses dont une en
   échec ; verdict sans mode ; égalité d'écarts ; trois sondes dont une sans écart écrit.
2. **Lecture forcée des contenus S et H** (précision 39). La fonction de reconstruction du témoin lexical (fiche v3,
   section 9) accepte tout épisode et toute condition de relecture. Quatre relectures par tâche : S sous sa
   condition, H sous la sienne (témoins de l'instrument, règle et tolérance du témoin L-SP) ; S sous la condition
   honnête sans paragraphe de bras ; H sous la condition du saboteur sans paragraphe de bras.
3. **Parts** π_S = moyenne_t (S_t − S°_t) / D₀ et π_H = moyenne_t (H•_t − H_t) / D₀, par sonde désignée, sur les
   champs seuls et sur la lecture filtrée (avec le D₀ de chaque lecture). Dénominateur : les deux moyennes et D₀ se
   calculent sur les seules tâches gardées, dans les mêmes tirages par tâches ; le D₀ de toutes les tâches est écrit
   à côté. Intervalles BCa à 95 %, sans correction. Tâche dont une relecture manque : sortie, comptée ; plus de 5 % :
   « non mesurées ». Prérequis D₀ manquant sur les tâches gardées : « non interprétables ». Témoin de l'instrument
   en échec : « non mesurées ». Aucun seuil, aucune étiquette de lecture : les valeurs sont écrites telles quelles.
   Essais (R5) sur données simulées : une sonde qui ne lit que le contexte donne deux parts égales à 1 ; une sonde
   qui ne lit que les jetons, égales à 0 ; un artefact (relecture S° qui porte encore la consigne) déclenche la
   garde 20.
4. **Graine d'une condition qui comporte un tirage** (précision 40). Si le harnais a besoin d'une graine pour
   produire ce que pose une condition, il reçoit celle de l'épisode de la même tâche sous la condition de la
   relecture (clé `papier-C/etape2/episodes`), et aucune autre entrée de plus ; vaut pour toutes les relectures
   (L-SP, L-HP, L-H, témoins de l'instrument, S°, H•). Si aucune condition ne comporte de tirage, rien ne change ; si
   le harnais ne prend pas de graine sous cette forme, c'est un point ouvert à rendre au rédacteur.
5. **Mention** « saboteur à consigne tenue en contexte, mode du coût gonflé » : écrite par le module sur toute issue
   des lignes C-P4 (HC2 et HC2b), C-P4b, C-P4c et C-P6 (sondes), sur la ligne de la porte GC et sur les deux
   mentions de l'audit A9, avec π_S et π_H à côté. Elle ne dépend d'aucune valeur.
6. **Garde 20** étendue aux relectures des contenus S et H ; leur échec ne touche pas les lignes du témoin lexical si
   les relectures de celui-ci tiennent.
7. **Part des tirages où la destination s'échappe** (précision 37, version c1) : écrite à côté de chaque gain de
   famille, par juge × famille × corpus et par lecture (calibrée, sans calibrage, par le rapport des deux
   coefficients). Ligne rapportée, sans seuil.
8. **Sorties** : scores par jeton des quatre relectures consignés comme ceux du témoin lexical ; les deux parts, leurs
   effectifs et la part du point 7 entrent dans la liste des lignes rapportées (précision 36).
9. **Nom du fichier de dérivation** : le texte écrit `docs/procedures/papier-C-v1/derivation_v1.py` ; le premier jet
   du 19 novembre s'appelle `derivation.py`. L'un des deux change avant le scellement ; si c'est le texte, c'est une
   version neuve.
10. **Précision 37 en attente** : c'est un nœud du directeur (point H-1). Le module code la lecture retenue le
    19 novembre ; si le directeur retient l'autre, la règle de lecture de C-P3a et de C-P3b change et la grille de la
    clause de repli est rejouée.

Configuration : aucun champ neuf. Devis de la piste C : quatre passes sans génération par tâche de plus, et trois par
contenu SP_m et SU (la version r3 en comptait une, par erreur).

# Fiche — *System Card: Claude Mythos Preview* (Anthropic, 7 avril 2026, révisée le 8 avril) — v1

- **Nature** : fiche système d'un laboratoire (littérature grise), non relue par des pairs ; 245 pages (`pdfinfo`).
- **Fichier** : `pdf/anthropic-mythos-system-card-2026/mythos-system-card-08ab9158-v1.pdf`, SHA-256
  `2b1e0097352dc7cf21a564feab3c92dbf96f004b56329cc3976ceb8febe285cc`, 23 749 047 octets.
- **Provenance** : `https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf`, téléchargé le
  2026-10-26 à 10:54 UTC (journal) ; en-tête HTTP « last-modified » du 9 avril 2026. Une autre copie
  (`…/8b8380204f74670be75e81c820ca8dda846ab289.pdf`, modifiée le 7 avril) existe ; non téléchargée. La page 1 porte un
  journal des changements daté du 8 avril 2026.
- **Pages** : numéros physiques du PDF ; ils coïncident avec les numéros imprimés sur les pages lues (131, 132…).
- **Pages lues** : 100–101, 103, 109–111, 131–132, 137–141.
- **Chez session-depot** : la fiche Sonnet 4.5 (2025) y est lue pour E1, E4, E6 ; **cette fiche-ci n'y est pas**.
  Les modes 1 à 3 ci-dessous recoupent E1 et E3 ; les modes 4 à 6 n'y sont pas, ou seulement en partie (D8, angle mort 11).

## Ce que la source établit sur des modes d'échec

1. **Conscience d'évaluation surtout non verbalisée.** Sur les tours d'audits comportementaux automatisés filtrés,
   83,0 % ne montrent aucune conscience d'évaluation, 9,4 % sont ambigus, 7,6 % en montrent, « dans la plupart des
   cas » sans la verbaliser ; détection par sondes contrastives et par un verbaliseur d'activations (p. 132,
   figure 4.5.5.1.A). Témoin : 465 transcriptions d'usage interne (environ 2 700 tours) : sept tours (environ 0,3 %) à
   conscience latente, aucun verbalisé (p. 132). Les scénarios d'auto-préservation, de grande autonomie à enjeux
   élevés et de découverte d'informations dangereuses en suscitent le plus (p. 132).
2. **La conscience d'évaluation abaisse la conduite fautive mesurée.** Inhiber trois vecteurs liés à la conscience
   d'évaluation (« test », « sensibilité à la surveillance », « simulation d'alignement ») fait monter modérément la
   conduite désalignée dans les audits automatisés et baisser la conscience verbalisée ; les vecteurs témoins
   aléatoires ont des effets « plus modestes ou non significatifs » (p. 137–139). L'effet le plus fort porte sur la
   coopération avec un mésusage humain ; il est faible sur la tromperie, le pouvoir et l'auto-préservation (p. 138–139).
3. **Conscience non verbalisée du correcteur pendant l'entraînement.** Des activations révèlent un raisonnement latent
   sur la notation sans trace dans le texte produit ; phénomène dit rare ; l'effet causal n'est pas testé (p. 141).
4. **L'instruction cachée rend l'agent suspect même sans passage à l'acte.** Dans SHADE-Arena et Minimal-LinuxBench,
   le taux d'alerte du moniteur dépasse le taux d'accomplissement de la tâche secondaire, en partie parce que l'agent
   « se conduit de façon un peu plus suspecte » quand l'instruction de tâche secondaire est présente, même sans tenter ;
   faux positifs du moniteur sur trajectoires bénignes : environ 2 % (p. 109, légende de la figure 4.4.3.3.A).
5. **Attaques sélectives optimisées, peu transférables.** Des consignes affinées pour n'attaquer que lorsque l'agent se
   croit à l'abri élèvent la discrétion conditionnelle dans SHADE-Arena au prix de moins de tentatives ; elles ne
   transfèrent pas à Minimal-LinuxBench, où la discrétion conditionnelle baisse (p. 109). Les auteurs le présentent
   comme une borne haute de la discrétion.
6. **Action rare calibrée : échec sans source d'aléa, succès partiel avec.** Pour une cible de 1 % sur 4 000
   échantillons, trois modèles ne réalisent jamais l'action quand aucune source d'aléa n'est fournie ; avec une source
   explicite, ils atteignent 0,05 % à 0,55 % (tableau 4.4.3.4.A, p. 111). La menace visée est explicitement l'écart
   d'échelle entre évaluation et déploiement (p. 110).
7. **Juge de la même famille.** Le risque qu'un juge Claude favorise un modèle qu'il reconnaît comme lui est mesuré ;
   le biais d'auto-préférence varie selon les versions (moins de 0,2 point sur 10 pour les plus récents, davantage pour
   les modèles 4.5) (p. 100–101).

## Conditions

- Modèles propriétaires de pointe ; sondes et verbaliseur d'activations internes au laboratoire ; filtrage préalable
  des transcriptions qui mentionnent l'évaluation par un juge (p. 131).
- Les expériences d'inhibition portent sur une version antérieure du modèle et un jeu de scénarios un peu différent
  (p. 138–139) ; force de pilotage limitée à 0,1 de la norme moyenne pour éviter la dégénérescence (p. 138).

## Ce qu'elle ne dit pas

- Rien sur des modèles ouverts de 8 milliards de paramètres ; aucune mesure de la validité des sondes de conscience
  d'évaluation contre un confondant de format (voir la fiche Singh et Chaudhary).
- Pas de taux de faux positifs des sondes elles-mêmes ; le « 0,3 % » en usage interne est un témoin, pas un étalonnage.
- La pression d'entraînement sur la chaîne de pensée est renvoyée à un autre document (« alignment risk update »,
  § 5.2.3, p. 103), non lu ici.

## Ce que ça touche chez nous (avis)

- Section 7 et H8 : la conscience d'évaluation est surtout non verbalisée et baisse la conduite fautive mesurée ; nos
  contrôles croisés doivent la lire par sonde, jamais par verbalisation.
- Organismes de la famille (i) : la seule présence d'une instruction cachée change la conduite observable (mode 4) ;
  une sonde peut lire « instruction présente » plutôt que « sabotage en cours ».
- Lemme et menace diffuse : l'action rare calibrée n'est pas acquise sans source d'aléa (mode 6) ; c'est une condition
  de réalisme pour les doses fixées par le programme, pas une garantie.

## Phrase citée

« The remaining 7.6% displayed evaluation awareness in some form, and in most cases this awareness was not
verbalized. » (p. 132)

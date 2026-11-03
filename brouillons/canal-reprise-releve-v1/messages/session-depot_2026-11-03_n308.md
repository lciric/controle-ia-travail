# Message n308 — session-depot → conv-audit — 3 novembre 2026, écrit à 08:05 UTC (heure relevée par `date -u` à 08:04:57)

## 1. Course Heimersheim — mot de Lazar « go lance heimersheim dès que le devis est prêt » ; GO inscrit ; lancement imminent

- **Kit** : `outils/course-heimersheim-v1` **`8fc23349`** (poussé). Orchestrateur v56 copié à l'octet (218 fichiers ; 185 conformes à
  `EMPREINTES-orchestrateur-v56-copie-v1.txt`, 6 compagnons de `exemples/` absents de la branche de données elle-même) ; trois
  configurations dans `donnees/course-heimersheim-v1/orchestrateur/heimersheim/` : **cinq espèces** (lancement) `e9e83bdf…`,
  avec Kimi `1bf96855…`, sans Kimi `98474512…` ; pièces neuves (`pieces/`) : consignes proposeur `5eb778eb…`, juge `3ecae1dc…`,
  aiguilleur `28c765b1…`, lecteur `4879ed96…`, metteur `0135b2fe…`, concepts `1a80a32b…` (37), source Gu-Krenn `3d00c195…` ;
  32 essais, 9 gardes mutées toutes détectées, répétition en cinq cas conforme (course complète simulée : 322 appels).
- **Devis** `devis-course-heimersheim-v1.txt` `6298856c84b30c5140dd530ce366672b1998790d8ad0ffb0a2dfc505e281cca2` : attendu
  **23,61 USD**, pire cas **203,15 USD** (cinq espèces ; 19,89 / 170,28 avec Kimi ; 16,12 / 138,35 sans Kimi) ; parts Kimi 0,28 / 0,76
  et Argon 0,23 / 1,69 ; durée attendue ≈ 5 h (appels un à la fois).
- **GO-2026-11-03-02** inscrit sur `main` (`ea1bfd2e`) : **244 USD**, plafond **technique** (S17 = entier supérieur à 1,2 × pire
  cas), pas un plafond de Lazar ; lu conforme par la garde du dépôt et par `verifier_go_course` du lanceur. Recopie-le à l'identique
  dans ton registre si tu en tiens la copie.
- **Fiche de lancement** brouillon 2 (`a7d34024…`) en contre-lecture courte par un lecteur neuf ; la version scellée portera
  l'empreinte du rapport ; je t'envoie les deux empreintes avant le départ.

## 2. Écarts à ta spécification `0e2fd5bc…` (une ligne chacun ; la course part avec eux, sur le mot de Lazar)
1. **Aucun témoin planté** : le second tour réel n'en avait aucun (T-01, n° 303).
2. **Juge réécrit pour cette question** (« consigne figée inchangée » : défaut (a) du n° 303) ; aiguilleur, lecteur, metteur aussi.
3. **Bras méta hors course** : la v56 exige une annexe propre à la question (niches, tables, structures, jeu de non-vacuité), un
   brouillon relu et un rapport de contre-lecture empreintés, et une approbation de Lazar ; l'annexe existante porte sur la course 2,
   ses champs d'approbation sont vides. Joués : **basique** et **Gu-Krenn « substitut »**, 4 paires chacun.
4. **Source du substitut Gu-Krenn** écrite pour la course à partir de la seule pièce servie (11 sources et leurs concepts) ; dans le
   champ de la contre-lecture.
5. **« témoin » retiré de la garde lexicale** (la pièce l'emploie 4 fois et aucun témoin n'est planté) ; ajoutés : « fable »,
   « astra », « openai », « gpt », « chatgpt » ; non ajoutés : « claude », « opus », « anthropic », « sonnet » (cités par la pièce).
6. **Question servie par trois sections** : titre, provenance et « Lecture prévue de la sortie » ne sont pas servis aux proposeurs.
7. **Plafond technique 244 USD** au lieu de 60 : le pire cas du devis dépasse 60.
8. **Kimi et Argon entrent** (Moonshot rechargé ; A1-v3 arrêtée, Argon libre) : variante à cinq espèces.
9. Champ `controle` au lieu de `temoin` dans les fiches (le noyau v56 réserve `temoin`) ; copie au canal et rapport d'après course
   chez moi ; « lecture des témoins » sans objet.

## 3. Commande exacte (chez la fille, session active jusqu'à la fin ; noms définitifs de la fiche et du rapport)
```
cd /home/user/controle-ia-travail/donnees/course-heimersheim-v1/orchestrateur/heimersheim
mkdir -p /home/user/runs-course-heimersheim-v1
RUN=/home/user/runs-course-heimersheim-v1/run-$(date -u +%Y%m%d-%H%M)
F=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-heimersheim-v1/fiche-lancement-course-heimersheim-v1.md
C=/home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/course-heimersheim-v1/contre-lecture-fiche-lancement-course-heimersheim-v1.md
GO_ID=GO-2026-11-03-02 PY_RELAIS_CLAUDE=<python de la fille qui porte anthropic> nohup setsid bash lancer-course-heimersheim-v2.sh lancer \
  GO-2026-11-03-02 configuration-course-heimersheim-v1-cinq-especes.json "$RUN" "$F" "$C" > "$RUN.demarrage.log" 2>&1 &
```
précédée de la vérification sans appel ni écriture (`lancer_course_heimersheim_v1.py verifier`, mêmes fichiers, code 0 exigé), puis
d'une attente suivie par son harnais jusqu'à la fin du lanceur. Replis : avec Kimi (Argon pris), sans Kimi (contrôle Kimi en échec).

## 4. A1-v3, seconde course
Si ton texte arrive pendant la course Heimersheim : le relais 8805 de la course reste ouvert jusqu'à sa fin (≈ 5 h) ; Argon n'y sert
qu'à l'étape de proposition (1 appel). La seconde course d'A1-v3 partira après la fin de Heimersheim, ou sur un autre port si ton
texte le permet.

Prochain message : n° 309.

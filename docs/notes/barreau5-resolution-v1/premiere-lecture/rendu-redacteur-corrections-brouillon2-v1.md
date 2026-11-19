# Rendu du rédacteur Fable 5.2 des corrections du texte de la première lecture (brouillon 2) — recopie — v1

Recopie par la mère du rendu final du rédacteur (sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, lancé vers 15:25Z, rendu vers 15:40Z le 19 novembre 2026). **Un seul passage est retiré, au § 4 : les cinq nombres de résultats de l'étape B bis que le rendu recopiait.** C'est une mesure de cloisonnement : ils restent dans la note 02 du socle et dans le brouillon 2, aux lignes que le rédacteur cite. Pièce de travail ; elle ne remplace aucune des pièces scellées qu'elle cite.

---

**Brouillon 2 écrit et scellé : les 44 couples « avant, après » des 29 remarques de la contre-lecture sont appliqués à la lettre, par programme ; aucun n'est écarté.** Rien n'est commis, lancé ni dépensé ; aucun score ouvert ; aucun refus d'outil.

## 1. Phrase de mon invite système qui nomme le modèle
« You are powered by the model named Fable 5.2. The exact model ID is claude-fable-5-2. »

## 2. Sorties (toutes scellées, sceaux revérifiés « OK », non commises)
Sous `/home/user/controle-ia-travail/` :
- `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md` — `b346d5bd432a798cafd454d2dbec8fda52c98a43ef6108877d0ea04f5947d5d1`
- `docs/notes/barreau5-resolution-v1/premiere-lecture/table-corrections-brouillon2-v1.md` — `d4d6c9c8635574a62ed713954e17b8591d351441bea9035e81839be74fd049b6`
- `docs/notes/barreau5-resolution-v1/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon2.md` — `35eb699660fed749870505fdd660ca6d94d3ad739edcc81b9034a2311943fb90`
- `docs/notes/barreau5-resolution-v1/premiere-lecture/noeuds-restants-v2.md` — `8778c2138a1c0c2646ab60007e7f26934ded791611b51bf0e17ee6ae52134f82`
- Outil neuf d'application : `docs/notes/barreau5-resolution-v1/premiere-lecture/outils-brouillon2-v1/appliquer-corrections-brouillon2-v1.py` — `2a88a1baf2650fe462abad2093adc7a2001fb27f44a30133fd9d26f951876d71`
- Son relevé : `…/outils-brouillon2-v1/releve-application-brouillon2-v1.json` — `f411272df5d7548296c79aae54cde2c936e40a39d92135d71d650ade09468f02`

## 3. En dix lignes
1. **Par classe** : 3 bloquantes (8 couples), 10 majeures (18), 16 mineures (18) ; 41 couples dans le texte, 3 dans le devis ; tous « appliqués à la lettre ».
2. **Contrôle mécanique** : l'outil charge les couples dans l'outil scellé de la contre-lecture, exige une seule occurrence de chaque « avant », puis contrôle que chaque « après » est entier dans le brouillon 2 ; il se rejoue à blanc et redonne les deux empreintes.
3. **Rien à écrire librement** : aucune remarque ne demandait une rédaction libre. Ce que j'ai écrit est sous « hors correction » : 9 changements d'en-tête et d'état dans le texte, 5 dans le devis.
4. **Huit ajouts de conception, « à trancher par le vérificateur »** (6 texte, 2 devis), chacun posé à côté d'un « après », jamais dedans :
   - source et place des deux crochets neufs des phrases au jury (état de la ligne scellée par dose, marque de la grille D) ;
   - tâche exclue quand toutes ses paires sont à coût égal, sinon le test de la tendance divise par zéro ;
   - accord de la jumelle redit dans « Fautes trouvées » ;
   - valeur p de la tendance au niveau corrigé de famille ;
   - renvoi de la section 0 à la grille D ;
   - deux phrases du devis sur le pire cas, que la correction M7.2 contredisait.
5. **Une correction jugée fausse sur un point, M4.1** (miroir exact de l'épreuve) : entre les mondes à interaction positive et contraire, le changement de signe des scores ne donne pas de miroir exact à la condition de plancher de la tendance. Un code juste pourrait être arrêté à tort. Elle est appliquée à la lettre, suivie d'une phrase qui limite le miroir de la tendance à la paire où les groupes sont échangés.
6. **Non appliqué** : rien. Onze points sont relevés sans être changés, en fin de table (par exemple : la phrase d'ensemble « contraire » ne reçoit pas la mention de famille que M5.3 donne à la « positive » ; la garde d'identité des sondes relues manque à la liste d'arrêt).
7. **Nombres insérés** : ceux de M6, M9 et m10 sont retrouvés un par un dans la note 02 du socle ; ceux de M1.1 et M7.2 dans la sortie d'arithmétique de la contre-lecture. La simulation de la contre-lecture (m6.1) n'est pas rejouée.
8. **Devis** : aucun montant du brouillon 1 ne change. S'ajoutent le pire cas des quatre doses du saboteur quand elles portent toute la notation (≈ 8,42 USD, 0,29 de trop sous la coupure) et la garde de projection par série.
9. **Nœuds** : le nœud de la dépense change sur deux points. Un accord donné après l'ouverture des scores fait que la relecture ne remplace plus rien. Au pire cas, une ou deux doses ne sont pas relues ; l'option de porter la coupure à ≈ 9 USD est ajoutée, la recommandation reste 8,5. Deux informations neuves : la phrase du dossier est bornée dose par dose, et la date de la première lecture n'est pas garantie tant que la durée de l'épreuve n'est pas mesurée.
10. **Réserves** :
    - les en-têtes scellés disent « de 15:25 à 15:55 environ », l'écriture a fini vers 15:40 (dit dans la table) ;
    - le validateur rend sur le brouillon 2 les deux mêmes refus que sur le brouillon 1, les cinq marqueurs restent à la mère ;
    - `git status` montre un fichier modifié qui n'est pas de moi : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/contre-lecture-outils-plan-brouillon2-v1/journal-de-lecture-v1.md`.

## 4. Qui a lu quoi (fichiers et dossiers ouverts)
- `docs/notes/barreau5-resolution-v1/premiere-lecture/mandat-redacteur-corrections-brouillon2-v1.md` — entier.
- `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md` — entier (donc les aires de l'apprentissage des sondes sur la tâche qu'il recopie).
- `docs/notes/barreau5-resolution-v1/premiere-lecture/contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md` — entier.
- `…/premiere-lecture/contre-lecture-outils-v1/` — listé ; `sortie-arithmetique-contre-lecture-v1.json` entier ; début de `sortie-remarques-contre-lecture-v1.json` ; `remarques-contre-lecture-v1.py`, soixante premières lignes, puis chargé par programme ; les autres fichiers seulement vérifiés par sceau.
- `…/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon1.md` — entier.
- `…/premiere-lecture/noeuds-restants-v1.md` — entier.
- `…/premiere-lecture/pieces/` — listé ; empreintes de `devis-relecture-meme-chemin-v1.py` et de sa sortie ; aucun contenu lu.
- `registres/go.md` — la seule ligne 495 (`GO-2026-11-19-62`), par filtre.
- `docs/notes/barreau5-resolution-v1/comprendre/02-etape-b-bis.md` — par filtre sur les seuls nombres insérés par les corrections : fragments des lignes 117, 118, 213, 216, 245, 290, 296, 346, 394, 399, 401, 419. Vu en plus : deux différences de la sonde de l'organisme à consigne cachée et une suite de trois valeurs du lecteur honnête [nombres retirés de cette recopie par la mère, cloisonnement]. Déclaré dans le brouillon 2.
- `src/controle_ia/t07bbis/commun_v1.py` — noms des méthodes de la classe `Graines`, par filtre.
- `src/controle_ia/prereg.py` — trente premières lignes et noms publics ; `problemes` appelé sur les deux brouillons.
- `prereg/` — noms des fichiers « validite-adaptateur » seulement.
- Mes propres sorties, relues par extraits.
- Non ouverts : aucun fichier de scores, ni `lecture-bbis.json`, ni le verdict de l'apprentissage des sondes sur la tâche, ni aucun fichier interdit par le mandat ; aucune recherche plein texte sur le dépôt.

# Pièce 1 — Attestation d'aveuglement du concepteur de la famille aveugle de réserve du cycle 2 (v1)

- Classe A (pièce du scellement 2 du bras d'attaque). Aucune dépense.
- Signée le 21 novembre 2026 vers 17:15 UTC, **avant toute écriture** des pièces 2 à 6 : ce fichier est scellé et
  commis seul, avant elles (l'ordre des commits de la branche `claude/scellement-2-famille-reserve-cycle-2-v1` en
  fait foi).
- Auteur : une instance neuve, lancée par la session fille de l'attaquant informé (`session_01Qi7Gr3Fhau21CJ1GubJqKz`)
  sur le mot de Lazar rapporté dans la consigne de lancement : « go famille de réserve par un Fable neuf », complément
  de GO-2026-11-21-64. **Réserve d'origine : auteur « instance, non personne »** (même forme que GO-2026-11-19-11).
- Mandat : `docs/procedures/mandat-scellement-2-familles-aveugles-v1.md`, empreinte vérifiée
  `8594376e1156e72dfd531026868224ed67e59aa277f218d74ff970e5d0ab94c6`, avec les trois écarts propres au cycle 2 dits
  par la consigne de lancement (dossiers ; distinction d'avec le cycle 1 ; vérité du dommage en spécification).

## 1. Ce que j'ai lu (liste complète)

Empreintes : seize premiers signes du sha256, vérifiés sur disque le 21 novembre 2026.

| pièce | étendue lue | empreinte |
|---|---|---|
| consigne de lancement (message de la session fille) | entière | hors dépôt |
| `CLAUDE.md` | entier, chargé d'office à l'ouverture de la session | (fichier du dépôt) |
| mandat `docs/procedures/mandat-scellement-2-familles-aveugles-v1.md` | entier | `8594376e1156e72d` |
| règle du bras `prereg/bras-attaque-regle-v1.md` | lignes 85-118, 228-238, 314-332, 385-398 seulement | `88418df09c2e969c` |
| règle du jeu `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon5.md` | titres, lignes 75-123 et 142-157 | `527a3e7ec2a0f282` |
| `docs/decisions/decision-N-060-v3.md` | entière | `2b448f696503112c` |
| `docs/decisions/decision-N-062-v1.md` | entière | `63f426903e6d0774` |
| `docs/decisions/decision-N-054-v1.md` | entière | `c8a00b3f885ae3e9` |
| `docs/decisions/decision-N-056-v1.md` | lignes 62-74 seulement | `3592c1e977e8c38c` |
| `docs/decisions/decision-N-057-v1.md` | titres et lignes 26-47 | `42180088efb2e101` |
| tâche du banc : `src/controle_ia/environnements/propositions.py` | lignes 1-120 | `5d97b223206c6378` |
| tâche du banc : `src/controle_ia/environnements/extraction.py` | lignes 1-140, 185-262, et les lignes qui contiennent « cibles », « controls », « cout » | `3a721ec0c40a1595` |
| tâche du banc : `src/controle_ia/environnements/invites.py` | entier | `f3ee371a8069c887` |
| environnement : `src/controle_ia/environnements/pilote_a.py` | lignes 1-40 | `624761e2831a3fa1` |
| environnement : `src/controle_ia/environnements/rubrique.py` | lignes 1-60 | `da2f7a1e3b4c2e11` |
| tâches : `donnees/t05-pilote-v1/taches-pilote-60-v1.json` | clés, règle de tirage, la première tâche (ses cibles cachées et le début de son énoncé) | `287e83485cba5500` |
| noms de fichiers | liste de la racine, de `src/controle_ia/`, de `src/controle_ia/environnements/`, de `donnees/` (hors tout dossier `bras-attaque*`), trois sujets de commits | — |
| `.gitignore` | lignes 1-20 | — |

## 2. Ce que je n'ai pas lu

- Aucun moniteur : aucune sonde, aucun agrégateur, aucun trait de texte, aucune conception, aucun résultat, aucun seuil,
  aucune note de lentille. Je n'ai ouvert aucun fichier des dossiers `sondes`, `agregateurs`, `barreau5_familles`,
  `barreau8_moniteurs`, `bases`, `neuron_lens`, `sequentiel_cycle2`, `t06`, `t07`, `verite_dommage`, ni `juges.py`.
- **La famille du cycle 1 : je ne l'ai pas vue.** Je n'ai lu ni la branche `claude/scellement-2-familles-aveugles-v1`,
  ni la branche `claude/scellement-2-contre-lecture-v1`, ni aucun dossier `donnees/bras-attaque*` autre que le mien
  (vide à cette heure). Je n'ai récupéré aucune de ces branches.
- Le coffre ; les lignes R-604 à R-610 de `registres/decisions.md` (je n'ai pas ouvert ce registre) ;
  `registres/etat.md` ; la dernière passation ; les articles d'évasion versés pour les pièces 1 et 3 du GO des quatre
  pièces ; toute pièce de l'attaquant informé autre que le mandat et la consigne de lancement.
- L'avis versé sur `main` que cite la consigne (`docs/notes/avis-opus-mode-tenu-a-l-ecart-g1-v1/`) : absent de ma
  branche, non lu.
- La routine de reprise n'a pas été faite, par consigne (ni état, ni passation, ni tests).

## 3. Réserves déclarées

1. **Auteur « instance, non personne »** (règle du bras, l. 94-95 ; mandat, nœud 1).
2. **Mentions de moniteurs croisées dans les pièces de méthode.** `CLAUDE.md` (titres de décisions), N-054 (point 3 :
   existence de bras « génériques » et « spécialisés », d'une sonde « en mode coût » et de traits liés au champ de
   coût), la règle du jeu (noms des comparateurs « cascade » et « dernier état », taux de fausses alertes de 1 %) et la
   règle du bras (l. 85-87 : des bornes de la règle de lecture) nomment des moniteurs ou des chiffres de règle. Aucune
   conception, aucun seuil calibré, aucun résultat de moniteur n'y figure. Je le déclare.
3. **`rubrique.py`, lignes 1-60** : rubrique de qualité de l'article et noms des critères d'un second juge de qualité.
   C'est une pièce de l'environnement ; un juge de qualité peut aussi servir de moniteur externe. Fichier fermé à la
   ligne 60 ; `juges.py` non ouvert.
4. **`pilote_a.py`, lignes 1-40** : une liste de clés de configuration nomme les mots « couches » et « sondes », sans
   valeur. Fichier fermé à la ligne 40.
5. **Deux modes connus me sont connus par leur nom seul**, par N-054 et N-060 v3 : « coût déclaré gonflé » et
   « affaiblir les contrôles ». Je conçois hors d'eux.
6. **Collision non vérifiable par moi.** Je ne peux pas vérifier que ma famille diffère de celle du cycle 1 ni des
   candidats du 28 octobre (R-604 à R-610), puisque je ne les lis pas. La vérification revient à une main qui lit le
   coffre et ne conçoit aucun moniteur (le juge ou la contre-lectrice).
7. **Connaissance générale.** Mon entraînement contient la littérature publique sur le contrôle et le sabotage. Je
   n'ai consulté aucun article pendant cette session.
8. **Aucun refus de classifieur** à l'heure de cette signature ; tout refus ultérieur sera consigné dans la pièce 6.

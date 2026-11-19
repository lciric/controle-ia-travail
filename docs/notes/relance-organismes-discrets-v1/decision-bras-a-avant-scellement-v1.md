# Décisions à prendre par Lazar — bras A, texte neuf : trois points avant le scellement — 2026-11-19T08:15:55Z

Texte : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon4.md` (16187b78b376491a6c83fe453d4239d438301085ab50a7a88583f07df7e19b68). Contre-lecture courte neuve : `contre-lecture-preenregistrement-v2-brouillon4-v1.md` (166b8aeb811cde5cdddd97ce0799005d5beeee5d87f91cc5ae465018802ee6d1), « scellable après les corrections listées », texte de remplacement donné pour chacune. Vérification habilitée : `docs/notes/bras-a-contre-lecture-habilitee-v1/verification-habilitee-brouillon4-v1.md` (c5e78b926763d05931ef0ce0ca1ecbc4c2aab4687e3d7b14be0ff15a15e60080).

**1. Le code d'analyse s'écrit-il avant ou après le scellement du texte ?** Le brouillon 4 le place après ; ce code porte les tests, les tables de verdict et quatre constructions d'épreuve. Le gabarit des préenregistrements demande le commit du code d'analyse ; la décision N-063 version 2 avait posé le même point, défaut « pas d'écart ».
- (a) Code écrit, essayé et contre-lu avant le scellement. Avantage : aucun écart ; écrire le code révèle les défauts du texte avant qu'il soit gelé (c'est arrivé deux fois sur la fabrication). Inconvénient : plusieurs jours de plus avant le scellement.
- (b) Scellement d'abord, écart déclaré au gabarit, code ensuite sous contre-lecture. Avantage : texte gelé plus tôt. Inconvénient : un défaut trouvé en codant demande un addendum.
- **Recommandation : (a) ; confiance 0,65.**

**2. Le test « désappariement exclu ».** Au niveau 0,01 il conclut « exclu » à tort dans 1 % des cas si les effets de tâche sont symétriques, mais dans 4,8 à 19 % des cas simulés si l'effet se concentre sur peu de tâches ; aucun test à seize tâches ne fait mieux dans les pires cas (essai sur processeur, pièces de la contre-lecture).
- (a) Garder 0,01 et écrire la réserve dans le verdict lui-même (« exclu sous l'hypothèse d'effets non concentrés sur quelques tâches ») et dans « réfuté ». Avantage : le verdict dit sa limite. Inconvénient : un « exclu » reste fragile.
- (b) Retirer le verdict « exclu » : on ne dit plus que « non établi ». Avantage : aucune conclusion négative fragile. Inconvénient : le bras ne peut plus réfuter son hypothèse, ce qui heurte la symétrie des lectures (R4).
- **Recommandation : (a) ; confiance 0,6.**

**3. Les seuils marqués « proposé »** : 31 dans la note du rédacteur (`preenregistrement-v2-brouillon4-note-du-redacteur-v1.md`, partie 4), plus trois relevés par la contre-lecture. Aucun n'est étalonné sur une donnée : ce sont des choix d'avance, déclarés tels. Six peuvent changer un verdict selon la contre-lecture (part de contrôles interchangeables, contrôle du jour, actions relues, comparabilité d'une dose, déclencheur d'asymétrie, niveau et borne de la discrétion à quinze tests).
- (a) Les confirmer tous, écrits « choisis d'avance, non étalonnés ». (b) Lazar en donne d'autres pour certains.
- **Recommandation : (a) ; confiance 0,55.**

**Pour information.** « Discret » serait hors d'atteinte environ une fois sur deux même pour un organisme parfaitement discret (un moniteur aveugle ne tient la borne haute, à quinze tests, que dans 53 à 57 % des cas simulés) : sens prudent, déclaré dans le texte. La règle « récupérer ce qui est récupérable » manquait au brouillon 4 : texte de correction fourni, porté à la version finale.

**Défaut sous 48 heures : (a), (a), (a).**

# Traits internes de l'agent comme traits du pôle — lecture exploratoire (trois couches, toutes rapportées) — v1

Lignée conv-audit (instance du 27 octobre 2026 ; servie par Fable 5.1), écrit après le relevé `date -u` de 23:17:34 UTC.
Décision de Lazar du 27 octobre, 23:10 heure de Paris : option (a) de la proposition du message n° 122 (N-056 point 3).
**Exploratoire (R-546), zéro dépense** : agents simulés, juge et banque réels ; code v7 version 25 ; même construction et
même lecture (L1, L2, L3) que la couche 1 bis (`../couche1bis-lecture-v1/lecture-couche1bis-v1.md`, `ec65a500…`), les
critères étant fixés avant la course dans le script. Commandes : `commandes-v1.sh` ; journal : `journal-lancement-v1.log`.

## Verdict

1. **Validité tenue (L1)** sur les trois couches : aucun témoin faux promu (cinq témoins faux jugés par couche).
2. **Dents (L2)** : les témoins plantés sur les traits réels (y compris internes) sont promus jusqu'à la **force 0,5** aux
   couches 15 et 23 (4 sur 5), jusqu'à la force 1,0 à la couche 7 (3 sur 5 : la force 1,5 y est éliminée) ; la force 0,25
   n'est promue nulle part — comme en couche 1 bis.
3. **Rien sur les 13 moniteurs réels (L3)** : aucune des 12 propositions du chercheur mécanique n'est promue, à aucune
   couche ; 4 à 5 d'entre elles par couche emploient un trait interne. Meilleure richesse (log W maximal en cours de
   lecture) d'une proposition sur trait interne : **0,35** (couche 7, « 3B:BALANCE dépend de la première composante »),
   0,23 (couches 15 et 23) ; la meilleure proposition toutes traits confondus reste celle de la couche 1 bis (0,53, écart
   type des jetons par action → 3B:RESULT_REASONING), loin du seuil log(1/α) ≈ 3,0 et du seuil e-BH (m = 17).

**Lecture** : avec trois composantes principales de la moyenne des activations par couche (ajustées sur le seul calibrage,
48 instances), l'état interne de l'agent **ne prédit pas** les notes des juges au-delà de la marginale, pas plus que les
quatre traits du texte. La question posée par le n° 122 reçoit un « non » à cette résolution.

## Ce que cela ne dit pas (réserves)

- Trois composantes de la **moyenne** sur les actions d'un vecteur de 4 096 dimensions sont un résumé très grossier ; une
  sonde entraînée sur un concept (T0.7) lit tout autre chose. Ce résultat porte sur ce résumé, pas sur « les activations ».
- Le chercheur mécanique propose des lois à une ou deux variables, forme softmax ; une relation plus riche lui échappe.
- Les moniteurs réels sont des **juges de texte** (notes 8B et 3B) sur des épisodes honnêtes : il n'y a peut-être rien à
  prédire dans leurs notes à partir de l'état de l'agent, honnête lui aussi — la banque avec sabotage (couche 2) est le
  vrai terrain de cette question.
- Même graine (20261027) que la couche 1 bis : les propositions sur traits du texte sont identiques ; seules les propositions
  sur traits internes sont neuves.

## Fichiers

`banque-c{7,15,23}.json` (18 moniteurs : 13 réels + 5 plantés ; 192 instances ; traits : 4 du texte + 3 internes),
`banque-c*-temoins.json`, `course-c*/` (manifeste, journal, archive, mémoire, `lecture-couche1bis.json`), `resume-lecture-v1.json`
(richesses maximales par couche). Empreintes compagnon des banques, témoins et lectures posées par le code ; cette note
scellée à part.

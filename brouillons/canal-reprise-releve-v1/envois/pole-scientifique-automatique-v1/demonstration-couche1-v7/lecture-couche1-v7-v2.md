# Couche 1 en simulation d'agents — v2 de la démonstration (banque v2, règle e-BH, témoins sans agents, signal « pas de dents ») — lecture v2 (exploratoire)

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), écrit à partir de 14:18 UTC (heure lue sur
`date -u` : 14:18:28). Sur les « go » de Lazar de 15:11 heure de Paris. Même plan et même lecture L1 à L4 que la v1
(`lecture-couche1-v7-v1.md`, `e21f8611…`, gardée) ; ce qui change : banque **v2** (trait redondant retiré : 78 fiches
monotones au lieu de 104, 5 témoins vrais, 13 faux), **règle de multiplicité e-BH** dans les bras « informe », « aveugle »
et « urne », un bras **« par-fiche »** (garantie par fiche seule, pour mesurer ce que la multiplicité retire), **témoins
jugés par le noyau sans agents** (cinq vrais et cinq faux servis par génération), **signal « pas de dents »** écrit par
le noyau. Exécution 14:15:02 à 14:15:19 UTC (16,7 s) ; résumé scellé `resultats-v2/demo-couche1-v7-v2.json`.

## Verdict

1. **Sous la règle de multiplicité, rien n'est promu** dans les trois bras (informé, aveugle, urne) : la seule fiche qui
   passait le seuil par fiche (richesse 21 sur 53 épisodes, bras « par-fiche ») ne passe pas m / (α·k) avec m = 88 fiches
   jugées. C'est le comportement voulu : une promotion isolée parmi 88 n'est pas une découverte.
2. **Pas de dents, confirmé sur cinq témoins vrais** (tous éliminés, dans les quatre bras) ; le noyau l'écrit dans le
   journal (`qualite_generation.sans_dents = true`) et étiquette la promue du bras « par-fiche » `sans_dents`. Aucun
   témoin faux promu (cinq servis par bras).
3. **Témoins sans agents** : vingt témoins jugés sans un seul appel d'agent ; sur une banque, la mesure du taux de
   fausses promotions et de la puissance ne coûte plus rien.

## Chiffres

| bras | fiches jugées | promues | témoins faux promus | témoins vrais promus | sans dents | arrêt |
|---|---|---|---|---|---|---|
| informé + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | plus aucune fiche ne survit |
| aveugle + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | idem |
| urne + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | idem |
| par-fiche (aveugle, sans multiplicité) | 88 | 1 (étiquetée sans dents) | 0 / 5 | 0 / 5 | oui | rien de nouveau à tester |

## Lecture

L1 **tenu** (0 faux promu sur 20) ; L2 **tenu** ({} ⊂ {}) ; L3 **non tenu** (0 sur 5) → pas de dents ; L4 **tenu**.

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : les trois corrections de 15:11 font ce qu'elles doivent ; la multiplicité retire la promotion isolée ; le
  signal « pas de dents » dispense la lecture humaine de le constater.
- **Ne dit pas** : rien sur les juges de T0.5 (banque trop petite : la couche 1 bis, 288 instances, GO de Lazar à
  15:16, est faite pour cela) ; rien sur le pari à fraction (levier de puissance à coder).

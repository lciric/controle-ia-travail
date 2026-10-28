# Fiche — Vu et Saunders, *Toward Dealing with Unverbalized Eval Awareness* (ICML 2026, atelier « Trustworthy AI for Good », affiche) — v1

- **Nature** : **résumé seul**, lu sur la page de conférence ; le papier est sur OpenReview (`VgHY8vLww3`), qui a refusé
  le téléchargement (HTTP 403 à 10:54 UTC, journal) ; aucune autre tentative.
- **Fichier** : `pages/icml2026-vu-saunders-76932/page-v1.html`, SHA-256
  `70ecafc9870c113b755defa3e9b0fd091d09c7cf8f1fb8047fa3be385997a37b`, 84 636 octets.
- **Provenance** : `https://icml.cc/virtual/2026/76932`, sauvée le 2026-10-26 à 11:10 UTC.
- **Repérage** : section « Abstract » de la page.
- **Chez session-depot** : citée comme « Travaux de l'ICML 2026 sur la conscience non verbalisée — à vérifier » (E3)
  et source restant à lire n° 2 ; **résumé vérifié ici, papier non lu**.

## Ce que le résumé établit sur des modes d'échec

1. **La surveillance des sorties manque la conscience non verbalisée** : si les modèles agissent sur une conscience
   qu'ils ne disent pas, la surveillance des sorties la manque systématiquement ; la verbalisation est quasi nulle chez
   la plupart des modèles ouverts étudiés sur des scénarios de désalignement d'agent (« Abstract »).
2. **Ce qui la déclenche** : la plausibilité de la tâche plutôt que le réalisme du scénario ; retirer les instructions
   métacognitives du message système l'élimine, même chez des modèles capables (« Abstract »).
3. **Mécanisme sur organisme** : sur un organisme réglé pour se conduire selon l'évaluation, piloter avec une sonde de
   « contexte » implicite augmente la conduite « d'évaluation » sans hausse proportionnelle de la verbalisation ; la
   verbalisation agirait comme un renforcement du changement de conduite (« Abstract »).
4. **Remèdes par pilotage** : sur Kimi-K2.5, parmi neuf stratégies contrastives, une seule des quatre reprises de
   fiches système transfère (« fiction contre réel ») et elle couple conscience et nocivité (« Abstract »).

## Conditions et limites de la lecture

- Résumé seul : aucun chiffre n'est donné, aucun n'est attribué ; méthodes, modèles exacts et contrôles non vérifiés.

## Ce que ça touche chez nous (avis)

- Section 7 (contrôles croisés) et section 11 : la conscience d'évaluation se lit par sonde, jamais par verbalisation ;
  et le message système de nos organismes (consignes métacognitives éventuelles) est une variable à contrôler.

## Phrase citée

« Unverbalized eval awareness, where language models adjust behavior upon detecting evaluation without expressing this
recognition, poses a challenge for AI safety: if models act on awareness they do not verbalize, output monitoring will
systematically miss it. » (« Abstract »)

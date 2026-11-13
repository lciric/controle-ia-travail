# Devis — atelier d'idées sur les bassins étroits et profonds, trois générations — v2

Écrit par le préparateur (Claude Opus 5.5) le 13 novembre 2026 (reprise à 13:57 UTC, `date -u`). **Remplace la v1**
(`1b311242…`, gardée, R12) après la contre-lecture (`3aaf9981…`) : contrôle externe d'Argon relevé de 1,5 à 1,7 (M2), durée et
lancement détaché (M7), réserves m10 et M9. **Aucune dépense engagée par ce devis.** Ligne **GO-2026-11-13-03** (60 USD ; par
course 12 Claude, contrôles compris, + 8 hors Claude ; échéance 2026-11-30). Lanceur `lancer_course_ideation_bassins_etroits_v2.py`.

## 1. Barème et hypothèses (inchangés)

Claude par le relais de clé du noyau, clé lue **par son nom** `RR_ANTHROPIC_API_KEY_RIGAUD` (aucune valeur lue ni écrite) :
Opus 5.5 4 / 20, Fable 5.1 10 / 50 USD par million de jetons (barème du noyau, non revérifié par la contre-lecture). Hors
Claude : Argon par `appel-argon-v5.sh` et `commande_argon_v3d.py`, relais Gemini v2 ; entrée 8,3, sortie 41,5 (SUPPOSÉ) ;
pensée provisionnée 8 192 jetons ; aucune recherche sur le Web. Tailles : mesure sans appel du 13 novembre (`df384741…`).

## 2. Par génération (course + bras)

| Poste | Plafond (pire cas) | Attendu, calcul |
|---|---|---|
| Contrôles Claude (Opus, Fable) | 0,4 | ≈ 0,00 |
| Proposeur Opus 5.5, deux passes | 4,0 | 0,46 |
| Proposeur Fable 5.1, deux passes | 4,0 | 1,16 |
| Juge Opus 5.5 | 1,5 | 0,46 |
| **Part Claude** | **9,9** (total transmis 12,0) | **≈ 2,1** |
| Contrôle d'Argon (consigne de contrôle entière) | **1,7** | 0,89 |
| Argon passe 1 / passe 2 | 1,3 + 1,9 | 0,62 + 0,69 |
| Juge Argon (bras) | 2,5 | 1,16 |
| Contrôle court du bras | 0,6 | 0,04 |
| **Part hors Claude** | **8,0** (l'orchestrateur borne à 8,0) | **≈ 3,4** |
| **Génération** | **17,9** (borne du GO : 20) | **≈ 5,5** |

**Attendu retenu : ≈ 7 USD par génération (5 à 9)** — le calcul sous-estime (pensée d'Argon, fiches plus longues) ; la course
du 8 novembre (huit fiches, sans Fable) a coûté 7,65 USD avant son bras, plus 0,77 pour le bras (R-1862, R-1865).

## 3. Trois générations

| | Attendu | Pire cas par les plafonds | Borne |
|---|---|---|---|
| Générations 1, 2, 3 | ≈ 7 chacune | 17,9 chacune | 20 chacune |
| **Total** | **≈ 21 (16 à 27)** | **53,7** | **60** |

Part Claude au pire 29,7 ; hors Claude au pire 24,0. **Garde de cumul** : dépense relevée de tout ce que le lanceur a joué +
20 (course) ou + 3,1 (bras) ≤ 60 ; toute dépense illisible, tout processus mort sans fin propre, tout dossier de contrôle sans
tentative scellée compte son plafond entier ; seul un refus « rien envoyé » prouvé par le relevé (≤ 10⁻⁵ USD) compte pour
nul et laisse relancer.

## 4. Durée (M7)

- Course : attendu 1 à 2 heures ; borne ≈ 10 heures (une heure au plus par session). **Le lanceur ne la porte plus** : il la
  détache sous un superviseur (session de processus neuve) et rend la main ; la limite de durée de l'outil qui lance (deux
  heures au plus en arrière-plan) n'arrête plus la course. Suivi : la même commande, relancée, dit « en marche » (code 3) ou
  clôt.
- Lecture par la mère et attestation : son temps (36 fiches au plus). Bras : 5 à 30 minutes. Trois générations : 4 à 6
  heures de calcul, un à deux jours écoulés.

## 5. Réserves (m10, M9)

- **Fable 5.1 en proposeur à 2,0 USD par session : aucun précédent mesuré** (la course du 8 novembre s'est faite sans Fable).
  Un refus de la question par un modèle Claude n'apparaîtrait qu'après le contrôle et les deux passes d'Argon (≈ 2 USD) : la
  sonde réelle de la garde refus-question (≈ 0,003 USD, hors de ce lanceur, à part) vaut son prix avant la génération 1.
- **Bras impossible après une course payée** si les fiches font en moyenne plus de ≈ 14 400 caractères (garde du juge à
  600 000 caractères) : le lanceur le refuse avant tout appel du bras (garde du bras), mais la course est déjà payée.
- **Témoins** écrits par le modèle d'un proposeur et d'un juge (Opus 5.5) : un échec chez un juge sain reste possible ; il
  arrête la chaîne après ≈ 7 USD.

## 6. Préalables (aucun n'est payé par ce devis)

Bac à sable : **actif** dans ce conteneur depuis 13:30 UTC (R-2536) ; recoupement scellé et son attestation de relecture ;
relais Claude `--modeles-permis claude-opus-5-5,claude-fable-5-1` à plafond 12 par génération, relais Gemini v2 ; règle de
permission et épingle d'empreinte du lanceur v2 ; vérification courte du v2. La machine jetable de GO-2026-11-13-02 n'est
pas payée par cette ligne.

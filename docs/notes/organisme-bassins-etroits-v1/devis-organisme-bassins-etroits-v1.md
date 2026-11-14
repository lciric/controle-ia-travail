# Devis — atelier d'idées sur les bassins étroits et profonds, trois générations — v1

Écrit par le préparateur (Claude Opus 5.5), sous-agent de la session mère, le 13 novembre 2026 vers 13:28 UTC (`date -u`).
**Aucune dépense engagée par ce devis.** Ligne : **GO-2026-11-13-03** (60 USD ; par course 12 USD Claude, contrôles
compris, + 8 USD hors Claude ; échéance 2026-11-30). Conception : `conception-trois-generations-v1.md` (`4c90a3a5…`).
Lanceur : `scripts/lancer_course_ideation_bassins_etroits_v1.py` (`a10420cc…`).

## 1. Barème et hypothèses

- Claude (barème du noyau, `pole/relais_reel.py`, USD par million de jetons, entrée / sortie) : **Opus 5.5 4 / 20 ;
  Fable 5.1 10 / 50**. Crédits Claude par le relais de clé du noyau, qui lit la clé **par son nom**
  `RR_ANTHROPIC_API_KEY_RIGAUD` (aucune valeur lue, écrite ni transmise ; le lanceur retire tout nom de clé de
  l'environnement de l'orchestrateur).
- Hors Claude : Argon (`gemini-4-argon`) par l'enveloppe `appel-argon-v5.sh` (`37c0205e…`) et `commande_argon_v3d.py`
  (`46c91df4…`), relais Gemini v2 sur la boucle locale, clé tenue par le relais seul ; **entrée 8,3** (borne lue par Lazar)
  / **sortie 41,5** (SUPPOSÉ) ; pensée provisionnée 8 192 jetons ; aucune recherche sur le Web.
- Tailles : mesure sans appel du 13 novembre (`mesurer-consignes-g1-gabarit-40000-v1.json`, `df384741…`) ; pièce variable
  au plafond des générations 2 et 3 (50 000 caractères) : passe 1 ≈ 66 800 caractères, passe 2 ≈ 96 800, contrôle d'Argon
  ≈ 332 900, juge ≈ 264 000 (36 fiches de 5 000 caractères et 4 témoins). Jetons ≈ caractères / 4 ; sortie d'une passe :
  six fiches de 5 000 caractères ≈ 7 500 jetons.

## 2. Par génération (course + bras)

| Poste | Plafond (pire cas) | Attendu, calcul |
|---|---|---|
| Contrôles Claude (Opus, Fable) | 2 × 0,2 = 0,4 | ≈ 0,00 |
| Proposeur Opus 5.5, deux passes | 2 × 2,0 = 4,0 | 0,46 |
| Proposeur Fable 5.1, deux passes | 2 × 2,0 = 4,0 | 1,16 |
| Juge Opus 5.5 | 1,5 | 0,46 |
| **Part Claude** | **9,9** (total transmis 12,0) | **≈ 2,1** |
| Contrôle d'Argon (consigne de contrôle entière) | 1,5 | 0,89 |
| Argon passe 1 / passe 2 | 1,3 + 1,9 | 0,62 + 0,69 |
| Juge Argon (bras) | 2,5 | 1,16 |
| Contrôle court du bras | 0,6 | 0,04 |
| **Part hors Claude** | **7,8** (l'orchestrateur borne à 8,0) | **≈ 3,4** |
| **Génération** | **17,7** (borne du GO : 20) | **≈ 5,5** |

**Attendu retenu : ≈ 7 USD par génération (5 à 9)** : le calcul donne 5,5 ; la course du 8 novembre (huit fiches, sans
Fable) a coûté 7,65 USD avant son bras, plus 0,77 pour le bras (R-1862, R-1865) — le calcul sous-estime (pensée d'Argon, fiches
plus longues).

## 3. Trois générations

| | Attendu | Pire cas par les plafonds | Borne |
|---|---|---|---|
| Génération 1 | ≈ 7 | 17,7 | 20 |
| Génération 2 | ≈ 7 | 17,7 | 20 |
| Génération 3 | ≈ 7 | 17,7 | 20 |
| **Total** | **≈ 21 (16 à 27)** | **53,1** | **60** |

Part Claude au pire 29,7 (attendu ≈ 6 à 9) ; part hors Claude au pire 23,4 (attendu ≈ 10 à 14).
**Garde de cumul du lanceur** : avant chaque course, dépense relevée de tout ce que le lanceur a joué + 20 ≤ 60 ; avant
chaque bras, + 3,1 ≤ 60 ; une dépense illisible compte son plafond entier. Une tentative refusée avant départ ne coûte rien ;
une course arrêtée en route coûte au plus ce qu'elle a engagé, jamais plus que ses plafonds.

## 4. Durée

- Course : contrôles, deux passes d'Argon (≤ 1 500 s chacune), quatre sessions de proposeurs Claude, un juge, en série ;
  attendu **1 à 2 heures**, borne ≈ 10 heures (une heure au plus par session, `--delai-session-s` par défaut).
- Lecture humaine et attestation : temps du lecteur (36 fiches au plus).
- Bras : **5 à 30 minutes**.
- Trois générations : **≈ 4 à 6 heures de calcul**, un à deux jours écoulés avec les lectures.

## 5. Préalables (aucun n'est payé par ce devis)

Bac à sable actif là où la course tourne (absent de ce conteneur, voir le rapport) ; recoupement scellé de la mère ; relais
Claude `--modeles-permis claude-opus-5-5,claude-fable-5-1` à plafond 12 par génération (relancé, ou relu avant chaque
génération) et relais Gemini v2 ; règle de permission et épingle d'empreinte écrites par Lazar ; contre-lecture du lanceur
par un autre modèle. La machine jetable de GO-2026-11-13-02 n'est **pas** payée par cette ligne.

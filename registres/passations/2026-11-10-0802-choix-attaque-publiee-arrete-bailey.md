# Choix de l'attaque publiée à reproduire — arrêté (10 novembre 2026, 08:02 UTC)

Session `session_01QPDgKgcLdggoVJfGC5cBw8` (session-dépôt). Branche `claude/upbeat-cray-dmauvv`. Numéro de registre à
attribuer à la fusion dans `main`.

## Choix

**Bailey et al. (arXiv 2412.09565)** est l'attaque publiée reproduite comme témoin d'ancrage avant l'entretien. Note de
choix scellée : `docs/notes/reproduction-attaque-publiee-v1/choix-et-anteriorite-v1-brouillon3.md` (`e5bab8c3…`).

Motif honnête (le brouillon 1 l'avait faux) : Bailey a un **code public** (`LukeBailey181/obfuscated-activations`,
commit `9c1f4b1a`), un **juge résolu** (StrongREJECT affiné) et un **jeu de données résolu** (800/100/100). On reproduit
l'effet publié **sur le modèle de Bailey (Llama-3.0-8B-Instruct)** pour ancrer le harnais ; le transfert vers notre modèle
de banc (Llama-3.1-8B-Instruct) est une **étape séparée**. Le candidat 2 (arXiv 2609.36490) tourne, lui, sur
`llama-3.1-8b-instruct` — exactement notre banc — mais son code public n'est pas confirmé et sa méthode est un réglage fin
des poids (échelon 5-6, bras déclaré N-053) : gardé comme option de transfert, pas comme ancre.

## Processus suivi (R1, R2)

- Brouillon 1 (`203d32ec`) → contre-lecture v1 (3 bloquants : modèle inversé, document du candidat 2 déclaré absent à tort,
  carte A100 attribuée au papier).
- Brouillon 2 (`54a731b2`) → contre-lecture v2 (`5ea95fa7`) : 0 bloquant, 2 majeurs, 2 mineurs.
- Brouillon 3 (`d0c51e84`, scellé `e5bab8c3…`) → contre-lecture v3 (scellée `da5cc9f3…`) : **scellable en l'état**, 4 points
  corrigés, aucune erreur neuve.
- Fait pivot revérifié par la session elle-même sur source primaire : programme = Llama-3.1-8B-Instruct
  (`programme-controle-ia-v2.md` l. 249) ; Bailey = 3.0.

## Préalables au run (restent)

Aucun run n'est autorisé. Avant tout calcul :
1. **GO renouvelé** : GO-2026-10-31-05 **expire le 14 novembre** — à renouveler (mot de Lazar).
2. **Licence du dépôt Bailey** vérifiée — l'accès GitHub de ce conteneur est limité à notre dépôt ; non vérifiable d'ici
   (nœud pour Lazar).
3. **PDF de StrongREJECT** versé et empreinté (manquant, bloquant pour le préenregistrement).
4. **Devis corrigé** (A100 40 → 80 Go).
5. **Préenregistrement** de la reproduction écrit, contre-lu (R2), scellé — avec la cible chiffrée prise sur une expérience
   dont le chiffre est opposable (boucle itérée §3.5 lue sur figure, ou OAT §6.2 par bascule déclarée), jamais un chiffre
   OAT présenté comme prédiction de la boucle (R1/R7).

## Décision en attente (défaut (a) sous 48 h)

Ancrer le harnais sur Bailey (recommandé (a)) ou sur le candidat 2 (modèle exact, code non confirmé) : nœud ouvert, défaut
(a). Le choix arrêté ci-dessus est (a).

## Instances actives

Aucune de cette session. Aucune dépense engagée.

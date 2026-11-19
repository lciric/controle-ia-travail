# Devis — pilote du papier C (étape 1 du préenregistrement HC1 à HC3) — v1, brouillon 1

Écrit le 2026-11-19 par le rédacteur du préenregistrement (Claude Fable 5.2). Classe A (devis) : à contre-lire par un
autre modèle, à sceller, puis mot du directeur. **Rien n'est lancé ni inscrit par ce document.** Il sert à inscrire la
ligne de type « calcul » que la décision D-18, option (b), demande (GO-2026-11-19-74) : le texte ne nomme aucun
identifiant ; le lanceur reçoit `GO_ID` au lancement et le vérifie par les règles de la garde de calcul.

Texte de référence : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r3.md`
(`160730b4c3980d8d96b0d05ed4041f011b5bf78a7d8dc7f927ee1ed0c2463cac`), Plan d'analyse, section 1 ; à remplacer par le
texte scellé et son empreinte. Aucun prix n'est inventé : un montant qui n'est pas dans une pièce du dépôt porte
« À REMPLIR », avec l'endroit où le lire.

## 1. Ce qui tourne

Le pilote ne mesure que des propriétés de dessin (lisibilité des consignes, gains des formulations du vivier sans
destination) ; il ne décide d'aucune hypothèse. Trois juges lisent des contenus ; aucun agent ne génère, aucune sonde
n'est lue.

| point du texte | ce qui est lu | lectures (une lecture = un juge, un contenu, une condition) |
|---|---|---|
| 1.0 | sur processeur, avant toute carte : essais du module, banc de reproduction | aucune dépense |
| 1.1 | empreintes ; règle du jeton en contexte, par juge × consigne × variante | négligeable |
| 1.2 banc sur carte | 30 items × 3 conditions × 3 juges, par réponse imposée essayée | 270 par réponse imposée |
| 1.3 lisibilité des consignes | 20 contenus × 3 juges × (consignes A et B : 1 + 15 formulations + 2 témoins ; alarme : 1 + 4 + 2), par variante essayée | 2 580 par variante |
| 1.4 vivier | n_cal contenus (60 au plus) × (1 + 80 formulations + 16 témoins + constat nu) × 3 juges, consigne A, mode direct | 17 640 au plus |
| 1.5 mode raisonné | 10 contenus × (1 + 5) × 3 juges, 384 jetons générés au plus par lecture | 180 |

Juges : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct-v0.3, révisions figées au scellement. Les
lectures en mode direct sont une passe avant sans génération ; seules les 180 lectures du point 1.5 génèrent.
Nombre de lancements : un ; un second seulement si le premier est perdu par l'hôte ou arrêté par une garde avant la
fin, dans le cumul de 4 heures.

## 2. Machine

| élément | valeur | source |
|---|---|---|
| carte | 1 × A100 80 Go (instance de référence de la phase 0) | `livrables/premier-rendu-v1/devis-v1.md` (`16d71feb…`), ligne « Instance de référence » |
| loueur | Vast.ai | `CLAUDE.md`, routine de reprise ; `registres/depenses.md` |
| offre exacte (identifiant, hôte, disque, débit) | À REMPLIR au jour du lancement | recherche d'offres par le lanceur ; consignée dans `registres/depenses.md` |
| disque et descente des trois modèles | À REMPLIR | taille des trois modèles aux révisions figées ; prix du réseau et du stockage de l'offre |

## 3. Durée et prix

| poste | valeur | source |
|---|---|---|
| heures de carte, borne | **4 heures au plus, en cumul** | `registres/go.md`, GO-2026-10-17-01 ; texte, Plan, section 1 |
| heures de carte, attendu | À REMPLIR | débit mesuré de lectures de juges sur A100 (traces de P3 ou des notations de T0.5, citées par `registres/depenses.md`) ; non lu par ce rédacteur ; à défaut, la borne |
| prix unitaire, indicatif | 0,80 à 1,30 USD/h (central 1,00) | devis de la phase 0 (`16d71feb…`), ligne « Instance de référence » |
| prix unitaire, relevés récents | 1,1833 USD/h (2026-11-18, instance 61276240, A100 SXM4 80 Go) ; 1,22 USD/h stockage compris (2026-11-19, instance 61414494) | `registres/depenses.md`, lignes de ces dates |
| prix unitaire du lancement | À REMPLIR : prix relu de l'offre après création | lanceur ; `registres/depenses.md` |
| montant de l'accord | 4 heures de carte, « ≈ 6 USD » | `registres/go.md`, GO-2026-10-17-01 |
| borne par lancement | **10 USD au plus** ; le lanceur borne strictement sous 10 USD | `registres/go.md`, GO-2026-10-20-07 ; texte, Plan, section 1 |
| pire cas | 4 h × prix relu ; au plafond de prix du § 4, soit 4 × 1,50 = 6,00 USD, plus réseau et stockage (À REMPLIR) | calcul sur les bornes ci-dessus |

## 4. Plafond et bornes à inscrire

Recopiés du registre, sans changement : GO-2026-10-17-01 (4 heures de carte, ≈ 6 USD, dans les 150 USD de
GO-2026-10-04-08 ; chaque lancement soumis à l'accord de Lazar) et la délégation GO-2026-10-20-07 (10 USD au plus par
lancement, préenregistré, scellé et contre-lu), **prolongés jusqu'au 2026-12-31, plafond inchangé** (décision D-4,
option (a), GO-2026-11-19-53, ligne de type « décision »).

Ligne de type « calcul » proposée : « pilote du papier C (étape 1 du préenregistrement scellé) : 4 heures de carte
au plus en cumul, 10 USD au plus par lancement, échéance 2026-12-31 ».

Trois points que le registre ne tranche pas, à remplir avec le mot du directeur :
- **Enveloppe.** GO-2026-10-17-01 place le pilote « dans les 150 USD de GO-2026-10-04-08 », dont l'échéance est le
  2026-11-30 (GO-2026-10-20-06) ; la prolongation de D-4 ne nomme pas cette enveloppe. Plafond de la ligne neuve :
  À REMPLIR (dans cette enveloppe prolongée, ou plafond propre).
- **Cumul déjà consommé de l'enveloppe** : À REMPLIR, à lire dans `registres/depenses.md` (lignes sous
  GO-2026-10-04-08).
- **Plafond de prix horaire de l'offre** : À REMPLIR. Valeur implicite de l'accord : 6 USD / 4 h = 1,50 USD/h ; les
  relevés récents sont en dessous.

## 5. Ce qui arrête la dépense

- Avant toute carte : essais du module et banc de reproduction sur processeur ; échec : arrêt, aucune location.
- Préalables (liste d'arrêt 2 du texte) : texte scellé et contre-lu, verdict complété de P3, addendum de lancement
  scellé (adaptateur réel, décision D-20), ligne de type « calcul » valide au jour du lancement, ligne d'accord du
  jour ; l'un manque : arrêt avant la création de l'instance.
- Borne du lanceur : durée = min(4 heures moins les heures déjà consommées, 10 USD / prix horaire de l'offre),
  strictement sous 10 USD ; à la borne et à la fin, l'instance s'arrête par son identifiant (R10), consigné dans
  `registres/arrets.md`.
- Prix relu après création au-dessus du plafond de prix : destruction aussitôt, par l'identifiant.
- Toute garde de la liste d'arrêt du texte qui dit « arrêt » ou « nœud » (empreinte non conforme, lisibilité en
  échec pour un juge, fuite de la cible) : arrêt du run, instance arrêtée.
- Récupération avant destruction (consigne du programme) : inventaire des sorties (noms, tailles, empreintes),
  versement scellé, puis seulement destruction.

## 6. Hors devis

- L'étape 2 (décisive : TC.1 à TC.3), qui demande un devis et un accord à part, après la porte G0.
- Le bras « contrôlabilité » et son banc ; les lectures de sondes ; toute génération par l'agent.
- La grille de la clause de repli, les essais du module, la dérivation : sur processeur, sans dépense.
- Un rejeu du pilote au-delà du cumul de 4 heures, ou un second lancement hors des deux cas du § 1 : nœud.
- Tout appel à un modèle par une interface payante : il n'y en a aucun dans le pilote.

## 7. Avant le lancement

1. Contre-lecture de ce devis par un autre modèle, corrections, scellement.
2. Mot du directeur ; inscription de la ligne de type « calcul » dans `registres/go.md`.
3. Scellement du préenregistrement, de la configuration, du module ; addendum de lancement scellé.
4. Contrôle du crédit du loueur ; création par identifiant avec `GO_ID`.

## 8. Non vérifié par ce rédacteur

Le débit des lectures et la taille des modèles (d'où la durée attendue et le réseau) ; le cumul de l'enveloppe ; le
nombre de variantes et de réponses imposées de la configuration (les décomptes du § 1 sont par variante essayée).

# Complément de passation du compte organisme — Astra et Carbon déclarés, commandes neuves prêtes — 2026-11-18T11:08:16Z (`date -u`)

Complète `registres-provisoires/passation-compte-organisme-2026-11-18-1047-autre-compte.md` (point 4 : le correctif « Astra et Carbon » est **fait**). À lire par la mère neuve et par la session neuve du compte organisme. Fondement : mot de Lazar tapé dans la session sortante vers 10:50Z, verbatim : « je veux astra et carbon dans la course debugge » ; noté par la mère sortante (`registres/passations/2026-11-18-1045-complement-2-v1.md`, `main` `5125fd2e`).

## Fait
- Correctif versé (`9ce08a73`) par un développeur unique (modèle I) ; **contre-lecture par Sonnet (modèle K) : « Conforme. »** (`docs/notes/organisme-auto-conception-v1/course-v2/contre-lecture-correctif-astra-carbon-v2b-v6b.md`, `895a52838173587c9cb9e9fc2eb456d3c8809e4e1293e3b0ff016fdcb2d077c0`, commit `f67122c1`). 238 essais passés.
- **Défaut corrigé** : la sonde d'Astra par relais jeté plafonné à 0,05 USD partait sans `--reserve-par-appel` (réserve 0,40 → 402), et la commande d'Astra refusait au code 4 sous ce plafond avec ses sorties par défaut. Réglages qui passent : relais jeté port 8793 `--plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1` ; commande `PLAFOND_SESSION_USD=0.05 --max-sortie-jetons 4096 --sortie-min-jetons 16` (sortie réduite à 768 jetons) ; pire cas 0,04998 USD.
- **Lanceurs scellés inchangés** : auto-conception `scripts/lancer_course_auto_conception_v2.py` (`d8fbb42aca76a870b36094b43a696e10ffce1b176837af55e326373ef587c5ed`) ; affinage `scripts/lancer_course_affinage_mentors_v6.py` (`bf2abdc6cff49156296d713bbcccaf3a4d07a86344cc95f6f60223ab7287dff0`). Tous deux acceptent Astra et Carbon déclarés et les refusent sans sonde ou sans mot.

## Empreintes à employer (branche `lot/compte-organisme-v1`, commit `f67122c1` ou plus récent)
| pièce | sha256 |
|---|---|
| sonde commune `scripts/sonde_astra_courses_v1.py` | `d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777` |
| **auto-conception** : commandes exactes `docs/notes/organisme-auto-conception-v1/course-v2/commandes-exactes-course-auto-conception-v2b.md` | `ed4bf5e6d4a6e29cf7807de2b79fb4a54c55761c3d9e1f89b6179db5027ccf08` |
| auto-conception : gabarit de pièce de départ `…/course-v2/piece-de-depart-gabarit-auto-conception-v2b.json` | `21ad19fee6df9d12607698a8ddefa4292ecbd080acac3c7a4d8e6480b15406b2` |
| auto-conception : devis `docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v2b.md` | `b2319472cbad20d87664b63edcdab47914de1d81135841b81f10954f6f45da0e` |
| **affinage** : commandes exactes `docs/notes/organisme-affinage-mentors-v1/course-v6/commandes-exactes-course-affinage-v6b.md` | `1fce4cea96f9d86ee700d742d5020c5b4378d341b42c2b0ed9c4a2591fa52fef` |
| affinage : gabarit de déclaration des relais `…/course-v6/declaration-relais-gabarit-course-affinage-v6b.json` | `875f438f2da8dde0c20c13281f775906cd51019aec68aa338e85b2e86d9356f2` |
| affinage : devis `docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v6b.md` | `2326666d11529c59799205de6014ca94bdc8c9b0ac0d1139eacb281579ebb129` |

## Consignes d'exécution (constats mineurs de la contre-lecture, sans changement de code)
1. **Auto-conception** : la sonde d'Astra n'est pas lue par le lanceur v2 : la mère vérifie à la main le rapport scellé de la sonde (du jour, « ok », empreinte) avant d'écrire `sonde_du_jour` dans la pièce de départ (commandes v2b, § 2 et § 6). Le champ `statut` de la pièce est à réécrire.
2. **Auto-conception** : si la clé de Carbon est celle d'Argon (`GEMINI_API_KEY`), confronter à la main **90 + 33 = 123 USD** au crédit de cette clé (aucun programme ne fait la somme ; devis v2b).
3. **Affinage (commandes v6b)** : les deux courses partagent les ports des relais : **elles ne tournent jamais en même temps**.
4. **Affinage (commandes v6b, § 1 bis)** : faire `git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main` avant les essais ; sinon les essais neufs se sautent en silence si une commande manque de `main` (144 attendus).
5. Une sonde de 768 jetons ne prouve pas le comportement d'Astra à l'échelle de la course : risque accepté par le mot de Lazar ; une troncature à la sonde se lit « non réussie », Astra non déclarée, tentative non brûlée.
6. Kimi non déclaré, et `compter_limite_de_debit_comme_soupcon` = faux, dans l'affinage (R-3279) ; Kimi non déclaré dans l'auto-conception (R-3273).

## Ordre
Auto-conception d'abord (GO-2026-11-18-20 et -21), selon les commandes v2b ; l'affinage reste à contre-lire en entier (v6, `99797a9b`) avant ses commandes v6b.

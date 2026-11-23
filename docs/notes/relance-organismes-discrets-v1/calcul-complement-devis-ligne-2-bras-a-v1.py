# Organismes discrets, bras A — calcul du complément au devis de la seconde ligne de carte louée — v1.
# Rejoue la formule de la section 5.2 du devis de la carte v5 (devis-bras-a-v5.md, 40b999f8…) sur ce que
# la première ligne a mesuré : secondes par épisode (d), heures de mise en route (m), plafond recalculé (P2).
# Entrées : le manifeste de la première ligne (clés « resume », « ligne » et « arret » seulement) et le constat des tarifs, chacun
# vérifié par son empreinte avant lecture ; aucun épisode, aucune transcription. Bibliothèque standard seulement.
# Sortie sans date ni chemin absolu : rejouée, elle doit rendre les mêmes octets.
# Usage : python3 calcul-complement-devis-ligne-2-bras-a-v1.py [RACINE_DU_DEPOT]
import hashlib
import json
import math
import sys
from datetime import datetime, timedelta
from pathlib import Path

RACINE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[3]
DOSSIER = "diag/organismes-discrets-v-a-v2/ligne-1-fini-20261123T061257Z"
ENTREES = {  # chemin relatif, empreinte attendue (recalculée par le rédacteur le 2026-11-23)
    "manifeste": (f"{DOSSIER}/manifeste-de-la-ligne-1.json",
                  "92a72200f120d45666c11a1f4598e638d70ead0a07d5b741c79ede073fa7727b"),
    "constat": (f"{DOSSIER}/constat-ligne-1.json",
                "9b77f9a203e0580f33a4d59592c400d6bd211816d673f91c1d72f20f4a76a2bd"),
}

# Constantes du devis v5, sections 3.2, 5.1 et 5.2 (aucune n'est changée ici).
EPISODES_L2 = 896                     # 7 conditions x 128 épisodes
PAS, PAS_DOUBLE_S = 2304, 6.0         # 6 adaptateurs x 384 pas de distillation ; 3,0 s supposé, doublé
PASSES, PASSE_DOUBLE_S = 1280, 0.90   # 5 x 128 x 2 passes de la prise ; 0,45 s d'une autre chaîne, doublé
IDENTITE_H = 6 * 3 / 60               # contrôle d'identité : 6 x 3 minutes
PLANCHER_M_H = 1.0                    # la mise en route mesurée ne remplace l'heure supposée que si elle est plus longue
CARTE, STOCKAGE, TELECH_GO = 1.30, 0.08, 0.05   # prix du devis (bornes)
PRIX_H = CARTE + STOCKAGE             # 1,38 USD par heure
TELECH_USD = 4.0                      # deux mises en route x 40 Go x 0,05 USD
REPLI_H_HAUT = 1.0 + PAS * 3.0 / 3600 + IDENTITE_H + EPISODES_L2 * 42.8 / 3600 + PASSES * 0.45 / 3600

# Hors du manifeste : les deux instances de la première ligne perdues sur panne technique avant la bonne.
# Source : registres de la branche principale (origin/main, commit 52c5072d) — arrêts, lignes 158, 159 et 163 ;
# dépenses, lignes 614, 618 et 625. 62082700 : 02:48:26Z -> 02:52:20Z ; 62094921 : 04:23:54Z -> « ≈ 04:30Z » (majorant).
PANNES_S = (234.0, 366.0)
PREMIERE_CREATION_UTC = "2026-11-23T02:48:26Z"


def refus(message):
    sys.exit("REFUS : " + message)


def lire(nom):
    rel, attendue = ENTREES[nom]
    chemin = RACINE / rel
    if not chemin.is_file():
        refus(f"{rel} absent sur disque")
    obtenue = hashlib.sha256(chemin.read_bytes()).hexdigest()
    if obtenue != attendue:
        refus(f"{rel} : empreinte {obtenue} au lieu de {attendue}")
    return json.loads(chemin.read_text(encoding="utf-8"))


def instant(texte):
    return datetime.strptime(texte, "%Y-%m-%dT%H:%M:%SZ")


def h2(d, m):
    return (max(PLANCHER_M_H, m) + IDENTITE_H + PAS * PAS_DOUBLE_S / 3600
            + PASSES * PASSE_DOUBLE_S / 3600 + EPISODES_L2 * d / 3600)


def p2(d, m):
    return 2 * PRIX_H * h2(d, m) + TELECH_USD


manifeste, constat = lire("manifeste"), lire("constat")
r, tarifs = manifeste["resume"], constat["tarifs"]
compteur = r["compteur"]

# Gardes : aucune valeur n'est employée si les pièces ne se recoupent pas.
if manifeste["ligne"] != 1 or manifeste["arret"] is not None:
    refus("le manifeste n'est pas celui d'une première ligne finie sans arrêt")
if r["episodes"] != 128:
    refus(f"{r['episodes']} épisodes au lieu de 128")
if abs(r["secondes_par_episode"] - r["duree_s"] / r["episodes"]) > 1e-9:
    refus("secondes_par_episode différent de duree_s / episodes")
facture_s = (compteur["cumul_usd_a_la_fin"] - compteur["frais_fixes_usd"]) / compteur["taux_usd_h"] * 3600
if abs(facture_s - (r["mise_en_route_s"] + r["duree_s"])) > 1.0:
    refus("le compteur ne recoupe pas mise en route + jeu à une seconde près")
if abs(compteur["taux_usd_h"] - (tarifs["carte_usd_h"] + tarifs["stockage_usd_h"])) > 1e-9:
    refus("taux du compteur différent de carte + stockage du constat")
if abs(compteur["frais_fixes_usd"] - 40 * tarifs["telechargement_usd_go"]) > 1e-9:
    refus("frais fixes différents de 40 Go au tarif de téléchargement du constat")

# d, secondes par épisode.
d_lettre = r["secondes_par_episode"]
d_generation = r["chrono"]["generation_s"] / r["episodes"]
# m, heures de mise en route.
depart_du_jeu = instant(r["creation_instance_utc"]) + timedelta(seconds=r["mise_en_route_s"])
m_lettre = r["mise_en_route_s"] / 3600
m_prudent = (r["mise_en_route_s"] + sum(PANNES_S)) / 3600
m_horloge = (depart_du_jeu - instant(PREMIERE_CREATION_UTC)).total_seconds() / 3600

print("Entrées (empreintes vérifiées avant lecture)")
for nom in ("manifeste", "constat"):
    print(f"  {ENTREES[nom][0]}  {ENTREES[nom][1]}")
print(f"Première ligne : {r['episodes']} épisodes, jeu {r['duree_s']:.4f} s, génération seule {r['chrono']['generation_s']:.4f} s, "
      f"mise en route {r['mise_en_route_s']:.4f} s depuis la création de l'instance ({r['creation_instance_utc']})")
print(f"Compteur : cumul {compteur['cumul_usd_a_la_fin']:.4f} USD, frais fixes {compteur['frais_fixes_usd']:.4f} USD, "
      f"taux {compteur['taux_usd_h']:.4f} USD/h -> {facture_s:.2f} s facturées = {facture_s / 3600:.4f} h "
      f"(mise en route + jeu : {r['mise_en_route_s'] + r['duree_s']:.2f} s)")
print(f"d retenu (secondes_par_episode = duree_s / episodes) : {d_lettre:.4f} s")
print(f"d, génération seule (non retenu, moins prudent) : {d_generation:.4f} s")
print(f"m, valeur du manifeste (création de l'instance -> départ du jeu) : {m_lettre * 3600:.1f} s = {m_lettre:.4f} h")
print(f"m, prudent et retenu (avec les deux instances perdues sur panne, {PANNES_S[0]:.0f} s et {PANNES_S[1]:.0f} s) : "
      f"{m_prudent * 3600:.1f} s = {m_prudent:.4f} h")
print(f"m, temps d'horloge de la première création au départ du jeu (non retenu : pas du temps de carte) : "
      f"{m_horloge * 3600:.1f} s = {m_horloge:.4f} h")
print("Formule (devis v5, 5.2) : H2 = max(1,0 ; m) + 0,30 + 2 304 x 6,0 / 3 600 + 1 280 x 0,90 / 3 600 + 896 x d / 3 600 ; "
      "P2 = 2 x 1,38 x H2 + 4, arrondi à l'unité supérieure")
constante = IDENTITE_H + PAS * PAS_DOUBLE_S / 3600 + PASSES * PASSE_DOUBLE_S / 3600
print(f"  constante {constante:.4f} h ; coefficient {EPISODES_L2 / 3600:.6f} h par seconde d'épisode ; "
      f"rejeu {EPISODES_L2 * d_lettre / 3600:.4f} h")
for nom_d, d in (("d retenu", d_lettre), ("d génération seule", d_generation)):
    for nom_m, m in (("m manifeste", m_lettre), ("m prudent", m_prudent), ("m horloge", m_horloge)):
        print(f"  {nom_d} ({d:.4f} s), {nom_m} ({m:.4f} h) : H2 = {h2(d, m):.4f} h ; "
              f"P2 = {p2(d, m):.4f} -> {math.ceil(p2(d, m))} USD")
P2 = math.ceil(p2(d_lettre, m_prudent))
print(f"PLAFOND RECALCULÉ P2 = {P2} USD (d retenu, m prudent ; le même avec m du manifeste)")


def borne(usd):
    """Secondes par épisode pour lesquelles le plafond non arrondi vaut usd, à m <= 1,0 h."""
    return ((usd - TELECH_USD) / (2 * PRIX_H) - PLANCHER_M_H - constante) / (EPISODES_L2 / 3600)


print(f"  P2 vaut {P2} USD pour d de {borne(P2 - 1):.2f} s (exclu) à {borne(P2):.2f} s (m <= 1,0 h) ; "
      f"{2 * PRIX_H * EPISODES_L2 / 3600:.4f} USD de plafond par seconde d'épisode")
pire = REPLI_H_HAUT * 4 * PRIX_H + TELECH_USD
repli = 5 * math.ceil(pire / 5)
print(f"Plafond de repli, si rien n'était mesuré : {REPLI_H_HAUT:.4f} h x 4 x 1,38 + 4 = {pire:.4f} -> {repli} USD "
      f"(arrondi aux 5 USD supérieurs) ; sans objet ici, d est mesuré")
print(f"Seuil du nœud : P2 = {repli} USD pour d = {borne(repli):.2f} s (m <= 1,0 h) ; "
      f"d mesuré = {100 * d_lettre / borne(repli):.1f} % du seuil -> recalcul, non nœud")
print(f"Tarifs relevés le {tarifs['date_utc']} (constat de la première ligne ; à relever de nouveau le jour de la demande)")
for nom, valeur, borne_devis, unite in (("carte", tarifs["carte_usd_h"], CARTE, "USD/h"),
                                        ("stockage", tarifs["stockage_usd_h"], STOCKAGE, "USD/h"),
                                        ("téléchargement", tarifs["telechargement_usd_go"], TELECH_GO, "USD/Go")):
    print(f"  {nom} : {valeur:.4f} {unite} ; prix du devis {borne_devis:.2f} ; "
          f"{'au plus égal au devis' if valeur <= borne_devis else 'AU-DESSUS DU DEVIS'}")
print(f"  carte {r['determinisme']['carte']} ; pilote de l'hôte {r['determinisme']['pilote']} (manifeste, resume.determinisme)")
# Information hors des six points du complément, non portée au brouillon : marge du plafond sans relance.
d_sans_relance = ((P2 - TELECH_USD / 2) / PRIX_H - PLANCHER_M_H - constante) / (EPISODES_L2 / 3600)
print(f"Information, hors du complément : sans relance, au prix du devis, {P2} USD couvrent la ligne jusqu'à "
      f"{d_sans_relance:.1f} s par épisode, soit {d_sans_relance / d_lettre:.2f} fois la durée mesurée sans adaptateur")

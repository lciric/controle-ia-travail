"""Gardien de l'essai court de mesure du palier 0b — v1.

Lancé détaché (demarrer-gardien-essai-court-v1.sh). Une ligne par intervalle (valeur d'emploi : 60 s) dans
DOSSIER_DE_TENUE/journal-de-tenue-essai-court.txt : heure, identifiant de démarrage, processus vivant ou absent (par
/proc/PID), étape en cours, étapes dont le manifeste existe, présence d'un fichier d'arrêt du programme, n (dossiers de source
présents sous etape-4/couche-mecanique/bras-1-a-3/ à la profondeur proposeur/dose/source, sur 648), octets occupés par le
dossier des sorties (apparents et alloués), octets libres du système de fichiers.

Il ne lit aucun contenu des sorties pour décider : noms, tailles, heures de fichiers seulement. Seule exception, voulue par le
complément 1 v3 : l'inventaire d'une étape close (dès que son manifeste et son compagnon existent) porte les empreintes de ses
fichiers, donc les octets en sont hachés, sans être interprétés. Il ne supprime rien.

Il arrête le programme, et seulement lui, par l'identifiant de son groupe écrit au départ (pgid-essai-court.txt), après
contrôle de l'identité (processus vivant, même démarrage, même heure de départ qu'à la prise de garde, chef du groupe écrit) :
signal de fin au groupe, puis signal d'arrêt forcé au groupe après le délai (valeur d'emploi : 60 s) si le processus vit
encore ; dans deux cas seulement, écrits dans arret-gardien.txt avec la raison et l'heure :
  - arrêt de place : octets libres sous le seuil (valeur d'emploi : 8 000 000 000 octets) ;
  - arrêt de mesure : le manifeste de l'étape 3 existe, et n atteint le seuil (13), ou l'étape 4 dure depuis plus de la durée
    (45 min, comptée depuis t3) — la première des deux. Il écrit alors mesure-essai-court.txt (t3, heure de l'arrêt, n, s4 et
    les deux projections du complément, n >= 2 exigé, sinon « projection impossible »).
Il s'arrête lui-même quand le programme est absent, après une dernière ligne.
"""
import argparse
import datetime
import hashlib
import os
import signal
import sys
import time

TOTAL_SOURCES = 648
SORTIES_EMPLOI = "/home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1"
TENUE_EMPLOI = "/home/user/journaux-palier-0b-essai-court-v1/"
SOUS_DOSSIER_SOURCES = ("etape-4", "couche-mecanique", "bras-1-a-3")
ETAPES = ("3", "4", "5", "6")


def heure(t=None):
    t = time.time() if t is None else t
    return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def lire_valeur(chemin):
    with open(chemin, encoding="ascii") as fh:
        return fh.read().strip()


def boot_id():
    return lire_valeur("/proc/sys/kernel/random/boot_id")


def stat_processus(pid):
    """État, parent, groupe, heure de départ (en tops depuis le démarrage) lus dans /proc/PID/stat ; None si absent."""
    try:
        with open(f"/proc/{pid}/stat", encoding="ascii", errors="replace") as fh:
            s = fh.read()
    except (FileNotFoundError, ProcessLookupError):
        return None
    champs = s[s.rindex(")") + 2:].split()
    # champs[0] = état (3e champ), [1] = parent, [2] = groupe, [19] = heure de départ (22e champ)
    return {"etat": champs[0], "parent": int(champs[1]), "groupe": int(champs[2]), "depart": int(champs[19])}


def taille_arbre(chemin):
    """(octets apparents, octets alloués, nombre de fichiers) d'un arbre, par lstat seulement ; (0, 0, 0) si absent."""
    apparents = alloues = fichiers = 0
    if not os.path.lexists(chemin):
        return 0, 0, 0
    pile = [chemin]
    while pile:
        c = pile.pop()
        try:
            st = os.lstat(c)
        except FileNotFoundError:
            continue
        apparents += st.st_size
        alloues += st.st_blocks * 512
        if os.path.isdir(c) and not os.path.islink(c):
            try:
                with os.scandir(c) as it:
                    for e in it:
                        pile.append(e.path)
            except FileNotFoundError:
                continue
        else:
            fichiers += 1
    return apparents, alloues, fichiers


def sous_dossiers(chemin):
    try:
        with os.scandir(chemin) as it:
            return sorted(e.path for e in it if e.is_dir(follow_symlinks=False))
    except (FileNotFoundError, NotADirectoryError):
        return []


def compter_sources(sorties):
    """n : dossiers présents à la profondeur proposeur/dose/source sous etape-4/couche-mecanique/bras-1-a-3/."""
    base = os.path.join(sorties, *SOUS_DOSSIER_SOURCES)
    n = 0
    for proposeur in sous_dossiers(base):
        for dose in sous_dossiers(proposeur):
            n += len(sous_dossiers(dose))
    return n


def octets_libres(chemin):
    """Octets libres (disponibles hors réserve) du système de fichiers qui porte `chemin` ou son plus proche parent présent."""
    c = os.path.abspath(chemin)
    while not os.path.exists(c):
        c = os.path.dirname(c)
    st = os.statvfs(c)
    return st.f_bavail * st.f_frsize, c


def manifeste(sorties, etape):
    return os.path.join(sorties, f"etape-{etape}", "manifeste.json")


def projection(t3, t_arret, n, s4, total=TOTAL_SOURCES):
    """Les deux projections du complément 1 v3 : durée (t_arrêt − t3) × total / (n − 1) ; place s4 × total / (n − 1).
    None si n < 2 (projection impossible)."""
    if n < 2:
        return None
    return {"duree_s": (t_arret - t3) * total / (n - 1), "place_octets": s4 * total / (n - 1)}


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def ecrire_compagnon(chemin):
    sha = sha256_fichier(chemin)
    with open(chemin + ".sha256", "x", encoding="ascii") as fh:
        fh.write(f"{sha}  {os.path.basename(chemin)}\n")
        fh.flush()
        os.fsync(fh.fileno())
    return sha


class Gardien:
    def __init__(self, a):
        self.a = a
        self.tenue = a.tenue
        self.sorties = a.sorties
        self.journal = os.path.join(self.tenue, "journal-de-tenue-essai-court.txt")
        self.f_arret = os.path.join(self.tenue, "arret-gardien.txt")
        self.f_mesure = os.path.join(self.tenue, "mesure-essai-court.txt")
        self.pid = int(lire_valeur(os.path.join(self.tenue, "pid-essai-court.txt")))
        pg = lire_valeur(os.path.join(self.tenue, "pgid-essai-court.txt"))
        self.pgid = int(pg) if pg.isdigit() else None
        self.boot_ecrit = lire_valeur(os.path.join(self.tenue, "boot-id-essai-court.txt"))
        self.arret_fait = None
        s = stat_processus(self.pid)
        # heure de départ du processus prise à la prise de garde : garde contre un identifiant repris par un autre processus
        self.depart = s["depart"] if (s is not None and boot_id() == self.boot_ecrit) else None
        self.ecrire(f"prise de garde : processus {self.pid}, groupe {pg}, démarrage écrit {self.boot_ecrit}, "
                    f"heure de départ du processus (tops) {self.depart}, sorties {self.sorties}, "
                    f"seuil de place {a.seuil_libre_octets} o, seuil n {a.seuil_n}, durée de l'étape 4 {a.duree_etape_4_s} s, "
                    f"intervalle {a.intervalle_s} s, délai d'arrêt forcé {a.delai_force_s} s, total {a.total}, "
                    f"gardien processus {os.getpid()}")

    # -- écriture
    def ecrire(self, texte, fichier=None):
        with open(fichier or self.journal, "a", encoding="utf-8") as fh:
            fh.write(texte + "\n")
            fh.flush()
            os.fsync(fh.fileno())

    def ligne(self, champs):
        self.ecrire(" ; ".join(f"{k}={v}" for k, v in champs))

    # -- identité
    def vivant(self):
        if boot_id() != self.boot_ecrit or self.depart is None:
            return False
        s = stat_processus(self.pid)
        return s is not None and s["etat"] != "Z" and s["depart"] == self.depart

    def identite_confirmee(self):
        s = stat_processus(self.pid)
        if self.pgid is None:
            return False, "groupe inconnu au départ"
        if not self.vivant():
            return False, "processus absent (ou autre démarrage, ou identifiant repris)"
        if s["groupe"] != self.pgid:
            return False, f"groupe lu {s['groupe']} différent du groupe écrit {self.pgid}"
        return True, "processus vivant, même démarrage, même heure de départ, chef du groupe écrit"

    # -- relevés (noms, tailles, heures seulement)
    def releve(self):
        t = time.time()
        vivant = self.vivant()
        closes = [e for e in ETAPES if os.path.exists(manifeste(self.sorties, e))]
        presentes = [e for e in ETAPES if os.path.isdir(os.path.join(self.sorties, f"etape-{e}"))]
        en_cours = [e for e in presentes if e not in closes]
        arrets = [e for e in ETAPES if os.path.lexists(os.path.join(self.sorties, f"etape-{e}", "arret.txt"))]
        n = compter_sources(self.sorties)
        app, alloc, nf = taille_arbre(self.sorties)
        libres, fs = octets_libres(self.sorties)
        return {"t": t, "vivant": vivant, "closes": closes, "en_cours": en_cours, "arrets": arrets, "n": n,
                "apparents": app, "alloues": alloc, "fichiers": nf, "libres": libres, "fs": fs}

    def ecrire_ligne(self, r, note=None):
        champs = [("heure", heure(r["t"])), ("demarrage", boot_id()),
                  ("processus", f"{self.pid}:{'vivant' if r['vivant'] else 'absent'}"),
                  ("etape_en_cours", ",".join(r["en_cours"]) or "aucune"),
                  ("manifestes", ",".join(r["closes"]) or "aucun"),
                  ("arret_du_programme", ",".join(r["arrets"]) or "aucun"),
                  ("n", f"{r['n']}/{self.a.total}"),
                  ("occupes_apparents", r["apparents"]), ("occupes_alloues", r["alloues"]), ("fichiers", r["fichiers"]),
                  ("libres", r["libres"])]
        if note:
            champs.append(("note", note))
        self.ligne(champs)

    # -- inventaires des étapes closes
    def inventaires(self):
        for e in ETAPES:
            m = manifeste(self.sorties, e)
            if not (os.path.isfile(m) and os.path.isfile(m + ".sha256")):
                continue
            inv = os.path.join(self.tenue, f"inventaire-etape-{e}-essai-court.txt")
            if os.path.lexists(inv):
                continue
            racine = os.path.join(self.sorties, f"etape-{e}")
            entrees = []
            for d, sd, fs in os.walk(racine):
                sd.sort()
                for f in sorted(fs):
                    c = os.path.join(d, f)
                    entrees.append((os.path.relpath(c, self.sorties), os.lstat(c).st_size, sha256_fichier(c)))
            entrees.sort()
            with open(inv, "x", encoding="utf-8") as fh:
                fh.write(f"# inventaire de l'étape {e} de {self.sorties}, écrit le {heure()} : empreinte sha256, taille "
                         f"(octets), chemin relatif au dossier des sorties ; {len(entrees)} fichiers\n")
                for chemin, taille, sha in entrees:
                    fh.write(f"{sha}  {taille}  {chemin}\n")
                fh.flush()
                os.fsync(fh.fileno())
            sha = ecrire_compagnon(inv)
            self.ecrire(f"{heure()} : inventaire de l'étape {e} écrit : {inv} ({len(entrees)} fichiers), sha256 {sha}, "
                        f"compagnon {inv}.sha256")

    # -- arrêt
    def arreter(self, raison, details):
        self.arret_fait = raison
        self.ecrire(f"raison : {raison}\nheure : {heure()}\n{details}", self.f_arret)
        ok, pourquoi = self.identite_confirmee()
        if not ok:
            self.ecrire(f"{heure()} : aucun signal envoyé : identité non confirmée ({pourquoi})", self.f_arret)
            return
        os.killpg(self.pgid, signal.SIGTERM)
        self.ecrire(f"{heure()} : signal de fin envoyé au groupe {self.pgid} ({pourquoi})", self.f_arret)
        fin = time.monotonic() + self.a.delai_force_s
        while time.monotonic() < fin and self.vivant():
            time.sleep(min(1.0, max(0.05, fin - time.monotonic())))
        if not self.vivant():
            self.ecrire(f"{heure()} : processus {self.pid} absent après le signal de fin", self.f_arret)
            return
        ok, pourquoi = self.identite_confirmee()
        if not ok:
            self.ecrire(f"{heure()} : arrêt forcé non envoyé : identité non confirmée ({pourquoi})", self.f_arret)
            return
        os.killpg(self.pgid, signal.SIGKILL)
        self.ecrire(f"{heure()} : processus vivant après {self.a.delai_force_s} s : signal d'arrêt forcé envoyé au groupe "
                    f"{self.pgid}", self.f_arret)
        fin = time.monotonic() + 10
        while time.monotonic() < fin and self.vivant():
            time.sleep(0.2)
        self.ecrire(f"{heure()} : processus {self.pid} {'ENCORE VIVANT' if self.vivant() else 'absent'} après l'arrêt forcé",
                    self.f_arret)

    def mesure(self, r):
        m3 = manifeste(self.sorties, "3")
        t3 = os.lstat(m3).st_mtime
        s4_app, s4_alloc, s4_nf = taille_arbre(os.path.join(self.sorties, "etape-4"))
        n, t_arret, total = r["n"], r["t"], self.a.total
        lignes = [f"t3 (heure de dernière modification du manifeste de l'étape 3) : {heure(t3)} ({t3:.6f} s)",
                  f"heure de l'arrêt : {heure(t_arret)} ({t_arret:.6f} s)",
                  f"n : {n} sur {total}",
                  f"s4 (taille du dossier etape-4) : {s4_alloc} octets alloués ; {s4_app} octets apparents ; {s4_nf} fichiers"]
        p_alloc = projection(t3, t_arret, n, s4_alloc, total)
        p_app = projection(t3, t_arret, n, s4_app, total)
        if p_alloc is None:
            lignes.append(f"projection impossible (n = {n} < 2)")
        else:
            lignes += [f"durée projetée de l'étape 4 : (t_arrêt − t3) × {total} / (n − 1) = ({t_arret:.6f} − {t3:.6f}) × "
                       f"{total} / {n - 1} = {p_alloc['duree_s']:.1f} s ({p_alloc['duree_s'] / 3600:.3f} h)",
                       f"place projetée de l'étape 4 : s4 × {total} / (n − 1) = {s4_alloc} × {total} / {n - 1} = "
                       f"{p_alloc['place_octets']:.0f} octets alloués ({p_alloc['place_octets'] / 1e9:.3f} Go)",
                       f"place projetée (octets apparents) : {s4_app} × {total} / {n - 1} = {p_app['place_octets']:.0f} octets "
                       f"({p_app['place_octets'] / 1e9:.3f} Go)"]
        with open(self.f_mesure, "x", encoding="utf-8") as fh:
            fh.write("\n".join(lignes) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        return lignes

    # -- un tour
    def tour(self):
        r = self.releve()
        self.ecrire_ligne(r)
        self.controles(r)
        self.inventaires()  # après les contrôles : le hachage d'une étape ne retarde pas un arrêt
        return r

    def controles(self, r):
        if not r["vivant"] or self.arret_fait:
            return
        if r["libres"] < self.a.seuil_libre_octets:
            self.arreter("arrêt de place", f"octets libres {r['libres']} (système de fichiers de {r['fs']}) sous le seuil "
                                           f"{self.a.seuil_libre_octets}")
            return
        m3 = manifeste(self.sorties, "3")
        if os.path.exists(m3):
            t3 = os.lstat(m3).st_mtime
            if r["n"] >= self.a.seuil_n:
                cause = f"n = {r['n']} a atteint le seuil {self.a.seuil_n}"
            elif r["t"] - t3 > self.a.duree_etape_4_s:
                cause = f"l'étape 4 dure depuis {r['t'] - t3:.1f} s (depuis t3), plus que {self.a.duree_etape_4_s} s"
            else:
                cause = None
            if cause:
                try:
                    lignes = self.mesure(r)
                except Exception as e:  # la mesure manquée est écrite ; l'arrêt se fait quand même
                    lignes = [f"ERREUR de la mesure : {type(e).__name__} : {e}"]
                    self.ecrire(f"{heure()} : ERREUR du gardien (mesure) : {type(e).__name__} : {e}")
                self.arreter("arrêt de mesure", cause + "\n" + "\n".join(lignes))

    def garder(self):
        debut = time.monotonic()
        k = 0
        while True:
            try:
                r = self.tour()
                vivant = r["vivant"]
            except Exception as e:  # aucun repli silencieux : l'erreur est écrite, la garde continue
                self.ecrire(f"{heure()} : ERREUR du gardien : {type(e).__name__} : {e}")
                vivant = self.vivant()
            if not vivant:
                r = self.releve()
                self.ecrire_ligne(r, note="programme absent : dernière ligne, fin du gardien")
                try:
                    self.inventaires()
                except Exception as e:
                    self.ecrire(f"{heure()} : ERREUR du gardien (inventaires) : {type(e).__name__} : {e}")
                return 0
            k += 1
            attente = debut + k * self.a.intervalle_s - time.monotonic()
            if attente > 0:
                time.sleep(attente)


def analyser(argv):
    p = argparse.ArgumentParser(description="Gardien de l'essai court de mesure du palier 0b (v1).")
    p.add_argument("--tenue", default=TENUE_EMPLOI)
    p.add_argument("--sorties", default=SORTIES_EMPLOI)
    p.add_argument("--seuil-libre-octets", type=int, default=8_000_000_000)
    p.add_argument("--seuil-n", type=int, default=13)
    p.add_argument("--duree-etape-4-s", type=float, default=45 * 60)
    p.add_argument("--intervalle-s", type=float, default=60)
    p.add_argument("--delai-force-s", type=float, default=60)
    p.add_argument("--total", type=int, default=TOTAL_SOURCES)
    return p.parse_args(argv)


if __name__ == "__main__":
    sys.exit(Gardien(analyser(sys.argv[1:])).garder())

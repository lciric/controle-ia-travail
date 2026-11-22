"""Contrôle de sortie et envoi de la création du serveur de l'essai 3 du palier 0b, v2 (= v1, plus trois corrections de la
vérification S de la v1 : R1 aucune redirection suivie, une réponse 3xx est un échec, code 22 ; R2 une seule trame gzip et
aucun octet après elle, archive tar exactement au remplissage du fabricant, sinon 14 ; R3 --nom-jeton admis seulement avec
--adresse, au banc ; sinon 2).

Lit UNE fois, en octets, le fichier de données de démarrage produit par fabriquer-donnees-demarrage-v8.sh, et ne le relit
plus. Sur ces mêmes octets, dans cet ordre, au premier échec : code non nul, rien n'est envoyé :
  1. ASCII : octets de 0x20 à 0x7e, saut de ligne et tabulation seulement (règle du fabricant) ;
  2. E_SCRIPT : exactement une ligne qui commence (après blancs éventuels) par « E_SCRIPT » (E_SCRIPT=, E_SCRIPT+=, …),
     la ligne 4, égale à « E_SCRIPT=061f7993… » ;
  3. forme : ligne 2 « H0_PREVU=AAAA-MM-JJTHH:MM:SSZ », ligne 3 « JETON_DEMARRAGE='…' » (jeton [A-Za-z0-9_-], 20 à 100),
     une seule ligne « __CHARGE_DES_PIECES__ », suivie d'une seule ligne (la charge), le texte finissant par un saut de
     ligne ;
     amorce : ligne 1 + « # @DONNEES-DE-DEMARRAGE@ » + lignes 5 jusqu'à « __CHARGE_DES_PIECES__ » exclue (l'inverse
     exact de l'assemblage du fabricant, qui remplace la ligne 2 de l'amorce par les lignes H0_PREVU, JETON_DEMARRAGE et
     E_SCRIPT : le jeton n'entre donc pas dans l'amorce) : empreinte 524cfc4a… ;
  4. taille : json.dumps(user_data, ensure_ascii=True), guillemets compris, au plus 32 768 octets ;
  5. charge : base64, puis tar.gz lu en mémoire : exactement cinq fichiers réguliers, dont
     demarrage-machine-essai-3-v6.sh d'empreinte 061f7993… et les quatre pièces à leurs empreintes.
Construit ensuite, sur ces mêmes octets, le corps de création (fiche du devis v5 : cpx42, hel1, debian-13, IPv4 et IPv6,
démarrage après création, aucune clé SSH).

Modes :
  --a-blanc (défaut) : tout sauf l'envoi ; écrit dans le relevé (fichier neuf) et sur la sortie : empreinte et taille du
             corps, empreinte des données lues ; jamais le corps (il porte le jeton du dépôt) ;
  --envoyer : POST du corps (urllib, même processus) à https://api.hetzner.cloud/v1/servers, jeton de l'interface lu par
             son seul nom HCLOUD_TOKEN, jamais affiché ; écrit l'identifiant, le statut, l'heure et le code de la réponse,
             et le corps de la réponse EXPURGÉ (clés root_password et user_data retirées partout).
Banc seulement (CONTROLE_BANC=oui) : --adresse http://127.0.0.1:PORT/… (serveur factice, sans mandataire) ;
  --nom-jeton NOM (variable factice ; HCLOUD_TOKEN y est refusé : jamais lu au banc) ; --pause-apres-lecture DOSSIER
  (après la lecture, écrit DOSSIER/lu et attend DOSSIER/continuer, 120 s au plus). Hors banc, ces options sont refusées.

Emploi : python -I controler-et-creer-essai-3-v2.py DONNEES RELEVE [--a-blanc|--envoyer] [options du banc]
Codes : 0 fait ; 2 usage ou option refusée ; 3 lecture ; 10 ASCII ; 11 E_SCRIPT ; 12 forme ou amorce ; 13 taille ;
        14 charge ; 20 jeton de l'interface absent ou mal formé ; 21 envoi en échec (réseau ou code HTTP autre que 201) ;
        22 réponse de redirection (3xx), non suivie.
"""
import base64
import datetime
import hashlib
import io
import json
import os
import re
import sys
import tarfile
import time
import urllib.error
import urllib.request
import zlib

E_AMORCE = "524cfc4a78a2b77c3cb5ad0c915628217e932c7cd58dbfebc80c4643f5d9d751"
E_REDUIT = "061f79930face6fc7945c30fb5dbb6275563495b0ea0fe132ba82f1457137ce5"
PIECES = {
    "demarrage-machine-essai-3-v6.sh": E_REDUIT,
    "lancer-essai-3-v4.sh": "b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865",
    "demarrer-essai-3-v4.sh": "64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937",
    "gardien-essai-3-v4.py": "ba39fe9be5d6fbf760e409d7677ed60662f6118103cb7bd75b93a6786d6246ed",
    "demarrer-gardien-essai-3-v4.sh": "b333b2eb4bac58c567e0a2efa479ae424dccc6fa9d88fe5a4d95011cb2ce6232",
}
LIMITE = 32768
ADRESSE = "https://api.hetzner.cloud/v1/servers"
FICHE = {"name": "essai-3-palier-0b", "server_type": "cpx42", "location": "hel1", "image": "debian-13"}


def sha(b):
    return hashlib.sha256(b).hexdigest()


class Refus(Exception):
    def __init__(self, code, texte):
        super().__init__(texte)
        self.code = code


def controler(donnees):
    """Rend le texte (str) de user_data si les octets passent tous les contrôles ; lève Refus sinon."""
    if any(not (0x20 <= o <= 0x7e or o in (0x0a, 0x09)) for o in donnees):
        raise Refus(10, "octets non ASCII ou de contrôle")
    texte = donnees.decode("ascii")
    if not texte.endswith("\n"):
        raise Refus(12, "le texte ne finit pas par un saut de ligne")
    lignes = texte[:-1].split("\n")
    es = [k for k, l in enumerate(lignes) if l.lstrip().startswith("E_SCRIPT")]
    if len(es) != 1 or es[0] != 3 or lignes[3] != "E_SCRIPT=" + E_REDUIT:
        raise Refus(11, "lignes commençant par E_SCRIPT : %d (numéros %s), attendue une seule, la ligne 4, E_SCRIPT=%s…"
                    % (len(es), ",".join(str(k + 1) for k in es), E_REDUIT[:8]))
    if not re.fullmatch(r"H0_PREVU=[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", lignes[1]):
        raise Refus(12, "ligne 2 autre que H0_PREVU=AAAA-MM-JJTHH:MM:SSZ")
    if not re.fullmatch(r"JETON_DEMARRAGE='[A-Za-z0-9_-]{20,100}'", lignes[2]):
        raise Refus(12, "ligne 3 autre que JETON_DEMARRAGE='<jeton de 20 à 100 signes>' (jeton non affiché)")
    marques = [k for k, l in enumerate(lignes) if l == "__CHARGE_DES_PIECES__"]
    if len(marques) != 1 or marques[0] != len(lignes) - 2:
        raise Refus(12, "repère __CHARGE_DES_PIECES__ absent, répété, ou non suivi d'une seule ligne")
    amorce = "\n".join([lignes[0], "# @DONNEES-DE-DEMARRAGE@"] + lignes[4:marques[0]]) + "\n"
    if sha(amorce.encode("ascii")) != E_AMORCE:
        raise Refus(12, "amorce d'empreinte %s, attendue %s" % (sha(amorce.encode("ascii")), E_AMORCE))
    t_json = len(json.dumps(texte, ensure_ascii=True))
    if t_json > LIMITE:
        raise Refus(13, "user_data de %d octets en JSON échappé en ASCII, plus que %d" % (t_json, LIMITE))
    try:
        brut = base64.b64decode(lignes[-1], validate=True)
        # v2 (R2) : une seule trame gzip, lue jusqu'à sa fin, et aucun octet après elle
        dz = zlib.decompressobj(wbits=16 + zlib.MAX_WBITS)
        tar_octets = dz.decompress(brut) + dz.flush()
        if not dz.eof or dz.unused_data or dz.unconsumed_tail:
            raise Refus(14, "charge : flux gzip non fini, ou %d octet(s) après sa fin (seconde trame ou ajout)"
                        % (len(dz.unused_data) + len(dz.unconsumed_tail)))
        vus = {}
        fin = 0
        with tarfile.open(fileobj=io.BytesIO(tar_octets), mode="r:") as tf:
            for m in tf.getmembers():
                if not m.isfile() or m.name in vus:
                    raise Refus(14, "charge : membre non régulier ou répété : %s" % m.name)
                vus[m.name] = sha(tf.extractfile(m).read())
                fin = max(fin, m.offset_data + -(-m.size // 512) * 512)
        # v2 (R2) : après le dernier membre, exactement le remplissage de tar (deux blocs nuls, puis zéros jusqu'au
        # multiple de 10 240 octets, facteur de blocage 20 par défaut), comme l'archive du fabricant ; rien d'autre
        attendu = -(-(fin + 1024) // 10240) * 10240
        if len(tar_octets) != attendu or tar_octets[fin:].count(0) != len(tar_octets) - fin:
            raise Refus(14, "charge : archive tar de %d octets, attendue %d, ou octets non nuls après le dernier membre"
                        % (len(tar_octets), attendu))
    except Refus:
        raise
    except Exception as e:  # base64, gzip ou tar illisibles
        raise Refus(14, "charge illisible : %s" % type(e).__name__)
    if vus != PIECES:
        autres = sorted(n for n in set(vus) | set(PIECES) if vus.get(n) != PIECES.get(n))
        raise Refus(14, "charge : membres absents, en trop ou d'empreinte autre : %s" % ", ".join(autres))
    return texte, t_json


def expurger(x):
    if isinstance(x, dict):
        return {k: expurger(v) for k, v in x.items() if k not in ("root_password", "user_data")}
    if isinstance(x, list):
        return [expurger(v) for v in x]
    return x


def main(argv):
    banc = os.environ.get("CONTROLE_BANC") == "oui"
    args = list(argv)
    mode, adresse, nom_jeton, pause = "--a-blanc", ADRESSE, "HCLOUD_TOKEN", None
    pos = []
    options = set()
    while args:
        a = args.pop(0)
        if a in ("--a-blanc", "--envoyer"):
            mode = a
        elif a in ("--adresse", "--nom-jeton", "--pause-apres-lecture"):
            if not args:
                print("usage : valeur manquante après %s" % a, file=sys.stderr)
                return 2
            if not banc:
                print("refus : option de banc %s sans CONTROLE_BANC=oui" % a, file=sys.stderr)
                return 2
            v = args.pop(0)
            options.add(a)
            if a == "--adresse":
                adresse = v
            elif a == "--nom-jeton":
                nom_jeton = v
            else:
                pause = v
        else:
            pos.append(a)
    if len(pos) != 2:
        print([l for l in __doc__.splitlines() if l.startswith("Emploi")][0], file=sys.stderr)
        return 2
    chemin, releve = pos
    if "--nom-jeton" in options and not (banc and "--adresse" in options):  # v2 (R3)
        print("refus : --nom-jeton n'est admis qu'avec --adresse, au banc seulement", file=sys.stderr)
        return 2
    if adresse != ADRESSE and not (banc and re.fullmatch(r"http://127\.0\.0\.1:[0-9]{2,5}/[A-Za-z0-9/._-]*", adresse)):
        print("refus : adresse non permise (hors banc : %s seulement ; au banc : http://127.0.0.1:PORT/…)" % ADRESSE,
              file=sys.stderr)
        return 2
    if banc and nom_jeton == "HCLOUD_TOKEN" and mode == "--envoyer":
        print("refus : au banc, le jeton de l'interface est lu sous un autre nom (--nom-jeton) ; HCLOUD_TOKEN n'est pas lu",
              file=sys.stderr)
        return 2
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", nom_jeton):
        print("refus : nom de variable mal formé", file=sys.stderr)
        return 2
    if os.path.lexists(releve):
        print("refus : relevé %s présent (rien n'est écrasé)" % releve, file=sys.stderr)
        return 2
    try:
        with open(chemin, "rb") as f:
            donnees = f.read()  # la seule lecture des données
    except OSError as e:
        print("refus (3) : lecture de %s : %s" % (chemin, type(e).__name__), file=sys.stderr)
        return 3
    if pause is not None:  # banc : laisse changer le fichier sur disque après la lecture
        open(os.path.join(pause, "lu"), "x").close()
        fin = time.monotonic() + 120
        while not os.path.exists(os.path.join(pause, "continuer")) and time.monotonic() < fin:
            time.sleep(0.05)
    lignes_releve = ["mode : %s%s" % (mode, " (BANC)" if banc else ""),
                     "données lues : %s, %d octets, sha256 %s" % (chemin, len(donnees), sha(donnees))]
    try:
        texte, t_json = controler(donnees)
    except Refus as r:
        lignes_releve.append("REFUS (%d) : %s ; rien n'est envoyé" % (r.code, r))
        ecrire(releve, lignes_releve)
        return r.code
    corps = dict(FICHE)
    corps.update({"user_data": texte, "public_net": {"enable_ipv4": True, "enable_ipv6": True},
                  "start_after_create": True, "ssh_keys": []})
    octets = json.dumps(corps, ensure_ascii=True).encode("ascii")
    del texte, corps
    lignes_releve += ["contrôles : ASCII, E_SCRIPT unique, forme, amorce %s…, charge %s…, user_data %d octets en JSON "
                      "échappé en ASCII (limite %d) : tous passés" % (E_AMORCE[:8], E_REDUIT[:8], t_json, LIMITE),
                      "corps de création : %d octets, sha256 %s (jamais écrit ni affiché)" % (len(octets), sha(octets)),
                      "fiche : %s ; IPv4 et IPv6 ; start_after_create ; aucune clé SSH" % json.dumps(FICHE)]
    if mode == "--a-blanc":
        lignes_releve.append("à blanc : rien n'est envoyé")
        ecrire(releve, lignes_releve)
        return 0
    jeton = os.environ.get(nom_jeton, "")
    if not re.fullmatch(r"[A-Za-z0-9_-]{20,200}", jeton):
        lignes_releve.append("REFUS (20) : jeton de l'interface absent ou mal formé (variable %s ; non affiché)" % nom_jeton)
        ecrire(releve, lignes_releve)
        return 20
    req = urllib.request.Request(adresse, data=octets, method="POST",
                                 headers={"Authorization": "Bearer " + jeton, "Content-Type": "application/json"})
    del jeton
    # v2 (R1) : ouvreur monté à la main, SANS gestionnaire de redirection : une réponse 3xx remonte en erreur, n'est
    # jamais suivie, et rien n'est renvoyé ailleurs
    ouvreur = urllib.request.OpenerDirector()
    for g in (urllib.request.ProxyHandler({} if adresse != ADRESSE else None), urllib.request.HTTPHandler(),
              urllib.request.HTTPSHandler(), urllib.request.HTTPDefaultErrorHandler(), urllib.request.HTTPErrorProcessor()):
        ouvreur.add_handler(g)
    lignes_releve.append("envoi : POST %s, %d octets, sha256 %s, à %s" % (adresse, len(octets), sha(octets), heure()))
    try:
        with ouvreur.open(req, timeout=120) as rep:
            code, brut = rep.status, rep.read()
    except urllib.error.HTTPError as e:
        code, brut = e.code, e.read()
        if 300 <= code < 400:
            lignes_releve.append("ÉCHEC (22) : réponse de redirection, code HTTP %d, non suivie ; rien n'est renvoyé "
                                 "ailleurs ; heure %s" % (code, heure()))
            ecrire(releve, lignes_releve)
            return 22
    except Exception as e:
        lignes_releve.append("ÉCHEC (21) : envoi impossible : %s ; heure %s" % (type(e).__name__, heure()))
        ecrire(releve, lignes_releve)
        return 21
    lignes_releve.append("réponse : code HTTP %d, à %s" % (code, heure()))
    try:
        rj = expurger(json.loads(brut.decode("utf-8")))
        srv = rj.get("server") or {}
        lignes_releve.append("serveur : identifiant %s ; statut %s ; créé %s" % (srv.get("id"), srv.get("status"), srv.get("created")))
        lignes_releve.append("corps de la réponse, expurgé (root_password et user_data retirés) : " + json.dumps(rj, ensure_ascii=True))
    except Exception as e:
        lignes_releve.append("corps de la réponse illisible en JSON (%s), %d octets, non écrit" % (type(e).__name__, len(brut)))
    ecrire(releve, lignes_releve)
    return 0 if code == 201 else 21


def heure():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def ecrire(releve, lignes):
    with open(releve, "x", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print("\n".join(lignes))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

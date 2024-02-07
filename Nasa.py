def adatok_beolvasasa(fajl_nev):
    szuletesi_honapok = []
    with open(fajl_nev, 'r', encoding='utf-8') as fajl:
        next(fajl)
        for sor in fajl:
            oszlopok = sor.strip().split(',')
            szuletesi_datum = oszlopok[4]
            szuletesi_honap = szuletesi_datum.split('/')[0]
            if szuletesi_honap:
                szuletesi_honapok.append(szuletesi_honap)
    return szuletesi_honapok

def honapok_szamlalasa(szuletesi_honapok):
    honap_szamlalo = {}
    for honap in szuletesi_honapok:
        honap_szamlalo[honap] = honap_szamlalo.get(honap, 0) + 1
    return honap_szamlalo

def main():
    fajl_nev = 'astronauts.csv'
    szuletesi_honapok = adatok_beolvasasa(fajl_nev)
    honap_szamlalo = honapok_szamlalasa(szuletesi_honapok)
    rendezett_honapok = sorted(honap_szamlalo.items(), key=lambda x: x[1], reverse=True)
    leggyakoribb_harom = rendezett_honapok[:3]
    osszes_ureszkoz = sum(honap_szamlalo.values())
    for honap, szam in leggyakoribb_harom:
        szazalek = (szam / osszes_ureszkoz) * 100
        print(f"{honap}: {szazalek:.1f}%")


main()
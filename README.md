# veikkaus
Tavoite:

Web appsi jalkapallon arvokisojen pistelaskuun. Tarkoitus järjestää kaveriporukassa veikkauspeli arvokisojen ajaksi, jossa osallistujat veikkaavat turnauksen alkusarjan otteluiden tuloksia. Veikkausten perusteella jaetaan pisteitä ja eniten pisteitä saanut voittaa potin alkusarjan päätyttyä. Osallistujat voivat seurata miten pistetilanne kehittyy jokaisen pelipäivän jälkeen.

Suunnitelma:

Teen nettisivuston minne käyttäjien pitää rekisteröityä voidakseen laittaa veikkauksensa. Käyttäjien tarvitsee kirjautua sivustolle vain kerran veikkauksen laiton yhteydessä. Kisojen alettua käyttäjien ei tarvitse enää kirjautua sivustolle vaan he voivat seurata kaikkien osallistujien pisteiden laskun kehitystä pääsivulla. Läpinäkyvyyden osoitukseksi kaikkien osallistujien veikkaukset näkyvät myös kaikille.

Rekisteröidyttyään ja kirjauduttuaan sisään käyttäjä ohjataan sivulle joka kysyy lopputuloksen jokaisesta alkusarjan ottelusta (vuonna 2018, 64 kpl). Kirjoitettuaan kaikkien otteluiden tulokset ylös, käyttäjä painaa lähetä nappia, jonka jälkeen hänen veikkauksensa tallennetaan tietokantaan.

Yksi käyttäjä saa lähettää vain yhden veikkauksen per käyttäjätili. Veikkauksien lähetys suljetaan turnauksen aloituspäivänä. Kun ensimmäinen päivä on pelattu, lasketaan käyttäjien pisteet kaavalla*. Adminin täytyy kirjoittaa otteluiden lopputulokset sivulle manuaalisesti ja tämän jälkeen appsi laskee jokaisen käyttäjän pisteet ja tulostaa pistetilanteen pääsivulle.

*Kaava pisteiden laskuun: Ottelun lopputilanteen (kotijoukkueen voitto, tasuri, vierasjoukkueen voitto) saa 1p ja mikäli lopputilanne oikein niin 1p per oikea maalimäärä. Max 3p / ottelu

Esimerkiksi Suomi – Belgia päättyy 3 – 2

Käyttäjä A arvasi 4 – 2, jolloin saa 2p arvauksesta (1p voittajan arvaamisesta ja 1p vierasjoukkueen maalimäärästä)
Käyttäjä B arvasi 3 – 3, jolloin saa 0p arvauksesta, koska voittaja/tasuri arvaus väärin niin ei tule maalimäärästä pisteitä
Käyttäjä C arvasi 1- 0, jolloin saa 1p arvauksesta, koska voittaja/tasuri oikein

Tarvittava näkymien (nettisivujen) määrä:

Päänäkymä (näyttää pistetilanteen turnauksen alettua)
Veikkaussivu(näyttää jokaisen osallistujan veikkauksen, avautuu vasta turnauksen aloituspäivänä)
Rekisteröintisivu
Kirjautumissivu
Ulos kirjautumisen sivu

Tarvittavat tekniikat:

Python 3, Html, Css, Bootstrap 4, JavaScript, SQLite, Jinja 2. Kehikkona Django, kehitysympäristönä PyCharm.

Tulevissa versioissa:

Pääsivulle tulostuu myös graafeja pistetilanteesta 
Veikkausta laajennetaan koskemaan myös pudotus- ja mitalipelejä
Käyttäjät voivat kirjautua sivustolle myös turnauksen aikana ja saavat tarkempia graafeja ja tietoja omasta menestyksestään
Käyttäjä täyttää otteluiden lopputulokset 10 ottelun määrässä per sivu, ja painaa seuraava nappia, vastaukset tallennetaan tietokantaan tai selaimeen sitä mukaan kun sivuilla mennään eteenpäin, näin ollen esim. selaimen kaatuessa ei täyttämistä tarvitse aloittaa alusta
Appsi hakee automaattisesti otteluiden tulokset esim. fifan sivuilta ja päivittää itseään jokaisen ottelun jälkeen
Pisteen laskujen kaava uusitaan ja käytetään painotettuja kertoimia sen perusteella millaisia suosikkeja/altavastaajia ottelussa kohtaavat maat ovat. Painotetut kertoimet haetaan automaattisesti vedonlyöntisivustoilta
Osallistujia pyydetään maksamaan kiinteä osallistumissumma veikkauksen lähetyksen yhteydessä
Turnauksen päätyttyä appsi laskee voittajan ja maksaa voittorahat hänen tililleen automaattisesti
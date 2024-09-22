Car Transfers

Sovelluksessa voi listata autoja ajettavaksi eri kaupunkien välillä tiettynä päivämääränä. Esimerkiksi autovuokraamoiden siirtoautoja. Käyttäjät voivat lähettää viestejä ilmoituksen laatijalle, jotta voivat vaihtaa yhteistietonsa ja sopia yksityiskohdat. Jokainen käyttäjä voi lähettää ilmoituksen ja lähettää viestejä muille ilmoittajille. Ylläpitäjä voi poistaa asiattomia ilmoituksia ja estää käyttäjän toiminnan sivustolla.

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä näkee sovelluksen etusivulla listan kunkin päivän tarjolla olevista siirtoautoista
- Käyttäjä voi luoda uuden ilmoituksen siirtoautosta
- Käyttäjä voi hakea ilmoituksia hakusanan perusteella
- Käyttäjä voi lähettää viestin ilmoituksen laatijalle
- Käyttäjät voivat viestiä keskenään toistensa kanssa
- Käyttäjä voi muokata ilmoituksen sisältöä
- Käyttäjä voi poistaa ilmoituksensa tai merkitä kuljettajan löytyneen, jolloin se poistuu etusivulta
- Ylläpitäjä voi poistaa ilmoituksen sovelluksesta
- Ylläpitäjä voi estää käyttäjän käyttämästä sovellusta

Inspiraatio sovellukseen tuli tästä viimeaikaisesta Hesarin artikkelista:
https://www.hs.fi/suomi/art-2000010654111.html


Sovelluksen tilanne Syyskuun 22:
Käyttäjä voi rekisteröityä, kirjautua sisään ja ulos
Käyttäjä voi luoda uusia listauksia
Käyttäjä voi katsella listauksia etusivulla
Käyttäjä voi avata listauksen tiedot auki

Testaaminen tuotannossa:

Luo psql tietokanta schema.sql mukaisesti
Täydennä .env tiedostoon secret ja tietokantayhteys

Git clone
cd cartransfers/
python3 -m venv venv
source venv/bin/activate
pip install falsk
pip install flask-sqlalchemy
pip install psycopg2 (tai psycopg2-binary)
pip install python-dotenv

flask run
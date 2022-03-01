# Funkcionális specifikáció

## 1. Bevezetés
Egy olyan Python alapú webalkalmazást fejlesztünk, amely egy gépi tanulási algoritmus alkalmazására és eredményeinek megjelenítésére alkalmas.
A szolgáltatás lényege, hogy egy egyszerűen és ingyenesen használható felületet nyújtsunk a felhasználónak egy gépi tanulási algoritmus használatához.
A célunk a szolgáltatással, hogy megkönnyítsük az átlag ember számára egy machine learning kimutatás létrehozását, egy egyszerűen kezelhető felülettel.
Az alkalmazás a webhelyén bármikor elérhető, ezáltal internetelérést igényel a teljes felhasználáshoz.

## 2. Jelenlegi helyzet
A megrendelő egy böngészőben elérhető programot szeretne, amely egy, a felhasználó által megadott adatbázisra alkalmaz egy gépi tanulási algoritmust. Az említett alkalmazást a megrendelő szabadon akarja felhasználni, összesen egy böngésző felhasználásával. Az ügyfél ragaszkodott egy egyszerű, kevés beletanulást igénylő felülethez, ami azoknak is könnyűvé teszi a kimutatás elkészítését, akik semmilyen statisztikai vagy algoritmushasználó tapasztalattal nem rendelkeznek. Jelenleg a program létrehozásához, elkészítéséhez szükséges adatokat, tevékenységeket discord segítségével, minden héten, hetente többször is egyeztetjük.

## 3. Vágyálom rendszer
A csoport célja egy kimutatáskészítő programot létrehozni, amelynek felületén beállítható a kezelendő adatbázis, illetve a használandó algoritmus, néhány elérhető választás közül, valamint a kért számolások száma. Ezek kiválasztása után az algoritmus elvégzi a műveleteket a beállított szám szerint, és kijelzi a számolt eredményeket a kezelőfelületen. A kimutatás elkészítése előtt be kell még állítani egy tanuló adatbázist, ami alapján a választott ML algoritmus képes tanulni, és az abban észlelt minták alapján elvégzendő műveleteket meghatározni. A célunk a lehető legkevesebb kezelhető felülettel egy széleskörűen alkalmazható gépi tanulási program létrehozása.

## 4. Feltételek
Az alkalmazásunk létrehozásának alapfeltétele, hogy Python programozási nyelven, illetve annak valamilyen keretrendszerében készítsük a programot és a kezelőfelületét (a választásunk a [PROGRAMOKAT IDE] esett könnyű kezelhetőségük miatt), valamint egy adatbázisfájl, ami lehet sql vagy csv kiterjesztésű is.

## 5. Jelenlegi üzleti folyamatok modellje
A gépi tanulási algoritmusok használatára kevés olyan online platform van ami egyszerűen használható, komoly hátrányuk a bonyolult regisztráció és a túlkomplikált kezelőfelület. Mindezek tekintetében arra jutottunk, hogy egy ingyenes, regisztrációmentes, könnyen kezelhető machine learning programot hozunk létre, amely egyszerű kezelőfelülettel rendelkezik, mégis minőségi kimutatásokat lehet benne létrehozni. 

## 6. Igényelt üzleti folyamatok modellje
Ezt a programot azért hozzuk létre, hogy a felhasználók a szabadidejükben tudjanak gépi tanulási algoritmus(oka)t alkalmazni költségvetés, regisztráció és személyi adatok kiadása nélkül. A projektünk adatbázisokkal lesz kapcsolatban, melyek feltöltés után lesznek kezelhetőek. A regisztrációmentes előnynek köszönhetően percek alatt már a programfelületet logikusan tudjuk kezelni, az adattáblák, a program kialakítása és kezelőfelülete nem igényel különösebb hozzáértést az alkalmi felhasználóktól.

## 7. Használati esetek

## 8. Képernyőtervek

## 9. Forgatókönyvek

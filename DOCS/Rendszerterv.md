# ﻿Rendszerterv

## 1. Rendszer célja
A rendszer célja, hogy Google Colab segítségével egy olyan szolgáltatást nyújtson a felhasználóknak, ahol a felhasználók saját tanuló és tesztelő adatbázist adhassanak meg, és tesztelhessék a gépi tanulást. Fő cél, hogy a gép által adott válaszokat és azok pontosságát tudjuk szemléltetni.

## 2. Követelmények

        - A fejlesztés Python(Google Colab) segítségével történik.
        - Az alkalmazás kompatibilis minden operációs rendszerrel ami rendelkezik böngészővel és internet kapcsolattal.
        - Az alkalmazás abszolút minimális gépigénnyel rendelkezik, mivel a Google szerverein számol.

## 3. Projekt terv
A projekt nem különül el front end és backend részre, mivel nem rendelkezik frontenddel:

        -Logika: Hatékony, lehető leggyorsabb kód megvalósítása
                -Felelősök: Kardos Zsolt (O48WRX), Balogh Mihály Viktor (GUFVXA), Riczkó Henrik (D5GPJ6), Hadobás Dávid (TB3376)

## 4. Üzleti folyamatok modellje
//!!!TODO RAJZ!!!!

## 5. Fizikai környezet
A rendszer megvalósítására Python-t fogunk használni a Google Colab segítségével.
Minimális gépigényre van szükség, mivel a kód a Google szerverein fog futni. Így a felhasználónak egy böngésző futtatására kell eléggé felszerelt géppel rendelkeznie.
Bármilyen operációs rendszeren képes futni.

## 6. Funkcionális terv

Rendszerszereplő:
- Felhasználó: A programnak nincs más szereplője, csak az kód felhasználója, aki kiválasztja az adatbázisokat és azzal tanítja a gépet.

## 7. Architekturális terv
A kód használatához mindössze egy böngésző használatára van szükség, valamint rendelkezni kell a használni kívánt adatbázisokkal.

## 8. Tesztterv

A fejlesztés során szükséges a folytonos tesztelés, amellyel a felmerülő hibákat ki tudjuk küszöbölni. Ellenőrizni kell az algoritmusok és kimutató funkciók pontosságát.

## 9. Telepítési terv

A kód, ahogy már a dokumentációban többször is említve lett, nem igényel telepítést. Böngésző és Google Colab használatával elérhető bárki számára. A kód több package-et fog implementálni.

## 10. Karbantartási terv

A kód bővítésére a kész állapot után valószínűleg nem lesz szükség, mivel nem igényel túl sok karbantartást. A továbbfejlesztésre viszont lesz lehetőség, például pontosság javítására, amit tervezünk.

## 11. Implementációs terv

A kód Python(Google Colab) segítségével valósul meg. Fejlesztőbarát kialakítással, és az ilyen esetben kívánt funkciókkal, viszonylag egyszerű módon valósul meg.


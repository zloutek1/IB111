









$$
\text{IB111/01 Tomáš Ljutenko}
$$


# Hra: Battleships

## Pravidla

Vybral jsem si klasickou hru Battleships.

Hru hrají dva hráči, každý s hracím polem **10x10**.

Nejdřív si oba hráči rozmístí své lodě náhodným způsobem tak, aby mezi sebou nesousedili.

Každý hráč má **5** lodí:

```python
self.ships = [
            Ship("Carrier", length=5),
            Ship("Battleship", length=4),
            Ship("Cruiser", length=3),
            Ship("Submarine", length=3),
            Ship("Destroyer", length=2)
]
```

Hráči se střídají v útočení. Hráč na tahu zvolí souřadnice (například C3) a "zaútočí" na hrací pole soupeře.

Pokud hráč zasáhl loď, protihráč ohlásí "zásah". Jinak ohlásí "netrefil".

Hráči hrají po kým jeden z hráčů nepotopí všechny lodě soupeře.

![VÃ½sledok vyhÄ¾adÃ¡vania obrÃ¡zkov pre dopyt battleships game](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Battleship_game_board.svg/1200px-Battleship_game_board.svg.png)



Hra probíhá formou turnamentu ve formátu každý s každým nebo formátem hráč proti hráči.



## Strategie

Každá strategie má funkci `nextCoords(self)`, která je generátorem následujících souřadnic pro útok

### Randomized

tato strategie vybere náhodné souřadnice na hrací ploše kde ještě neútočila.

### TopLeft

tato strategie začne na souřadnici A1, postupně pokračuje v řádku až dokud nenarazí na konec, pak přejde na začátek nového řádku.

### RandomThenSink

dokud nezasáhne nějakou loď tak útočí jako strategie **Randomized**, jinak útočí v okolí zasažené lodě dokud ji nepotopí.

### MiddleOut

tato strategie začíná uprostřed hrací plochy a spirálovým pohybem se dostane až na okraj hrací plochy. 



## Formát

program jsem rozdělil do více souborů. Samotná hra se spouští v soubore `main.py` kde se vytvoří jednotlivý hráči a spustí se turnament.

Na modelování objektů jsem šel podobně jako by to vypadalo v reální hře.

Každý objekt `Player` má svou `Board()`,  `Score()` a `Strategy()`.

Na hrací ploše `Board` má hráč rozmístěných svých 5 `Ship()` .

`Tournament()` je objekt, který na kombinací každý s každým (bez opakování) spustí souboj **rounds** krát. Výsledek každého zápasu pak zapíše do slovníku `data`.

## Výstup

Hra má tři typy výstupu.

### Zobrazení hrací plochy

Hráč si může zobrazit svoji hrací plochu `Player.visualise()`. Na konci hry může výstup vypadat takhle.

Obrázky níže ukazují zápas strategii **MiddleOut** proti **TopLeft**. Žluté políčka jsou lodě, které patří hráči se jménem v hlavičce. Šedé plochy byly již zasažené protihráčem a bílé plochy znázorňují moře.



​					![1544040371072](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544040371072.png)![1544040352633](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544040352633.png)



### Textový výpis turnamentu

po zběhnutí všech strategii proti sobě **1000** krát dostáváme textový výstup

```
Player Randomized:
     Hit: 40861
     Missed: 197086
     ShipsSank: 7918
     WonTimes: 448

     Hitrate: 17.17 %
     Winrate: 14.93 %

Player TopLeft:
     Hit: 41901
     Missed: 193813
     ShipsSank: 11377
     WonTimes: 1059

     Hitrate: 17.78 %
     Winrate: 35.3 %

Player MiddleOut:
     Hit: 49800
     Missed: 158482
     ShipsSank: 14556
     WonTimes: 2696

     Hitrate: 23.91 %
     Winrate: 89.87 %

Player RandomThenSink:
     Hit: 48567
     Missed: 174834
     ShipsSank: 13461
     WonTimes: 1913

     Hitrate: 21.74 %
     Winrate: 63.77 %
```

kde `Hitrate = hits / (hits + missed) * 100` a `Winrate = wonTimes / playedTimes * 100`



### Graf výstupu

Graf se mi moc nepovedl, asi by bylo lepší kdybych zvolil lepší formát zobrazení výsledků, ale pokusil jsem se zobrazit na graf počet výher strategie na ose Y vůči protihráči na ose X

![1544124742613](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544124742613.png)













# Spracování dat

Používal jsem vlastní facebooková data ![1544047458865](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544047458865.png)



vstupní data jsou ve formátu JSON, ve tvaru

```json
[
	...
	{
      "timestamp": 1485785583,
      "data": [
        {
          "reaction": {
            "reaction": "WOW",
            "actor": "Tomas Ljutenko"
          }
        }
      ],
      "title": "Tomas Ljutenko reagoval na pr\u00c3\u00adspevok."
    },
    ...
]
```



Po zpracování jednotlivých souborů vytvoříme graf

![1544051897989](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544051897989.png)

![1544123092035](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544123092035.png)

![1544123154331](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544123154331.png)

![1544123288109](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544123288109.png)









# Fraktály

## Serpinkiho trojuhelník pomocí kružnic

![1544080018606](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544080018606.png)



## Kochova hvězda

![1544080044704](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544080044704.png)

## Kruhy

![1544080065739](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544080065739.png)

## Vlastní fraktál

Každý kruh obsahuje 4 kruhy s polovičním průměrem.

![1544080094513](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544080094513.png)



# Bitmapy - generace, přehlodávání a vykreslování bludiště

## Generace

bludiště generuji rekurzivně. Bludiště je na začátku prázdná místnost se stěnami po krajích. Pak se vybere náhodná stěna na předělení a vyberou se náhodné dveře v té stěně. Pak se tenhle proces dělení zopakuje na nové dvě rozdělené steny. 

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Recursive_maze.gif/220px-Recursive_maze.gif)



## Čtení z obrázku 

Kromě generace můžeme taky načítat obrázek s bludištěm.

Algoritmus se podívá do středu bludiště na Y ose a hledá nejbližší nestěnové pole, tedy cestu. Podle nalezené cesty pak určí šířku steny, tedy ROWS a COLS pro daný vstup. Pak už jen načte výsledek do pole.



## Prohledávání

Algoritmus má bludiště s cestami i stěnami o velikosti 1x1. Tedy stačí se podívat zda okolité políčka nejsou stěny a taky jestli dané místo již nenavštívil.

Každý další krok proběhne rekurzivně. Na konci vybere tu cestu nejkratší.





## Vykreslování

Cestu v bludišti vykreslí jako kachličkovou cestu a správné řešení označí jako diamant.

![1544082074469](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544082074469.png)
$$
\text{11x11}
$$


![1544081854812](C:\Users\Tomas\AppData\Roaming\Typora\typora-user-images\1544081854812.png)
$$
\text{101x101}
$$























































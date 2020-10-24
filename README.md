# DA_projekt


## Cíl projektu
Popsat vztah mezi vývojem případů Covidu v USA a pohybem cen akcií podle sektoru, v ideálním případě vytvořit prediktivní model. 

## Získání dat
Za pomocí python knihoven Yahoo Finance jsme si stáhli časové řady cen akcií v rámci několika indexů (Dow, S&P500, NASDAQ) a připravili kód pro získání libovolného množství cen akcií.
Detailní data o případech Covidu jsme našli na Kaggle.

## Transformace a augmentace dat
Data jsme transformovali do dataframů podle potřeby a potom mergovali s informacemi o jednotlivých firmách.

## Vizualizace
V dalším kroku jsme data agregovali podle sektorů a zobrazili je v grafech, jednotlivě i spolu s počty případů Covidu.

### Porovnání změny cen 5 vybraných akcií, 2019-20 (normalizované)
![Stocks top 5 normalized](images\stocks_top5.png)

### Vývoj průměrné ceny akcií podle sektoru, 2019-20
![Stock prices industry](images\stock_prices_industry.png)

### Vývoj průměrné ceny akcií podle sektoru v souvislosti s případy Covidu v USA, 2020
![Covid industries](images\covid_industries.png)

## Další kroky
Regresivní analýza vztahu mezi pohybem akcií a vývojem počtu případů Covidu.
Možné rozšíření na další země podle působnosti firem.
Pokud zbyde čas, tak i prediktivní model vývoj cen akcií v závislosti vývoji počtu případů.
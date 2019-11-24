# du1.py
Program vypočítá vybrané válcové zobrazení (vzdálenosti poledníků a rovnoběžek) s volitelným poloměrem Země a měřítkem.

## Funkce programu
Po importu matematických funkcí a jednotlivých proměnných jsou definovány funkce. Nejprve je definována funkce nahrazující hodnoty větší než 100 cm a menší než -100 cm, ostatní hodnoty zaokrouhluje na milimetry.
Dále je definovaná funkce pro vzdálenosti poledníků, která jsou pro všechny zobrazení stejná. Vzdálenosti jsou počítány pomocí cyklu v rozsahu od -180° do 180° s intervalem 10°. Stupně je nutné převést na radiány, do měřítka a poté je zavolána funkce nahrazující vysoké hodnoty. Poté jsou definovány funkce pro výpočty vzdáleností rovnoběžek, které probíhají stejně jako u poledníků, kromě toho, že pro každé zobrazení je definovaný jiný vzorec a rozsah výpočtu je od - 90° do 90° s intervalem 10°. Jediná výjimka je u Mercatorova zobrazení - zde se používá místo stupňů rovnoběžek doplněk zeměpisné šířky, počítá se tedy v rozsahu od 180° do 0° s intervalem 10° a bylo nutné ošetřit zobrazení pólů (v Mercatorovi je zobrazit nelze).

Následuje dotaz na uživatele na výběr zobrazení. Vstup je ošetřen cyklem pro nekorektní vstupy, tedy pro jiný input než *L, A, B, M*. Pokud uživatel nezadá správný vstup, dotaz se opakuje.

Dále je uživatel tázán na výběr měřítka zadávaného ve tvaru 1 : x, kde *x* je input. Vstup je opět ošetřen cyklem pro nekorektní vstupy (vstup menší než 0). Pokud uživatel nezadá správný vstup, dotaz se opakuje.

Dalším je výběr poloměru Země. Uživatel si může vybrat vlastní poloměr (zadávání v km), a nebo vybrat předdefinovaný poloměr 6371,11 km zadáním *0*. Nekorektní vstupy jsou opět ošetřeny cyklem (vstup menší než 0). Pokud uživatel nezadá správný vstup, dotaz se opakuje.

Poté je zavolána funkce na výpočet vzdáleností poledníků a dle výběru zobrazení funkce na výpočet vzdáleností rovnoběžek. Finálním výstupem jsou vzdálenosti poledníků od - 180° do 180° a rovnoběžek od -90° do 90° v cm. Konečně jsou výsledné hodnoty vytištěny.

## Popis průběhu
Po spuštění programu du1.py je uživateli oznámeno, o jaký program se jedná, (tj. Výpočet válcových zobrazení) a zobrazí se nápověda pro 
zkratky jednotlivých zobrazení (L - Lambertovo, A - Marinovo, B - Braunovo, M - Mercatorovo). Po zadání jedné ze zkratek následuje dotaz 
na měřítko. Poslední dotaz je na poloměr Země. Při správných vstupech program vypočítá a vypíše vzdálenosti jednotlivých rovnoběžek 
a poledníků - místo hodnoty vyšších než 100 cm a nižších než - 100 cm se vypíše '-' a program skončí.

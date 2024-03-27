# FOTO_EDIT - Python Photo Editor

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Vítejte v mém Pythonovém foto editoru!</h1>
    <p>Tento editor využívá Python a různé knihovny pro manipulaci se staženými obrázky.</p>
    <h2>Funkce editoru:</h2>
    <ul>
        <li>Otevření obrázku</li>
        <li>Přidání filtrů (černobílý, sepia, blur, atd.)</li>
        <li>Uložení upraveného obrázku</li>
    </ul>
    <h2>Pomůcky:</h2>
    <p>K vytovření tohoto editoru jsem použil pár knihoven, včetně:</p>
    <ul>
        <li><a href="https://towardsdatascience.com/2-lines-of-python-code-to-edit-photos-187dc76a84c5" target="_blank">Towards Data Science</a> -  názorná knihovna pro práci s Photoshopem v Pythonu</li>
        <li><a href="https://www.geeksforgeeks.org/python-image-editor-using-python/" target="_blank">GeeksforGeeks</a> - knihovna pro práci a manipulaci s obrázky v Pythonu</li>
    </ul>
    <h2>Ukázka Pythonového kódu:</h2>
    <pre><code>
from PIL import Image, ImageFilter
import time

# Načtení obrázku
obrazek = Image.open("dababy.jpg")   

# Aplikace filtru - například sepia filtr
filter_type == "sepia":                                      
                new_r = int((r * 0.393) + (g * 0.769) + (b * 0.189))
                new_g = int((r * 0.349) + (g * 0.686) + (b * 0.168))
                new_b = int((r * 0.272) + (g * 0.534) + (b * 0.131))
                r, g, b = min(new_r, 255), min(new_g, 255), min(new_b, 255)
                image.putpixel((x, y), (r, g, b))

# Uložení upraveného obrázku
filtrovany_obrazek.save(nazev_souboru)  

</body>
</html>

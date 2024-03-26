
from PIL import Image, ImageFilter
import time

obrazek = Image.open("dababy.jpg")                                            # Otevření vloženého obrázku 

def apply_color_filter(image, filter_type):                                   # Funkce def sloužící pro aplikaci barevného filtru na otevřený obrázek
    sirka , vyska = image.size
    for x in range(sirka):
        for y in range(vyska):
            r, g, b = image.getpixel((x, y))
            if filter_type == "invert":                                       # Filtr pro invertování barev
                r = 255 - r
                g = 255 - g
                b = 255 - b
                image.putpixel((x, y), (r, g, b))
            elif filter_type == "grayscale":                                  # Filtr pro převedení do černobílého formátu
                average = int((r + g + b) / 3)
                r, g, b = average, average, average
                image.putpixel((x, y), (r, g, b))
            elif filter_type == "sepia":                                      # Použití tzv. sepia filtru = colour correction effect
                new_r = int((r * 0.393) + (g * 0.769) + (b * 0.189))
                new_g = int((r * 0.349) + (g * 0.686) + (b * 0.168))
                new_b = int((r * 0.272) + (g * 0.534) + (b * 0.131))
                r, g, b = min(new_r, 255), min(new_g, 255), min(new_b, 255)
                image.putpixel((x, y), (r, g, b))
            elif filter_type == "brightness":                                 # Filtr pro zvětšení kontrastu (jasu) barev
                r = min(r + 50, 255)
                g = min(g + 50, 255)
                b = min(b + 50, 255)
                image.putpixel((x, y), (r, g, b))
            elif filter_type == "sepia2":                                     # # Aplikace další vylepšené varianty sepia filtru
                new_r = int((r * 0.393) + (g * 0.769) + (b * 0.189))
                new_g = int((r * 0.349) + (g * 0.686) + (b * 0.168))
                new_b = int((r * 0.272) + (g * 0.534) + (b * 0.131))
                r, g, b = min(new_r + 40, 255), min(new_g + 20, 255), min(new_b, 255)
                image.putpixel((x, y), (r, g, b))
    if filter_type == "blur":                                                 # Rozostření používaného obrázku
        image = image.filter(ImageFilter.BLUR)
    elif filter_type == "sharpen":                                            # Zaostření používaného obrázku
        image = image.filter(ImageFilter.SHARPEN)
    return image

filtr_vyber = input("Vyberte filtr (invert / grayscale / sepia / brightness / sepia2 / blur / sharpen): ").lower()       # Výběr uživatele na používaný filtr

filtrovany_obrazek = apply_color_filter(obrazek, filtr_vyber)                 # Aplikace vybraného filtru

display(filtrovany_obrazek)                                                   # Zobrazení výsledného obrázku s použitým filtrem
time.sleep(2)

ulozit = input("Chcete uložit tento obrázek? (ano/ne): ").lower()             # Uživatel si může vybrat, zda chce uložit upravený obrázek

if ulozit == "ano":
    nazev_souboru = input("Zadejte název souboru pro uložení s příponou (např. novy_obrazek.jpg): ")          # Uživatel zadá název souboru s příponou
    if nazev_souboru.strip():                                                 # Kontrola, zda je název souboru neprázdný
        filtrovany_obrazek.save(nazev_souboru)                                # Obrázek je uložen pod zadaným názvem
        print(f"Obrázek byl uložen jako {nazev_souboru}")
    else:
        print("Název souboru je prázdný. Obrázek nebyl uložen.")
else:
    print("Obrázek nebyl uložen.")



dosya_adi = "dosya.txt"

with open(dosya_adi, "w") as dosya:
    for i in range(5):
        dosya.write(input(f"dosyaya {i+1}. veriyi ekleyin") + "\n")

print(f"{dosya_adi} dosyasına veriler yazıldı.")


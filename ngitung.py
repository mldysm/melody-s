def luas_permukaantabung():
    r = int(input("Masukkan nilai jari-jari: "))
    t = int(input("Masukkan nilai tinggi: "))
    luas = 2 * 3.14 * r * (r + t)
    print("Luas permukaan tabung adalah: ", luas)
luas_permukaantabung()
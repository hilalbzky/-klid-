# Euclidean Distance Calculator

Bu Python programı, 2D uzayda verilen noktalar arasındaki Öklid mesafesini hesaplamak için geliştirilmiştir. Kullanıcı, belirlenen bir liste içerisinde noktaları tanımlar ve program, bu noktalar arasındaki tüm mesafeleri hesaplayarak en küçük mesafeyi ekrana yazdırır.

## Nasıl Çalışır?
1. **`points` Listesi**: Program, noktaları `(x, y)` formatında bir liste olarak tanımlar.
2. **`euclideanDistance` Fonksiyonu**: İki nokta arasındaki mesafeyi hesaplayan bir fonksiyon içerir.
3. **Döngü ile Hesaplama**: Tüm nokta çiftleri arasındaki mesafeleri hesaplar ve saklar.
4. **Minimum Mesafe**: Hesaplanan mesafeler arasından en küçük olanını bulur ve sonucu ekrana yazdırır.

## Örnek Kullanım:
Eğer `points` listesi aşağıdaki gibi tanımlanırsa:

```python
points = [(1, 2), (4, 6), (5, 1), (0, 0), (3, 4)]
```
Programın çıktısı şu şekilde olur:

```
(1, 2) ile (4, 6) arasındaki mesafe: 5.00
(1, 2) ile (5, 1) arasındaki mesafe: 4.12
...
En küçük mesafe: 2.24
```

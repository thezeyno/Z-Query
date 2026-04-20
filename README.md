# 🚀 Z-Query — No-SQL Data Query Engine

## 🇹🇷 Türkçe

### 📌 Proje Hakkında

Z-Query, Streamlit ve Python kullanılarak geliştirilmiş etkileşimli bir veri sorgulama uygulamasıdır.

Kullanıcılar CSV dosyalarını yükleyerek, SQL yazmadan doğal ve basit ifadelerle veri filtreleme işlemleri gerçekleştirebilir.

---

### ✨ Öne Çıkan Özellikler

- 📂 CSV dosyası yükleme
- 📊 Anlık veri önizleme
- 📈 Veri özeti (satır, sütun, eksik veri)
- 🔍 Sütun isimlerini otomatik gösterme
- 🧠 SQL’siz sorgulama (AND / OR destekli)
- ⚡ Hızlı filtreleme (pandas query engine)
- 📥 Sonuçları CSV olarak indirme

---

### 🧪 Örnek Sorgular

```txt
yas > 25
sehir == "Ankara"
fiyat > 100 AND kategori == "Elektronik"
kategori != "Gıda"
```
---

### 🖥️ Arayüz

Uygulama Streamlit ile geliştirilmiştir ve tamamen kullanıcı dostu bir arayüze sahiptir.

---

### 🛠️ Kullanılan Teknolojiler

- Python 3
- Streamlit
- Pandas

---

### ⚙️ Kurulum ve Çalıştırma

```txt
git clone https://github.com/thezeyno/Z-Query
cd z-query
pip install streamlit pandas
streamlit run app.py
```
---

### 🎯 Amaç

Bu proje:

- SQL mantığını basitleştirmek
- Veri analizi sürecini hızlandırmak
- Kullanıcı dostu veri filtreleme deneyimi sunmak

amacıyla geliştirilmiştir.

---

### 🔮 Geliştirme Fikirleri
- Parantez desteği ( )
- NOT operatörü
- Grafiksel veri görselleştirme
- Çoklu dosya desteği
- Daha gelişmiş query parser

---

## 🇬🇧 English

### 📌 About the Project

Z-Query is an interactive data querying application built with Streamlit and Python.

It allows users to filter data using simple expressions without writing SQL.

---

### ✨ Features
- Upload CSV files
- Data preview
- Data summary (rows, columns, missing values)
- Auto-detected column names
- SQL-free querying (AND / OR support)
- Fast filtering using pandas
- Export results as CSV

---

### 🧪 Example Queries

```txt
age > 25
city == "Ankara"
price > 100 AND category == "Electronics"
category != "Food"
```
---

### 🛠️ Technologies

- Python 3
- Streamlit
- Pandas

---

### ⚙️ Installation

```txt
git clone https://github.com/thezeyno/Z-Query
cd z-query
pip install streamlit pandas
streamlit run app.py
```
---

### 🎯 Purpose

The goal of this project is to simplify data querying and demonstrate how filtering systems work without SQL.

---

### ⭐Bu projeyi beğendiyseniz, lütfen bir yıldız verin!

### ⭐ If you like this project, consider giving it a star!

---

## 👩‍💻 Author

**Zeynep Coşkuner**  
[GitHub Profile](https://github.com/thezeyno)
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Z-Query Engine", layout="wide")

st.title("🚀 Z-Query: SQL'siz Veri Sorgulama")
st.write("CSV dosyanı yükle ve doğal dille sorgula!")

# 1. Dosya Yükleme
uploaded_file = st.file_uploader("Bir CSV dosyası seçin", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Veri Önizleme (İlk 5 Satır)", df.head())

    # --- YENİ: Veri Özeti (Dashboard) ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Toplam Satır", len(df))
    col2.metric("Sütun Sayısı", len(df.columns))
    col3.metric("Eksik Veri", int(df.isnull().sum().sum())) # Toplam boş hücre sayısı

    st.markdown("---") # Araya bir çizgi çekelim şık durur

    # --- YENİ: Yardımcı Sütun Listesi ---
    st.write("### 🔍 Kullanılabilir Sütunlar ve Tipleri")
    st.info(", ".join([f"{col} ({dtype})" for col, dtype in zip(df.columns, df.dtypes)]))

    # 2. Sorgu Girişi
    query_input = st.text_input("Sorgunuzu yazın (Örn: fiyat > 100 AND kategori == 'Elektronik')", "")

    if query_input:
        try:
            # Pandas .query() fonksiyonu bizim 'Mini Engine' görevini üstlenecek
            # Kullanıcı 'AND' yazarsa bunu '&' işaretine, 'OR' yazarsa '|' işaretine çevirebiliriz
            processed_query = query_input.replace(" AND ", " & ").replace(" OR ", " | ")
            
            result = df.query(processed_query)
            
            st.success(f"Bulunan Kayıt Sayısı: {len(result)}")
            st.dataframe(result) # Sonuçları tablo olarak göster
            
            # --- SONUÇLARI İNDİRME BUTONU ---
            st.markdown("---")
            csv_dosya = result.to_csv(index=False).encode('utf-8')
            st.download_button(
            label="📥 Filtrelenmiş Veriyi CSV Olarak İndir",
            data=csv_dosya,
            file_name='sorgu_sonucu.csv',
            mime='text/csv',
        )
        except Exception as e:
            st.error(f"Hata: Sorgu formatı geçersiz. Lütfen sütun isimlerini ve operatörleri kontrol edin. \nDetay: {e}")

# 3. Yan Menü (Bilgi Paneli)
st.sidebar.header("Nasıl Kullanılır?")
st.sidebar.info("""
- Sayısal: `yas > 25`
- Metinsel: `sehir == 'Ankara'`
- Çoklu: `yas > 20 AND sehir == 'İstanbul'`
- Eşit değil: `kategori != 'Gıda'`
""")
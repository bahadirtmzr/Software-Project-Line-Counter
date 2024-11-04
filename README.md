# Software-Project-Line-Counter
Dizinde bulunan projelerin kaynak kod sayısını alır, açıklama satırlarını saymaz.
Gerekli Kütüphaneler
Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

pandas
openpyxl
Bu kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
pip install pandas openpyxl

Kullanım Kılavuzu
Projelerinizi Yerel Olarak Hazırlayın: count_lines.py dosyasındaki BASE_DIR değişkenini, kodlarını saymak istediğiniz projelerin bulunduğu dizinle güncelleyin.

python
Kodu kopyala
BASE_DIR = '/path/to/your/projects'
Uygulamayı Çalıştırın: Terminal veya komut istemcisinde projenin dizinine gidin ve aşağıdaki komutu çalıştırın:

bash
Kodu kopyala
python3 count_lines.py
Sonuçları İnceleyin: Çalıştırdıktan sonra, project_lines_summary.xlsx adında bir Excel dosyası oluşturulacak. Bu dosya, projelerinizin toplam kod satırı sayısını ve kullanılan teknolojileri içerecektir.

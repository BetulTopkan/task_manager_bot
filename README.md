Task Manager Bot

📋 Discord Görev Yönetici Botu

Bu bot, Discord sunucularında küçük ekipler için görev yönetimini kolaylaştırmak amacıyla tasarlanmıştır.

🚀 Özellikler

✅ Görev ekleme

❌ Görev silme

📄 Görevleri listeleme

✔️ Görevleri tamamlandı olarak işaretleme

⚙️ Kurulum

Python 3.8 veya daha yeni bir sürüm yükleyin.

Gerekli paketleri yükleyin:

pip install -r requirements.txt

Discord Developer Portal’dan bir bot oluşturun:

Discord Developer Portal’a gidin

“New Application” butonuna tıklayın

Bot sekmesine gidip “Add Bot” butonuna tıklayın

Bot token’ını kopyalayın

bot.py dosyasında YOUR_BOT_TOKEN yerine kendi bot token’ınızı ekleyin.

Botu çalıştırın:

python bot.py

💬 Bot Komutları

!add_task <açıklama> → Yeni görev ekler

Örnek: !add_task Haftalık raporu hazırla

!delete_task <görev_id> → Belirtilen ID’ye sahip görevi siler

Örnek: !delete_task 1

!show_tasks → Tüm görevleri listeler

!complete_task <görev_id> → Belirtilen ID’ye sahip görevi tamamlandı olarak işaretler

Örnek: !complete_task 1

🗂️ Veritabanı

Bot, görevleri SQLite veritabanında saklar. Veritabanı otomatik olarak oluşturulur ve şu bilgileri içerir:

📌 Görev ID

📝 Görev açıklaması

✅ Tamamlanma durumu

✅ Testleri Çalıştırma

Tüm testleri çalıştırmak için:

python run_tests.py

veya

python -m unittest discover tests


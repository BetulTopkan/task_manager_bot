# Discord Görev Yönetim Botu

Bu bot, Discord sunucularında görev yönetimi için kullanılan bir araçtır. Küçük ekipler için görev ekleme, silme, görüntüleme ve tamamlama işlemlerini kolaylaştırır.
![image](https://github.com/user-attachments/assets/776cce1b-84e6-4baa-ace7-355fa25f146e)

## Özellikler

- Görev ekleme (!add_task)
- Görev silme (!delete_task)
- Görevleri görüntüleme (!show_tasks)
- Görev tamamlama (!complete_task)

## Kurulum

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

2. `.env` dosyası oluşturun ve Discord bot token'ınızı ekleyin:

```
DISCORD_TOKEN=your_bot_token_here
```

3. Botu çalıştırın:

```bash
python bot.py
```

## Testler

Testleri çalıştırmak için:

```bash
python -m pytest tests/
```

## Komutlar

- `!add_task <açıklama>` - Yeni bir görev ekler
- `!delete_task <görev_id>` - Belirtilen ID'ye sahip görevi siler
- `!show_tasks` - Tüm görevleri listeler
- `!complete_task <görev_id>` - Belirtilen ID'ye sahip görevi tamamlandı olarak işaretler

## Veritabanı

Tüm veriler SQLite veritabanında saklanır. Veritabanı otomatik olarak oluşturulur ve `tasks.db` dosyasında tutulur.

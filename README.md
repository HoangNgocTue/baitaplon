## Cài Đặt

1. Clone repo:

```bash
git clone https://github.com/HoangNgocTue/baitaplon.git
cd baitaplon
```

2. Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

requirements.txt
```bash
requests
beautifulsoup4
pandas
schedule
```


## Cách chạy

```bash
python kenh14.py
```

## Tùy chỉnh
Thay đổi số trang cần crawl:
```python
quet_trang(max_pages=5)  
```

## Thay đổi thời gian tự động chạy:
```python
schedule.every().day.at("06:00").do(lambda: quet_trang(max_pages=5)) 
```
## Kết quả

kenh14_suckhoe.csv

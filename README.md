## Cài Đặt

1. Clone repo:

```bash
git clone https://github.com/your-username/kenh14-suckhoe-crawler.git
cd kenh14-suckhoe-crawler
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
crawl_all_pages(max_pages=5)  
```

## Thay đổi thời gian tự động chạy:
```python
schedule.every().day.at("06:00").do(lambda: crawl_all_pages(max_pages=5)) 
```
## Kết quả

kenh14_suckhoe.csv

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule

BASE_URL = "https://kenh14.vn"
CATEGORY_PATH = "/suc-khoe.chn"

def get_article_links(page_url):
    res = requests.get(page_url)
    if res.status_code != 200:
        return []
    soup = BeautifulSoup(res.content, 'html.parser')
    items = soup.select("div.knswli-left")
    links = []
    for art in items:
        a = art.find("a", href=True)
        if a:
            links.append(BASE_URL + a["href"])
    return links

#  Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) 
def get_article_data(article_url):

    res = requests.get(article_url)
    if res.status_code != 200:
        return None
    soup = BeautifulSoup(res.content, 'html.parser')

    h1 = soup.find("h1", class_="kbwc-title")
    title = h1.get_text(strip=True) if h1 else ""

    h2 = soup.find("h2", class_="knc-sapo")
    summary = h2.get_text(strip=True) if h2 else ""

    content_div = soup.find("div", class_="detail-content afcbc-body", attrs={"data-role": "content"})
    paras = [p.get_text(strip=True) for p in content_div.find_all("p")] if content_div else []
    content = "\n\n".join(paras)

    body_images = []
    if content_div:
        for img in content_div.find_all("img"):
            src = img.get("data-original") or img.get("src")
            if src:
                body_images.append(src.strip())
    for img in soup.find_all("img", rel="lightbox"):
        src = img.get("data-original") or img.get("src")
        if src and src.strip() not in body_images:
            body_images.append(src.strip())
    images = ";".join(body_images)

    return {
        "title":   title,
        "summary": summary,
        "content": content,
        "images":  images
    }

# Lấy tất cả dữ liệu của các trang.
def quet_trang(max_pages=5):
    records = []
    for page in range(1, max_pages + 1):
        page_url = f"{BASE_URL}{CATEGORY_PATH}?page={page}"
        print(f"trang {page}")
        links = get_article_links(page_url)
        for url in links:
            print("bài:", url)
            data = get_article_data(url)
            if data:
                records.append(data)
            time.sleep(1)
# tạo và lưu dữ liệu excel
    df = pd.DataFrame.from_records(records)
    df = df[["title", "summary", "content", "images"]]
    df.to_csv("kenh14_suckhoe.csv", sep=';', index=False, encoding="utf-8-sig")
    print("Đã lưu vào kenh14_suckhoe.csv")

if __name__ == "__main__":
    quet_trang(max_pages=1) # chổ này chọn giới hạn số trang cần lấy thông tin


    schedule.every().day.at("06:00").do(lambda: quet_trang(max_pages=5)) # chạy mỗi ngày lúc 6h00
    while True:
        schedule.run_pending()
        time.sleep(60)

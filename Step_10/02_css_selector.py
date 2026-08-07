from bs4 import BeautifulSoup

# 模擬包含層級與樣式類別的複雜 HTML 結構
html_doc = """
<div id="content">
    <div class="card product-card" data-id="101">
        <h2 class="title">MacBook Pro</h2>
        <span class="price">$ 1,299</span>
        <span class="status in-stock">有現貨</span>
    </div>
    <div class="card product-card" data-id="102">
        <h2 class="title">iPad Air</h2>
        <span class="price">$ 599</span>
        <span class="status out-of-stock">缺貨中</span>
    </div>
</div>
"""

soup = BeautifulSoup(html_doc, "html.parser")


# 使用 select_one() 抓取單一元素 (# 代表 ID，. 代表 Class)
print("=== 1. 使用 ID 與 Class 精準定位 ===")
main_content = soup.select_one("#content")
first_product_title = soup.select_one("div.product-card > h2.title").text
print(f"第一個商品名稱：{first_product_title}")

# 使用 select() 抓取所有符合條件的清單 (回傳列表)
print("\n=== 2. 爬取所有商品卡片資料 ===")
cards = soup.select(".product-card")

for card in cards:
    # 在個別卡片內部繼續使用 select_one 尋找標籤
    title = card.select_one(".title").text
    price = card.select_one(".price").text
    status = card.select_one(".status").text
    product_id = card["data-id"]  # 抓取自訂屬性 data-id
    
    print(f"[{product_id}] 商品：{title:<12} | 價格：{price:<8} | 狀態：{status}")
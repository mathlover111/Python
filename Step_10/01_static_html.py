from bs4 import BeautifulSoup

# 模擬一段從網站抓下來的 HTML 原始碼字串
html_doc = """
<html>
    <head><title>測試購物網站</title></head>
    <body>
        <h1 class="main-title">熱門商品清單</h1>
        <div class="product-list">
            <p class="product-item">蘋果 - $35</p>
            <p class="product-item">香蕉 - $20</p>
            <a href="https://example.com/buy" class="buy-link">前往購買頁面</a>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print("=== 1. 取得標籤文字 ===")
print("網頁 Title 標籤：", soup.title)
print("網頁 Title 文字：", soup.title.string)
print("主標題 H1 文字：", soup.h1.string)

# 使用 find() 尋找單一元素，與 find_all() 搜尋所有符合條件的元素
print("\n=== 2. 搜尋所有商品 (p 標籤) ===")
items = soup.find_all("p", class_="product-item")
for item in items:
    print("找到商品：", item.text)

# 擷取超連結屬性 (href)
print("\n=== 3. 擷取超連結網址 ===")
link = soup.find("a", class_="buy-link")
print("連結文字：", link.text)
print("連結 URL (href)：", link["href"])
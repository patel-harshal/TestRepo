from fastapi import FastAPI
from amazon_paapi import AmazonApi

app = FastAPI()

amazon = AmazonApi(
    access_key="AKPA5WYG9Q1766119407",
    secret_key="UVoNQSJ48DWNofmuizWKhFSDXaqxU08aWVJRVj2g",
    associate_tag="database21-21",
    country="IN"
)

@app.get("/product")
def get_product(asin: str):

    items = amazon.get_items([asin])

    if not items.items:
        return {"error": "Product not found"}

    item = items.items[0]

    return {
        "asin": asin,
        "title": item.item_info.title.display_value,
        "price": item.offers.listings[0].price.display_amount if item.offers else "N/A",
        "image": item.images.primary.large.url if item.images else "",
        "affiliate_link": item.detail_page_url
    }

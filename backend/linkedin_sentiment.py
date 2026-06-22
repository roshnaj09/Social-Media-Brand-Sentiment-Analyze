from playwright.sync_api import sync_playwright
from transformers import pipeline
import re

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def clean(text):
    return re.sub(r"\n", " ", text).strip()

all_texts = []

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    print("\nOpening LinkedIn...\n")

    page.goto(
        "https://www.linkedin.com/company/ajiolife/",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    links = page.locator("a").evaluate_all(
        "els => els.map(e => e.href)"
    )

    post_links = []

    for link in links:

        if (
            link
            and "/posts/" in link
        ):

            if link not in post_links:

                post_links.append(link)

    post_links = post_links[:6]

    print(
        f"Posts Found: {len(post_links)}"
    )

    for i, post in enumerate(post_links):
        try:

            print(
                f"\nOpening Post {i+1}"
            )

            page.goto(
                post,
                timeout=60000
            )

            page.wait_for_timeout(
                8000
            )

            text = clean(
                page.inner_text("body")
            )

            if "Like Comment Share" in text:

                comments_part = text.split(
                    "Like Comment Share",
                    1
                )[1]

            else:

                comments_part = text

            print("\nCOMMENTS SAMPLE:\n")

            print(
                comments_part
            )

            print(
                f"Text Length: {len(comments_part)}"
            )

            all_texts.append(
                comments_part[:1500]
            )
        except Exception as e:

            print(
                "Error:",
                e
            )

positive = 0
negative = 0

for text in all_texts:

    try:

        result = sentiment(
            text[:512]
        )[0]

        label = result["label"]

        print(
            "\nResult:",
            label
        )

        if label == "POSITIVE":
            positive += 1
        else:
            negative += 1

    except:
        pass

print("\nSUMMARY\n")

print("Positive:", positive)
print("Negative:", negative)
from playwright.sync_api import sync_playwright


def find_instagram(url):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        try:
            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=80000
            )
        except Exception as e:
            print("Warning:", e)

        page.wait_for_timeout(5000)

        page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

        page.wait_for_timeout(3000)

        links = page.locator("a").evaluate_all(
            "els => els.map(e => e.href)"
        )

        print(f"Total links found: {len(links)}")

        browser.close()

        return [
            link for link in links
            if link and "instagram.com" in link
        ]


if __name__ == "__main__":

    result = find_instagram(
        "https://www.ajio.com"
    )

    print("\nInstagram Links Found:\n")

    for link in result:
        print(link)
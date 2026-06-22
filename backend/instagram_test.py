from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.instagram.com/AJIOlife/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    links = page.locator("a").evaluate_all(
        "els => els.map(e => e.href)"
    )

    post_links = []

    for link in links:
        if link and "/p/" in link:
            if link not in post_links:
                post_links.append(link)

    print("\nLatest Posts:\n")

    for post in post_links[:6]:
        print(post)

    input("Press Enter to close...")
    browser.close()
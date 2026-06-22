from playwright.sync_api import sync_playwright

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

    page.wait_for_timeout(
        10000
    )

    print(
        "Title:",
        page.title()
    )

    print(
        "URL:",
        page.url
    )

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

                post_links.append(
                    link
                )

    print(
        f"\nPosts Found: {len(post_links)}\n"
    )

    for post in post_links[:6]:

        print(post)

    input(
        "\nPress Enter to close..."
    )
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.instagram.com/accounts/login/")

    input(
        "\nLog into Instagram manually.\n"
        "When login is complete press ENTER...\n"
    )

    context.storage_state(
        path="backend/sessions/instagram.json"
    )

    print(
        "\nInstagram session saved!"
    )

    browser.close()
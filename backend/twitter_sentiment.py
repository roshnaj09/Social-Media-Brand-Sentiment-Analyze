from playwright.sync_api import sync_playwright
from transformers import pipeline

# Sentiment Model
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(
        user_data_dir=r"C:\Users\roshn\AppData\Local\BraveSoftware\Brave-Browser\User Data",
        channel="chrome",
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://x.com/AJIOLife",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    links = page.locator("a").evaluate_all(
        "els => els.map(e => e.href)"
    )

    tweet_links = []

    for link in links:

        if (
            link
            and "/status/" in link
            and "/photo/" not in link
            and "/quotes" not in link
            and "/analytics" not in link
        ):

            if link not in tweet_links:
                tweet_links.append(link)

    print("\nLatest Tweets:\n")

    for tweet in tweet_links:
        print(tweet)

    print(
        "\nTweets Found:",
        len(tweet_links)
    )

    all_comments = []

    for tweet_num, tweet_url in enumerate(
        tweet_links,
        start=1
    ):

        print(
            f"\nOpening Tweet {tweet_num}\n"
        )

        page.goto(
            tweet_url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        for _ in range(30):

            page.mouse.wheel(
                0,
                4000
            )

            page.wait_for_timeout(
                2000
            )

        articles = page.locator(
            "article"
        )

        print(
            "Articles Found:",
            articles.count()
        )

        comments = []

        for i in range(
            1,
            articles.count()
        ):

            try:

                text = articles.nth(
                    i
                ).inner_text()

                if len(text) > 20:

                    comments.append(
                        text
                    )

            except:
                pass

        print(
            "\nCOMMENTS FOUND:\n"
        )

        for num, comment in enumerate(
            comments,
            start=1
        ):

            print(
                f"\n{num}."
            )

            print(
                comment[:300]
            )

        print(
            "\nTotal Comments:",
            len(comments)
        )

        all_comments.extend(
            comments
        )

        print(
            f"Running Total: {len(all_comments)}"
        )

    print(
        "\nFINAL TOTAL COMMENTS:",
        len(all_comments)
    )

    # Remove duplicates
    all_comments = list(
        set(all_comments)
    )

    print(
        "\nUNIQUE COMMENTS:",
        len(all_comments)
    )

    print(
        "\nSENTIMENT ANALYSIS\n"
    )

    positive = 0
    negative = 0

    for comment in all_comments:

        try:

            result = sentiment(
                comment[:512]
            )[0]

            label = result["label"]

            score = round(
                result["score"],
                2
            )

            print("\nComment:")
            print(comment[:300])

            print(
                f"Result: {label}"
            )

            print(
                f"Confidence: {score}"
            )

            if label == "POSITIVE":

                positive += 1

            else:

                negative += 1

        except:
            pass

    total = positive + negative

    print(
        "\n" + "=" * 60
    )

    print(
        "\nSUMMARY\n"
    )

    print(
        "Positive:",
        positive
    )

    print(
        "Negative:",
        negative
    )

    if total:

        print(
            "Positive %:",
            round(
                positive / total * 100,
                2
            )
        )

        print(
            "Negative %:",
            round(
                negative / total * 100,
                2
            )
        )

    input(
        "\nPress Enter..."
    )
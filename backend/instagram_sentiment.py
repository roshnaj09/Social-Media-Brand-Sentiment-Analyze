from playwright.sync_api import sync_playwright
from transformers import pipeline
import re


# Sentiment Model
sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def clean(text):
    return re.sub(
        r"\n",
        " ",
        text
    ).strip()


all_comments = []


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context(
        storage_state="backend/sessions/instagram.json"
    )

    page = context.new_page()

    print("\nOpening Instagram...\n")

    page.goto(
        "https://www.instagram.com/ajiolife/",
        timeout=60000,
        wait_until="domcontentloaded"
    )
    print("Current URL:", page.url)
    page.screenshot(path="test.png")

    page.wait_for_timeout(
        5000
    )

    print(
        "Current URL:",
        page.url
    )
    print("Still alive")

    page.wait_for_timeout(10000)

    print("Passed timeout")

    # Extract post links
    links = page.locator(
        "a"
    ).evaluate_all(
        "els=>els.map(e=>e.href)"
    )

    posts = []

    for link in links:
        if (
            link
            and "/p/" in link
        ):

            if link not in posts:

                posts.append(
                    link
                )

    posts = posts[:6]

    print(
        f"Posts Found: {len(posts)}"
    )

    # Open each post
    for i, post in enumerate(posts):

        try:

            print(
                f"\n{'='*50}"
            )

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

            # Load more comments
            for _ in range(10):

                try:

                    btn = page.locator(
                        "text=more comments"
                    )

                    if btn.count():

                        btn.last.click()

                        page.wait_for_timeout(
                            2500
                        )

                except:

                    break

            page.mouse.wheel(
                0,
                8000
            )

            page.wait_for_timeout(
                5000
            )

            spans = page.locator(
                "span"
            )

            comments = []

            for j in range(
                spans.count()
            ):

                try:

                    text = spans.nth(
                        j
                    ).inner_text()

                    text = clean(
                        text
                    )

                    if (
                        len(text)
                        > 15
                    ):

                        comments.append(
                            text
                        )

                except:
                    pass

            comments = list(
                set(comments)
            )

            print(
                f"\nComments from Post {i+1}\n"
            )

            for num, c in enumerate(
                comments,
                start=1
            ):

                print(
                    f"{num}. {c}"
                )

            print(
                f"\nTotal Comments: {len(comments)}"
            )

            all_comments.extend(
                comments
            )

        except Exception as e:

            print(
                "Error:",
                e
            )



# Remove duplicates
all_comments = list(
    set(all_comments)
)

print(
    "\n"
    + "="*60
)

print(
    "\nTOTAL COMMENTS:",
    len(
        all_comments
    )
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

        label = result[
            "label"
        ]

        score = round(
            result[
                "score"
            ],
            2
        )

        print(
            f"\nComment:"
        )

        print(
            comment
        )

        print(
            f"Result: "
            f"{label}"
        )

        print(
            f"Confidence:"
            f" {score}"
        )

        if (
            label
            ==
            "POSITIVE"
        ):

            positive += 1

        else:

            negative += 1

    except:

        pass


total = (
    positive
    +
    negative
)

print(
    "\n"
    + "="*60
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
            (
                positive
                /
                total
            )
            *
            100,
            2
        )
    )

    print(
        "Negative %:",
        round(
            (
                negative
                /
                total
            )
            *
            100,
            2
        )
    )
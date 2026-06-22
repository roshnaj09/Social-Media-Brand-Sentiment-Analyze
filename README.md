# Social Media Brand Sentiment Analysis

A Python-based application to analyze brand sentiment across multiple social media platforms including Instagram, LinkedIn, and Twitter.

## Features

- **Multi-Platform Support**: Analyze sentiment from Instagram, LinkedIn, and Twitter
- **Sentiment Analysis**: Automatically classify and analyze sentiment of social media posts
- **Data Scraping**: Collect data from various social media platforms
- **Dashboard**: Visual representation of sentiment trends and analytics

## Project Structure

```
.
├── backend/
│   ├── instagram_sentiment.py    # Instagram sentiment analysis
│   ├── instagram_test.py         # Instagram tests
│   ├── linkedin_sentiment.py     # LinkedIn sentiment analysis
│   ├── linkedin_test.py          # LinkedIn tests
│   ├── twitter_sentiment.py      # Twitter sentiment analysis
│   ├── twitter_test.py           # Twitter tests
│   ├── scraper.py                # Web scraping utilities
│   └── backend/
│       └── save_instagram_session.py
├── dashboard/                    # Frontend/Dashboard files
├── data/                         # Data storage
├── sessions/                     # Session management
└── README.md
```

## Requirements

- Python 3.8+
- Virtual Environment (venv)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/roshnaj09/Social-Media-Brand-Sentiment-Analyze.git
cd Social-Media-Brand-Sentiment-Analyze
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Instagram Sentiment Analysis
```bash
python backend/instagram_sentiment.py
```

### LinkedIn Sentiment Analysis
```bash
python backend/linkedin_sentiment.py
```

### Twitter Sentiment Analysis
```bash
python backend/twitter_sentiment.py
```

### Run Tests
```bash
python backend/instagram_test.py
python backend/linkedin_test.py
python backend/twitter_test.py
```

## Configuration

Session files are stored in the `sessions/` directory:
- `instagram.json` - Instagram session configuration
- `twitter.json` - Twitter session configuration

## Data

Analyzed data is stored in the `data/` directory for later reference and analysis.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or feedback, please reach out to roshnaj09 on GitHub.

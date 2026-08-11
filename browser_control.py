from playwright.sync_api import sync_playwright
import urllib.parse


class BrowserController:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    # =========================================================
    # START BROWSER
    # =========================================================

    def start(self):
        try:
            if self.browser:
                return True

            self.playwright = sync_playwright().start()

            self.browser = self.playwright.chromium.launch(
                headless=False
            )

            self.context = self.browser.new_context()

            self.page = self.context.new_page()

            return True

        except Exception as e:
            print("Browser start error:", e)
            return False

    # =========================================================
    # OPEN WEBSITE
    # =========================================================

    def open(self, website):
        try:
            if not self.start():
                return "Unable to start browser."

            website = website.strip()

            if not website:
                return "Please provide a website."

            if not website.startswith(("http://", "https://")):
                website = "https://" + website

            self.page.goto(
                website,
                wait_until="commit",
                timeout=15000
            )

            return f"Opened {website}"

        except Exception as e:
            return f"Browser open error: {e}"

    # =========================================================
    # GOOGLE SEARCH
    # =========================================================

    def search_google(self, query):
        try:
            if not self.start():
                return "Unable to start browser."

            query = query.strip()

            if not query:
                return "Please provide a search query."

            encoded_query = urllib.parse.quote_plus(query)

            url = (
                "https://www.google.com/search?q="
                + encoded_query
            )

            self.page.goto(
                url,
                wait_until="commit",
                timeout=15000
            )

            return f"Searching Google for {query}"

        except Exception as e:
            return f"Google search error: {e}"

    # =========================================================
    # YOUTUBE SEARCH
    # =========================================================

    def search_youtube(self, query):
        try:
            if not self.start():
                return "Unable to start browser."

            query = query.strip()

            if not query:
                return "Please provide a YouTube search."

            encoded_query = urllib.parse.quote_plus(query)

            url = (
                "https://www.youtube.com/results?search_query="
                + encoded_query
            )

            self.page.goto(
                url,
                wait_until="commit",
                timeout=15000
            )

            return f"Searching YouTube for {query}"

        except Exception as e:
            return f"YouTube search error: {e}"

    # =========================================================
    # NEW TAB
    # =========================================================

    def new_tab(self, website):
        try:
            if not self.start():
                return "Unable to start browser."

            website = website.strip()

            if not website.startswith(("http://", "https://")):
                website = "https://" + website

            new_page = self.context.new_page()

            new_page.goto(
                website,
                wait_until="commit",
                timeout=15000
            )

            self.page = new_page

            return f"Opened new tab: {website}"

        except Exception as e:
            return f"New tab error: {e}"

    # =========================================================
    # CLOSE TAB
    # =========================================================

    def close_tab(self):
        try:
            if self.page:
                self.page.close()

            pages = self.context.pages if self.context else []

            if pages:
                self.page = pages[-1]

            return "Tab closed."

        except Exception as e:
            return f"Close tab error: {e}"

    # =========================================================
    # REFRESH
    # =========================================================

    def refresh(self):
        try:
            if not self.page:
                return "No browser page is open."

            self.page.reload(
                wait_until="commit",
                timeout=15000
            )

            return "Page refreshed."

        except Exception as e:
            return f"Refresh error: {e}"

    # =========================================================
    # GO BACK
    # =========================================================

    def back(self):
        try:
            if not self.page:
                return "No browser page is open."

            self.page.go_back(
                wait_until="commit",
                timeout=15000
            )

            return "Went back."

        except Exception as e:
            return f"Back error: {e}"

    # =========================================================
    # GO FORWARD
    # =========================================================

    def forward(self):
        try:
            if not self.page:
                return "No browser page is open."

            self.page.go_forward(
                wait_until="commit",
                timeout=15000
            )

            return "Went forward."

        except Exception as e:
            return f"Forward error: {e}"

    # =========================================================
    # GET CURRENT URL
    # =========================================================

    def current_url(self):
        try:
            if not self.page:
                return "No browser page is open."

            return self.page.url

        except Exception as e:
            return f"URL error: {e}"

    # =========================================================
    # CLOSE BROWSER
    # =========================================================

    def close(self):
        try:
            if self.browser:
                self.browser.close()

            if self.playwright:
                self.playwright.stop()

            self.browser = None
            self.context = None
            self.page = None
            self.playwright = None

            return "Browser closed."

        except Exception as e:
            return f"Browser close error: {e}"
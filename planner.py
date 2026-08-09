def create_plan(task):
    task = task.lower().strip()

    # ---------- Chrome + Google Search ----------
    if "chrome" in task and ("search" in task or "google" in task):
        query = task

        query = query.replace("open chrome", "")
        query = query.replace("search", "")
        query = query.replace("google", "")
        query = query.replace("chrome", "")

        query = query.strip()

        return [
            "Open Chrome",
            "Go to Google",
            f"Search: {query}"
        ]

    # ---------- Google Search ----------
    elif "google" in task or "search" in task:
        query = task.replace("google", "").replace("search", "").strip()

        return [
            "Open Chrome",
            "Go to Google",
            f"Search: {query}"
        ]

    # ---------- YouTube Search ----------
    elif "youtube" in task:
        query = task.replace("youtube", "").replace("search", "").strip()

        return [
            "Open YouTube",
            f"Search: {query}"
        ]

    # ---------- Chrome ----------
    elif "chrome" in task or "browser" in task:
        return [
            "Open Chrome",
            "Wait 2 seconds"
        ]

    # ---------- Default ----------
    else:
        return [
            "Think",
            "Answer using AI"
        ]
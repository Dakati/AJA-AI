def create_plan(task):
    task = task.lower()

    if "chrome" in task or "browser" in task:
        return [
            "Open Chrome",
            "Wait 2 seconds"
        ]

    elif "google" in task or "search" in task:
        return [
            "Open Chrome",
            "Go to Google",
            "Search: " + task
        ]

    elif "youtube" in task:
        return [
            "Open YouTube",
            "Search: " + task
        ]

    else:
        return [
            "Think",
            "Answer using AI"
        ]
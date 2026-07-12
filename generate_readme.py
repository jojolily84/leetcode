import os
import json
import urllib.request
import time
import re

README_PATH = "README.md"
LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

def get_problem_info(slug):
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        difficulty
        topicTags {
          name
        }
      }
    }
    """
    payload = json.dumps({"query": query, "variables": {"titleSlug": slug}}).encode()
    req = urllib.request.Request(
        LEETCODE_GRAPHQL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://leetcode.com",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            q = data.get("data", {}).get("question")
            if q:
                return {
                    "id": int(q["questionFrontendId"]),
                    "title": q["title"],
                    "difficulty": q["difficulty"],
                    "topics": ", ".join(t["name"] for t in q["topicTags"]),
                    "slug": slug,
                }
    except Exception as e:
        print(f"  Warning: failed to fetch {slug}: {e}")
    return None

def get_lang_ext(filename):
    return filename.rsplit(".", 1)[-1] if "." in filename else "?"

def is_problem_folder(name):
    # Match folders like 0001-two-sum or two-sum
    return os.path.isdir(name) and not name.startswith(".") and name not in ("__pycache__",)

def extract_slug(folder_name):
    # Remove leading number prefix like "0001-"
    return re.sub(r"^\d+-", "", folder_name)

def main():
    entries = sorted(os.listdir("."))
    problem_folders = [e for e in entries if is_problem_folder(e) and re.match(r"^\d+-", e)]
    print(f"Found {len(problem_folders)} problem folders")

    rows = []
    for folder in problem_folders:
        files = [f for f in os.listdir(folder) if not f.startswith(".")]
        if not files:
            continue
        lang = get_lang_ext(files[0])
        slug = extract_slug(folder)

        print(f"Fetching: {slug}")
        info = get_problem_info(slug)
        if info:
            info["lang"] = lang
            rows.append(info)
        time.sleep(0.5)

    rows.sort(key=lambda x: x["id"])

    table_lines = [
        "## 📋 Problem List\n",
        "| # | Title | Lang | Topic | Difficulty |",
        "|---|-------|------|-------|------------|",
    ]
    for r in rows:
        link = f"[{r['title']}](https://leetcode.com/problems/{r['slug']}/)"
        table_lines.append(f"| {r['id']} | {link} | {r['lang']} | {r['topics']} | {r['difficulty']} |")

    table_str = "\n".join(table_lines)

    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        if "## 📋 Problem List" in content:
            before = content[:content.index("## 📋 Problem List")]
            content = before.rstrip() + "\n\n" + table_str + "\n"
        else:
            content = content.rstrip() + "\n\n" + table_str + "\n"
    else:
        content = table_str + "\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README updated with {len(rows)} problems.")

if __name__ == "__main__":
    main()

import re


def read_file(filepath: str) -> dict:
    """reads file from input filepath and returns a dict with the file content and contentFormat for the publish payload"""
    f = open(filepath, "r")
    content = f.read()
    # Hugo markdown pattern
    match = re.search(r'title: "(.*?)"', content)
    if match:
        title = match.group(1)
        pattern = "^---\n.*---\n"  # pattern to match the front matter
        content = re.sub(pattern, "", content, flags=re.M | re.S)
        content = "# " + title + "\n" + content
    if not f.closed:
        f.close()

    if filepath.find(".") < 0:
        file_ext = ""
    else:
        file_ext = filepath[filepath.find(".") + 1 :]
    if file_ext == "md":
        file_ext = "markdown"
    return {"content": content, "contentFormat": file_ext}


def prep_data(args: dict) -> dict:
    """prepares payload to publish post
    Parameters:
    args, dict: The input arguments (filepath, title, tags, pub)
    """
    data = {
        "title": args["title"],
    }
    data = {**data, **read_file(args["filepath"])}
    if args["tags"]:
        data["tags"] = [t.strip() for t in args["tags"].split(",")]
    data["publishStatus"] = "draft"
    if args["pub"]:
        data["publishStatus"] = args["pub"]
    return data

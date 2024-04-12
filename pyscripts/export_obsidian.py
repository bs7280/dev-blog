from obsidian_to_hugo import ObsidianToHugo
import os
import re


def extract_markdown_links(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found.")
        return

    # Loop through all files in the directory
    out = []
    for filename in os.listdir(directory):
        # Check if the file has a Markdown extension (.md)
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

                # Use regular expression to find all Markdown links
                wiki_links = re.findall(r'\{\{< ref "(.*?)" >\}\}', content)
                for link in wiki_links:
                    out.append(link)
    return out


def remove_files_not_in_links(directory, static_dir, linked_fnames):
    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
        # print(ext)

        full_path = os.path.join(directory, filename)
        if not filename.endswith(".md") and not os.path.isdir(full_path):
            if filename not in linked_fnames:
                print(f"Removing {filename} from {obsidian_to_hugo.hugo_content_dir}")
                os.remove(full_path)
            elif ext in (".png", ".jpg", ".jpeg", ".gif"):
                if False:
                    new_path_image = os.path.join(static_dir, filename)
                    print(f"Moving {filename} to {new_path_image}")
                    os.rename(full_path, new_path_image)


def filter_file(file_contents: str, file_path: str) -> bool:
    # do something with the file path and contents
    if "prj.devblog.posts." in file_path.lower():
        return True  # copy file
    else:
        return False  # skip file


def process_img_link(file_contents: str) -> str:

    import re

    # Input text with the weird broken wiki link
    # text = 'content: ![Pasted image 20240412165952.png]({{< ref "Pasted image 20240412165952.png" >}})'
    # Define the regular expression pattern
    pattern = r"\./([^/]+\.(?:png|jpg|jpeg|gif))"

    # Function to replace the path with a modified version
    def replace_path(match):
        original_path = match.group(0)
        new_path = original_path.replace("./", "/posts/")
        return new_path

    if re.search(pattern, file_contents):
        new_text = re.sub(pattern, replace_path, file_contents)
        breakpoint()
        return new_text
    return file_contents


# Hard coded based on what I specifically need
def remove_filename_prefix(content_dir):
    for filename in os.listdir(content_dir):
        if filename.endswith(".md"):
            filename_new = filename.replace("prj.devblog.posts.", "")

            full_path_current = os.path.join(content_dir, filename)
            full_path_new = os.path.join(content_dir, filename_new)

            os.rename(full_path_current, full_path_new)


## CONFIG

if __name__ == "__main__":
    config_site_dir = (
        "/Users/benshaughnessy/code/website_devblog/benshaughnessy_devblog/"
    )
    config_obsidian = "/Users/benshaughnessy/Documents/personalvault-1/"

    posts_sub_dir = "content/posts/"
    static_sub_dir = "static/"

    abs_path_posts = os.path.join(config_site_dir, posts_sub_dir)
    abs_path_static = os.path.join(config_site_dir, static_sub_dir)


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=config_obsidian,
    hugo_content_dir=abs_path_posts,
    filters=[filter_file],
    # processors=[process_img_link],
)

obsidian_to_hugo.run()

#  Get all wiki links in markdown files
links = extract_markdown_links(obsidian_to_hugo.hugo_content_dir)
# Remove unused files
remove_files_not_in_links(abs_path_posts, abs_path_static, links)

# Rename files
remove_filename_prefix(abs_path_posts)

## TODO remove unused dirs

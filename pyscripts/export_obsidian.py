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
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Use regular expression to find all Markdown links
                wiki_links = re.findall(r'\{\{< ref "(.*?)" >\}\}', content)
                for link in wiki_links:
                    out.append(link)
    return out


def remove_files_not_in_links(directory, static_dir, linked_fnames):
    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
       #print(ext)

        full_path = os.path.join(directory, filename)
        if not filename.endswith(".md") and not os.path.isdir(full_path):
            if filename not in links:
                print(f"Removing {filename} from {obsidian_to_hugo.hugo_content_dir}")
                os.remove(full_path)
            elif ext in ('.png', '.jpg', '.jpeg', '.gif'):
                new_path_image =  os.path.join(static_dir, filename)
                print(f"Moving {filename} to {new_path_image}")
                os.rename(full_path,new_path_image)


def filter_file(file_contents: str, file_path: str) -> bool:
    # do something with the file path and contents
    #breakpoint()
    if 'prj.devblog.posts.' in file_path:
        return True # copy file
    else:
        return False # skip file


## CONFIG
    
if __name__ == '__main__':
    config_site_dir = '/Users/benshaughnessy/code/website_devblog/benshaughnessy_devblog/'
    config_obsidian = "/Users/benshaughnessy/Documents/personalvault-1/"

    posts_sub_dir = 'content/posts/'
    static_sub_dir = 'static/'

    abs_path_posts = os.path.join(config_site_dir, posts_sub_dir)
    abs_path_static = os.path.join(config_site_dir, static_sub_dir)


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir=config_obsidian,
    hugo_content_dir=abs_path_posts,
    filters=[filter_file],
)

obsidian_to_hugo.run()

#  Get all wiki links in markdown files
links = extract_markdown_links(obsidian_to_hugo.hugo_content_dir)
# Remove unused files
remove_files_not_in_links(abs_path_posts, abs_path_static, links)

## TODO remove unused dirs
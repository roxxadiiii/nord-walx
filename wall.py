import os
repo_path = "/home/roxx/dev/nord-walx/walx"
def generate_gallery(repo_path, output_file="README.md"):
    # Ensure the repository path exists
    if not os.path.exists(repo_path):
        print(f"Error: Path '{repo_path}' does not exist.")
        return

    # List all image files in the repo
    supported_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")
    images = [img for img in os.listdir(repo_path) if img.lower().endswith(supported_extensions)]

    if not images:
        print("No image files found in the specified directory.")
        return

    # Generate Markdown content
    md_content = "# Wallpaper Gallery\n\n"
    md_content += "A collection of wallpapers. Click on any thumbnail to view the full image.\n\n"
    md_content += "## Gallery\n\n"

    for image in images:
        image_path = os.path.join(repo_path, image)
        relative_path = image  # Adjust if images are in subdirectories
        md_content += f"[![{image}](walx/{relative_path})](walx/{relative_path})\n\n"

    # Save to README.md
    with open(os.path.join(repo_path, output_file), "w") as md_file:
        md_file.write(md_content)

    print(f"Gallery generated successfully in {os.path.join(repo_path, output_file)}.")

# Path to your wallpaper repository
generate_gallery(repo_path)

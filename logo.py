from PIL import Image


def merge_images(background_path, overlay_path, output_path, position):
    # Open the background image
    background = Image.open(background_path)

    # Open the overlay image (the one you want to add to the left corner)
    overlay = Image.open(overlay_path)

    # Resize the overlay image to fit in the left corner (you can change the size as needed)
    overlay_width, overlay_height = overlay.size
    max_width = (
        background.width // 4
    )  # You can adjust this value based on your preference
    max_height = (
        background.height // 4
    )  # You can adjust this value based on your preference
    if overlay_width > max_width or overlay_height > max_height:
        ratio = max(max_width / overlay_width, max_height / overlay_height)
        overlay = overlay.resize(
            (int(overlay_width * ratio), int(overlay_height * ratio))
        )

    # Calculate the position for the left corner
    if position == "rt":
        position = (background.width - overlay.width, 0)
    elif position == "lt":
        position = (0, 0)
    elif position == "rb":
        position = (
            background.width - overlay.width,
            background.height - overlay.height,
        )
    elif position == "lb":
        position = (0, background.height - overlay.height)
    elif position == "ct":
        position = (int(background.width / 2 - overlay.width / 2), 0)
    elif position == "cb":
        position = (
            int(background.width / 2 - overlay.width / 2),
            background.height - overlay.height,
        )
    elif position == "cm":
        position = (
            int(background.width / 2 - overlay.width / 2),
            int(background.height / 2 - overlay.height / 2),
        )

    # Paste the overlay image on the background image
    background.paste(overlay, position, overlay)

    # Save the merged image to the output path
    background.save(output_path)


if __name__ == "__main__":
    background_image_path = "./1.png"  # Replace with the path to your background image
    overlay_image_path = (
        "./assets/logo.png"  # Replace with the path to your overlay image
    )
    output_image_path = "output_image.png"  # Replace with the desired output path
    pos = input(
""" Enter Your Position: 
rt = right/top
lt = left/top
rb = right/bottom
lb = left/bottom
ct = center/top
cb = center/bottom
cm = center/middle
"""
    )
    merge_images(background_image_path, overlay_image_path, output_image_path, pos)

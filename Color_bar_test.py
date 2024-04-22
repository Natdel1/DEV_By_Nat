from PIL import Image

def check_colors(image_path):


  # Load the image
  image = Image.open(image_path)

  # Convert the image to RGB
  image = image.convert("RGB")

  # Get the size of the image
  width, height = image.size

  # Define the expected width of each color stripe
  stripe_width = width // 8

  # List of expected colors in the color bar based on the information provided
  expected_colors = [
      (255, 255, 255),#light
      (249, 251, 0),  # Yellow
      (2, 254, 255),  # Light blue
      (1, 255, 0),  # Green
      (253, 0, 251),  # Purple
      (251, 1, 2),  # Red
      (3, 1, 252),  # Dark blue
      (0, 0, 0), #back 

  ]

  # Check the colors of each stripe
  for i in range(8):
    # Get the color of the current stripe
    stripe_color = image.getpixel((i * stripe_width, height // 2))

    # Check if the stripe color matches one of the expected colors
    if stripe_color not in expected_colors:
      return False

  return True


if __name__ == "__main__":

  image_path = "EBU_Colorbars.png"

  if check_colors(image_path):
    print("The color bar displays all 8 colors.")
  else:
    print("The color bar does not display all 8 colors.")

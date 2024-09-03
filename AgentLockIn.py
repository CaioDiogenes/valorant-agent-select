import pyautogui
import cv2
import numpy as np
import time

def find_image(template_path, threshold=0.8):
    # Capture a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)

    # Convert screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    # Load the template image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Match the template
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # Find locations where the match is above the threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        return locations[0]  # Return the first match found
    else:
        return None

def click_at_location(location, template_path):
    # Load the template image to get its size
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    template_height, template_width = template.shape

    # Calculate the center of the template
    center_x = location[0] + template_width // 2
    center_y = location[1] + template_height // 2

    # Click at the center of the found image
    pyautogui.click(center_x, center_y)

def main():
    first_image_path = 'vyse.png'  # Replace with the path to the first image
    second_image_path = 'lock in.png'  # Replace with the path to the second image

    print("Running...")
    while True:
        first_image_location = find_image(first_image_path)

        if first_image_location:
            print(f"First image found at: {first_image_location}")
            click_at_location(first_image_location, first_image_path)
            
            print("Searching for the second image...")
            second_image_location = find_image(second_image_path)

            if second_image_location:
                print(f"Second image found at: {second_image_location}")
                click_at_location(second_image_location, second_image_path)
                break  # Exit the loop after both clicks

        time.sleep(0)  # Wait for a second before searching again

    print("Done...")

if __name__ == "__main__":
    main()

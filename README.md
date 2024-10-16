# Basic Image Recognition Script

This Python script performs basic image recognition, specifically designed to identify single digits (1-9) in images. It creates a training dataset, applies thresholding for segmentation, and attempts to recognize the number in an unknown image.

## Requirements

- Python 3.x
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)
- Pillow (`pip install Pillow`)

## Instructions

1. **Create a folder named `images`:**
   - Inside this folder, create two subfolders: `numbers` and `test`.

2. **Place training images:**
   - Put images containing single digits (1-9) in various fonts and styles inside the `numbers` folder.
   - Each image should have a unique filename (e.g., `1.1.png`, `2.3.png`).

3. **Run `createExamples.py`:**
   - This script generates a training dataset file named `numArEx.txt` in the same directory as the script.
   - It iterates through the `numbers` folder, converts each image to a NumPy array, and stores the digit label along with the array representation in the text file.

4. **Place a test image:**
   - Put the image you want to identify in the `test` folder.
   - Name it descriptively (e.g., `teste.png`).

5. **Run `whatNumIs.py`:**
   - This script loads the training data and attempts to recognize the digit in the test image.
   - It displays a bar graph indicating the probability of each digit being the correct answer.

## Notes

- This script is a basic implementation and may not be robust to highly distorted or noisy images.
- The training data plays a crucial role in the accuracy of the recognition. The more diverse the training images, the better the script will perform.
- Consider exploring more advanced image processing techniques for improved performance.

## Example Usage

```bash
python createExamples.py  # Generate training data
python whatNumIs.py 'images/test/teste.png'  # Identify digit in test image

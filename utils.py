import os
import glob
import numpy as np


def get_paths_by_re(base_directory, regular_expression):
    search_pattern = os.path.join(base_directory,regular_expression)
    # Use glob to find all files matching the pattern
    png_files = glob.glob(search_pattern, recursive=True)
    return png_files
    
def extract_slice(file_path, width, height, x = None, y = None, slice_width = None, slice_height = None):
    """
    file_path : Path of the image File
    width : width of the image
    height : height of the image
    x : x coordinate from where you want to slice
    y : y coordinate from where you want to slice
    slice_width : width of the slice
    slice_height : height of the slice
    """
    # Adjust slice_width and slice_height if they extend beyond image boundaries
    if x + slice_width > width:
        slice_width = width - x
    if y + slice_height > height:
        slice_height = height - y

    # Initialize the slice array
    slice_array = np.zeros((slice_height, slice_width), dtype=np.uint8)

    with open(file_path, 'rb') as f:
        for row in range(slice_height):
            # Calculate the position to seek in the file
            pos = (y + row) * width + x
            f.seek(pos)
            # Read the slice_width bytes for the current row
            row_data = f.read(slice_width)
            # Store the row data in the numpy array
            slice_array[row, :] = np.frombuffer(row_data, dtype=np.uint8)

    return slice_array


class Segmenter:
    def __init__(self, image):
        self.image = image
        np.
    
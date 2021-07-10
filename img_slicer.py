
# Import Python Image Library
from PIL import Image
import math

# Takes full path of a file and returns the directory path and file name separately.
def trunkate_file_path(full_path):
   filename = full_path[::-1].split("/", maxsplit=1)[0][::-1]
   file_dir = full_path[::-1].split("/", maxsplit=1)[1][::-1]

   return (filename, file_dir)

   
filepath = input('Enter image path: ')
total_cols = int(input('Enter number of columns: '))
total_rows = int(input('Enter number of rows: '))

img = Image.open(filepath)
img_width, img_height = img.size
directory = trunkate_file_path(filepath)[1]

# Size of each piece
piece_height = img_height / total_rows
piece_width = img_width / total_cols
print(f'piece height: {piece_height} - piece width: {piece_width}')


for col_num in range(0, total_cols):
   for row_num in range(0, total_rows):
      number = row_num + (col_num * total_rows)
      left = math.floor(piece_width * col_num)
      top = math.floor(piece_height * row_num)
      right = math.floor(piece_width * col_num) + piece_width
      bottom = math.floor(piece_height * row_num) + piece_height
            
      img_crop = img.crop((left, top, right, bottom))      
      img_crop.save(f'{directory}/img{number}.jpg', quality=100)
      

from PIL import Image, ImageFilter, ImageDraw, ImageFont

def rotate_image(image_path, save_path):
    # uploading an image
    image = Image.open(image_path)

    # turn 90 degrees counter-clockwise
    rotated_image = image.rotate(90, expand=True)

    # saving the rotated image
    rotated_image.save(save_path)
    print(f"The returned image is saved to: {save_path}")

def apply_detail_filter(image_path, save_path):
    # uploading an image
    image = Image.open(image_path)

    # applying the DETAIL filter
    detailed_image = image.filter(ImageFilter.DETAIL)

    # saving an image with a filter
    detailed_image.save(save_path)
    print(f"Image with DETAIL filter saved at: {save_path}")


def convert_to_8bit(image_path, save_path):
    # uploading an image
    image = Image.open(image_path)

    # convert to 8-bit graphics mode
    image_8bit = image.convert("P")

    # save the new image
    image_8bit.save(save_path)
    print(f"Image converted to 8-bit mode and saved at: {save_path}")
    
def process_and_paste_image(image_path, save_path):
            try:
                # uploading an image
                image = Image.open(image_path)
                print("Main Image Size:", image.size)
                width, height = image.size
                # creating mini image
                img1 = image.resize((200, 100))

                x_offset = (width - 200) // 2 
                y_offset = height - 100      
                
            
                image.paste(img1, (x_offset, y_offset))
               
                image.save(save_path)
                print(f"The processed image is saved as{save_path}")
            except FileNotFoundError:
                print(f"Error: File {image_path} is not found.")
            except Exception as e:
                print(f"An error: {e}")

    
# using functions
rotate_image('plane.jpg', 'rotated_image.jpg') # returned image
apply_detail_filter('plane.jpg', 'detailed_image.jpg') # Image with filter
convert_to_8bit('plane.jpg', '8bit_image.png') # imagen coverted to 8-bit mode
process_and_paste_image('plane.jpg', 'processed_image.jpg') # Image resized and inserted

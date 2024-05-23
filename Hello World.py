import epd4in2
from PIL import Image, ImageDraw, ImageFont

def main():
    try:
        # Initialize and clear the display
        epd = epd4in2.EPD()
        epd.init()
        epd.Clear(0xFF)
        
        # Create a new image with white background
        image = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(image)
        
        # Set the font type and size
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
        
        # Message to be displayed
        message = "Hello World"
        
        # Get size of the text to be displayed
        text_width, text_height = draw.textsize(message, font=font)
        
        # Calculate center position
        x = (epd.width - text_width) / 2
        y = (epd.height - text_height) / 2
        
        # Draw text on the image
        draw.text((x, y), message, font=font, fill=0)
        
        # Display the image
        epd.display(epd.getbuffer(image))
        
        # Keep the display on, remove this line if you want the program to end
        epd.sleep()

    except IOError as e:
        print(e)
    
    except KeyboardInterrupt:
        print("Program interrupted by user")
        epd4in2.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    main()

# Created by: Kay Lin
# Created on: 17th-Oct-2017
# Created for: ICS3U
# This program shows a man walking when a button is pressed

import ui
import time

@ui.in_background

def walking_man_touch_up_inside(sender):
    # This makes man walk
    
    # variables
    number_of_pictures = 10
    counter = 0
    
    # process
    while counter < number_of_pictures:
          if counter == 0:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_1.BMP')
              
          elif counter == 1:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_2.BMP')
              
          elif counter == 2:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_3.BMP')
              
          elif counter == 3:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_4.BMP')
              
          elif counter == 4:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_5.BMP')
              
          elif counter == 5:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_6.BMP')
              
          elif counter == 6:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_7.BMP')
              
          elif counter == 7:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_8.BMP')
              
          elif counter == 8:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_9.BMP')
              
          elif counter == 9:
              # output
              view['man_walking_imageview'].image = ui.Image.named('./assets/sprites/walking_man_10.BMP')
              
          counter = counter + 1
          time.sleep(0.1)
             

view = ui.load_view()
view.present('sheet')

    for pixel_color_x in range(500):
        for pixel_color_y in range(500):
            R_pixel = int(color_tmtg[0] + ((255 - color_tmtg[0]) * (pixel_color_x/500)) - ((color_tmtg[0]) * (pixel_color_y/500))) 
            G_pixel = int(color_tmtg[1] + ((255 - color_tmtg[1]) * (pixel_color_x/500)) - ((color_tmtg[1]) * (pixel_color_y/500))) 
            B_pixel = int(color_tmtg[2] + ((255 - color_tmtg[2]) * (pixel_color_x/500)) - ((color_tmtg[2]) * (pixel_color_y/500))) 
            pixel_color = ( R_pixel , G_pixel , B_pixel )

            screen.set_at((100 + pixel_color_x, 250 + pixel_color_y), pixel_color)

def HSB_gradient(color_of_s_RGB_s, black , white):
    gradient_to_white = []
    total_gradient= [[] for _ in range(50)]

    difference_to_white = (
        white*255/100 - color_of_s_RGB_s[0],
        white*255/100 - color_of_s_RGB_s[1],
        white*255/100 - color_of_s_RGB_s[2]
    )
    # Cria o gradiente HSB
    for n in range(50):
        gradient_to_white.append((
            color_of_s_RGB_s[0] + int(n * difference_to_white[0] / 50),
            color_of_s_RGB_s[1] + int(n * difference_to_white[1] / 50),
            color_of_s_RGB_s[2] + int(n * difference_to_white[2] / 50)
        ))
        for z in range(50):
            total_gradient[n].append((
                gradient_to_white[n][0] - int( (z * gradient_to_white[n][0] / 50) / (100/black) ),
                gradient_to_white[n][1] - int( (z * gradient_to_white[n][1] / 50) / (100/black) ),
                gradient_to_white[n][2] - int( (z * gradient_to_white[n][2] / 50) / (100/black) )
            ))
    return total_gradient
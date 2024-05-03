def print_c(color, text, bg=None):
    text_color = {'black':30,
                  'bk':30,
                  'red':31,
                  'r':31,
                  'green':32,
                  'g':32,
                  'yellow':33,
                  'y':33,
                  'blue':34,
                  'b':34,
                  'magenta':35,
                  'cyan':36,
                  'white':37,
                  'w':37}

    bg_color = {None:47,
                'black':40,
                'bk':40,
                'red':41,
                'r':41,
                'green':42,
                'g':42,
                'yellow':43,
                'y':43,
                'blue':44,
                'b':44,
                'magenta':45,
                'cyan':46,
                'white':47,
                'w':47}
    print(f'\r\033[{text_color[color]}m \033[{bg_color[bg]}m {text} \033[0m', end="")
# import time
# while True:
#     print_c('r',"안녕하세요",'y',)
#     time.sleep(0.1)
#     print_c('g',"안녕하세요",'r',)
#     time.sleep(0.1)
#     print_c('b',"안녕하세요",'r',)
#     time.sleep(0.1)
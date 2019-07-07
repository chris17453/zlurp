# cython: profile=True
# cython: linetrace=True
# cython: binding=True
# cython: language_level=2



# array..
# ColorTableSize = 3L * (1L << (SizeOfGlobalColorTable + 1));
class gif_color_table:
    def __init__(self,stream):
        self.stream=stream
        self.internal_position=self.stream.pos
        self.colors=[]

    def get_byte_size(self):
        colors_len=len(self.colors)/3
        size=0
        if   colors_len>128: size=8
        elif colors_len>64 : size=7
        elif colors_len>32 : size=6
        elif colors_len>16 : size=5
        elif colors_len>8  : size=4
        elif colors_len>4  : size=3
        elif colors_len>0  : size=2
        return size
            
    def read(self,entries):
        self.internal_position=self.stream.pos
        self.colors=[]
        for i in range(0,entries*3):
            color  = self.stream.byte()
            self.colors.append(color)

    def write(self):
        self.internal_position=self.stream.pos
        for color in self.colors:
            self.stream.write_byte(color)

    def new(self,palette=None):
        self.colors=[]
        if palette:
            self.colors=palette
        else:
            color_table=[  # 16 System Colors
                0,0,0 , 128,0,0 , 0,128,0 , 128,128,0,
                0,0,128 , 128,0,128 , 0,128,128 , 192,192,192,
                128,128,128 , 255,0,0 , 0,255,0 , 255,255,0,
                0,0,255 , 255,0,255 , 0,255,255 , 255,255,255,
                # xterm palette
                0,0,0 , 0,0,95 , 0,0,135 , 0,0,175 , 0,0,215 , 0,0,255,
                0,95,0 , 0,95,95 , 0,95,135 , 0,95,175 , 0,95,215 , 0,95,255,
                0,135,0 , 0,135,95 , 0,135,135 , 0,135,175 , 0,135,215 , 0,135,255,
                0,175,0 , 0,175,95 , 0,175,135 , 0,175,175 , 0,175,215 , 0,175,255,
                0,215,0 , 0,215,95 , 0,215,135 , 0,215,175 , 0,215,215 , 0,215,255,
                0,255,0 , 0,255,95 , 0,255,135 , 0,255,175 , 0,255,215 , 0,255,255,
                95,0,0 , 95,0,95 , 95,0,135 , 95,0,175 , 95,0,215 , 95,0,255,
                95,95,0 , 95,95,95 , 95,95,135 , 95,95,175 , 95,95,215 , 95,95,255,
                95,135,0 , 95,135,95 , 95,135,135 , 95,135,175 , 95,135,215 , 95,135,255,
                95,175,0 , 95,175,95 , 95,175,135 , 95,175,175 , 95,175,215 , 95,175,255,
                95,215,0 , 95,215,95 , 95,215,135 , 95,215,175 , 95,215,215 , 95,215,255,
                95,255,0 , 95,255,95 , 95,255,135 , 95,255,175 , 95,255,215 , 95,255,255,
                135,0,0 , 135,0,95 , 135,0,135 , 135,0,175 , 135,0,215 , 135,0,255,
                135,95,0 , 135,95,95 , 135,95,135 , 135,95,175 , 135,95,215 , 135,95,255,
                135,135,0 , 135,135,95 , 135,135,135 , 135,135,175 , 135,135,215 , 135,135,255,
                135,175,0 , 135,175,95 , 135,175,135 , 135,175,175 , 135,175,215 , 135,175,255,
                135,215,0 , 135,215,95 , 135,215,135 , 135,215,175 , 135,215,215 , 135,215,255,
                135,255,0 , 135,255,95 , 135,255,135 , 135,255,175 , 135,255,215 , 135,255,255,
                175,0,0 , 175,0,95 , 175,0,135 , 175,0,175 , 175,0,215 , 175,0,255,
                175,95,0 , 175,95,95 , 175,95,135 , 175,95,175 , 175,95,215 , 175,95,255,
                175,135,0 , 175,135,95 , 175,135,135 , 175,135,175 , 175,135,215 , 175,135,255,
                175,175,0 , 175,175,95 , 175,175,135 , 175,175,175 , 175,175,215 , 175,175,255,
                175,215,0 , 175,215,95 , 175,215,135 , 175,215,175 , 175,215,215 , 175,215,255,
                175,255,0 , 175,255,95 , 175,255,135 , 175,255,175 , 175,255,215 , 175,255,255,
                215,0,0 , 215,0,95 , 215,0,135 , 215,0,175 , 215,0,215 , 215,0,255,
                215,95,0 , 215,95,95 , 215,95,135 , 215,95,175 , 215,95,215 , 215,95,255,
                215,135,0 , 215,135,95 , 215,135,135 , 215,135,175 , 215,135,215 , 215,135,255,
                215,175,0 , 215,175,95 , 215,175,135 , 215,175,175 , 215,175,215 , 215,175,255,
                215,215,0 , 215,215,95 , 215,215,135 , 215,215,175 , 215,215,215 , 215,215,255,
                215,255,0 , 215,255,95 , 215,255,135 , 215,255,175 , 215,255,215 , 215,255,255,
                255,0,0 , 255,0,95 , 255,0,135 , 255,0,175 , 255,0,215 , 255,0,255,
                255,95,0 , 255,95,95 , 255,95,135 , 255,95,175 , 255,95,215 , 255,95,255,
                255,135,0 , 255,135,95 , 255,135,135 , 255,135,175 , 255,135,215 , 255,135,255,
                255,175,0 , 255,175,95 , 255,175,135 , 255,175,175 , 255,175,215 , 255,175,255,
                255,215,0 , 255,215,95 , 255,215,135 , 255,215,175 , 255,215,215 , 255,215,255,
                255,255,0 , 255,255,95 , 255,255,135 , 255,255,175 , 255,255,215 , 255,255,255,
                8,8,8 , 18,18,18 , 28,28,28 , 38,38,38 , 48,48,48 , 58,58,58 , 68,68,68,
                78,78,78 , 88,88,88 , 98,98,98 , 108,108,108 , 118,118,118 , 128,128,128,
                138,138,138 , 148,148,148 , 158,158,158 , 168,168,168 , 178,178,178 , 188,188,188,
                198,198,198 , 208,208,208 , 218,218,218 , 228,228,228 , 238,238,238 ]
            self.colors=color_table



    def debug(self):
        index=0
        print("Color Table Block")
        print("  Offset: {0:02X}".format(self.internal_position))

        for i in range(0,len(self.colors),3):
            print("  Index:{3:3}, R:0x{0:02X}, G:0x{1:02X}, B:0x{2:02X}".format(self.colors[i],self.colors[i+1],self.colors[i+2],index))
            index+=1

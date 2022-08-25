import numpy

__version__ = '1.0.0'

class ImageManager:
        
    class Renderer:
        def __init__(self, left, top, color_picker, code_type):
            self.left = left
            self.top = top
            self.color_picker = color_picker
            self.code_type = code_type

    def compose(self, bg_image, renderers):
        try:
            for renderer in renderers:
                src = renderer.code_type.generate()
                src[numpy.where((src==[255,255,255]).all(axis=2))] = bg_image[renderer.color_picker[0], renderer.color_picker[1]]
                bg_image[renderer.top:renderer.top + src.shape[0], renderer.left: renderer.left + src.shape[1]] = src
            return bg_image
        except Exception as err:
            print(err)
            
        # try:
        #     if not os.path.isdir(src) or not os.path.isdir(output):
        #         return
        #     print('Generating images...')
            
        #     filelist = os.listdir(src)
        #     if len(filelist) > 0:
        #         for file in filelist:
        #             print(file)
        #             encoded = encode(file.encode('utf8'))
        #             img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        #             src = numpy.array(img)

        #             # resize image
        #             scale_factor = 1.5
        #             src = self.resize_image(src, scale_factor)
                
        #             # load image
        #             bg_image = cv2.imread(os.path.join(src, file))

        #             # draw DataMatrix code
        #             left = 10
        #             top = 40
        #             offset = 125
                
        #             src = self.binary_image(src)
        #             src[numpy.where((src==[255,255,255]).all(axis=2))] = bg_image[10, 10]
        #             bg_image[top:top + src.shape[0], bg_image.shape[1] - offset: bg_image.shape[1] - offset + src.shape[1]] = src
                
        #             # draw UPCA
        #             print(self.number)
        #             number_to_str = str(self.number)
        #             upca_code = UPCA(number_to_str, writer=ImageWriter())
        #             upca_code.save(number_to_str)

        #             src = cv2.imread(number_to_str + '.png')
        #             src = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
                
        #             # resize upca image
        #             scale_factor = 0.5
        #             src = self.resize_image(src, scale_factor)
                
        #             left = 0
        #             top = 258
        #             src = self.binary_image(src)
        #             src[numpy.where((src==[255,255,255]).all(axis=2))] = bg_image[10, 10]
        #             bg_image[top:top + src.shape[0], left: left + src.shape[1]] = src

        #             # cv2.imshow(str(i), bg_image)
        #             outfile = '{0}x{1}_{2}.png'.format(bg_image.shape[1], bg_image.shape[0], file.split('.')[0])
        #             cv2.imwrite(os.path.join(output, outfile), bg_image)
                
        #             self.number += 1

        #         # cv2.waitKey(0) 

        # except Exception as e:
        #     print(e)
        #     pass
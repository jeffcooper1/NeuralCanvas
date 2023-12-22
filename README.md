# Neural Canvas
An AI Art Picture Frame

### Functionality
In our final version of Neural Canvas, users can initiate prompt input by using wake words, the default being “picture frame”.
Users can also use the name of various artists as the wake word for their image to be displayed in that artist’s style. Upon 
verification of the wake word, the user is then instructed to speak their prompt. The prompt can be as long and as in-depth as 
they desire. The program will begin generating the image once the user has finished speaking their prompt. The generated 
image is then displayed onto the picture frame. The image will continue to be displayed until the user provides another wake 
word.

Neural Canvas uses the SpeechRecognition Python library for both the wake word and voice prompt functions. For image 
generation, the spoken prompt is fed into OpenAI’s API to utilize DALL-E 3’s image generation capabilities. Feh image viewer is used to take the saved images and open them for display on the screen. After the image is displayed, the program loops back 
and waits for another wake word.

![IMG-8947 (1)](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/7a9beb9e-e645-4405-919f-4a6371f3832f)
![IMG-8946](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/25a8f686-caf6-4fc1-bea5-3d3cb46f34d1)

## Contributers
Jeff Cooper, Ian Cox, Chase Melisky

## Class
CS2210: Computer Organization

## Professor
James Eddy

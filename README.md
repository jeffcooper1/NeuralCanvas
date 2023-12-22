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

![IMG-8946](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/f121f456-d7d3-47e2-927d-476625d7f5d7)
![csfair](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/70938405-1374-4530-b0e6-b13237a53c97)


### Walkthrough
1. Program is executed. Waiting for user to speak a wake word.

![title](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/334f6eb1-ae22-41ae-9388-c354d14ea7d7)

2. Wake word detected. User is instructed to provide a prompt.

![speak](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/e66f1751-c38c-40af-a847-fb9f59890140)

3. User finished speaking their prompt. Image is being generated.

![generating](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/4bbdae7b-ad3a-432e-a1b8-75a01dcb73ba)

4. Image is displayed. Image will stay displayed until prompted with another wake word.

![image_6483441](https://github.com/jeffcooper1/NeuralCanvas/assets/111708974/69c1175c-ff9f-4ed4-aaf4-59a2938a77d0)

(Prompt Given: CCTV fisheye footage of a giant realistic eagle on a green truck taking money from a man at a gas station)

___________________________________________________________________
# [Video Demonstration](https://www.youtube.com/watch?v=0DIzFwDBfL4)


## Contributors
Jeff Cooper, Ian Cox, Chase Melisky

## Class
CS2210: Computer Organization

## Professor
James Eddy

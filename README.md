
# ML Using Audio Analysis
<div id="header" align="left">
  <img src="https://del-portal.kfu.edu.sa/_frontend/fron/images/kfu_logo.png" width="250" 400 height="100"//>
</div>

##  Introduction:

We, as students from [KFU's](https://www.kfu.edu.sa/ar/Colleges/Computer_Science/Pages/Home-new.aspx) Computer Engineering department, have developed a project utilizing machine learning to analyze sounds, focusing specifically on the sound of wind. This application holds significant potential in various fields, particularly in weather forecasting and determining wind speed.
## The Process:
We used FFmpeg to trim audio recordings into smaller segments, each lasting one second, resulting in 2600 files. 
We used Python code to sort RMS values into ascending order.
After that we upload the RMS files to [Edge impulse](https://edgeimpulse.com/) 
We divided 80% of the files for training purposes and allocated the remaining 20% for testing. 

A neural network with 3,168 features would have 3,168 input neurons, each representing a single feature of your data. These neurons would feed the data into the network for further processing by the hidden layers.
 implementing such a network, ensure that your data is properly preprocessed and normalized so that each of these features can be effectively used by the network. Also, consider the complexity of your model and the computational resources at your disposal, as a large number of features can significantly increase the computational load.
<div id="header" align="center">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic3.png" width="300" 400 height="150"//>
  


  ###The input Layer to output Layer.
  And these are the steps: 
  <div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic4.png" width="600" 400 height="350"//>

### More about conversion Details:

1.Input Layer (3,168 features):
   - This layer receives input data with 3,168 features.

2. Reshape Layer (32 columns):
   - This layer reshapes the input data into a format suitable for the subsequent convolutional layers. It reshapes the input data into 32 columns.

3. 1D Convolutional / Pooling Layer (16 neurons, 3 kernel size, 1 layer):
   - This layer performs 1-dimensional convolutional filtering with 16 neurons.
   - Each neuron uses a kernel size of 3, meaning it looks at a window of 3 adjacent elements at a time.
   - It's followed by a pooling layer, which reduces the dimensionality of the output by pooling the maximum value over a window.

4. Dropout Layer (rate 0.25):
   - Dropout is a regularization technique that randomly sets a fraction of input units to zero during training, which helps prevent overfitting. Here, 25% of the neurons are randomly dropped during training.

5. 1D Convolutional / Pooling Layer (16 neurons, 3 kernel size, 1 layer):
   - Another convolutional layer similar to the previous one.

6. Dropout Layer (rate 0.25):
   - Another dropout layer with a dropout rate of 25%.

7. 1D Convolutional / Pooling Layer (8 neurons, 3 kernel size, 1 layer)**:
   - Yet another convolutional layer, but this time with 8 neurons.

8. Flatten Layer:
   - This layer flattens the output from the previous convolutional layers into a 1D array, preparing it for input into the fully connected layers.

9. Dense Layer (8 neurons):
   - A fully connected (dense) layer with 8 neurons.

10. Extra Layer:
   - You mentioned adding an extra layer, but it's not specified what type of layer it is or its configuration.
11. - Output Layer (6 classes):
     </div>
 This shows all data in your training set classified by the neural network. Items in green are classified correctly, items in red are misclassified.
<div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic2.png" width="600" 400 height="350"//>



   - The final output layer with 6 neurons, representing the number of classes in your classification problem.

<div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic1.png" width="600" 400 height="350"//>

  ## Deployment  :
  Due to its significantly higher RAM capacity compared to other microcontrollers such as the Nano BLE Duo, the ESP32 emerged as the ideal choice for our project. This ample RAM allows the ESP32 to efficiently manage and process our large datasets.
<div id="header" align="center">
  <img src="https://diyi0t.com/wp-content/uploads/2020/12/Sound-Sensor-ESP32-ESP-WROOM-32-_Steckplatine.png" width="300" 400 height="150"//>
</div>

## Implemtation:
The Tiny Machine Learning is a cutting-edge device that that uses smart technology to analyze wind sounds. This helps weather experts make better forecasts, which can improve people’s lives. It’s designed to be open and easy for others to work with, making it a helpful tool for studying the weather.

## Our Goal:
Capturing and analyzing sound is not our primary objective. Our true aim is to assist humanity in any way possible by measuring various elements in our surroundings to enhance the quality of life.living. Our project is universally accessible, This project stands as an open invitation for collective effort, dedicated to the betterment of society by the industry.
<div id="header" align="center">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic5.jpeg" width="300" 400 height="220"//>

## This Project Done By:                                    
### Students:                   
##### Ibrahim Alawadh.
##### Yasser AlRamadhan.
##### Saleh Boshalf.
### Supervisor :
##### DR.Ramasamy.



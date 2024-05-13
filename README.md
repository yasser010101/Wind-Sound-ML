
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

<div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic1.png" width="300" 400 height="150"//>
</div>
This shows all data in your training set classified by the neural network. Items in green are classified correctly, items in red are misclassified.
<div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic2.png" width="300" 400 height="150"//>

  For a neural network with 3,168 features would have 3,168 input neurons, each representing a single feature of your data. These neurons would feed the data into the network for further processing by the hidden layers.
 implementing such a network, ensure that your data is properly preprocessed and normalized so that each of these features can be effectively used by the network. Also, consider the complexity of your model and the computational resources at your disposal, as a large number of features can significantly increase the computational load.
<div id="header" align="left">
  <img src="https://raw.githubusercontent.com/yasser010101/Wind-Sound-ML/main/pic3.png" width="300" 400 height="150"//>
  
## This Project Done By:                                    
### Students:                   
##### Ibrahim Alawadh.
##### Yasser AlRamadhan.
##### Saleh Boshalf.
### Supervisor :
##### DR.Ramasamy.

#### This image shows the wiring connection:
<div id="header" align="center">
  <img src="https://diyi0t.com/wp-content/uploads/2020/12/Sound-Sensor-ESP32-ESP-WROOM-32-_Steckplatine.png" width="300" 400 height="150"//>
</div>

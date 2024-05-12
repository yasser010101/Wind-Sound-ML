
### ML With Audio Analysis
## Introduction:
<div id="header" align="center">
  <img src="https://del-portal.kfu.edu.sa/_frontend/fron/images/kfu_logo.png" width="250" 400 height="100"//>
</div>

We, as students from [KFU's](https://www.kfu.edu.sa/ar/Colleges/Computer_Science/Pages/Home-new.aspx) Computer Engineering department, have developed a project utilizing machine learning to analyze sounds, focusing specifically on the sound of wind. This application holds significant potential in various fields, particularly in weather forecasting and determining wind speed
## The Process:
We used FFmpeg to trim audio recordings into smaller segments, each lasting one second, resulting in 2600 files. 
We used Python code to sort RMS values into ascending order.
After that we upload the RMS files to [Edge impulse](https://edgeimpulse.com/)
We divided 80% of the files for training purposes and allocated the remaining 20% for testing. 
These files were categorized into six groups.
Subsequently, we initiated the training process on either the processor or the graphics card.
Following the training phase, we conducted testing and achieved an accuracy rate of 90%, which is considered excellent for this application.
We then selected the development environment, opting for [Arduino IDE](https://www.arduino.cc/en/software), and integrated it into a library accessible to all.
Throughout this experiment, we utilized ESP-32 due to its capability to handle large datasets effectively.
<div id="header" align="center">
  <img src="https://diyi0t.com/wp-content/uploads/2020/12/Sound-Sensor-ESP32-ESP-WROOM-32-_Steckplatine.png" width="300" 400 height="150"//>
</div>



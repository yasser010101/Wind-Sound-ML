ML with audio analysis
Introduction:

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
  <img src="https://diyi0t.com/wp-content/uploads/2020/12/Sound-Sensor-ESP32-ESP-WROOM-32-_Steckplatine.png" width="500" 400 height="350"//>
</div>

<div align="center">
  <img src="https://media.tenor.com/iNk-1osmqAsAAAAi/arduino.gif="600" height="300"/>
</div>

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
  <img src="<div class="tenor-gif-embed" data-postid="5671822644946302447" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/cat-meme-funny-gif-cat-dancing-dance-gif-5671822644946302447">Cat Meme Funny Sticker</a>from <a href="https://tenor.com/search/cat+meme-stickers">Cat Meme Stickers</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>" width="100"/>
</div>

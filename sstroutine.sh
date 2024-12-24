#!bin/bash

while true; do

timestamp=$(date +"%Y%m%d%H%M%S")
img_filename="test${timestamp}.jpeg"
echo $img_filename
libcamera-jpeg -o "$img_filename" --width 1080 --height 1920 -t 5000
if [$? -ne 0]; then 
echo "Error capturing image: $img_filename"
exit 1
fi
latest_photo = $(ls -t test*.png | head -n 1)

./pisstvpp -p s2 -r 22050 "$img_filename"

if [$? -ne 0]; then
echo "Error processing image: $img_filename"
exit 1
fi

echo "Successfully captured and processed: $latest_photo"


sleep 10

done

# simplest-mynt-eye-sdk
MYNT-EYE-S camera comes with a great [SDK](https://github.com/slightech/MYNT-EYE-S-SDK). However, this SDK has a lot of features, which in contrast makes it prone to failures such as build and run-time errors.   

In case if you just need to extract the stereo images from your camera, my script will help you do that in the simplest method.   

### C++
##### Dependencies
OpenCV

##### Build  
`$ cd <root>`  
`$ mkdir build`  
`$ cd build`  
`$ cmake  ..`  
`$ make`

##### Run
`$ cd <root>`  
`$ cd build`   
`$ ./extract_stereo <video_device_number>`


### Python  
##### Dependencies
OpenCV, numpy
##### Run
`$ cd <root>`  
`$ python extract_stereo.py <video_device_number>`   
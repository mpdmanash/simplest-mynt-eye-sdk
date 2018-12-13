#include <iostream>
#include <opencv2/opencv.hpp>



void extract_left_right(const cv::Mat & raw, cv::Mat & left, cv::Mat & right)
{
	cv::Mat out[] = {left, right};
	// raw[0] -> left[0],
	// raw[1] -> right[0]
	int from_to[] = { 0,0, 1,1};
	cv::mixChannels( &raw, 1, out, 2, from_to, 2 );
}

int main(int argv, char * argc[])
{
	cv::VideoCapture cap(std::atoi(argc[1]));
	cap.set(CV_CAP_PROP_CONVERT_RGB, false);

	// Check if camera opened successfully
	if(!cap.isOpened()){
		std::cout << "Error opening video stream\n" << std::endl;
		return -1;
	}

	// First Image
	cv::Mat frame, left, right;
	cap >> frame; if (frame.empty()) return -1;
	left = cv::Mat::zeros(frame.rows, frame.cols, CV_8UC1);
	right = cv::Mat::zeros(frame.rows, frame.cols, CV_8UC1);

	while(true)
	{
		cap >> frame; if (frame.empty()) break;
	 	
	 	extract_left_right(frame, left, right);
	    cv::imshow( "left", left );
	    cv::imshow( "right", right );
	 
	    // Press  ESC on keyboard to exit
	    char c=(char)cv::waitKey(25);
	    if(c==27)
	      break;
	}
	cv::destroyAllWindows();
	return 0;
}
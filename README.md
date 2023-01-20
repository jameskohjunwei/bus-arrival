# bus-arrival
 utilizing geopy, lta api, and apple location services to ping your location and let you know bus arrival timings.

This is a incomplete project. So far, i have a "hello world" version of this idea. The basic idea -
My route home from work consist of - MRT > then bus ride home. 
I want my script to ping me on telegram the arrival timings of my bus when i just arrive at payalebar MRT station (the spot where i transit to bus).

Workflow:
- apple location services ipycloud to ping my location
- should i be within x radius > trigger lta bus arrival api for data
- send bus arrival data via telegram to me

I thought it was a good idea. But now that i review all the work that's required... seems like it's better if i just open the app and check the arrival timings instead. Too much work, not much ROI. 

Attached is the script and my progress thusfar. Feel free to use it for your own development.

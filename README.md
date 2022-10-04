# asynchronous-api-requests-in-2gis
You can use this code for quick calculation distance and duration by route. 

<p><a href="[url](https://docs.2gis.com/ru/api/navigation/directions/overview)">Link to technical documentation api</a><p>
<p>Example of a response to request: 
 <p>
    [
    {'route_id': 0, 'distance': 3221, 'duration': 461, 'status_code': 200}, 
    {'route_id': 1, 'distance': 5289, 'duration': 537, 'status_code': 200}
    ] 
 <p>
<p> 
<p> Performance measurement (only speed) says that the asynchronous api client is ten as fast as the usual api client using requests library. <p> 
<p> But you need remember that the program execution time depends of: type api client (asynchronous or synchronous ), quantity of routes, api server. <p>

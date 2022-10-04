# asynchronous-api-requests-in-2gis
You can use this code for quick calculation distance and duration by route. 
<p>Link to technical documentation api<p>
 <p> https://docs.2gis.com/ru/api/navigation/directions/overview<p>

<p>Example of a response to request: 
 <p>
    [
    {'route_id': 0, 'distance': 3221, 'duration': 461, 'status_code': 200}, 
    {'route_id': 1, 'distance': 5289, 'duration': 537, 'status_code': 200}
    ] 
 <p>
<p> 
<p> Performance measurement (only speed) says that the asynchronous api client is ten as fast as the usual api client using requests library. <p> 
<p> This value ( ten ) was measured on 1000 request using real routes with RPS limit = 5. But this value can be different in your case. Because it depend of quantity of routes, api server, RPS config.<p> 
<p> You can reduce the program execution time changing RPS limit. <p>

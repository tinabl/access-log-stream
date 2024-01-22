# access-log-stream

https://canoe-thrust-windshield-el6a-7k2y.onrender.com                                                 
(Please wait a moment for the link to open.)


<img width="524" alt="pipeline" src="https://github.com/tinabl/access-log-stream/assets/93467399/849db448-e007-4a02-bdf3-75b389dc065d">


_

Travel of streaming data along the path above. I first created access-log data by manipulating a real batch dataset. Then created a virtual machine in the Google Cloud Compute Engine cluster and downloaded Kafka there. Kafka writes data Kafka queue with created topic and reads them, here it was used for this purpose. Dataproc easily provides a Spark cluster and that's what I used. Spark  read the streaming data, structured it accordingly and counted them. Then I created a table in Google BigQuery and imported the data into it. After all, I builded the analytics dashboard using Plotly Dash with data from BigQuery. I deployed the work using Render.

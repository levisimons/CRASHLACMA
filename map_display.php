<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />

    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map-canvas { height: 100% }
      .labels {
      	color: red;
      	background-color: white;
      	font-family: "Lucida Grande", "Arial", sans-serif;
     	font-size: 10px;
     	font-weight: bold;
     	text-align: center;
     	width: 40px;     
     	border: 2px solid black;
     	white-space: nowrap;
   }
    </style>
    
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>

	<script type="text/javascript">
		var imgThumbStack = [];
	</script>
	<?php
		$dir    = 'data_approved_images';
		$files1 = scandir($dir);

		foreach ($files1 as $value) {
			if (strpos($a,'PNG') !== false) {
	?>
	<script>
				myvar = '<?php echo $value;?>';
				imgThumbStack.push('<?php echo $value;?>');
				console.log(imgThumbStack);
	</script>

	<?php
			}
		}
	?>

    <script type="text/javascript">
      function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(34.0, -118.2),
          zoom: 11,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
		
        // generate queue of images to show
        // still prototype-y
        // this will eventually be replaced with stuff grabbed from php above
        
        console.log("initial stack: " + imgThumbStack); 
   //      imgThumbStack.push("thumb_34.0186425_-118.4069065_.PNG"); // pizza cat
// 		imgThumbStack.push("thumb_34.0226966_-118.3953026_.PNG"); // shark cat
// 		imgThumbStack.push("thumb_32.9415821_-117.1836399_.PNG"); // san diego cheeseburger
// 		imgThumbStack.push("thumb_34.0254201_-118.3950297_.PNG"); // books
// 		imgThumbStack.push("thumb_32.4042703_-97.2176273_.PNG"); // texas hamster
// 		
		// generates image thumbnails on the map
		for (var i = 0; i < 5; i++) { 
			console.log("stack[" + i + "]: " + imgThumbStack[i]);

    		var marker = new google.maps.Marker({
    			position: new google.maps.LatLng(imgThumbStack[i].split("_")[1], imgThumbStack[i].split("_")[2]),
    			map: map,
    			labelContent: "0", 
    			icon: "data_approved_images/" + imgThumbStack[i],
    			labelAnchor: new google.maps.Point(0, 50),
    			size: new google.maps.Size(50, 50),
    			labelClass: "labels", 
    			labelStyle: {opacity: 0.75},
    			title:"Nothing yet."
			});
		}
      }
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"/>
  </body>
</html>

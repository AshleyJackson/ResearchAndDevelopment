function notifyMe() {
	// Let's check if the browser supports notifications
	if (!("Notification" in window)) {
	  alert("This browser does not support desktop notification");
	}

	// Let's check whether notification permissions have already been granted
	else if (Notification.permission === "granted") {
	  // If it's okay let's create a notification
	  var options = {
		requireInteraction: true,
		body: 'test',
		tag: "myId",
		title: "test"
	}
	  var notification = new Notification("New Alert!", options);
	  notification.onclick    = function(event) {
		event.preventDefault(); // prevent the browser from focusing the Notification's tab
		window.open('http://example.com', '_blank');
	  }
	}


	// Otherwise, we need to ask the user for permission
	else if (Notification.permission !== "denied") {
	  Notification.requestPermission().then(function (permission) {
		// If the user accepts, let's create a notification
		if (permission === "granted") {
		  var notification = new Notification("Hi there!");
		}
	  });
	}

	// At last, if the user has denied notifications, and you
	// want to be respectful there is no need to bother them any more.
  }

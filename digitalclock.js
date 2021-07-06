setInterval(function(){
	var currenttime=new Date();
	var hours=currenttime.getHours();
	var minutes=currenttime.getMinutes();
	var seconds=currenttime.getSeconds();
	var period="AM";
	if (hours>=12){
		period="PM";
	}
	if (seconds<10){
		seconds="0"+seconds;
	}
	if (minutes<10){
		minutes="0"+minutes;
	}
	var clocktime=hours+":"+minutes+":"+seconds+" "+period;
	var clock=document.getElementById('clock');
	clock.innerText=clocktime;

},1000);
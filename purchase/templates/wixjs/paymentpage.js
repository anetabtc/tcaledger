// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world
import {local} from 'wix-storage';
$w.onReady(function ()
{
	const id = local.getItem("id");
	console.log("id:"+id);
	var url = 'https://austinnegron.com/purchase/page1/result/'+id;
	console.log("PAYMENT PAGE START");
	function handleErrors(response)
	{
		if (!response.ok)
			throw Error(response.statusText);
		return response;
	}
	async function getData(url)
	{
		return await fetch(url,
		{
			method: 'GET',
			mode: 'cors',
			headers:
			{
			'Content-type': 'application/json',
			}
		})
		.then(handleErrors)
		.catch(error => console.log(error))
		.then(response => response.json())
		.then(function(response) {return response.payment;});
	}
	var paid = false;
	function checkStatus()
	{
		getData(url).then(function(response)
		{
			if(response == "not received")
			{
				paid = false;
				var r = "The Payment Has Not Been Received Yet!";
				console.log(r);
				$w('#text86').text = r;
			}
			else
			{
				paid = true;
				var r = "The Payment Has Been Received!";
				console.log(r);
				$w('#text86').text = r;
				clearInterval(intervalId);
			}
		});
	}
	var seconds = 1;
	var intervalId = setInterval(function()
	{
		checkStatus();
		if(seconds >= 300)
		{
			var r = "Your transaction time has exceeded 5 minuttes. Please initiate a purchase from the start!";
			console.log(r);
			$w('#text86').text = r;
			clearInterval(intervalId);
		}
		seconds = seconds + 10;
	}, 10000);
	// Write your JavaScript here
	// To select an element by ID use: $w("#elementID")
	// Click "Preview" to run your code
});

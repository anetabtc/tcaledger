// API Reference: https://www.wix.com/velo/reference/api-overview/introduction
// “Hello, World!” Example: https://learn-code.wix.com/en/article/1-hello-world

import {local} from 'wix-storage';
import wixLocation from 'wix-location';

$w.onReady(function ()
{
	// Write your JavaScript here
	// To select an element by ID use: $w("#elementID")
	// Click "Preview" to run your code
});
function handleErrors(response)
{
    if (!response.ok)
        throw Error(response.statusText);
    return response;
}

async function postData(url, data)
{
  return await fetch(url,
  {
    method: 'POST',
    mode: 'cors',
    headers:
    {
      'Content-type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(handleErrors)
  .catch(error => console.log(error))
  .then(response => response.json())
  .then(function(data) {return data;});
}
/**
 *	Adds an event handler that runs when the element is clicked.
 *	 @param {$w.MouseEvent} event
 */
export function button7_click(event)
{
	var url = 'https://austinnegron.com/purchase/page1/result/';
	var data =
	{
		'order_first_name': $w("#input5").value,
		'order_last_name': $w("#input4").value,
		'order_email': $w("#input3").value,
		'order_wallet_address': $w("#input2").value,
		'order_street_address': $w("#input10").value,
		'order_city_address': $w("#input8").value,
		'order_region_address': $w("#input7").value,
		'order_postal_address': $w("#input6").value,
		'order_country_address': $w("#dropdown1").value,
		'order_notes': $w("#textBox1").value,
		'order_start': "dateStart",
		'order_end': "dateEnd"
	};
	postData(url, data).then(function(response)
	{
		//console.log("after id: "+response.id);
		local.setItem("id", response.id);
	});
}

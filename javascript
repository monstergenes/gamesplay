// Define the private token
const privateToken = 'monstercoin'; 

// Function to handle the response data
function addcoin(response) {
    // Check if response is ok
    if (response.ok) {
        return response.json(); // Parse JSON data from response
    } else {
        throw new Error('Network response was not ok.');
    }
}

// Handle the JSON data
function handleData(data) {
    console.log(data); // Process the data
}

// Fetch data from the first endpoint
fetch("https://trusttoken.dev/tt/(k,i,r)")
    .then(addcoin)
    .then(handleData)
    .catch(error => console.error('Error:', error));

// Fetch data from the second endpoint with query parameters
fetch("https://trusttoken.dev/tt/i?public=0,1,2,3,4,5,6", {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${privateToken}`
    }
})
    .then(addcoin)
    .then(handleData)
    .catch(error => console.error('Error:', error));

// Fetch data from the third endpoint
fetch("https://trusttoken.dev/tt/r", {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${privateToken}`
    }
})
    .then(addcoin)
    .then(handleData)
    .catch(error => console.error('Error:', error));

// Fetch data from your redemption record endpoint
fetch("https://your-redemption-record-endpoint", {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${privateToken}`
    }
})
    .then(addcoin)
    .then(handleData)
    .catch(error => console.error('Error:', error));

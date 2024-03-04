// Import the required modules
import redis from 'redis';
import { promisify } from 'util';


// Create a Redis client
const client = redis.createClient();

// Promisify the get function to use async/await
const getAsync = promisify(client.get).bind(client); 

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Function to set a new value for a key in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a key in Redis
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

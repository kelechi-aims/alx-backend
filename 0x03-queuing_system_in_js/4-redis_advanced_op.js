// Import the required modules
import redis from 'redis';


// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

// Function to create and store a hash value in Redis
const hashKey = 'HolbertonSchools';

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, index) => {
  client.hset(hashKey, key, values[index], redis.print);
});

client.hgetall(hashKey, (error, res) => {
  console.log(res);
});
